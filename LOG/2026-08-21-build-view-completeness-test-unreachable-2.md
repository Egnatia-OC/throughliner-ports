# 7bc2c58 — The build view's completeness test counts only block-needing items, so equal is reachable

The generator's summary printed how many cleared items it found and how many carried a build block, and the epoch-4 migration test reads equal numbers as "migration complete". `[user]` and `[freeform]` items are cleared and neither is built from a block, so any project holding one could never read equal — and a number that can never match distinguishes nothing at the moment it is read.

The two counted numbers now cover block-needing flavors only. Cleared `[user]`/`[freeform]` items are reported separately on the same line as items that need none, so they are excluded rather than hidden.

Verified against this queue immediately after: 12 and 12. A test pins that a genuinely blockless build item still reads unequal, which is the half that matters — the fix must not make the check unfailable.

A prose-only fix stayed refused: the printed number would still have distinguished nothing.

`migrate-checklist.md`'s completeness test is reworded to match.

**Files touched:** plugin/throughliner/scripts/generate_build_view.py, plugin/throughliner/docs/migrate-checklist.md, resources/testing/test_build_view.py
**Routed to Captures:** none
Rule gate: not needed — a counting fix plus the matching wording; what the migration requires is unchanged.
