# [HASH] — The spec-sync gate stops describing a SPEC-trails-behaviour model

The /plan close's spec-sync gate carried a paragraph from the model that preceded
SPEC-leads. It said editing SPEC when a change was merely *decided* would make it
describe a product that does not exist yet — "a false SPEC, not a synced one" —
and that SPEC moves when the behaviour does.

That is now backwards. SPEC is read at build time: a run reads it once at the
start and each item is built against it. A sentence has to be there *first* for
that to mean anything, so SPEC leading the build is the architecture rather than a
defect in it, and the planning session writes the sentence with the user present.

The paragraph is repealed. In its place the gate says what it actually checks —
that every decision this session made had its SPEC sentence written at the
decision step — and states plainly that a SPEC sentence describing
decided-but-unbuilt behaviour is the designed lead, bounded by the cleared item
that builds it.

**The gate's purpose survives untouched**: it still stops a close where a
decision's sentence was never written. Only the model it explained was wrong.

**Reverting to SPEC-moves-with-behaviour was refused on the item**, since it
contradicts build-time SPEC reads — architecture already shipped and relied on.

**The grep the item required found only the repealed paragraph.** "false SPEC"
appears nowhere else across the plugin, FAQ, SPEC, CLAUDE.md, README or resources,
so nothing else needed rewording.

**Files touched:** `plugin/throughliner/docs/done-plan.md`.

**Routed to Captures:** none.

**Confirmed by this run's own close.** SPEC turned out to already carry the
sentences for the queue-reading model, the completion-ask carve-out and the date
anchor — all written at planning, ahead of the builds. The lead model was working;
the gate's text was the only thing describing it wrongly.

Rule gate: run — repeal inside done-plan.md's spec-sync gate, superseded by the lead model already operative in plan.md and SPEC; the gate's purpose survives; nothing else evicted.
