# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## 090d845 — Capture wording approval rule

**Files touched:**
- plugin/si-plugin/docs/next.md: Step 4 "User raises something out of scope" — changed step 1 from silent capture to draft-and-approve flow
- plugin/si-plugin/docs/done.md: Step 1.3 "Route findings to Captures" — changed from direct write to draft-show-approve before writing
- plugin/si-plugin/docs/plan.md: ground rules — broadened "never add to the queue" rule to explicitly cover both batches and captures

**Why:** Claude was writing captures to QUEUE.md without showing the user the wording first. The user has no chance to refine, correct, or reject what gets captured — and since captures flow through to batches via /plan, bad wording compounds. All other writes to QUEUE.md (batch entries, promote dispositions) already require approval; captures were the gap. Adding the rule to all three procedure docs where captures originate (next.md for out-of-scope items, done.md for findings, plan.md as a ground rule) closes it.

**Routed to Captures:** none

## 9905759 — Remove test generation from /done

**Files touched:**
- plugin/si-plugin/docs/done.md: removed steps 1.2 (Generate tests), 1.3 (Run Claude-verifiable tests), 1.4 (Present user tests); renumbered 1.5→1.2, 1.6→1.3, 1.7→1.4; removed Tests field from LOG template; removed "test results" from recap; removed test-related rules; updated Phase 1 description
- plugin/si-plugin/docs/plan.md: updated Test section guidance — replaced "/done already generates post-build tests" with "/done does not generate tests, so anything that needs verification must be planned here"
- plugin/si-plugin/skills/done/SKILL.md: removed "generate tests" from skill description
- plugin/si-plugin/templates/faq-template.md: removed reference to /done generating post-build tests

**Why:** /done was generating ad hoc tests after every build, duplicating what /plan should be doing. Testing is planned work — it belongs in batches where the planner can decide what needs verification, assign the right verifier (Claude vs user), and size the batch accordingly. Ad hoc generation at close-out produced tests with no planning context and no connection to the batch's intent. Removing it makes /plan the single owner of test planning and simplifies the /done flow.

**Routed to Captures:** Plan panel compatibility (captured before build, research filed at resources/research/plan-panel-integration.md)

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
