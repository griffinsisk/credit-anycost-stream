import calendar
import os
import re
from decimal import Decimal

import boto3
from requests.exceptions import HTTPError

import cloudzero_client
import csv_parser
from logger import get_logger

logger = get_logger(__name__)

_FILENAME_RE = re.compile(r"credits-(\d{4})-(\d{2})\.csv$")


def _last_second_of_month(year: int, month: int) -> str:
    last_day = calendar.monthrange(year, month)[1]
    return f"{year:04d}-{month:02d}-{last_day:02d}T23:59:59Z"


def _build_cbf_rows(credits: list[dict], usage_start: str, usage_end: str) -> list[dict]:
    rows = []
    for credit in credits:
        amount = credit["amount_usd"]
        negated = str(-amount)
        rows.append(
            {
                "lineitem/type": "MAP Credit (Monthly)",
                "lineitem/description": "Monthly MAP Credit",
                "time/usage_start": usage_start,
                "time/usage_end": usage_end,
                "resource/account": credit["account_id"],
                "resource/service": "AWSCredits",
                "cost/cost": negated,
            }
        )
    return rows


def lambda_handler(event: dict, context) -> dict:
    api_key = os.environ["CLOUDZERO_API_KEY"]
    connection_id = os.environ["CLOUDZERO_CONNECTION_ID"]

    try:
        record = event["Records"][0]["s3"]
        bucket = record["bucket"]["name"]
        key = record["object"]["key"]
    except (KeyError, IndexError) as exc:
        logger.error("malformed S3 event", extra={"error": str(exc)})
        raise ValueError(f"Malformed S3 event: {exc}") from exc

    filename = key.split("/")[-1]
    match = _FILENAME_RE.search(filename)
    if not match:
        logger.error(
            "filename does not match expected pattern credits-YYYY-MM.csv",
            extra={"key": key},
        )
        raise ValueError(f"Filename '{filename}' does not match pattern credits-YYYY-MM.csv")

    year = int(match.group(1))
    month = int(match.group(2))
    billing_month = f"{year:04d}-{month:02d}-01T00:00:00Z"
    usage_start = billing_month
    usage_end = _last_second_of_month(year, month)

    logger.info("processing credits file", extra={"bucket": bucket, "key": key, "billing_month": billing_month})

    try:
        s3 = boto3.client("s3")
        obj = s3.get_object(Bucket=bucket, Key=key)
        csv_text = obj["Body"].read().decode("utf-8")
    except Exception as exc:
        logger.error("failed to download file from S3", extra={"bucket": bucket, "key": key, "error": str(exc)})
        raise

    try:
        credits = csv_parser.parse_credits_csv(csv_text)
    except Exception as exc:
        logger.error("CSV parsing failed", extra={"error": str(exc)})
        raise

    if not credits:
        logger.error("no valid rows parsed from CSV", extra={"key": key})
        raise ValueError(f"No valid rows parsed from '{key}'")

    cbf_rows = _build_cbf_rows(credits, usage_start, usage_end)

    total_credit = sum(c["amount_usd"] for c in credits)
    unique_accounts = [c["account_id"] for c in credits]

    try:
        cloudzero_client.post_billing_drop(api_key, connection_id, billing_month, cbf_rows)
    except (ValueError, HTTPError) as exc:
        logger.error("billing drop failed", extra={"error": str(exc), "billing_month": billing_month})
        raise
    except Exception as exc:
        logger.error("unexpected error posting billing drop", extra={"error": str(exc)})
        raise

    logger.info(
        "credits pipeline complete",
        extra={
            "file": key,
            "billing_month": billing_month,
            "row_count": len(credits),
            "unique_accounts": len(unique_accounts),
            "total_credit_usd": str(total_credit),
        },
    )

    return {
        "statusCode": 200,
        "billing_month": billing_month,
        "row_count": len(credits),
        "unique_accounts": len(unique_accounts),
        "total_credit_usd": str(total_credit),
    }
