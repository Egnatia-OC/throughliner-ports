# [HASH] — CONTRADICTED now needs unanimity, and stops inheriting dispositions from entries that merely mention a commit

Two defects, both silencing the same three false fires, and it matters that they were fixed and verified **separately** — because either one alone would have made the board go quiet while leaving the other underneath.

The first is the unit. `_log_dispositions` maps a commit to the *set* of disposition kinds across all LOG entries naming it, and the signal fired where that set contained `not needed` and the always-loaded count rose. On a sixteen-item run every entry carries one hash, so a single item legitimately recording `not needed` — a script fix, a test repair — put that kind into the set while a sibling item authored a rule and correctly recorded `run`. The check reported a contradiction between two artifacts that agreed. It now fires only where **every** disposition naming the commit says `not needed`.

The second was found in the post-close tail and is worse-shaped. `b51d205` committed two files and its own entry records `run`; it was flagged because a *different* entry, belonging to `e5d169b` and saying so in its heading, described reproducing a test "against a detached checkout of `b51d205`". Hashes were matched anywhere in the entry, so a prose mention silently donated that entry's disposition to another commit. Entries in this project cite prior commits constantly. Attribution now reads the entry's **heading** only — the position the backfill writes and the one the entry's identity rests on.

Why both, when the unanimity rule alone silences all three: it silences `b51d205` for the wrong reason, and the misattribution survives underneath with its failure direction inverted. A future commit could inherit a `not needed` from an unrelated entry that merely names it, which under the new rule would *mask* a genuine contradiction rather than create a false one. Verified separately for exactly that reason: `b51d205` now resolves to `{run}` alone, so the prose mention no longer reaches it; `e5d169b` and `0ae69d6` resolve to `{run, not needed}` and are excluded by unanimity.

The cost is recorded rather than left to be discovered. A mixed run where one item genuinely authored a rule and wrongly recorded `not needed` now passes silently, because a sibling recorded `run`. That is a real loss of coverage, accepted against a check that would otherwise fire falsely at every large run — and a check that cries wolf gets skimmed past. The printed message was reworded to name that gap alongside the older one it already admitted: it still cannot tell an honest `run` from a dishonest one.

Keying the check on the LOG entry rather than the commit remains the correct shape and remains unbuildable: the count delta comes from a per-commit diff.

**Files touched:** `resources/rule_signals.py`

**Routed to Captures:** none

**Rule gate:** not needed — a detector correction; no rule authored and no always-loaded text changed.
