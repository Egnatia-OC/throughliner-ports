# Freeform close-out

Close-out for freeform sessions. Reached from done.md's router for a run's `[freeform]` line, or when _build.md came from an on-demand `/next freeform` run. Freeform has no finding list to verify and no work line to return to the queue — the record is what changed and what was discussed.

## Phase 1: Judgment (while context is fresh)

### 1.1 Route findings to Unprocessed [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged — ideas raised, observations, follow-up work — is _build.md's notes plus any captures already appended at the moment of noticing; sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Append each to Unprocessed, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Freeform files captures but never processes them; processing waits for /plan.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files. A freeform session has no work-line slug, so name it by session type and date — `LOG/freeform-<YYYY-MM-DD>.md` (append `-2`, `-3` if the name is taken). Use this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what the session did and why, re-authored as inline prose: what was changed, what was discussed, what was decided. No `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files). This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

There's no pre-generated candidate for a freeform session — author the index entry fresh against the Index entries rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Stay silent when nothing's stale; surface a flag in one or two sentences when something is. Quick check of the remaining work lines in QUEUE.md — any staleness from any cause:
- Do any remaining Unprocessed or Processed work lines reference files this session (or an earlier shift the queue hasn't caught up to) renamed or deleted?
- Do any reference behaviour or rules a shift since has moved past?
- Are any sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag it — and split by fix path: a fate decision (drop / rewrite / keep the affected line) is /plan's, so defer it; a pure pointer drift — a file reference whose target content is unchanged — is mechanical, so fix it here and report it in one line, riding this commit, with no approval ask.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. Freeform sessions may or may not change source files — stage what _build.md's Changes records, plus the method docs and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the queue situation in everyday words. Keep the plain statement accurate: don't say the queue is clear when work is still waiting to be sorted.

Before recommending, scan the still-unprocessed work for overlap with the top processed item — work that contradicts, invalidates, or would benefit it if sorted first. State the scan's result either way, not only when it blocks: nothing unprocessed — say nothing's waiting for /plan; unprocessed work waiting but none overlaps the next item — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three items are waiting to be sorted; none touches the next piece of work, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
1. Captures appended this session that need sorting → recommend /plan, name them. Freeform often leaves captures behind, so this is the common recommendation.
2. Processed work exists → name the next item, then ask whether the user is continuing into another /next now.
3. Processed empty → "Queue is clear. Run /plan when you have more."
