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

Check for **this session's** build working file, `_build-<session-id>.md` — not
any other session's, which belongs to a build running in another chat.
**The check is automatic: route on what you find, silently.**

**Run every judgment step the routed sub-doc calls for, whatever the user says
about committing.** "Just commit" asks for the close to be quick, not for its
checks to be dropped — the steps are what make the commit safe to make, and they
are the close's whole substance.

**The read is unconditional.** When it exists, read it in full before
the close-out runs, *regardless of how much of the session you remember*.
Conversation memory enriches the LOG entry (tradeoffs, colour the file doesn't
capture) but never substitutes for the read. A "read it only if you don't
remember" condition hangs on Claude assessing its own memory, which fails exactly
post-/clear and post-compaction — when the session *feels* remembered but the
details are gone.

```
the build working file EXISTS  ->  read it, then route by the run's work-item flavors:
    build items (no tag)  ->  done-build.md
                              # a build that changed SPEC.md closes here like
                              # any other build — same steps, same commit core
    [audit] items         ->  done-audit.md
    mixed run             ->  each item closes through its OWN flavor's
                              close-out, one LOG entry per item, sharing the
                              single end-of-session commit

NO build working file          ->  done-plan.md, which carries all three
                                   no-build shapes and picks between them:
    a planning session
        (queue managed, captures processed, readiness line moved)
    a completed [user] item
    standalone handmade work
        (no planning either, and the tree holds uncommitted edits the
         session didn't make)
```

A no-build close touches QUEUE.md, SPEC.md and LOG/ and nothing else, whichever
of the three it is — which is why one sub-doc carries all three and a build close
never reads any of them.

Detect a completed `[user]` item from what the session can already see. The
detection rules and the close itself are in done-plan.md; a completed item can
coincide with a planning session, and that one sub-doc handles both.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit
core below, then return to the sub-doc for the recommendation.

**There is no test close-out** — the test flavor is retired. A check Claude can
run is part of building, closed by done-build.md. A check only the user can run is
a `[user]` work item, which never enters a build working file — so /done doesn't close it
*as a build*, but once the user has run it, /done records its completion and
removes it from the queue through done-plan.md.

## Verify completion  [SILENT] when every item is ticked; [PROMPT] when any is not

The build and audit close-outs point here for their completion check.

Read the build working file. Is every item ticked — each build item done, each audit finding
captured or dropped?

```
yes             ->  proceed
some unticked   ->  [PROMPT] ask: finish the rest (/next), or close partial?
                    Wait for the user's call.
```

**A partial close restores nothing, and that is the design.** An item is removed
from QUEUE.md only as it is ticked, so an unticked item is still sitting in
Processed exactly where it was. Closing partial means deleting the build working file and
leaving the queue alone — there is no copy-back step, no count to reconcile, and
nothing that can be lost by getting it wrong.

Before deleting the build working file, confirm the two halves agree: every ticked item is
gone from QUEUE.md, and every unticked one is still there. A mismatch means an
interruption landed between the tick and the removal — say what you found and fix
that one item, rather than proceeding.

**Build-close delta — reconcile against memory.** At a build close, where the
session is still remembered, reconcile the build working file against what you recall. If the
file and memory disagree — work that happened but went unticked, a Changes note
missing something memory knows was done — **that mismatch is itself a finding
about build discipline**, and it routes to Unprocessed. It's the only routine
check the build working file's accuracy gets before a fresh session has to rely on it. An audit
close carries no such reconcile.

## The close's checks report as one narration  [BRIEF]

Several checks fire across a close — verify completion, the staleness sweep, the
red-flag lifecycle, the wind-down re-scan. Combine what they turn up into one
"here's what came up: …" rather than letting each speak in turn.

**The wind-down re-scan's numbered set is its own message**, being something the
user must act on.

**Run the scrub checklist before writing a LOG entry** (skill-nonspecific-rules.md,
Scrub before writing). A LOG entry is committed text that quotes the session's own
discussion back, so it is the moment a real name or a case detail reaches a
permanent record.

## Staleness sweep  [SILENT] when clean; [BRIEF] when flagging

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

**Run the scrub checklist before writing** (skill-nonspecific-rules.md, Scrub before
writing). A LOG entry gets committed, and a session that ran on someone's real
situation is where a name or a case detail arrives without anyone noticing. Fix
what you find at the same level of usefulness rather than dropping the fact — and
don't tell the user the entry is clean afterwards, because you can't know that.

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

