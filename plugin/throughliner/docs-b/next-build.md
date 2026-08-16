---
name: next-build
docset: current
note: Execution procedure for build-flavor work items. Reached from next.md.
---

# Build procedure

next.md routes here for each build item (a work item with no flavor tag).

## Execute  [SILENT]

The silence governs the **success path** — making changes and ticking the item
when things go fine. It is not a gag on the moments that must speak: reporting a
failure, asking before scope grows, and revealing a readable edit's new text all
speak. A tag on one of those overrides this step's silence.

**Make the edit, then say what changed.** The work was already agreed in /plan,
so an edit goes straight in — no point-form list of what you are about to change
before it lands. Holds for every edit, readable or code.

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

**How the reveal renders** follows the view-in-doc rule (skill-nonspecific-rules.md). The
text is now doc-resident, so: a plain link to the edited file with the line named
in the prose ("around line 40" — the app ignores a link's line anchor), falling
back to an inline excerpt if the link won't resolve. If the user took the opening
inline-text offer, paste the new wording inline as a wrapped block instead. Either
way, only after the write is confirmed.

**The run's answer is in the working file's `Edit display:` line**, including any
items the user agreed to keep on line references. Read it rather than deciding
per edit — the judgment was made once, when the run was presented.

Note what this is not: showing an edit is **visibility**, not approval. The item
was already agreed at /plan and stop is always available, so displaying an edit
waits on nothing and the run stays unattended. Show-before-write is the thing
that gates, and it is a separate switch in the rules file.

**A small mid-build tweak to a just-surfaced readable edit is in scope**
[PROMPT]. Once the new text is visible the user may ask to change one bit. That
refines the build's already-agreed work product, so: make it, reveal the updated
text, and record it in the build working file Changes so it folds into the LOG entry /done
writes. No separately logged object, no /plan round-trip. A request that's
actually new scope — a different feature, or a change to something that already
worked — routes out via Scope management below.

## Build the item

```
1. read relevant existing code or context
2. make the changes                        # no point-form preview first
3. if readable content -> reveal the new text (informational, no ask)
   if code             -> stay silent
4. check what was built against SPEC       # SILENT unless it contradicts
5. tick it, in whichever of the two forms is true (see below)
```

**The tick takes two forms, and choosing between them is not optional.**

```
built AND confirmed      ->  - [x] item description — done, confirmed
                             # something ran and passed: a suite, a command, a
                             # read-back, an inspection of the output

built, NOT confirmed     ->  - [x] item description — done, UNCONFIRMED:
                                   <what still needs running>
                             # name the check, the command, or the observation
                             # nobody has made yet
```

**A build that ships code nothing ever ran is not rare enough to leave to
judgement.** The tick used to mean one thing — the writing finished — and carried
no claim that anything ran, while a shipped safety rule in `done-plan.md` already
depends on the built-versus-confirmed distinction: an item whose prose names a
slug that LOG records as built but not yet verified is held below the readiness
line. Its input was whatever prose a previous session happened to write. One rule
wrote the distinction by choice; another read it as though it were guaranteed.

**Written here rather than required of the LOG entry, and that is the whole
point.** An obligation discharged by remembering to write a sentence at the close
is indistinguishable from one skipped. The mark is written at the moment the
knowledge exists — the build has just run or just not run the thing — rather than
at the close, where it has to be reconstructed. Same reasoning that moved the rule
gate's disposition onto the queue item.

The tick lives in the build working file, not in QUEUE.md, so no hook parses it
and the queue lint needs no change — verified rather than assumed.

**Step 4 checks the work against SPEC; it never edits SPEC to fit the work.** SPEC
was read once at run start (next.md's pre-flight), so this costs almost nothing,
and a contradiction caught at the item that caused it is far cheaper to fix than
one found after five more items are built on top of it. **Silent unless it finds
something** — an unattended run must not narrate a passing check.

```
built work agrees with SPEC        ->  say nothing, tick, continue
built work CONTRADICTS SPEC        ->  [PROMPT] stop and name which SPEC sentence
                                       it contradicts, in plain words. The user
                                       decides whether the build is wrong or
                                       SPEC is.
build establishes NEW product      ->  the ordinary scope-grow route below: ask,
  truth SPEC doesn't yet carry         add SPEC.md to Files, edit inline
```

**A check Claude can run is part of building, not a separate test.** Run whatever
verification you can — read the code back, run a command, inspect output, check
file content — as part of getting the item right.

```
a check Claude CAN run   ->  just building
a check needing the user ->  a [user] capture, which /plan would have kept as
                             its own item; /next walks the user through it
a check Claude can run   ->  it stays OUTSTANDING in the run's working file.
  but a circumstance of      Retry it before the close; if the circumstance
  the moment blocks          still hasn't cleared, the close files it as a
  (the app must be on        capture. No new state, no new tag.
  screen and stealing
  focus would interrupt
  the user)
```

If mid-build you discover the work needs a user-run check that isn't already a
`[user]` item, route it (see Course-correction) — don't invent a deferral here.

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

**Where the project's own instructions require a rule-gate disposition, it is
transcribed from the item, never composed here** — see next.md's per-item
completion step, which also says what to do when the item carries none.

## Scope management

**When a mid-build discovery is work only the user can run** — a rename you can't
do, an account action, a device step — **file it as a `[user]` line, never float
it as a live question.** The failure to avoid is waving it off as "separate work
you'd handle yourself" or asking a yes/no about it: that leaves real work living
only in chat. If you can't yet script every step, file the line with a rough
walkthrough anyway.

### User raises something out of scope  [PROMPT]

```
1. write the capture into Unprocessed, placed per the Captures placement rule
2. report in one line what was filed and where it went, WITH one clause saying
   why it is being captured rather than done now
3. ask "anything else?" — repeat until no
4. resume the build
```

**The reason clause fires every time, not only when the user sounds impatient.**
Judging whether someone wants it now is a noticing-based trigger, and this method
has repeatedly found those do not fire — a session that has settled on an answer
notices nothing. Firing always costs one clause. It is one clause, not a lesson:
the reason is given so the user can act on it, not taught.

What to say, drawn from what capturing actually buys: it protects the run from
drift; the item gets weighed against work still to come rather than against
whoever is in the room; and it gets a keep-check and a file list before anything
is written, which is what stops a half-designed change landing mid-run.

**On a second ask for the same thing, yield** — the same intent counts, not the
same words, and Claude judges that rather than pretending a mechanical test
exists. Claude's standing rules already hold that where a concern is raised and
the user repeats the request, that is their decision and the work proceeds; this
is that pattern reaching build scope.

```
second ask, MINOR (1-2 files)  ->  carry it through. Append any unlisted file
                                   to the working file's Files: BEFORE editing.
second ask, SIGNIFICANT        ->  still propose the split. A repeated request
                                   does not make a large change small, and
                                   absorbing a many-file change mid-run is what
                                   the run bound exists to prevent.
```

**Coherence exception** (narrow, keyed to throughline coherence): if the item
would share the built item's log entry and index line, and folding it in makes the
work *easier to find later*, add it to the build working file as part of this item's work
(appending any files it names to `Files:`) and continue. Evaluate against the
coherence rules, not user convenience. **When uncertain, capture.**

### Scope grows during the build  [PROMPT]

The trigger is growth against **the described work**, not the Files: list. Name
the new work and the files it needs, then:

```
minor        ->  ask to add it: "This needs [work], which means editing [file] —
(1-2 files)      add it to scope?" Once approved, append any unlisted file to
                 the build working file's Files: BEFORE editing it — the scope-lock denies
                 edits to unlisted files.

significant  ->  propose splitting. Finish what's scoped, /done to close, then
(many files,     /plan to queue the rest.
 design
 uncertainty)
```

**A SPEC change the build discovers it needs is a legitimate scope-grow.** Name
the change and ask, then append SPEC.md to `Files:` before editing. Safe in-build
because spec-driven development wants the spec to move in the same commit as the
behaviour change, and the /done-build spec-sync gate backstops it. **A SPEC
change is product truth, so it always gets the explicit ask** — it never rides in
silently.

**The ask names itself as the normal route**, in the same breath as the change:
this is the standard path when a build establishes product truth the spec does
not yet carry, and it always asks first. Say it as something routine, not as a
request for an exception — e.g. *"This adds behaviour the spec doesn't describe
yet. When that happens the build asks before touching SPEC, which is what I'm
doing now: I'd add the sentence 'X' to SPEC. Add SPEC.md to scope?"*

Read cold, an unexpected request to edit product truth mid-build looks like a run
asking permission to break a rule rather than a run following one — **the method's
own author read it that way.** An external non-coder has strictly less context, so
the likely consequence is worse than confusion: they say no to a change the method
wanted, and SPEC silently falls behind the behaviour.

**The SPEC-contradiction halt above is not this and must not be softened to
match.** That branch is a genuine "something is wrong here" and stays alarming.

**What may be written into SPEC is governed by the three SPEC-maintenance rules —
admission, rationale-leaves-the-sentence, and staleness — in plan.md's "SPEC is a
normal doc" ground rule.** Read them there rather than restating them here, so the
two sites cannot drift.

## Mid-build course-correction

### Claude discovers user-runnable testing is needed  [PROMPT]

When something will need user-runnable testing beyond this build — a visual check,
physical-device behaviour, a subjective judgment you can't verify — and it isn't
already a `[user]` item:

```
1. append it to Unprocessed as a [user] capture (what needs checking, and why)
   write it, then report in one line what was filed
2. ask "anything else?" — repeat until no
3. resume the build
```

Don't attempt the check inline if it genuinely needs the user, and don't extend
this item's scope to include it.

**Before assuming a device or environment is absent, check.** Ask whether one is
available rather than assuming none is; a check wrongly skipped on a guess sits
unrun for weeks.

**And confirm before connecting to or acting on the user's physical device or
external hardware** — adb against a connected phone, flashing firmware, driving
attached hardware. Ask — "May I use your connected device to test this?" — and
wait for a yes. A channel like adb reaches far past installing one app, into the
user's whole device, so using it silently is a consent surprise.

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
                      Update the build working file to match.
abort and requeue ->  if the item is unsalvageable:
                        a. return it to QUEUE.md's Processed (placement is your
                           call — original position or top, by what was learned)
                        b. append any captures surfaced during the attempt
                        c. append the reshape direction, naming the item's slug
                        d. tell the user to run /done
```

The reshape-direction trigger is mechanical: *abort + item returned + a reshape
direction or learning the queue needs in conversation = capture needed.* Unrouted,
it survives only in the LOG entry, which /plan doesn't read at planning time, so
the item re-presents unchanged at the next /next.

the build working file stays in place so /done's router still fires the build close-out. The
differences: the LOG entry describes the attempt and why it was aborted, and the
item returns to QUEUE.md rather than disappearing into the log.

## Context management

You can't sense the context window filling — you only learn a session is wearing
thin when the **user** says so. So this isn't a trigger to watch for; it's what to
do when the user reports the squeeze.

```
most of the run is ticked      ->  finish and /done. Short-term memory is enough.
significant work remains       ->  close partial: /done what's ticked, requeue
                                   the rest. The next session picks up cleanly
                                   from the build working file and QUEUE.md.
```

Either way, pair it with the fresh-session handoff offer.

## Completion  [BRIEF, PROMPT]

When this item is done, next.md moves to the run's next. When the whole run is
built (every Claude-work item ticked, any `[user]` item walked through):

```
1. tell the user the build is complete
2. say what remains — nothing to record yet, and the option to tighten what
   was just built before closing
3. do NOT end on a command string. Naming the close as the thing to type, at
   the end of a long finished piece of work, is how a completion message gets
   acted on as an instruction. The user reaches for the close themselves.
```

Recording still only happens at the close — that is why nothing else is
recommended here, and never another build.

Tightening means refining done work — not raising new work. Anything new routes
through the existing paths. **No chat summary of the changes** — the LOG entries
/done writes are the single session record.

**Do NOT delete the build working file yourself.** That's /done's job.
