# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**E2E: install guide drives a fresh Claude chat through SI setup** **[e2e-install-guide]**
Depends on: install-guide

Once INSTALL.md and the README reframing exist, the only meaningful verification is the actual flow it's meant to support: a fresh Claude chat with no prior context, given the repo link and "guide me through setup." This catches three things at once — whether Claude finds INSTALL.md from the README pointer, whether the opening interview questions land for a real user, and whether the branched walkthrough (Claude Code install → paid plan → plugin install) runs cleanly. Splitting this from the build batch keeps the build commit clean and gives the test its own LOG entry, since the result is feedback (does the guide work?) not changed files.

Test:
- E2E (user-run, separate live session): open a fresh Claude chat at claude.ai with no prior context. Paste the SI repo URL. Say "guide me through setup." Observe whether Claude finds INSTALL.md, runs the opening interview, and walks through the branches cleanly. Report findings as captures (anything Claude missed, mis-paced, or routed to the terminal when it shouldn't have).

**Refresh reader-test-workflow.js to match current SI shape** **[reader-test-refresh]**

The reader-test workflow's fake project has drifted from how SI actually works now: it includes a DECISIONS.md doc and routes design rationale through it, queue entries are type-tagged inline as [build]/[test]/[idea]/[question], and the mirrored CLAUDE.md likely shows the older shape too. Running the workflow as-is mostly measures drift between current docs and a stale fake project, not drift between current docs and real reader comprehension — so findings come out noisy and signal is lost. The refresh aligns the fake project with current SI (LOG-based why-pipeline, Build/Test subheadings + Captures section, current CLAUDE.md template), re-checks the session-start hook output strings against the current session_start.py, and audits the 5 stock user questions for ones now trivially answered or phrased in ways a real user wouldn't. The synthesis FAQ vs Other split stays — user-question-shaped findings feed the FAQ template, procedure findings feed procedure docs; collapsing would lose that signal. FAQ template staleness gets handled downstream by running the refreshed workflow, not as upfront work here.

Build:
- resources/reader-test-workflow.js: drop FAKE_DECISIONS and DECISIONS.md references; replace with a short FAKE_LOG showing 1-2 entries in current format (inline prose rationale, **Files touched:** block).
- resources/reader-test-workflow.js: rewrite FAKE_QUEUE to use bold batch titles with Build/Test subheadings and a separate Captures section; drop inline [build]/[test]/[idea]/[question] type tags.
- resources/reader-test-workflow.js: rewrite FAKE_CLAUDE_MD to mirror current plugin/si-plugin/templates/CLAUDE-TEMPLATE.md.
- resources/reader-test-workflow.js: verify SESSION_NO_BUILD and SESSION_ACTIVE_BUILD strings against current plugin/si-plugin/hooks/session_start.py output; update if drifted.
- resources/reader-test-workflow.js: audit the 5 USER_QUESTIONS; replace any now trivially answered by current docs or phrased in ways a real user wouldn't.
- resources/reader-test-workflow.js: leave the synthesis FAQ/Other split intact.

Test:
- Run the refreshed workflow once (user-triggered, requires ultracode/opt-in). Inspect the synthesis output: do findings reflect real comprehension gaps in current docs, or do they still flag old-shape mismatches? Route useful findings to QUEUE Captures.

### Parked

- **[sizing-gates-rework]** Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- /next's Step 7 completion close-out says "Run /done to record this and commit, or keep adjusting" — but Claude has been observed instructing the user to run /next instead, while still inside /next after the batch completed. Two problems with that drift: (1) it skips /done entirely, leaving the build uncommitted and _build.md in place, which then blocks the next /next via the "one build at a time" rule; (2) it nudges the user toward a back-to-back build pattern that bypasses the close-out judgment steps /done exists to enforce. The doc says the right thing already, so the fix isn't a wording change at Step 7 — it's tightening whatever lets Claude substitute /next for /done at completion. Candidates: tag Step 7 [SEQUENCE] or add an explicit "never recommend /next from inside /next" rule under Scope discipline in plugin-behaviour.md, since "one build at a time" is the same principle in different framing. Pairs with **[keep-adjusting-rewrite]** — that one narrows what "keep adjusting" means; this one closes the larger /done-skip drift.

### Parked

- Add scenarios to reader-test-workflow.js — after [reader-test-refresh] lands and the refreshed workflow has been run once, evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Decision deferred because the refreshed first run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity. Promote as one or more build batches once scenarios are picked.

- Trickle-up audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for rules that are repeated across multiple docs or aren't skill-specific. Move them to plugin-behaviour.md so they're stated once and apply everywhere. Parked pending the audit-as-batch-type batch landing — once /next handles audit batches, this gets promoted as an audit batch with the target (the four procedure docs) and criteria (repetition, non-skill-specific rules) already defined here.

- Output tag overhaul audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for prose that describes output behaviour where a tag ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) should be used instead. Includes: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report). Parked pending the audit-as-batch-type batch landing — same reason as the trickle-up audit capture.

- In-scope / out-of-scope distinction audit: review plan.md, next.md, and plugin-behaviour.md for whether the in-scope vs out-of-scope distinction is stated explicitly enough, or whether it's currently load-bearing on Claude's judgment without being written down. The capture this came from also flagged build-abort mechanics and the "keep adjusting" close-out language; both of those got promoted as their own batches. This audit is the remaining thread. Parked pending the audit-as-batch-type batch landing — same dependency as the trickle-up and output-tag audits.

- Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Queue ordering rule: builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into a mechanical rule. (The companion /next-time check — recommend switching to /plan if related captures exist for the top batch — shipped as the next.md blocker-gate capture scan.)
- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
