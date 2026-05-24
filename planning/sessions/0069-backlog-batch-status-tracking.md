# 0069 — BACKLOG batch status tracking

## Goal

Add `Status:` line to consumer-project BACKLOG batches — four states (active, queued, parked, shipped). Replaces the implicit "first unticked batch is current" heuristic with explicit state.

## Inputs

- `parse_backlog.py`, all five subagent bodies, `stop.py`, `user_prompt_submit.py`
- Templates: BACKLOG-TEMPLATE, DOC-STRUCTURE, VOCABULARY, Reference manual
- `tests/` fixtures

## Outputs

- Parser exposes `status` field per batch
- before-build → `Status: active`, after-build → `Status: shipped`
- Planning can park/unpark batches
- Templates, docs, Reference manual, tests updated

## State machine

```
queued ──→ active ──→ shipped
  ↑          │
  └── parked ←┘
```

- **Queued → Active**: before-build
- **Active → Shipped**: after-build (+ tick)
- **Active → Parked**: planning
- **Parked → Queued**: planning removes Status line
- No Status line = queued (default)

## Open questions

- Should `Status: shipped` coexist with `[x]` tick? (Current design: yes — tick is visual, Status is parser authority.)
- Does batch-executor need Status awareness? (Probably not — it builds whatever before-build locked.)

## Risks / dependencies

- parse_backlog.py is load-bearing — thorough test coverage required.
- Both folder and single-file modes must work.
- No external dependencies.
