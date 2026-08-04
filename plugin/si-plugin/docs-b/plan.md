---
name: plan
docset: B
note: >
  /plan procedure, docset B. Authored by subtraction from docset A.
  Register: structure in typed blocks, everything else in prose, tags inline.
---

# /plan procedure

/plan is where unprocessed work becomes processed work through discussion. **No
building happens here.** Claude owns sequencing — the order work sits in, what
gets built first — through discussion, not silently.

## Ground rules

- **Never build during /plan.** Want to write code? Queue it. Nothing mechanically
  stops you — there is no `_build.md` in a planning session, so the build
  scope-lock isn't engaged and every file in the project is writable. What you get
  instead is a **prompt**: a write to anything outside QUEUE.md, SPEC.md, LOG/ and
  this session's own notes asks the user first. It asks, it never denies, because
  in planning there is no agreed file list to drift from — the user is right there,
  and a legitimate write is authorised in one word. Treat the prompt as the point:
  it doesn't stop you doing something urgent, it stops you doing it unremarked.
- **One item at a time.** Finish one before presenting the next.
- **Read SPEC.md before proposing work.** Don't queue contradictions.
- **Process the accumulated unprocessed work before new planning work.**
- **Never write to QUEUE.md without showing the exact text first.** The rule keys
  to the *write*, not to where you are in the loop: the message immediately before
  any QUEUE.md write must contain the text verbatim. Approval attaches to shown
  text, never to a described shape — a recommendation, however concrete, is not a
  draft, and "I'll add a line that does X" is not the entry. Keying it to the
  action holds even when a compacted session has lost track of which beat it's on.
- **A recommendation is not a decision. A draft is not a written line.** Both need
  the user's call.
- **SPEC is a normal doc.** When a planning decision changes what SPEC says — a
  new capability, a scope change, a reworded rule (**the test: does any SPEC
  sentence go wrong or incomplete?**) — edit SPEC in that same /plan session, with
  the user present and approving. Don't defer it. Spec-driven development's
  contract is that a change altering behaviour updates the spec in the same
  commit; the /plan-close spec-sync gate enforces that atomicity. When a change
  touches no SPEC sentence, none of this applies. Two other routes exist: a build
  that discovers it needs a SPEC change asks, adds SPEC.md to its Files, and edits
  it inline (next-build.md); and a large SPEC rework is its own piece of work,
  naming SPEC.md among its files like any other build.
- **/plan resolves what it can in-session; capture is only for what it can't.**

```
resolve NOW (within /plan's reach):
    research · queue-wide cleanup (line-ref drift, quoted-string staleness)
    cross-item reconciliation · doc verification

capture instead ONLY when /plan genuinely can't resolve it this session:
    needs data the session doesn't have
    needs design discussion across sessions
    needs user input not yet available
    surfaces a structural question whose answer would gate the work
```

  A default, not an absolute. The test is "can /plan resolve this with what it has
  right now."

## Capture and processing discipline

- **Two sections, one move between them.** The only move is Unprocessed →
  Processed, made in /plan by discussing an item and agreeing to keep it. No third
  state, no parking.
- **A work item carries a user-credit only when the user raised it.** Provenance is
  asymmetric and default-AI; the credit stays on the item after processing.
- **Who does the work, and how.** Work is Claude's to build by default.

```
[user]    only when Claude genuinely CANNOT perform or witness it
          — a check needing the user's eyes, a decision only they can make,
            a physical action (tapping send, connecting a device)
          — work Claude can run but is BLOCKED on a push/restart stays
            Claude-work: shelve it below the line with a lift-condition
          — must carry a DESCRIBED walkthrough, settled at the keep-step

(no tag)  a build — the default Claude-work flavor
[audit]   a review pass: reports findings instead of editing files
```

- **Filing is any session; processing is /plan's.** Moving an item into Processed
  or deleting it is the user's decision to make.
- **A surfaced risk is kept only once its flag is cleared.** Clearing is part of
  processing: **cleared** once the risk is designed out in-session, or the user is
  told it plainly and chooses to proceed (the LOG records which). A risk that
  can't be cleared stays a capture and returns to the bottom of Unprocessed.

## Step 1: Read state and entry question

Read QUEUE.md (both sections) and SPEC.md. Check whether Unprocessed has items.