[Prose rationale — re-authored from the work's rationale in the build working file (or, for a
planning session, what motivated these queue changes), expanded with what was
learned along the way. Inline prose, no `Why:` label. Re-authoring is where
reasoning gets re-attributed by accident: credit the user only for reasoning
they gave in their own words, write mixed authorship as mixed, and don't wear
Claude's reasoning as theirs (skill-nonspecific-rules.md, rationale provenance).]

[per-flavor body fields]
````

```
per-flavor body fields — the only delta between flavors:

build       **Files touched:**       from the build working file Changes
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

**The frame, identical for every flavor.** Write the entry, then report in one
line what landed and where. A revert undoes a LOG entry, so it doesn't wait on
approval — the commit message does, because a commit is harder to unwind and
never becomes file content.

```
run shipped ONE item     ->  the commit message derives from this entry: title
                             from the one-liner, body from the rationale. Show
                             that message at the commit step — short, and the
                             user has the entry to read behind it
run shipped SEVERAL      ->  the commit message is a one-line summary of the
                             whole run, shown and approved at the commit step;
                             each item's entry still stands on its own
```

This entry is the session's summary — **there is no separate chat recap.** Before
writing it, check whether this session raised and resolved a concern or weighed an
alternative that lost; if so, carry it with why it lost.

**Reuse the item's candidate.** A ticked build item always carries one, written
at its tick and so describing what the build actually did rather than predicting
it — reuse it. Planning sessions have no candidate; author fresh against the same
rule.

Prepend to `LOG/index.md` after the header, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

**The 20% proportional cap that used to sit here was repealed on 2026-08-12**,
after measurement showed it fired on short entries rather than on long lines; do
not restore it or replace it with another figure. What the line must carry is in
the behaviour rules' Index entries section.

**Each entry is its own file under `LOG/`, date-prefixed** so the folder sorts
newest-first on a name sort — never appended to a shared log file:

```
session closing work items    ->  LOG/<YYYY-MM-DD>-<slug>.md
    (build, audit)                # one entry file per item, all sharing the date
session with no slug          ->  LOG/<YYYY-MM-DD>-<type>.md
    (planning, setup, handmade)   # e.g. 2026-06-09-plan.md
name already taken            ->  append -2, -3, …
```

**Every date written at a close is the close date** — today's date, at the moment
you are closing. That covers the filename prefix and every date written into the
words of a session record or a queue item alike ("processed 2026-08-12",
"cleared 2026-08-12"). One rule, no exceptions, so there is nothing to work out
in the moment. It is not the commit date, and the filename prefix is not a second
copy of the hash; its only job is the name sort.

**Where a session ran across more than one calendar day, say so in one plain
sentence in its record:**

> This session ran across 2026-08-11 and 2026-08-12.

That is the whole accommodation — no change to any filename or datestamp. A
session spanning two days is ordinary rather than exotic: it is what happens
whenever someone stops for the night, or runs out of usage and picks it up in
the morning.

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

## The record a routing step sweeps

Both close sub-docs route leftovers to Unprocessed, and both sweep the same
record. Defined once here; each points at it.

```
the RECORD a routing step sweeps:
    the build working file's notes
    any captures already appended at the moment of noticing
conversation memory  ->  a same-session BONUS pass, never a source the step
                         depends on
```

An audit run has a build working file like any other run — its findings are
ticked there — so the first line applies to both closes unchanged.

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

## Red-flag lifecycle at close

The sub-doc close-outs point here when the closing item carries a marker.
Clearing happened at processing, so the close **records** and does not re-decide.

Where a flag was cleared *this session*, record **how** in the session's LOG
entry:

```
designed out / fixed  ->  how the risk was removed
consciously accepted  ->  the informed-consent trail: what the user was warned
                          about, and that they chose to proceed
