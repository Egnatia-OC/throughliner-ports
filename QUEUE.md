# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Session-start message tone**
Files:
- `plugin/si-plugin/hooks/session_start.py`
- [build] Reword the active-build branch (~line 96): "The previous session was interrupted mid-build" implies a crash. Make it neutral — the build is simply still open/unfinished, which is normal when the user closes the app deliberately.
- [build] Review the no-active-build branch (~line 103) and soften if needed so both branches share a calm, reassuring tone.
- [test] Trigger session_start in both states (active build present / absent) and confirm each message reads as reassuring, not alarming.

**LOG test-to-decision linkage**
Files:
- `plugin/si-plugin/docs/done.md`
- [build] Add rule to done.md: LOG keeps all test results in the Tests field. When a test outcome drove a design decision (failure caused requeue, rethink, or revealed a gap), the Decisions entry cites that test outcome as its rationale. Routine passes stay in Tests only — they don't generate decisions.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Captures

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.


### Parked
