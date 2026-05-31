# V60 — 2026-05-24 — BACKLOG batch status tracking

**What shipped.** Scope 0069. `Status:` line for BACKLOG build batches — four lifecycle states (queued, active, parked, shipped). Parser (`parse_backlog.py`) exposes `status` field in output JSON and skips shipped/parked batches when finding the top batch. Session-start hook (`session_start.py`) updated to skip shipped/parked batches in top-batch detection. Stop hook (`stop.py`) skips shipped batches in folder-mode after-build detection (prevents false-positive redirect when `Status: shipped` advances BACKLOG mtime past TEST-LOG mtime). Before-build writes `Status: active`; after-build writes `Status: shipped`; planning parks/unparks. DOC-STRUCTURE, VOCABULARY, Reference manual, crash-course guide, both BACKLOG templates, INVENTORY updated. 14 new tests (37 total parse_backlog tests), 166 total suite. Test fixtures updated with shipped/parked batch files.

**Decisions.** Status line positioned at top of batch body (after heading, before Goal) — easy to spot and parse. Absent = queued (backwards-compatible default). Stop hook's shipped-skip only implemented for folder mode; single-file mode retains existing mtime heuristic (legacy, lower priority). Batch-executor unchanged — builds whatever it receives regardless of status.

**Pivots.** Session-start hook's `detect_top_build_batch` needed updating too — it had independent batch-detection logic that didn't know about Status. Refactored from first-match to iterating with skip logic.

**Carried forward.** Nothing.

