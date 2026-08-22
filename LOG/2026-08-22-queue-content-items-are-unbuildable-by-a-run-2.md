# c904687 — Lint check shipped: a cleared item naming QUEUE.md in its Files line is flagged, whatever the flavor

Built in this run's three-check lint extension. The reasoning and design are in the shared entry [2026-08-22-lint-three-checks-build.md](2026-08-22-lint-three-checks-build.md); this entry names the item for its own slug per the sibling-citation rule, including the widening that absorbed [audit-cannot-read-queue-prose].

Tick: done, confirmed (all four assertions pass via `py`, including the [audit] case).
Rule gate: run — escalation to a hook; no method text changes and no keep-step clause is added.
FAQ: not needed because no user action changes.

**Files touched:** plugin/throughliner/hooks/post_tool_use.py, resources/testing/test_queue_lint_flags.py
**Routed to Captures:** none
