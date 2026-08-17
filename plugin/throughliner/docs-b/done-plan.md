---
name: done-plan
docset: current
note: >
  Close-out for every no-build session. Reached from done.md's router when no
  build working file exists — /plan sessions, /setup sessions, method-doc-only
  sessions, a completed [user] item, and standalone handmade work.
---

# No-build close-out

Reached whenever there is no build working file. Three shapes arrive here and
they overlap freely — a planning session can also close a completed `[user]`
item, and either can carry hand edits.

```
queue managed, captures processed, readiness line moved, or a planning
    working file exists          ->  run every step below
a completed [user] item          ->  the Completed [user] items step, plus the
                                     LOG entry, commit and recommendation
the user made ad-hoc hand edits  ->  the Standalone handmade-work steps, plus
                                     the same three
```

The reorder, the marker placement and the `[user]`-placement step reach every
plan-type close — a /plan session, a /setup session, and a session that changed
only the method docs; none is /plan-only.

## Spec-sync gate  [SILENT] in sync; [PROMPT] on drift

**This is the only close that syncs SPEC.** A build close runs a *check-against*
instead (done-build.md) — it reads what was built against SPEC and reports a
contradiction rather than editing SPEC to match. Audits land no product changes,
so an audit close has neither.

Why the build close no longer syncs: a sync on a document the build never read can
only record what the build did, so it cannot catch a build that contradicted the
spec. /next now reads SPEC at run start, which is what makes a real check possible,
and the sync belongs where the decision that changes product truth is made.

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

No scope-lock is active at any close reaching this doc, so edit SPEC.md directly
in-session. Editing SPEC to match a decision the user already made this session is
RECORDING, not re-planning. That covers all three shapes alike.

**A decision made this session but not yet built satisfies the gate when its work
item lists SPEC.md.** This is the case the gate now meets by default, so say what
happens rather than leaving it to be re-derived. Editing SPEC the moment a
retirement is *decided* would make it describe a product that doesn't exist yet —
a false SPEC, not a synced one. Where SPEC still describes the shipped product
accurately and the item carrying the change names SPEC.md among its files, SPEC
moves when the behaviour does, and the gate passes.

A session that changed only queue ordering or captures touched no SPEC sentence
and passes silently.

## Standalone handmade-work close  [BRIEF, PROMPT]

Runs only where the user made ad-hoc edits by hand and wants them recorded.
**Never required:** hand edits left uncommitted are simply swept into the next
/done that runs. This exists for when the user wants them logged and committed as
their own clean record.

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

Write each entry's one-liner and rationale, then **report what landed.**

**3. Stage the hand-edited files explicitly** at the commit step. The commit
message is the approved entry; for several entries, the title names the
handmade-work close and the body carries each entry's summary. Unlike a planning
close, a handmade close **does** offer push when a remote exists — it's real
project work, not bookkeeping.

## Batch the human stops in Processed  [SILENT] when nothing moves; [BRIEF] when it does

**One pass, over Processed only: put `[user]` and `[audit]` lines at the end.**
Everything else the close used to reorder is repealed.

```
repealed — do not reinstate:
    build-order re-derivation across Processed
    the Unprocessed reorder by unblock-potential
```

Do **not** reintroduce `Blocks:` / `Depends on:` headers. The one dependency
field that exists is `Blocked by:`, written on the item that is held and naming
one or more slugs — the item lifts only when every one of them resolves — and
it is lint-checked precisely so it can't go stale the way those headers did.
Its sibling `Not before: YYYY-MM-DD` holds an item until a date rather than
until another item, and is lint-checked the same way. Everything else stays
prose slug-references.

**Place `[user]` and `[audit]` lines end-preferred**, after
contiguous blocks of build work. Both flavors force /next to stop for the user — a
step they must run, an audit whose findings they must approve — so one sitting
*inside* a contiguous build run interrupts an otherwise-unattended sequence.
Position them at the **end** of the block so the human-in-the-loop stops batch
together.

**Don't move a `[user]` or `[audit]` line past a build item that genuinely depends
on its outcome** — a real dependency wins; end-preferred is the default only
among items with no such constraint.

