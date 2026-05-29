# v136 — 2026-05-29 — Dev-side rules reconciliation (batch 0136)

**What shipped.** Prose equivalents of 10 plugin behavioural rules added to the dev-side method, plus 2 contradiction resolutions. session-protocol.md gained: OQ blocker check (step 4b), mid-session rules subsection (no stealth fixes, no unplanned refactoring with carve-outs, compact nudge), session handoff protocol (new section), close-is-mandatory statement, and red-flag routing in the idea sweep. CLAUDE.md gained: adherence-drop diagnostic, proactive research, make-edits-directly rule, and command-execution clarification. Reconciliation map: 12 checkboxes ticked (G01–G10, C03, C04).

**Decisions taken and why.** Red-flag routing adapted for dev context — no separate Red flags section in dev BACKLOG; instead routes to `[SECURITY]`-marked batches or OQs. Session handoff placed between session-middle and session-close as a standalone section rather than a subsection of either. C04 resolved by adding a new "Command execution" section rather than modifying the existing "My experience level" section — keeps the two concerns (Alex's experience vs. Claude's execution model) separate.

**Pivots and surprises.** None. All 12 items mapped cleanly to dev-side prose. The lighter-close idea sweep didn't need editing — it already references "same triage as implementation close step 4."
