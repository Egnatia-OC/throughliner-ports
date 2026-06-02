# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Tighten /plan Captures processing step 2**
- [build] Rewrite plan.md step 2 of the Captures loop — require engaging with substance and recommending in the same turn as presentation, and require presenting all four disposition options (promote / question first / park / drop) with the recommendation marked
- [test] Verify step 2 text explicitly requires both engagement and full option set

**Scope /done test generation to code changes**
- [build] Add scoping rule to done.md Step 1.2 — generate post-build tests only for code/app file changes, not for procedure doc or template edits where the batch's own [test] entries already cover verification
- [test] Verify Step 1.2 text distinguishes code from doc changes

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
- [build] /plan batch format implies every batch needs a [test] entry — Claude pattern-matches and generates arbitrary tests even when the build entries are self-verifying. plan.md should say test entries are only added when there's a behaviour to verify that isn't self-evident from the build entries. Related to but distinct from the /done test-generation scoping fix (that's about post-build tests; this is about planning-time test entries).

### Parked
