import os
import sys
from unittest.mock import patch, MagicMock

import pytest

# Ensure scripts/ is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from backfill import generate_months, run_backfill


# ---------------------------------------------------------------------------
# Month range generation
# ---------------------------------------------------------------------------

def test_generate_single_month():
    assert generate_months("2025-01", "2025-01") == ["2025-01"]


def test_generate_full_year():
    months = generate_months("2025-01", "2025-12")
    assert len(months) == 12
    assert months[0] == "2025-01"
    assert months[-1] == "2025-12"


def test_generate_13_months_cross_year():
    months = generate_months("2025-01", "2026-01")
    assert len(months) == 13
    assert months[0] == "2025-01"
    assert months[-1] == "2026-01"


def test_generate_mid_year_to_mid_year():
    months = generate_months("2025-06", "2025-09")
    assert months == ["2025-06", "2025-07", "2025-08", "2025-09"]


# ---------------------------------------------------------------------------
# Dry run — no API calls
# ---------------------------------------------------------------------------

def test_dry_run_does_not_call_api(tmp_path):
    csv_file = tmp_path / "credits.csv"
    csv_file.write_text("123456789012,$100.00\n")

    with patch("backfill.cloudzero_client.post_billing_drop") as mock_post:
        results = run_backfill(
            csv_path=str(csv_file),
            start_month="2025-01",
            end_month="2025-03",
            dry_run=True,
        )

    mock_post.assert_not_called()
    assert len(results) == 3
    assert all(r["status"] == "dry_run" for r in results)


# ---------------------------------------------------------------------------
# Failure and continue
# ---------------------------------------------------------------------------

def test_continues_on_failure(tmp_path, monkeypatch):
    csv_file = tmp_path / "credits.csv"
    csv_file.write_text("123456789012,$100.00\n")

    monkeypatch.setenv("CLOUDZERO_API_KEY", "test-key")
    monkeypatch.setenv("CLOUDZERO_CONNECTION_ID", "test-conn")

    call_count = 0

    def mock_post(api_key, connection_id, billing_month, data):
        nonlocal call_count
        call_count += 1
        if call_count == 2:
            raise Exception("API error on month 2")
        return {}

    with patch("backfill.cloudzero_client.post_billing_drop", side_effect=mock_post), \
         patch("backfill.time.sleep"):
        results = run_backfill(
            csv_path=str(csv_file),
            start_month="2025-01",
            end_month="2025-03",
            dry_run=False,
            delay=0,
        )

    assert len(results) == 3
    assert results[0]["status"] == "ok"
    assert results[1]["status"] == "failed"
    assert results[2]["status"] == "ok"
