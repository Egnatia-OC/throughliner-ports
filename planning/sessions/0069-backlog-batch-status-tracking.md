# 0069 — BACKLOG batch status tracking

## Goal

Add explicit batch-state tracking to consumer-project BACKLOGs. A `Status:` line in each batch body carries one of four states — active, queued (default / no line), parked, shipped — replacing the implicit "first unticked batch is current" heuristic. Sessions can immediately see where the project is in its build cycle without reconstructing state from scattered signals.

## Inputs

- `plugin/scripts/parse_backlog.py` — current parser (add Status line reading)
- `plugin/agents/before-build.md` — writes `Status: active` when locking a batch
- `plugin/agents/after-build.md` — writes `Status: shipped` alongside the existing batch tick
- `plugin/agents/planning.md` — park/unpark batches
- `plugin/agents/batch-executor.md` — confirm no changes needed (works on whatever before-build locked)
- `plugin/hooks/stop.py` — routes based on parse results
- `plugin/hooks/user_prompt_submit.py` — session-open classification, resume detection
- `plugin/templates/BACKLOG-TEMPLATE.md` — document the Status line
- `plugin/docs/DOC-STRUCTURE.md` — BACKLOG format spec gains the Status field
- `plugin/docs/VOCABULARY.md` — active/parked/shipped as defined terms
- `Crash course.md` — user-facing explanation of batch states
- `tests/` — parse_backlog tests, fixture updates

## Outputs

- Updated `parse_backlog.py` exposing `status` field per batch (values: `active`, `queued`, `parked`, `shipped`)
- before-build subagent sets `Status: active` when locking a batch
- after-build subagent sets `Status: shipped` when ticking the batch
- planning subagent can park (`Status: parked`) and unpark (remove Status line) batches
- Stop hook and UserPromptSubmit hook understand the new states
- BACKLOG-TEMPLATE documents the Status line convention
- DOC-STRUCTURE, VOCABULARY, Crash course updated
- Tests covering all four states and transitions

## Success criteria

- Parser correctly reads Status lines in both folder and single-file BACKLOG modes
- Session-open scan rule: find `Status: active` first (resume), else first batch with no Status line (next queued)
- before-build → active, after-build → shipped transitions work end-to-end
- Planning can park and unpark batches
- All existing tests still pass; new tests cover the four states

## State machine

```
queued ──→ active ──→ shipped
  ↑          │
  └── parked ←┘
```

- **Queued → Active**: before-build sets `Status: active`
- **Active → Shipped**: after-build sets `Status: shipped` + ticks batch checkbox
- **Active → Parked**: planning sets `Status: parked`
- **Parked → Queued**: planning removes the Status line
- No Status line = queued (default for new batches)

## Open questions for this session

- Should `Status: shipped` be written even though the `[x]` tick already signals done? (Current design: yes, both coexist — tick is visual shorthand, Status is parser authority.)
- Does the batch-executor need any awareness of Status, or does it remain agnostic (it builds whatever files before-build locked)?

## Risks / dependencies

- parse_backlog.py is load-bearing — parser bugs break the entire build cycle. Thorough test coverage required.
- Folder mode and single-file mode must both work. Test both.
- No dependency on other queued scope files.
