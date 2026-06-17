# /next procedure

You are executing the next piece of work from the queue. One batch at a time, scope-locked.

## Step 1: Pre-flight checks

Before starting:

1. **Active build check:** If _build.md exists, a build is in progress — offer to resume it (read _build.md for state) rather than start new, opening with a [BRIEF] line naming what's being read and why: _build.md holds the interrupted build's progress and remaining work, so the session picks up where it stopped instead of starting over. If _build.md does not exist: [SILENT] — move on, no output.

2. **Read QUEUE.md:** Find the top batch under "Batches." If the first non-empty line there is `--- Push required before continuing ---`, halt: tell the user the next batch depends on host-side effects (hooks or skill procedures that only refresh after push + uninstall/reinstall) and that they must push and reinstall before re-running /next. Don't read further; don't pick a batch past the marker. [BRIEF] If instead the first non-empty line is `--- Plan session here: <reason> ---`, halt the same way: tell the user a planning session is needed before the next batch, and name the reason the marker carries. Don't read further; don't pick a batch past the marker. [BRIEF]

3. **Send the top batch verbatim:** [BRIEF] As soon as QUEUE.md is read and no halt marker sits at the top, send the top batch as its own beat — one preamble line (e.g. "here's the top batch, checks to follow"), then the batch text verbatim — before the blocker gate and the rest of pre-flight run. The batch is visible first; the gate's findings arrive as follow-up after it. The send is what puts the batch in front of the user before any thinking; don't fold it into the gate output.

4. **Blocker gate:** [BRIEF] Scan for blockers that would force guessing. Surfacing each finding is brief — the batch is already visible from sub-step 3, so these arrive as a short follow-up:
   - Batch references something in SPEC.md that doesn't exist? → Block. Run /plan first.
   - Unresolved questions in batches above this one, or within the batch? → Surface them. Resolve or confirm they're independent. Captures-section questions don't block — /plan processes them — but surface any that clearly affects this batch.
   - Scan Captures for items (ideas or questions) relevant to the top batch. → Flag any that contradict, invalidate, or would benefit the batch if incorporated first. [PROMPT] If found, recommend /plan and wait — incorporating it first is the user's call to make before the build locks.
   - Unpark-candidate scan (per plugin-behaviour.md Dependency ownership Unpark watch). → Any parked item newly unblocked by work since? Surface and recommend /plan if found.
   - Stale-batch scan (per plugin-behaviour.md Dependency ownership Staleness watch). → Any batch or capture stale enough that surrounding code or rules have moved past it? Surface and recommend /plan if found.

5. **If no blockers:** [BRIEF, PROMPT] Ask "Ready?" — the batch text is already visible from sub-step 3, so this is just the go-ahead. If the user wants to change scope or reorder, route to /plan. On confirm, the full batch text moves into _build.md.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** from the batch title and rationale, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the same shape /done writes to LOG/index.md at close — pre-generating here makes it reusable instead of regenerated. If the build runs as planned, /done reuses it verbatim; if scope shifts, /done re-authors against the same rule.

2. **Create _build.md** with this structure:
```markdown
# Active Build

Entry: [copy the batch title and all entry text]

Index entry candidate: [the pre-generated entry from sub-step 1]

Files:
- [each file the batch entries name — one bare path per line, relative to project root, nothing else on the line]

Progress:
[empty — ticked as entries complete]

Changes:
[empty — accumulated as entries complete]
```

   The `Files:` section feeds the scope-lock — build scope's mechanical approximation (see plugin-behaviour.md Scope): during the session, the pre_tool_use hook allows edits only to the listed files plus the method docs (QUEUE.md, LOG/, _build.md) and denies everything else. Populate it from the files the batch entries name, paths relative to the project root. Files: lines must be bare paths — one path per line, nothing else on the line: the hook matches each line as an exact path, so any annotation on the line becomes part of the path and silently breaks the match (the file stays denied despite being listed). A batch whose entries name no files to edit (audit batches, test-only batches) gets the `Files:` header with no entries — that locks the session to method docs only.

3. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done deletes _build.md after close.

4. **Narrate the lock** [BRIEF] — one sentence on what _build.md is for, in user-facing terms: the build's working file — it carries the batch while QUEUE.md stays free, lists the files the safety check allows, tracks progress so an interrupted session can resume, and holds the reasoning /done writes into the session record.

Progress format varies by batch type:
- **Build entries:** `- [x] entry description — done`
- **Test entries:** `- [x] Test description — ✓` or `- [x] Test description — ✗ (reason)` or, when the test can't run in this session, `- [x] Test description — deferred (reason)`
- **Audit findings:** `- [x] Finding description — captured` or `- [x] Finding description — dropped`

_build.md is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Route to per-type procedure

Load the procedure doc matching the batch's subheadings:

- **Build batches** (Build subheading, optionally with Test) → read and follow `next-build.md`. A **Spec-edit** batch (Spec-edit subheading, the batch that edits SPEC.md) routes here too — it executes like any build.
- **Test-only batches** (Test subheading, no Build) → read and follow `next-test.md`.
- **Audit batches** (Audit subheading) → read and follow `next-audit.md`.
- **Freeform batches** (Freeform subheading) → read and follow `next-freeform.md`. Freeform is unqueued or loosely-scoped work that isn't a build, a test, or an audit — somewhere to make changes and talk them through when none of the other three fit. See next-freeform.md for what it's for and what it won't do.

### On-demand freeform: `/next freeform` with no queued batch

When the user runs `/next freeform` and no Freeform batch sits at the top of the queue, this is on-demand freeform work. Run the gate first [PROMPT]: ask whether the work could instead be a build, a test, or an audit — those three have homes already, and freeform is the refuge only for work that fits none of them. Require a one-line answer naming why none fit before proceeding; don't start until that's stated. Once it is, follow `next-freeform.md` directly — there's no queued batch to read or lock, so the Step 1 batch-pick and the Step 2 batch-move don't apply; next-freeform.md creates _build.md with an empty Files list and grows scope ask-by-ask.

## Ending before scope-lock

Any session end before Step 2 locks scope — a push-marker halt, a blocker-gate stop, the user calling it off at "Ready?" — closes through this branch:

1. **Route any reshape direction to Captures.** [PROMPT] The trigger is mechanical: session ending + no batch locked + a reshape direction or learning the queue needs in conversation = capture needed. Route it as a capture pointing at the batch slug — draft the wording, show it for approval, per plugin-behaviour.md Captures. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the batch re-presents unchanged at the next /next. Nothing reshape-shaped in conversation: skip, no output.
2. **Name /done as the next step.** [BRIEF] Whatever the session did before stopping — hash backfills, captures filed — gets recorded and committed only by /done. Other recommendations the stop requires (run /plan to resolve a blocker, push and reinstall) ride alongside; they never replace naming /done.

What doesn't happen: no batch returns to the queue, because none left it — scope was never locked, so QUEUE.md already holds the batch.

## Rules

- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory — it's the crash-recovery mechanism.
- At build completion, the only valid next-step recommendation is /done — never /next, never another build. The finished build isn't recorded until /done writes its LOG entry and commits, so recommending more building first leaves the just-finished batch without a record. (Completion counterpart to one-build-at-a-time in plugin-behaviour.md: that rule guards a build's start, this one guards its end.)
- If context runs long mid-build, suggest finishing the current file and running /done. A clean close beats pushing into a context squeeze — the next session resumes cleanly from _build.md.
