---
name: done
docset: B
note: >
  /done procedure. Routes to a per-flavor close-out and states the
  shared close core once; the sub-docs carry the flavor-specific steps.
---

# /done procedure

Close the current session — record what happened, update docs, commit.

## Route by session shape  [SILENT]

Check for _build.md. **The check is automatic — don't ask, and don't narrate the
routing; just route.**

**The _build.md read is unconditional.** When it exists, read it in full before
the close-out runs, *regardless of how much of the session you remember*.
Conversation memory enriches the LOG entry (tradeoffs, colour the file doesn't
capture) but never substitutes for the read. A "read it only if you don't
remember" condition hangs on Claude assessing its own memory, which fails exactly
post-/clear and post-compaction — when the session *feels* remembered but the
details are gone.

```
_build.md EXISTS  ->  read it, then route by the run's work-item flavors:
    build items (no tag)  ->  done-build.md
                              # a build that changed SPEC.md closes here like
                              # any other build — same steps, same commit core
    [audit] items         ->  done-audit.md
    mixed run             ->  each item closes through its OWN flavor's
                              close-out, one LOG entry per item, sharing the
                              single end-of-session commit

NO _build.md      ->  three shapes:
    a completed [user] item   ->  Completed [user]-item close (below)
    a planning session        ->  done-plan.md
        (queue managed, captures processed, readiness line moved,
         or _plan.md exists)
    standalone handmade work  ->  Standalone handmade-work close (below)
        (no planning either, and the tree holds uncommitted edits the
         session didn't make)
```

Detect a completed `[user]` item **from what the session can already see — never
by asking.** A `[user]` item is walked through, and that is all; no step of its
life asks whether it's done.

```
walked through to its end in THIS session   ->  completed. Close it here.
the user has said they did it               ->  completed. Close it here.
anything else                               ->  leave it in Processed, silently
```

Where the item's walkthrough names an observable check — a file present or
absent, a branch gone, a URL responding — **run it before recording completion**,
rather than taking the report at face value. Checking the world is not asking the
user. A failed check is reported as what was found, and the item stays in place.

The gap this leaves is real and is meant to stay: an item the user completed on
their own between sessions, with nothing observable to show for it, will sit in
the queue until they mention it. **That is the fallback, not a hole to plug** —
mentioning it is already a supported path, and a completion ask is exactly what
this removed. Don't reintroduce one under any wording.

This can coincide with a planning session; when it does, close the item through
that section and let done-plan.md handle the rest.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit
core below, then return to the sub-doc for the recommendation.

**There is no test close-out** — the test flavor is retired. A check Claude can
run is part of building, closed by done-build.md. A check only the user can run is
a `[user]` work item, which never enters a _build.md — so /done doesn't close it
*as a build*, but once the user has run it, /done records its completion and
removes it from the queue through the close below.

## Completed `[user]`-item close  [BRIEF]

A `[user]` item never entered a _build.md, so it isn't ticked and closed like a
build. This is the close that records it and removes it from Processed, so a
finished item doesn't strand in the queue and get re-presented by the next /next.
It also runs inside a /plan close when the user mentions async-completed items.

```
1. take the completed item(s) from what the session can see  [SILENT]
   # the routing test above already identified them. Don't ask, and don't
   # list the other [user] items still sitting in Processed — an item whose
   # completion isn't visible simply stays where it is.
   # where the walkthrough named an observable check, run it first
2. write a LOG entry per completed item, named after its slug
   # records what the user did and its outcome; draft and show for approval
   # if it carried a red-flag marker -> run Red-flag lifecycle at close
3. remove each completed item from Processed
   # this is what stops it being re-presented
4. run the wind-down re-scan, then the commit core
   # staging QUEUE.md and the LOG changes
```

A remote-gated push offer applies as normal — a completed `[user]` item is real
project progress, not bookkeeping.

## Standalone handmade-work close  [BRIEF, PROMPT]

Reached with no _build.md and no planning work — the user made ad-hoc edits by
hand and wants them recorded. **Never required:** hand edits left uncommitted are
simply swept into the next /done that runs. This exists for when the user wants
them logged and committed as their own clean record.

**1. Read the edits as the user's own work — don't panic.** Uncommitted changes
the session didn't make are most likely the user's expected work. Run `git status
--porcelain`, and where what changed isn't self-evident, look. Confirm with the
user that these are theirs and meant to be saved. **Never report them as a broken
repo, and never try to undo them.**

**2. Decide LOG granularity by judgment.**

