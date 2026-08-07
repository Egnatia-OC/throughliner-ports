# [HASH] — The mover now reports which side of the readiness marker a cross-section move landed on

Built in the 2026-08-08 overnight blitz, run 2 — processed autonomously under the softened bar (departure recorded): the capture's own analysis named the reported-outcome route as strongest and cheapest, and the machinery already existed. `reorder_queue.py`'s `--move-section` now prints, whenever the target section carries the cleared-to-run marker, whether the moved item sits ABOVE it (cleared to run) or BELOW it (waiting, not cleared) — making the ambiguity visible at the moment it happens instead of removing it. The observed defect (AFTER the marker's anchor item lands the block below the marker, shelving what was meant to be cleared, with a normal success line) is pinned in `test_reorder_queue.py` as two new cases; the full suite is green. The mover-change and documentation-only routes were the item's other options; both are superseded by the report, which costs nothing and covers every future placement.

**Files touched:** plugin/si-plugin/scripts/reorder_queue.py, resources/testing/test_reorder_queue.py
**Routed to Captures:** none
FAQ: not needed because the mover's stderr is read by Claude, not by a consumer.
