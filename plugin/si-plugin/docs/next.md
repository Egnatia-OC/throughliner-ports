# /next procedure

You are executing the next piece of work from the queue. One batch at a time, scope-locked.

## Step 1: Pre-flight checks

Before starting:

1. **Backfill LOG hashes:** [BRIEF] Run `git grep -l '\[HASH\]' -- LOG/log.md LOG/index.md`. If empty: move on, no output. Otherwise batch-read the matching files. Common case — one placeholder in each sharing the same hash: run `git log -n 1 --pretty=%h -- LOG/log.md` and use it for both. Fallback — multiple placeholders, or the common-case hash doesn't match the entry titles: for each remaining placeholder, run `git log -S "<entry title>" --pretty=%h -- LOG/` and use the returned hash. Replace `[HASH]` in place. No separate commit; the edit folds into this session's later commit.

2. **Active build check:** [SILENT] If _build.md exists, a build is in progress — offer to resume it (read _build.md for state) rather than start new. If not, move on (no output either way).

3. **Read QUEUE.md:** Find the top batch under "Batches." If the first non-empty line there is `--- Push required before continuing ---`, halt: tell the user the next batch depends on host-side effects (hooks or skill procedures that only refresh after push + uninstall/reinstall) and that they must push and reinstall before re-running /next. Don't read further; don't pick a batch past the marker.

4. **Blocker gate:** Scan for blockers that would force guessing:
   - Batch references something in SPEC.md that doesn't exist? → Block. Run /plan first.
   - Unresolved questions in batches above this one, or within the batch? → Surface them. Resolve or confirm they're independent. Captures-section questions don't block — /plan processes them — but surface any that clearly affects this batch.
   - Scan Captures for items (ideas or questions) relevant to the top batch. → Flag any that contradict, invalidate, or would benefit the batch if incorporated first. Recommend /plan if found.
   - Unpark-candidate scan (per plugin-behaviour.md Dependency ownership Unpark watch). → Any parked item newly unblocked by work since? Surface and recommend /plan if found.
   - Stale-batch scan (per plugin-behaviour.md Dependency ownership Staleness watch). → Any batch or capture stale enough that surrounding code or rules have moved past it? Surface and recommend /plan if found.
   - Unconfirmed tests from a previous build? → Surface them. The user can confirm, skip, or defer.

5. **If no blockers:** Present the batch: [BRIEF, PROMPT]
   - Batch title, a one-line gist from the rationale, and entry counts (build / test / audit). Don't re-render full entry text — the user just wrote it in QUEUE.md and can open it anytime; full text moves into _build.md on confirm.
   - "Ready?" — if the user wants to change scope or reorder, route to /plan.

6. **Branch on batch type:** After confirm, route by the subheadings present:
   - **Build batches** (Build subheading, optionally with Test) → Step 2.
   - **Test-only batches** (Test subheading, no Build) → Step 2; Step 3 handles test entries as verification.
   - **Audit batches** (Audit subheading) → jump to **Audit procedure** at the end. Audit batches don't edit files; their close shape differs.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** from the batch title and rationale, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the same shape /done writes to LOG/index.md at close — pre-generating here makes it reusable instead of regenerated. If the build runs as planned, /done reuses it verbatim; if scope shifts, /done re-authors against the same rule.

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

3. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done Step 2.3 deletes _build.md after close.

For test entries, Progress uses pass/fail instead of entry ticking:
```
Progress:
- [x] Test description — ✓
- [x] Test description — ✗ (reason)
```

_build.md is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Build [SILENT]

Execute entry by entry.

### Build entries

For each:

1. Read any relevant existing code or context.
2. Make the changes.
3. Tick it in _build.md Progress: `- [x] entry description — done`

### Test entries

When a batch contains test entries (under a Test subheading), execution is verification, not file editing:

1. Read the test description to understand what's checked.
2. Run every test you can verify yourself: read code, run commands, inspect output, check file content. Only tests needing real human interaction (visual appearance, physical device behaviour, subjective judgment) go to the user.
3. Tick each in _build.md Progress, pass/fail:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
4. Accumulate results in Changes: what was checked, what passed, what failed.

**On test failure:**
- Isolated (one test, rest unaffected): note it, continue, route the fix to Captures at close.
- Fundamental (invalidates the batch premise or blocks remaining tests): stop, go to Step 5.

### Rules during build

Absolute regardless of entry type:

- Stay within the entries' described work. To touch something unrelated, say so first: "I need to also edit [file] because [reason]. Add to scope?" Wait for approval.
- REGISTRY.md is not build scope. /done Step 1.5 handles registry updates after close.
- SPEC.md is read-only. Found a spec issue? Note it for /plan; don't fix now.
- Don't fix unrelated problems you notice. Note them for the queue.
- State regressions plainly. If something breaks, say so immediately. Don't silently fix or apologize — state the facts.

**Accumulate close notes** as you go: for each file or test, jot what changed in _build.md so /done needn't re-explore:
```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
```

