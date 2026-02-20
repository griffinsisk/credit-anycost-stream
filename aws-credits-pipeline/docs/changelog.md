# Changelog

## [MVP] — 2026-02-20

### Added
- `src/csv_parser.py` — Parses headerless credits CSV; handles `$`/comma amounts, leading-zero
  account IDs, duplicates (keep first, warn), bad rows (warn and skip).
- `src/cloudzero_client.py` — Posts billing drop to CloudZero AnyCost Stream; retries on 429/5xx
  (tenacity, 3 attempts, exponential backoff 2–30s); raises immediately on 4xx; 4.5 MB size guard.
- `src/handler.py` — Lambda entry point; extracts billing month from filename
  (`credits-YYYY-MM.csv`); builds CBF rows with negated amounts; logs structured JSON summary.
- `src/logger.py` — JSON logger factory via `python-json-logger`.
- `template.yaml` — SAM template: S3 bucket, Lambda function, IAM role (least privilege).
- `samconfig.toml` — SAM deploy config; reads API key + connection ID from shell env vars.
- `events/s3_put_event.json` — Sample S3 event for `sam local invoke`.
- `tests/test_csv_parser.py` — 13 tests; 90%+ coverage of csv_parser.
- `tests/test_cloudzero_client.py` — 11 tests; covers happy path, auth header, retry, no-retry, size guard.
- `tests/test_handler.py` — 8 tests; covers billing month extraction, error cases, summary log.