```

The LOG is where the how-it-cleared lives; the marker on the work item carries
only `State: cleared`. **Recording is unconditional once a flag clears** — the
record never rides only in chat or on the marker, because no later session
re-reads those for clearing history.

At a build or audit close the flag was cleared in an earlier /plan session, so
two things:

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

**Write every candidate to Unprocessed first, then report them as ONE numbered
set.** Nothing waits on approval before reaching disk — a capture in a
git-tracked QUEUE.md is recoverable without the user's help, which is the
write-first test. The user contests by number, and a contested item is reverted
or reworked one at a time.

Add them to this session's LOG entry's "Routed to Captures:" line as a
working-tree edit riding this commit.

**Why the set still arrives together.** Delivering all of them at once is the
bulk-approval inversion, which governs SEQUENCING — one item per message, or
all together — and never approval-before-write. Reading it as "show for
approval first" is what put this step in conflict with the write-first rule
that governs above it.

**State this sentence, as written, when the step runs:**

> I can't tell whether any of our earlier conversation has dropped out of view,
> so this is what I could still see rather than a guarantee I've caught
> everything.

**Say it as written rather than conveying its sense.** An instruction to
"explain the limit honestly" invites improvement, and improving it is exactly
what went wrong: a session once opened with "this has been a long session, so I
can only re-read what's still in view". Session length is a proxy Claude *can*
observe, standing in for the thing that actually determines the result — whether
the conversation has been compacted — and that is not observable at all. There
is no signal announcing it; a compaction that lands cleanly leaves nothing to
notice, in the same way a truncated file read looks complete from the inside.
So the substituted caveat invites the user to discount the result by a factor
that is fictional.

**The limit on the fix, stated rather than implied:** a fixed sentence is harder
to improve on than an intent, but nothing prevents a session rewording it and no
check will catch that. This reduces the odds; it does not close the hole.

Never name session length, duration, message count, or any other observable
proxy for compaction.

One thing to state, not fix: a fresh-chat /done has none of the session's
thinking in view, so there is nothing to re-scan.

**This is the only wind-down re-scan in the method, and there is no second one
to coordinate with.** /plan has none — a re-scan defined by the position "after
every item is processed" never reaches that position in a session that processes
in batches at the user's direction, so it attached itself to whatever felt like a
pause and ran three times in one session, twice at a moment no document names.
Each run is a stop-and-ask, so an invented cadence spends the user's turns on a
beat they did not ask for and cannot predict. Do not reintroduce one.

> "Re-read our discussion — nothing came up that isn't already captured."

## Session-file cleanup (throwaway artifacts)  [BRIEF, PROMPT]

Commit core points here, so it runs at every close. The build working file is
deleted by the close already; this generalises that lifecycle to *other* throwaway
files this session created. (Prevention comes first — temp files should have gone
to the scratchpad and never reached the project. This catches the ones that landed
anyway.)

Offer to delete only files meeting **all** of these:

```
Claude created or wrote them THIS session
    # established from the build working file Changes and this session's own edits.
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
the build working file Changes), method docs updated during the session or close-out (QUEUE.md,
SPEC.md, LOG/), and the build working file's deletion where one was removed.

**2. Detect out-of-scope dirty paths.** Run `git status --porcelain` and compare
against the active build's file list. Any dirty path outside it is a user edit no
build staged.

```
RECOGNISE THE INHERITED TAIL FIRST — and skip the investigation:
    a dirty LOG entry from a PREVIOUS session carrying a marked tail section,
    or a capture at the bottom of Unprocessed that no session here filed
        -> the previous session's post-commit tail, which by design commits
           nothing and rides into this commit
        -> fold it in with at most a one-line note

RECOGNISE THE HASH-BACKFILL SIGNATURE TOO — and skip the investigation:
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

**Where the staged paths include a method doc, name them in one line before
committing** — "staging QUEUE.md, SPEC.md and two log entries". One sentence, no
diff, no file-by-file account.

It exists because the check above is blind to the commonest case. It compares
dirty paths against the build's file list, so it cannot see anything inside a
file the session already owns — and QUEUE.md is the file a planning session edits
by design. A hand edit the user made there during the close, or a line another
session left in it deliberately, arrives inside a file Claude already considers
its own and is swept into the commit with no mention. Naming the files makes the
sweep visible.

**Two limits, and neither may be softened.** Naming the staged files makes a
swept edit **visible**, not **detected** — nothing cheap will ever tell the user
that a particular line inside QUEUE.md was theirs rather than Claude's. And
against the worst case it does almost nothing: where another session has already
*committed* this session's in-progress work under its own message, this line
produces the word "QUEUE.md" — true, useless, and silent about whose work is
inside. Do not describe it as covering that.

**3. The commit message is not drafted fresh** — it derives from the LOG entry
already written at the entry step. It is shown before the commit either way: a
commit is harder to unwind than a file edit, and the message never becomes file
content, so there is nothing to revert and nothing to read in the doc.

```
ONE work item shipped        ->  the message IS that entry:
(and plan/setup closes)          title = the index line's one-liner, verbatim
                                 body  = the written rationale, verbatim
                                 # show it, stating that identity plainly

