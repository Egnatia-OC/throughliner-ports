# 08c885b — The INBOX commit question dropped in favour of ignoring it unconditionally, on both setup paths

This item carried a red flag, cleared at processing on 2026-08-11. It is recorded here as carried and cleared; the substantive clearing record was written at that /plan close.

Mixed authorship. The Understudy project reported the defect and suggested adding the question to Step 2C; the user widened it to cover every project and supplied the reasoning that decided the design; the file-level scoping is Claude's.

**What was wrong.** `setup.md` Step 2 created the `INBOX/` folder and then asked once whether messages should be committed. Step 2C — the migration path — said to check each doc and folder from Step 2's scaffold list and create what was missing. It copied the folder and left the question behind, so a migrated project ended up with a mailbox and no decision recorded. Understudy hit exactly this migrating from 1.11.0 to 1.20.0-test4, and this project had silently migrated into the same gap.

**The design: the question is dropped, not carried across.** Both paths now write `INBOX/` into `.gitignore` and say so in one line. The user's reasoning, which is what settled it: anything read from the INBOX enters the project as a capture or a work item and emerges through processing as this project's own shown work, so the mailbox itself is leftover comms until cleared. Claude's supporting argument was the mechanic that reinforces it — a read message is *moved to `INBOX/archive/`*, not deleted, so an un-ignored mailbox accumulates another project's raw text in the repository forever, after its useful content has already been carried into the queue in this project's own words. And the safe outcome must not depend on a question being asked, because a question is skippable and this one was skipped.

**The rejected alternative, kept so it is not re-proposed.** Understudy's own suggestion — add the question to Step 2C, conditional on no INBOX decision being recorded — is the smaller change. It loses because it preserves a question whose skippability is the whole defect.

**The structural half, which is the general failure the report only instanced.** Step 2C restored Step 2's missing *files* and never re-ran the *decisions* attached to them. A second instance was found by reading the doc rather than inferred: Step 2 requires `.gitignore` to carry a `.throughliner/` entry, and under 2C an existing `.gitignore` counts as "exists → skip", so a migrated project could keep a `.gitignore` that never gained that line either. Step 2C therefore gained a settings-reconciliation step with those two as its current members.

**The case that is surfaced rather than papered over.** Adding an ignore line does not untrack files already committed and cannot remove anything from history. Where a migrating project has INBOX files in git history, 2C says so plainly instead of writing the line and implying the mail is now private — the same never-overstate-the-gate rule the scrub checklist holds to.

**Files touched:**
- `plugin/si-plugin/docs-b/setup.md` — Step 2's INBOX block rewritten; new Step 2C step 1b (settings reconciliation, and the already-committed-history disclosure); the "one settings question" note at the discovery step corrected to say there is none.
- `SPEC.md` — the Cross-project INBOX paragraph's closing sentence replaced.
- `FAQ/faq.md`, `FAQ/index.md` — new entry, "Why is my INBOX folder ignored by git, and can I change that?"

**Routed to Captures:** none.

FAQ: updated — new entry "Why is my INBOX folder ignored by git, and can I change that?"
