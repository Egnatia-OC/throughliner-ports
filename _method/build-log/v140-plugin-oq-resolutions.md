# v140 — 2026-05-29 — Plugin OQ resolutions: volunteered test results, carve-out snapshot, walkthrough pacing

**What shipped.** Three OQ resolutions from v135 deliberation implemented into plugin docs. `testing.md`: new "Volunteered results" subsection accepting specific per-row test reports (component name or row number + explicit status), skipping guided walkthrough for accepted rows. Defines valid confirmation format. `build.md`: new "Snapshot reflects the split" paragraph documenting that `active-build.md` shrinks after re-batching carve-out and `/sovclose` runs on the reduced snapshot. `universal-behaviour.md`: new "Guided test walkthrough pacing" bullet — one row per message during `/sovtest`, cowboy tests exempt. Doc-parity fix: added "cowboy test" to `VOCABULARY.md`.

**Decisions taken and why.** Placed the volunteered-results rule as a subsection within the walkthrough section (not a top-level section) — it's an exception to the walkthrough flow, not a parallel mechanism. Kept the walkthrough pacing rule as a separate bullet from the generic "walkthroughs one step at a time" rule in universal-behaviour.md because it adds the cowboy-test exemption, which is test-specific.

**Pivots and surprises.** None. Straightforward doc additions per batch scope.
