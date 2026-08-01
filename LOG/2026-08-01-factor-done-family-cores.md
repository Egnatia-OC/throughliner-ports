# b6f2344 — Factored four shared cores out of the done family into done.md; flavor docs reduced to deltas + pointers

The done-family docs each carried near-identical copies of four close-out mechanics. Lifted them into shared cores in done.md — Verify completion, Spec-sync gate, Staleness sweep, Recommend next, plus a shared LOG-entry template + approval frame under LOG entry files — and reduced each flavor doc to a pointer plus its per-flavor delta. Why-clauses were relocated to the shared home, never cut: 4.8 needs the rationale riding each rule, so the dedupe reclaims duplication without shedding the whys. This is the last real work on docset A before it freezes (the opus-5 gate). One judgment during the build: the spec-sync gate serves both build and plan closes with only a permission delta (build must add SPEC.md to the scope-locked Files list; plan edits in-session), so a single shared gate with two deltas was kept rather than two statements — the SDD-atomicity why is identical for both.

**Files touched:**
- plugin/si-plugin/docs/done.md — added four shared cores + shared LOG-entry template/approval frame
- plugin/si-plugin/docs/done-build.md — reduced 1.1, 1.3, 2.1, 2.2, Phase 3 to deltas + pointers
- plugin/si-plugin/docs/done-audit.md — reduced 1.1, 2.1, 2.2, Phase 3 to deltas + pointers
- plugin/si-plugin/docs/done-plan.md — reduced Spec-sync gate, LOG entry, Recommend next to deltas + pointers

**Routed to Captures:** none
