# [HASH] — Rewrote CLAUDE.md's Model-target rule to the two-docset model (docset A frozen as the 4.8 fallback, docset B the active light 5-series docset)

Phase 1 of the Opus 5 work. Replaced CLAUDE.md's single-Opus-4.8 target (resolved 2026-06-15) with the two-docset model, recording the decision and its reasoning. Docset A — the current heavy docset, carrying the why-clauses 4.8 needs — is frozen as the known-good fallback so a bad migration can never strand the project with no working plugin (the user's non-negotiable); shipping this build *is* the freeze of A. Docset B — lighter, authored by subtraction from A — becomes the active docset the method evolves on, serving Fable 5 + Opus 5. session_start will pick B for the 5-series, A for 4.8, defaulting to A when the model field is absent. The fork it resolves: Opus 5 isn't "as fussy as 4.8" but fussy the opposite way (over-does, needs subtraction), and Fable 5 agrees, so the two 5-series models converge on one lighter docset — collapsing the old "N docsets" worry to two. Also recorded the no-regress authoring rule (B's lighter register must never be applied back to A) and that this is phase 1 of three (phase 2 authors B, phase 3 wires detection).

**Files touched:**
- CLAUDE.md — rewrote the "Model target" section

**Routed to Captures:** [handover-bundling-fights-one-at-a-time], [line-anchored-link-dead-in-desktop-app]
