---
name: done-build
docset: B
note: >
  Close-out for build-flavor work items. Reached from done.md's router for the
  run's build items (work items carrying no flavor tag).
---

# Build close-out

A build that changed SPEC.md — because it grew scope mid-build, or a build item
listed it — closes here like any other build. There is no separate spec-edit
close.

```
a run may contain SEVERAL build items:
    per built item  ->  the judgment and record steps, one LOG entry each
    once per close  ->  the staleness sweep, the commit, the recommendation
```

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### Mid-close directive — new scope vs build-completing fix  [PROMPT]

If a new directive arises during the close — the user raises a change, or
verification turns one up — decide by one line: **does it complete the just-built
work's own verification, or is it new scope?**

```
a fix to a genuine bug in what this build was meant to deliver
    ->  FOLDS IN. Finish it, tick it — it's part of the build.
new scope (a redesign, a new feature, a change to something that already worked)
    ->  ROUTES OUT: a fresh /next, or a capture to Unprocessed if not urgent.
        Even if it looks small. Even if the user raises it here.
```

/done records and commits; it doesn't take on new build scope.

### 1.1 Verify completion

Run done.md's **Verify completion**. Its build-close delta applies: reconcile
_build.md against memory where the session is still remembered, and route any
mismatch to Unprocessed per 1.2.

### 1.2 Route findings to Unprocessed  [PROMPT]

Each finding is drafted, shown and approved before it's written, so this step
waits on the user.

```
the RECORD this step sweeps:
    _build.md's notes
    any captures already appended at the moment of noticing
conversation memory  ->  a same-session BONUS pass, never a source this step
                         depends on
```

Append each finding to Unprocessed, placed per the Captures placement rule
(narrate the placement). Append any fix a build check surfaced too.

### 1.3 Spec-sync gate  [SILENT] when nothing drifts, [PROMPT] on drift

Run done.md's **Spec-sync gate** and apply its **Build close** delta: SPEC.md is
scope-locked, so add SPEC.md to _build.md's `Files:` list before editing, then edit
SPEC to match what the build landed and commit it in this same commit.

### 1.4 Red-flag close  [SILENT] when no flag, [PROMPT] when an item carries one

Per built item: if it carries a `Red flag · State: …` marker, run done.md's
**Red-flag lifecycle at close** before the item leaves the queue. Its flag was
cleared at processing, so carry the cleared flag into this item's LOG entry (2.1);
the backstop stops only if the marker still reads uncleared. Silent when no built
item carries a flag.

## Phase 2: Record

### 2.1 Write LOG entry  [DISCUSS, PROMPT]

**Narrate first** [BRIEF]: one sentence noting the work's reasoning is being
carried from _build.md into the LOG entry — the file's last job before /done
deletes it.

Write **one LOG entry file per built item**, each named after that item's slug.
Follow done.md's **LOG entry files** section, using its **Build** body fields
(`Files touched` from _build.md Changes; `Routed to Captures`).

If a built item carried a red flag, note in this entry that it carried one and
that it was cleared — the carry-through, since the substantive clearing record was
written at the /plan close that cleared it.

### 2.2 Staleness sweep  [SILENT] when clean, [BRIEF] when flagging

Run done.md's **Staleness sweep**.

### 2.3 Delete _build.md  [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. **Only
after everything above is complete.**

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Build close** delta: the shared
overlap scan + queue-state ladder are the whole recommendation.
