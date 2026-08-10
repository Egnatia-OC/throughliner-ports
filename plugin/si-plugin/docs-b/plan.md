---
name: plan
docset: B
note: >
  /plan procedure. The method's one docset, originally authored by subtraction
  from the now-retired heavy docset.
  Register: structure in typed blocks, everything else in prose, tags inline.
---

# /plan procedure

/plan is where unprocessed work becomes processed work through discussion. **No
building happens here.** Claude owns sequencing — the order work sits in, what
gets built first — through discussion, not silently.

## Ground rules

- **Never build during /plan.** Want to write code? Queue it.
- **One item at a time.** Finish one before presenting the next.
- **Read SPEC.md before proposing work.** Don't queue contradictions.
- **Process the accumulated unprocessed work before new planning work.**
- **Write to QUEUE.md first, then report what landed.** Don't paste the text into
  chat for approval ahead of the write. Write it, then say in one line what went
  in and where — specific enough that the user can object without opening the
  file. The full rule, including the one test that decides which moments still
  show first, is in skill-nonspecific-rules.md's approval-time outputs.
- **Nothing mechanically contains a planning session, so the containment is a
  prompt.** There is no build working file here and so no engaged scope-lock; what
  a session gets instead is an ask before any write outside the quiet list —
  QUEUE.md, SPEC.md, `LOG/`, and the session's own planning notes. It doesn't stop
  you doing something urgent, it stops you doing it unremarked.
- **A recommendation is not a decision.** Whether an item is kept or deleted is
  still the user's call, and a written line is not an agreed one — the user can
  reject what was written, and it is reverted.
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
  asymmetric and default-AI; the credit stays on the item after processing. The
  credit needs the user's **own words** as its source — approving what Claude
  reasoned out is agreement, not authorship. Where both contributed, write it as
  mixed and name who did which part. The same bar binds reason-shaped sentences
  in the prose ("their reason", "the user's call"): don't write one unless the
  user gave that reason.
- **Who does the work, and how.** Work is Claude's to build by default.

```
[user]    only when Claude genuinely CANNOT perform or witness it
          — a check needing the user's eyes, a decision only they can make,
            a physical action (tapping send, connecting a device)
          — work Claude can run but is BLOCKED on a push/restart stays
            Claude-work: file what it waits on as its own item, and shelve
            this one below the line naming that item as its blocker
          — must carry a DESCRIBED walkthrough, settled at the keep-step

(no tag)  a build — the default Claude-work flavor
[audit]   a review pass: reports findings instead of editing files
[freeform] work done by hand in a session of its own — /next must NOT build it
```

- **`[freeform]` marks work /next must not run.** Either the user or Claude may
  designate it, typically as a stopgap or as the nuclear option for something too
  big to fix stepwise. Its defining case is a repair to the machinery /next itself
  uses — the queue mover, the scope-lock, the lint — where running the broken
  mechanism to build past it is the failure. **Place it at one end of the cleared
  region, never interleaved with Claude-work:** first when it is a prerequisite or
  repairs machinery /next uses, last when it is unrelated so the run clears the
  buildable work before stopping. Both ends satisfy the rule; narrate which end and
  why, like any other ordering judgment. If later cleared work genuinely depends on
  the freeform fix landing first, that is an ordinary `Blocked by: [slug]`
  relationship — no new mechanism.

- **Filing is any session; processing is /plan's.** Moving an item into Processed
  or deleting it is the user's decision to make.
- **A surfaced risk is kept only once its flag is cleared.** Clearing is part of
  processing: **cleared** once the risk is designed out in-session, or the user is
  told it plainly and chooses to proceed (the LOG records which). A risk that
  can't be cleared stays a capture and returns to the bottom of Unprocessed.

## Step 1: Read state and entry question

Read QUEUE.md (both sections) and SPEC.md. Check whether Unprocessed has items.

