# [HASH] — Nineteen LOG headings repointed, twenty-one index placeholders resolved, and a close that commits after a partial staging failure stopped

Filed 2026-08-10 at the user's instruction after Claude surfaced it. Mixed authorship: Claude found the wrong hashes and the cause, the user instructed the filing, and the user agreed at processing that the cause-side fix belongs in this item rather than in a line of its own.

**The corrections.** All nineteen 2026-08-10 entry headings named `10d6474`, one commit past their own subject. Verified against git before touching anything: `94bba66` carried the work and `10d6474` added only the entry files. The replacement was made **in hash position only** — every one of the nineteen occurrences was on line 1 of its file, and a repo-wide grep confirms no body-prose occurrence was altered, which matters because at least one of these entries discusses hashes literally.

The index's twenty-one placeholders were resolved by checking which commit actually carried each session's work rather than by the oldest-containing rule: nineteen to `94bba66`, the 2026-08-10-plan-2 line to `bf44410`, and the 2026-08-11-plan line to `801c85a`.

**Two independent causes, and the second was found at this close rather than at processing.**

The first is the one the item recorded. The staging command for `94bba66` aborted partway when it hit a gitignored path, and the commit ran anyway, so the entry files were left out and were added separately in `10d6474`. The session-start backfill then resolved each placeholder to the oldest commit containing that entry title — exactly what its rule says to do — and with the files absent from `94bba66`, `10d6474` genuinely was the oldest. **The rule behaved correctly on inputs that were wrong.**

The second explains the index specifically, and the item's account did not have it. The backfill matches the literal token `[HASH]` in hash position. The index lines said `[UNFILLED]`. That token appears nowhere in any procedure doc, template or hook — a previous session invented it freehand — so those lines could never have been backfilled by any commit, correct staging or not. Nothing needs changing in the docs, which name the right token throughout; it is recorded so the two failures aren't collapsed into one.

**The cause-side fix replaces both options the item originally offered.** The item proposed either leaving the backfill rule alone as a one-off or adding same-commit verification to the close. Both address the symptom. The cause is in the item's own account: a close committed after its own staging step had partially failed. So `done.md`'s commit core now verifies that everything it meant to stage actually staged, and **stops rather than committing** when anything is missing. No second condition was added to the backfill rule, which is working. Wrong hashes were one visible consequence; entries missing from the commit they describe is the general one.

**Files touched:**
- `LOG/2026-08-10-*.md` (19 files) — heading hash corrected.
- `LOG/index.md` — all twenty-one placeholders resolved.
- `plugin/si-plugin/docs-b/done.md` — commit core gained step 5a, the partial-staging stop.

**Routed to Captures:** none.

FAQ: not needed because nothing user-facing changed — the corrections are to this project's own records, and the close-gate addition changes when a commit is refused, not anything a consumer reads.
