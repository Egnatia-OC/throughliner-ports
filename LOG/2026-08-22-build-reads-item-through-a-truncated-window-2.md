# 576506c — The close's per-item fetch is now the whole block, and a dispositioned question is transcribed rather than re-asked

A close once read queue items through a ~36-line window against items running past 50, and two wrong outputs followed — a false capture, and an FAQ question put to the user that the item's own text had already dispositioned the other way, costing an approved entry that was then reverted. The paging rule that would have caught it is shipped and did not fire, joining the recorded class; per that record the fix makes the fetch mechanical rather than the rule louder.

Built, both amendments in done-build.md's record-writing step: the fetch is specified as the item's whole block, from its `####` heading to the next heading or section end, from the pre-run QUEUE.md in git, with the hand-sized window named as the form that produced two wrong outputs; and where the fetched item's own text already dispositions a question the close is about to ask, the close transcribes the disposition instead — an ask that deliberately re-opens one names the recorded decision it re-opens. This session's own close used the whole-block form.

Tick: done, confirmed — the fetch instruction names the heading-to-heading form; the re-opening clause reads beside the step that asks; no other close doc contradicts either.

**Files touched:** plugin/throughliner/docs/done-build.md
**Routed to Captures:** none
Rule gate: run — two amendments to existing done-build.md provisions: the record-writing step's fetch gains the whole-block form, and the prior-decisions rule gains its close-site clause. Subordinate on both counts, nothing evicted. Failure evidence: two wrong outputs from one windowed read, one reaching the user.
FAQ: not needed because this is close mechanics; nothing a user does changes.
