# [HASH] — The revert-span sweep run: seven stale claims corrected, and a broken fetch path nobody had itemised

Captured by the user after `19ff11b` and widened on 2026-08-09 from SPEC-and-README-only to the whole doc set. The 2026-08-09 revert unwound 65 commits and nothing was audited afterwards.

**Method.** The item's own instruction was to establish the extent first rather than assume it. That meant grepping the retired vocabulary — the old model number, the retired docsets and documents, the retired section names, the retired setup fields, the retired queue markers — across SPEC, README, INSTALL, CLAUDE.md, `docs-b/`, the templates and the FAQ, then reading each hit to decide whether it was stale or correct in context. Several hits were correct and left alone: the old section names in `migrate-checklist.md` and `setup.md`'s conversion trigger name the format being converted *from*, and the one surviving mention of the retired behaviour doc is a historical note in frontmatter.

**What was actually wrong:**

- `README.md`'s Tested environment said Claude Opus 4.8 — the confirmed instance the item was filed on. Corrected to Opus 5 and Fable 5.
- **Four FAQ entries documented mechanisms that no longer exist**, and were rewritten rather than deleted: Batches and Captures became the two sections and the single move between them; the entry-organisation answer became headings, slugs and flavor tags in place of Build/Test/Audit subheadings; the pinned Red flags section became the marker riding the work, with uncleared/cleared replacing Open/Resolved/Accepted; and the Deferred tests section became deferred checks folding back into the queue as ordinary items. Each rewrite says plainly what it replaces, so a user with an older mental model can see what changed rather than quietly reading new text over an old memory.
- The /plan-/next-/done entry still said /next "picks the top batch and builds it" — corrected to the marker-bounded multi-item run.
- The **shipped** template's "Plan session here" entry documented a retired marker as live. Replaced with an entry naming both retired markers, what replaced each, and that an old queue carrying them can delete them. Index line and its anchor updated with it.
- `skill-nonspecific-rules.md` said "all three hooks parse" the work-item line — made wrong by this same run's Stop hook. Reworded.
- **A genuinely broken fetch path**, found by the sweep and itemised nowhere: `setup.md` told a migration to load `${CLAUDE_PLUGIN_ROOT}/docs/migrate-checklist.md`, where the folder is `docs-b/`. Every other reference in the corpus says `docs-b/`. That fetch would have failed on any migration that reached it — which is the whole conversion path for a project on an old queue format.

**Verified clean rather than assumed clean:** every `docs-b/*.md` cross-reference in the procedure docs and skills resolves to a file that exists, and no reference survives to `plugin-behaviour.md`, `AGENTS.md`, `authoring-heuristic.md` or `consistency-audit-plan.md` outside that one correct historical note.

**Not re-reported**, per the item's own exclusion list: [evict-claude-md-staleness], [session-start-cap-docstring-wrong], [claude-template-references-retired-test-flavor], and the show-first contradictions, which were built earlier in this same run.

**Why this stayed a correcting build rather than an `[audit]`,** confirmed in the doing: the work was volume-neutral — wrong text replaced with right text, no rules added — so a review pass that only reported findings would have added a round trip for nothing.

**One consequence for another item.** Four of the five stale entries [faq-backfill] names as its evidence were corrected here. That does not lift its hold, which is on the lifecycle design rather than on the staleness count, but it changes what remains of the job — captured as [faq-backfill-partly-overtaken] rather than left for a later session to rediscover.

**Files touched:**
- `README.md`, `FAQ/faq.md`, `FAQ/index.md`
- `plugin/si-plugin/templates/faq-template.md`, `faq-index-template.md`
- `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `setup.md`

**Routed to Captures:** [faq-backfill-partly-overtaken].

FAQ: updated — four entries rewritten and one shipped-template entry replaced; correcting the FAQ was part of this item's own scope rather than a sync obligation triggered by it.
