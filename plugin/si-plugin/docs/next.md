# /next procedure

You are executing the next piece of work from the queue. One batch at a time, scope-locked.

## Step 1: Pre-flight checks

Before starting:

1. **Backfill LOG hashes:** [BRIEF] Run `git grep -l '\[HASH\]' -- LOG/`. If empty: move on, no output. Otherwise batch-read the matching files. Common case — one entry file and the matching index line sharing the same hash: run `git log -n 1 --pretty=%h -- LOG/<entry file>` (the last commit touching a per-entry file is the /done commit that wrote it) and use it for both. Fallback — multiple placeholders, or the placeholder sits in a pre-split shared log file: for each remaining placeholder, run `git log -S "<entry title>" --pretty=%h -- LOG/` and use the returned hash. Replace `[HASH]` in place. No separate commit; the edit folds into this session's later commit.

2. **Active build check:** If _build.md exists, a build is in progress — offer to resume it (read _build.md for state) rather than start new, opening with a [BRIEF] line naming what's being read and why: _build.md holds the interrupted build's progress and remaining work, so the session picks up where it stopped instead of starting over. If _build.md does not exist: [SILENT] — move on, no output.

3. **Read QUEUE.md:** Find the top batch under "Batches." If the first non-empty line there is `--- Push required before continuing ---`, halt: tell the user the next batch depends on host-side effects (hooks or skill procedures that only refresh after push + uninstall/reinstall) and that they must push and reinstall before re-running /next. Don't read further; don't pick a batch past the marker.

4. **Blocker gate:** Scan for blockers that would force guessing:
   - Batch references something in SPEC.md that doesn't exist? → Block. Run /plan first.
   - Unresolved questions in batches above this one, or within the batch? → Surface them. Resolve or confirm they're independent. Captures-section questions don't block — /plan processes them — but surface any that clearly affects this batch.
   - Scan Captures for items (ideas or questions) relevant to the top batch. → Flag any that contradict, invalidate, or would benefit the batch if incorporated first. Recommend /plan if found.
   - Unpark-candidate scan (per plugin-behaviour.md Dependency ownership Unpark watch). → Any parked item newly unblocked by work since? Surface and recommend /plan if found.
   - Stale-batch scan (per plugin-behaviour.md Dependency ownership Staleness watch). → Any batch or capture stale enough that surrounding code or rules have moved past it? Surface and recommend /plan if found.
   - Deferred tests: read QUEUE.md's "## Deferred tests" section and re-present every entry there — the section is the record; don't rely on remembering past sessions. A test the user confirms (or that this session's own behaviour confirms) gets its line removed, with the confirmation recorded in this session's LOG entry. Unconfirmed entries stay listed for the next pre-flight. Section empty or absent: move on, no output.

5. **If no blockers:** Present the batch: [BRIEF, PROMPT]
   - Batch title, a one-line gist from the rationale, and entry counts (build / test / audit). Don't re-render full entry text — the user just wrote it in QUEUE.md and can open it anytime; full text moves into _build.md on confirm.
   - "Ready?" — if the user wants to change scope or reorder, route to /plan.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** from the batch title and rationale, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the same shape /done writes to LOG/index.md at close — pre-generating here makes it reusable instead of regenerated. If the build runs as planned, /done reuses it verbatim; if scope shifts, /done re-authors against the same rule.

2. **Create _build.md** with this structure:
```markdown
# Active Build

Entry: [copy the batch title and all entry text]

Index entry candidate: [the pre-generated entry from sub-step 1]

Files:
- [each file the batch entries name, one per line, path relative to project root]

Progress:
[empty — ticked as entries complete]

Changes:
[empty — accumulated as entries complete]
```

   The `Files:` section feeds the scope-lock: during the session, the pre_tool_use hook allows edits only to the listed files plus the method docs (QUEUE.md, REGISTRY.md, LOG/, _build.md) and denies everything else. Populate it from the files the batch entries name, paths relative to the project root. A batch whose entries name no files to edit (audit batches, test-only batches) gets the `Files:` header with no entries — that locks the session to method docs only.

3. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done deletes _build.md after close.

4. **Narrate the lock** [BRIEF] — one sentence on what _build.md is for, in user-facing terms: the build's working file — it carries the batch while QUEUE.md stays free, lists the files the safety check allows, tracks progress so an interrupted session can resume, and holds the reasoning /done writes into the session record.

Progress format varies by batch type:
- **Build entries:** `- [x] entry description — done`
- **Test entries:** `- [x] Test description — ✓` or `- [x] Test description — ✗ (reason)`
- **Audit findings:** `- [x] Finding description — captured` or `- [x] Finding description — dropped`

_build.md is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Route to per-type procedure

Load the procedure doc matching the batch's subheadings:

- **Build batches** (Build subheading, optionally with Test) → read and follow `next-build.md`.
- **Test-only batches** (Test subheading, no Build) → read and follow `next-test.md`.
- **Audit batches** (Audit subheading) → read and follow `next-audit.md`.

## Ending before scope-lock

Any session end before Step 2 locks scope — a push-marker halt, a blocker-gate stop, the user calling it off at "Ready?" — closes through this branch:

1. **Route any reshape direction to Captures.** [PROMPT] The trigger is mechanical: session ending + no batch locked + a reshape direction or learning the queue needs in conversation = capture needed. Route it as a capture pointing at the batch slug — draft the wording, show it for approval, per plugin-behaviour.md Captures. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the batch re-presents unchanged at the next /next. Nothing reshape-shaped in conversation: skip, no output.
2. **Name /done as the next step.** [BRIEF] Whatever the session did before stopping — hash backfills, captures filed — gets recorded and committed only by /done. Other recommendations the stop requires (run /plan to resolve a blocker, push and reinstall) ride alongside; they never replace naming /done.

What doesn't happen: no batch returns to the queue, because none left it — scope was never locked, so QUEUE.md already holds the batch.

## Rules

- One build at a time. Never start a second while _build.md exists.
- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory — it's the crash-recovery mechanism.
- Unsure about an implementation choice? Ask. Don't guess and build wrong.
