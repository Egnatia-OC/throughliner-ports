# [HASH] — The board now separates reports from signals, and CLAUDE.md's account of it is no longer wrong in two directions

The board described itself wrongly in two places at once, and the two errors pointed opposite ways. Its printed header read "N of 6 signalling" over a board where only four entries could signal at all — MEASURED and AUDITED both lost their trigger when the rule-corpus ceiling was removed, and had been carrying a hard-coded `firing: False` ever since. Meanwhile CLAUDE.md's always-loaded description called it "five independent signals" and named five, omitting CONTRADICTED entirely. The header over-counted what was watched; the prose under-counted what existed.

The printed output now groups the two classes under their own headings — reports, which measure and never fire, then signals, which do — and the header counts signals only. The permanently-False `firing` key is gone from both reports and replaced by an explicit `kind: "report"`; a field that always reads False looks meaningful and is not. Header now reads "0 of 4 signalling".

CLAUDE.md's description was rewritten to six entries in two classes, naming all six, and it now states the reports-versus-signals distinction so the count stays meaningful as entries are added. Its stale gloss on MEASURED — "rule-statement count against the ceiling" — went with it, since the ceiling was removed. The "five independent triggers" phrasing in the why-a-board paragraph was made count-free rather than corrected to six, so it cannot go stale the same way again.

Two things were established rather than assumed. `session_start.py` consumes the board by filtering output lines for `[FIRING]` and never reads the header, so reshaping it cannot change what a session sees — confirmed at the filtering line itself. And the three surviving `firing: False` values in the file are error paths on genuine signals, where git was unavailable and the signal could not compute; those are correct and were left.

Doing nothing was weighed on the honest ground that both message bodies already say plainly that neither fires. It lost because the header is the line most readings stop at, so the inaccuracy sat exactly where it did the most work — and this project's own standard, written about this very board, is that a check which over-claims makes the corpus look guarded when it is only partly guarded.

**Files touched:** `resources/rule_signals.py`, `CLAUDE.md`

**Routed to Captures:** none

**Rule gate:** not needed — a reporting-accuracy correction to a host-only script and to this project's description of it. No rule authored; the always-loaded consumer text gained no obligation.
