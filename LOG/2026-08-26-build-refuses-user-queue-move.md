# 3b094b5 — A queue move the user explicitly directs mid-run is now performed, not refused

From a live consumer session. A run halted correctly on a walkthrough-less `[user]` item; the user then explicitly directed it to skip the item and move it back into the unprocessed section. The session held the filing-versus-processing boundary correctly and noted nothing else was cleared — then closed by asking whether she would rather it move the item and she "take the consequences of the build session doing it".

Two findings in one instance, and only one needed a rule. The narration was improvisation in a design gap: the ask names no actual consequence, reads as a dare, and re-offers the refused action as a flat menu instead of leading with a recommendation. The recommend-first and plain-language rules already govern that wording, so nothing new was written for it.

The design question was genuinely undecided, and is now settled: an explicit user direction carries through. The boundary guards Claude's own authority — an unattended run must not slide into processing — while the user owns an item's fate and ordering by standing rule, so executing her explicit move is not processing at all. Same logic as the yield rule's existing second-ask carve-out, which is why this is an arm on that rule rather than a rule of its own.

Two guards ride with it: nothing moves on inference, only on an explicit direction, and a delete still follows its own rules.

Refused at planning: keeping section moves planning-only against explicit direction. It protects nothing the boundary was built for, and it produced the dare.

**Files touched:** `plugin/throughliner/docs/next-build.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed — the halt-then-refuse-then-dare path has no footing left.
Rule gate: run — an amendment to next-build.md's yield rule, its parent: the queue-move arm joins the second-ask carve-out. Nothing evicted.