## Step 4: Scope management

### User raises something out of scope [PROMPT]

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first in a fenced code block for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume the build.

**Coherence exception:** Default is capture, per above. The exception is narrow and keyed to why-pipeline coherence: if the item would share the build's log entry and index line — per plugin-behaviour.md Index entries — and folding it in makes the batch easier to find later rather than harder, add it to _build.md as a new entry and continue. Evaluate against the coherence rules, not user convenience. When uncertain, capture.

### Scope grows during the build

If Claude discovers additional work is needed:

- **Minor** (one more file, small prerequisite): ask to add, continue if approved.
- **Significant** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

## Step 5: Mid-build course-correction

### Claude discovers user-runnable testing is needed [PROMPT]

When Claude notices something will need user-runnable testing beyond the batch's Test section — visual check, physical-device behaviour, subjective judgment Claude can't verify:

1. Route the discovery to Captures in QUEUE.md as a future test-only batch. Draft the wording (what needs testing and why), show before writing per plugin-behaviour.md Captures.
2. Ask "anything else?" — repeat until no.
3. Resume the build.

Don't attempt the test inline. Don't extend the current batch's scope to include it. Same destination as Step 4's out-of-scope rule, different source — there the user raises it, here Claude notices it.

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a false assumption, a missing dependency, an approach that isn't working:

1. **Stop building.** Don't push through a broken approach.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop an entry, add a prerequisite, change the approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable:
     1. Return the batch text to QUEUE.md under Batches. Placement is Claude's call per plugin-behaviour.md Dependency ownership — original position or top, by what was learned.
     2. Route any captures surfaced during the attempt to Captures as normal (Step 4 rules unchanged).
     3. Tell the user to run /done. _build.md stays in place so /done's mode detection still fires Build close-out — see done.md. Differences from a completed build: the LOG entry's "what was built" describes the attempt and why it was aborted, and the batch returns to QUEUE.md rather than disappearing into the log.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Step 6: Context management

If context is running low, prefer in order:

1. **Finish and /done.** If most entries are ticked, push through. Short-term memory is enough.
2. **Close partial.** If significant work remains, /done what's ticked and requeue the rest. The next session picks up cleanly from _build.md and QUEUE.md.

## Step 7: Completion [BRIEF, PROMPT]

When all entries are ticked:

1. Tell the user the build is complete.
2. Show what was done (the Changes section from _build.md).
3. Say: "Run /done to record this and commit, or tighten what's already built before closing." Tightening means refining done entries — not raising new work. Anything new routes through the existing paths: out-of-scope via Step 4, thinking work via Captures.

Do NOT delete _build.md yourself. That's /done's job.

## Audit procedure

For audit batches only. Reached from Step 1.6 when the batch carries an Audit subheading. The shape audits need is read-many-propose-many — systematic read of the target, then handle findings one at a time (capture or drop). No file edits land directly; everything routes through Captures so /plan can convert findings into normal batches with the usual dialogue.

1. **Lock scope** [SILENT] — Create _build.md as Step 2 does (entry text + pre-generated index entry candidate), and remove the batch from QUEUE.md. Progress tracks findings rather than file edits:
```
Progress:
- [x] Finding description — captured
- [x] Finding description — dropped
```

2. **Read the target systematically against the criteria** [SILENT] — Open every file named by the target. Apply the criteria pass by pass — one criterion across the whole target, then the next, not mixing criteria per file. Don't skim; an audit's value is reading what's there. Accumulate observations in _build.md Changes with file:line references so the user can verify each.

3. **Compile findings** [SILENT] — Once the read is complete, group observations into discrete findings. One finding per actionable change. Phrase each as observed + why it matters — the shape a capture takes, since that's where they'll land.

4. **Present findings one at a time** [SEQUENCE, PROMPT] — State the count upfront ("N findings. First: ..."). For each: the observation, the file:line reference, why it matters. Wait for the user's call — **capture** or **drop**. Don't preview upcoming findings.

5. **Route approved findings to Captures** — For each marked capture, draft the wording in a fenced code block for approval, per plugin-behaviour.md (Captures + approval-time outputs). Once approved, append to Captures in QUEUE.md. Tick the finding in _build.md Progress as `captured` or `dropped`.

6. **Close** [BRIEF, PROMPT] — When all findings are handled, tell the user the audit is complete and show what was routed. Say: "Run /done to record this and commit, or keep reviewing." /done writes the LOG entry (audits get a normal entry — "files touched" names the target docs read, and routed captures get listed) and commits the _build.md deletion plus the QUEUE.md capture additions. No source file edits are staged because the audit produced none.

## Rules

- One build at a time. Never start a second while _build.md exists.
- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory — it's the crash-recovery mechanism.
- Unsure about an implementation choice? Ask. Don't guess and build wrong.
- Build and test entries follow the same procedure (pre-flight → lock → execute → close). Mechanics differ: [build] entries edit files, [test] entries verify. See Step 3.
