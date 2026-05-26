# V28 — V27 fix sweep + helpers extraction (2026-05-18)

Live `claude --plugin-dir` against rebuilt g4 fixture. Two-session run: (1) Stop hook → after-build → MANIFEST + recap + TEST-LOG row; (2) restart → tripwire → planning read-back → Pass recorded. All rows Pass; one caveat on #069.

Three V27 Skipped rows unblocked: AB1 (#059), AB3 (#060) retested via after-build; P1 (#057) regression-checked. P2 #061, L1 #062, L2 #063 remain Skipped (need narrower fixtures).

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 064 | 2026-05-18 | V28 | AB2 retest — after-build writes blank-Status rows to `TEST-LOG.md` when opening a test session (the V19-check-(a) fix) | `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES += "TEST-LOG.md"`) + `plugin/agents/after-build.md` | Pass | Write(TEST-LOG.md) succeeded; row #001 landed with blank Status. Flips V27 #058 Fail. |
| 065 | 2026-05-18 | V28 | AB1 retest — after-build silently updates `MANIFEST.md` for created elements | `plugin/agents/after-build.md` (MANIFEST silent update step) | Pass | MANIFEST entry added (alphabetical, single-line). Flips V27 #059 Skipped. |
| 066 | 2026-05-18 | V28 | AB3 retest — after-build recap labels `[Requested]` / `[Suggested]` from BACKLOG.md change-list bullets | `plugin/agents/after-build.md` (recap shape, label-read pass) | Pass | Recap "What shipped" carried `[Requested]` label from BACKLOG. Flips V27 #060 Skipped. |
| 067 | 2026-05-18 | V28 | SessionStart tripwire fires post-refactor (V27 #056 regression check after V28 helpers extraction) | `plugin/hooks/session_start.py` (TEST-LOG tripwire) + `plugin/scripts/project_state.py` (extracted helpers) | Pass | Run 2 (restart with unconfirmed row from run 1). Main Claude invoked planning subagent to close test session. Confirms `project_state.py` extraction faithful to V27 behaviour. |
| 068 | 2026-05-18 | V28 | Planning subagent per-row read-back post-refactor (V27 #057 regression check) | `plugin/agents/planning.md` (V27 extension — Rule 2) | Pass | Specific-row read-back shape preserved post-refactor. Full advance-after-answer path also verified (see #070). |
| 069 | 2026-05-18 | V28 | Stop hook exits silent when previous-batch test session is open (V28 stop.py fix) | `plugin/hooks/stop.py` (V28 `is_test_session_open` check before `run_parser`) + `plugin/scripts/project_state.py` | Pass (caveat) | Stop hook exited silent as expected. **Caveat:** fixture's batch was fully ticked, so `run_parser` would return empty even without V28's check — uniquely-V28-distinguishing scenario (unticked batch + unconfirmed rows) not replicated. Mechanical inspection supports Pass. |
| 070 | 2026-05-18 | V28 | Planning subagent records Pass + closes test session via Edit on `TEST-LOG.md` | `plugin/agents/planning.md` (read-back close-out) + `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES` applies to Edit too) | Pass | Edit flipped row #001 Status to Pass, Confirmed Explicitly to Yes. Drift checks clean. Demonstrates Edit (not just Write) uses the V28 fix path. |

