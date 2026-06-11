# Audit close-out

Close-out for audit batches. Reached from done.md's router when _build.md's Entry carries an Audit subheading. Audits edit no source files — the session's product is the captures it routed.

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion

Read _build.md. All findings ticked (captured or dropped)?
- **Yes:** Proceed.
- **Some unticked:** Ask — finish presenting them (/next) or close partial (defer unticked, route the remainder back to QUEUE.md).

### 1.2 Route stragglers to Captures

The findings themselves were routed during the audit. Check _build.md and the conversation for anything else flagged along the way — observations outside the audit's criteria, process issues — and route each to Captures, placed per plugin-behaviour.md Captures placement (narrate the placement).

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled at the next /plan or /next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what was audited against which criteria and why, re-authored from the batch's rationale in _build.md; what the read surfaced. Inline prose, no `Why:` label.]

**Files touched:**
- [the target artifacts that were read — the audit edited nothing]

**Routed to Captures:** [findings captured, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. After approval, write it to the new entry file.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and the audit ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep

Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this audit surfaced:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that anything since has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag (don't edit without asking). Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md

Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. No source file edits are staged because the audit produced none — the staged paths are the QUEUE.md capture additions, the LOG/ changes, and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Findings routed this session sit unprocessed in Captures — the default recommendation after an audit is /plan, to process them into batches. Name the count.

If nothing was routed, recommend by queue state:
1. Parked items unblocked by this session (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
2. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first.
3. Batches empty → "Queue is clear. Run /plan when you have more."
