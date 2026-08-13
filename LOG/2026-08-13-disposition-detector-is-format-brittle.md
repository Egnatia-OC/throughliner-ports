# 340e7ef — Both disposition patterns tolerate a bolded label, changed in one edit

`resources/rule_signals.py`'s `DISPOSITION_RE` and `NOT_NEEDED_RE` now accept an
optionally-emphasised label. The code carries a comment saying they must always
change together, because the danger is specific and silent: make only the first
tolerant and a bolded `**Rule gate:** not needed` matches the disposition check
while still failing the not-needed check, so it is counted as **run**. That
inverts what the entry says, which is worse than today's failure, where a bolded
disposition is merely invisible. The item guessed `NOT_NEEDED_RE` might be
affected; the answer was worse than it guessed.

`CLAUDE.md`'s specimen now says explicitly to write the label plain, so the
authoring instinct is corrected rather than only forgiven at the reading end.

The item's own objection is answered rather than left open: a detector accepting
an optionally-emphasised label is not accepting "any line mentioning the phrase"
— the anchor, the label and the line position are unchanged, and emphasis is not
a different shape.

What settles it is the recurrence. The failure happened twice, the second time in
a session that had just read the sentence describing the brittleness and then
bolded every disposition it wrote. A rule depending on authors resisting an
instinct they demonstrably cannot resist is not a rule.

Board clean before and after: 0 of 4 signalling.

**Files touched:** `resources/rule_signals.py`, `CLAUDE.md`
**Routed to Captures:** none
