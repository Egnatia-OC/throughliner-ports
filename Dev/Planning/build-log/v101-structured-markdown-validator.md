# v101 — 2026-05-27 — Structured-markdown validator

**What shipped.** PostToolUse validation extended from BACKLOG-only to five doc types: BACKLOG parse (existing), scope-context (batch files), TEST-LOG column count, build-log entry sections, and proxy header format. New `validate_docs.py` script with four validators. Five file-type detection helpers added to `project_state.py`. 36 new tests (31 validator unit + 5 PostToolUse integration), total suite now 220.

**Decisions taken and why.**
1. Separate script (`validate_docs.py`) — validators are shape-checkers, distinct from `parse_backlog.py`'s data-extraction role. Different consumers, different evolution pace.
2. PostToolUse as primary trigger — same write-time validation pattern as the existing BACKLOG check. Also usable standalone via CLI.
3. Lenient warnings, not blocks — `additionalContext` format so Claude sees and self-corrects. Same philosophy as the BACKLOG parser.
4. Operational proxies (backlog.md, build-log.md, test-log.md) exempt from proxy header validation — they're directly edited indexes with different format rules.
5. Scope-context check only fires on batch files with enough content to be non-trivial (≥3 non-heading lines). Avoids false positives on drafts under construction.
6. Build-log entry check requires a heading to fire — empty files and stubs are not false positives.

**Pivots and surprises.** Two test failures on initial run: empty-string inputs triggered warnings for build-log and proxy validators. Fixed with early-return guards for empty/stub content.

**Carried forward.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 3 new/modified (validate_docs.py, project_state.py, post_tool_use.py) + 2 test files + 21 footer bumps + plugin.json + 3 crash-course/guide updates + INVENTORY
- **Carve-outs:** None
- **Session notes:** Full test suite passes (220 tests, 6.22s).
