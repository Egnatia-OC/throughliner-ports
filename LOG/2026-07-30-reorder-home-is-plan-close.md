# fda7b07 — done-plan.md: /plan-close reorder places `[user]` lines end-preferred

Implemented the placement half of the run-boundary fix in the /plan close, where reordering belongs (an execution skill like /next can't reorder, and the durable order is set at the /plan close). The "Reorder both sections" step's Processed rule now places `[user]` handover lines end-preferred, after contiguous blocks of build/write work, so a handover doesn't split an otherwise-unattended build run. Build-order stays the primary sort — a `[user]` line is not moved past a build item that genuinely depends on its outcome; end-preferred is the default only among items with no such ordering constraint. This pairs with the next.md non-termination change: /next no longer terminates at a `[user]` line, and this reorder is what keeps handovers from splitting the Claude block in the first place.

**Files touched:**
- plugin/si-plugin/docs/done-plan.md: Reorder both sections — Processed placement rule

**Routed to Captures:** none
