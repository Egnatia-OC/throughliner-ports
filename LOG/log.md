# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## e3e6db9 — Add test execution context and E2E batch rule to plan.md

**Files touched:**
- plugin/si-plugin/docs/plan.md: added test execution context paragraph (what Claude can verify vs what needs the user) and E2E batch separation rule to Step 3

**Tests:** None (doc-only change)

**Why:** The planner had no guidance on how test entries would actually be executed by /next. Without knowing that Claude can self-verify code traces but not visual/device/subjective checks, test entries got written ambiguously. And E2E tests that need a separate live session were getting appended to build batches, blocking the build flow while waiting on external verification. Both rules make planning decisions that previously required implicit knowledge.

**Routed to Captures:** next.md Step 1 blocker gate — check new captures for hard blockers (written during build); _build.md entry ticking over-communicated — should be [SILENT] or [BRIEF], not narrated (written during /done)

## a8a7c28 — Add operating conditions section to README

**Files touched:**
- README.md: added "Operating conditions" section between "Install" and "Getting started"

**Tests:** None (doc-only change)

**Why:** The README had install instructions but no guidance on what environment the plugin is tested under. Users need to know the difference between hard prerequisites (/setup) and soft assumptions (model, mode, context hygiene) so they can troubleshoot when something doesn't work as expected.

**Routed to Captures:** next.md Step 1 "No active build" narration wording (captured during /next)
