---
name: next
docset: B
note: >
  Docset B is the light 5-series docset, authored by subtraction from docset A
  (docs/). Register: structure in typed blocks, everything else in prose, tags
  inline.
---

# /next procedure

You are building the cleared work from the queue. /next works the Processed
section top-down — building Claude-work items, walking the user through user-work
— scope-locked to the files that work touches.

## What /next runs on

QUEUE.md holds two sections: **Unprocessed** (captured, not yet processed) and
**Processed** (agreed, ready). /next builds only from Processed, and only from
above the cleared-to-run marker.

```
run       = Processed[ top .. `--- Cleared to run above this line ---` )
flavor(item):
    (no tag)  ->  build   ->  next-build.md
    [audit]   ->  review  ->  next-audit.md
    [user]    ->  walk the user through it; never built
```

**Never pick an item from past the marker.** This is a standing rule, not a
branch condition — it holds at every step, on every path through /next.

The run includes any `[user]` items among the cleared work; Step 3 walks the user
through each *without ending the run*. The marker is the only thing that bounds a
run.

## Step 1: Pre-flight

### 1. Active build check

```
exists(_build.md)  ->  [BRIEF]   offer to resume; read it for state
otherwise          ->  [SILENT]  no output; continue
```

`_build.md` holds an interrupted build's progress and remaining work, so resuming
picks up where it stopped instead of starting over.

### 2. Find the run  [SILENT]

Read Processed top-down and take everything above the marker.

```
early exits:
    Processed[top] == marker      ->  NOTHING_CLEARED
    marker MISSING from Processed ->  NOTHING_CLEARED   # fail closed
    run has no build/[audit] item ->  ALL_WALKTHROUGHS
```

**A missing marker means nothing is cleared — never everything.** The run is
defined as everything above the marker, so with no marker the range has no
terminator; reading that as "all of Processed" would hand an unattended run
work nobody cleared, including work deliberately held below the line. Tell the
user the marker is missing, recommend /plan to restore it, and stop.

**On NOTHING_CLEARED** [BRIEF] — tell the user the next work isn't cleared to run
yet, recommend /plan to vet it, and stop.

**On ALL_WALKTHROUGHS** [PROMPT] — there's nothing to build, so skip Step 2's
build scaffolding entirely and go straight to Step 3's walk-through branch.

**Why the run is marker-bounded rather than stop-at-first-`[user]`.** Step 2
builds all the Claude-work, then Step 3 walks the `[user]` items. The two passes
never interleave, so no cleared Claude-work is left unbuilt — even when a `[user]`
item sits mid-run.

**Never check whether a `[user]` item is already done.** Not up front, not in
passing, not as a trailing note. A `[user]` item is walked through, and that is
all — its whole lifecycle carries no completion ask. If the user has already done
one, they'll say so, and that's the moment it gets recorded. Asking treats ready
work as probably-already-done and makes the user re-assert it before you'll help.

### 3. Present the run and offer the off-ramp  [BRIEF, PROMPT]

Put the run in front of the user and invite a last-glance change **in the same
message** — presenting and offering the off-ramp are one beat, not two.

**Don't ask "Ready?"** Invoking /next already signalled readiness, so a
permission-to-start question is redundant. What the pause is *for* is the one
deliberate human checkpoint before /next runs unattended-in-practice: a last
chance to change scope or reorder. Frame it as that.

```
render(run):                    # full rule: plugin-behaviour.md, doc-bound text
    a short list naming each item (its exact heading text, or a faithful
    shortening when headings run long), plus a link to QUEUE.md; the full
    item text is offered on request, never front-loaded
```

These items already exist in QUEUE.md, so confirm the link resolves before
sending it — and link to the file only, never with a line number, which is dead
for `.md` in the desktop app.

**Where the run's items share a file scope, name the group and its shared scope
in ONE line** — "these three all change the behaviour rules, so they build as
one pass." That line *is* the explanation of the order: the ordering unit is the
group, and the group's reason is derivable from the Files lists on the spot, so
no handoff artifact and no second advisory has to carry it.

