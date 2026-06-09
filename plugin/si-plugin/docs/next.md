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

3. **Remove the batch from QUEUE.md** (move it to _build.md — the queue is now free for other sessions). /done deletes _build.md after close.

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

## Rules

- One build at a time. Never start a second while _build.md exists.
- The entries are the contract. Don't exceed the described work without explicit approval.
- Per-entry ticking is mandatory — it's the crash-recovery mechanism.
- Unsure about an implementation choice? Ask. Don't guess and build wrong.
