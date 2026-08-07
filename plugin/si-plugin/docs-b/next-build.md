---
name: next-build
docset: B
note: Execution procedure for build-flavor work items. Reached from next.md.
---

# Build procedure

next.md routes here for each build item (a work item with no flavor tag).

## Execute  [SILENT]

The silence governs the **success path** — making changes and ticking the item
when things go fine. It is not a gag on the moments that must speak: reporting a
failure, asking before scope grows, and revealing a readable edit's new text all
speak. A tag on one of those overrides this step's silence.

**No pre-edit preview.** Don't precede an edit with a point-form list of what
you're about to change. The work was already agreed in /plan, and a "here's what
I'm about to change" beat before an edit that lands instantly is noise. Holds for
every edit, readable or code.

**Readable edits reveal their new text** — informational, not an ask.

```
readable content (a doc, copy, a spec section — anything a person READS)
    ->  surface the actual new wording AFTER the edit
    ->  no approval ask; the change was already agreed in /plan

code
    ->  no reveal. A non-coder can't review code text the same way.
    ->  success path stays silent (still no preview)
```

Why it's worth surfacing: the exact wording is produced here in /next and was
never seen in /plan, which agreed only the intent. This is the first time the user
meets the real words.

**How the reveal renders** follows the doc-bound-text rule (plugin-behaviour.md).
The text is doc-resident by the time it's revealed, so: a short summary of what
the new wording does, plus a link to the edited file with the exact heading text
of the section that changed, and the full new text on request. Never line-anchor
a link to a `.md` file — the desktop app opens it at the top and silently
ignores the anchor, so the link promises a position it won't deliver. And only after the
write is confirmed by a re-read.

**A small mid-build tweak to a just-surfaced readable edit is in scope**
[PROMPT]. Once the new text is visible the user may ask to change one bit. That
refines the build's already-agreed work product, so: make it, reveal the updated
text, and record it in _build.md Changes so it folds into the LOG entry /done
writes. No separately logged object, no /plan round-trip. A request that's
actually new scope — a different feature, or a change to something that already
worked — routes out via Scope management below.

## Build the item

```
1. read relevant existing code or context
2. make the changes                        # no point-form preview first
3. if readable content -> reveal the new text (informational, no ask)
   if code             -> stay silent
4. tick it: - [x] item description — done
5. remove the item from QUEUE.md THROUGH THE MECHANICAL MOVER:
       python <plugin-root>/scripts/reorder_queue.py QUEUE.md \
           --delete <slug> Processed
                                           # tick first, then remove —
                                           # destination-first at every step
```

**The removal goes through the mover, never a hand-edit and never a shell
splice.** It removes the whole block byte-exactly, refuses rather than guessing on
an unresolvable or ambiguous slug, and re-anchors the readiness marker if the
removed item was what the marker sat after. This is the *highest-frequency*
removal in the method — once per item, in every build loop — and the one that runs
with no user present to notice a shortcut being taken, which is exactly why it
must name the tool rather than leave the operation to judgment.

**Read `_build.md` before stating anything about the run's progress**, and compose
the statement from what it returned — how many items remain, which one is next,
what was ticked. Not from memory of the run. `_build.md` is written to at every
tick precisely so the run does not have to remember, and an unattended run is
where a wrong state claim has nobody watching. This is the standing rule in
plugin-behaviour.md's Context awareness section, firing here.

