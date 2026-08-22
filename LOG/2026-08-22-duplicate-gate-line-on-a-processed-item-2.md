# [HASH] — Lint check shipped: an item block with two or more `Rule gate:` lines is flagged by slug

Built in this run's three-check lint extension. The reasoning and design are in the shared entry [2026-08-22-lint-three-checks-build.md](2026-08-22-lint-three-checks-build.md); this entry names the item for its own slug per the sibling-citation rule.

Tick: done, confirmed (suite passes via `py`).
Rule gate: run — escalation to a hook rather than a rule; no method text changes and no slot is spent; the lint's advisory posture is unchanged.
FAQ: not needed because no user action changes.

**Files touched:** plugin/throughliner/hooks/post_tool_use.py, resources/testing/test_queue_lint_flags.py
**Routed to Captures:** none