**It must stay one line.** This step is `[BRIEF]` and carries the deliberate
passage below forbidding caveats, warnings and proposed pause points, on the
stated grounds that the expense is not the warning but the negotiation it
invites. A group explanation that grows into a paragraph is the same cost in
different clothes.

Close that same message with the off-ramp, e.g. **"Say the word to change scope
or reorder — otherwise I'll start."**

```
user wants a change  ->  route to /plan
user says go         ->  Step 2: lock scope, build begins
```

Present-once is deliberate: a separate "here it is" beat followed by a separate
confirm beat is the redundant gate this collapses.

**Don't size the run.** Present every cleared item. Don't warn the run is long,
don't suggest splitting it, don't propose building half now and half later, and
don't hedge the off-ramp with a caveat about how much will fit. The canonical
rule is in plugin-behaviour.md (Context awareness) and in next-build.md: **the
trigger for any context conversation is the user's report, never you noticing on
its own.** It is restated here because this is where the impulse actually fires —
the canonical statements sit in context-management sections that answer *what to
do when the user reports a squeeze*, so a session standing at this step has the
disposition toward caution with nothing nearby contradicting it.

This costs the user a real thing. The warning isn't the expense — the
*negotiation* is: a round spent re-litigating how much fits, every run, against a
risk that has not once materialised. Runs get talked down to half and then finish
the other half fine.

The same rule covers caution expressed as process, which is the form that slips
past a narrowly-read version of this: proposing pause points, staged markers, or
"we should stop and check in partway" for a long run is the same warning wearing
different clothes. If the user asks how much is cleared, answer plainly — that's
their question, not your caveat.

There is no blocker gate, push marker, or unpark/staleness scan — those belonged
to the old model and are gone. Ordering and readiness are settled in /plan before
work reaches the cleared region.

## Step 2: Lock scope  [SILENT]

Once the user confirms:

**1. Pre-generate the candidate index entry** for each Claude-work item — artifact
touched + nature of change (plugin-behaviour.md, Index entries). This is the shape
/done writes at close, so pre-generating makes it reusable: if the item builds as
planned /done reuses it verbatim, if scope shifts /done re-authors it.

**2. Self-scope.** Read each Claude-work item's description and rationale, work
out which files it will change, and list them. `[audit]` items name no files —
an audit reads and reports — so a run of only audit items gets an empty Files
list, locking the session to the queue, the log, and its own working file.

Two situations must not be conflated:

```
you CAN'T tell which files THIS item's       ->  underspecification
    described work would change, OR the          SURFACE IT. The only case
    item names files but not what changes        that halts — building it means
    INSIDE them                                  inventing scope the user never
                                                 agreed to.

you CAN scope it, but notice OTHER work      ->  adjacent-work discovery
    worth doing beyond it                        CAPTURE AND CONTINUE on the
                                                 decided scope. Never a blocking
                                                 scope-ask.
```

The test has two limbs because the first alone doesn't discriminate: design
work almost always names files — "Files (rough): plugin-behaviour.md, plan.md"
is exactly what an undesigned item looks like — so a files-only test passes it
and the run proceeds with a file list and nothing to build from. An item is
buildable only when it says what changes *inside* the files it names.

A blocking ask on adjacent work both defeats the unattended run and reopens a
scope decision reserved for /plan. The extra look self-scoping gives is preserved
by capturing what it finds, not by asking.

*Worked example.* Building a terminology rename, self-scoping enumerates the docs
the item names. A doc silent on which sections change → underspecification,
surface it. Noticing the *hooks* also carry the old term when the item didn't
list them → adjacent-work discovery, capture it and continue.

**3. Create _build.md:**

````markdown
# Active Build

Run: [flavor + slug of each Claude-work item, top-down]

Entries:
[For each Claude-work item: its flavor tag (or "build"), its description, and all
its rationale text — but drop any line starting with `Files:`.]

Index entry candidates:
[the pre-generated entry, one per Claude-work item]

