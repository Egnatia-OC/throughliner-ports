# e5d169b — Conditional response-shape tags get one convention, applied at all thirteen sites

A step whose output shape depends on what it finds was being written three different ways. The convention is now `[TAG] when <condition>; [TAG] when <condition>` — every arm carries its own bracketed tag, and the condition sits outside the brackets. It is stated once, in `skill-nonspecific-rules.md`'s Response-shape tags section, with both failing shapes shown as counter-examples.

The grep the item demanded was run across all of `docs-b/` before settling anything, and it found more than the item's three sites: thirteen conditional headings across five documents. `done-audit.md`, `done-build.md` (twice) and `done.md` used a comma between correctly-tagged arms; `done-plan.md` (four) and `plan.md` (three) smuggled the prose inside the bracket, which is the substitution the tags exist to replace — there are five tags and a condition is not one of them. `done.md`'s Verify completion tagged only the loud arm, `[PROMPT] when unticked`, leaving the quiet one to be guessed; it now reads `[SILENT] when every item is ticked; [PROMPT] when any is not`.

Authoring the convention once against every site, rather than fixing three and retro-fitting later, is the hook-enforced-format tracing rule applied to a doc convention.

The second limb: `plan.md`'s skip-to-defer recommendation carried `[DISCUSS]` and no `[PROMPT]`. It recommends a fate decision — whether an item is sharpened and shelved — which is the user's call, and `[DISCUSS]` licenses length without stopping to wait. Only `[PROMPT]` does. This is the same failure class as [continue-read-as-approval], reached through a missing tag rather than a permissive clause.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `docs-b/plan.md`, `docs-b/done.md`, `docs-b/done-plan.md`, `docs-b/done-build.md`, `docs-b/done-audit.md`
**Routed to Captures:** none from this item
**Rule gate:** run — one rule admitted into the always-loaded corpus, the conditional-tag convention. It defines the syntax of a mechanism already stated at that site, and thirteen sites were guessing at it. It fires in all four skills, which is the file's own admission test. Nothing needed evicting to make room: the same session's eviction pass removed ~104 words from the same file, so this lands net-negative.
