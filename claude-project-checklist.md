# Claude Code Project Checklist

A reusable checklist for starting and running projects with Claude Code. Work through each phase in order — don't skip ahead until the gate check passes.

---

## Phase 1: Ideation & Spec

The goal here is to think before you build. Use voice mode or chat to brainstorm, then save outputs as markdown files.

### Define the Project
- [ ] What are you trying to do? (1-2 sentence mission)
- [ ] Who is this for? (Target user)
- [ ] What problem does it solve?
- [ ] What does the product actually do? (Be detailed on UX, workflows, and process)

### Define Milestones
- [ ] **MVP** — Initial core features (what's the smallest useful thing?)
- [ ] **V1** — Improvements and additional features
- [ ] **V2** — Extended core functionality
- [ ] **Later** — Nice to have
- [ ] **Not in Scope** — Explicitly out for now (this prevents scope creep)

### Create the Spec Doc
A lightweight combo of a Product Requirements Doc (PRD) and Engineering Design Doc (EDD).

**Product Requirements:**
- [ ] User personas and use cases
- [ ] Detailed UX flow (screens, interactions, edge cases)
- [ ] Success criteria — how do you know it works?

**Engineering Design:**
- [ ] Tech stack decisions (or ask Claude to recommend based on your goals)
  - Programming language
  - Frontend framework
  - Backend framework
  - Database
  - Cloud / hosting
  - AI models (if applicable)
- [ ] High-level architecture (ask Claude to draft this)
- [ ] API design (endpoints, data flow)
- [ ] Database schema / structure
- [ ] Hosting & deployment plan

> **Tip:** Tell Claude to *interview you first* with clarifying questions before writing the spec. You'll get a much better doc.

### ✅ Gate Check: Ready for Setup?
- [ ] Spec doc is written and reviewed
- [ ] Milestones are clearly defined
- [ ] Tech stack is chosen
- [ ] You can explain the MVP in one sentence

---

## Phase 2: Project Setup

### Repository & Environment
- [ ] Create GitHub repo
- [ ] Set up `.gitignore` (include `.env`, `node_modules`, OS files, etc.)
- [ ] Create `.env` file — ask Claude to generate an `.env.example` based on your stack, then fill in real values
- [ ] Verify secrets are never committed (check `.gitignore`)

### CLAUDE.md
Keep this lean and focused. It's Claude's working memory — don't bloat it.

- [ ] Project goals (2-3 sentences)
- [ ] Architecture overview (folder structure)
- [ ] Design style guide & UX guidelines
- [ ] Constraints & policies (e.g., "never push to main", "always use env vars for secrets")
- [ ] Repo etiquette (branching strategy, PR vs. direct merge rules, naming conventions)
- [ ] Frequently used commands (so Claude runs without asking)
- [ ] Links to other doc files and what they contain

> **Tip:** Iterate on CLAUDE.md as the project evolves. Use a custom command or `#memorize` to keep it current.

### Documentation Files (separate from CLAUDE.md)
- [ ] `docs/architecture.md` — System design, frontend components, data flow
- [ ] `docs/changelog.md` — What's changed over time
- [ ] `docs/project-status.md` — Current state so you can leave and return
- [ ] `docs/reference/` — Key feature documentation as needed

> Tell Claude: *"Update files in the docs folder after major milestones and additions."*

### Testing Strategy
- [ ] Decide on testing approach: unit tests, E2E, or both
- [ ] Set up test framework (Jest, Vitest, Playwright, etc.)
- [ ] Define what "tested" means for your project (e.g., "all API routes have tests")

### MCP Servers
Integrations that connect Claude to external tools. Make sure your tech stack is defined first.

- [ ] Frontend MCP (if applicable)
- [ ] Database MCP (if applicable)
- [ ] Browser testing: Playwright MCP or Puppeteer MCP (for web apps)
- [ ] Deployment: Vercel MCP, Netlify, etc.
- [ ] Analytics: Mixpanel, PostHog, etc. (if applicable)
- [ ] Project management: Linear, GitHub Issues, etc. (if applicable)
- [ ] Confirm each MCP has setup docs referenced in your project

### Slash Commands & Subagents
- [ ] Set up core slash commands:
  - `/commit` — Commit with message
  - `/commit-push-pr` — Commit, push, and open PR
  - `/update-docs` — Update docs folder with changes
  - `/changelog-updater` — Update changelog after features/fixes
  - `/frontend-tester` — Run Playwright E2E tests
  - `/retro-agent` — Reflect on session, update CLAUDE.md and commands
  - `/create-issue` — Log a GitHub issue from a description
- [ ] Set up subagents for parallelizable tasks (subagents fork context — they don't share state with each other)

### Plugins (Optional)
- [ ] Browse Claude Plugin Marketplace for useful extensions
- [ ] Consider: frontend-design, feature-dev, AI dev toolkit

### Advanced (Optional)
- [ ] Pre-configure permissions (allow Claude to run commands without asking)
- [ ] Set up hooks for automation (e.g., Slack/SMS notifications on events)

### ✅ Gate Check: Ready to Build?
- [ ] Repo created, `.env` configured, secrets protected
- [ ] CLAUDE.md is written and focused
- [ ] Docs folder structure is in place
- [ ] MCP servers connected and tested
- [ ] At least `/commit` and `/update-docs` commands are working
- [ ] Testing framework is set up

---

## Phase 3: Build

### Pre-Build
- [ ] Select model: Opus (planning, complex tasks) or Sonnet (implementation)
- [ ] Enter plan mode (`/plan`) — understand what Claude will do before it does it
- [ ] Point Claude at the spec doc and ask it to build MVP (Milestone 1)
- [ ] Ask Claude to use parallel subagents where tasks are independent

### Build Workflows

Choose the right workflow for the situation:

| Workflow | When to Use |
|---|---|
| **Single Feature** | One feature at a time, straightforward work |
| **Issue-Based** | Disciplined teams; GitHub Issues are the source of truth |
| **Multi-Agent** | Multiple independent features in parallel (requires git worktrees) |

**Single Feature Flow:**
`Research → Plan → Implement → Test`

1. **Research** — Ask Claude to create a research report. Reference transcripts, docs, or web searches. Save to `docs/`.
2. **Plan** — Use plan mode or `/feature-dev` to break down tasks before coding.
3. **Implement** — Build it. Keep commits small and frequent.
4. **Test** — Run tests. Use `/frontend-tester` for E2E. Fix what breaks.

**Issue-Based Flow:**
1. Log features and tasks as GitHub Issues (be disciplined — use `/create-issue`)
2. Ask Claude to pick up and work on specific issues
3. Reference issue numbers in commits and PRs

**Multi-Agent Flow (Advanced):**
1. Set up git worktrees so parallel work doesn't conflict
2. Spin up multiple Claude sessions on different features
3. Merge completed work back together
4. Resolve conflicts carefully

---

## Ongoing Practices

These aren't one-time tasks — keep doing them throughout the project.

- [ ] **Update CLAUDE.md** periodically (use a custom command + git commit)
- [ ] **Regression prevention** — When a mistake happens, use `#memorize` to add the lesson so it doesn't repeat
- [ ] **Run retros** — Use `/retro-agent` after dev sessions to improve your setup
- [ ] **Keep docs current** — Use `/update-docs` after milestones
- [ ] **Review Claude's work** — Even solo, skim diffs before merging. Claude makes mistakes.
- [ ] **Don't be afraid to start over** — Sometimes a fresh conversation or approach is faster than debugging a bad path

---

## Quick Reference: Recommended Tools

> Keep this as a separate companion doc if your checklist gets long.

**Plugins:**
- `frontend-design` @ claude-code-plugins — Better UI generation
- `feature-dev` @ claude-code-plugins — Structured feature development
- `compounding-engineering` @ every-marketplace — AI-powered dev workflow tools

**MCP Servers:**
- Vercel MCP — Deployment
- Mixpanel — Analytics
- Linear — Project management
- Playwright / Puppeteer — Browser testing

**Models:**
- Opus 4.5 — Planning, architecture, complex reasoning
- Sonnet 4.5 — Day-to-day implementation
