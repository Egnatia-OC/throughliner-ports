# /next procedure

You are executing the next piece of work from the queue. One batch at a time, scope-locked.

## Step 1: Pre-flight checks

Before starting:

1. **Backfill LOG hashes:** [BRIEF] Scan `LOG/log.md` and `LOG/index.md` for `[HASH]` placeholders. For each, find the hash of the commit that introduced the entry (e.g. `git log --diff-filter=A --pretty=%h -- LOG/log.md` walked top-down, or by blame) and replace `[HASH]` in place. No separate commit — the working-tree edit folds into whatever commit this session later makes. If nothing to backfill, no output.

2. **Active build check:** [SILENT] If _build.md exists, a build is already in progress. Offer to resume it (read _build.md for state) rather than starting a new one. If _build.md does not exist, move on — no output either way.

3. **Read QUEUE.md:** Find the top batch under "Batches."

4. **Blocker gate:** Scan for blockers that would force guessing:
   - Does the batch reference something in SPEC.md that doesn't exist? → Block. Run /plan first.
   - Are there unresolved questions in batches above the current one, or within the batch itself? → Surface them. Resolve or confirm they're independent. Captures-section questions don't block — they get processed in /plan — but if one clearly affects this batch, surface it.
   - Scan Captures for items (ideas or questions) relevant to the top batch. → Flag any that contradict, invalidate, or would benefit the batch if incorporated first. Recommend switching to /plan if any are found.
   - Unpark-candidate scan (per plugin-behaviour.md Dependency ownership Unpark watch). → Any parked item newly unblocked by work that's landed since? Surface and recommend /plan first if any are found.
   - Stale-batch scan (per plugin-behaviour.md Dependency ownership Staleness watch). → Any batch or capture stale enough that surrounding code or rules have moved past it? Surface and recommend /plan first if any are found.
   - Are there unconfirmed tests from a previous build? → Surface them. The user can confirm, skip, or defer.

5. **If no blockers:** Present the batch to the user: [BRIEF, PROMPT]
   - Batch title, a one-line gist synthesized from the rationale, and entry counts (build / test / audit). Don't re-render the full entry text — the user just wrote it in QUEUE.md and can open it anytime; the full text moves into _build.md once they confirm.
   - "Ready?" — if the user wants to change scope or reorder, route to /plan

6. **Branch on batch type:** After the user confirms, route by the subheadings present in the batch:
   - **Build batches** (Build subheading, optionally with Test) → continue to Step 2 below.
   - **Test-only batches** (Test subheading, no Build) → continue to Step 2 below; Step 3 handles test entries as verification work.
   - **Audit batches** (Audit subheading) → jump to the **Audit procedure** section at the end of this doc. Audit batches don't edit files; their close shape is different.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** from the batch title and rationale, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the same shape /done will write to LOG/index.md at close — pre-generating it here makes it reusable instead of regenerated. If the build runs as planned, /done reuses it verbatim; if scope shifts during the build, /done re-authors against the same rule.

2. **Create _build.md** with this structure:
```markdown
# Active Build

Entry: [copy the batch title and all entry text]

Index entry candidate: [the pre-generated entry from sub-step 1]

Progress:
[empty — ticked as entries complete]

Changes:
[empty — accumulated as entries complete]
```

3. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done Step 2.3 deletes _build.md after the build closes.

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

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first and show it in a fenced code block for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until the user says no.
3. Resume the build.

**Adding to scope instead:** If the user explicitly asks to add it to the current build rather than capturing it, confirm first: "This would expand the current build scope. Add it here, or capture it for a future batch?" If confirmed, add it to _build.md as a new entry and continue. This is a workaround, not the normal flow — captures keep builds focused and reasoning traceable.

### Scope grows during the build

If Claude discovers during the build that additional work is needed:

- **Minor addition** (one more file, small prerequisite): ask to add, continue if approved.
- **Significant growth** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

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

## Step 7: Completion [BRIEF, PROMPT]

When all entries are ticked:
1. Tell the user the build is complete.
2. Show what was done (the Changes section from _build.md).
3. Say: "Run /done to record this and commit, or keep adjusting."

Do NOT delete _build.md yourself. That's /done's job.

## Audit procedure

For audit batches only. Reached from Step 1.6 when the batch carries an Audit subheading. The shape audits actually need is read-many-propose-many — systematic read of the target, then disposition of findings one at a time. No file edits land directly; everything routes through Captures so /plan can convert findings into normal batches with the usual dialogue.

1. **Lock scope** [SILENT] — Create _build.md the same way Step 2 does (entry text + pre-generated index entry candidate), and remove the batch from QUEUE.md. The Progress section tracks findings rather than file edits:
```
Progress:
- [x] Finding description — captured
- [x] Finding description — dropped
```

2. **Read the target systematically against the criteria** [SILENT] — Open every file named by the target. Apply the criteria pass by pass — one criterion across the whole target, then the next, rather than mixing criteria per file. Don't skim; the value of an audit is reading what's actually there. Accumulate observations in _build.md's Changes section as you go, with file:line references so the user can verify each one.

3. **Compile findings** [SILENT] — Once the read is complete, group the observations into discrete findings. One finding per actionable change. Phrase each as what was observed + why it matters — the same shape a capture takes, since that's where findings will land.

4. **Present findings one at a time** [SEQUENCE, PROMPT] — State the count upfront ("N findings. First: ..."). For each finding: show the observation, the file:line reference, and why it matters. Wait for the user's call — **capture** or **drop**. Don't preview upcoming findings.

5. **Route approved findings to Captures** — For each "capture" disposition, draft the capture wording in a fenced code block for approval, per plugin-behaviour.md (Captures + approval-time outputs). Once approved, append to Captures in QUEUE.md. Tick the finding in _build.md's Progress section as `captured` or `dropped`.

6. **Close** [BRIEF, PROMPT] — When all findings are disposed, tell the user the audit is complete and show what was routed. Say: "Run /done to record this and commit, or keep reviewing. Run `/clear` first to keep context clean." /done writes the LOG entry (audits get a normal entry — the "files touched" line names the target docs that were read, and the routed captures get listed) and commits the _build.md deletion plus the QUEUE.md capture additions. No source file edits are staged because the audit produced none.

## Rules

- One build at a time. Never start a second while _build.md exists.
- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory. It's the crash-recovery mechanism.
- If you're unsure about an implementation choice, ask. Don't guess and build wrong.
- Build and test entries follow the same procedure (pre-flight → lock → execute → close). Execution mechanics differ: [build] entries edit files, [test] entries verify behaviour. See Step 3 for each.
