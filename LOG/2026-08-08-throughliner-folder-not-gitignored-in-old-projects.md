# [HASH] — This project's .gitignore gains .throughliner/ and FAQ/; the untrack step is deferred to the user

Built in the 2026-08-08 overnight blitz. Part 1 of the item's local repair shipped: `.throughliner/` and `FAQ/` added to this project's `.gitignore`, closing the gap /setup's scaffold step never reached here because /setup has not been re-run since those steps shipped (the general fix is [setup-as-migration-home]'s). Part 2 — untracking the already-committed `FAQ/faq.md` and `FAQ/index.md` — was the item's own explicit condition: it removes committed files from the repository and must not happen on an inference during an unattended run. **Departure note:** run overnight under the blitz departures, so rather than asking live, the deferred half was filed as [untrack-faq-needs-your-yes] so it stays tracked instead of living only in this entry. Nothing was deleted or untracked this session.

**Files touched:** .gitignore
**Routed to Captures:** [untrack-faq-needs-your-yes]
FAQ: not needed because the change is to this development project's own repo hygiene, invisible to consumers.
