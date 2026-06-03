# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Captures

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] Push markers in LOG — append a `**Pushed:** v<VERSION>` line to the last LOG entry before push-and-rezip runs, so you can scan what happened between releases without running git commands.
- [idea] /done spec check — after authoring the LOG **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. If so, surfaces it to the user and updates spec on approval. May replace the current /plan pipeline gate ("if a user would see or experience the difference") rather than complement it — the /done check works retrospectively with actual decisions written down, which is a stronger signal than Claude guessing prospectively at planning time.
- [idea] Session-start "no active build" message is confusing — when the user is about to start a build, reporting the absence of one reads like a failure. Rephrase or remove so it doesn't alarm the user before they've even begun.
- [build] /plan batch format implies every batch needs a [test] entry — Claude pattern-matches and generates arbitrary tests even when the build entries are self-verifying. plan.md should say test entries are only added when there's a behaviour to verify that isn't self-evident from the build entries. Related to but distinct from the /done test-generation scoping fix (that's about post-build tests; this is about planning-time test entries).

### Parked
