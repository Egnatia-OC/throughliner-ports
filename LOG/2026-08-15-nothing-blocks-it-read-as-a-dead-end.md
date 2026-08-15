# b4de5bf — The work-cycle block now says processing a capture is how held work gets released

The user has given this correction five to ten times in about a month, and her words at processing were the design: this is solvable by an addition to the build cycle description — Claude needs to know that in /plan, not only are captures processed, but items under the line get lifted, and the how is that we process the capture that blocks that item, thus unblocking it; and a capture does not have to hold the Magna Carta, it can literally be "process this to unblock X".

The rule was already shipped in two places and was not the problem. `plan.md`'s keep-step says to write the blocker into Unprocessed first if it is not already a queue item. The failure is that a session never arrives from the placement side: it arrives holding a problem, asks whether below-the-line is available, concludes "nothing blocks this, so that route is closed", and starts designing a new mechanism instead. The rule sits one step past where the decision is actually made.

So the fix is upstream of every firing site. The work-cycle block is orientation, read at every skill opening, and it is where a session forms its model of what /plan does. That model said /plan processes captures — keep or delete — and said nothing about lifting held work, so a capture was never a thing whose processing releases other work. Amending the model reaches the question "what capture would unblock this?" before a session has ruled the route out.

The second limb matters at least as much. Every recorded failure involves a session hunting for a blocker weighty enough to look like a real item, finding nothing, and closing the route. Saying plainly that a capture may be a single line whose whole job is to unblock something removes the bar that produces that conclusion. It does not license placeholders: the manufactured item must still be real work.

The second recorded instance is the sharper evidence and it is why this was not answered by restating the rule again. A session that had read this very item in full the same day, and applied the chaining mechanism correctly to three of four items, hit the fourth, found no existing item to name, said in terms that no honest blocker was available, and mis-cited the placeholder-misuse warning as the reason — a warning that says a manufactured blocker must be real work, not that manufacturing one is forbidden. The guard clause was read as the rule.

`plan.md`'s keep-step clause was read in full before deciding whether it is now a duplicate, as the item required rather than assumed. It is kept: it is the operative instruction at the moment of writing, while the amendment is the model that makes a session look for it.

Rule gate: run — amends the work-cycle block's step 1 and the Captures section in `skill-nonspecific-rules.md`. Admitted as an amendment with a named parent, so no slot is spent and nothing is evicted. Escalation to a hook was refused: whether a session should manufacture a blocker is a judgment about work that does not yet exist.

FAQ: not needed because this changes how Claude reasons at a planning step, and leaves every action the user takes unchanged.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none.