Everything this step surfaces folds into **one** opening narration, per the
consolidate-the-scans rule.

**Read the forward-recommendation advisory** [SILENT when absent; BRIEF when
present]. If the top of Unprocessed holds a "Last session advises…" line, read it
and let it orient *where the session starts*. It never narrows the session to only
the advised item — Step 2 still processes the full queue. Surface it in one line:
"Last session recommends starting with [slug]." Orientation, not a command. The
**clear** happens at the /done close, not here, so it can't be skipped by a
session that ends via an off-ramp.

**No completion sweep for `[user]` work.** /plan never asks whether Processed's
`[user]` items are already done — that ask is gone from the method entirely, and
so is the setting that used to toggle it. If the user mentions having done one,
close it at this session's /done (log under its slug, remove from Processed);
otherwise leave them alone and say nothing about them.

**Below-the-line revisit** [SILENT when nothing lifts; BRIEF when proposing a
lift; PROMPT only for the user-only batch]. Walk the below-line items; for each,
read the lift-condition its prose records and classify:

```
mechanically checkable    ->  check silently; if cleared, propose lifting
    (a dependency built per LOG, a push done, a file now present)
user-only                 ->  DON'T ask per item. Gather every user-only
    (an external event            condition into ONE consolidated question,
     only the user knows)         asked once this session.
provably still-waiting    ->  skip silently
```

Per-item asking is the nagging this revisit exists to avoid. An item with no
recorded lift-condition can't be classified without nagging — note it as a gap.

**When the same item keeps coming back, stop asking and propose moving it.** An
item whose condition only the user can answer will otherwise surface every single
session, forever — one such item was asked about at three consecutive sessions,
and the user's irritation was entirely fair: it was never a priority, it was just
unsilenceable. So the revisit gets a legitimate way to stop:

```
asked about across MULTIPLE sessions and still not moving
    ->  don't ask again. Propose returning it to the BOTTOM of Unprocessed,
        in one line, as this session's suggestion.
    ->  the user accepts or declines. Declining is fine — it just means keep
        asking about this one.
```

The bottom of Unprocessed is the **only** legitimate way to postpone something.
Do not invent an alternative — a new state, a "lift when you raise it" condition,
a quiet shelf — no matter how much pressure the repetition creates. Those aren't
postponing, they're losing the item somewhere nothing will look again.

That last point generalises, and it's worth stating plainly because it has now
gone wrong three separate ways: **wherever this method forbids something at a
moment that creates real pressure, the legitimate alternative is named in the same
breath.** A prohibition with no stated escape route reliably produces an invented
one, and an invented move is worse than the thing prohibited, because nothing
recognises or records it.

**Seed the queue from SPEC** [BRIEF, PROMPT in the trigger state; otherwise
SILENT]. A rich SPEC can describe buildable features with no path into the queue —
the whole feature set "dies in SPEC" with nothing to build it.

```
auto-trigger (narrow):  Processed is empty or near-empty
                        AND SPEC describes real features not yet built
                            (check LOG/index.md so built features don't count)
manual:                 the user can ask to seed any time
```

Deliberately does **not** fire whenever SPEC merely outruns the queue — that would
mean diffing the whole SPEC against the whole queue every session, the
staleness-and-cost trap the method fights. Outside the trigger state, say nothing.

On either entry, ask whether to derive **coarse milestones** or **granular
per-feature items** — the user's call. Output goes to **Unprocessed, never
Processed**: seeding fills the backlog, it never greenlights a build. Draft the
items as ordinary captures, show for approval, append on approval.

This step lives in /plan, never in /setup — /setup stays scaffolding + interview
and never auto-spawns work.

**Then ask** [PROMPT]: "Anything to discuss before we go through the unprocessed
work?" (If Unprocessed is empty, ask what they'd like to work on.)

If the user has something to discuss, handle it via the Step 2 loop, then ask
"anything else before we go through the queue?" — repeat until nothing more.
**Then process the unprocessed work.** A discussion item is an optional first
stop, never an alternative to processing.

## Step 2: Process work  [SEQUENCE]

**Planning state file: _plan.md.** Create it when processing begins, to hold the
item list, the current item, and the beat reached. Update it at each beat
transition, and append each item with its disposition — kept / deleted /
skipped-this-session — with slug, one line each.

