import logging
from decimal import Decimal

import pytest

from csv_parser import parse_credits_csv

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_CSV = """\
062951470133,$0.00
073933415963,"$6,407.96"
233466153464,"$23,436.83"
235494797904,"$1,828.24"
284954390955,"$32,728.09"
331238891350,$453.84
339712813083,"$32,258.79"
400210543042,$412.07
497723851829,"$116,319.27"
546885038385,"$1,000.54"
568064661016,"$3,233.09"
585876524959,"$13,154.71"
605134457544,"$16,883.68"
654654353366,"$25,087.88"
767397766098,"$4,812.64"
785080043467,"$6,743.73"
054736553085,"$11,845.35"
197545325174,"$22,393.16"
332999210940,$132.10
832337494075,"$2,016.40"
869578675382,$624.05
992382782732,"$11,124.29"
664220444271,"$3,938.27"
054736553085,"$11,845.35"
"""


# ---------------------------------------------------------------------------
# Basic parsing
# ---------------------------------------------------------------------------

def test_parse_normal_row():
    result = parse_credits_csv("331238891350,$453.84\n")
    assert result == [{"account_id": "331238891350", "amount_usd": Decimal("453.84")}]


def test_parse_amount_with_commas():
    result = parse_credits_csv('073933415963,"$6,407.96"\n')
    assert result[0]["amount_usd"] == Decimal("6407.96")


def test_parse_large_amount_with_commas():
    result = parse_credits_csv('497723851829,"$116,319.27"\n')
    assert result[0]["amount_usd"] == Decimal("116319.27")


def test_parse_zero_amount():
    result = parse_credits_csv("062951470133,$0.00\n")
    assert result[0]["amount_usd"] == Decimal("0.00")


# ---------------------------------------------------------------------------
# Leading-zero account IDs
# ---------------------------------------------------------------------------

def test_leading_zero_account_preserved():
    result = parse_credits_csv('054736553085,"$11,845.35"\n')
    assert result[0]["account_id"] == "054736553085"


def test_short_account_padded_with_zeros():
    # e.g. an 11-digit id should be zero-padded to 12
    result = parse_credits_csv("12345678901,$10.00\n")
    assert result[0]["account_id"] == "012345678901"


# ---------------------------------------------------------------------------
# Duplicate handling
# ---------------------------------------------------------------------------

def test_duplicate_keeps_first(caplog):
    csv_text = '054736553085,"$11,845.35"\n054736553085,"$11,845.35"\n'
    with caplog.at_level(logging.WARNING, logger="csv_parser"):
        result = parse_credits_csv(csv_text)
    assert len(result) == 1
    assert result[0]["account_id"] == "054736553085"
    assert any("duplicate" in r.message.lower() for r in caplog.records)


def test_duplicate_logs_both_raw_values(caplog):
    csv_text = "123456789012,$100.00\n123456789012,$200.00\n"
    with caplog.at_level(logging.WARNING, logger="csv_parser"):
        parse_credits_csv(csv_text)
    warning = next(r for r in caplog.records if "duplicate" in r.message.lower())
    assert "123456789012" in str(warning.__dict__)


# ---------------------------------------------------------------------------
# Bad row handling — warns and continues
# ---------------------------------------------------------------------------

def test_bad_amount_skipped(caplog):
    csv_text = "123456789012,$0.00\n234567890123,NOT_A_NUMBER\n345678901234,$5.00\n"
    with caplog.at_level(logging.WARNING, logger="csv_parser"):
        result = parse_credits_csv(csv_text)
    assert len(result) == 2
    ids = [r["account_id"] for r in result]
    assert "234567890123" not in ids


def test_bad_account_id_skipped(caplog):
    csv_text = "BADACCOUNT,$10.00\n123456789012,$5.00\n"
    with caplog.at_level(logging.WARNING, logger="csv_parser"):
        result = parse_credits_csv(csv_text)
    assert len(result) == 1
    assert result[0]["account_id"] == "123456789012"


def test_short_row_skipped(caplog):
    csv_text = "123456789012\n234567890123,$5.00\n"
    with caplog.at_level(logging.WARNING, logger="csv_parser"):
        result = parse_credits_csv(csv_text)
    assert len(result) == 1


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

def test_empty_input_returns_empty_list():
    assert parse_credits_csv("") == []


def test_full_sample_returns_23_unique_accounts():
    result = parse_credits_csv(SAMPLE_CSV)
    assert len(result) == 23


def test_full_sample_account_ids_are_strings():
    result = parse_credits_csv(SAMPLE_CSV)
    for row in result:
        assert isinstance(row["account_id"], str)
        assert len(row["account_id"]) == 12


def test_full_sample_amounts_are_decimal():
    result = parse_credits_csv(SAMPLE_CSV)
    for row in result:
        assert isinstance(row["amount_usd"], Decimal)


# ---------------------------------------------------------------------------
# Negative amount handling
# ---------------------------------------------------------------------------

def test_negative_amount_with_dollar_sign():
    result = parse_credits_csv("123456789012,-$100.00\n")
    assert result[0]["amount_usd"] == Decimal("100.00")


def test_negative_amount_without_dollar_sign():
    result = parse_credits_csv("123456789012,-100.00\n")
    assert result[0]["amount_usd"] == Decimal("100.00")
