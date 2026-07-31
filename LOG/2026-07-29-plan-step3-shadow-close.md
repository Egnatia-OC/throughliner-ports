# 2f31148 — Consolidated /plan's Step 3 shadow close into the always-run /done close (done-plan.md)

plan.md's Step 3 "Close out" had accreted a second, near-/done-sized close — SPEC-sync, reorder both sections, position the cleared-to-run marker, hold-back check, place ready `[user]` work — that ran only when the user explicitly hit the /plan checkpoint's "close out" off-ramp. A session that ended any other way (or a bare /done) skipped that durable work, and it duplicated the "/done is THE close" boundary. The fix consolidates the durable work into done-plan.md, the one close that always runs (via /done) however a /plan session ends — mirroring how /next holds no close work and pushes everything to done-build.md.

Moved from plan Step 3 into done-plan.md: "Reorder both sections" (with the mechanical mover instructions) and "Position the cleared-to-run line", the latter absorbing hold-back-on-unverified-dependency, record-lift-condition, and place-ready-`[user]`-work-above-the-marker. They run after done-plan's Spec-sync gate and before the LOG entry/commit. Dropped plan Step 3's duplicate SPEC-sync — done-plan already hard-gates it. Shrank plan Step 3 to a stub pointing at the /done close.

Direction A (consolidate into the always-run close) was chosen over B (make plan Step 3 fire unconditionally): B isn't mechanically achievable — a skill has no guaranteed every-exit trigger of its own; a /plan session ends when the user runs /done, so the only always-runs moment is /done, and B collapses into A.

Scope grew by one file during the build: next.md's handover branch referenced "(plan.md Step 3)" for marker placement, which the move made stale — repointed to the /plan close (done-plan.md). Two in-plan.md Step-1 pointers were fixed the same way. SPEC's "Readiness line" and "Close-out reorder" were reworded to attribute positioning/reorder to the always-run /done close; the behaviour is unchanged, so this was a wording-honesty edit, not a product-truth change. "Lifting shelved work" was left as-is.

**Files touched:**
- plugin/si-plugin/docs/plan.md — shrank Step 3; fixed two Step-1 pointers
- plugin/si-plugin/docs/done-plan.md — absorbed reorder + cleared-to-run positioning (hold-back, lift-condition, place-`[user]`-work)
- plugin/si-plugin/docs/next.md — repointed handover-branch reference
- SPEC.md — reworded Readiness line & Close-out reorder

**Routed to Captures:** [next-run-boundary-judgment-datapoint]
