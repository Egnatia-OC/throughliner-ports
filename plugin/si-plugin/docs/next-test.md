# Test procedure

Execution procedure for test-only batches. Reached from next.md after pre-flight checks and scope lock are complete.

## Execute [SILENT]

For each test entry:

1. Read the test description to understand what's checked.
2. Run every test you can verify yourself: read code, run commands, inspect output, check file content. Only tests needing real human interaction (visual appearance, physical device behaviour, subjective judgment) go to the user.
3. Tick each in _build.md Progress, pass/fail:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
4. Accumulate results in Changes: what was checked, what passed, what failed.

**On test failure:**
- Isolated (one test, rest unaffected): note it, continue, route the fix to Captures at close.
- Fundamental (invalidates the batch premise or blocks remaining tests): stop, go to Course-correction below.

### Rules during test

- Stay within the test entries' described scope. If a test reveals something unrelated, note it for the queue.
- SPEC.md is read-only.
- State regressions plainly. If something fails, say so immediately.

**Accumulate close notes** as you go:
```
Changes:
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
- [test] checked error handling path — ✗ (missing fallback for empty input)
```

## Scope management

### User raises something out of scope [PROMPT]

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first in a fenced code block for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume testing.

### Test surfaces unexpected scope

If a test reveals additional verification is needed beyond the batch's entries:

- **Minor** (one related check): ask to add, continue if approved.
- **Significant** (new test area, design uncertainty): note for the queue. Finish the scoped tests first.

## Course-correction

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a test is impossible to run as described, a prerequisite is missing, or the test batch's premise is invalid:

1. **Stop testing.** Don't push through a broken premise.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop a test, add a prerequisite, change the verification approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable:
     1. Return the batch text to QUEUE.md under Batches.
     2. Route any captures surfaced during the attempt to Captures as normal.
     3. Tell the user to run /done.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Context management

If context is running low, prefer in order:

1. **Finish and /done.** If most tests are ticked, push through.
2. **Close partial.** If significant tests remain, /done what's ticked and requeue the rest.

## Completion [BRIEF, PROMPT]

When all tests are ticked:

1. Tell the user testing is complete, with the pass/fail counts — failures were already stated plainly as they happened.
2. Say: "Run /done to record this and commit, or review what's already tested before closing." No chat summary of the results — the LOG entry /done writes is the single session summary.

Do NOT delete _build.md yourself. That's /done's job.