```
one coherent change     ->  a single entry: LOG/<YYYY-MM-DD>-handmade.md
                            (-2 if the name is taken)
several distinct        ->  a separate entry per logical change
logical changes             # better recall than one lumped entry
```

Draft each entry's one-liner and its rationale and **show them for approval before
writing** — this close is reached by sessions with no build and no planning behind
them, so the shared LOG-entry approval frame is a doc away. Step 3's "the commit
message is the approved entry" refers to this approval.

**3. Run the wind-down re-scan, then the commit core**, staging the hand-edited
files explicitly. The commit message is the approved entry; for several entries,
the title names the handmade-work close and the body carries each entry's summary.
Unlike a planning close, this one **does** offer push when a remote exists — it's
real project work, not bookkeeping.

## Verify completion  [PROMPT when unticked]

The build and audit close-outs point here for their completion check.

Read _build.md. Is every item ticked — each build item done, each audit finding
captured or dropped?

```
yes             ->  proceed
some unticked   ->  [PROMPT] ask: finish the rest (/next), or close partial
                    (defer the unticked items, returning them to Processed)?
                    Wait for the user's call.
```

**Build-close delta — reconcile against memory.** At a build close, where the
session is still remembered, reconcile _build.md against what you recall. If the
file and memory disagree — work that happened but went unticked, a Changes note
missing something memory knows was done — **that mismatch is itself a finding
about build discipline**, and it routes to Unprocessed. It's the only routine
check _build.md's accuracy gets before a fresh session has to rely on it. An audit
close carries no such reconcile.

## Spec-sync gate  [SILENT] in sync; [PROMPT] on drift

The build and plan close-outs point here. (Audits land no product changes, so an
audit close has no spec-sync gate.)

**Did this session's work change what SPEC says?** Apply the spec-entry trigger
test **in plan.md's own wording** — quote it from there rather than keeping a copy
here, so the two can't drift apart. Read against what this session landed.

If it fires, **stop the close — don't commit yet.** Surface the drift in plain
words, naming which SPEC sentence the session made wrong, get approval to fix it,
then edit SPEC and commit it **in this same commit**. Don't file it as a capture
for a later session.

Spec-driven development's contract is that the spec moves in the same commit as
the behaviour change. Deferring the fix would close a commit with SPEC already
behind, breaking that atomicity — the exact drift this gate prevents.

```
build close  ->  SPEC.md is scope-locked: ADD SPEC.md to _build.md's Files:
                 first, then edit. Also catches a build landing a
                 spec-affecting change with no prior spec entry.
plan close   ->  no scope-lock active: edit SPEC.md directly in-session.
                 Editing SPEC to match a decision the user already made this
                 session is RECORDING, not re-planning.
```

The plan branch covers every plan-type close — a /plan session, a setup session,
and a method-doc-only session alike. None of the three runs a scope-lock, so all
three edit SPEC directly.

A session that changed only queue ordering or captures touched no SPEC sentence
and passes silently.

## Staleness sweep  [SILENT] when clean, [BRIEF] when flagging

The build and audit close-outs point here. Quick check of the remaining work items
— any staleness from any cause, not just what this session changed:

```
do any remaining items reference files since renamed or deleted?
do any reference behaviour or rules a shift since has moved past?
are any sitting long enough that surrounding code or rules have drifted away?
```

If so, flag it — and **split by fix path**:

```
a fate decision (drop / rewrite / keep)  ->  /plan's. Defer it.
a pure pointer drift                     ->  mechanical. Fix it HERE, report in
    (a file reference whose target             one line, riding this commit,
     content is unchanged)                     with no approval ask.
```

## LOG entry files

Every sub-doc's entry-writing step points here.

**One text, several positions.** The session authors **two** texts, not four:

```
the one-liner  ->  the entry heading's summary
                   the index line's body
                   the commit title
the rationale  ->  the entry body
                   the commit body
```

The user approves both once, at the entry-writing step, and the commit step reuses
them verbatim — nothing new to read.

**Entry template** (placeholder hash — backfilled automatically at the next
session start):

````markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the work's rationale in _build.md (or, for a
planning session, what motivated these queue changes), expanded with what was
learned along the way. Inline prose, no `Why:` label. Re-authoring is where
reasoning gets re-attributed by accident: credit the user only for reasoning
they gave in their own words, write mixed authorship as mixed, and don't wear
Claude's reasoning as theirs (plugin-behaviour.md, rationale provenance).]

[per-flavor body fields]
````

