# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Wire up the why-pipeline: preserve prose rationale, retrieve from log**
Why: The why-pipeline exists in fragments across behaviour.md, plan.md, and done.md but isn't named or owned as a single thing — and the retrieval half has never fired (Claude always infers from code, never reads the log). Captures, batches, and log entries must carry rationale as prose, re-authored at each stage with user approval, never collapsed into a structured field. When asked why something exists, Claude searches the log first.

Build:
- behaviour.md: add a "Why-pipeline" section. Two halves. Preserve: rationale travels capture → batch → log as prose; Claude shows wording at each stage for user approval; no dedicated why-field, the reasons live inline in the entry text. Retrieve: when asked why something exists or why a decision was made, Claude searches LOG/log.md and LOG/log-v*.md first; only falls back to the code if nothing relevant is found.
- behaviour.md Prior decisions: rewrite the two "check LOG/" lines so they point at the new Why-pipeline section instead of duplicating the rule.
- plan.md: remove the dedicated "why-line" from the batch structure (Step 3). Captures keep their prose rationale; batches carry that prose forward in the entry itself; user approves wording before write, same as today.
- done.md: remove the dedicated Why: field from both LOG entry templates (Build close-out 2.1, Plan close-out section 2). Log entry prose carries the rationale inline.
- done.md: change Phase 2 from [SILENT] to require log-entry wording approval before write — closes the one stage that currently bypasses user oversight.

Test:
- Ask Claude "why does [some recently-built component] exist?" — confirm it reads from LOG before inferring from code.

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

**Remove the [idea]/[question] capture tags**
Why: The tags are defined only in faq-template.md and CLAUDE-TEMPLATE.md, nothing in any procedure branches on them, and the two definitions contradict each other — the FAQ frames them as parallel categories while the idea → question pipeline in plan.md/behaviour.md treats them as sequential refinement stages. Dead and self-contradictory; leaving them ships that confusion to every new project.

Build:
- faq-template.md: rewrite the Captures sentence (line 15) and the "I just had an idea" answer (line 27) to drop the [idea]/[question] tags — captures become plain bullets that carry their own reasoning.
- CLAUDE-TEMPLATE.md: drop the ([idea]/[question] tags) parenthetical from the QUEUE.md line (line 10).
- This project's QUEUE.md: strip the leading [idea] from existing Captures bullets so the live doc matches the new convention.

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
- [idea] /done hash backfill is self-defeating: it commits, writes the short hash into LOG/log.md + index.md, then `git commit --amend` — but amending rewrites the commit to a new hash, so the recorded hash never matches the final commit. Confirmed this session: commit was 13c4612, post-amend HEAD is 44ab617, LOG records 13c4612. Every entry is affected. Fix: record the hash in a separate follow-up commit instead of amending, or stop recording hashes and reference by date/summary instead.
- [idea] During /plan, the promote/park/drop call comes before the batch entry is drafted, so the user approves a direction without seeing concrete outputs — they can't fully know what they're approving. Two candidate fixes: (a) Claude frames the work in concrete-output terms when recommending promotion, so the call is informed; (b) move the promote question to after the entry is drafted. (b) risks repeated re-drafting and fatigue from re-reading full entries. Surfaced live this session: user approved promotion of a three-part conceptual item with nothing concrete in front of them. Overlaps with the parked Sizing-gates-rework idea (concrete outputs as the readiness gate).
- [idea] Add a "one item at a time" rule to behaviour.md. When presenting multiple things where the user's next action depends on the previous (sequential questions, items needing approval, walkthrough steps), give one per message and state the count upfront. Don't preview upcoming items. Currently this lives only in Alex's global CLAUDE.md as a user preference — it should be universal plugin behaviour so it applies on every install. Overlaps with the parked Pull-down-audit capture.
- [idea] Add a "don't collapse rationale into structure" rule to behaviour.md. Reasons exist as prose. Don't force them into one-line summaries, dedicated why-fields, or typed taxonomies (e.g. "UX reason / functionality reason"). Both collapse meaning — a line truncates, a taxonomy is never complete. Preserving rationale means carrying the prose forward. Surfaced this session designing the why-pipeline; the why-pipeline batch encodes it specifically for capture→batch→log flow, but the general principle belongs in behaviour.md so it prevents the same mistake elsewhere.

### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
