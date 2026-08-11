# [HASH] — The forward advisory states conditions, not counts [advisory-falsified-by-intervening-run]

Filed from a wind-down re-scan, approved by the user, observed live.

**What happened.** An advisory written at a /plan close said an item "sits ninth in the cleared region and cannot be scoped by a build, so a /next run clears the eight items ahead of it and then halts there." True when written. Between then and the next session a run shipped the items ahead of it, and by the time the advisory was read the item sat **first** — so a session trusting it expected eight items of runway that did not exist, when in fact a run would halt immediately having built nothing.

**Why it generalises rather than being one stale sentence.** An advisory is written at a close and consumed at the next /plan's opening, and the whole point of the interval is that work happens in it. Positions in the cleared region are precisely what a build run changes.

**What did not fail, which is what narrowed the fix.** The advisory's substance was right and useful: it identified the correct item, gave the correct reason, and named what to process alongside it. Only the positional claim rotted. So this is not an argument against advisories.

**Located precisely at processing, which moved the file and shrank the change.** The advisory is authored in `done.md`, not `done-plan.md` as the item first guessed, and its **template is already position-free** — it refers by slug and names no position. Every perishable claim was in the prose written beneath it. So nothing in the shipped mechanism was wrong; what was missing was a constraint on what that prose may assert.

**The rule: a condition stays true however the queue reorders; arithmetic against a snapshot does not.** Two alternatives rejected — re-deriving the advisory at read time is a mechanism where a wording constraint does the job, and barring advisories from naming anything specific would remove the substance that worked.

**Admission:** an amendment to an existing block, and a weak one in the good sense — it applies a principle already in force (queue position never encodes a relationship; cross-references are written as slugs) at a site that was missing it. The same shape as [lift-step-has-no-placement-rule], built in the same run.

**Files touched:** `plugin/si-plugin/docs-b/done.md`
**Routed to Captures:** none from this item
