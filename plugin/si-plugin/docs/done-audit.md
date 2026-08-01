# Audit close-out

Close-out for audit-flavor work items. Reached from done.md's router for the run's `[audit]` items. Audits edit no source files — the session's product is the captures it appended to Unprocessed.

A run may contain several audit items. The record step writes one LOG entry per audit item; the staleness sweep, commit, and recommendation run once for the whole close.

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion

Run **Verify completion** in done.md. An audit close carries no memory-reconcile delta — a finding is ticked when captured or dropped.

### 1.2 Route stragglers to Unprocessed [PROMPT]

Each straggler is drafted, shown, and approved before it's written, so this step waits on the user. The findings themselves were appended during the audit. The record of anything else flagged along the way — observations outside the audit's criteria, process issues — is _build.md's notes plus any captures already appended at the moment of noticing; sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Append each to Unprocessed, placed per plugin-behaviour.md Captures placement (narrate the placement).

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

A run may have run several audit items — write one LOG entry file per audit item, each named after that item's slug. Follow done.md's **LOG entry files** section (Entry template and approval), using its **Audit** per-flavor body fields (`Files touched` — the target artifacts read, since the audit edited nothing; `Routed to Captures`; and `Approval outcomes`). The shared frame covers the template, approval, candidate reuse, and the index-line prepend.

An audit doesn't clear red flags — clearing happens at processing (plugin-behaviour.md Flag states). A security, privacy, or breach risk this audit surfaces is filed as an ordinary uncleared capture in Unprocessed (`Red flag · State: uncleared`), which a later /plan clears; note in this entry that the audit surfaced it.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Run the **Staleness sweep** in done.md.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. No source file edits are staged because the audit produced none — the staged paths are the QUEUE.md capture additions, the LOG/ changes, and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Run **Recommend next** in done.md and apply its **Audit close** delta: findings appended this session sit unprocessed, so the default recommendation is /plan, to sort them into work — name the count. Only when nothing was appended does the shared overlap scan run and the ladder apply.
