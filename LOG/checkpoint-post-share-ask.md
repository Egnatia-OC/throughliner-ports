# [HASH] — /plan capture loop ends on the ask; clear park/drop recommend merges into the interview close

Two roughnesses in /plan's capture loop, both about turn shape, fixed in plan.md.

(1) End on the ask. The first capture's presentation and each per-item checkpoint ended the message on a raw verbatim block, which reads as Claude stopping mid-thought with nothing handing the decision back. The earlier [verbatim-at-checkpoint] decision put the verbatim last on purpose, so the turn boundary separates the item from the next turn's analysis — but the message still needs a landing. Now the checkpoint leads with the next capture's verbatim and closes on the three off-ramps as the final, bold ask (the off-ramps moved below the verbatim; the offer-above shape was dropped), and the first-item presentation ends its quote message on a brief, bold prompt inviting the user to continue. Both keep the quote-as-its-own-beat and the confirm-against-the-file re-read.

(2) Don't split a clear park/drop recommend across turns. When Claude already has a clear park or drop lean by the end of the interview, it used to close with a bare "anything to add?" and then re-state the recommendation in a separate turn — naming the route twice with a content-free exchange between. Now a clear park/drop lean merges its recommendation into the exposition-closing turn as one combined, bold ask ("…my recommendation is park; anything you'd change, or shall I park it?"). The standalone recommend-and-wait stays the fallback for an unclear lean. Promote's fold-to-draft (its draft is the safety net) and park/drop's terminal-approval requirement are both preserved — park and drop can't fold to the action, but their approval doesn't need its own separate turn.

This refines the shipped [verbatim-at-checkpoint] decision rather than reversing it: the verbatim still lands on its own beat ahead of analysis; what changed is that the message now closes on the ask instead of the raw quote.

**Files touched:**
- plugin/si-plugin/docs/plan.md

**Routed to Captures:** none