```
per-flavor body fields — the only delta between flavors:

build       **Files touched:**       from _build.md Changes
            **Routed to Captures:**  items added, or "none"

audit       **Files touched:**       the target artifacts READ (an audit edits
                                     nothing)
            **Routed to Captures:**  findings captured, or "none"
            **Approval outcomes:**   what happened at bulk approval — findings
                                     dropped or reworded, each with the user's
                                     reason; or "all findings approved as-is"

plan/setup  **Queue changes:**       work processed, reordered, or modified
                                     (for setup: the first rough build item and
                                     the docs scaffolded)
            **Work processed:**      kept / deleted, with slugs, or "none"
```

The audit's Approval-outcomes line means a decision made at audit time doesn't
vanish — without it, the only trace of a dropped or reworded finding is its
absence.

**The approval frame, identical for every flavor.** Show the wording for approval
before writing.

```
run shipped ONE item     ->  this approval ALSO covers the commit message: title
                             and body derive verbatim from this entry, so the
                             commit step reviews nothing new
run shipped SEVERAL      ->  the commit message is a one-line summary of the
                             whole run, drafted and approved at the commit step;
                             each item's entry still stands on its own
```

This entry is the session's summary — **there is no separate chat recap.** Before
showing it, check whether this session raised and resolved a concern or weighed an
alternative that lost; if so, carry it with why it lost.

**Reuse the pre-generated candidate** where one exists: if _build.md carries a
matching index-entry candidate and the item built as planned, reuse it verbatim;
if scope shifted, author fresh against the same rule. Planning sessions have no
candidate — author fresh.

Prepend to `LOG/index.md` after the header, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

**Each entry is its own file under `LOG/`, date-prefixed** so the folder sorts
newest-first on a name sort — never appended to a shared log file:

```
session closing work items    ->  LOG/<YYYY-MM-DD>-<slug>.md
    (build, audit)                # one entry file per item, all sharing the date
session with no slug          ->  LOG/<YYYY-MM-DD>-<type>.md
    (planning, setup, handmade)   # e.g. 2026-06-09-plan.md
name already taken            ->  append -2, -3, …
```

The date prefix is the **session** date, not the commit date — write it from the
current date at close. Its only job is the name sort; it is not a second copy of
the hash.

**The hash lives in the entry heading and the index line, never in the filename** —
the commit hash doesn't exist yet when the file is written, which is why the
placeholder pattern exists.