**Leave an `[audit]` that reads a tool item's output sitting immediately after
that item.** The dependency runs the other way from the case above — the audit
depends on the build — and it carries no `Blocked by:` line, because placement is
what orders the pair. Moving the audit to the end separates it from the tool it
runs, and the close happens after /next, so the separation arrives in time to
break the *next* run rather than this one.

Order here is low-stakes and reversible, so the narration is the catch-point
where the user can redirect.

**Use the mechanical mover — don't retype blocks.** Moving an item by hand means
retyping its whole prose block verbatim, which on a long queue silently degrades
to a partial sort and can corrupt an item with no error. Only the *decision* — the
desired order — passes through you; never the prose.

```
locate:  scripts/reorder_queue.py under the PLUGIN ROOT
         # the plugin root is the grandparent of the running skill's base
         # directory (.../<plugin-root>/skills/<skill>). Derive it from there
         # so it resolves wherever the plugin is installed — never hardcode.

invoke:  python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
             <Processed|Unprocessed> <slug1> <slug2> …
         # give the section's full desired top-to-bottom slug order
         # for Processed, place the marker with:
         #     --marker-after <slug|TOP|BOTTOM>
         # omit it to keep the marker where it currently sits

trust the self-check:  exits non-zero -> NOTHING was written. A slug-set
                       mismatch usually means the queue changed under you —
                       re-read it, rebuild the order, re-run.
```

```
narration scales:
    changes what /next would pick next  ->  flag it clearly
        "Moved [slug-a] above [slug-b] so it builds first — say if not."
    a trivial tidy (no pick-order change)  ->  one line
    no reorder needed                      ->  say nothing
```

## Position the cleared-to-run line  [SILENT] when unchanged; [BRIEF] when it moves

Walk Processed top-down and put the `--- Cleared to run above this line ---`
marker just below the last item the user has agreed is ready to build.

```
every processed item greenlit  ->  the line goes at the BOTTOM of Processed
none greenlit                  ->  at the TOP
setup / method-doc-only session with no processed work
                               ->  no line to place, nothing to reorder.
                                   Say nothing.
```

Narrate where it lands **only when it actually moves** — one plain line:
"Everything processed this session is cleared to run; the line sits at the
bottom." When your walk confirms it's already correct, confirm silently.

**Hold back an item that depends on unverified work.** A processed item must not be
cleared if it depends — by a slug reference in its prose — on another item that has
been **built but whose verification is still pending** (a host-side item shipped
but not confirmed live after reinstall, or an observed check simply not run yet).

```
dependency BUILT only            ->  NOT enough. Keep the dependent below.
dependency BUILT and VERIFIED    ->  no hold; it may clear.
```

The why is autonomy: a cleared item can be built unattended with no user in the
loop, so clearing one that rests on built-but-unverified work would let the run
stack committed work on a foundation that might later fail its check. Narrate it
when it holds an item back — one line naming which item waits on which.

**Re-derive prerequisite state from LOG, not from memory, by reading the
dependency entry's transcribed tick.** Every built item's entry carries either
`done, confirmed` or `done, UNCONFIRMED: <what still needs running>`, written into
the build working file at the moment the work happened and copied into the entry
at the close (next-build.md, done-build.md). Read that field. This rule and the
`[user]`-placement rule below both depend on the answer, and a fresh short session
has no memory to fall back on.

**Read the field, don't infer the answer from the entry's prose.** The field
replaced exactly that: this rule used to depend on whatever a previous session
happened to write in sentences, so a rule that must know whether something was
verified was reading a distinction nothing guaranteed. An entry with no such field
predates the mechanism — treat it as unconfirmed and say so, rather than reading
its prose for a claim it may never make.

**Name the holding fact when placing any item below the marker.** One line in
the item's block, whichever holds it:

```
Blocked by: [slug]
Blocked by: [slug], [slug]      # a group: lifts only when ALL resolve
Not before: YYYY-MM-DD
```

Every slug must resolve to a real work item in this queue, and a date must be a
real `YYYY-MM-DD` — the queue lint checks both. Below the line means held by a named
queue item or by a date, and nothing else.

```
a date is what it waits for      ->  write the date. No blocker item: the date
                                     resolves itself, so nobody confirms it
nothing holds it                 ->  it goes ABOVE the marker, not below
it waits on something else in    ->  file that as its own item in Unprocessed
    the world (a restart, a          first, then name it here. /plan will
    reply, a site going live)        process it like any other work.
you can't yet say what it        ->  Unprocessed — it still needs thought
    would build
```

