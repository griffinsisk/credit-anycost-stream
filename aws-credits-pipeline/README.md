# AWS MAP Credits Pipeline

Automates the monthly push of AWS credits into CloudZero. Drop a credits CSV into S3 — Lambda parses it and posts the data to CloudZero's AnyCost Stream billing drop API automatically.

## How it works

```
credits-YYYY-MM.csv  →  S3 bucket  →  Lambda  →  CloudZero AnyCost Stream
                                          ↓
                                    CloudWatch Logs
```

---

## Before you start — install the tools

You need two CLI tools installed. Run these commands to check if they're already installed:

```bash
aws --version
sam --version
```

If either is missing:

```bash
# Install AWS CLI (macOS)
brew install awscli

# Install SAM CLI (macOS)
brew install aws-sam-cli
```

You also need your AWS CLI configured with credentials for the account you're deploying into. If you haven't done this yet:

```bash
aws configure
```

It will prompt you for your AWS Access Key ID, Secret Access Key, default region (e.g. `us-east-1`), and output format (just press Enter for default).

---

## Step 1 — Set your credentials as environment variables

You need two values from CloudZero. Open a terminal and run both export commands with your real values pasted in:

```bash
export CLOUDZERO_API_KEY=paste_your_api_key_here
export CLOUDZERO_CONNECTION_ID=paste_your_connection_id_here
```

> **Important:** These exports only last for your current terminal session. If you close the terminal and reopen it, you'll need to run these again before deploying.

To confirm they're set:

```bash
echo $CLOUDZERO_API_KEY
echo $CLOUDZERO_CONNECTION_ID
```

Both should print your values (not blank).

---

## Step 2 — Build the Lambda package

From inside the `aws-credits-pipeline/` folder, run:

```bash
sam build
```

This packages your Python code and dependencies for Lambda. You should see `Build Succeeded` at the end. If you see errors, make sure you're in the right folder.

---

## Step 3 — Deploy to AWS

### First time only — run the guided deploy

```bash
sam deploy --guided
```

SAM will walk you through a series of prompts. Here's what to enter:

| Prompt | What to enter |
|---|---|
| Stack Name | `aws-credits-pipeline` (or press Enter to accept) |
| AWS Region | Your target region, e.g. `us-east-1` |
| Parameter CloudZeroApiKey | Press Enter — SAM reads it from your env var |
| Parameter CloudZeroConnectionId | Press Enter — SAM reads it from your env var |
| Confirm changes before deploy | `y` |
| Allow SAM CLI IAM role creation | `y` |
| Save arguments to configuration file | `y` |
| SAM configuration file | Press Enter to accept `samconfig.toml` |
| SAM configuration environment | Press Enter to accept `default` |

After the prompts, SAM will show you a changeset (what it's about to create) and ask:

```
Deploy this changeset? [y/N]
```

Enter `y` to proceed.

### What gets created

- An S3 bucket named `aws-credits-pipeline-<AccountId>-<Region>`
- A Lambda function named `aws-credits-processor`
- An IAM role with least-privilege permissions

### Subsequent deploys

After the first deploy, just run:

```bash
sam deploy
```

---

## Step 4 — Upload a credits file

The filename must follow the pattern `credits-YYYY-MM.csv`. The billing month is read from the filename, not the upload date.

Replace `<AccountId>` and `<Region>` with your values (you can find the bucket name in the deploy output):

```bash
aws s3 cp credits-2025-01.csv s3://aws-credits-pipeline-<AccountId>-<Region>/credits-2025-01.csv
```

The Lambda triggers automatically within a few seconds of the upload.

---

## Step 5 — Verify it worked

### Check CloudWatch Logs

1. Open the [AWS Console](https://console.aws.amazon.com)
2. Go to **CloudWatch → Log groups**
3. Find `/aws/lambda/aws-credits-processor`
4. Open the most recent log stream
5. Look for a structured JSON summary log with fields like `billing_month`, `row_count`, `total_credit_usd`

### Check CloudZero

Credits should appear in your AnyCost Stream connection for the uploaded billing month within a few minutes.

### Re-uploading the same file is safe

The pipeline uses `replace_drop` — re-uploading the same month replaces the existing data rather than adding duplicates.

---

## Credits CSV format

No header row. Two columns:

| Column | Description | Example |
|---|---|---|
| 0 | AWS Account ID (12 digits, leading zeros matter) | `054736553085` |
| 1 | USD credit amount | `$0.00`, `"$6,407.96"`, `"$116,319.27"` |

If an account ID appears more than once, the first row is used and duplicates are skipped with a warning in the logs.

---

## Running tests locally

```bash
pip install -r src/requirements.txt -r tests/requirements.txt
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Local smoke test (optional — no deploy needed)

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
