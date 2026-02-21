import json

import requests
from requests.exceptions import HTTPError
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from logger import get_logger

logger = get_logger(__name__)

_BASE_URL = "https://api.cloudzero.com"
_MAX_BODY_BYTES = 4_500_000  # conservative limit below the 5 MB API cap


def _is_retryable(exc: BaseException) -> bool:
    """Retry on 429 or 5xx; raise immediately on other HTTP errors."""
    if isinstance(exc, HTTPError):
        status = exc.response.status_code
        return status == 429 or status >= 500
    return False


@retry(
    retry=retry_if_exception(_is_retryable),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    stop=stop_after_attempt(3),
    reraise=True,
)
def post_billing_drop(
    api_key: str,
    connection_id: str,
    billing_month: str,
    data: list[dict],
) -> dict:
    """POST a billing drop to the CloudZero AnyCost Stream endpoint.

    Args:
        api_key: CloudZero API key (no Bearer prefix).
        connection_id: AnyCost Stream connection ID.
        billing_month: ISO-8601 month string, e.g. "2025-01-01T00:00:00Z".
        data: List of CBF row dicts.

    Returns:
        Parsed JSON response body.

    Raises:
        ValueError: If the payload exceeds the size guard.
        HTTPError: On non-retryable 4xx, or after exhausting retries on 429/5xx.
    """
    payload = {
        "month": billing_month,
        "operation": "replace_drop",
        "data": data,
    }

    serialised = json.dumps(payload)
    if len(serialised.encode("utf-8")) > _MAX_BODY_BYTES:
        raise ValueError(
            f"Payload size {len(serialised)} bytes exceeds limit of {_MAX_BODY_BYTES} bytes"
        )

    url = f"{_BASE_URL}/v2/connections/billing/anycost/{connection_id}/billing_drops"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
    }

    logger.info(
        "posting billing drop",
        extra={
            "connection_id": connection_id,
            "billing_month": billing_month,
            "row_count": len(data),
        },
    )

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    logger.info(
        "billing drop accepted",
        extra={"status_code": response.status_code, "billing_month": billing_month},
    )
    return response.json() if response.content else {}
