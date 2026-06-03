# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Push markers in LOG**
- [build] Add a `**Pushed:** v<VERSION>` line to the push-and-rezip procedure — appended to the last LOG entry before repackaging, so release boundaries are visible in LOG without git commands

**Move /done handoff before push prompt**
- [build] Reorder done.md so the queue-state recommendation (Phase 3 handoff) comes before the "push to remote?" prompt in Step 2.4, not after

**Rephrase session-start status messages**
- [build] Update session_start.py to rephrase "no active build" so it reads as neutral status, not a failure — review all session-start messages for similar tone issues while in there

**Scope planning-time test entries**
- [build] Add rule to plan.md Step 3 — test entries are only added to a batch when there's a behaviour to verify that isn't self-evident from the build entries. Not every batch needs a [test] entry.

**E2E: verify /setup on fresh project**
- [test] Run /setup in consumer project, verify it scaffolds all four project docs and CLAUDE.md correctly

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Capture moments should loop — when a user shares an idea or observation during any skill (not just /plan), Claude should ask "anything else?" before resuming the procedure. Currently the user has to interrupt to share a second thought.

### Parked

- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
