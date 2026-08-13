# 340e7ef — A Claude-raised capture in /plan asks once: file it, or work it now?

Two failures in the same paragraph of `plan.md`, which is why they were one item.
The user-raised branch had dropped its *anything else to add first?* clause; it is
restored and marked as not optional, since it is the clause that stops a user's
idea being closed off before they have finished the thought. The Claude-raised
branch had no offer at all, so the only scripted path was to file and then
separately ask whether to process — a two-step where one question would do, and
one that defaults to filing when the answer is often "deal with it now".

The user's words: *"you should be able to ask me 'file it or just process it
now?'"* The design is Claude's.

Nothing had to change mechanically, which is what made this cheap. The direct
route already exists — an item that comes out of /plan discussion and is kept is
authored straight into Processed. What was missing was the offer.

The anything-else clause belongs to the user-raised branch only. On a
Claude-raised item the user was not mid-thought, so there is nothing of theirs to
invite, and asking would be the soliciting the always-loaded rule bars. That rule
is not reversed: it stops Claude soliciting *further* captures off the back of its
own, and this offer disposes of the one thing already raised.

Nor does it erode write-first, and the text says so rather than leaving it to be
argued later. Both branches write; the question decides only where. Where
work-it-now lands the item in Processed in the same turn, the exposure is
identical, so filing first is not the safer order either.

`skill-nonspecific-rules.md` gained the one-clause carve-out the consistency check
owed — matching the sentence already there for the user-raised offer, not a
/plan-only procedure in the always-loaded file.

Rule gate: run — admitted as an amendment to the existing process-now offer.

FAQ: not needed because the new question is plain English and answers itself.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`,
`plugin/si-plugin/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none
