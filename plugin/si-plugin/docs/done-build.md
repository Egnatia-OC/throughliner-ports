# Build close-out

Close-out for build-flavor work items. Reached from done.md's router for the run's build items (work items carrying no flavor tag). A build that changed SPEC.md (because it grew scope to include it mid-build, or a build item listed it) closes here like any other build — there is no separate spec-edit close.

A run may contain several build items. The judgment and record steps below apply per built item where noted — one LOG entry per item — while the staleness sweep, commit, and recommendation run once for the whole close.

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### Mid-close directive — new scope vs build-completing fix [PROMPT]

If a new directive arises during the close — the user raises a change, or verification turns one up — decide where it goes by one line: does it complete the just-built work's own verification, or is it new scope? A fix to a genuine bug in what this build was meant to deliver folds in (finish it, tick it — it's part of the build). New scope — a redesign, a new feature, a change to something that already worked — routes out: a fresh /next, or a capture appended to Unprocessed if it isn't urgent, even if it looks small and even if the user raises it here. /done records and commits; it doesn't take on new build scope. This applies the general mid-close rule in plugin-behaviour.md (Routing and discipline) at the build close.

### 1.1 Verify completion

Run **Verify completion** in done.md. Its build-close delta applies here: reconcile _build.md against memory where the session is still remembered, and route any mismatch to Unprocessed per 1.2.

### 1.2 Route findings to Unprocessed [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged is _build.md's notes plus any captures already appended at the moment of noticing — sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Append each finding to Unprocessed, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Append any fix a build check surfaced too.

### 1.3 Spec-sync gate [SILENT] when nothing drifts, [PROMPT] when drift found

Run the **Spec-sync gate** in done.md and apply its **Build close** delta: SPEC.md is scope-locked, so add SPEC.md to _build.md's `Files:` list before editing, then edit SPEC to match what the build landed and commit it in this same commit.

### 1.4 Red-flag close [SILENT] when no flag, [PROMPT] when an item carries one

Per built item: if the item carries a `Red flag · State: …` marker, run the Red-flag lifecycle at close in done.md before the item leaves the queue. Its flag was cleared at processing, so carry the cleared flag into this item's LOG entry (2.1); the backstop stops only if the marker still reads uncleared. Silent when no built item carries a flag.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Narrate first [BRIEF]: one sentence noting the work's reasoning is being carried from _build.md into the LOG entry — the file's last job before /done deletes it.

A run may have built several build items — write one LOG entry file per built item, each named after that item's slug. Follow done.md's **LOG entry files** section (Entry template and approval), using its **Build** per-flavor body fields (`Files touched` from _build.md Changes; `Routed to Captures`). The shared frame covers the template, approval, candidate reuse, and the index-line prepend.

If a built item carried a red flag, note in this entry that it carried a red flag and that it was cleared, per done.md Recording a cleared red flag — the carry-through, since the substantive clearing record was written at the /plan close that cleared it.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Run the **Staleness sweep** in done.md.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next [BRIEF, PROMPT]

Run **Recommend next** in done.md and apply its **Build close** delta: the shared overlap scan + queue-state ladder are the whole recommendation.
