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
    run has no build/[audit] item ->  ALL_WALKTHROUGHS
```

**On NOTHING_CLEARED** [BRIEF] — tell the user the next work isn't cleared to run
yet, recommend /plan to vet it, and stop.

**On ALL_WALKTHROUGHS** [PROMPT] — there's nothing to build, so skip Step 2's
build scaffolding entirely and go straight to Step 3's walk-through branch.

**Why the run is marker-bounded rather than stop-at-first-`[user]`.** Step 2
builds all the Claude-work, then Step 3 walks the `[user]` items. The two passes
never interleave, so no cleared Claude-work is left unbuilt — even when a `[user]`
item sits mid-run.

**The already-done check rides Step 3; it never leads.** A `[user]` item may
already have been done — run in a past session that never removed it from
Processed. Handle that as a *trailing* note in Step 3, never as an opening
question: leading with "have you already done this one?" treats ready work as
probably-already-done and makes the user re-assert it before you'll help.
Detection is by asking, not by scanning for an artifact — a `[user]` step can be a
device check or a decision, with no file to find.

### 3. Present the run and offer the off-ramp  [BRIEF, PROMPT]

Put the run in front of the user and invite a last-glance change **in the same
message** — presenting and offering the off-ramp are one beat, not two.

**Don't ask "Ready?"** Invoking /next already signalled readiness, so a
permission-to-start question is redundant. What the pause is *for* is the one
deliberate human checkpoint before /next runs unattended-in-practice: a last
chance to change scope or reorder. Frame it as that.

```
render(run):                    # full rule: plugin-behaviour.md, working mode
    local AND editor recorded  ->  one-line pointer naming the items,
                                   linking to QUEUE.md
    remote OR no editor        ->  one-line preamble, then the items verbatim
```

The pointer is the token-saving path, the inline quote the safe default. These
items already exist in QUEUE.md, so confirm the link resolves before sending it.

Close that same message with the off-ramp, e.g. **"Say the word to change scope
or reorder — otherwise I'll start."**

```
user wants a change  ->  route to /plan
user says go         ->  Step 2: lock scope, build begins
```

Present-once is deliberate: a separate "here it is" beat followed by a separate
confirm beat is the redundant gate this collapses.

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
list, locking the session to method docs.

Two situations must not be conflated:

```
you CAN'T tell which files THIS item's       ->  underspecification
    described work would change                  SURFACE IT. The only case
                                                 that halts — building it means
                                                 inventing scope the user never
                                                 agreed to.

you CAN scope it, but notice OTHER work      ->  adjacent-work discovery
    worth doing beyond it                        CAPTURE AND CONTINUE on the
                                                 decided scope. Never a blocking
                                                 scope-ask.
```

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
those files plus the method docs, and denies everything else. **Lines must be
bare paths** — the hook matches each line as an exact path, so any annotation
becomes part of the path and silently breaks the match. Make sure no other line
in the file starts with `Files:`.

**4. Remove the run's Claude-work items from QUEUE.md** now that _build.md holds
them — the queue is free for other sessions.

```
Claude-work items  ->  moved to _build.md, REMOVED from QUEUE.md
[user] items       ->  STAY in QUEUE.md
```

A `[user]` item is walked through in Step 3, not built, and is closed later by
/done or /plan. Extracting it into _build.md would strand it, since _build.md is
deleted at close. The ordering here is deliberately destination-first: items are
written into _build.md *before* being removed, so the run survives an interruption
between the two.

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
at the Step 1 off-ramp, so there's no per-item re-confirmation. Tick each item in
_build.md Progress before starting the next.

### Walk-through branch — the `[user]` items  [SEQUENCE, PROMPT]

Once the Claude-work is built (or if the run had none), walk the user through each
`[user]` item still in the cleared region. Walking one through does **not** end
the run — it's the last pass of a run whose Claude work is already done.

**One item at a time — never bundled.** Each in its own message, led by its own
walk-through. Finish one fully — or record that the user deferred it — before
moving to the next. (This is *not* the [SEQUENCE] bulk-approval inversion: that's
for a deterministic result set the user reads and accepts in one pass. A
walk-through is an action driven live.)

**Lead with the walk-through, and drive it live — one step, then wait.** Run
whatever parts you can, give the **first** concrete step the item records, and
**stop and wait** for the user to report back. Then the next step, and so on —
walking beside them, not dumping a list for them to work alone.

Never say "want me to walk you through it?", and never satisfy this branch with
"it stays open until you've done it". Never open with "have you already done this
one?" — leading with the completion-ask treats ready work as probably-already-done
and makes the user re-assert it before you'll help. That inversion is the bug this
branch exists to remove.

**Say nothing about /done until the walk-through is complete.** While driving the
steps, don't mention /done, don't frame the item as "handed over", don't recommend
recording it. Mentioning the close mid-walk-through is what once demoted this to a
mere offer.

**The already-done check is a trailing note**, only on an item a past /next could
plausibly have presented before: "…or let me know if you've already done this and
I'll just record it." A freshly-cleared item carries no such note. If the user says
it's done, don't walk it through — recommend /done to record it.

**Once an item's walk-through is complete (or deferred), name its close.** A
`[user]` item stays in the queue for a later session, so it won't record or remove
itself:

```
run /done                ->  logs it under its slug, removes it from the queue
raise it at the next /plan  ->  if the user would rather mention it there
```

When every `[user]` item has been walked through or deferred, tell the user the
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
slug; draft the wording and show it first. Unrouted, the direction survives only
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
- **Per-item ticking is mandatory** — it's the crash-recovery mechanism.
- **At build completion the only valid next-step recommendation is /done** —
  never /next, never another build. The finished build isn't recorded until /done
  writes its LOG entries and commits, so recommending more building first leaves
  the just-finished work without a record.
