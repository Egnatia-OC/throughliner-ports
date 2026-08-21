# 7bc2c58 — The filing-claim hook now reads LOG/ before blocking, so a citation of shipped work passes

The hook blocks when a message names a slug that is not a `#### ` heading in QUEUE.md. A built item leaves the queue, so from the queue alone a citation of finished work and a report of a write that never happened look identical. Five recorded instances, every one a session correctly citing its own completed work.

A slug absent from the queue but present as a `LOG/<date>-<slug>.md` entry now suppresses the block, on the reasoning that a record means the slug names shipped work.

Distinguishing citation from filing-claim by parsing the sentence stayed refused — the item's own finding is that the two shapes are identical at the level the detector reads, so the suppression keys on the record instead.

One bug found in building: matching `-<slug>.md` with a leftmost search swallows the date, so `2026-08-21-already-shipped.md` yielded `08-21-already-shipped`. The date prefix is now stripped rather than matched around.

The block-once-per-claim downgrade and the no-LOG-folder behaviour are pinned unchanged, so a project without a `LOG/` behaves exactly as before.

**Files touched:** plugin/throughliner/hooks/stop.py, resources/testing/test_stop_hook.py (new)
**Routed to Captures:** [stop-hook-blind-between-tick-and-close]
Rule gate: not needed — a hook fix plus its tests; no method rule changes.
