# /next procedure

You are executing the next piece of work from the queue. One batch at a time, scope-locked.

## Step 1: Pre-flight checks

Before starting:

1. **Active build check:** If _build.md exists, a build is already in progress. Offer to resume it (read _build.md for state) rather than starting a new one.

2. **Read QUEUE.md:** Find the top batch under "Batches."

3. **Blocker gate:** Scan for blockers that would force guessing:
   - Does the batch reference something in SPEC.md that doesn't exist? → Block. Run /plan first.
   - Are there unresolved questions in batches above the current one, or within the batch itself? → Surface them. Resolve or confirm they're independent. Captures-section questions don't block — they get processed in /plan — but if one clearly affects this batch, surface it.
   - Are there unconfirmed tests from a previous build? → Surface them. The user can confirm, skip, or defer.

4. **If no blockers:** Present the batch to the user: [BRIEF, PROMPT]
   - Batch title and all entry text from QUEUE.md
   - "Ready?" — if the user wants to change scope or reorder, route to /plan

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Create _build.md** with this structure:
```markdown
# Active Build

Entry: [copy the batch title and all entry text]

Progress:
[empty — ticked as entries complete]

Changes:
[empty — accumulated as entries complete]
```

2. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done Step 2.3 deletes _build.md after the build closes.

For test entries, the Progress section uses pass/fail format instead of entry ticking:
```
Progress:
- [x] Test description — ✓
- [x] Test description — ✗ (reason)
```

The _build.md file is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Build [SILENT]

Execute the work entry by entry.

### Build entries

For each build entry:

1. Read any relevant existing code or context.
2. Make the changes.
3. Tick it in _build.md's Progress section: `- [x] entry description — done`

### Test entries

When a batch contains test entries (under a Test subheading), execution is verification — not file editing:

1. Read the test description to understand what's being checked.
2. Run every test you can verify yourself: read code, run commands, inspect output, check file content. Only tests requiring real human interaction (visual appearance, physical device behaviour, subjective judgment) go to the user.
3. Tick each test in _build.md's Progress section using pass/fail format:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
4. Accumulate results in the Changes section: what was checked, what passed, what failed.

**On test failure:**
- Isolated failure (one test, rest of batch unaffected): note the failure, continue with remaining tests, route the fix to Captures at close.
- Fundamental failure (invalidates the batch premise or blocks remaining tests): stop and go to Step 5 (course-correction).

### Rules during build

These rules are absolute regardless of entry type:

- Stay within the work described by the entries. If you need to touch something unrelated, say so first: "I need to also edit [file] because [reason]. Add to scope?" Wait for approval.
- REGISTRY.md is not build scope. /done Step 1.5 handles all registry updates after the build closes.
- SPEC.md is read-only. If you find a spec issue, note it for /plan. Don't fix it now.
- Don't fix unrelated problems you notice. Note them for the queue.
- State regressions plainly. If something breaks or doesn't work as expected, say so immediately. Don't silently fix it or apologize — just state the facts.

**Accumulate close notes** as you go: for each file or test, jot what changed in _build.md so /done doesn't need to re-explore:
```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
```

## Step 4: Scope management

### User raises something out of scope [PROMPT]

When the user brings up something that isn't part of the current batch:

1. Route it to Captures in QUEUE.md.
2. Ask "anything else?" — repeat until the user says no.
3. Resume the build.

**Adding to scope instead:** If the user explicitly asks to add it to the current build rather than capturing it, confirm first: "This would expand the current build scope. Add it here, or capture it for a future batch?" If confirmed, add it to _build.md as a new entry and continue. This is a workaround, not the normal flow — captures keep builds focused and reasoning traceable.

### Scope grows during the build

If Claude discovers during the build that additional work is needed:

- **Minor addition** (one more file, small prerequisite): ask to add, continue if approved.
- **Significant growth** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

The sizing principle: right size = verification burden, not line count. A batch that touches 2 files but produces 15 things to test is too big. A batch that touches 8 files but has 3 observable behaviours is fine.

## Step 5: Mid-build course-correction [DISCUSS, PROMPT]

If something goes wrong during the build — an assumption turns out to be false, a dependency is missing, or the approach isn't working:

1. **Stop building.** Don't push through a broken approach.
2. **State the problem plainly.** What you expected, what actually happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop an entry, add a prerequisite, change the approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable, close what's done via /done and route the rest back to QUEUE.md for replanning.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Step 6: Context management

If the conversation is getting long and context is running low, prefer these options in order:

1. **Finish and /done.** If most entries are ticked, push through to completion. Short-term memory is enough.
2. **Close partial.** If significant work remains, /done what's ticked and requeue the rest. The next session picks up cleanly from _build.md and QUEUE.md state.
3. **Compact as last resort.** Only if you can't close the build and the remaining work would lose critical context. Tell the user: "Context is running low. I can compact, but I'll lose detail on [X]. Okay to proceed?"

Never compact silently. The user should know what's being traded away.

## Step 7: Completion [BRIEF, PROMPT]

When all entries are ticked:
1. Tell the user the build is complete.
2. Show what was done (the Changes section from _build.md).
3. Say: "Run /done to record this and commit, or keep adjusting. Run `/compact` or `/clear` first to keep context clean."

Do NOT delete _build.md yourself. That's /done's job.

## Rules

- One build at a time. Never start a second while _build.md exists.
- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory. It's the crash-recovery mechanism.
- If you're unsure about an implementation choice, ask. Don't guess and build wrong.
- Build and test entries follow the same procedure (pre-flight → lock → execute → close). Execution mechanics differ: [build] entries edit files, [test] entries verify behaviour. See Step 3 for each.
