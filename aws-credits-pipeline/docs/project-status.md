# Project Status

## Current Phase: MVP Complete — Ready for Deploy

### Phase 1 — Spec & Design ✅
- Requirements, milestones, tech stack confirmed.
- CloudZero API docs reviewed; endpoint, auth, CBF schema confirmed.
- Sample credits CSV reviewed; format confirmed (no header, col 0 = account ID, col 1 = USD amount).

### Phase 2 — Project Setup ✅
- SAM project scaffold created.
- `.gitignore`, `.env.example`, `samconfig.toml` in place.
- `src/` and `tests/` requirements files created.

### Phase 3 — MVP Build ✅
- All source modules implemented (`csv_parser`, `cloudzero_client`, `logger`, `handler`).
- Full test suite: 32 tests across 3 test files.
- SAM template with S3 bucket, Lambda, IAM role (least privilege).

### Prerequisites Before First Deploy
- [ ] `git init` and push to GitHub remote.
- [ ] Retrieve `CLOUDZERO_CONNECTION_ID` from CloudZero → Settings → Billing Connections → AnyCost Stream.
- [ ] Confirm target AWS account/region; update `samconfig.toml` after `sam deploy --guided`.
- [ ] Run tests locally: `pip install -r tests/requirements.txt -r src/requirements.txt && pytest tests/ --cov=src`.

### Deploy Steps
```bash
# 1. Install SAM CLI (if not already installed)
brew install aws-sam-cli

# 2. Set credentials
export CLOUDZERO_API_KEY=<your_key>
export CLOUDZERO_CONNECTION_ID=<your_connection_id>

# 3. Build
sam build

# 4. First deploy (interactive — sets region, S3 bucket for artifacts)
sam deploy --guided

# 5. Subsequent deploys
sam deploy
```

### Verification
1. Upload `credits-2025-01.csv` (rename of `credits-example.csv`) to the S3 bucket.
2. CloudWatch Logs → `/aws/lambda/aws-credits-processor` → confirm structured summary log, 23 accounts.
3. CloudZero dashboard → credits visible under AnyCost Stream connection for January 2025.
4. Re-upload same file → no duplicate credits (`replace_drop` is idempotent).
5. `pytest tests/ --cov=src --cov-report=term-missing` → ≥90% coverage.
