# Testing procedure — no-code method

Follow this procedure when the user invokes `/sovtest`. Guides non-coders through pending User-verified TEST-LOG rows one at a time, turning each Test Description into actionable steps and routing failures through structured debugging.

## Scope

`/sovtest` handles **User-verified rows only** — rows with `Verifier: User` and `Status:` blank (open). Claude-verified rows are already run and confirmed by `/sovclose`.

**Exception — unrunnable Claude-verified rows.** If a Claude-verified row wasn't completed by `/sovclose` (Status still blank), `/sovtest` may encounter it. Before guiding the user through it manually, explain why Claude couldn't auto-run it and **ask whether the user wants to walk through it manually or skip it**. Never silently hand off Claude's testing work to the user.

## First action — load state

1. `CLAUDE.md` — path block.
2. `MANIFEST.md` — component names for cross-referencing.
3. `TEST-LOG` — in folder mode (path block → `proxies/test-log.md`): read index, then the most recent per-session file. In single-file mode: read `TEST-LOG.md`.
4. Identify pending rows: `Verifier: User` with blank `Status`, or unrunnable Claude-verified rows with blank `Status`.

**No pending rows.** If every User-verified row already has a Status, say so and stop: "No pending tests — nothing to walk through."

**No test session.** If TEST-LOG has no rows at all, say so and stop: "No test session open. Run `/sovclose` after a build to create test rows."

## Walkthrough — one row at a time

**[SEQUENCE]** Walk pending rows in `#` order (lowest first). State the count at the start: "N tests to walk through. First:"

### Per row

1. **[BRIEF] Present the test.** State the row number, Component, Test Description, and Type. Plain English — no table formatting.

2. **[SEQUENCE] Guide by type.** Expand the Test Description into steps the user can follow:

   **Look and click:**
   - "Open [target — derive from Component and Test Description]."
   - "Do [the interaction the description names]."
   - "Look for [the expected result]."

   **Run and read:**
   - "Run this command: [derive from Test Description]."
   - "You should see [expected output]."
   - "Does the output match?"

   **Trigger and observe:**
   - "Set up [the condition — derive from Test Description]."
   - "Trigger [the event]."
   - "Watch for [the expected response]."

   **Generate and inspect:**
   - "Run [the generation step]."
   - "Open [the output file or artifact]."
   - "Check that [the expected content is present]."

   These are generic shapes. The specifics come from the Test Description and Component — adapt the steps to what the row actually says. If the Test Description is too vague to expand into steps, ask the user what the test means before guiding them.

3. **[PROMPT] Ask for outcome.** "Pass, Fail, or Skipped?"
   - Wait for this row's answer before moving on.

4. **Route the outcome.**

   **Pass:**
   - Update the row: `Status: Pass`, `Confirmed Explicitly: Yes (YYYY-MM-DD)`.
   - Move to next row.

   **Skipped:**
   - Ask: "Why skipped?" (reason required).
   - Update the row: `Status: Skipped`, `Confirmed Explicitly: Yes (YYYY-MM-DD)`, `Notes: [reason]`.
   - Move to next row.

   **Fail:**
   - Enter the debugging flow (below).
   - After debugging resolves, update the row: `Status: Fail`, `Confirmed Explicitly: Yes (YYYY-MM-DD)`, `Notes: [summary of what went wrong + BACKLOG batch reference if created]`.
   - Move to next row.

5. **Next row.** Repeat from step 1 for the next pending row.

## Debugging flow (on Fail)

Structured triage — not a full fix session.

1. **[PROMPT] Gather symptoms.** Ask: "What did you expect to see, and what did you see instead?"

2. **[BRIEF] Investigate.** Read relevant source code (from MANIFEST paths and the batch's Files: list). Form a hypothesis about the cause.

3. **[BRIEF] Propose diagnosis.** State the likely cause in plain English. If multiple possibilities, list them ranked by likelihood.

4. **[PROMPT] Confirm or correct.** Ask the user if the diagnosis matches what they observed.

5. **Route to BACKLOG.** Create a build batch in BACKLOG with:
   - Goal: fix the diagnosed issue (or investigate if unclear).
   - Context: what the user reported, what Claude found in code, the TEST-LOG row reference.
   - `Serves UX.md:` pointing at the relevant entry.

   If the cause is unclear despite investigation, the batch Goal should say "Investigate" and the context should include everything gathered so far plus a "needs investigation" note.

6. **[BRIEF] Confirm routing.** Tell the user: "Created BACKLOG batch [name] for the fix. Moving to the next test."

**No fixing inside `/sovtest`.** Debugging identifies and routes. Building fixes. Don't blur the boundary.

## Completion

After all rows are walked:

1. **[BRIEF] Summary.** State counts: N passed, N failed, N skipped. Name any BACKLOG batches created from failures.

2. **[PROMPT] Next action.** If failures created BACKLOG batches: "New fix batches are in BACKLOG. Run `/sovplan` when you're ready to prioritize them." If all passed: "All tests passed. Ready for your next planning session."

## What you must not do

- **Don't run tests yourself.** You're guiding, not executing. Exception: investigating code during debugging.
- **Don't fix failures.** Route to BACKLOG. Fixing is a build session.
- **Don't infer outcomes.** Every row needs the user's explicit answer.
- **Don't bulk-confirm.** If the user says "they all pass," push back: "I need each row confirmed individually. Next: row #NNN, [description] — Pass, Fail, or Skipped?"
- **Don't edit source-of-truth docs.** UX.md stays locked. Flag implications in the summary.
- **Don't silently hand off Claude-verified tests.** Ask consent first.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 85.*
