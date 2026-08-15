# b4de5bf — The migration recipe now refreshes whenever the format epoch is bumped

The recipe for converting an old-format project to the current shape drifts as the format keeps changing, and a stale recipe is worse than none. It had no maintenance trigger at all.

The user's original suggestion was to run the pass on every rezip. That was reversed at processing, on Claude's recommendation and her approval. A rezip fires whenever she wants to test something locally, so the overwhelming majority of rezips touch nothing to do with the document format — and a maintenance pass firing on unrelated work is the cry-wolf shape this project has repealed measures for twice. It gets learned past, and then the one rezip that did change the format is skimmed with the rest.

The format-epoch bump is the right trigger because it already fires on exactly the population that stales the recipe: builds that make an existing project's files structurally wrong. No new detection, no new judgment, and it rides a rule that already exists, so it spends no slot. Same family as the README-sync and SPEC-sync triggers, both of which work the same way.

The clause requires the LOG entry to say what was refreshed or why nothing needed refreshing. That is the required-artifact shape this project trusts: a silent omission becomes a visible one.

The migration-notes changelog is dropped rather than left open. It had ridden on this item since 2026-08-01, rehomed from a deleted item. It loses because git history and the recipe itself already hold that information, and a changelog nothing requires anyone to read is a second document needing the same maintenance this item exists to provide. Adding a maintenance burden to solve a maintenance burden is the shape to refuse; do not re-propose it without new evidence that the recipe alone is insufficient.

Rule gate: run — amends the existing `FORMAT_EPOCH` bump rule with one clause, with a named parent, spending no slot. One proposal refused in the same move: the changelog.

FAQ: not needed — the rule is host-only, in a file consumers do not carry, and it can never fire for them.

**Files touched:** `CLAUDE.md`.

**Routed to Captures:** none.