**Page QUEUE.md to the end before reasoning over it.** A long queue can come back
truncated, and a truncated read looks exactly like a complete one to whatever
reasons over it — so the check belongs here, at the read. If the read stopped
short, page the rest before going on; if for any reason you cannot, say so plainly
rather than reasoning from the part you have.

Everything this step surfaces folds into **one** opening narration, per the
consolidate-the-scans rule.

**Read the forward-recommendation advisory** [SILENT when absent; BRIEF when
present]. If the top of Unprocessed holds a "Last session advises…" line — it
carries the reserved slug `[forward-advisory]` at the end of its heading — read it
and let it orient *where the session starts*. It is **not** a work item and never
goes through keep/delete in Step 2; skip it there. It never narrows the session to only
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
lift]. Every below-line item names its blocker as `Blocked by: [slug]`, so the
revisit is one check per item:

```
blocker shipped per LOG   ->  propose lifting the item above the marker
blocker still open        ->  skip silently
blocker missing or not
    a real queue item     ->  a fault; surface it and fix it this session
```

Read shipped-ness off LOG, never off memory — a fresh short session has none.
**Nothing here is a question for the user.** Lifting is narrated; a still-blocked
item says nothing at all.

The four-way classifier this replaces — mechanically-checkable / Claude-downstream
/ user-only / still-waiting — existed because a blocker used to be a prose
sentence that had to be interpreted before it could be acted on, and the
consolidated user-only question existed to stop that interpretation nagging. Both
are gone with the sentences. So is the downstream-action test: an item can only be
blocked by a queue item now, and a thing in the world becomes a queue item before
anything blocks on it, so a condition waiting on an action nobody filed can no
longer be written.

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
Processed**: seeding fills the backlog, it never greenlights a build. Write the
items as ordinary captures, then report what was seeded.

This step lives in /plan, never in /setup — /setup stays scaffolding + interview
and never auto-spawns work.

### The opening — two beats, drop then order

**Beat 1 — the droppable set** [SEQUENCE — bulk-approval inversion]. Skim
Unprocessed for items obviously not worth doing and present them as ONE numbered
set the user contests by number.

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
obviously droppable this beat doesn't fire at all — say nothing and go to beat 2.

> "Two look droppable — 1. **[old-slug]**: its premise is gone, the feature it
> targeted was cut. 2. **[dupe-slug]**: duplicates **[other-slug]**. Drop both, or
> name any to keep?"

Dropping comes first because there is no point ordering items that are about to be
deleted, and what gets dropped changes what is left to order.

**Beat 2 — the ordering ask** [PROMPT]. One question, with the default named:
**"Anything you want to prioritise, or shall I work through them
most-unblocking-first?"** One question, not a menu — the only alternative offered
is the user's own priorities. This absorbs the old "anything to discuss?" opening:
a user with something on their mind answers it here.

(If Unprocessed is empty there's nothing to order, so offer seeding from SPEC by
name instead — the step above. If SPEC is thin too, it's an ordinary conversation
about what they want next; **not** a new session type, mode, or container.)

If the user raises something to discuss, handle it via the Step 2 loop, then ask
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

**Run the scrub checklist before writing a kept item's text** (skill-nonspecific-rules.md,
Scrub before writing). Keeping an item is where a capture's rough wording becomes
the version that ships into a committed doc, so it is the last cheap moment to
rewrite a real name or a case detail out of it.

