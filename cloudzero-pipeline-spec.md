# CloudZero AWS Credits Pipeline — Spec Doc
*PRD + Engineering Design Doc | Last updated: February 2026*

---

## Mission

Automate the monthly redistribution of AWS credits for Kiteworks into CloudZero, replacing a manual process with a reliable, low-maintenance pipeline that runs on file upload.

---

## Target User

**Griffin Sisk / CloudZero internal team.** This is internal tooling — the team builds and maintains it. Kiteworks is the downstream beneficiary whose credits are being tracked, but they do not interact with the pipeline directly.

---

## Problem Statement

AWS credits for Kiteworks arrive monthly and need to be parsed and pushed into CloudZero for accounting. Doing this manually is error-prone and time-consuming. This pipeline fully automates that flow from file drop to CloudZero ingestion.

---

## Milestones

### MVP — Core Pipeline
The smallest useful, working thing:
- S3 file drop triggers Lambda automatically
- Lambda parses credits file by AWS account ID
- Parsed credits are pushed to CloudZero via API
- Success/failure logged to CloudWatch

### V1 — Validation & Confirmation
- Confirm allocations landed correctly in CloudZero dashboards
- Basic output report or log summary per run (e.g., number of accounts processed, total credit value pushed)
- Confirm process with Kiteworks team

### V2 — Robustness & Maintainability
- Handle structural changes in the credits file format gracefully (schema validation, versioning)
- Replay / retry mechanism for failed API calls
- Idempotency: re-uploading the same file doesn't double-credit

### Later
- Error alerting (Slack or email via SNS) on pipeline failure
- Monitoring dashboard for pipeline run history

### Not in Scope
- Frontend UI of any kind
- Real-time or streaming credit processing (monthly batch only)
- Multi-tenant support (scoped to Kiteworks only for now)

---

## Product Requirements

### User Personas

**Griffin / CloudZero Ops** — Uploads the monthly credits file to S3 and needs confidence it will be processed correctly and automatically, with no manual follow-up required.

**Kiteworks Accounting** — Downstream consumer. Does not interact with the pipeline. They simply see accurate credits reflected in CloudZero each month.

### Operational Workflow (UX Flow)

```
1. AWS credits file is generated monthly (CSV or similar format)
2. Griffin (or an automated process) uploads the file to a designated S3 bucket
3. S3 event triggers Lambda automatically — no manual invocation needed
4. Lambda reads and parses the file, mapping credits to account IDs
5. Lambda calls CloudZero API to push each account's credit allocation
6. Results are logged to CloudWatch (success / partial failure / full failure)
7. Griffin spot-checks allocations in CloudZero dashboard to confirm (V1)
```

### Edge Cases to Handle
- Malformed or missing file — Lambda should fail gracefully with a clear error log
- Account ID in file not found in CloudZero — log and skip, do not crash pipeline
- API rate limiting or timeout — implement retry with exponential backoff
- Duplicate file upload — (V2) idempotency check to prevent double-crediting

### Success Criteria
- Credits file uploaded to S3 → credits visible in CloudZero within 5 minutes, no manual steps
- Zero silent failures: every run produces a CloudWatch log entry
- All account IDs in the file are processed or explicitly skipped with a logged reason

---

## Engineering Design

### Tech Stack

| Layer | Decision | Notes |
|---|---|---|
| Language | Python 3.12 | Best ecosystem for AWS + data parsing |
| Compute | AWS Lambda | Event-driven, serverless, zero infra management |
| Trigger | S3 Event Notification | Fires on file upload (ObjectCreated event) |
| Storage | Amazon S3 | Receives the monthly credits file |
| IaC / Deployment | AWS SAM (CloudFormation superset) | SAM simplifies Lambda + S3 trigger config significantly vs. raw CloudFormation; synthesizes to a CloudFormation stack you can review and deploy via `sam deploy` |
| Logging | Amazon CloudWatch Logs | Lambda logs automatically; add structured log statements |
| API Integration | CloudZero REST API | See API docs for endpoint details |
| Error Handling | Python try/except + CloudWatch | Structured error logging; retry logic for API calls |

> **Note on CloudFormation vs. SAM:** Both are valid. AWS SAM is a superset — it generates a CloudFormation stack but requires far less boilerplate for Lambda functions and S3 triggers. Recommended to use SAM and treat the resulting CloudFormation stack as the deployment artifact.

### High-Level Architecture

