# Phase 1 Checklist — CloudZero AWS Credits Pipeline
*Pre-flight planning status + Claude Code terminal steps*

Two columns as you work: **Cowork (done)** tracks what's been completed here, and **Your action** is what you should do in your separate Claude Code terminal (or manually before opening Code).

---

## Define the Project ✅

| Item | Status | Notes |
|---|---|---|
| What are you trying to do? | ✅ Done | Automate monthly AWS credits redistribution for Kiteworks into CloudZero |
| Who is this for? | ✅ Done | Griffin / CloudZero internal team |
| What problem does it solve? | ✅ Done | Replaces manual monthly credits allocation with an automated S3 → Lambda → API pipeline |
| What does the product actually do? | ✅ Done | See spec doc for full UX flow and edge cases |

---

## Define Milestones ✅

| Milestone | Scope |
|---|---|
| **MVP** | S3 trigger → Lambda → parse credits by account ID → CloudZero API → CloudWatch logs |
| **V1** | Confirm allocations in CloudZero; output run summary report |
| **V2** | Schema validation, replay/retry, idempotency (re-upload protection) |
| **Later** | Error alerting (Slack / email via SNS) |
| **Not in Scope** | Frontend UI, real-time processing, multi-tenant support |

---

## Create the Spec Doc ✅

Spec doc created: `cloudzero-pipeline-spec.md`

| Section | Status |
|---|---|
| User personas and use cases | ✅ |
| Detailed UX flow | ✅ |
| Success criteria | ✅ |
| Tech stack decisions | ✅ |
| High-level architecture | ✅ |
| API design notes | ✅ (pending CloudZero API doc review) |
| Database schema | N/A — stateless pipeline, no database needed |
| Hosting & deployment plan | ✅ (AWS SAM → CloudFormation stack) |

---

## ✅ Gate Check: Phase 1 → Phase 2

| Gate Item | Status | Action Needed |
|---|---|---|
| Spec doc written and reviewed | ⏳ Needs your review | Open `cloudzero-pipeline-spec.md` and confirm |
| Milestones clearly defined | ✅ | — |
| Tech stack chosen | ✅ | Python 3.12 / Lambda / SAM / CloudZero API |
| MVP explainable in one sentence | ✅ | "Upload credits file to S3 → Lambda parses and pushes to CloudZero automatically" |
| CloudZero API docs reviewed | ✅ Done | Endpoint, auth, and payload schema confirmed — see spec for details |
| Sample credits file reviewed | ❌ Pending | **Your action: pull a sample and drop it in project** |
| AnyCost `connection_id` retrieved | ❌ Pending | **Your action: Settings > Billing Connections in CloudZero** |

---

## Your Actions Before Opening Claude Code

These are the things you need to do outside of the AI terminal before kicking off Phase 2.

### 1. ~~Pull together the CloudZero API docs~~ ✅ Done
The `_CZ_Docs_` folder was already in the project. API endpoint, auth method, and payload schema have been confirmed and documented in the spec.

- **Endpoint:** `POST /v2/connections/billing/anycost/{connection_id}/billing_drops`
- **Auth:** `Authorization: <api_key>` (no Bearer prefix)
- **Payload type:** AnyCost CBF rows with `lineitem/type: Credit`

### 1b. Get your `connection_id` (NEW — required before build)
You need the AnyCost Stream `connection_id` from CloudZero to call the billing drop endpoint.

**Your action:** In CloudZero → Settings → Billing Connections → find your AnyCost Stream connection → copy the connection ID. Store it as an env var (`CLOUDZERO_CONNECTION_ID`).

### 2. Get a sample credits file
You need at least one real (or anonymized) example of the monthly AWS credits CSV so Claude can write a parser that actually matches the format.

**Your action:** Pull a sample from wherever these are currently being stored/received. Anonymize account IDs if needed. Drop it in your project repo before building the Lambda parser.

### 3. Confirm your AWS deployment target
Before `sam deploy`, you need to know:
- Which AWS account you're deploying to
- Which region
- Whether the S3 bucket already exists or needs to be created

### 4. Create your GitHub repo

**In Claude Code terminal (once repo is created):**
```
# After `git init` and initial commit, tell Claude:
"Initialize a Python AWS SAM project for a Lambda function triggered by S3. Set up the folder structure, .gitignore (include .env, .aws-sam/, node_modules/), and a basic README."
```

---

## Suggested Phase 2 Kickoff Prompt (Claude Code)

Once you've done the above, paste this into your Claude Code terminal to start Phase 2:

```
I'm starting a new project. Please read the spec doc at docs/cloudzero-pipeline-spec.md and the CloudZero API docs at docs/cloudzero-api.pdf before doing anything. Then:
1. Ask me any clarifying questions you have
2. Create a CLAUDE.md with project goals, architecture overview, and key constraints
3. Set up the SAM project structure with Python 3.12
4. Create a .env.example with all environment variables we'll need (API keys, bucket names, etc.)
Use plan mode first — I want to review your approach before you write any code.
```
