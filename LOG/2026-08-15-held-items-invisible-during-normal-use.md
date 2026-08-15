# [HASH] — The planning opening names each held item, what it waits on, and how long it has been held

A correctly held item is as invisible as a wrongly held one. /next presents the cleared region and builds from it; the held region is read at /plan's below-the-line revisit, which is deliberately silent while an item is still blocked. So a user who runs /next and /done, and doesn't sit through a revisit, has no moment where held work is named. In a consumer project that meant someone asking why a feature "isn't queued" when it was queued, fully designed, and held for a good reason. Here it meant four Discord posts sitting held while the user's own post never went out, unnoticed for a day.

What ships is a named line, not a count — and this session was the evidence for the distinction. The opening *did* report four items held, because `session_start` computes the number at every start, and it still read as background. What it could not say was that the chain had been stuck since the 14th and that releasing it needed one word from her. A bare count is background; "held since the 14th, waiting on you" is not.

The held-since date comes from `queue_digest.py`'s existing git pass, which already walks QUEUE.md's whole patch history to date each slug. **Attribution is partial and the code says so.** With no diff context, a hold line can be tied to an item only when the two were added together — the ordinary case, since an item is normally written already held — so an item that was cleared and later held by a line added on its own gets no date and prints none. A missing date reads as "not known", never "not held". Widening the git pass or guessing were both rejected in favour of printing only what is known and stating the limit in the doc and the FAQ.

This is stated as separate from the below-line revisit's silence, so a later session does not read the two as contradicting: the revisit's silence is about the *lift* question, and this is about the user knowing the work exists. It is not in /next, on the user's decision and her reason — nothing surfaced during a build is actionable there, so it would be per-run noise on every run.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs-b/plan.md`, `resources/testing/test_queue_digest.py`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to Step 1's existing enumeration of what the opening narration surfaces, adding one element to a list that already holds five. Failure evidence is two independent instances in two different projects. Question four of the admission test is answered by the mechanism carrying the work: the count already exists in `session_start` and the per-item detail is computed by the digest, so the rule only has to say the line is spoken. **Nothing is evicted; this is a net addition of one narration element.**

FAQ: updated — new entry "The planning session told me some work is 'being held'. Do I need to do something?"
