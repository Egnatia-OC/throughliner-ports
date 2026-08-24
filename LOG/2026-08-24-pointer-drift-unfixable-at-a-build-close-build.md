# 3ed3db1 — Built: the queue tool gains --replace-in, making the close's pointer-drift arm performable

done.md told a build close to fix pure pointer drift "HERE" while the scope-lock rightly refused the edit — the rule catching up with the machinery. `reorder_queue.py` gained `--replace-in <slug> --old <literal> --new <literal>` (optional `--section`): keyed by slug, refusing unless the old string occurs exactly once in that entry, touching no other entry byte-for-byte (self-checked), reporting the replacement. done.md's sweep arm names the route. Five suite cases in `test_reorder_queue.py` cover must-fire and must-refuse, exercised against scratch copies. The operation got its first live uses the same day it shipped — a quote-claim fix and a heading fix on fresh captures, both flagged by the lint mid-session. The refused alternatives stand: planning-closes-only, filing a capture instead, and a general in-entry edit (judgment edits stay out of builds).

Rule gate: run — amendment to done.md's staleness-sweep pointer-drift arm, rewording it to name the tool route; no freestanding rule, nothing evicted. Admitted on the recorded 2026-08-23 instance.

Files touched: plugin/throughliner/scripts/reorder_queue.py; plugin/throughliner/docs/done.md; resources/testing/test_reorder_queue.py
Routed to Captures: none
Done, confirmed: full queue-tool suite green via py, including the five new cases.
