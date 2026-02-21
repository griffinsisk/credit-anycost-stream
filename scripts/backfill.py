#!/usr/bin/env python3
"""Backfill historical credits to CloudZero AnyCost Stream.

One-time CLI script that posts the same credits CSV for multiple billing months.
Use this to load historical data before the automated S3 pipeline takes over.

Usage:
    python scripts/backfill.py \
        --csv credits-example.csv \
        --start-month 2025-01 \
        --end-month 2026-01

    # Validate without posting:
    python scripts/backfill.py \
        --csv credits-example.csv \
        --start-month 2025-01 \
        --end-month 2026-01 \
        --dry-run

Requires CLOUDZERO_API_KEY and CLOUDZERO_CONNECTION_ID environment variables.
"""

import argparse
import os
import sys
import time
from datetime import date

# Allow imports from src/ when run from repo root or scripts/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import cloudzero_client
import csv_parser
from handler import _build_cbf_rows, _last_second_of_month


def generate_months(start: str, end: str) -> list[str]:
    """Generate YYYY-MM strings from start to end inclusive."""
    sy, sm = (int(x) for x in start.split("-"))
    ey, em = (int(x) for x in end.split("-"))

    months = []
    y, m = sy, sm
    while (y, m) <= (ey, em):
        months.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
    return months


def run_backfill(
    csv_path: str,
    start_month: str,
    end_month: str,
    dry_run: bool = False,
    delay: float = 2.0,
) -> list[dict]:
    """Run the backfill, returning a list of result dicts per month."""
    api_key = os.environ.get("CLOUDZERO_API_KEY", "")
    connection_id = os.environ.get("CLOUDZERO_CONNECTION_ID", "")

    if not dry_run:
        if not api_key:
            print("ERROR: CLOUDZERO_API_KEY environment variable not set")
            sys.exit(1)
        if not connection_id:
            print("ERROR: CLOUDZERO_CONNECTION_ID environment variable not set")
            sys.exit(1)

    with open(csv_path, "r") as f:
        csv_text = f.read()

    credits = csv_parser.parse_credits_csv(csv_text)
    if not credits:
        print(f"ERROR: No valid rows parsed from {csv_path}")
        sys.exit(1)

    total_credit = sum(c["amount_usd"] for c in credits)
    months = generate_months(start_month, end_month)

    print(f"CSV: {csv_path} — {len(credits)} accounts, ${total_credit:,.2f}")
    print(f"Months: {months[0]} through {months[-1]} ({len(months)} months)")
    if dry_run:
        print("MODE: dry-run (no API calls)")
    print()

    results = []
    failures = []

    for i, month_str in enumerate(months, start=1):
        year, month = (int(x) for x in month_str.split("-"))
        billing_month = f"{year:04d}-{month:02d}-01T00:00:00Z"
        usage_start = billing_month
        usage_end = _last_second_of_month(year, month)

        cbf_rows = _build_cbf_rows(credits, usage_start, usage_end)

        if dry_run:
            print(f"[{i}/{len(months)}] {month_str} — {len(credits)} accounts, ${total_credit:,.2f} — DRY RUN")
            results.append({"month": month_str, "status": "dry_run"})
            continue

        try:
            cloudzero_client.post_billing_drop(api_key, connection_id, billing_month, cbf_rows)
            print(f"[{i}/{len(months)}] {month_str} — {len(credits)} accounts, ${total_credit:,.2f} — OK")
            results.append({"month": month_str, "status": "ok"})
        except Exception as exc:
            print(f"[{i}/{len(months)}] {month_str} — FAILED: {exc}")
            results.append({"month": month_str, "status": "failed", "error": str(exc)})
            failures.append(month_str)

        if i < len(months):
            time.sleep(delay)

    print()
    if failures:
        print(f"DONE — {len(failures)} failure(s): {', '.join(failures)}")
    elif dry_run:
        print(f"DRY RUN COMPLETE — {len(months)} months validated")
    else:
        print(f"DONE — {len(months)} months posted successfully")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Backfill historical credits to CloudZero AnyCost Stream"
    )
    parser.add_argument("--csv", required=True, help="Path to credits CSV file")
    parser.add_argument("--start-month", required=True, help="First billing month (YYYY-MM)")
    parser.add_argument("--end-month", required=True, help="Last billing month (YYYY-MM)")
    parser.add_argument("--dry-run", action="store_true", help="Validate without posting to API")
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between API calls (default: 2)")

    args = parser.parse_args()
    run_backfill(args.csv, args.start_month, args.end_month, args.dry_run, args.delay)


if __name__ == "__main__":
    main()
