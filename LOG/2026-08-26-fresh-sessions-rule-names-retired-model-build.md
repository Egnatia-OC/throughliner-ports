# [HASH] — Fresh-sessions rule no longer names 4.8 as the model the plugin is tuned for

The fresh-sessions bullet in this project's CLAUDE.md closed with a parenthetical asserting that the rule "does not change the Model target above — 4.8 stays the model the plugin is tuned for." That stopped being true on 2026-08-09, when docset A was retired and the Model target section began saying the one docset serves the 5-series with 4.8 explicitly no longer a supported target. The same bullet therefore stated the Fable-plans / Opus-builds split and, one clause later, named a model the project had stopped targeting.

The clause is repealed. The parenthetical now reads that the rule is about robustness to session-memory loss and does not change the Model target above — the rule's subject intact, the stale claim gone.

The item's second instruction was conditional and resolved against leaving it: the sentence's "post-Fable development model (from ~2026-06-20)" framing was to be dropped only if it contradicted the Model target. It names no retired model and describes a period rather than a target, so it stands. The item's scope was the 4.8 clause and it stayed there.

Acceptance confirmed by grep: `4.8` now appears in CLAUDE.md only in the Model target section's three history sentences, which the item's refusal line correctly protects as dated record.

Depth: short.

Rule gate: run — amendment rewording one clause of the fresh-sessions rule to match the Model target section; repeals the stale "4.8 stays the model the plugin is tuned for" clause, nothing added.

**Files touched:** `CLAUDE.md` (fresh-sessions rule's closing parenthetical, line 368).
**Routed to Captures:** none.
**Advisory:** not needed — see the sibling entry for this run.