Files:
- [each file the run's items will change — one bare path per line, nothing else]

Progress:
[empty — ticked as each item completes]

Changes:
[empty — accumulated as each item completes]
````

The `Files:` section feeds the scope-lock: pre_tool_use allows edits only to
those files plus the queue, the log, and this session's own working file, and
denies everything else — SPEC.md is not in that set, so a build edits it only by
listing it here. **Lines must be
bare paths** — the hook matches each line as an exact path, so any annotation
becomes part of the path and silently breaks the match. Make sure no other line
in the file starts with `Files:`.

**4. Leave the queue in place — items are removed one at a time as they build,
not here.** _build.md now holds the whole run (written in full at scope-lock,
before anything is removed), but each Claude-work item stays in QUEUE.md until
the moment it is ticked complete in Step 3. The queue visibly shrinks as the
run progresses, and it always tells the truth: an item still showing means not
built yet. This is also the safer shape on abandonment — a run that dies
partway leaves the queue holding exactly the work that was never done, instead
of having stripped everything up front into a file the close deletes.

```
Claude-work items  ->  in _build.md AND QUEUE.md while the run works;
                       removed from QUEUE.md at each item's completion tick
[user] items       ->  STAY in QUEUE.md throughout
```

The duplication window is harmless — _build.md is the crash-recovery source of
truth throughout.

**A run removes items from Processed and never inserts them.** The per-item
removal (and the close's marker repositioning) is /next's whole write access to
Processed. New work found mid-run is captured to Unprocessed; moving anything
*into* Processed is processing, which is /plan's, because that decision is the
user's. The queue lint backstops this — a heading inserted under Processed
while a build is active gets flagged.

A `[user]` item is walked through in Step 3, not built, and is closed later by
/done or /plan. Extracting it into _build.md would strand it, since _build.md is
deleted at close.

**5. Narrate the lock** [BRIEF] — one sentence, in user-facing terms: _build.md is
the build's working file — it carries the run's work while QUEUE.md stays free,
lists the files the safety check allows, tracks progress so an interrupted session
can resume, and holds the reasoning /done writes into the session record.

```
progress format:
    build item  ->  - [x] item description — done
    audit item  ->  - [x] Finding description — captured | dropped
```

_build.md is the crash-recovery mechanism: if the session dies, the next session
sees it and offers to resume.

## Step 3: Work the run

Two passes: **build all the Claude-work items first, then walk the user through
the `[user]` items.** This is what lets a `[user]` item be walked through without
terminating the run — the Claude work is all built regardless of where the
`[user]` item sat in the queue order.

```
build item (no tag)  ->  read and follow next-build.md
[audit] item         ->  read and follow next-audit.md
```

Between build items, keep going autonomously — the user confirmed the whole run
at the Step 1 off-ramp, so there's no per-item re-confirmation. As each item
completes: **tick it in _build.md Progress first, then remove it from
QUEUE.md**, then start the next. Tick-then-remove preserves destination-first at
every step — there is never a moment when an item exists in neither file.

**Resuming from a mid-run pause**  [PROMPT]. Some work items build in a deliberate
stop — switch models here, have the user judge this, check that before continuing.
Coming back from one, ask **the one thing the pause was for**, and nothing else:

```
the pause's own question   ->  ask it, alone, and wait
anything else it surfaced  ->  file it, or hold it for the run's close
```

The pull here is to bundle — the pause surfaced two or three things at once and
they all feel due now. Resist it. This is a stop the procedure itself created, so
without a shaped move for coming back the move gets improvised, and improvisation
bundles: that is exactly how a live run once merged "does this read right?" with
"should the rest be its own /next?" into one message despite the one-at-a-time
rule being present and complete. Then carry on with the run as normal.

### Walk-through branch — the `[user]` items  [SEQUENCE, PROMPT]

Once the Claude-work is built (or if the run had none), walk the user through each
`[user]` item still in the cleared region. Walking one through does **not** end
the run — it's the last pass of a run whose Claude work is already done.

**One item at a time — never bundled.** Each in its own message, led by its own
walk-through. Finish one fully — or record the user's stop — before moving to
the next. (This is *not* the [SEQUENCE] bulk-approval inversion: that's for a
deterministic result set the user reads and accepts in one pass. A walk-through
is an action driven live.)

**When the user stops mid-walk-through, record it as a set-aside** — the marker
defined in plugin-behaviour.md (Set aside). Write the `Set aside ·` line into
the item's block in QUEUE.md: the date, their words quoted, which steps were
reached, what stopped it, and what would make it retryable where they said so.
That line is what lets the next run resume at the right step instead of
restarting — and it is recorded only on the user's own stop, never proposed
because a step looks hard. Resuming a part-walked item later, start from the
marker's reached-line, not from step one.

**Before leading with the walk-through, re-run the capability check** — the last
line of defence, and nearly free because the run is about to act on the tag: name
the tool that would do this work and confirm it is absent or unauthenticated
(plugin-behaviour.md, the `[user]` flavor rules). A wrongly-tagged item stops an
unattended run dead for work nobody needed the user to do — if the check finds
Claude can do it after all, say so, do it as ordinary work, and note the
correction for the close.

**Lead with the walk-through, and drive it live — one step, then wait.** Run
whatever parts you can, give the **first** concrete step the item records, and
**stop and wait** for the user to report back. Then the next step, and so on —
walking beside them, not dumping a list for them to work alone.

Never say "want me to walk you through it?", and never satisfy this branch with
"it stays open until you've done it".

**No completion ask, anywhere in this branch — not leading, not trailing.** Don't
open with "have you already done this one?", and don't close with "…or tell me if
you've already done it". A `[user]` item is walked through, full stop. If the user
volunteers that it's done, take them at their word: don't walk it through, and
recommend /done to record it. If they don't say anything, walk it through.

**Say nothing about /done until the walk-through is complete.** While driving the
steps, don't mention /done, don't frame the item as "handed over", don't recommend
recording it. Mentioning the close mid-walk-through is what once demoted this to a
mere offer.

**Once an item's walk-through is complete (or set aside on the user's word),
name its close.** A
`[user]` item stays in the queue for a later session, so it won't record or remove
itself:

```
run /done                ->  logs it under its slug, removes it from the queue
raise it at the next /plan  ->  if the user would rather mention it there
```

When every `[user]` item has been walked through or set aside, tell the user the
whole run is complete — Claude-work built, user steps addressed — and recommend
/done.

**Copy discipline when the run is all `[user]` items.** Don't fold the silent
active-build check into the first message ("no active build" blurs two unrelated
things), and don't frame it as "there's nothing for me to build" — /next helps
either way. Say plainly that the next ready item is a step for the user to run,
say why it's theirs, and start walking them through it.

## Ending before scope-lock

Any session end before Step 2 locks scope — a soft-stop at the marker, the user
calling it off:

**1. Route any reshape direction to Unprocessed** [PROMPT]. The trigger is
mechanical: *session ending + no scope locked + a reshape direction or learning
the queue needs in conversation = capture needed.* Append it naming the item's
slug, then put the wording in front of the user for approval where it now sits.
Unrouted, the direction survives only
in the LOG entry, which /plan doesn't read at planning time, so the work
re-presents unchanged at the next /next. Nothing reshape-shaped in conversation →
skip, no output.

**2. Name /done as the next step** [BRIEF]. Whatever the session did before
stopping gets recorded and committed only by /done. Other recommendations (run
/plan to vet the next work) ride alongside; they never replace naming /done.

No item returns to the queue, because none left it — scope was never locked.

## Rules

- **The work items are the contract.** Don't exceed the described work without
  explicit approval.
- **Clarifying questions inherit the solicitation rule** (plugin-behaviour.md,
  the private-information section): when surfacing underspecification or asking
  to grow scope, don't ask for sensitive identifiers — addresses, account
  numbers, keys, payment details — that the work doesn't need. The user supplies
  those at the moment of use; they never belong in the queue or the log.
- **Per-item ticking is mandatory** — it's the crash-recovery mechanism.
- **At build completion the only valid next-step recommendation is /done** —
  never /next, never another build. The finished build isn't recorded until /done
  writes its LOG entries and commits, so recommending more building first leaves
  the just-finished work without a record.
