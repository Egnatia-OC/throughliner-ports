# [HASH] — The "Plan session here" marker retired: six references removed, and the readiness line left as the only in-queue halt

**Decided at processing: retire, the user's call.** The fork was implement-or-retire, and the two directions cost very differently. Implementing meant a new halt in `next.md` plus a place-and-remove step in `plan.md`, which the method then maintains and tests forever. Retiring meant deleting the references.

**The reasoning is the method's own precedent.** This is the exact shape of the **push marker**, killed for being documented in two docs and honoured by none, with the finding recorded that a gate maintained in two places and honoured in none is worse than no gate at all. And the readiness line already does the job: work needing a planning session before it runs sits below the line, which is the gate the method actually maintains, tests and surfaces at every close. A second in-queue halt would rebuild the two-gates-bounding-one-run shape that `next.md` was deliberately collapsed to remove.

**The finding was worse than the capture stated, established by grep rather than inherited:** the marker appears in **no procedure doc in either docset** — not only docset B, but the frozen 4.8 docset A as well. So it was never implemented at any point, rather than implemented and lost.

Removed: the FAQ entry and its index line; this project's CLAUDE.md sentence calling it "the only in-queue halt marker", rewritten to say the readiness line is, and to record both retired siblings and why.

**One build nuance kept the change from overreaching.** The hook's `STRUCTURAL_LINE` regex is generic (`^---\s.*---$`) and legitimately covers the readiness marker too, so only the **comment** naming the planning-gate marker changed. Whether to narrow the regex was weighed at build and left alone, with the reasoning written into the comment: narrowing would make the orphaned-prose check stricter, which may be right, but would also flag any other structural line a queue legitimately grows, and nothing has established such lines don't exist.

**The honest cost, recorded so it is not discovered later as a surprise:** the readiness line marks *where* the boundary is and carries no *reason*. Retiring the marker gives up the ability to say why a particular point in the queue needs planning attention. Judged worth it, because a reason nothing acts on is a comment, and an item's own prose already carries reasons for the work it belongs to.

This project's own `FAQ/faq.md` and `FAQ/index.md` were deliberately left alone: [faq-backfill] replaces them wholesale from the templates, so an edit here would be overwritten there.

**One thing the decision did not weigh, filed rather than acted on:** deleting the FAQ entry leaves anyone whose queue still carries such a line with no answer anywhere — [retired-faq-entry-strands-legacy-users].

**Files touched:** `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`, `plugin/si-plugin/hooks/post_tool_use.py`, `CLAUDE.md`
**Routed to Captures:** [retired-faq-entry-strands-legacy-users]
**FAQ:** updated — the "Plan session here" entry and its index line deleted
