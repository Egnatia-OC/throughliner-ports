# [HASH] — setup.md stops claiming the always-loaded rules are never in force, and keeps both guards it restates

The redundancy audit flagged two passages in `setup.md` as duplicating the always-loaded rules — the plain-language guard and the one-question-per-message rule — and `setup.md` justified both by asserting that /setup runs before adoption, so those rules are not loaded. The always-loaded doc says the opposite: its rules *are* active for /setup's migration and top-up runs.

**Resolved from the hook rather than from the two documents.** `session_start.py` was read directly. Where a folder has no `SPEC.md` it returns early with a single message and never appends the rules directive; where the project is adopted, it appends it. So both documents are truthful about different runs. Neither describes behaviour wrongly. Each states its own case as though it were the only case, and that is the whole defect.

**The two restated guards are KEPT, which reverses the audit's provisional reading of its findings 16 and 17.** They must hold on the fresh-adoption run — the run where a brand-new non-coder meets the method for the first time and nothing else governs the output. Deleting them to remove duplication on the migration run would trade a real protection in the exposed case for a cosmetic saving in the safe one.

**What was genuinely wrong was one assertion in three places**, and all three were reworded: the frontmatter note, the no-tags paragraph, and the plain-language guard. Each now says the rules are absent on a fresh adoption and present on a migration or top-up run, while the guards themselves stay unconditional. A doc that guards only sometimes would first have to work out which run it is on, which is a worse thing to ask of it than the duplication.

**The no-tags decision stands and its stated reason did not.** Response-shape tags stay out of `setup.md`. The old reason — that they would be undefined tokens — is false on a migration run. The honest reason, now written, is that they are undefined on the fresh-adoption run, and one text cannot carry markers meaning something on one run and nothing on the other.

**Deliberately out of scope**, named so a later pass does not widen into it: the third passage the audit flagged conditionally, `setup.md`'s first work item carrying a "captured by you" credit. That is a provenance question, not a loading question.

**Files touched:** `plugin/throughliner/docs-b/setup.md`
**Routed to Captures:** none

Rule gate: not needed — no rule authored or amended. One false assertion about when the always-loaded rules load, corrected in three places; both restated guards left standing.