**Entry prose never writes the literal placeholder token.** The token belongs only
in hash position, where the automatic backfill treats any match mechanically. A
prose mention is one find-replace away from corrupting the entry. When an entry
needs to describe the mechanism, say it indirectly ("the placeholder", "the
unfilled hash").

Pre-split entries live in `LOG/log.md` and `LOG/log-v*.md` — untouched, found by
hash or title search.

**Captures filed after the commit.** When a capture comes up in the post-commit
tail, the same move that appends it to QUEUE.md also updates this session's
just-written entry — edit its "Routed to Captures:" line to include it, as a
working-tree edit with no separate commit. It rides into the next session's
commit, exactly as the hash backfill does. The entry is the session's record, and
a capture belongs to the session it came up in.

## Checks the closing session couldn't run

The deferred-tests section is retired — there is no separate test queue.

```
a verification only the user can run  ->  a [user] work item
a check Claude can run                ->  just part of building
```

So the only thing /done does with a check it couldn't run is the ordinary capture
move: if the closing session discovers a needed verification that isn't already a
`[user]` item, file it as a `[user]` work item appended to Unprocessed. Nothing
tracks it in a dedicated section, and **no LOG-only prose stands in for the queue
line** — an unrun check recorded only in a log entry never surfaces again.

## Recording a cleared red flag

A red flag is cleared at *processing* — the /plan moment its item is judged ready.
When a flag was cleared this session, record **how** in the session's LOG entry:

```
designed out / fixed  ->  how the risk was removed
consciously accepted  ->  the informed-consent trail: what the user was warned
                          about, and that they chose to proceed
```

The LOG is where the how-it-cleared lives; the marker on the work item carries
only `State: cleared`. **Recording is unconditional once a flag clears** — the
record never rides only in chat or on the marker, because no later session
re-reads those for clearing history.

## Red-flag lifecycle at close

The sub-doc close-outs point here when the closing item carries a marker. By the
time a red-flagged item reaches a build or audit close its flag was already
cleared at processing, so the close does **not** re-decide it. Two things:

```
1. carry the cleared flag into this item's LOG entry
   # note it carried a red flag and that it was cleared. The substantive
   # how-it-cleared record was written at the /plan close that cleared it.
2. BACKSTOP [PROMPT]: marker still reads State: uncleared?
   # should be impossible. STOP and surface it rather than committing — an
   # uncleared flag at a ship close means the model was bypassed.
```

## Wind-down re-scan (file-only)  [BRIEF, PROMPT]

Commit core points here, so it runs at **every** /done close regardless of session
type.

Before committing, re-read this session's own discussion and surface candidate
captures — things the user thought out loud but never flagged.

```
/done  ->  may FILE the surfaced captures
       ->  never ROUTES them (keep / delete)
# filing is capture-making, allowed in any session;
# routing is planning, /plan's alone
```

Present all candidates as ONE numbered set of fully-drafted captures for a single
approval; the user contests by number, and only contested items go one at a time.
Append the approved ones to Unprocessed, and add them to this session's LOG entry's
"Routed to Captures:" line as a working-tree edit riding this commit.

**Name the step's best-effort nature in plain words when it runs** — it re-reads
whatever discussion is still in view, so a surfaced-nothing result is "nothing
jumped out in what I could still see," not a guarantee nothing was missed.

Two things to state, not fix: a fresh-chat /done has none of the session's
thinking in view, so there is nothing to re-scan; and when /plan already ran its
own wind-down re-scan this session, this is a harmless no-op.

> "Re-read our discussion — nothing came up that isn't already captured."

## Session-file cleanup (throwaway artifacts)  [BRIEF, PROMPT]

Commit core points here, so it runs at every close. _build.md and _plan.md are
deleted by the close already; this generalises that lifecycle to *other* throwaway
files this session created. (Prevention comes first — temp files should have gone
to the scratchpad and never reached the project. This catches the ones that landed
anyway.)

Offer to delete only files meeting **all** of these:

```
Claude created or wrote them THIS session
    # established from _build.md Changes and this session's own edits.
    # A file Claude did not create this session is NEVER presumed rubbish —
    # uncommitted changes the session didn't make are the user's own work.
they have NO future use
    # not a deliverable, not a research finding, not evidence a later session
    # must re-read. Purely throwaway.
```

```
one at a time, user approves each  [PROMPT]  ->  never auto-delete
git-tracked file                             ->  recoverable from history;
                                                 say so plainly (low stakes)
untracked, or outside the repo               ->  NOT recoverable. Give a clear
                                                 warning before removing it.
```

If nothing session-created looks throwaway, say so in one line and move on.

## Commit core  [BRIEF, PROMPT]

Every sub-doc's Commit step points here.

**Run the wind-down re-scan before staging** — it files any un-flagged captures
from this session's discussion so they land in this same commit. File-only.

**Run the session-file cleanup before staging too**, so any deletions the user
accepts fold into this same commit.

**Shipped-slug cross-check (work-item closes).** When this session shipped work
items, cross-check each shipped slug named in this session's LOG entries against
Processed and confirm it's been removed. A work item is normally removed when
/next locks scope, so the slug should already be gone — this is the safety net. If
a shipped slug is still sitting in Processed as active work, surface it in one line
and remove it (or halt and ask) before committing.

A prior multi-item run shipped fourteen work items but left one in QUEUE.md —
genuinely built, never removed — so it re-presented the next session as unbuilt.
Trivial for a single-item close; the net earns its place on multi-item and
unattended closes. A planning close names no shipped slug, so there's nothing to
check. **Silent unless a stray slug is found.**

**1. Stage explicitly — name each path:** files this session changed (from
_build.md Changes), method docs updated during the session or close-out (QUEUE.md,
SPEC.md, LOG/), and the _build.md deletion where one was removed.

**2. Detect out-of-scope dirty paths.** Run `git status --porcelain` and compare
against the active build's file list. Any dirty path outside it is a user edit no
build staged.

```
RECOGNISE THE HASH-BACKFILL SIGNATURE FIRST — and skip the investigation:
    a dirty LOG/index.md or LOG/<slug>.md whose ONLY change is a placeholder
    hash becoming a real hash, in an entry heading or the start of an index line
        -> the session-start hook's automatic backfill, already announced in
           its opening housekeeping line
        -> DON'T open a git diff. DON'T explain it file-by-file.
        -> fold it in with at most a one-line note

any OTHER out-of-scope dirty path
        -> full treatment: surface it in a one-line summary and offer to stage
           it, investigating where the change isn't self-evident
```

This exact dirt appears every session and the answer is always "it's the backfill,
stage it," so re-investigating it is pure delay for zero decision value.

**3. The commit message is not drafted fresh** — it derives from the LOG entry
already approved at the entry step:

```
ONE work item shipped        ->  the message IS that entry:
(and plan/setup closes)          title = the index line's one-liner, verbatim
                                 body  = the approved rationale, verbatim
                                 # present by stating that identity plainly

SEVERAL work items shipped   ->  title = a one-line summary of what the run
(a multi-item /next run)                 shipped across all its items
                                 body  = each shipped item's one-liner, one
                                         per line
                                 # this roll-up IS genuinely new text — draft
                                 # it and show it for approval

staged extras (backfills,    ->  the body appends ONE line naming them
sweep edits, rolled-in user
edits from step 2)
```

**Never write a meta-description of the derivation** ("the rationale as approved,
plus an appended line naming the backfill…") — that reads as a third text the user
has to check, defeating the nothing-new-to-read point.

**4. No pre-commit ask.** The commit always happens at /done and its message was
already approved, so there's nothing new to confirm. Only the push is optional.

```
commit first (the safe, local action), THEN gate the outward push on consent:
    run one `git remote` check
        remote exists  ->  "Committed. Also push to the remote?"  (plain yes/no)
        no remote      ->  say it's committed; offer no push
```

A sub-doc may override to fit its session shape — done-plan.md commits and doesn't
offer push — but these commit-first mechanics stay canonical.

**5. Pass the message shell-agnostically.** Write it to a file in the project root
(e.g. `COMMIT_MSG.tmp`), commit with `git commit -F COMMIT_MSG.tmp`, then delete
the file. One mechanism on every machine — it sidesteps inline-quoting fragility
(embedded newlines vary by shell, and a PowerShell here-string needs its closing
token at column 0). The file is writable here because the sub-doc deletes _build.md
before Commit, or none ever existed, so the scope-lock isn't active on the root.

**6. Commit with `git commit -F`.** No fresh okay needed. Then offer push only
when a remote exists, and push only if the user accepts.

The LOG entry keeps its placeholder. The session-start hook backfills it at the
next session, as a working-tree edit folding into that session's commit — no
amend, no two-commit flow.

## Recommend next  [BRIEF, PROMPT]

Every sub-doc's final step points here, adding only its flavor delta.

**Plain-language guard.** Narrate the queue situation in everyday words — never
the background section-bookkeeping phrasing. Keep it accurate: **don't say the
queue is clear when work is still waiting to be sorted.**

**Overlap scan.** Before recommending, scan the still-unprocessed work for overlap
with the top processed item — work that contradicts, invalidates, or would benefit
it if sorted first. **State the result either way, not only when it blocks:**

```
nothing unprocessed              ->  say nothing's waiting for /plan
unprocessed but no overlap       ->  name what's waiting, give the plain verdict
                                     that nothing blocks it
overlap found                    ->  recommend /plan first, and name the overlap
```

The clean case is a plain assessment, not a hedge — "Three items are waiting to be
sorted; none touches the next piece of work, so nothing blocks it," never "there
may be overlap worth checking."

**Queue-state ladder.** When nothing blocks:

```
1. captures appended this session that affect the next work
       ->  recommend /plan, name the blocker
2. Processed work exists
       ->  name the next item, then ask whether the user is continuing into
           another /next now. If yes and a reorder applies, offer to reorder
           first so the next /next picks the right item.
3. Processed empty
       ->  "Queue is clear. Run /plan when you have more."
```

**File the forward-recommendation advisory.** When this step made a *concrete*
recommendation, file it as a capture at the top of Unprocessed, worded as advice,
consumed and cleared by the next /plan. A generic recommendation files nothing.

```
flavor deltas:
    build close   ->  the shared ladder is the whole recommendation
    audit close   ->  findings appended this session sit unprocessed, so the
                      DEFAULT is /plan, to sort them into work — name the count.
                      Only when nothing was appended does the overlap scan run
                      and the ladder apply (steps 2–3).
    plan/setup    ->  a fresh setup session whose only work item is the rough
                      first build item recommends /plan to scope it, NEVER
                      /next — the interview wrote that item deliberately
                      unscoped. Otherwise the shared scan + ladder apply.
```

## Rules

- **Do NOT skip the sub-doc's judgment steps even if the user says "just commit."**
- **Routing is automatic. Don't ask** — check for _build.md.
