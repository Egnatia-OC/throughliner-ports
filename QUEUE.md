# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Post-update migration — no version tracking exists in consumer projects. After a plugin update that changes doc structure, existing projects silently drift. session_start should detect a version mismatch and trigger a migration process before any skill runs. Design questions: where to store the version (CLAUDE.md managed block? dotfile?), what migration looks like (automated rewrite vs guided walkthrough), how to handle interrupting the user's intended skill.
- [idea] Mid-build scope expansion protocol — when a user raises something out of scope during /next, Claude should default to routing it to Captures (or batch at discretion), explicitly mentioning "you can also add it to this build's scope" as a last-resort workaround framed as out-of-procedure. Two sub-questions: (1) should CLAUDE.md always be in scope for every batch, since it's the most common target for mid-build out-of-scope edits? (2) should the explicit "add to scope" workaround only be available in self-hosting projects building their own SI fork?
- [test] E2E: run /setup in a project that already has docs from an older plugin version — verify it handles existing files (overwrites, merges, or errors) without corrupting or silently dropping content
- [idea] /setup oversteps into /plan territory — two related issues from E2E testing: (1) Q4 procedure says "creates the first entry, mark it as [build]" (singular) but Claude expanded into 5 entries (2 build + 3 test), making scope decisions that belong in /plan; (2) closing message directs to /next first ("Run /next to start building, or /plan to adjust the queue first") which implies the batch is build-ready. Both need fixing: Q4 should produce one rough [build] entry, closing should direct to /plan to scope the work.
- [idea] /done handoff ordering — push question should come first, not after the "next up" recommendation. Currently "not yet" results in nothing, and the user is left choosing between a dead-end answer and ignoring the question to run /next. Better flow: ask about push first, then if the answer is "not yet," give the handoff ("run /next or /plan when ready").
- [idea] Capture moments should loop — when a user shares an idea or observation during any skill (not just /plan), Claude should ask "anything else?" before resuming the procedure. Currently the user has to interrupt to share a second thought.

### Parked

- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
