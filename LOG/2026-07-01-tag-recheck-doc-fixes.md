# 08823b6 — Build [tag-recheck-doc-fixes]: three procedure-doc fixes from the 2026-06-29 tag-placement recheck + a SPEC sync

Three low-risk authoring tweaks surfaced by the `[full-tag-placement-recheck]` audit, batched by shared origin and kind.

(1) **Readiness-line narration was doubled and over-mandated.** The line was narrated at the /plan close (plan.md Step 4) and again at the /done-plan close (done-plan.md), and both mandated narrating every close even when the line hadn't moved — cutting against the method's anti-nag principle. Fixed to narrate-on-move, silent-when-unmoved, mirroring the sibling dependency-graph check that stays silent when coherent. plan.md Step 4 now narrates only when the line actually moves this close and confirms silently otherwise; its tag became `[SILENT when its placement is unchanged; BRIEF when it moves]`. done-plan.md's step confirms silently when placement is already correct (the normal case, since /plan just positioned it — restating would say the same boundary twice) and surfaces only when it had to fix placement; tag `[SILENT when placement is correct; BRIEF when you fix it]`. SPEC's readiness-line sentence softened from "narrates where it sits" (every close) to narrate-on-move / silent-when-unmoved, keeping SPEC in sync in the same batch.

(2) **Dependency-tracing rules preached "show the shape" but carried no exemplar** while their section-neighbours do. Added the same one-line trace-evidence exemplar to plan.md Step 3's "Trace dependencies" ("Record where you traced …") and to plugin-behaviour.md's Dependency tracing "Record the trace evidence" obligation — "Traced against next-build.md's scope-lock step and SPEC's scope paragraph; producer is [scope-lock-core] (shipped); no shared primitive with other queued batches."

(3) **done-freeform.md Phase 3 was the odd one out** among the four done-* docs — its siblings all state the capture-overlap scan result either way (clean case a plain assessment, not a hedge) and it didn't. Aligned its Phase 3 scan sentence to the done-build.md wording verbatim in shape.

Fixes (2) and (3) are self-verifying at build via a read (the exemplars are present; done-freeform Phase 3 now matches its siblings). Fix (1)'s live behaviour — a /plan close confirms the readiness line silently when unchanged and narrates only on move, and a /plan→/done flow no longer states the boundary twice — is host-side, deferred to observation after push + reinstall.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/done-plan.md
- SPEC.md
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/done-freeform.md

**Routed to Captures:** none