The skipped-slug record is what stops a skipped item re-surfacing later in the
same session. The file survives compaction, gives an interrupted /plan a resume
path, and hands /done a mechanical record instead of a reconstruction from memory.
/done reads it at close and deletes it — same lifecycle as _build.md.

**Process order.** Unprocessed top to bottom, then items raised in this session's
own discussion. State the count upfront, counting both together ("5 items.
First: …"). Position in the file *is* the order — an item placed next to its
relatives is processed there by design.

**Name the always-available moves once, here, in that same opening.** In one
sentence, tell the user they can skip anything they don't want to get into, and
raise something of their own at any point. Said once at the start, they hold for
the whole session — which is why the per-item checkpoint stops reciting them and
asks only carry-on-or-stop.

Two passes run once, before the loop. Both fire at the same opening, so combine
what they surface into the fewest messages.

**Triage bulk-drop pass** [SEQUENCE — bulk-approval inversion]. Skim Unprocessed
for items obviously not worth doing and present them as ONE numbered set the user
contests by number.

```
bulk-droppable ONLY when the reason is one sentence and uncontestable:
    its premise no longer holds
    it duplicates another item
    LOG/index.md shows it already decided

if the drop-reason needs ANY argument  ->  not bulk-droppable; leave it for the
                                           one-at-a-time loop
```

**This pass only ever deletes — it never keeps in bulk.** Sliding undesigned work
into Processed unread is the exact failure this ceiling prevents. If nothing is
obviously droppable, say so in one line and move on.

> "Two look droppable — 1. **[old-slug]**: its premise is gone, the feature it
> targeted was cut. 2. **[dupe-slug]**: duplicates **[other-slug]**. Drop both, or
> name any to keep?"

**Start-of-processing reorder and throughput floor** [BRIEF]. Order the survivors
by **unblock-potential** — the item whose processing would let the most other work
move forward goes first — then narrate the session's shape in one line.

The reorder is **conditional and change-scoped**, not a full re-derivation:
consider only what changed since last session (items newly captured, dropped, or
whose relationships shifted — read the slug-references items already carry), and
if the order already puts the biggest unblockers first, leave it. The floor
narration fires either way; the *move* is what's skipped.

Word the floor as a recommendation, not a cap: "Ordered to process the biggest
unblockers first — recommend processing at least N before your next /next." It's a
planning-throughput target, not a context-budget count.

### For each item

**1. Present and interview**  [DISCUSS, PROMPT]

The item's verbatim text lands ahead of analysis.

```
first item        ->  quote it at the loop's opening; analysis follows in the
                      SAME message
every item after  ->  it was already sent at the prior item's checkpoint, so
                      open directly with analysis — no re-quote, no
                      "my read to follow" pre-framing
```

**There is no separate "ready to dig into this one?" turn.** Presenting the item
and beginning to work it is one beat. The one wait that stays is the [PROMPT] at
the end of the interview, where the user's decision is actually needed. The
verbatim still leads because the user takes an item in more easily reading the raw
text before Claude's framing — leading-then-analysing does that within one
message, without spending a turn on a content-free "shall I continue?".

When quoting the first item, re-read it from QUEUE.md to confirm the quote matches
the file — this catches a context-drifted quote before it's discussed. For later
items that re-read already happened at the checkpoint.

**Verify the item's load-bearing factual claims before discussing it on its own
terms.** A capture is written when its claims are true and then sits for weeks
while the project moves under it. Nothing re-reads it: the below-line revisit
re-checks lift-conditions, but only for items already in Processed, so a claim
stated as prose inside an Unprocessed capture rots unobserved. Processing is the
one moment the item is read closely, so the check belongs here.

**Load-bearing means the item's *disposition* rests on it** — would the item change
shape, priority, or readiness if the claim were false? That test is what keeps this
from becoming a fact-audit of every sentence. Background colour needs no check. A
stated blocker does, and so does any assertion about what the docs say, what a
number is, or what has or hasn't shipped. A stated blocker is one kind of
load-bearing claim, not the category — that framing was tried and was too narrow.

```
"blocked on X existing"     ->  check whether X exists now
"the docs say Y"            ->  grep for Y
"the payload is N bytes"    ->  measure it
"we can't do Z yet"         ->  check whether that's still true
```

Cheap by construction: one item, one check, and only when the item makes such a
claim — so the cost scales with the work being done, not with the size of the
queue. A sweep over all of Unprocessed at the close was considered and rejected
for exactly that reason: it would near-always find nothing, and a check that
near-always no-ops is one that gets skipped.

Three real catches, all of which happened only because someone thought to look:
an item blocked on a recipe that had shipped the day before; an item whose fix
direction reversed once the docs were grepped and said the opposite; and an item
resting on a byte count that measured fifteen times larger. Two of the three were
caught after the item had already been half-discussed on a false premise.

Engage with the item's substance: ask follow-ups to sharpen it or surface missing
context, depth scaling with the item, until the picture is clear.

```
closing the interview:
    delete lean already clear  ->  close on the combined recommend-and-ask
                                   (see sub-step 2's merge guidance)
    lean not clear yet         ->  close with "anything else to add?" and let
                                   sub-step 2 carry the recommendation
```

**View-in-doc.** The item already exists in QUEUE.md, so it's pointer-eligible:
when mode is `local` AND an editor is recorded, lead with a one-line pointer
instead of the pasted quote — `First item — **[work-slug]** — is in
[QUEUE.md](QUEUE.md) under Unprocessed.` — then the analysis in that same message.
The confirm re-read still runs in its pointer form (a resolves-check, not a
text-match). Remote or no editor → keep the inline quote. What counts as a
recorded editor is defined once in plugin-behaviour.md's working-mode render
rule — read it there rather than judging by eye.

**2. Recommend**  [PROMPT]

```
keep    the work is worth doing -> move it into Processed
delete  remove it. If already decided (check LOG/index.md), state the prior
        decision and commit.
```

**A keep recommendation must describe what would actually get built**, in terms
the user recognizes as the work product — which files change, what gets added,
removed or rewritten, not just the topic. *Forcing function:* if the interview
hasn't yielded enough to describe the work concretely, the recommendation isn't
ready — return to interviewing.

Part of keeping is settling who does it and how: Claude-work by default or
`[user]`; and for Claude-work, its flavor. Claude places the item in Processed by
relationship judgment and reports where it went.

Stop and wait. The user decides.

**Fold the recommend into the action when the user already agreed** during the
interview — name the route in one line ("going with keep — drafting the item
now") and go straight to sub-step 3.

```
keep    ->  CAN fold. The draft-approval step is still the user's, so folding
            loses no decision — the draft is the safety net.
delete  ->  CANNOT fold to the action. It's terminal, with no later approval
            step, so explicit approval is still required.
```

**Merge a clear delete recommend into the interview-closing turn.** Don't close
with a bare "anything else to add?" and then re-state the recommendation
separately — that names the route twice with a content-free exchange between.
Close the exposition on one combined bold ask: *"…my recommendation is to drop
this; anything you'd change, or shall I delete it?"* That reply is the terminal
approval delete requires, so merging loses no decision — it drops the empty middle
turn. The standalone recommend-and-wait stays the path when the lean isn't clear.

**3. Execute keep or delete**

**Keep** [DISCUSS, PROMPT] — Draft the processed item: its one-line description
(slug at the end, `[user]` leading if user-work) and the prose rationale carrying
the discussion's reasoning inline.

*When the item is `[user]`, apply the matched pair now:* confirm it's genuinely
user-only (work Claude can run but can't run *yet* is Claude-work shelved below
the line — the over-tag guard); and **don't under-file** — genuine user work must
become a `[user]` line, never a live chat question or a "you'd do that yourself"
aside. Then draft the walkthrough into the item's prose. Not being able to script
every step is **not** a reason to withhold the line: file it with a rough
walkthrough and sharpen it here.

*Decompose a mixed Claude-prep + user-step item.* When an item bundles work Claude
can do with an irreducible user action, don't keep it as one `[user]` item with
Claude-work buried inside:

```
Claude-doable parts  ->  build item(s)
the irreducible user action  ->  a single [user] line, reduced to ONLY that
                                 action, cross-referenced by slug
```

Show the draft as a blockquote under **Work item:**. Don't write until approved.
On approval, make the move so the item is never visible in both sections at once:

```
1. REMOVE from Unprocessed        <- source first
2. ADD to Processed at the reported placement
   (both writes in the same turn)
```

Adding first leaves a window where the item shows in *both* sections, which reads
as a lingering duplicate. Removing first means it's briefly in neither — which
reads correctly as a move in progress. Safe because the drafted item is already
approved and on screen. If the raw capture had no slug, give it one now. Report
"moved to Processed as [slug]" only after the Write succeeded and a re-read
confirms it landed in Processed and is gone from Unprocessed.

*If this item waits on something, choose its route deliberately — don't leave the
dependency to position or to prose.* Two routes, and the choice is stated once
here so it isn't re-derived every time:

```
waits on other queued work   ->  Blocked by: [slug]
    # one line under the description. The named item must be in the queue,
    # above this one. The queue lint checks both.

waits on ANYTHING ELSE       ->  a lift-condition in the prose, and the item
                                 sits below the readiness line
    # a restart, an external event, a decision only the user can make — and
    # equally, work that must be released and running first. Don't clear an
    # item that needs a push; shelve it with "once <this> is pushed and
    # reinstalled" as its lift-condition, like any other external wait.
```

The push marker that used to be a third route here is retired: /next never
honoured it, so it silently let work run against a stale host.

A lift-condition that names another item's slug is the tell that it should have
been `Blocked by:` — rewrite it. Position is not a route: it says what comes
next, not why, so a reorder silently undoes it.

*Split out a buried user-only prerequisite before keeping.* Scan the item's
rationale for a gating action that is both user-only and gates this or other work.
When found buried in prose, split it into its own `[user]` line with its own slug
and reference that slug from the original. A gating action left embedded is
invisible as next-work — its next-ness survives only in the memory of whoever read
the prose.

**Keep a surfaced risk with a red-flag marker** [DISCUSS, PROMPT] — the item gets
one extra line under its description: `Red flag · State: <cleared | uncleared>`.
Processing the risk *means* clearing it. Set **cleared** once this session designs
it out (record how) or the user is told plainly and chooses to proceed (record the
informed consent — what they were warned about and that they chose to go ahead).
An item only moves into Processed with its flag cleared; if it can't be cleared,
return it to the bottom of Unprocessed.

**Delete** — Remove the item from Unprocessed. **Relocate before removing when the
content belongs elsewhere.** Delete means "not worth doing," so routing a fold
through a plain delete risks dropping content the user wanted kept. When the
content belongs in another home — a SPEC sentence, a LOG entry, another item's
rationale — edit the target first with approval, then remove the standalone item.
Still a delete, just after its worth-keeping content has been carried across.

**4. Checkpoint**  [PROMPT]

After every item, present the next item and close on the off-ramps as the
message's final, bold ask.

```
message order:
    1. the NEXT item's verbatim (item only, no analysis)
       — re-read from QUEUE.md first to confirm the quote matches
    2. below it, ONE two-sided question as the closing bold ask:
         **"Carry on, or stop here?"**
```

**Two sides, equal weight, always.** The failure this shape fixes is a statement
followed by a trailing "…close out here?", which reads as a *recommendation* to
stop — a first-time user took it that way over and over and thought the session
had finished. Both alternatives must be present in the ask itself. Never end on
a one-sided question.

**Only that pair gets offered per checkpoint.** Skipping an item and raising
something else are always available just by saying so, so reciting them every
checkpoint teaches nothing and buries the ask. Name them **once, at the start of
the session** — "you can skip anything, or raise something of your own, any time"
— and then don't repeat them. A four-option menu at every checkpoint was tried
live and was worse: the user called it excessive.

Putting the ask last gives the message a landing instead of ending on a raw quote
that reads as stopping mid-thought.

The verbatim here is that next item's own presentation, not a forbidden
look-ahead — the user acts on it immediately, so it's no [SEQUENCE] violation.

**Skip-to-defer.** Skipping is always available in conversation, named once at the
session's start, never its own turn — a separate "dig in or skip?" gate before
every item would re-create the over-asking the method removed.

```
on skip:
    move the item to the bottom of Unprocessed VIA THE MECHANICAL MOVER:
        python plugin/si-plugin/scripts/reorder_queue.py QUEUE.md Unprocessed \
            --move <slug> BOTTOM
    # relocates the whole prose block byte-for-byte. The text is unchanged by a
    # skip, so hand-retyping it via Edit is pure corruption exposure.
    record its slug in _plan.md as skipped-this-session
    don't re-present it this session — present the item after it
```

A skipped item is not deleted and not processed. **The skipped record is the
_plan.md slug and nothing else** — there is no durable queue marker, no "parked"
or "dedicated-pass" tag written to QUEUE.md. Next session it's ordinary
Unprocessed again.

Skipping the last item leaves Unprocessed non-empty, which is fine.

**The last item is the case that breaks this shape, so word it deliberately.**
There is no next item to name, so the two-sided ask has nothing in front of it —
and an ask with nothing before it collapses straight back into "shall we close?",
the exact failure being fixed. The final checkpoint of every session would
reintroduce it. So on the last item, **give continuing a concrete face** rather
than leaving it as the unnamed alternative:

> "That's the last thing waiting. We can keep going — anything you want to
> capture or talk through — or stop here. Which?"

Both options are live and equally weighted. Never "anything else, or shall we
close out?" — a trailing close-question with a vague alternative is a lean toward
stopping however neutrally it's phrased. An empty Unprocessed is a resting state,
not a signal the session is over.

**Recommend skip-to-defer when an item won't design out this session** [DISCUSS].
Skip isn't only the user's to pick. When you can't yet describe what an item's
build would change, or the design keeps opening more questions than it closes,
propose sharpening what you can and then skipping it to the bottom — rather than
reaching for a phantom "give it its own dedicated pass" container. **There is no
dedicated-pass state; the only defer is this skip.** The sharpen-first is part of
the move: capture whatever design progress was made into the item's prose so the
next /plan starts further along.

**View-in-doc applies here too** — when local and an editor is recorded, lead with
a one-line pointer to the next item in place of its verbatim, off-ramps below it
unchanged.

### Process-now offer after a user-filed capture  [PROMPT]

When the *user* files a fresh capture mid-/plan, don't close on a bare "anything
else?" — that can read as parking their idea. File it first, then offer the
branch:

```
process it now   ->  loops straight into the present-and-interview loop
carry on         ->  leaves it in Unprocessed for its turn
(either way: anything else to add first?)
```

Scoped to a capture the **user** raised — processing is /plan's to do, so the
offer is real here. A capture *Claude* raised confirms and resumes instead.

### After all items

Unprocessed should be empty except items skipped this session; Processed holds the
kept work in order; section headers intact.

**Neutral end-of-queue gate** [PROMPT]. When the queue empties, do **not** presume
the session is over and do not slide into the wind-down re-scan or the close. An
empty Unprocessed is a resting state, not a stop signal. Ask the same two-sided
question the last checkpoint uses — continuing named concretely, stopping named
plainly, neither favoured — and wait. If the user raises a further capture, file
it and **return to this same gate** — never re-lean to close after filing.

New items from conversation follow the same loop — check QUEUE.md for overlap
first. If you notice a gap: "I notice [X] — want to hear a suggestion?"

### Wind-down re-scan  [DISCUSS, PROMPT]

After every item is processed and before recommending /done, re-read this
session's own discussion and surface candidate captures — things the user thought
out loud but never explicitly flagged.

**Name the step's best-effort nature in plain words when it runs**: it re-reads
whatever conversation is still in view, and a long session may have lost earlier
discussion to compaction — so a surfaced-nothing result isn't read as "nothing was
missed."

Present all candidates as ONE numbered set of fully-drafted captures for a single
approval; the user contests by number, and only contested items go one at a time.
Approved candidates are filed to Unprocessed; processing them follows the normal
flow, this session or later.

This is a best-effort safety net behind the capture-at-the-moment-of-noticing
rule. A non-coder who thinks out loud generates capturable material they never
flag.

```
/plan  ->  runs the FULL re-scan: files the captures AND can process them
/done  ->  runs a FILE-ONLY version (filing is allowed in any session;
           processing is what the no-planning-in-execution rule protects)
```

## Step 3: Close out  [BRIEF, PROMPT]

The durable close work runs at the /done close (done-plan.md), not here —
reordering both sections, positioning the cleared-to-run marker, holding back
items that depend on unverified work, recording lift-conditions, and placing ready
`[user]` work above the marker. /done is the one close that always runs however a
session ends, so consolidating there is what stops it being silently skipped. The
spec-sync obligation is likewise the /done close's hard gate, not a duplicate here.

So closing a /plan session is just this: **"Run /done to record this and commit,
or keep planning."** No chat summary — the LOG entry /done writes is the single
session summary.
