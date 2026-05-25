# v44 — 2026-05-22 — Consumer-batch structure ideation + V49/V50 scoping

**What shipped.** Dev-internal ideation. (1) Interrogated which V-file scope sections propagate to consumer batches. Five landed (Goal, Outputs, Success criteria, Decisions to make this batch, Dependencies). Risks scoped out (degrades to hand-waving for non-coders). Re-framing: consumer batches skew V-file-sized because non-coders absorb ideas mid-stream. (2) ADR-style numbering (`NNNN-kebab-title.md`) confirmed as fix for V-numbering churn. Scoped as V49 (batch structure) then V50 (file-split + numbering). New OQ: red-flag/threat-class marker.

**Decisions.** V49 before V50 (structure first, file-split after). Retroactive rename in V50 (cleaner than partial cutover). No slash command for session creation. Risks section scoped out. Red-flag concern parked separately.

**Pivots.** Alex pushed back on "smaller consumer batches" — recalibrated to five sections. Reference manual "absorbs mid-stream ideation" section surfaced as V49 deliverable.

**Carried forward.** V49 and V50 await build. Red-flag/threat-class OQ awaits trigger.

