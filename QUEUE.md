# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Add inline-reads rule to behaviour.md**
Why: Claude spawned an agent for the pre-push consistency sweep — a sequential checklist that only needs a handful of Read and Grep calls. No procedure told it to use agents, but nothing told it not to. A general rule prevents this across all skills.

Build:
- Add rule to target behaviour.md: use direct tool calls (Read, Grep, Glob) for work that's a bounded checklist of file reads and comparisons. Don't spawn agents for lookups that don't require exploration.

**Add context management to skill handoffs + update README model**
Why: Claude loses routing accuracy as context degrades late in sessions — prescribing `/compact` or `/clear` between skills addresses the root cause instead of patching individual symptoms.

Build:
- Add a context management line to each skill's handoff/close-out step: tell the user to run `/compact` before invoking the next skill, or `/clear` if there was a push or commit.
- Update README tested model to Opus 4.6 on max effort.

**Fix next.md clean-slate output for active build check**
Why: Four attempts to land this fix — it keeps getting lost. The active build check narrates "No active build" when no _build.md exists, which reads like a failure. Needs explicit direction for the clean-slate path.

Build:
- In target next.md Step 1 point 1, mark the active build check `[SILENT]`. If _build.md exists, offer to resume. If not, move on — no output either way.

**Reorder done.md Phase 3 handoff**
Why: Knowing what's queued changes whether the user wants to push. Current flow bundles push + next-up; correct flow separates them and adds context management.

Build:
- Reorder target done.md Phase 3: next-up recommendation first (its own turn), then push prompt as a separate turn.
- The push/handoff turn includes context management guidance: run `/compact` before invoking the next skill, or `/clear` if a push just happened.

**Add capture scan to next.md blocker gate**
Why: Captures can land between /plan and /next. The blocker gate checks SPEC.md and unresolved questions but not fresh captures — a relevant capture could contradict or improve the batch about to be built.

Build:
- Add a step to target next.md Step 1 blocker gate: scan Captures for items relevant to the top batch. Flag any that contradict, invalidate, or would benefit the batch if incorporated first. Recommend switching to /plan if found.

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Capture tags ([idea]/[question]) aren't pulling their weight — everything gets tagged [idea] and the tag does no work. Rethink whether these tags are useful or should be dropped/replaced.
- [idea] Pull-down audit: review Alex's global CLAUDE.md for rules that should be universal plugin behaviour (behaviour.md). Anything that shapes how Claude works with the user — and would apply to any user, not just Alex — belongs in the plugin so it doesn't behave differently on other people's devices.
- [idea] Trickle-up audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for rules that are repeated across multiple docs or aren't skill-specific. Move them to behaviour.md so they're stated once and apply everywhere.
- [idea] /done close-out steps need user-facing context in their output — "staleness sweep" and similar labels are internal jargon that tells the user nothing about what's happening or why they're waiting. Each visible step should say what it's checking and against what (e.g. "sweeping QUEUE.md for references to files or behaviour changed in this build"). Not explanations, just enough that someone watching knows what they're being held up for.
- [idea] "Disposition" in plan.md is jargon non-coders won't understand. Replace with a plain-language term (e.g. "decision" or "call") throughout the procedure.
- [idea] Output tag overhaul across all procedure docs. The tagging system ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) is defined in behaviour.md but many steps describe output behaviour in prose instead of using the tags. Audit all procedure docs (setup.md, plan.md, next.md, done.md) and replace prose output guidance with the proper tags. Includes: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report).
- [idea] When /plan decides no Test section is needed for a batch, that decision should be [SILENT] — no need to narrate "no test section because..." to the user.

### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
