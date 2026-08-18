# [HASH] — the close-out gate gains a precondition, and the fix is smaller than either option the item offered

A session once named three items at the opening, processed them, and then offered to close with thirty-five items still unprocessed — reaching for the neutral end-of-queue gate, which is specified for the case where Unprocessed *empties*. Applied to a full queue it stops being neutral: it silently reclassifies waiting work as nothing left to do.

**The settlement is smaller than the two routes the item proposed, because what to do next is already specified.** `plan.md`'s checkpoint says that after every item you present the next item. Nothing was missing about the behaviour. What was missing is that the session took a subset the *user* named to be the length of the session.

So two clauses on statements that already exist. The end-of-queue gate gains a precondition — it may fire only where Unprocessed holds nothing but items skipped this session — and the ordering ask at the opening gains one clause: a subset the user names sets the order, not the session's length. With the gate unavailable, the only thing left to reach for is the checkpoint, which is the correct behaviour.

This is the third instance of one family, with [close-invites-same-session-next] and [plan-gates-say-close-out-for-a-retired-phase], both shipped — a close offered where continuing was better. That is what makes the evidence weightier than a single case, and it earned SPEC a matching sentence, written this session: a planning session never offers to stop while unprocessed work remains.

**Queue changes:** [subset-done-has-no-stated-shape] settled and cleared; SPEC gained the matching promise.
**Work processed:** kept — [subset-done-has-no-stated-shape].
