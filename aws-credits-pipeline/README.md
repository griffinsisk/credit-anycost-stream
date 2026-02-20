# AWS MAP Credits Pipeline

Automates the monthly push of AWS credits into CloudZero. Drop a credits CSV into S3 — Lambda parses it and posts the data to CloudZero's AnyCost Stream billing drop API automatically.

## How it works

```
credits-YYYY-MM.csv  →  S3 bucket  →  Lambda  →  CloudZero AnyCost Stream
                                          ↓
                                    CloudWatch Logs
```

## Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) configured with credentials for your target account
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Python 3.12+
- A CloudZero account with an AnyCost Stream billing connection

---

## Step 1 — Get your CloudZero API key

1. Log into CloudZero
2. Go to **Settings → API Keys**
3. Create a new key (or use an existing one)
4. Copy the key value — you'll use it as `CLOUDZERO_API_KEY`

> The API key is used directly in the `Authorization` header with no `Bearer` prefix.

---

## Step 2 — Get your AnyCost Stream connection ID

1. In CloudZero, go to **Settings → Billing Connections**
2. Find your **AnyCost Stream** connection (create one if it doesn't exist)
3. Copy the connection ID from the connection's detail page — you'll use it as `CLOUDZERO_CONNECTION_ID`

---

## Step 3 — Set environment variables

```bash
export CLOUDZERO_API_KEY=<paste your API key here>
export CLOUDZERO_CONNECTION_ID=<paste your connection ID here>
```

These are read at deploy time and passed securely to Lambda as environment variables. They are never hardcoded in any file.

---

## Step 4 — Build and deploy

```bash
# Install SAM CLI (macOS)
brew install aws-sam-cli

# Build the Lambda package
sam build

# First-time deploy — walks you through region, S3 artifact bucket, stack name
sam deploy --guided

# Subsequent deploys
sam deploy
```

During `sam deploy --guided` you will be prompted to confirm the parameter overrides — SAM reads `CLOUDZERO_API_KEY` and `CLOUDZERO_CONNECTION_ID` from your shell environment and passes them in.

The deploy creates:
- An S3 bucket named `aws-credits-pipeline-{AccountId}-{Region}`
- A Lambda function named `aws-credits-processor`
- An IAM role scoped to CloudWatch writes and `s3:GetObject` on credits files only

---

## Step 5 — Upload a credits file

The filename must match the pattern `credits-YYYY-MM.csv`. The billing month is parsed from the filename — not the upload timestamp.

```bash
aws s3 cp credits-2025-01.csv s3://aws-credits-pipeline-<AccountId>-<Region>/credits-2025-01.csv
```

The Lambda triggers automatically on upload.

---

## Credits CSV format

No header row. Two columns:

| Column | Description | Example |
|---|---|---|
| 0 | AWS Account ID (12 digits, leading zeros matter) | `054736553085` |
| 1 | USD credit amount | `$0.00`, `"$6,407.96"`, `"$116,319.27"` |

If an account ID appears more than once, the first row is kept and subsequent duplicates are logged as warnings and skipped.

---

## Verifying the run

**CloudWatch Logs:**
```
/aws/lambda/aws-credits-processor
```
A successful run emits a structured JSON summary log with fields: `file`, `billing_month`, `row_count`, `unique_accounts`, `total_credit_usd`.

**CloudZero:**
After a successful run, credits appear in the AnyCost Stream connection for the uploaded billing month.

**Re-uploading the same file is safe.** The pipeline uses `replace_drop`, which replaces all data for that month rather than appending — no double-crediting.

---

## Running tests locally

```bash
pip install -r src/requirements.txt -r tests/requirements.txt
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Local smoke test (no deploy needed)

```bash
sam build
sam local invoke CreditsProcessorFunction -e events/s3_put_event.json \
  --env-vars '{"CreditsProcessorFunction": {"CLOUDZERO_API_KEY": "test", "CLOUDZERO_CONNECTION_ID": "test"}}'
```

---

## Project structure

```
aws-credits-pipeline/
├── src/
│   ├── handler.py             # Lambda entry point
│   ├── csv_parser.py          # CSV parsing
│   ├── cloudzero_client.py    # CloudZero API client
│   ├── logger.py              # Structured JSON logging
│   └── requirements.txt
├── tests/
│   ├── test_csv_parser.py
│   ├── test_cloudzero_client.py
│   ├── test_handler.py
│   └── requirements.txt
├── docs/
│   ├── architecture.md
│   ├── changelog.md
│   └── project-status.md
├── events/
│   └── s3_put_event.json      # Sample event for sam local invoke
├── template.yaml              # SAM template
├── samconfig.toml             # SAM deploy config
└── .env.example               # Reference for required env vars
```
