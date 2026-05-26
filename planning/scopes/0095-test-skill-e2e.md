# 0095 — /test skill E2E validation

## Goal

End-to-end test of the `/test` skill and testing procedure (shipped in 0094) against a real project. Validate that a non-coder can invoke `/test` after a build, follow Claude's guided walkthrough for each pending test row, report a failure, and get walked through structured debugging — all without needing independent knowledge of what to check or how to diagnose.

Uses a burner app (Polite Fart Announcer or fresh scaffold) with a just-completed build that has pending User-verified TEST-LOG rows across multiple test types.

## Inputs

- `/test` skill and `plugin/docs/procedures/testing.md` — shipped by 0094.
- A burner app with at least one completed build batch and pending TEST-LOG rows. Ideally rows covering multiple test types (Look and click, Run and read at minimum). If 0088 has shipped by then, reuse that app's state; otherwise scaffold fresh via `/setup` + a quick build cycle.
- `research/e2e-greenfield-post-redesign.md` — prior E2E findings (if relevant app state exists).

## Outputs

1. **Updated or new research file** — `research/e2e-test-skill-validation.md` with findings.
2. **New scope files or BACKLOG open-question entries** for any issues found.
3. **After-build procedure update validation** — confirm the step 14 closing prompts correctly reference `/test` and the handoff is smooth.

## Test plan

### Happy path

1. Invoke `/test` in the burner app session after a build has shipped.
2. Confirm it loads the right TEST-LOG rows (User-verified, Status: blank).
3. Walk through a "Look and click" test — verify Claude expands the one-line description into actionable steps, tells the user what to look for, and defines what pass/fail looks like.
4. Report "Pass" on one test — verify the row updates correctly (Status, Confirmed Explicitly, Notes).
5. Walk through a "Run and read" test if present — verify Claude generates the exact command, explains what to look for in the output, and interprets the result with the user.

### Failure and debugging path

6. Deliberately report "Fail" on a test — verify Claude enters the debugging protocol rather than just recording the failure.
7. Confirm Claude asks structured questions (what did you see, what did you expect, etc.).
8. Confirm Claude suggests a diagnostic step appropriate to the test type.
9. Confirm the debugging session produces either a cause or a routable description for a new BACKLOG item.
10. Verify the TEST-LOG row captures the failure details in Notes.

### Edge cases

11. Invoke `/test` when no pending tests exist — confirm graceful exit message.
12. Invoke `/test` mid-build (if detectable) — confirm it doesn't run during the wrong phase.
13. User says "skip" or "I can't test this right now" — confirm partial progress is saved.

### Handoff validation

14. After `/test` completes, start a planning session — confirm the read-back step (planning procedure step 1) handles rows that `/test` already confirmed (depending on what 0094 decided about design decision #3).

## Success criteria

1. A non-coder (Alex) can complete the full `/test` flow without needing to ask "what should I check?" independently.
2. The debugging protocol produces useful output on at least one deliberate failure — not just "noted, moving on."
3. TEST-LOG state after `/test` is consistent with what the planning procedure expects at next session open.
4. No silent failures — every pending row is either addressed or explicitly deferred with a reason.

## Risks / dependencies

- **Hard dependency on 0094** — the `/test` skill and procedure must ship first.
- **Soft dependency on 0088** — if the build E2E has shipped, reuse its app state. If not, need a quick build cycle first, which adds setup time.
- **Risk:** the burner app may not have enough test-type variety. If all tests are "Look and click," the E2E won't validate "Run and read" or "Trigger and observe" guidance. May need to manually add TEST-LOG rows covering other types before testing.
- **Risk:** design decision #3 from 0094 (direct recording vs. deferred to planning) directly affects test plan step 14. If not resolved before this E2E, test both paths.
