# Test close-out

Close-out for test-only batches. Reached from done.md's router when _build.md's Entry carries a Test subheading and no Build subheading.

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion

Read _build.md. All tests ticked (✓ or ✗ with reason)?
- **Yes:** Proceed.
- **Some unticked:** Ask — finish (/next) or close partial (defer unticked, route back to QUEUE.md).

### 1.2 Route findings to Captures

Check _build.md and the conversation for anything flagged during testing. Route each to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Every ✗ needs a routed fix unless the user explicitly drops it.

### 1.3 Write deferred tests

Any planned test from the batch that couldn't run in this session goes to QUEUE.md's "## Deferred tests" section, per done.md Deferred tests — never as LOG-entry prose alone.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what was tested and why, re-authored from the batch's rationale in _build.md; what the results mean. Inline prose, no `Why:` label.]

**Tested:**
- [from _build.md Changes — each test with ✓ or ✗ (reason)]

**Routed to Captures:** [items added — including fixes for failures — or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and testing ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep

Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this session surfaced:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that anything since has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag (don't edit without asking). Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md

Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. Test sessions usually change no source files — the staged paths are typically the method docs and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
1. Fixes routed this session that affect the next batch → recommend /plan, name the blocker.
2. Parked items unblocked by this session's results (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
4. Batches empty → "Queue is clear. Run /plan when you have more."
