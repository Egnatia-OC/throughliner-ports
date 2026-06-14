# Build procedure

Execution procedure for build batches. Reached from next.md after pre-flight checks and scope lock are complete.

## Execute [SILENT]

Execute entry by entry.

### Build entries

For each:

1. Read any relevant existing code or context.
2. Make the changes.
3. Tick it in _build.md Progress: `- [x] entry description — done`

### Test entries

When the batch contains test entries (under a Test subheading), execution is verification, not file editing:

1. Read the test description to understand what's checked.
2. Run every test you can verify yourself: read code, run commands, inspect output, check file content. Only tests needing real human interaction (visual appearance, physical device behaviour, subjective judgment) go to the user.
3. Tick each in _build.md Progress, pass/fail:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
4. Accumulate results in Changes: what was checked, what passed, what failed.

**On test failure:**
- Isolated (one test, rest unaffected): note it, continue, route the fix to Captures at close.
- Fundamental (invalidates the batch premise or blocks remaining tests): stop, go to Course-correction below.

### Rules during build

Absolute regardless of entry type:

- Stay within the entries' described work. To touch something unrelated, say so first: "I need to also edit [file] because [reason]. Add to scope?" Wait for approval.
- REGISTRY.md is not build scope. /done handles registry updates after close.
- SPEC.md is read-only. Found a spec issue? Note it for /plan; don't fix now.
- Don't fix unrelated problems you notice. Note them for the queue.
- State regressions plainly. If something breaks, say so immediately. Don't silently fix or apologize — state the facts.

**Accumulate close notes** as you go — jot what changed in _build.md so /done needn't re-explore:
```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
```

## Scope management

### User raises something out of scope [PROMPT]

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first as a blockquote with a content-type lead-in (**Capture draft:**) for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume the build.

**Coherence exception:** Default is capture, per above. The exception is narrow and keyed to why-pipeline coherence: if the item would share the build's log entry and index line — per plugin-behaviour.md Index entries — and folding it in makes the batch easier to find later rather than harder, add it to _build.md as a new entry (appending any files it names to the `Files:` section) and continue. Evaluate against the coherence rules, not user convenience. When uncertain, capture.

### Scope grows during the build

If Claude discovers additional work is needed:

- **Minor** (one more file, small prerequisite): ask to add. Once approved, append the file to _build.md's `Files:` section before editing it — the scope-lock denies edits to unlisted files.
- **Significant** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

## Mid-build course-correction

### Claude discovers user-runnable testing is needed [PROMPT]

When Claude notices something will need user-runnable testing beyond the batch's Test section — visual check, physical-device behaviour, subjective judgment Claude can't verify:

1. Route the discovery to Captures in QUEUE.md as a future test-only batch. Draft the wording (what needs testing and why), show before writing per plugin-behaviour.md Captures.
2. Ask "anything else?" — repeat until no.
3. Resume the build.

Don't attempt the test inline. Don't extend the current batch's scope to include it.

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a false assumption, a missing dependency, an approach that isn't working:

1. **Stop building.** Don't push through a broken approach.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop an entry, add a prerequisite, change the approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable:
     1. Return the batch text to QUEUE.md under Batches. Placement is Claude's call per plugin-behaviour.md Dependency ownership — original position or top, by what was learned.
     2. Route any captures surfaced during the attempt to Captures as normal.
     3. Route the reshape direction to Captures, pointing at the batch slug. The trigger is mechanical: abort + batch returned + a reshape direction or learning the queue needs in conversation = capture needed. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the batch re-presents unchanged at the next /next.
     4. Tell the user to run /done. _build.md stays in place so /done's router still fires the build close-out — see done.md. Differences from a completed build: the LOG entry describes the attempt and why it was aborted, and the batch returns to QUEUE.md rather than disappearing into the log.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Context management

If context is running low, prefer in order:

1. **Finish and /done.** If most entries are ticked, push through. Short-term memory is enough.
2. **Close partial.** If significant work remains, /done what's ticked and requeue the rest. The next session picks up cleanly from _build.md and QUEUE.md.

## Completion [BRIEF, PROMPT]

When all entries are ticked:

1. Tell the user the build is complete.
2. Say: "Run /done to record this and commit, or tighten what's already built before closing." Tightening means refining done entries — not raising new work. Anything new routes through the existing paths: out-of-scope via Scope management above, thinking work via Captures. No chat summary of the changes — the LOG entry /done writes is the single session summary.

Do NOT delete _build.md yourself. That's /done's job.