**Before building, and again whenever the work stalls: is this item's goal
already met by a tool the user has?** If it is, stop building — say so plainly,
name the thing that already works, and tick the item. Don't build a second
route to a result that already exists (plugin-behaviour.md, the
don't-hand-build counterweight). This fires *mid-build*, not only at the start,
because that is where it was actually needed: a run spent most of its length
trying to obtain Claude's own command-line route to two capabilities the user
already had working, until the user stopped it with *"why are we doing it this
way? why can't i just use android studio like i always do?"*

The condition is checkable rather than a judgment: the goal is met by something
the user has. It is not "never write anything a tool could write".

**A check Claude can run is part of building, not a separate test.** Run whatever
verification you can — read the code back, run a command, inspect output, check
file content — as part of getting the item right.

```
a check Claude CAN run   ->  just building
a check needing the user ->  a [user] work item, which /plan would have set as
                             its own item; /next walks the user through it
```

If mid-build you discover the work needs a user-run check that isn't already a
`[user]` item, route it (see Course-correction) — don't invent a deferral here.
The one sanctioned "not now" is the set-aside marker (plugin-behaviour.md, Set
aside), and it exists only for the user's own stop — it is never yours to
reach for.

## File structure — split by independent unit

**Fires only when the build creates or grows the project's files and there's a
genuine choice about how to split the work across them.** A build that only edits
existing files raises no such choice, so it gets no file-structure recommendation.
When it does fire, this is guidance you offer, not a hard rule — file structure
stays case-by-case.

```
genuinely independent unit        ->  split into its own file
    (a self-contained tool, a standalone path through the app)
content reasoned across as one    ->  keep together, even when large
    connected whole
```

Splitting pays off **because the AI does the editing**: an edit's blast radius is
one file, the AI reasons over less at once, and a mistake is contained by the file
boundary. That contained blast radius is what makes it worth the cost.

The counter-force that bounds it: an AI reasons *less* well across files than
within one. So closely interdependent logic that's constantly reasoned about
together stays in a single file — splitting it would make the AI's job harder.

## Rules during build

Stay within the active run's described work. Growing past it needs approval first.

**Accumulate close notes** as you go, so /done needn't re-explore:

```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
```

## Scope management

**When a mid-build discovery is work only the user can run** — a rename you can't
do, an account action, a device step — **file it as a `[user]` work item, never float
it as a live question.** The failure to avoid is waving it off as "separate work
you'd handle yourself" or asking a yes/no about it: that leaves real work living
only in chat. If you can't yet script every step, file the line with a rough
walkthrough anyway.

### User raises something out of scope  [PROMPT]

```
1. write the capture into Unprocessed, placed per the Captures placement rule
   (narrate the placement)
2. put the wording in front of the user for approval — a short summary plus a
   link with the heading text, full text on request. Remove it if they say no.
3. ask "anything else?" — repeat until no
4. resume the build
```

**Coherence exception** (narrow, keyed to why-pipeline coherence): if the item
would share the built item's log entry and index line, and folding it in makes the
work *easier to find later*, add it to _build.md as part of this item's work
(appending any files it names to `Files:`) and continue. **The test is the two
conditions named in this paragraph — one shared log entry and index line, and
easier to find later — not user convenience** (there is no separate body of
"coherence rules" to consult; this is it). **When uncertain, capture.**

### Scope grows during the build

The trigger is growth against **the described work**, not the Files: list. And
the first question is which of two things happened, because they get different
answers:

```
THE WORK GREW               ->  WIDEN AND NARRATE, then CONTINUE.
  the described work is         Append the file to _build.md's Files: list, say
  clear; it turns out to        in one line which file you added and why, and
  need a file the list          carry on. The addition rides into the commit,
  didn't name                   where it is as readable as any other change.

THE ITEM WAS UNDERSPECIFIED ->  HALT and surface it  [PROMPT].
  you can't tell what the       Building it means inventing scope the user never
  described work changes        agreed to, and no amount of narration fixes
  inside the files it names     that. This is the same seam /next self-scoping
                                already uses.
```

**Widening is permitted because the mechanism always permitted it — the halt was
instruction, not enforcement.** `_build.md` is classed alongside the queue and
the log, so a build has always been able to write to its own Files list; the
hook's own denial text says as much. So this costs no hook change, and the
scope file being editable is not a new risk being taken on.

**The narration limb is NOT optional, and it is what makes this safe.** An
expansion that is permitted but unannounced is strictly worse than one that
halts: the check becomes a human reading a diff, and that only works if the
change is visible where they are looking. One line, at the moment you add the
file.

**Why the halt was worth trading away.** /next is unattended in practice, so
every legitimate scope discovery ended a run that could have continued. That is
not hypothetical — a real build's self-scoping caught a genuine ripple and could
only report it by halting mid-run, which is exactly the interruption an
unattended run should not need.

```
significant  ->  still propose splitting. Finish what's scoped, /done to close,
(many files,     then /plan to queue the rest. Widening covers a file or two the
 design          work turns out to need; it is not a licence to absorb a second
 uncertainty)    piece of work.
```

**A SPEC change the build discovers it needs is a legitimate scope-grow.** Name
the change and ask — "this needs SPEC to say X instead of Y — add SPEC.md to
scope?" — then append SPEC.md to `Files:` before editing. Safe in-build because
spec-driven development wants the spec to move in the same commit as the behaviour
change, and the /done-build spec-sync gate backstops it. **A SPEC change is
product truth, so it always gets the explicit ask** — it never rides in silently.

## Mid-build course-correction

### Claude discovers user-runnable testing is needed  [PROMPT]

When something will need user-runnable testing beyond this build — a visual check,
physical-device behaviour, a subjective judgment you can't verify — and it isn't
already a `[user]` item:

```
1. append it to Unprocessed as a [user] work item (what needs checking, and why),
   then put the wording in front of the user for approval where it now sits
2. confirm and resume — name what you filed, then carry on
   # "I noticed X, filed it, resuming." NOT "anything else?"
3. resume the build
```

**Step 2 is confirm-and-resume, not an invitation for more, and the distinction is
who raised it.** This procedure is Claude-raised by construction — you noticed the
gap, the user didn't — so it closes by stating what was filed and continuing. The
"anything else?" loop belongs to a *user*-raised capture, where asking respects
that they were the one interrupting. Inviting more on something you raised yourself
turns your own observation into an open-ended interruption of a build the user
already approved.

Don't attempt the check inline if it genuinely needs the user, and don't extend
this item's scope to include it.

**Before assuming a device or environment is absent, check.** Ask whether one is
available rather than assuming none is. And before using any connected device, ask
permission — "May I use your connected device to test this?" — then wait. A
connected device you touch unexpectedly is a consent surprise; a check wrongly
skipped on a guess sits unrun for weeks.

### Going in circles  [PROMPT]

/next is unattended in practice — it works faster than the user can follow — so an
item that silently thrashes wastes the run with no one watching.

```
signature of no progress on one item:
    the same error recurring
    an empty diff (an edit that changes nothing)
    the same check failing the same way
        ~3 times  ->  STOP. Don't keep trying.
```

Tell the user plainly what repeated — the exact error, or what wouldn't change —
and hand them the decision via Approach not working.

Judgment, not a counter: three is a rough trigger and the point is to surface a
stuck item. The old runner's iteration and spend ceilings are deliberately not
recreated — they were arbitrary and undetectable, and session length is handled at
plan time.

### Approach not working  [DISCUSS, PROMPT]

```
1. STOP building — don't push through a broken approach
2. state the problem plainly: what you expected, what happened, why this
   approach won't work
3. propose a path forward
4. WAIT for the user's call — don't pick a path without confirmation
```

```
adjust scope      ->  drop the item, add a prerequisite, or change the approach.
                      Update _build.md to match.
abort and requeue ->  if the item is unsalvageable:
                        a. LEAVE IT WHERE IT IS — it was never ticked, so it
                           is still sitting in Processed. Nothing to return.
                        b. append any captures surfaced during the attempt
                        c. append the reshape direction, naming the item's slug
                        d. tell the user to run /done
```

**There is nothing to return, and step (a) says so rather than performing a
move.** Items leave QUEUE.md one at a time, at each one's completion tick — so an
aborted item never left. Read literally, an instruction to "return it to Processed"
performs an *insertion*, which is not /next's to make: a run removes items from
Processed and never inserts them, and the queue lint flags a heading appearing under
Processed while a build is active. Repositioning is warranted only where what was
learned during the attempt changes where the item should sit; that is a judgment
about order, not a recovery step, and it goes through the mover like any other move.

The reshape-direction trigger is mechanical: *abort + a reshape direction or
learning the queue needs in conversation = capture needed.* Unrouted, it survives
only in the LOG entry, which /plan doesn't read at planning time, so the item
re-presents unchanged at the next /next.

_build.md stays in place so /done's router still fires the build close-out. The
difference: the LOG entry describes the attempt and why it was aborted, while the
item itself simply stays in the queue, which is what the queue was already saying.

## Context management

You can't sense the context window filling — you only learn a session is wearing
thin when the **user** says so. So this isn't a trigger to watch for; it's what to
do when the user reports the squeeze.

```
most of the run is ticked      ->  finish and /done. Short-term memory is enough.
significant work remains       ->  close partial: /done what's ticked, requeue
                                   the rest. The next session picks up cleanly
                                   from _build.md and QUEUE.md.
```

Either way, pair it with the fresh-session handoff offer.

## Completion  [BRIEF, PROMPT]

When this item is done, next.md moves to the run's next. When the whole run is
built (every Claude-work item ticked, any `[user]` item walked through):

```
1. tell the user the build is complete
2. say: "Run /done to record this and commit, or tighten what's already built
   before closing."
```

Tightening means refining done work — not raising new work. Anything new routes
through the existing paths. **No chat summary of the changes** — the LOG entries
/done writes are the single session record.

**Do NOT delete _build.md yourself.** That's /done's job.