SEVERAL work items shipped   ->  title = a one-line summary of what the run
(a multi-item /next run)                 shipped across all its items
                                 body  = each shipped item's one-liner, one
                                         per line
                                 # this roll-up IS genuinely new text — show
                                 # it for approval

staged extras (backfills,    ->  the body appends ONE line naming them
sweep edits, rolled-in user
edits from step 2)
```

**Show the message itself, verbatim, and nothing else about it.** A description
of how it was derived ("the rationale as approved, plus an appended line naming
the backfill…") reads as a third text the user has to check, which defeats the
nothing-new-to-read point.

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
token at column 0). The file is writable here because the sub-doc deletes the build working file
before Commit, or none ever existed, so the scope-lock isn't active on the root.

**5a. A staging step that partly failed is a STOP, not something to commit
around** [BRIEF, PROMPT]. Check that every path this close meant to stage is
actually staged — `git status --porcelain` and read what is in the index — before
running the commit. Where anything intended is missing, say plainly what did not
stage and why, and **do not commit.** Fix the staging and re-check, or let the
user decide.

The real failure this prevents: a staging command aborted partway when it hit a
gitignored path, and the commit ran anyway. Nineteen LOG entries describing that
commit's work were left out of it and had to be added by a second commit — after
which the session-start backfill correctly resolved each one to that second
commit, because with the files absent from the first, the second genuinely was
the oldest commit containing them. Every entry then pointed one commit past its
own subject.

Note what that rules out as the fix: the backfill rule behaved correctly on
inputs that were wrong, so nothing is added to it. Wrong hashes were one visible
symptom; entries missing from the commit they describe is the general failure,
and it is a partial commit either way.

**6. Commit with `git commit -F`.** No fresh okay needed. Then offer push only
when a remote exists, and push only if the user accepts.

**6a. An isolated session names its branch and warns about "remove"** [BRIEF].
Fires only where session_start reported this session is in its own worktree; in a
shared tree, say nothing. After committing, say plainly which branch the work is
on and that **it is not merged back** — the harness never merges a session
worktree, and choosing **remove** at exit deletes the worktree and the branch with
all the work in them. Use that word, because it is the word the exit prompt uses
and a user reads it as tidying up.

Don't try to merge here: git refuses to update a branch checked out in another
working tree, so an isolated session cannot merge itself into the main line. The
merge is offered at a main-checkout session's start instead, where session_start
reports worktrees carrying unmerged commits. Say that too, so the user knows the
work has somewhere to go.

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
2. work sits ABOVE the readiness marker
       ->  name the next item as information, and say a build wants a fresh
           session. No question, and no command string ending the message.
2b. Processed holds work but the cleared region is EMPTY (the marker is at
    the top)
       ->  say the next work still needs vetting, and point at planning.
           A build run would soft-stop here, costing a round trip.
3. Processed empty
       ->  say the queue is clear and that planning is where more work comes
           from.
```

**Rung 2 states the next item and stops there.** It used to ask whether the user
was continuing into another /next now — and a message that ends by asking a
question whose answer looks like a command is one keystroke from being run by
accident, because the harness offers the slash command it just saw as a
tab-completion. A user was caught by exactly that. Rewording the question is not
enough: the same defect was fixed once before, in plan.md's four-routes recital,
by removing the named command from that moment rather than by phrasing it more
carefully.

**A build wants a fresh session**, which is the user's decision and is the
reason rung 2 no longer invites one. A run inheriting a full build plus its
close is the opposite of the fresh short session everything here is designed
for.

**Rungs 2b and 3 name no command either.** Rung 2b exists because rung 2 used to
key only on "Processed work exists", which cannot tell work /next can run from
work that needs vetting first — so a close that had just emptied the cleared
region still pointed at /next, straight into a stop.

**A session makes exactly one commit, and the tail makes none.** That is the
whole shape, and everything below follows from it. The close commits; work
arriving afterwards is written to the working tree and left there, to be carried
by the next close. No amendment commit, no delta commit, no second close.

```
the close                ->  ONE commit. Everything the session did.
the post-commit tail     ->  writes files, commits NOTHING:
                               a capture appended to QUEUE.md
                               an append to this session's LOG entry
                               a hash the session-start backfill filled in
                             all of it rides into the NEXT close's commit
```

