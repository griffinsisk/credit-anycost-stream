import csv
import io
import re
from decimal import Decimal, InvalidOperation

from logger import get_logger

logger = get_logger(__name__)

_ACCOUNT_RE = re.compile(r"^\d{12}$")


def parse_credits_csv(csv_text: str) -> list[dict]:
    """Parse a headerless credits CSV.

    Each row: <account_id>,<amount>
    - Column 0: 12-digit AWS account ID (leading zeros preserved)
    - Column 1: USD amount like $0.00, "$6,407.96", "$116,319.27"

    Returns a list of {"account_id": str, "amount_usd": Decimal}.
    Duplicate account IDs: keeps the first occurrence, logs WARNING for subsequent.
    Rows with invalid data: logs WARNING and skips; processing continues.
    """
    rows = []
    seen: dict[str, str] = {}  # account_id -> raw amount of first occurrence

    reader = csv.reader(io.StringIO(csv_text))
    for line_num, row in enumerate(reader, start=1):
        if len(row) < 2:
            logger.warning("skipping short row", extra={"line": line_num, "row": row})
            continue

        raw_account = row[0].strip()
        raw_amount = row[1].strip()

        # Normalise account ID: pad to 12 digits
        account_id = raw_account.zfill(12)

        if not _ACCOUNT_RE.match(account_id):
            logger.warning(
                "skipping row with invalid account ID",
                extra={"line": line_num, "raw_account": raw_account},
            )
            continue

        # Clean amount: strip $, commas, whitespace
        clean_amount = raw_amount.replace("$", "").replace(",", "").strip()
        try:
            amount_usd = abs(Decimal(clean_amount))
        except InvalidOperation:
            logger.warning(
                "skipping row with invalid amount",
                extra={"line": line_num, "account_id": account_id, "raw_amount": raw_amount},
            )
            continue

        # Duplicate check
        if account_id in seen:
            logger.warning(
                "duplicate account ID — keeping first occurrence, skipping this row",
                extra={
                    "account_id": account_id,
                    "line": line_num,
                    "first_raw_amount": seen[account_id],
                    "duplicate_raw_amount": raw_amount,
                },
            )
            continue

        seen[account_id] = raw_amount
        rows.append({"account_id": account_id, "amount_usd": amount_usd})

    return rows
