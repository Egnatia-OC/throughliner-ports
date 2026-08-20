# 8330209 — the shipped render rule already answers the wrapping fences and stops one sentence short

The capture instructed the processing session to check a sibling item first, and that instruction is what caught the thing. [fences-wrap-so-prose-rule-reason-is-false] was filed 2026-08-07, grew to roughly 1,500 words, and has left the queue — it survives only as a line in a length-growth research file. Its subject was a prose rule whose stated *reason* was false, an argument about a justification rather than about what Claude emits, so there was no fold target and the capture's own suspicion about that was right.

The stronger finding is that the shipped rule already covers this. The always-loaded render rule states what a fence is *for*: a paste target, or content whose exact characters are the substance — code, shell commands. A labelled two-column layout is neither; it is explanation wearing a fence. So the block that broke on Alex's display, where the right-hand column wrapped under the left and half the rungs appeared to have no title, was already outside the rule. What the rule never says is that using a fence for anything else is wrong, and the procedure docs model the wrong shape at scale, which is why it recurs.

The remedy is one clause on the inline-forming block: structured explanation shown to the user goes one item per line, never in aligned columns. Reformatting the procedure docs is refused on the item's own reasoning — those blocks are read by Claude in a wide view and work there, so rewriting them would fix the half that is not broken. The scope is output and never documents, which is the same split reached independently by [slug-never-explained-to-the-user] hours later; both entries record it and neither invented it alone.

Evidence is thin by count — one clear instance — and carries on cost rather than weight: the failure is visible to the user, wastes a whole message, and the fix is a sentence. A hook was considered and refused, because nothing mechanical reads Claude's chat output.

**Queue changes:** [two-column-fences-wrap-unreadably] kept into Processed, placed ahead of the restyle passes so the subordination lens meets the clause as part of the file.

**Work processed:** kept — [two-column-fences-wrap-unreadably]. Deleted — none.
