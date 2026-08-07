# [HASH] — Three retirements finished in live text, three inert artifacts deleted, one read before deleting

**The batch-type rule was deleted outright rather than corrected.** CLAUDE.md's "A new batch type touches four places" named `ALLOWED_SUBHEADINGS` — a constant existing nowhere in code, deleted from the lint on 2026-07-04 — plus retired batch types, and routed wiring at `docs/` paths. Batch types are retired, so there is nothing left for the rule to govern: a corrected version would be a rule about a thing that does not exist. Its lesson survives in the sibling immediately below it, the hook-enforced-format ripple-grep, which this same run generalised.

**Two retired nouns in live-loaded text.** `plan.md`'s "the user-only batch" became "the consolidated user-only question" — one phrase, in a doc every docset-B planning session loads. `session_start.py`'s three "deferred-test roll" comments now name the live mechanism, /plan's below-line revisit (done alongside [audit-hook-doc-reconciliation], which owned the same file).

**CLAUDE.md's wider "batch" usage was treated as a judgment at build, as the item directed, and deliberately not swept.** Two usages misdescribed current mechanics and were fixed: the `pre_tool_use` description (which now says the active run's file list in `_build.md`, and gains the scripted-write denial it never mentioned), and the self-hosting ordering section's opening sentence. The rest — "method docs" as a heading, "batch" in prose about past work — reads clearly in context, and a rename sweep would be a large diff nobody asked for.

**The three inert artifacts: deleted, the user's decision.** Git history keeps every one, and the LOG records what each was for.

- `FABLE-BRIEF.md` — **already gone**, deleted by the user by hand ("it seemed stale"), independently reaching the same conclusion. The item warned the build must not look for it; it greps clean, which is the expected result rather than a missed step.
- `resources/reader-test-workflow.js` — its expected criteria are the **inverse** of the current rules. A test asserting retired behaviour is worse than no test, because anyone running it would read the failures as the method being broken.
- `resources/queue-two-section-migration-recipe.md` — **read once before deleting**, per the relocate-before-removing rule, since this was the one with a real case for keeping. Checked against the shipped `migrate-checklist.md`: every judgment rule it holds is already there — the re-copy-don't-regenerate rule with its per-file discriminator, the drop-empty-placeholders rule, and the live validation record. Nothing needed carrying across, and that is a finding rather than an assumption. Its one genuinely stale element (a "by Claude" provenance label, from before provenance became default-AI-unmarked) was another reason not to preserve it.

**Files touched:** `CLAUDE.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/hooks/session_start.py`, and deletion of `resources/reader-test-workflow.js` and `resources/queue-two-section-migration-recipe.md`
**Routed to Captures:** none