**Process order.** Unprocessed top to bottom, then items raised in this session's
own discussion. State the count upfront, counting both together ("5 items.
First: …"). Position in the file *is* the order — an item placed next to its
relatives is processed there by design.

The droppable set was already handled at Step 1's opening (beat 1), so the
survivors are what's left to order.

**Start-of-processing reorder and throughput floor** [BRIEF]. Apply the order the
user chose at beat 2 — their own priorities if they named any, otherwise the
default, **unblock-potential**: the item whose processing would let the most other
work move forward goes first. Then narrate the session's shape in one line.

**The fallback ladder — internal, applied, never offered.** When nothing meaningfully
unblocks anything else, don't fall through to file order silently. Work down:

```
1. an uncleared red flag in Unprocessed   an unaddressed data-exposure or privacy
                                          risk outranks throughput: the cost of
                                          leaving it is a breach, not a delay
2. unblock-potential                      the stated default; what nearly every
                                          session actually uses
3. decay                                  a premise going stale, or evidence that
                                          only holds while the observation is fresh
4. cheap to settle                        decidable in one exchange; clears volume
                                          so the queue stops reading as heavy
5. file order                             position in the section
```

The ladder is never presented as a choice — it's surfaced only through the one-line
floor narration, which names whichever rung the order actually came from.

The reorder is **conditional and change-scoped**, not a full re-derivation:
consider only what changed since last session (items newly captured, dropped, or
whose relationships shifted — read the slug-references items already carry), and
if the order already sits right, leave it. The floor narration fires either way;
the *move* is what's skipped.

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

Engage with the item's substance: ask follow-ups to sharpen it or surface missing
context, depth scaling with the item, until the picture is clear.

```
closing the interview:
    delete lean already clear  ->  close on the combined recommend-and-ask
                                   (see sub-step 2's merge guidance)
    lean not clear yet         ->  close with "anything else to add?" and let
                                   sub-step 2 carry the recommendation
```

**View-in-doc.** The item already exists in QUEUE.md, so pointing is the default:
lead with a one-line pointer instead of the pasted quote — `First item —
**[work-slug]** — is in [QUEUE.md](QUEUE.md) under Unprocessed.` — then the
analysis in that same message. The confirm re-read still runs in its pointer form
(a resolves-check, not a text-match). If the user took the opening inline-text
offer, keep the inline quote instead.

**2. Recommend**  [PROMPT]

```
keep    the work is worth doing -> move it into Processed
delete  remove it. If already decided (check LOG/index.md), state the prior
        decision and commit.
```

**A keep recommendation must describe what would actually get built**, in terms
the user recognizes as the work product — which files change, what gets added,
removed or rewritten, not just the topic. **This is a blocking check, not a prompt
to try harder:** before recommending keep, state the build in both limbs — the
files that change AND what changes inside them — and if either limb can't be
stated, the keep cannot proceed.

Naming files alone is not passing. "Files (rough): skill-nonspecific-rules.md, plan.md"
is exactly what undesigned work looks like, and items in that shape have reached
Processed and then stalled a /next run that had a file list and nothing to build
from. An item that can't pass both limbs gets sharpened further in the interview,
or skip-to-deferred with its design progress written into its prose — never kept.

This is where a design item is caught. An item whose build list is *the design's
own output* fails the second limb by construction, so it never clears to run, and
/next never has to meet it. That is the cheap place to catch it: at planning time,
where the user is already in the conversation, rather than at build time, where
the run halts to ask.

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

*If the item goes below the cleared-to-run line, place it destination-first too.*
Below the line means one thing: a named queue item blocks this one. So name the
blocker, and **if that blocker is not already a queue item, write it into
Unprocessed first**, then write the held item with its `Blocked by: [slug]` line.
Same reason as the ordering below — a reference resolves the moment its target
exists. Written the other way round, the held item names a blocker nothing can
resolve; that has happened, three items at once, and only the queue lint caught it
after the write. If nothing in the queue blocks the item, it belongs **above** the
line, not below it.

Write the item, then report it. Make the move in this order:

```
1. ADD to Processed at the chosen placement    <- destination first
2. REMOVE from Unprocessed
   (both writes in the same turn)
```

Destination-first because nothing is on screen to fall back on. If something
interrupts between the two writes, the item exists in Processed and only needs
the stale copy cleaned up; the other order would leave it in neither section and
lose the written text entirely. The cost — a one-turn window where it shows in
both sections, reading as an uncleaned duplicate — is the lesser one, and closing
both writes in the same turn keeps it to that.

If the raw capture had no slug, give it one now. Report "moved to Processed as
[slug]" only after the Write succeeded and a re-read confirms it landed in
Processed and is gone from Unprocessed.

*Split out a buried user-only prerequisite before keeping.* Scan the item's
rationale for a gating action that is both user-only and gates this or other work.
When found buried in prose, split it into its own `[user]` line with its own slug
and reference that slug from the original. A gating action left embedded is
invisible as next-work — its next-ness survives only in the memory of whoever read
the prose.

*Before any `[user]` tag stands, run the capability check.* Name the tool that
would do the work and confirm it is absent or unauthenticated (the over-tag
guard, skill-nonspecific-rules.md). Don't reason from what the task *sounds* like —
"create a GitHub repo" sounded browser-shaped and went to the user when `gh`
would have done it in seconds. This is the cheapest place to catch a wrong tag.

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
    2. below it, the off-ramps as the closing bold question:
         continue to the next item
         skip this next one to the bottom for a later session
         close out now (Step 3)
         raise something else (loop back into Step 2)
```

All four must be genuinely on offer; deliver them conversationally, but below the
verbatim, not above it. Putting the ask last gives the message a landing instead
of ending on a raw quote that reads as stopping mid-thought.

The verbatim here is that next item's own presentation, not a forbidden
look-ahead — the user acts on it immediately, so it's no [SEQUENCE] violation.

**Skip-to-defer.** Skipping is one option among four, never its own turn — a
separate "dig in or skip?" gate before every item would re-create the over-asking
the method removed.

```
on skip:
    move the item to the bottom of Unprocessed VIA THE MECHANICAL MOVER:
        python <plugin-root>/scripts/reorder_queue.py QUEUE.md Unprocessed \
            --move <slug> BOTTOM
    # the plugin root is the grandparent of the running skill's base directory
    # (.../<plugin-root>/skills/<skill>). Derive it from there so it resolves
    # wherever the plugin is installed — never hardcode a path. A hardcoded
    # path resolves only in the project the method is developed in, and the
    # fallback when it fails is hand-retyping the block, which is exactly the
    # corruption exposure the mover exists to remove.
    # relocates the whole prose block byte-for-byte. The text is unchanged by a
    # skip, so hand-retyping it via Edit is pure corruption exposure.
    record its slug in _plan.md as skipped-this-session
    don't re-present it this session — present the item after it
```

A skipped item is not deleted and not processed. **The skipped record is the
_plan.md slug and nothing else** — there is no durable queue marker, no "parked"
or "dedicated-pass" tag written to QUEUE.md. Next session it's ordinary
Unprocessed again.

Skipping the last item leaves Unprocessed non-empty, which is fine. On the last
item there's no next verbatim, so the message is just the off-ramps — worded
**neutrally**, "anything else to capture or discuss, or close out?", never as a
lean toward closing. An empty Unprocessed is not a signal the session is over.

**Recommend skip-to-defer when an item won't design out this session** [DISCUSS].
Skip isn't only the user's to pick. When you can't yet describe what an item's
build would change, or the design keeps opening more questions than it closes,
propose sharpening what you can and then skipping it to the bottom — rather than
reaching for a phantom "give it its own dedicated pass" container. **There is no
dedicated-pass state; the only defer is this skip.** The sharpen-first is part of
the move: capture whatever design progress was made into the item's prose so the
next /plan starts further along.

**View-in-doc applies here too** — by default lead with a one-line pointer to the
next item in place of its verbatim, off-ramps below it unchanged.

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
empty Unprocessed is a resting state, not a stop signal. Ask one neutral question
— "anything else to capture or discuss, or shall we close out?" — and wait. If the
user raises a further capture, file it and **return to this same neutral gate** —
never re-lean to close after filing.

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
items that depend on unverified work, naming each held item's blocker, and placing ready
`[user]` work above the marker. /done is the one close that always runs however a
session ends, so consolidating there is what stops it being silently skipped. The
spec-sync obligation is likewise the /done close's hard gate, not a duplicate here.

So closing a /plan session is just this: **"Run /done to record this and commit,
or keep planning."** No chat summary — the LOG entry /done writes is the single
session summary.
