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
  instead is a **prompt**: a write to anything outside the quiet-list asks the
  user first. The quiet-list is QUEUE.md, SPEC.md, LOG/, this session's own
  notes, and **FAQ/** — the close's FAQ-sync disposition is a mandated edit, and
  a required step that prompts every time trains the user to click through the
  ask that matters. Three more paths pass silently here as they do everywhere
  else: the user's memory directory, `resources/research/`, and the session
  scratchpad. `templates/` is deliberately **not** on the list — editing a
  template changes what every future project receives, which is exactly the
  class of change the gate exists to surface. It asks, it never denies, because
  in planning there is no agreed file list to drift from — the user is right there,
  and a legitimate write is authorised in one word. Treat the prompt as the point:
  it doesn't stop you doing something urgent, it stops you doing it unremarked.
- **One item at a time.** Finish one before presenting the next.
- **Read SPEC.md before proposing work.** Don't queue contradictions.
- **Process the accumulated unprocessed work before new planning work.**
- **Approval attaches to exact text, never to a described shape.** A
  recommendation, however concrete, is not a draft, and "I'll add a line that does
  X" is not the entry. What changes is *where* the user reads that text: write it
  into QUEUE.md first, then give a short summary plus a pointer to it, full text
  on request (plugin-behaviour.md's doc-bound-text rule), and they approve it in
  its final position. If they say no, take out exactly what was written, re-read to
  confirm it's gone, and say so. The rule keys to the *write* either way, so it
  holds even when a compacted session has lost track of which beat it's on: no
  QUEUE.md line stands without the user having read those exact words and agreed.
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

- **Research is never queued for /next.** Its only output is knowledge —
  findings, corrected premises, better-informed designs — never a build. So
  research that turns out to be needed in /plan is conducted **then and there**,
  in /plan.

  **The tell: a work item whose first step is "research X" is the sign that
  /plan skipped its own job.** Queuing it defers the very information the
  planning discussion needed, so the item gets designed on an unverified premise
  and the research arrives later as a stale errand.

  Two boundaries, both stated because the prohibition creates real pressure and
  a prohibition with no named alternative reliably produces an invented one:

```
"does anything survive this work    ->  the discriminator. YES = it is a BUILD,
  except knowledge?"                     whatever its subject. A measurement
                                         harness leaves a runner, scenarios and
                                         checkers behind — that is infrastructure,
                                         not research, and the rule must not
                                         swallow every investigative-sounding item.

a genuinely MULTI-SESSION           ->  it stays in Unprocessed, and its
  investigation                         PROCESSING is the research — across as
                                        many /plan sessions as it takes. It never
                                        becomes /next work and needs no new
                                        container.
```

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
The read is governed by the page-to-completion rule (plugin-behaviour.md): when
the file comes back capped, page it to the end before any queue-wide reasoning —
ordering, dependencies, the readiness line, duplicates, the below-line revisit
all need the whole queue in view.

Everything this step surfaces folds into **one** opening narration, per the
consolidate-the-scans rule.

**Read the forward-recommendation advisory** [SILENT when absent; BRIEF when
present]. If the top of Unprocessed holds a "Last session advises…" line, read it
and let it orient *where the session starts*. It never narrows the session to only
the advised item — Step 2 still processes the full queue. Surface it in one line:
"Last session recommends starting with [slug]." Orientation, not a command. The
**clear** happens at the /done close, not here, so it can't be skipped by a
session that ends via an off-ramp.

**Missing-setting catch-up** [SILENT when nothing is missing; BRIEF otherwise].
Read the project's CLAUDE.md and check it carries the settings the current
templates add. Missing one → **add only what's missing**, never rewriting or
clobbering anything the user wrote. Where a setting needs an answer, ask for it
in one line here.

**This lives in /plan, and its location is the fix rather than a detail.** It
used to run from the session-start hook, which fires before anything knows what
the session is for — so its question could not pick a good moment and simply
attached itself to whichever command came first. It wedged an unrelated ask into
a close, and on another occasion held a queued /next run behind a question about
a setting the method had since retired. /plan already reads project state,
already folds what it finds into one opening narration, and cannot hold a build
run — which is the whole point of it being here.

**Whatever asks must say why it wants the answer.** Name the setting, what reads
it, and what changes once it is answered. The question that failed did so on two
counts and only one was timing: *"Which .md editor do you work in here?"* was
also unanswerable, because neither the user nor the session asking could say
what the answer was for.

**No completion sweep for `[user]` work.** /plan never asks whether Processed's
`[user]` items are already done — that ask is gone from the method entirely, and
so is the setting that used to toggle it. If the user mentions having done one,
close it at this session's /done (log under its slug, remove from Processed) —
and where the item names an observable result, the close checks the world
rather than accepting the report (plugin-behaviour.md, the `[user]` lifecycle);
otherwise leave them alone and say nothing about them.

**Below-the-line revisit** [SILENT when nothing lifts; BRIEF when proposing a
lift; PROMPT only for the consolidated user-only question]. Walk the below-line
items; for each,
read the lift-condition its prose records and classify:

```
mechanically checkable    ->  check silently; if cleared, propose lifting
    (a dependency built per LOG, a push done, a file now present)
set aside, retry is       ->  CHECK IT SILENTLY, exactly as the first row.
    CHECKABLE                     The marker suppresses asking, not seeing. If
    (the item carries a           it has cleared, propose lifting — a proposal
     Set aside · line AND         on a condition that really cleared is news,
     something could check        not a re-offer.
     its condition)
set aside, retry is       ->  skip silently. The user's "no change" or "not
    USER-ONLY                     now" already answered this question; it
    (the item carries a           re-surfaces only at queue exhaustion, or
     Set aside · line and         when the user raises it themselves.
     only they can say)
user-only                 ->  DON'T ask per item. Gather every user-only
    (an external event            condition into ONE consolidated question,
     only the user knows)         asked once this session.
provably still-waiting    ->  skip silently
SPENT                     ->  surface it for a rewrite, don't skip it.
    (the anchoring event has        The condition can no longer happen as
     already passed, so the         written, so "has it happened yet?" will
     condition can never clear)     return "no" forever.
```

When the consolidated question comes back "no change" for an item, that answer
is a set-aside signal: record the `Set aside ·` line on the item
(plugin-behaviour.md, Set aside), quoting the answer, so later sessions skip it
instead of re-asking.

**And where that item's condition is one only the user can answer, say so in one
line as you record it.** Nothing will raise this again on its own; the user
mentioning it is the route back. The behaviour was already correct and completely
undiscoverable — a user had to ask what would ever prompt them before anyone
noticed. Disclosure costs a sentence at the one moment the user is looking.

**Queue exhaustion is a way back, not a guarantee:** when the queue offers nothing
else — no cleared work, nothing unprocessed but set-aside items — raise them
plainly. On a working queue of dozens of items that condition will not arrive, so
don't lean on it. The silent check above is what actually reaches.

The spent outcome exists because a dead anchor reads exactly like a live one:
the revisit asks "has it happened yet", which silently returns "no" both for a
condition still waiting its turn and for one whose occasion is already gone. An
item in that state sits below the line forever with the revisit reporting
nothing wrong. When one surfaces, propose rewriting its condition to a
repeatable future event — the recording rule in done-plan.md — or returning the
item to Unprocessed if what it waits on no longer exists at all.

Per-item asking is the nagging this revisit exists to avoid. An item with no
recorded lift-condition can't be classified without nagging — note it as a gap.

**Before asking any user-only condition, run the downstream-action test:** is
the awaited event downstream of an action the user has to perform first? "The
collaborator replies" reads like an external event, but if the user has never
sent the message, the revisit will ask "has it happened yet?" forever about a
thing that cannot happen — user work existing only as a recurring chat
question, manufactured by correctly-followed rules. If yes: that action is a
`[user]` work item — propose filing it, with the condition rewritten to wait
on *it*. If no (a restart, a release, someone else's unprompted move), the
condition stands and joins the consolidated question. When several conditions
await the same person, one `[user]` walkthrough carries all of them — never
several walkthroughs that have the user message the same person repeatedly.

**The set-aside marker is what stops the repeat-ask** — it replaced the older
escape (asking across several sessions, then proposing a return to Unprocessed).
One such item was asked about at three consecutive sessions, and the user's
irritation was entirely fair: it was never a priority, it was just
unsilenceable. Now the first "no change" records the marker and the asking
stops there, with queue exhaustion as the guaranteed way back. The marker is
recorded from the user's own answer, never proposed by Claude.

The bottom of Unprocessed and the set-aside marker are the **only** legitimate
ways to postpone something — a queue move, and a raise-suppression that moves
nothing. Do not invent an alternative — a new state, a "lift when you raise it"
condition, a quiet shelf — no matter how much pressure the repetition creates.
Those aren't postponing, they're losing the item somewhere nothing will look
again.

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
Processed**: seeding fills the backlog, it never greenlights a build. Write the
items into Unprocessed as ordinary captures, re-read to confirm, then put a short
summary plus a pointer in front of the user for approval — and edit back out
whatever they reject.

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

**Position in the file sets the durable DEFAULT order — the order anyone
resuming cold inherits — not an order this session is bound to.** A session may
work its own order at the user's request; the file stays authoritative for
everyone else.

**So when the user asks for prioritisation, default to a session-local focus
order rather than rewriting the queue.** Rewriting pays a full mechanical
rewrite for something a session can simply hold as an order of attention, and
where the user's real want is *which work gets attention next*, the cheap answer
already satisfies it in full.

```
"focus on X first" / "do the      ->  SESSION-LOCAL FOCUS ORDER: state the
   design forks" / "leave the          order, work it, skip what doesn't match
   user items"                         as you reach it. Narrate it ONCE.
                                       Move nothing.

"reorder the queue"               ->  don't just execute it. First ask what
   (an explicit request)               outcome they want — usually about the
                                       next build or two — then name a
                                       non-reorder route that reaches it AND
                                       offer the reorder anyway with its cost
                                       named. Their call either way.
```

**The second branch is not a refusal.** The reorder is still honoured on
request; what changes is that it stops being taken as a bare instruction. One
question is cheap, and it frequently reveals the want is "build this next",
which the readiness line or a focus order already delivers. Offering the reorder
in the same breath is what keeps this from reading as talking the user out of
what they asked for.

**Narrate the divergence when you work a focus order** — one line, at the point
you adopt it. The objection this answers is real and was nearly fatal to the
rule: a session that silently works a different order from the file leaves the
real order living only in `_plan.md`, which the close deletes. Declaring it as
sanctioned and session-scoped is what fixes that — the defect was never a
session having its own order, it was the order being undeclared while the doc
claimed otherwise.

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

**The check's subject is any load-bearing claim in play, not only the item's.**
Same test, same cheapness, one more subject: it applies to what *you* are about to
assert as much as to what the item asserts. That widening is one word in scope and
it closes a real hole — the verification rules all point at text somebody else
wrote, so a recommendation's own premises are checked by nothing. The failure that
earned it: asked a direct question, Claude recommended making the repository
private, which would have ended every install and update, because the plugin is
distributed from inside that same repository. One grep of README.md would have
caught it, and the fact it establishes was already written in the project's own
CLAUDE.md. A recommendation is made at exactly the moment a confident answer is
most welcome and least examined, which is why the remedy is an action taken
*before* speaking rather than a restraint applied while speaking.

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

**When the user asks how their work maps onto the method, read the doc before
answering.** /plan is where domain-mapping questions land, and it is where a
claim about what a skill, hook or queue mechanism does gets made with the most
authority and the least checking. The claim to be most careful with is the one
made in passing — a clause inside an answer to a different question, which is
exactly the shape that has gone wrong here. And don't build an inference on such
a claim and present it as a finding before the claim itself is checked
(plugin-behaviour.md, the diagnosis-order rule turned inward).

**Resolving a check in-session is right; DRIVING a verification that already has
a home is not.** Before running or walking the user through a test, ask one
question: **does this work already exist as a tracked item?** If it does, stop —
route it to /next, which walks a `[user]` item live and carries its findings
through the proper close, rather than scattering them as loose captures. If
nothing is tracked, the file gate already governs the write, so do it here and
now: deferring a small instrument that unsticks the discussion re-creates the
cycling it would have fixed. Full rule in plugin-behaviour.md, under the
routing-and-discipline rules.

**Follow-ups inherit the solicitation rule** (plugin-behaviour.md, the private-
information section): don't ask for sensitive identifiers — addresses, account
numbers, keys, payment details — that the item doesn't need to be actionable.
The user holds those details at the moment they do the work; the item almost
never needs them, and an answered ask is one draft-review away from a public
commit.

```
closing the interview:
    delete lean already clear  ->  close on the combined recommend-and-ask
                                   (see sub-step 2's merge guidance)
    lean not clear yet         ->  close with "anything else to add?" and let
                                   sub-step 2 carry the recommendation
```

**View-in-doc.** The item already exists in QUEUE.md, so lead with a short
summary of what it says and a one-line pointer instead of the full pasted quote —
`First item — **[work-slug]** — is in [QUEUE.md](QUEUE.md) under Unprocessed,
the heading beginning "<the item's exact opening words>".` — then the analysis
in that same message, with the item's full text on request. Carry the heading
text: the link lands at the top of the file, so it is what turns a scan into a
search. The confirm re-read still runs in its pointer form (a resolves-check,
not a text-match).

**2. Recommend**  [PROMPT]

```
keep    the work is worth doing -> move it into Processed
delete  remove it. If already decided (check LOG/index.md), state the prior
        decision and commit.
```

**A keep recommendation must describe what would actually get built**, in terms
the user recognizes as the work product — which files change, what gets added,
removed or rewritten, not just the topic. **This is a blocking check, not a
prompt to try harder:** before recommending keep, state the build in both limbs
— the files that change AND what changes inside them — and if either limb can't
be stated, the keep cannot proceed. Naming files alone is not passing: "Files
(rough): plugin-behaviour.md, plan.md" is exactly what undesigned work looks
like, and items in that shape have reached Processed and stalled a /next run
that had a file list and nothing to build from. An item that can't pass both
limbs gets sharpened further in the interview, or skip-to-deferred with its
design progress written into its prose — never kept.

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
the discussion's reasoning inline. The draft inherits the private-information
rules (plugin-behaviour.md): no solicited identifiers, and context about the user
written as decision-plus-reason, never as an assessment of the person.

*When keeping several findings from one audit, destination follows the
consolidation rule* (plugin-behaviour.md's bulk-approval inversion): unambiguous
repairs consolidate into one work item with numbered points; a finding carrying
a design call stays standalone. Still discussed one at a time — the rule sets
where kept work lands, never how it's decided.

*Merging or folding one piece of work into another follows the Files-list test,
not an ask* (plugin-behaviour.md, dependency ownership):

```
merge does NOT widen the Files list  ->  free. Narrate it and proceed.
merge DOES add files to the run      ->  a widening. Still asks.
```

Whenever a merge is narrated or proposed, name what it does to scope in the
same line ("this adds no files" / "this adds two files") — the narration is the
catch-point that lets the user object before scope compounds.

*Group items by shared scope, and let the GROUP be the unit that moves.* Items
whose Files lists overlap process and build better together — one coherent pass
over a file instead of three sequential ones — and where a group is agreed
together, it moves into Processed as a unit and runs as one. That is one
decision instead of three.

This **promotes** clustering from where it used to sit. It was a tie-breaker
applied only where it was free; it is now the unit work actually moves in. What
does not change is the precedence, and it must survive intact or a blocking item
gets starved because it belongs to a different group:

```
1. dependencies       ->  a blocker runs on its dependency order, whatever its
                          file scope. NEVER displaced by grouping.
2. unblock-potential  ->  the existing ordering principle, unchanged.
3. shared-scope group ->  the unit work moves in — applied after the two above.
```

**The grouping changes the packaging, never the standard.** This is the risk the
old tie-breaker bound was written to prevent, and promoting clustering does not
retire it: **sharing a scope is not evidence that work is ready.** Every item in
a group still passes the keep-step on its own merits — files named, and what
changes inside them — or it does not go. The group moves; the standard stays
per-item. Without that, an undesigned item rides in on a well-designed sibling's
coat-tails because it happens to touch the same file.

Clustering also stays a **preference, never a gate**: a run is never limited to
one group, and an array of misfits is sometimes the only option and must still
run.

Groups are drawn from Files lists, which is mechanical — nothing has to be named
or refreshed by hand. Grouping happens here at processing, where Files lists are
firmed up; capture time is usually too early to know an item's scope, so record
a rough guess there where it's known.


*When the work would start something from scratch, ask whether a generator
exists for it* — the Android Studio new-project wizard, `cargo new`,
`npm create vite`, `django-admin startproject`, `dotnet new`. Scoping is where
this is cheapest to catch, because it decides whether the item is
"hand-assemble these files" or "run the generator, then edit what it made".
Hand-assembly fails hardest at build configuration, which is exactly what a
generator gets right. Where only the user can run the generator, that becomes
its own `[user]` work item with a real walkthrough, not a recommendation left
hanging (plugin-behaviour.md, the don't-hand-build counterweight).

*When the item is `[user]`, apply the matched pair now:* confirm it's genuinely
user-only (work Claude can run but can't run *yet* is Claude-work shelved below
the line — the over-tag guard); and **don't under-file** — genuine user work must
become a `[user]` work item, never a live chat question or a "you'd do that yourself"
aside. **The over-tag half is a check, not a judgment: name the tool that would
do the work and confirm it is absent or unauthenticated before the tag stands**
(plugin-behaviour.md, the `[user]` flavor rules) — a browser-sounding task with
a working CLI path is Claude-work, and this is the cheapest moment to catch it.
Then draft the walkthrough into the item's prose. Not being able to script
every step is **not** a reason to withhold the line: file it with a rough
walkthrough and sharpen it here.

*Decompose a mixed Claude-prep + user-step item.* When an item bundles work Claude
can do with an irreducible user action, don't keep it as one `[user]` item with
Claude-work buried inside:

```
Claude-doable parts  ->  build item(s)
the irreducible user action  ->  a single [user] work item, reduced to ONLY that
                                 action, cross-referenced by slug
```

**Write the item before showing it** — the doc-bound-text rule. Edit the block in
place, where it still sits in Unprocessed, to the drafted wording; re-read to
confirm it landed; then put a short summary plus a pointer (a link to QUEUE.md and
the item's exact heading text) in front of the user, with the full text offered on
request. If they reject it, edit the wording back out and confirm the removal by
re-read. On approval, **move it mechanically** — the never-retype rule still
holds: only the decision passes through you, never the prose.

```
1. EDIT the block in place, where it still sits in Unprocessed, to the
   drafted wording — BEFORE showing it, then re-read to confirm
   # the heading rewrite and rationale re-author are deliberate edits; the
   # [slug] at the end of the heading line stays exactly as it is
2. MOVE the block mechanically, once the user has approved:
       python <plugin-root>/scripts/reorder_queue.py QUEUE.md \
           --move-section <slug> Unprocessed Processed [--position ...]
   # relocates the whole block byte-for-byte; the item is never visible in
   # both sections, and nothing is hand-retyped
```

**Edit-then-move, and the order is the point.** The mover rewrites the whole
file, so editing a moved block afterwards trips the "file modified on disk since
you last read it" warning — on nearly every kept item. That warning is a real
safety mechanism (a concurrent session's write once destroyed an item heading
and reached a commit), and the file-safety rule is right to forbid reasoning
past it. But a warning that fires several times a session, always innocently, is
training the response to the dangerous case on schedule: one session ran the
mover on seventeen dispositions, checked every occurrence properly, found every
one benign — and recorded that by the fourth the pull to skip the check was
noticeable.

Reversing the sequence spends nothing, because it **removes the collision
instead of excusing it**. No exception has to be written on a safety rule, and
no judgment has to be made about whether this occurrence is the innocent kind.

**The one constraint, and it is narrow rather than fatal: don't change the slug
in step 1.** The mover addresses blocks by the `[slug]` at the end of the
heading line, so that token must survive the edit. Slugs are immutable by design
and survive reorders and renames anyway, so the ordinary keep — rewrite the
description and the rationale, slug untouched — is safe.

If the raw capture had no slug, give it one (an in-place edit in Unprocessed)
before the move — the mover addresses blocks by slug. Report "moved to Processed
as [slug]" only after a re-read confirms it landed in Processed and is gone from
Unprocessed.

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
When found buried in prose, split it into its own `[user]` work item with its own slug
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

**Delete** — Remove the item from Unprocessed, **via the mechanical mover**, the
same never-retype rule the keep-move and the skip already follow:

```
python <plugin-root>/scripts/reorder_queue.py QUEUE.md --delete <slug> Unprocessed
# removes the whole block, addressed by slug. It refuses rather than guessing
# when the slug resolves to nothing or to more than one item, prints the
# heading it removed, and keeps the readiness marker where it was.
```

Hand-editing a long block away with exact-string replace is what makes a scripted
shell splice start to look cheaper — the move this method forbids and that has
been reached for anyway. The command removes the reason.

**Relocate before removing when the
content belongs elsewhere.** Delete means "not worth doing," so routing a fold
through a plain delete risks dropping content the user wanted kept. When the
content belongs in another home — a SPEC sentence, a LOG entry, another item's
rationale — edit the target first with approval, then remove the standalone item.
Still a delete, just after its worth-keeping content has been carried across.

*Where a decided-no's reasoning lives — one test.* Does the decision merely need
to **sit in the record**, or does it need to **stop something recurring**? The
record case is the default and goes to the LOG (the /done entry carries the
delete and its why). The recurrence case needs an always-read home — CLAUDE.md,
SPEC, or the surviving item's own prose — and earns it only on evidence: the
question has *already* come back at least once, not a guess that it might.
Left unstated, every rejection tends to become either a bookkeeping work item
(queue inflation) or a LOG line nothing re-reads (silent re-litigation); the
test is what routes between the two failures.

**4. Checkpoint**  [PROMPT]

After every item, present the next item and close on the off-ramps as the
message's final, bold ask.

**Read `_plan.md` before naming which item is next or how many remain**, and
compose both from what it returned — not from what you remember of the session.
The numbered list written at the start of processing is the record; conversation
memory is not. This is the standing rule in plugin-behaviour.md's Context
awareness section, firing at the one step that makes tracked-state claims every
time it runs.

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
        python <plugin-root>/scripts/reorder_queue.py QUEUE.md Unprocessed \
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

**View-in-doc applies here too** — lead with a short summary and a one-line
pointer to the next item (carrying its heading text) in place of its verbatim,
full text on request, off-ramps below it unchanged.

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

**Write the candidates into Unprocessed first**, then present them as ONE numbered
set for a single approval — the doc-bound-text rule, applied to a result set. The
message carries a short summary of each, a link to QUEUE.md and the headings to
search for, and the ask; the full text is one word away on request. The user
contests by number, and only contested items go one at a time. A contested
candidate is edited back out, and the removal confirmed by re-read. Processing the
kept ones follows the normal flow, this session or later.

This is a best-effort safety net behind the capture-at-the-moment-of-noticing
rule. A non-coder who thinks out loud generates capturable material they never
flag.

```
/plan  ->  runs the FULL re-scan: files the captures AND can process them
/done  ->  runs a FILE-ONLY version (filing is allowed in any session;
           processing is what the no-planning-in-execution rule protects)
```

## Step 3: Point at /done  [BRIEF, PROMPT]

There is no separate close-out step here, and **never say "close out" to the
user** — the term names a step that was retired when its work moved into the
/done close, and hearing it makes users wonder whether running /done alone
skips something. It doesn't: the /done close runs everything — reordering both
sections, positioning the cleared-to-run marker, holding back items that depend
on unverified work, recording lift-conditions, placing ready `[user]` work
above the marker, and the spec-sync gate. /done is the one close that always
runs however a session ends, so consolidating there is what stops any of it
being silently skipped.

So ending a /plan session is just this, in plain words: **"Run /done and I'll
record this and commit it — or keep planning."** No chat summary — the LOG
entry /done writes is the single session summary.
