# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**LOG multi-file split**
- [build] Split LOG into per-push files — push caps the current file and creates a new one. Naming convention TBD during implementation.
- [build] Reverse index.md ordering (newest first) and ensure it works across multiple log files
- [build] Update /done to prepend new entries to the top of the current log file
- [build] Update push-and-rezip to cap the current log file and start a new one

**Why pipeline polish**
- [build] Audit capture, /plan promotion, batch drafting, /next execution, and /done logging for why-preservation — ensure reasoning captured at any stage survives through the full pipeline into the log
- [build] Tighten Q4 procedure in /setup to produce one rough [build] entry, not multiple scoped entries — E2E showed Claude expanding a singular instruction into 5 entries (2 build + 3 test), making scope decisions that belong in /plan

**Skill handoff polish**
- [build] Audit all skill-to-skill handoff prompts across /setup, /plan, /next, and /done — for each, simulate the prompt text and summarise the immediate context the user is in when they see it, then polish for clarity and flow
- [build] Fix /done handoff ordering — push question first, then "run /next or /plan when ready" if not pushing
- [build] Fix /setup closing message — direct to /plan first, not /next

**Mid-build scope expansion protocol**
- [build] Add mid-build capture routing to /next procedure — when user raises something out of scope, default to capturing it and ask "anything else?" before resuming
- [build] Add "anything else?" loop to all skills after any capture moment — currently the user has to interrupt to share a second thought
- [build] Add "add to scope" workaround as an explicit last-resort option, framed as out-of-procedure behaviour requiring user confirmation

**Post-update migration detection**
- [build] Add .si-version dotfile to /setup scaffolding, written with the current plugin version
- [build] Add version mismatch detection to session_start — compare .si-version against plugin version, warn user to run /setup if mismatched
- [build] Update /setup to handle existing docs (re-scaffold without overwriting user content)
- [test] E2E: run /setup in a project that already has docs from an older plugin version — verify it handles existing files without corrupting or silently dropping content

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.






### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
