# V65 — 2026-05-25 — Session-open status summary

**What shipped.** Scope 0074. SessionStart hook's tier 3 output now includes a mandatory user-facing status summary: batch counts (queued/active/parked), next batch name with goal and file count, pending test count, and red-flag count. A directive in the hook output tells Claude to present this block to the user as the first action in every session — before routing, before questions. Three new helpers in `session_start.py`: `count_batch_statuses()`, `detect_top_batch_details()`, and two new regex patterns (`BATCH_GOAL_PATTERN`, `BATCH_FILES_ENTRY_PATTERN`). Six new tests in `test_session_start.py` (172 total, all pass). INVENTORY.md, Reference manual.md, and crash-course/getting-started.html updated for parity. All footers bumped V64→V65, plugin 0.64.0→0.65.0.

**Decisions.** Hybrid approach: hook-injected data (deterministic — always present) + hook-injected directive (tells Claude to present it). No rule added to universal-behaviour.md — the hook's own directive is authoritative and avoids doc duplication. Shipped/parked counts excluded from the summary (user only needs actionable state). The "Batch: " prefix that appears in Taskflow's batch names is a data quality issue from `/setup` case 4's file generation, not something to strip here.

**Pivots.** None. Scope delivered as specified.

**Carried forward.** The reframing note on 0074's PLAN.md row said "direct main-Claude presentation (no subagent routing)" — this aligns with the 0079 architecture redesign direction. When 0079 removes subagents, the status summary will continue working unchanged (it's hook→Claude, no subagent in the path).

