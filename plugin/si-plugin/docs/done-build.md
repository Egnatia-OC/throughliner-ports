# Build close-out

Close-out for build batches (including their test entries). Reached from done.md's router when _build.md's Entry carries a Build subheading.

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### 1.1 Verify completion

Read _build.md. All entries ticked?
- **Yes:** Proceed.
- **Some unticked:** Ask — finish (/next) or close partial (defer unticked, route back to QUEUE.md).

### 1.2 Update REGISTRY.md

For each file created, renamed, deleted, or significantly modified:
- Add new entries (path + one-line description)
- Update descriptions if the role changed
- Remove entries for deleted files

### 1.3 Route findings to Captures

Check _build.md and the conversation for anything flagged during the build. Route each to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Route test failure fixes too.

### 1.4 Write deferred tests

Any planned test from the batch that couldn't run in this session goes to QUEUE.md's "## Deferred tests" section, per done.md Deferred tests — never as LOG-entry prose alone.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Narrate first [BRIEF]: one sentence noting the batch's reasoning is being carried from _build.md into the LOG entry — the file's last job before /done deletes it.

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled at the next /plan or /next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the batch's rationale in _build.md, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. After approval, write it to the new entry file.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and the build ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep

Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this build changed:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that this build (or any prior shift the queue hasn't caught up to) has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag (don't edit without asking). Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md

Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors next.md Step 1.4). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
1. Captures routed this session that affect the next batch → recommend /plan, name the blocker.
2. Parked items unblocked by this session's work (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
4. Batches empty → "Queue is clear. Run /plan when you have more."