```
┌─────────────────┐     S3 ObjectCreated     ┌──────────────────┐
│   S3 Bucket     │ ─────────────────────── ▶ │  AWS Lambda      │
│  (credits file) │                           │  (Python 3.12)   │
└─────────────────┘                           └────────┬─────────┘
                                                       │
                              ┌────────────────────────┤
                              │                        │
                              ▼                        ▼
                    ┌──────────────────┐   ┌───────────────────┐
                    │  CloudZero API   │   │  CloudWatch Logs  │
                    │  (POST credits)  │   │  (run results)    │
                    └──────────────────┘   └───────────────────┘
```

### Lambda Function Design

**Trigger:** S3 ObjectCreated event on the designated bucket/prefix

**Steps:**
1. Extract bucket name and object key from the S3 event payload
2. Download and read the credits file from S3 using `boto3`
3. Parse the file — map each row to `{ account_id, credit_amount, ... }`
4. For each account: call CloudZero API to POST the credit allocation
5. Collect results (success / skipped / failed per account)
6. Log structured summary to CloudWatch
7. Raise exception if >0 accounts failed API call (triggers Lambda failure state)

**Retry Strategy:** Use `tenacity` or manual retry with exponential backoff for CloudZero API calls (handle 429 / 5xx responses).

### CloudZero API Integration

**Confirmed from API docs (`_CZ_Docs_/reference/`):**

| Detail | Value |
|---|---|
| Endpoint | `POST /v2/connections/billing/anycost/{connection_id}/billing_drops` |
| Base URL | `https://api.cloudzero.com` |
| Auth | `Authorization: <api_key>` header — **no `Bearer` prefix** |
| Required scope | `connections:create_billing_anycost_billing_drop` |
| Content-Type | `application/json` |
| Idempotency | `cloudzero-idempotency-key` header (use for V2 re-upload protection) |
| Validate-only endpoint | `POST /v2/connections/billing/anycost/validate_billing_drop` (dry run, no data written) |
| Max uncompressed body | 5 MB (returns 413 if exceeded) |

**Request body schema (`anycost_stream_connection_billing_drop`):**
```json
{
  "month": "2025-01-01T00:00:00Z",
  "operation": "replace_drop",
  "data": [
    {
      "lineitem/type": "Credit",
      "lineitem/description": "AWS promotional credit",
      "time/usage_start": "2025-01-01T00:00:00Z",
      "time/usage_end": "2025-01-31T23:59:59Z",
      "resource/account": "123456789012",
      "resource/service": "AWSCredits",
      "cost/cost": "-50.00"
    }
  ]
}
```

**`operation` values:**
- `replace_drop` (default) — replaces all data for that month (use this for idempotency on re-upload)
- `replace_hourly` — replaces overlapping hours only
- `sum` — appends to existing data

**`lineitem/type` for credits:** Use `Credit`

**Key unknowns still needed before build:**
- `connection_id` — the AnyCost Stream connection ID in CloudZero (retrieve from Settings > Billing Connections)
- Exact column names and format of the source credits CSV

- Store API key in AWS Secrets Manager or Lambda environment variable (never hardcoded)

### S3 File Format Assumptions (confirm before build)
- File format: CSV (assumed — confirm with Kiteworks)
- Key column: AWS Account ID (not name)
- Expected columns: TBD — document after reviewing a sample file

### AWS SAM Template (key resources to define)
- `AWS::S3::Bucket` — credits bucket
- `AWS::Lambda::Function` — parser + API caller
- S3 event trigger (defined inline in SAM as an `S3` event source)
- `AWS::IAM::Role` — Lambda execution role (S3 read, Secrets Manager read, CloudWatch write)

### Deployment Plan
1. Set up SAM project structure locally
2. Configure `samconfig.toml` for target AWS account/region
3. `sam build` → `sam deploy --guided` for first deploy
4. Use `sam deploy` for subsequent updates
5. Test with a sample credits file upload

---

## Open Questions / Prerequisites Before Building

- [x] Review CloudZero API docs — confirmed: AnyCost Stream billing drop, API key auth, CBF row schema
- [ ] Get a sample credits file to confirm format and columns
- [ ] Get `connection_id` for the AnyCost Stream connection (Settings > Billing Connections in CloudZero)
- [ ] Confirm target AWS account and region for deployment
- [ ] Confirm S3 bucket naming convention (existing bucket or create new?)
- [ ] Confirm with Kiteworks team after V1 is running

---

## Gate Check: Ready for Phase 2 (Setup)?

- [x] Mission is clear and 1-sentence explainable
- [x] Target user defined
- [x] Milestones defined (MVP through Later / Not in Scope)
- [x] Tech stack chosen
- [x] CloudZero API docs reviewed — endpoint, auth, payload schema confirmed
- [ ] Sample credits file reviewed
- [ ] `connection_id` for AnyCost Stream connection retrieved
- [ ] Spec reviewed by Griffin
