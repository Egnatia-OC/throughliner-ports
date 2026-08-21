# 15e10c9 — The editing-state contract gains a conformance test and a known-consumers line; the delete stays refused

Build entry; the planning record is `2026-08-21-editing-state-contract-status.md`. The user's three questions were settled at processing — a published field-level spec is standard practice where another program reads the format, so the contract stays and gains the two things it lacked. `resources/testing/test_editing_state_contract.py` loads `pre_tool_use.py`, calls the marker-writing function in a temp project, and asserts the payload matches the documented fields: version parity with the contract's stated "Currently 2", exactly the five documented keys, real booleans, project-relative forward-slash paths, the absolute-path fallback for outside files, and the `throughliner` producer constant — 15 assertions, passing. It runs under the existing hooks-staged-paths close trigger, the only moment the format can change. The contract now carries a Known consumers line naming the companion application and pointing at the test.

**Files touched:** `resources/testing/test_editing_state_contract.py` (new), `EDITING-STATE-CONTRACT.md`.
**Routed to Captures:** none from this item.
Tick: done, confirmed — the suite passes against the current hook and contract.
FAQ: not needed because nothing user-facing changes.
Rule gate: not needed — no method rule is authored or amended; the build is a test and a doc note.
