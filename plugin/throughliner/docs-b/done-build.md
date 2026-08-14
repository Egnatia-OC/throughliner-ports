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
the build working file against memory where the session is still remembered, and route any
mismatch to Unprocessed per 1.2.

### 1.2 Route findings to Unprocessed  [PROMPT]

Each finding is written to Unprocessed first, then reported — the whole set as
one numbered report. What this step sweeps is done.md's **The record a routing
step sweeps**.

Append each finding to Unprocessed, placed per the Captures placement rule
(narrate the placement). Append any fix a build check surfaced too.

### 1.3 Spec check-against  [SILENT] when the run agrees with SPEC; [PROMPT] on a contradiction

**The build close checks the run's work against SPEC. It does not sync SPEC to
match it.** Each item was already checked as it was built (next-build.md, step 4);
this is the run-level look, over work that has accumulated.

```
run agrees with SPEC   ->  silent; nothing to report
run CONTRADICTS SPEC   ->  name the SPEC sentence and the work that contradicts
                           it, in plain words, and let the user decide which is
                           wrong. Do NOT rewrite SPEC to fit what was built.
```

**Where a build genuinely established new product truth, that route is unchanged
and is not this step:** it asks mid-build, adds SPEC.md to the working file's
`Files:` list, and edits SPEC inline in the same commit (next-build.md, Scope
management). This step exists for the contradictions that route did not catch.

### 1.4 Red-flag close  [SILENT] when no flag; [PROMPT] when an item carries one

Per built item: if it carries a `Red flag · State: …` marker, run done.md's
**Red-flag lifecycle at close** before the item leaves the queue. Its flag was
cleared at processing, so carry the cleared flag into this item's LOG entry (2.1);
the backstop stops only if the marker still reads uncleared. Silent when no built
item carries a flag.

### 1.5 Reply to mail the run opened  [SILENT] when no mail arrived; [PROMPT] when it did

Where /next's pre-flight opened a message that changed work here, draft the reply
now and show it. The close is the moment the user is reliably present, which
mid-run is not — and a reply leaves the machine, so it goes out only on their
explicit yes to the exact wording. Never auto-sent, and never left for them to
ask for.

## Phase 2: Record

### 2.1 Write LOG entry  [DISCUSS, PROMPT]

**Narrate first** [BRIEF]: one sentence noting the work's reasoning is being
carried from the build working file into the LOG entry — the file's last job before /done
deletes it.

Write **one LOG entry file per built item**, each named after that item's slug.
Follow done.md's **LOG entry files** section, using its **Build** body fields
(`Files touched` from the build working file Changes; `Routed to Captures`).

**One entry per built item is unconditional**, however long the run. A work item's
queue text is *consumed* when it builds — /next removes it — so after the build the
LOG entry is the only surviving record of what the work was for.

**Each item's depth field says which form its entry takes — read it, don't judge
it.** The field is defined at its authoring site, next.md's per-item completion
step. Never judge by run size — a twelve-item run can still contain the
session's most contested decision.

**A ticked item with no depth field is read as short**, and noted at the close as
a discipline slip rather than passing silently: the field is required, so a
missing one means the build skipped a step, and saying so is what keeps it from
decaying back into an optional line.

**If a `[user]` item's entry was already started**, the walk-through opened it live
and appended as it went (next.md). Continue that file rather than writing a fresh
one, and don't treat the existing entry as a duplicate.

If a built item carried a red flag, note in this entry that it carried one and
that it was cleared — the carry-through, since the substantive clearing record was
written at the /plan close that cleared it.

### 2.2 Staleness sweep  [SILENT] when clean; [BRIEF] when flagging

Run done.md's **Staleness sweep**.

### 2.3 Delete the build working file  [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. **Only
after everything above is complete.**

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Build close** delta: the shared
overlap scan + queue-state ladder are the whole recommendation.

**No size judgment about the next run.** Don't advise how many items the next /next
should take, and don't write one into the forward advisory. The cleared-to-run line
already *is* the run bound and the user sets it at /plan; a second, softer cap
downstream of it is a guess with no measurement behind it, since Claude has no gauge
of context filling at all. Where a run genuinely needs to stop early, that is a
behaviour-based stop — the no-progress halt — never a number.
