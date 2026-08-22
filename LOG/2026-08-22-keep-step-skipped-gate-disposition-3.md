# [HASH] — Lint check shipped: a cleared rule-path item with no gate disposition is flagged by slug

Built in this run's three-check lint extension. The reasoning and design are in the shared entry [2026-08-22-lint-three-checks-build.md](2026-08-22-lint-three-checks-build.md); this entry names the item for its own slug per the sibling-citation rule.

Tick: done, confirmed (all four assertions pass via `py`).
Rule gate: run — escalation to a hook; no method text changes; the trigger-path set is the gate's own, already enumerated in CLAUDE.md.
FAQ: not needed because no user action changes.

**Files touched:** plugin/throughliner/hooks/post_tool_use.py, resources/testing/test_queue_lint_flags.py
**Routed to Captures:** none
