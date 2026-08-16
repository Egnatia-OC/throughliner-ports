---
name: next
docset: current
note: >
  /next procedure. This is the method's one docset — light, for the 5-series,
  originally authored by subtraction from the now-retired heavy docset.
  Register: structure in typed blocks, everything else in prose, tags inline.
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
    (no tag)    ->  build   ->  next-build.md
    [audit]     ->  review  ->  next-audit.md
    [user]      ->  walk the user through it; never built
    [freeform]  ->  HALT — needs a session of its own; never built here
```

**Never pick an item from past the marker.** This is a standing rule, not a
branch condition — it holds at every step, on every path through /next.

**A `Runs alone` line on an item is the run's second bound.** Walking the
cleared region top-down:

```
marker on an item, run has already built something
    ->  stop before it. The run ends there.
marker on the run's FIRST item
    ->  build it, then end the run after it.
```

Say plainly why the run stopped: this item must not be built alongside other
work, so it gets a run of its own — then recommend /done. Mechanical, no
judgment. It composes with the cleared-to-run line rather than replacing it:
whichever bound comes first ends the run. What the marker means and where it is
written are in plan.md's keep-step, which is the authoring site.

The run includes any `[user]` items among the cleared work; Step 3 walks the user
through each *without ending the run*. The marker is the only thing that bounds a
run.

## Step 1: Pre-flight

**Whatever these checks surface folds into ONE narration** [BRIEF], carried with
the run at step 4 rather than trickling out check by check. The session's first
opening narration also carries the inline-text offer as one clause.

### 1. Active build check

```
exists(this session's build working file)
                   ->  [BRIEF]   offer to resume; read it for state
otherwise          ->  [SILENT]  no output; continue
```

The build working file holds an interrupted build's progress and remaining work,
so resuming picks up where it stopped instead of starting over.

**It is per session, not per project: `_build-<session-id>.md`.** Check for the
one belonging to *this* session and no other, matching that exact name — a
pattern written for the retired bare `_build.md` matches only the old name and
can never find a current one, which makes the check report "no interrupted
build" every time, silently, forever. A build running in another chat has its
own, and its file list is not this session's scope — a planning session that
read another session's working file used to conclude it was inside that build.

**Before creating any file at the project root, read the untracked list in the
session's opening snapshot.** A file listed there exists but has never been
committed, so git holds no copy and overwriting it destroys the only version.
The editing tool will not stop you: it reports the write as creating a new file,
because from its point of view there was nothing there to protect. This is a
habit, not a rule with machinery behind it.

### 2. Find the run, and read SPEC  [SILENT]

**Read SPEC.md once here, at run start** — not per item. It is the product truth
each item is built against, and a build that never reads it cannot be checked
against it. Reading it once per run is what makes the per-item check below cost
almost nothing.

Then read Processed top-down and take everything above the marker.

```
early exits:
    Processed[top] == marker      ->  NOTHING_CLEARED
    an item in the run carries
      `Red flag · State: uncleared` ->  UNCLEARED_FLAG
    Processed[top] is `[freeform]`  ->  FREEFORM_HALT (nothing has started)
    run has no build/[audit] item ->  ALL_WALKTHROUGHS
```

**On NOTHING_CLEARED** [BRIEF] — tell the user the next work isn't cleared to run
yet, recommend /plan to vet it, and stop.

**On UNCLEARED_FLAG** [BRIEF, PROMPT] — stop. Don't build the item, and don't
build the rest of the run around it. Name the risk in plain English, say the item
reached the ready region with its flag still uncleared, and recommend /plan to
clear it. Then wait.

This should be impossible: a flag is cleared at processing, so an item only
reaches Processed with a cleared flag, and the cleared region is red-flag-safe by
construction. That is exactly why the check is here. A backstop for an impossible
case never fires, so nothing ever reveals it missing — and this one *was* missing,
promised by SPEC and the behaviour rules while no code path implemented it. What
it guards is real: without it, an unattended run would silently build work
carrying an unaddressed data-exposure risk, which is the one thing the whole
red-flag model exists to prevent.

**On FREEFORM_HALT** [BRIEF, PROMPT] — say plainly what the item is and that it
needs a session of its own where the work is done by hand rather than built from
the queue, and stop. Don't skip past it to the next item.

A `[freeform]` item is placed at one end of the cleared region, never in the
middle, so the halt is always cheap: met first, nothing has started; met last,
everything else is already finished. When one sits at the *end* of the run, Step 3
builds everything above it and then halts on it, which is the same stop reached
from the other side.

**On ALL_WALKTHROUGHS** [PROMPT] — there's nothing to build, so skip Step 2's
build scaffolding entirely and go straight to Step 3's walk-through branch.

**Why the run is marker-bounded rather than stop-at-first-`[user]`.** Step 2
builds all the Claude-work, then Step 3 walks the `[user]` items. The two passes
never interleave, so no cleared Claude-work is left unbuilt — even when a `[user]`
item sits mid-run.

**Before handing a `[user]` item over, run the LIGHT capability check.** Name the
tool that would do the work and confirm it is absent or unauthenticated (the
over-tag guard, skill-nonspecific-rules.md). This is the last line of defence
against a wrong tag, and it's nearly free — the run is about to act on that tag.
If the check finds a tool that can do it, do the work as ordinary work and note
the correction for the close; a wrong `[user]` item otherwise stops an unattended
run dead for work nobody needed the user to do.

**Light, not thorough — no reframe, no search, no trying the tool.** The heavy
version belongs at /plan's keep-step, where the user is in the room. Here the
user is not, and a run should not stop to explore.

### 3. Open waiting mail  [SILENT] when the mailbox is empty; [BRIEF] when it isn't

Read anything waiting in this project's `INBOX/`, before the run is presented.
That ordering is the point: mail can block work, so it is read while the run can
still change rather than after scope is locked. Full mechanics —
`${CLAUDE_PLUGIN_ROOT}/docs-b/feedback-and-inbox.md`.

```
/next OPENS, FILES and DEFERS. It never processes.
    anything a message raises   ->  a capture in Unprocessed
    a message bearing on an     ->  name it at the present-the-run beat and
      item in the cleared           recommend dropping that item FROM THIS
      region                        RUN ONLY. Leave the queue untouched.
    the message file            ->  moves to INBOX/archive/
```

Processing — deciding an item's fate — stays /plan's, which is the boundary the
whole method rests on. The reply draft is offered at the close, not here: a run
is unattended in practice, and stopping it to approve text that leaves the
machine would defeat that.

Nothing in the scope-lock blocks this: `pre_tool_use` treats any project's
`INBOX/` as always editable, so reading and archiving mail during a locked run
cannot be denied.

### 4. Present the run and offer the off-ramp  [BRIEF, PROMPT]

Put the run in front of the user and invite a last-glance change **in the same
message** — presenting and offering the off-ramp are one beat, not two.

**Don't ask "Ready?"** Invoking /next already signalled readiness, so a
permission-to-start question is redundant. What the pause is *for* is the one
deliberate human checkpoint before /next runs unattended-in-practice: a last
chance to change scope or reorder. Frame it as that.

```
render(run):                        # full rule: skill-nonspecific-rules.md, view-in-doc
    default                    ->  one-line pointer naming the items,
                                   linking to QUEUE.md
    user took the inline offer ->  one-line preamble, then the items verbatim
```

The pointer is the default and the token-saving path; the inline quote is what the
opening inline-text offer switches on. These items already exist in QUEUE.md, so
confirm the link resolves before sending it.

**Present the whole cleared region, and never recommend a subset of it.** The
cleared-to-run line is the run bound and the user set it at /plan; a softer cap
proposed here is a guess dressed as prudence, because Claude has no gauge of
context filling at all. Don't say a run looks large, don't suggest stopping after
the first few, and don't inherit such a suggestion from a previous session's
advisory. If a run should stop early, that is decided by observed behaviour — the
no-progress halt — not by a number chosen up front.

**The one thing that may drop an item from the run is waiting mail** [BRIEF].
Where a message read at the step above bears on an item in the cleared region,
name it here and recommend dropping that item from **this run only** — the queue
is left untouched and /plan decides its fate. That is not the softer cap this
rule forbids: it rests on something a message actually said, not on a guess
about how large a run should be.

**If the user took the inline offer, advise on the large items here** [BRIEF].
Inline display is settled by the session's opening offer, not by a question of
its own — but *which items* would bury the run in text can only be judged once
the run is known, which is now. Name the items whose edits are large enough that
inline display would swamp everything else, recommend leaving those on line
references, and let the user answer in the same breath as the off-ramp.

```
inline OFF (the default)  ->  say nothing about display
inline ON                 ->  one clause naming the large items, e.g. "item 6
                              rewrites most of a doc, so I'd keep that one on
                              line references — inline for the rest?"
```

Judge "large" against the item's own files — the share of a file its edits
rewrite — never against a bare number of lines. This is an ordering-style
judgment, so narrate it in one sentence like any other.

The answer holds for the run. On a resumed run, carry the previous answer
forward from the working file rather than re-asking.

Close that same message with the off-ramp, e.g. **"Say go and I'll start — or say
the word to change scope or reorder first."** The affirmative first, the exception
second.

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

**What scope means here — two layers.** The **described work** is the test (its
definition is in skill-nonspecific-rules.md's Scope section); the `Files:` list
below is its mechanical approximation: pre_tool_use allows edits only
to listed files (plus the method docs, the user's memory dir,
`resources/research/`, the session scratchpad, and any project's `INBOX/`) and
denies the rest, as a backstop. **The two layers are not the same thing** — a build
can stay inside every listed file and still do more than the work describes. The
described work is the test; the `Files:` list is the guardrail.

/next **self-scopes**: it reads the Claude-work items it's about to build and
derives the scope from them. Work outside the described work is appended to
Unprocessed, not folded in.

Once the user confirms:

**1. Self-scope.** Read each Claude-work item's description and rationale, work
out which files it will change, and list them. `[audit]` items name no files —
an audit reads and reports — so a run of only audit items gets an empty Files
list, locking the session to method docs.

Two situations must not be conflated:

```
you CAN'T tell which files THIS item's       ->  underspecification
    described work would change,                 SURFACE IT. The only case
  OR you can name the files but the item        that halts — building it means
    doesn't say WHAT CHANGES INSIDE THEM         inventing scope the user never
                                                 agreed to.

you CAN scope it, but notice OTHER work      ->  adjacent-work discovery
    worth doing beyond it                        CAPTURE AND CONTINUE on the
                                                 decided scope. Never a blocking
                                                 scope-ask.
```

**An item is buildable only when it says what changes *inside* the files it
names.** The same two-limb test runs at /plan's keep-step, which carries the full
argument and is where an item like this should be stopped; meeting one here means
it got through.

**Both limbs halt, and the second one is why.** A design question about the item
in hand — "how should this behave?" — is not a question about which files change
and is not other work, so under a one-limb test it fell through both routes with
no defined path, and a run meeting one improvised: it stopped and asked. **That
question IS underspecification** — the item did not say how — arriving late
because limb two was never tested here. It routes through the mechanism that
already exists rather than through a design-question branch, which would
legitimise stopping an unattended run to ask how things should be.

This matters most where it is least visible. A halt on "which files" is a clean
stop with a clear question; a halt on "how should this work" is a design
conversation started by the runner, in a session whose whole premise is that
design already happened.

*Worked example, second limb.* An item names `plan.md` and says its ordering rule
should be "improved" without saying what the new rule is. The files are perfectly
clear and the item is still unbuildable — halt as underspecified rather than
choosing a rule the user never agreed.

A blocking ask on adjacent work both defeats the unattended run and reopens a
scope decision reserved for /plan. The extra look self-scoping gives is preserved
by capturing what it finds, not by asking.

*Worked example.* Building a terminology rename, self-scoping enumerates the docs
the item names. A doc silent on which sections change → underspecification,
surface it. Noticing the *hooks* also carry the old term when the item didn't
list them → adjacent-work discovery, capture it and continue.

**2. Create this session's build working file** — `_build-<session-id>.md`, in
the project root:

````markdown
# Active Build

Run: [flavor + slug of each Claude-work item, top-down]

Entries:
[One line per Claude-work item: its flavor tag (or "build"), its slug, and its
description. Rationale is NOT copied — it lives in QUEUE.md under that slug and is
read from there.]

Index entry candidates:
[empty — one added as each item is ticked]

Edit display: [line references (the default) | inline, except: <items>]

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

**Rationale is pointed at, not copied, and the safety that governs the pointer.**
Each item's reasoning stays in QUEUE.md and is read from there when the item is
built. The reason not to copy it: on a fifteen-item run the copy came to roughly
eight thousand tokens, all of it text read from QUEUE.md minutes earlier, and it
is re-paid on every run touching those items. The reason the pointer is *safe* is
step 3 below — each item stays in QUEUE.md until the moment it is ticked, so no
item's only copy ever sits in a file scheduled for deletion. **If that copy-per-item
ordering is ever changed, this pointer must be revisited with it**; the two
together are what replaced copying every item's prose in.

**3. Leave QUEUE.md alone. Copy, never cut.**

```
Claude-work items  ->  COPIED into the build working file, and they STAY in QUEUE.md
[user] items       ->  STAY in QUEUE.md
```

Nothing is removed from QUEUE.md here. Each Claude-work item is removed **one at
a time**, at the moment it is ticked in the working file's Progress (Step 3) — so the queue
visibly shrinks as the run progresses, and an item still showing in QUEUE.md means
exactly one thing: not built yet.

A `[user]` item is walked through in Step 3, not built, and is closed later by
/done or /plan. It never enters the build working file, since the build working file is deleted at close.

**4. Narrate the lock** [BRIEF] — one sentence, in user-facing terms: the build working file is
the build's working file — it carries a copy of the run's work, lists the files the
safety check allows, tracks progress so an interrupted session can resume, and
holds the reasoning /done writes into the session record. The queue keeps its own
copy of everything not yet built, and each item drops out of it as it's finished.

```
progress format:
    build item  ->  - [x] item description — done
    audit item  ->  - [x] Finding description — captured | dropped
```

The build working file is the crash-recovery mechanism: if the session dies, the
session that resumes sees it and picks up from it. A working file left by a
session that never came back is surfaced at session start as a leftover — never
deleted, because it may hold the only record of what that session did.

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
at the Step 1 off-ramp, so there's no per-item re-confirmation.

**As each item completes, do four things before starting the next:** tick it in
the working file's Progress, record that item's depth field, write that item's
index-entry candidate, then remove that one item from QUEUE.md with the
mechanical mover, addressed by its slug.

**Where the project's own instructions require a rule-gate disposition and the
item carries one, copy it across unchanged.** Transcribe, never compose. Where
the item is about to author or amend a standing rule and carries no disposition,
halt and say so: the gate's site is planning, and a disposition written now could
only describe what is already built.

**The tick is the accumulation point.** `Progress:`, `Index entry candidates:`
and `Changes:` all grow one item at a time, so the working file only ever
describes work that actually happened. The index candidate is artifact touched +
nature of change (skill-nonspecific-rules.md, Index entries), and written here it
*describes* the build rather than predicting it — more accurate as well as
cheaper, since a run is never guaranteed to reach its end and a candidate is only
ever redeemed by an item that builds. Nothing is lost by moving it: the readiness
check pre-generation doubled as still runs at /plan's keep-step, which refuses an
item whose index line cannot be written yet.

**The depth field is required, not optional, and it is written here rather than
loosely during the build.** One line per ticked item, under the Progress tick:

```
Depth: short
Depth: full — <which trigger: reasoning contested | alternative seriously weighed>
```

A required field is the point. The close reads these hours later, when every
item's reasoning is simultaneously fresh and every one *feels* worth telling at
length — so an absent line is not a signal that presents itself, and honouring
the short-form default would mean hunting item by item for something that is not
there. Writing the field at the tick turns a silent omission into a visible one,
which is the shape this method already trusts for the FAQ-sync disposition and
the rule-gate line.

```
python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
    --delete <slug> Processed
# the plugin root is the grandparent of the running skill's base directory
# (.../<plugin-root>/skills/<skill>) — derive it, never hardcode a path.
```

Tick first, then remove. That order means an interruption between the two leaves
the item in both files, which a resume can see and settle — the reverse order
would leave it in neither.

### The `[user]` walk-through lifecycle

How a `[user]` item is run and closed. (What earns the tag is the matched pair in
skill-nonspecific-rules.md, Captures.) Without the back half, a finished `[user]`
item strands in Processed and the next /next presents it again as if unbuilt.

- **/next leads with the walk-through and drives it live.** Name what's theirs to
  do, run whatever parts you can, give the **first** concrete step, and **wait**.
  One step at a time. This is a live drive, not an offer — you walk *beside* the
  user, you don't step back and hand off.
- **The close is named only after the walk-through finishes.** How completion gets
  recorded is told to the user *after* the last step is done or they defer.
- **One `[user]` item at a time — never bundled.** Each in its own message, led by
  its own live walk-through. Not a bulk-approval result set.
- **Three things count as knowing an item is complete**, and nothing else: it was
  walked to its end this session, the user said they did it, or its walkthrough
  named an observable check and that check passed. An item whose blocker visibly
  hasn't shipped is not complete. A failed check produces a plain statement of
  what was found and leaves the item in place.
- **The gap this leaves is deliberate: leave the item in place.** An item the user
  completed on their own, with nothing observable to show for it, will sit in
  Processed until they mention it — and mentioning it is already a supported path.
  This is written down precisely so nobody later notices the hole and proposes an
  ask to fill it. Don't.
- **A completed `[user]` item has a defined close:** log it under its slug and
  remove it from Processed. Lives in **both** /done (the user runs /done right
  after finishing) and /plan (they completed it async and mention it).
- **Re-clearing dependents** is the below-the-line revisit's job, not the close's.

### Walk-through branch — the `[user]` items  [SEQUENCE, PROMPT]

Once the Claude-work is built (or if the run had none), walk the user through each
`[user]` item still in the cleared region. Walking one through does **not** end
the run — it's the last pass of a run whose Claude work is already done.

**One item at a time — never bundled.** Each in its own message, led by its own
walk-through. Finish one fully — or record that the user deferred it — before
moving to the next. (This is *not* the [SEQUENCE] bulk-approval inversion: that's
for a deterministic result set the user reads and accepts in one pass. A
walk-through is an action driven live.)

**Open the item's LOG entry file when the walk-through starts, and append each
action as it happens.** A walk-through legitimately has Claude doing real work —
running a reinstall, bumping a version, pruning a cache — and none of it has any
other home: a `[user]` item never enters the build working file, so without this
the work exists only in conversation and a crash loses it entirely, leaving a
working file that positively suggests it never happened. Write the entry under the
item's slug, in `LOG/`, and add to it as you go. The item itself stays in QUEUE.md
untouched, so nothing is stranded, and a crash mid-walk-through leaves a partial
entry saying exactly what was done. The close then finds an entry already started
rather than writing one fresh.

This is a place to record, never a restriction on doing. The branch is *supposed*
to run whatever parts Claude can — that is what makes it a live drive. The record
goes to `LOG/` precisely because `LOG/` is writable whatever the scope-lock says,
so recording can never be what blocks the walk-through.

**Lead with the walk-through, and drive it live — one step, then wait.** Run
whatever parts you can, give the **first** concrete step the item records, and
**stop and wait** for the user to report back. Then the next step, and so on —
walking beside them, not dumping a list for them to work alone.

Never say "want me to walk you through it?", and never satisfy this branch with
"it stays open until you've done it".

**Where the user volunteers that an item is done, take them at their word:** skip
the walk-through and recommend /done to record it.

**Where the item's walkthrough names an observable check, run it** — a file
present or absent, a branch gone, a URL responding. A failed check is reported
plainly as what was found, and the item stays in place.

**Confirm the step can produce the observation the item names** — the light
form: check that the step names something which yields the evidence, and no
more. No experiment, no search, no stopping. (The heavy version, where the
command is actually run, belongs at /plan's keep-step, where the walkthrough is
authored and the user is in the room.)

**Verify any command before handing it over to be pasted.** Run it where doing
so is safe — a scratch fixture — or read the tool's `--help`. The scope is
narrow on purpose: a command *Claude* runs with a wrong flag costs one turn and
self-corrects, because the error arrives, the help gets read, and the work
continues. The cost only lands when the command goes into a block for the user
to run: they are a non-coder, they cannot tell a typo from a broken tool, and
the failure arrives in their hands rather than yours. A tool's own flag list is
not an external fact to be careful about — it is one `--help` away, so the gap
this closes is ordering, not knowledge.

**Say nothing about /done until the walk-through is complete.** While driving the
steps, don't mention /done, don't frame the item as "handed over", don't recommend
recording it. Mentioning the close mid-walk-through is what once demoted this to a
mere offer.

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
slug; write it, then report what was filed. Unrouted, the direction survives only
in the LOG entry, which /plan doesn't read at planning time, so the work
re-presents unchanged at the next /next. Nothing reshape-shaped in conversation →
skip, no output.

**2. Name /done as the next step** [BRIEF]. Whatever the session did before
stopping gets recorded and committed only by /done. Other recommendations (run
/plan to vet the next work) ride alongside; they never replace naming /done.

No item returns to the queue, because none left it — scope was never locked.

## Resuming

When resuming an active build, read its working file for state rather than
re-exploring.

