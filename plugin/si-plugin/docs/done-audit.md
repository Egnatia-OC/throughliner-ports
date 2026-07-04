# Audit close-out

Close-out for audit-flavor work lines. Reached from done.md's router for the run's `[audit]` lines. Audits edit no source files — the session's product is the captures it appended to Unprocessed.

A run may contain several audit lines. The record step writes one LOG entry per audit line; the staleness sweep, commit, and recommendation run once for the whole close.

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion

Read _build.md. All findings ticked (captured or dropped)?
- **Yes:** Proceed.
- **Some unticked:** [PROMPT] Ask — finish presenting them (/next) or close partial (defer the unticked, returning the remainder to QUEUE.md's Processed section). Wait for the user's call.

### 1.2 Route stragglers to Unprocessed [PROMPT]

Each straggler is drafted, shown, and approved before it's written, so this step waits on the user. The findings themselves were appended during the audit. The record of anything else flagged along the way — observations outside the audit's criteria, process issues — is _build.md's notes plus any captures already appended at the moment of noticing; sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Append each to Unprocessed, placed per plugin-behaviour.md Captures placement (narrate the placement).

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

A run may have run several audit lines. Write one LOG entry file per audit line, each named after that line's slug (done.md LOG entry files), reusing that line's pre-generated Index entry candidate. Draft each as its own file under `LOG/`, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what was audited against which criteria and why, re-authored from the work line's rationale in _build.md; what the read surfaced. Inline prose, no `Why:` label.]

**Files touched:**
- [the target artifacts that were read — the audit edited nothing]

**Routed to Captures:** [findings captured, or "none"]

**Approval outcomes:** [what happened at bulk approval — findings dropped or reworded, each with the user's reason; or "all findings approved as-is"]
```

The Approval outcomes line records what the bulk-approval step decided: a finding the user dropped, or reworded, with the reason they gave. Recording it means a decision made at audit time doesn't vanish — without it, the only trace of a dropped or reworded finding is its absence. When every finding was approved as-is, say so in one phrase rather than omitting the line.

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files). This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md carries a matching `Index entry candidate` for the line and the audit ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Stay silent when nothing's stale; surface a flag in one or two sentences when something is. Quick check of the remaining work lines in QUEUE.md — any staleness from any cause, not just what this audit surfaced:
- Do any remaining Unprocessed or Processed work lines reference files anything since has renamed or deleted?
- Do any reference behaviour or rules a shift since has moved past?
- Are any sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag it — and split by fix path: a fate decision (drop / rewrite / keep the affected line) is /plan's, so defer it; a pure pointer drift — a file reference whose target content is unchanged — is mechanical, so fix it here and report it in one line, riding this commit, with no approval ask.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. No source file edits are staged because the audit produced none — the staged paths are the QUEUE.md capture additions, the LOG/ changes, and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the queue situation in everyday words. Keep the plain statement accurate: don't say the queue is clear when work is still waiting to be sorted.

Findings appended this session sit unprocessed — the default recommendation after an audit is /plan, to sort them into work. Name the count.

If nothing was appended, scan the still-unprocessed work for overlap with the top processed item — work that contradicts, invalidates, or would benefit it if sorted first. State the scan's result either way, not only when it blocks: nothing unprocessed — say nothing's waiting for /plan; unprocessed work waiting but none overlaps the next item — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three items are waiting to be sorted; none touches the next piece of work, so nothing blocks it," never "there may be overlap worth checking." Then, if nothing blocks, recommend by queue state:
1. Processed work exists → name the next item, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first.
2. Processed empty → "Queue is clear. Run /plan when you have more."
