# 3102929 — The epoch-marker dead end kept on a narrower diagnosis: /setup stops stamping an epoch whose conversion was skipped

All three of the item's candidates treated the symptom; the root cause is /setup writing `4` after skipping the epoch-4 conversion. The fix is at the write — the migration stamps the new epoch only when its conversion ran, and a skip leaves the old value with a plain warning that the halt will recur. For a marker already wrong, the item's own third candidate stands: accept the lock, cost is one queue item, because widening a lock to admit approved cases is how locks stop meaning anything. Build block on the item.

**Queue changes:** [close-cannot-correct-a-marker-setup-wrote] moved Unprocessed → Processed, cleared, beside the other setup.md item.
**Work processed:** kept.
