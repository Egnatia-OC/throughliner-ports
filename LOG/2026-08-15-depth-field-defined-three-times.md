# [HASH] — The depth field's two downstream restatements evicted, leaving the definition at its authoring site

The field was defined three times: in `next.md`'s per-item completion step, again in `next-build.md`, and again in `done-build.md`. All three said the same thing — two values, short is the default, written at the tick rather than loosely during the build.

All three sites were read at processing rather than taken on the source audit's word, and the finding held exactly. `next.md` is the authoring site, where the field is actually written, and it keeps the full definition and its justification. `next-build.md`'s copy adds nothing the other two do not, so it is deleted outright — including its pointer back to `next.md`, since a build run has that doc open anyway and a pointer to an open document is not a pointer. `done-build.md`'s copy is cut to a reference.

What must survive a flat cut, and did: `done-build.md` keeps read-it-don't-judge-it, the never-judge-by-run-size clause, and the missing-field rule — that a ticked item with no depth field is read as short and noted at the close as a discipline slip. That last is the only place the absent-field case is handled at all, it fires at the close rather than at the tick, and it is genuinely that doc's own.

Three statements of one field is the drift shape this project fights: each copy is a chance for the values to diverge silently. The same judgment as the `done-plan.md` subtraction pass and the close sub-docs' routing step, applied consistently across all three builds in this run — a downstream copy survives only where it serves its own moment.

Rule gate: run — two restatements evicted. No rule authored or amended; the canonical statement is untouched and nothing moves to always-loaded.

FAQ: not needed because the depth field is internal bookkeeping in a working file the user never reads.

**Files touched:** `plugin/throughliner/docs-b/next-build.md`, `plugin/throughliner/docs-b/done-build.md`.

**Routed to Captures:** none.