This is the enabling half of the below-the-line revisit: with a slug the revisit
is a single check per item, and with a sentence it was an interpretation. It also
closes a failure the sentence version kept producing — an item waiting on
something nobody had filed, so the wait could never end.

**Place ready `[user]` walk-through work above the marker.** The marker is the
single gate for walk-throughs as well as builds — /next walks a `[user]` item
through only when it sits above the marker.

```
prerequisite work shipped (built, and verified where a live check was needed)
    ->  place the [user] item ABOVE the marker
prerequisite still pending
    ->  it stays BELOW, exactly like any other not-yet-ready item
```

**Anti-pattern: don't hold a `[user]` item below the marker merely because it's the
user's to run.** Being a `[user]` item is not a reason to shelve it — only a
pending prerequisite keeps it below. This lives in the /plan close rather than
/next so the marker stays one positional gate, instead of /next growing a second
readiness check of its own. Narrate it when a `[user]` item moves above the marker
— one line naming which is now ready.

## Completed `[user]` items  [SILENT] when none; [BRIEF] when closing one

A `[user]` item never entered a build working file, so it isn't ticked and closed
like a build. This is the close that records it and removes it from Processed, so
a finished item doesn't strand in the queue and get re-presented by the next
/next. It runs both as a close of its own and inside a planning close.

**Identify completed items from what the session can already see.**

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
mentioning it is already a supported path.

```
1. take the completed item(s) from what the session can see  [SILENT]
   # don't list the other [user] items still sitting in Processed — an item
   # whose completion isn't visible simply stays where it is
2. write a LOG entry per completed item, named after its slug
   # records what the user did and its outcome; write it, then report it
   # if it carried a red-flag marker -> run done.md's Red-flag lifecycle
3. remove each completed item from Processed
   # this is what stops it being re-presented
```

Fold each entry into this session's records alongside any planning entry, and its
slug into the commit. When nothing was mentioned and nothing was walked through,
say nothing. A remote-gated push offer applies as normal — a completed `[user]`
item is real project progress, not bookkeeping.

## 1. Write LOG entry  [DISCUSS, PROMPT]

Follow done.md's **LOG entry files** section, using its **Plan / setup** body
fields (`Queue changes`; `Work processed`). Planning sessions carry no
index-entry candidate — author the index entry fresh.

If a red flag was cleared this session, record **how** per done.md's Recording a
cleared red flag: for a design-out, how it was eliminated; for an acceptance, what
the user was warned about and that they chose to proceed. Clearing happens at
processing, so /plan is where this record is written.

**Read what this session did off the queue itself, not off memory:**

```
git diff HEAD -- QUEUE.md
```

That is the mechanical record — every item kept, every item deleted, and the
reasoning written into each one as it was processed — so the entry's Queue
changes and Work processed lines are filled from the artifact rather than
reconstructed. It is the same argument the method already makes for preferring a
generated digest over a paged read: code cannot silently truncate, and memory can.

**Skipped items are the one thing the diff cannot see, and they are deliberately
not recorded anywhere.** Skipping moves nothing and edits nothing, so it leaves no
trace; a skipped item simply returns next session. Don't reintroduce a file to
hold them.

## 2. Commit

Run the commit core in done.md. Staged paths are the changed method docs
(QUEUE.md, SPEC.md, LOG/), plus the hand-edited files where this was a handmade
close — planning sessions touch nothing else.

**The push offer differs by which shape closed, so decide it before running the
core:**

```
planning / setup / method-doc-only  ->  commit, and DON'T offer push. Planning
                                        state is local bookkeeping, and push is
                                        reserved for shipping — in a
                                        self-hosting project a push fires the
                                        full ritual off a commit that shipped
                                        nothing. A default, not a prohibition:
                                        push stays available when the user asks
                                        or is deliberately backing up.
completed [user] item / handmade    ->  offer push as the commit core does.
                                        Both are real project progress.
```

## 3. Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Plan / setup close** delta: a
fresh setup session whose only work item is the rough first build item recommends
/plan to scope it, never /next; otherwise the shared overlap scan + ladder apply.
