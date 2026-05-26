# V25 — Build orchestration core (2026-05-16)

CLI pre-validation via outputs/ workaround. Windows integration deferred to post-commit PowerShell session.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 031 | 2026-05-16 | V25 | `parse_backlog.py` CLI: 15-scenario suite covering top-batch detection, change_list parsing, Files: tick-state, Serves line extraction, prerequisite labels, malformed-input lenience | `plugin/scripts/parse_backlog.py` | Pass | 15/15. Pre-validation tier (CLI). outputs/ workaround. Windows retest owed. |
| 032 | 2026-05-16 | V25 | Stop hook end-to-end CLI: 8-scenario suite covering empty backlog, single-batch redirect, post-completion next-batch redirect, `stop_hook_active` loop prevention, parser-error lenience | `plugin/hooks/stop.py` (+ `parse_backlog.py`) | Pass | 8/8. Pre-validation. Loop-exit (Opus risk #2) verified. outputs/ workaround. Windows retest owed. |
| 033 | 2026-05-16 | V25 | PreToolUse boundary check (V25 (c)) + V19 (a)/(b) read-only and V22 (e) Serves-line regression: 9-scenario suite | `plugin/hooks/pre_tool_use.py` | Pass | 9/9. Pre-validation. New (c) blocks edits outside Files: and allows prerequisite-labeled files; V19/V22 checks still pass. outputs/ workaround. Windows retest owed. |