**Why the tail loses its commits rather than the tail losing its work.** Work
genuinely does arrive after a commit — a question answered, a reply sent, an
observation worth keeping — and recording it beats pretending the session ended.
So the thing to remove is the commit per increment, not the increment. A close
was producing two and three commits every time, and the user's word for it was
*every time*: this is a recurring shape, not one untidy session.

**The cost, stated rather than discovered: the tree is dirty between one close
and the next, always.** That is accepted, and it is what makes the dirt
*legible*. Uncommitted changes at a session's opening now mean one thing — the
previous session's tail, plus the backfill — so a session recognises the
signature instead of investigating it, exactly as it already does for the
backfill alone. Dirt that is always the same shape can be read at a glance;
dirt that is sometimes tail and sometimes an unexplained commit cannot.

**What was rejected, and why it is not reopened.** Requiring the close to leave a
clean tree cannot be done without either forbidding post-close work or committing
each increment — the first loses the record, the second is the defect. A second
lightweight close over the tail was weighed and lost for the same reason: it is
another commit wearing a different name, and it needs the user to decide when the
tail has ended, which nothing can tell them.

**So the close's staging check keeps its teeth**, because the dirt it must catch
is now sharply distinguishable: tail-shaped dirt is the previous session's LOG
entry, a capture at the bottom of Unprocessed, or a backfilled hash. Anything
else is a user edit and still gets the full treatment.

**After the close, if further work changes a file, offer once to append it to
this session's LOG entry** [BRIEF, PROMPT]. The entry is written and committed by
now, so anything done afterwards — a fix, a question answered, a piece of work
run on request — is invisible in the record unless the entry is amended. **The
amendment is not committed; it waits for the next close** — that is what the one
commit per session rule above means in practice at this exact moment, which is
the moment it was most often broken.

```
append, never rewrite   ->  a marked tail section on the existing entry, so it
                            reads plainly as work that came after the close.
                            Leave the index line alone unless the tail changes
                            what the entry is ABOUT.
once per tail           ->  not once per exchange. An offer reappearing after
                            every message is the nagging shape this method
                            keeps deleting.
only where a file        -> post-close conversation that alters nothing has
  changed                   nothing to record, and offering there trains the
                            user to decline.
```

The evidence is recurrence rather than one miss: the user has had to ask for this
amendment repeatedly, which is the same signal that carried the reply-draft
offer. A thing they keep having to ask for is a thing the method should offer.

**Announce a `[freeform]` item if Processed holds one.** /next will not build it —
it halts on it — so a close that recommends /next without saying so sends the user
into a stop. Say plainly what the item is and that it needs a session where the
work is done by hand rather than run from the queue, so they reach for that instead
of /next or /plan.

**File the forward-recommendation advisory.** When this step made a *concrete*
recommendation, file it as a capture at the top of Unprocessed, worded as advice,
consumed and cleared by the next /plan. A generic recommendation files nothing.

```
#### Last session advises processing <slug> next [forward-advisory]
```

**In the prose beneath, state conditions, not counts.** A condition stays true
however the queue reorders. Arithmetic against a snapshot does not, because the
advisory is written at a close and read at the next /plan's opening — and the
whole point of that interval is that work happens in it. Positions in the
cleared region are precisely what a build run changes.

```
write:      a /next run will halt on this item and build nothing past it
never:      it sits ninth, with eight items ahead of it
```

This trims nothing worth keeping. The advisory that failed named the right item,
gave the right reason, and named what to process alongside it — only its numbers
rotted, and by the time it was read the item it called ninth sat first.

The trailing `[forward-advisory]` is a fixed, reserved slug — always that literal
string, never the slug of the item it points at. Written any other way the
advisory is a heading with no slug at its end, which the queue lint flags on
every later edit and which stops the queue mover dead: it refuses on the whole
file, so no move or deletion can run at all while the advisory is present.

**The advisory is a transient orientation handoff, not work.** It is read at the
next /plan's opening to orient where that session starts, and cleared there, at
that same read (plan.md). Nothing about clearing it is this close's job. It never
runs through keep/delete and never moves into Processed. It stays in QUEUE.md rather than getting a file of its own
because it is read at the top of Unprocessed anyway, and a separate document would
be one more thing for the user to learn about for one transient line — what made it
misread as unprocessed work was never its location but that nothing in it said what
it was, which is why the heading text carries that now.

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

