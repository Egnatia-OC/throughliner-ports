# v50 — 2026-05-22 — Automated vs. manual test split + non-UI test types

**What shipped.** V48 scope — biggest method change since V27. Four test types (Look and click, Run and read, Trigger and observe, Generate and inspect). Per-row Claude/User verifier split. 10-column TEST-LOG (adding Type + Verifier, renaming User Notes→Notes). Tests: sub-section in BACKLOG batches. Claude-automated test execution in after-build. Two-section recap ("Claude verified" / "Please check"). Commit/tag prompt (UX friction item 5). Backwards-compatible: shared regex handles 10- and 8-column; case 4 backfills. Extracted shared `parse_test_log_rows` from session_start.py into project_state.py (caught real bug — 8-column regex misparsed 10-column rows). Footer V45→V46; plugin 0.45.0→0.46.0.

**Decisions.** Tests in after-build (not batch-executor) — keeps build/test boundary clean. Verifier per-row (not per-type) — same test type can be structural or judgement. Optional regex group for backwards compat.

**Pivots.** Frame-correction sweep caught session_start.py misparse: 8-column regex on 10-column rows assigned Verifier to `confirmed_explicitly`, falsely flagging all rows.

**Carried forward.** OQ "test split" removed. UX friction 5/7 done. "Graduate" prerequisite 2 shipped (3/4 done).

