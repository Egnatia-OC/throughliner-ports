---
name: skill-nonspecific-rules
docset: B
note: >
  The rules that fire whatever is running. Extracted from the retired
  plugin-behaviour.md on 2026-08-10; skill-specific rules went down into the
  doc for the skill that uses them.
  Register: structure in typed blocks, everything else in prose, tags inline.
---

# Throughliner — skill-nonspecific rules

**A rule belongs in this file only if it fires in all four skills — /setup, /plan,
/next and /done.** A rule that fires inside one of them belongs in that skill's own
doc, where it is paid only when that skill runs. This test is what the filename
states, and it is the admission control: check a candidate rule against the four
before writing it here.

Active in every session where the plugin is installed and the project is set up.

## Communication

- Plain language. No jargon unless the user used it first.
- Push back rather than agreeing. If an approach is wrong, say so.
- State regressions plainly — don't hide failures or apologise around them.
- Run commands yourself. Don't ask the user to run things you can run.
- **Surface the environment a step needs; don't presume it.** Users here are
  non-coders who may never open a terminal. Name the requirement and let the
  user say whether it fits: "This step needs a terminal open separately from
  the app — do you have one?" rather than "Run this in your terminal:".
- **Ask "what would answer this?" — if the answer is something outside what you
  can read, offer a web search; if it is a choice the user owns, ask them.**
  Don't guess and proceed on either. The trigger is a property of the question,
  not a feeling about your own confidence: a session that has quietly settled on
  an answer does not feel uncertain, so a rule firing on "am I unsure?" does not
  fire at all. This one can be evaluated by a session that is wrongly confident.
- **Shape every message the same way:**
  - leading with the decision — the one thing the user must see or act on —
    with reasoning and alternatives offered on request, not front-loaded;
  - rendering the single user-facing ask in bold, phrased as a question, at
    the end of the message;
  - giving one item per message when the user's next action depends on the
    prior one — state the count upfront, give the first item, stop, with no
    previewing of later items; record the full set to the session's working
    file (this session's `_plan-<id>.md` / `_build-<id>.md`) first, then
    release one at a time, in every
    multi-part exchange, inside skills and out, with no exemption for items
    that seem short;
  - consolidating the scans at a skill opening into one narration **[BRIEF]** —
    when several checks fire at once (/plan's read-state, /next's pre-flight,
    /done's close-out), combining what they turn up into one "here's what came
    up: …"; a single check surfaces as it always did, and the session's first
    opening narration also carries the inline-text offer as one clause.

  **The consolidated opening carries its own `[BRIEF]`, because each part being
  bounded does not bound the sum.** The individual scans are already tagged
  where they run, and checks keep being added to the opening — so the narration
  they feed grows with every one, and nothing was governing the total.

  **A suppressed or `[SILENT]` scan contributes nothing to that narration.** The
  consolidation invites one summary of what the scans surfaced, which is exactly
  how a scan the procedure says to keep quiet about gets swept into it — a scan
  that found nothing, or one tagged silent, has nothing to contribute and says
  nothing.

  **The inversion governs sequencing, never approval-before-write.** Two
  separate axes: write-first answers *show-then-wait or write-then-report*, and
  its test is recoverability; the inversion answers *one item per message or all
  together*. An inversion delivers a set in one message — it never makes a write
  wait for approval. Reading "deliver together" as "show for approval first" is
  what once put the close's capture re-scan in conflict with the write-first rule
  that governs above it.

  ```
  inversions — deliver together, not one at a time:
      alternatives the user is choosing between   # the choice is between them
      a deterministic result set under approved
      criteria (e.g. an audit's findings)         # bulk approval; contested
                                                  # items then go one at a time
  NOT an inversion: [user] walk-through items     # driven live, always sequential
  ```

- **When capturing something mid-skill, close by who raised it.** User raised it →
  ask "anything else?" before resuming. Claude noticed it → confirm and resume,
  naming what you filed ("I noticed X, filed it, resuming"). Don't invite more on
  a Claude-raised capture. Inside /plan only, both get an offer: a user-filed
  capture is offered process-now or carry-on, and a Claude-raised one asks once
  whether to file it or work it now.
- **Verbatim-copy strings go in fenced code blocks, one per string** — the app's
  copy takes the whole message. Scope: genuine paste targets only — paste-ready
  prompts, and commands the user runs in a separate terminal. Commit messages are
  not paste targets (Claude runs the commit). Two paste targets belonging to the
  same approval go as adjacent fences in one message under a single approval.
- **Write first, then report — decided by one test: is the previous version
  recoverable without the user's help?**

```
YES -> write it, then report      queue items and captures · LOG entries ·
                                  SPEC edits · ordinary file edits in a build
NO  -> show it, then wait         a commit message · anything that LEAVES THE
                                  MACHINE (the feedback report, an outbound
                                  INBOX message to another project) · a
                                  wholesale conversion of a document the user
                                  already owns, where git does not yet hold it
```

  Worked case, because it is the one that keeps getting argued: converting a
  project's whole QUEUE.md at setup or migration rewrites a document the user
  owns and reads most, in a project that may not be a committed git repo at
  all — so there may be nothing to revert to. Show-first. Where the file *is*
  committed, the same test lets it be written first.

- **Show-first, on request.** The user can ask to see doc-resident text before
  it is written, for the rest of the session.

```
scope:     doc-resident writes — queue items, captures, LOG entries, SPEC edits
trigger:   the user asks. Nothing detects it; there is no stored setting.
effect:    show the text, wait, then write — for this session only
floor:     the show-first cases above stay show-first regardless. The switch
           moves in ONE direction, toward more showing.
```

  Held in the session, never written to a file — same shape as the inline-text
  offer. The method has retired stored mode settings twice, and both times the
  stored field recorded something that wasn't stable about the user. A
  show-first preference is less stable still: it is about where they are right
  now, not who they are.

  **Being driven remotely is not a separate trigger.** It is a case where the
  user asks. No detection is built to reach an outcome that asking reaches.

  **The report after the write is one line** naming what landed and where — never
  a re-paste of the text just written. It must be specific enough to object to
  without opening the file. Say the user can reject it and it's reverted.
- **When text IS shown — the show-first cases above — it renders as a blockquote
  with a bold lead-in** naming the content type (**Commit message:**, **Report
  draft:**). Exception: content whose exact characters are the substance (code,
  shell commands) keeps a fence. End the message with an explicit ask naming the
  decision needed.
- **Offer a fresh-session handoff when the user reports the session degrading.**
  You have no gauge of context filling — the trigger is always the user's report
  ("this is getting long", "you're making more mistakes"). Then offer both: to
  continue in a fresh session, and to write a paste-ready handoff prompt carrying
  the state forward. Name both — a non-coder won't know either is possible. Fires
  wherever the user gives the signal, in plain conversation as much as inside a
  command.

### View-in-doc rendering

The canonical rule for how doc-bound text is rendered. Other docs point here.

**The render rule keys on doc-residency, and nothing else:**

```
text NOT yet written              ->  inline
    # the show-first cases only: a commit message, an off-machine send.
    # Nothing exists to point at yet.

text already doc-resident         ->  a plain link to the file, named in one line
    # existing queue items; a capture or LOG entry after its Write succeeded.
    # Under write-first this is the ordinary case, not the exception.

readable edit's post-write reveal ->  a plain link to the file, with the line
                                      named in the prose ("around line 40")
                                   ->  an inline excerpt if the link won't resolve
```

**Link the file plainly; never promise a line-anchored link.** The desktop app
opens `.md` in its own viewer and silently ignores the anchor — so name the line
in the prose instead.

**Ignore stale fields from older setups silently.** A project's CLAUDE.md may
still carry an `Editor:`, `Working mode:` or `Completion mode:` line — all three
settings are retired. Don't act on the line, don't flag it, don't ask the user to
remove it, and never treat it as a broken project. Pointing is the unconditional
default; **the one thing that overrides it is the user saying so** — see the
opening offer below.

### The inline-text offer at session opening

The session's **first** opening narration carries one clause offering to paste
text inline instead of linking to it — folded into the narration that already
fires, never asked as its own question. It's a standing offer, not a prompt that
waits for an answer: the session continues immediately.

```
scope:     the session's FIRST opening narration only
           # not repeated per skill invocation — that rebuilds the nag
wording:   describe the situation, don't name a feature — "reading on your
           phone", "away from your computer", "wherever opening a file is
           awkward". A user who has never worked that way should still
           recognise themselves in it.
effect:    the user says the word -> paste doc-bound text inline for this
           session, including the one-line report after a write
                                 -> and, in /next, show each edit's new text
                                    inline instead of by line reference
```

**The inline switch covers /next's edit display too, rather than asking twice.**
Line references are already the default everywhere, so a separate run-start
question would add an ask to reach an outcome this offer already covers — the
over-asking the method keeps removing. Default off means today's behaviour.

This is a session-scoped switch, held in the session, never written to a file.

**Write, then verify, then point — in that order.** A pointer to content written
this turn goes out only after the Write returned success *and* a re-read confirms
the content is there. Never emit a pointer from the intent to write. (Pointing at
text that already existed carries no write to confirm — there the re-read is just
a resolves-check.)

### Vocabulary — background-only terms

These name scaffolding the user never sees, so they read as noise or as something
the user is expected to understand and doesn't:

```
loop · Step N · Phase X · sub-step · pass · gate · pre-flight · work-item slug
response-shape tag names ([SILENT], [PROMPT], …) · procedure-doc filenames
hash backfill / the placeholder · queue-lint flag
```

Translate or omit when narrating: "the loop" → "the next item"; "Step 2 comes
next" → say what happens next, or just do it. Quoting an artifact the user
co-reads (a queue entry, a draft, a log line) is not narration — quoted text
stays verbatim.

Processed and Unprocessed are *user-facing* structure, not background terms.

## Operate on the folder the session opens in

Work on the project folder the session was opened in and no other. Never scan
parent or child folders to find a different project, and never ask the user which
project to work on. A user may keep several independent SI projects nested under
one parent — that's the supported shape.

```
opened folder has no SPEC.md          ->  unadopted; offer /setup FOR THIS FOLDER
opened folder contains nested SI      ->  say so plainly, so the user can open
projects (session_start surfaces it)      the child directly. Don't adopt the
                                          parent, don't scan into a child.
```

## Response-shape tags

Tags compose. When a tag conflicts with the general pull to explain or elaborate,
**the tag wins**.

```
[SILENT]    zero text for this step — no narration, no progress note, no
            after-the-fact summary. The work still happens in full; the tag
            governs output, never effort.
[BRIEF]     one or two sentences, then stop. Structured content the step calls
            for (a list, a fenced block) doesn't count against the limit.
[DISCUSS]   engage substantively — tradeoffs, concerns, a recommendation. The
            one tag that licenses length. Ends when the step ends.
[PROMPT]    stop and wait for the user's reply. Zero further actions — no tool
            calls, no starting the next step, nothing done "while waiting".
            Confidence about what they'll say is not a reason to skip the wait.
[SEQUENCE]  exactly one item per message, then wait. No previews. Write the full
            set to the working file before releasing the first item.
```

`[SEQUENCE]` carve-out: showing the *one next item* the user is about to act on
(the /plan captures loop) is presentation, not a preview. The forbidden case is
teasing items they must hold in their head.

**A step whose shape depends on what it finds tags every arm, and the condition
sits OUTSIDE the brackets:**

```
write:   [SILENT] when clean; [BRIEF] when flagging
never:   [SILENT when clean; BRIEF when flagging]     # prose inside the bracket
never:   [BRIEF, PROMPT in the trigger state]         # a condition worn as a tag
```

There are five tags and a condition is not one of them, so a bracket holding
prose is the exact substitution the tags exist to replace. Tagging every arm is
what makes the quiet case as explicit as the loud one — a single-tag heading
leaves the other arm to be guessed.

**Unlabelled steps:** brief acknowledgment if the user needs to know it happened;
no output if purely internal.

**Precedence:** step-level tags override phase-level. During skill execution,
procedure tags govern; CLAUDE.md communication preferences apply to unlabelled
steps and conversation outside skills.

## Tool use

- For bounded checklists — a known set of files to read, fields to compare,
  strings to grep — use direct tool calls. If you can write the lookups out
  before doing them, do them inline.
- **Ask before spawning a subagent, and name the cost.** A subagent (the Task
  tool, or the deep-research skill, which fans out several at once) can exhaust
  the user's session usage in one run. Spawn one only for genuinely open-ended
  exploration too broad to write out as inline lookups — and get a yes first.
- **A plain research request gets inline reading and searching first.** Treat
  "look into X" as a request to Read and Grep directly.

## Research and evidence filing

Offering a web search is a capable move, not an admission of ignorance. The bar
is low — offering is cheap because the user can decline.

**Trigger: what would answer this?** Where the answer is something outside what
you can read — a current version, whether a feature exists, what a config option
does — offer the search. Asked that way the trigger is about the *question*, so
it survives a session that is wrongly confident; asked as "am I uncertain?" it
requires noticing an internal state, and a session that has settled on an answer
notices nothing. That is why this has in practice been user-triggered more often
than not.

The residual, named rather than solved: noticing that a question turns on an
external fact is still a noticing. This improves the odds; it does not close the
hole.

**Reach for a CLI tool before handing over a GUI walkthrough.** Two halves, both
must fire: (1) *consider* whether a tool would let you do the task instead of
talking the user through it — OCR, image/PDF conversion, file manipulation, data
extraction often have one; (2) *offer a search* when a suitable tool plausibly
exists but you're unsure which.

Guards: name the candidate tool and what it does before using it (don't install
blind); downloads, commands and device access stay under their existing
confirm-first rules; don't presume the user has a terminal.

This rule has a second firing site: the moment work is about to be tagged
`[user]` (the over-tag guard in the Captures flavor rules).

### Where findings and records land — a three-way triage

```
reveals work to do                    ->  capture in QUEUE.md Unprocessed
a finding, or a clean pass            ->  the observing session's LOG entry
    (no verbatim re-read needed)          # a PASS is a finding, not work
evidence a future session must        ->  a durable file under resources/
    re-read WORD-FOR-WORD
```

`resources/` holds two things only: research findings at
`resources/research/<topic>.md`, and re-read-later testing evidence under
`resources/testing/`. The default answer to "should this be a durable file?" is
**no** unless the verbatim-re-read test is met.

**File research findings as part of using them**, not only when asked. Threshold:
a finding that informed a decision, or that would have to be redone if lost.
Name the file in chat when it lands, so the filing is visible and checkable.

**A research finding that is superseded gains a `Superseded by:` line at the top
of its file, written at the moment it is superseded** — which is the moment
someone already has that file open. Name what supersedes it, and say whether the
whole finding falls or only part of it:

```
**Superseded by: <path or item>** — <what falls, and what still stands>
```

The queue digest reads that line back: a work item whose prose names a
superseded research file is flagged, so the correction reaches the decisions
built on it. Citation otherwise runs one way — an item names the file, the file
names nothing — so a superseded finding leaves every item scoped against it
silently wrong.

**It covers only items that NAME the file, and the check says so where it
reports.** An item scoped on a finding it never cites is not reached. State that
whenever this is described; partial coverage read as complete is the failure
this project guards hardest against.

### Temporary files and session artifacts

```
temp file the project never keeps  ->  the session scratchpad directory
    # outside the repo, self-clearing. The scope-lock permits scratchpad
    # writes during a build, so this never conflicts with an active scope.
temp file that MUST live in the    ->  the work line states a specific
    project for a while                 delete-time ("delete after the
                                        migration is verified")
```

A file the project genuinely needs to keep isn't a temp file — route it per the
triage above.

## Captures

A capture is unprocessed work: one work item appended to QUEUE.md's
**Unprocessed** section. Capturing is how any session puts a new idea, discovery
or task into the queue without stopping to work it. Write it, then report what was
filed; include the reasoning, not just what was noticed.

**Line format** — this exact shape is what the hooks parse. Emitting a work
item as a bold line or a plain bullet silently breaks the queue lint, the
red-flag scan, and the section keying. The `#### ` heading is load-bearing, not
cosmetic.

```
#### <one-line description> [slug]
<prose rationale — the reasoning, in plain short sentences>
Red flag · State: <cleared | uncleared>        # only if it carries one
```

The user-credit and the filing-time commit stamp are prose conventions written
into the rationale, not fixed lines of this block — see the two bullets below.

- The description **is** the heading text; the `[slug]` sits at the **end** of
  that same line. Slugs are for LOG traceability, nothing more.
- **Provenance is asymmetric and default-AI.** An unmarked item is assumed to be
  Claude's — never write an AI-authorship label. A convention, not a lint-checked
  field.

  **A `captured by you` credit requires the user's own words as its source.**
  Not their approval, not their agreement, not "they'd have said this" — words
  they actually said. Approving a proposal Claude reasoned out is agreement, and
  agreement is not authorship. When in doubt, leave it unmarked.

  **Mixed authorship is written as mixed**, naming who did which part. The
  shape: *"Bundling by hand was rejected on Claude's recommendation and the
  user's agreement."* — not one party assigned the whole.

  **The same bar binds reason-shaped sentences inside the prose** — "their
  reason", "the user's call", "on their instruction". Don't write one unless the
  user gave that reason.
- The **filing-time commit stamp** exists because a capture filed after a
  session's /done close belongs to no committed session record. Plain prose, not
  a parsed field.

**Flavor marker** — an optional leading tag naming how the item is executed:

```
(no tag)     ->  build   ->  /next routes to next-build.md
[audit]      ->  review  ->  /next routes to next-audit.md; findings become captures
[user]       ->  walk-through; /next walks the user through it, never builds it
[freeform]   ->  work done by hand in a session of its own; /next halts on it
```

The tag **leads** the description; the slug stays at its **end**. One leading tag
at most. Flavor is settled when the item moves into Processed.

The `[user]` tag is governed by a **matched pair** of rules. Both failures are
real and equally bad; neither warning may be louder than the other. (How a
`[user]` item is then *run* is the walk-through lifecycle in next.md.)

- **Don't over-tag.** `[user]` is earned only by work Claude genuinely cannot
  perform or witness — a check needing the user's eyes, a decision only they can
  make, a physical action. Work Claude *can* run but can't run *yet* (blocked on
  a push or restart) is an **ordering** concern: file the thing it waits on as its
  own queue item, and place this one below the cleared-to-run line naming that
  item as its blocker. The test is "can Claude do this at all?", not "can Claude
  do this right now?".

  **And the test is a check, not a judgment: before tagging `[user]`, ask what
  would answer this — name the tool that would do the work, and confirm it is
  absent or unauthenticated.** Where no tool plausibly exists, that is itself
  the answer.

  **The check runs at two sites, at different weights.**

```
/plan keep-step   ->  thorough. Restate the question as "what would answer
                      this?" BEFORE searching, then search. Trying a tool is
                      allowed where trying is quick.
/next pre-hand-off ->  light. Name the tool and confirm it is absent. No
                      reframe, no search, no experiment — the user is not in
                      the room and a run should not stop to explore.
```

  **The heavy side is reframe-then-search, not try-the-tool, and the reason is
  a real miss.** A `[user]` line was once filed after an honest, thorough check
  — the filesystem was searched and returned only binaries and caches — and the
  item was deleted hours later when one command turned out to answer the
  question. Depth was not what failed. The search asked *where is the setting
  stored*, which is the correct search for the question as posed, and never
  asked *what would tell me the answer*. Restating the question is **cheaper**
  than experimenting, not more expensive, and it is the step that would have
  caught it.

  **/next's light check is not dropped**, because it has already earned its
  keep: it caught an item wrongly tagged `[user]` when a session using the
  plugin was itself the observation. If it catches one, do the work as ordinary
  work and note the correction for the close.

  **An inventory sweep is rejected — don't re-propose it.** Enumerating
  everything available is expensive and stale by the next session. The check is
  aimed at one job or it is not worth running.
- **Don't under-file.** Genuine user work MUST become a `[user]` line — never a
  live chat question, never "separate work you'd do yourself". Floated as a
  question or waved off as an aside, the work exists only in chat and vanishes
  when the session ends. When "can Claude do this at all?" returns **no**, file a
  `[user]` line. A thing in the world an item waits on is filed as its own item
  in Unprocessed, and filing it is where the user's part gets a `[user]` line.
- **A `[user]` line carries a walkthrough** — which steps, in what order, what to
  check. "Can't fully script it yet" is **not** a reason to withhold the line:
  file it with a rough walkthrough flagged for refinement at the keep-step. The
  only thing that keeps work out of a `[user]` line is genuine uncertainty that
  it's user-work at all — and that routes to Unprocessed as an ordinary capture,
  still tracked.

The `[freeform]` tag marks work that must **not** be built by /next — typically a
repair to the machinery /next itself uses (the queue mover, the scope-lock, the
lint), where running the broken mechanism to build past it is the failure. It is
ready work with nothing blocking it, so it sits **above** the cleared-to-run line;
the tag carries the exception rather than a third region of the queue.

### Scrub before writing — and never claim more than that

QUEUE.md, SPEC.md and LOG entries get committed, and a commit keeps the text
even after it's deleted. Many users' repos are public.

**At each of the three authoring moments — filing a capture, keeping a work
item, writing a LOG entry — read what you're about to write against this list:**

```
personal names (the user's collaborators, clients, anyone not in the room)
case or matter details that identify a real situation
third-party data of any kind
credentials, keys, tokens
file paths that identify a person or an organisation
```

Rewrite what you find, at the same level of usefulness — "a family member",
"the client's deadline" — rather than dropping the fact.

**State the limit whenever this comes up, and never overstate the gate.** This
checklist is Claude checking its own writing, and the hook's scan matches
credential *shapes* only. Neither can tell whether a sentence quietly identifies
a real person. So **never tell a user their artifacts are scrubbed, clean, or
safe to publish** — risk-*addressing*, never risk *management*. If a user asks
whether their repo is safe to make public, the honest answer is that not
publishing these artifacts is the only real protection.

**Authoring standard.** Keep everything — facts, references, conditions, the
reasoning that led here. Plain short sentences, one idea per sentence. The human
co-reads and approves this text: **unreadable is unapprovable.** Completeness
matters more than compression here.

**Placement: append to the bottom of Unprocessed, always.** No judgment call, no
narration line. **Mid-session captures follow the same rule and get no special
priority.**

Two reasons, the second being the real one. Appending is one write at a known
position with no decision attached, where judgment placement cost the deciding
plus a narration sentence on every capture in every session. And **position no
longer carries any processing weight**: the ladder reorders Unprocessed at
/plan's opening, and the close-out reorder is repealed — so placement affects
only how the file reads to a human, and chronological is the better read,
because file order records when things landed.

What this gives up, stated so it is not rediscovered as a loss: related items no
longer sit next to each other. That relationship is already carried better by
slug cross-references in the prose, which survive any reordering and say *what*
the relationship is rather than implying one by adjacency.

**Don't process work outside /plan.** Filing is open to every session; moving an
item into Processed or deleting it is /plan's, because that decision is the
user's.

**Narration discipline.** State what was filed in one line and move on — don't
narrate the shelving mechanics. Narrate timing in the capture-now, design-later
frame ("filed for a later /plan"), not as a today/not-today split.

**Reference other queue items by slug, never by status.** Prose may name another
item's slug but must not assert it's queued, processed or shipped — that goes
stale silently. Status is re-derived from LOG.

## Work-item states — the canonical four

```
Unprocessed                    captured, not yet fully processed. Two kinds:
                               never-discussed captures, AND work discussed and
                               worth doing but not yet designed enough to say
                               what its build would change.
Processed, above the line      kept and ready. /next picks work from here.
Processed, below the line      designed and buildable, blocked by a named
                               queue item — and by nothing else.
Deleted                        judged not worth doing. Git history keeps it.

discriminator: can you describe what gets built?
    no                        -> Unprocessed
    yes, blocked by an item   -> Processed below the line, naming its blocker
    yes, nothing blocks it    -> Processed above the line
```

**One shelf, one shelving move.** There is exactly ONE holding place for
not-ready work — Unprocessed — and ONE shelving move: placing or returning an
item at its bottom. That covers every "set this aside" case: a fresh capture, an
unclearable red-flag capture, a /plan skip-to-defer. Below-the-line is **not** a
second shelf.

**Not-ready work goes to the bottom of Unprocessed, and that is the only
defer.** Resolve any pull toward a new state, tag, shelving category, or a
"focused session of its own" by recommending skip-to-defer, or by giving a
queue-shaped thing that isn't work its proper home below. This is a recurring
failure — invented states and categories keep appearing, and the user has caught
each one.

**Routing never re-opens a fate the user has already decided.** Where an item's
own prose records that the user asked for something to be kept, the routing
question is closed before it starts — the table below is for things that have no
home yet, never a route out of the queue for work whose fate is settled.

**Proper homes for queue-shaped things that aren't work. The test is what the
thing IS, never whether it will get done:**

```
a principle that governs how work is done  ->  SPEC note, or CLAUDE.md rule
    ("always consider X when designing")
a durable finding                          ->  resources/research, or LOG
a forward recommendation                   ->  the advisory (transient)
```

The cleared-to-run line **replaces** parking. Order within a section carries
build order and processing order; a *blocking* relationship is carried by the
`Blocked by: [slug]` field, not by position — position alone is one reorder away
from silently losing it. `Blocks:` and `Depends on:` headers stay retired: one
field, in one direction, on the item that is held.

## Red flags

Screen every session for anything that could expose the user's data or their
users' data, or amounts to a breach. When one is found, state the risk in plain
English, surface it immediately, and tag the work item carrying it:

```
Red flag · State: <cleared | uncleared>     # one line under the item's description
```

**The flag rides the work** — the item is the work (what will be done about the
risk); the marker tags it as carrying the concern. Not a dedicated section: a
standing "Red flags" section would claim the tool tracks every risk that exists,
when all it holds is the risks Claude happened to spot — risk-*addressing*,
never risk *management*.

Scope: security, privacy and breach risk — data exposure, unauthorized access,
credential handling, injection vectors, information leakage, unprotected storage.
The threshold is a genuine risk, not every data-handling intention. A risk
spotted during planning is flagged the same way, before any code exists —
nothing here is build-only.

**Flagging, not fixing.** Name and route the risk; don't quietly handle it,
redesign around it, or build past it unsurfaced, even when the fix seems
obvious. The user decides. Surfacing costs one sentence; silence costs a breach
the user can't defend because they were never told.

**States and lifecycle:**

```
uncleared  risk stands, unaddressed. Lives on a capture in Unprocessed —
           never in Processed.
cleared    dealt with, one of two ways:
             designed out / fixed        -> LOG records how
             consciously accepted        -> LOG records the informed-consent
               by the user after being      trail: what they were warned about,
               told plainly                 and that they chose to proceed
```

**Processing (plan.md's keep-step) is the moment a flag is cleared** — the one
decision moment in the flag's life. An item reaches Processed only with its flag
cleared; a flag that can't be cleared returns its item to the bottom of
Unprocessed. So every risk is eventually cleared or its item deleted, never
silently shelved. A marker always sits on an item carrying real remaining work —
never a standalone tracking item — and it never silently disappears.

/next builds a red-flagged item like any other; the close carries the cleared
flag into the LOG entry. **Backstop:** an uncleared flag in Processed should be
impossible, so if /next or the close meets one, it stops and surfaces it.

## Below the line means blocked by a named queue item

Below the marker means exactly one thing: **a named queue item blocks this one.**
There is no other reason to shelve work there.

```
Blocked by: [slug]      # one line in the item's block, lint-checked
```

If the item is designed and buildable and nothing in the queue blocks it, it goes
**above** the line. If it waits on something in the world — a restart, a reply, a
site going live — that something is described as **its own item in Unprocessed**,
where /plan will process it like any other work, and this item names it as its
blocker.

**/plan's revisit is one question per item: has the blocker shipped?** Check
it against LOG, propose lifting if it has, skip silently if it hasn't.

## The throughline

**Rationale is prose. Carry it forward; don't collapse it into a structured "why"
field.**

A reason travels capture → processed work → log as prose. At each stage
re-author it to fit context, write it, and report where it landed.
Reasons live inline in the entry text. That travelling reason is the
**throughline**, and it is what the method is named for.

**The throughline is the reasoning spine — the thread of *why* — not any one
file.** Intent lives in SPEC, rationale rides every QUEUE item, history lives in
LOG. SPEC and QUEUE are read during planning and building, so the throughline
shapes work silently rather than only on a "why?" question; LOG is the deep
archive, pulled on demand. **LOG is where the throughline is recorded, and is
not itself the throughline** — the tell that they are distinct is that a
complete LOG can carry no throughline at all, every event recorded with the
reasoning stripped out, which is exactly the failure this fights.

What it buys: Claude's memory resets each session, and the throughline is why a
fresh, short session still builds the project the way the user meant instead of
re-deriving intent from the code and guessing wrong.

**Rationale provenance is asymmetric and default-AI**, exactly like the work-item
credit: reasoning is assumed to be Claude's unless explicitly credited as the
user's stated intention, marked inline where the rationale lives ("the user's
reason for this: …"). Never add an AI-authorship marker. A prose convention, not
a lint-checked field. The credit-requires-their-words bar (Captures, provenance)
applies here in full: if Claude produced the reasoning, write it as Claude's,
and where both contributed, name who did which part.

What counts as rationale is broader than the decision's reasoning: it includes a
concern raised and resolved, and an alternative seriously weighed, each carried
with **why it lost**. The intuitive-but-rejected alternative most needs
preserving — without the why-it-lost recorded, a later session re-proposes it and
relitigates a settled decision.

```
qualifies:      a concern raised and addressed; an alternative seriously weighed
                a decision whose rejected path is the INTUITIVE one — always
doesn't:        a passing mention
```

Three collapse-shapes look reasonable and lose meaning silently. Named, because
the same mistake gets remade when they aren't:

```
don't shrink rationale to a one-line summary   # leaves a label, not the chain
don't move it into a dedicated why-field       # breaks the inline carry, and
                                               # trains authors to write empty fields
don't sort it into a typed taxonomy            # never complete; forces nuance
   ("UX reason / functionality reason")        # into the nearest slot
```

**Retrieve.** When asked why something exists, search `LOG/index.md` first — its
one-line-per-entry shape points to candidates faster than scanning prose. Then
open the matched entry's file directly (the index line ends with its filename).
Pre-split entries live in `LOG/log.md` and `LOG/log-v*.md` — find those by the
index line's hash or title. Only fall back to inferring from code if the index
and logs have nothing.

## Index entries

`LOG/index.md` is **Claude-facing, not user-facing.** It exists so a retrieve can
decide which entry to open without reading every entry's prose. Terseness for
human scannability is not the criterion — **specificity for that open/skip
decision** is.

```
each entry must carry:
    the artifact touched      # which file, doc, section, rule, or area
    the nature of the change  # added/removed/renamed/reframed/tightened, with
                              # enough substance to decide open-or-skip
    the entry's filename      # at the end of the line
```

**No length cap of any kind — not absolute, not proportional.** Length follows
from the content requirement above. The bound is the requirement itself: an
index line must carry enough to support the open/skip decision, and must not
restate the entry. An entry too short to support that decision fails even at one
line; a line that reproduces its entry fails at any length.

**A 20% proportional cap stood here until 2026-08-12 and was repealed on
measurement, which is recorded so it is not restored.** It was derived from
three entries of 968, 1,055 and 1,738 words — all long. Measured across the
whole index, it turned out to be monotonic in *entry* length rather than in line
length: not one of the fifteen entries over 1,000 words breached it, while two
thirds of the entries under 200 words did, the worst being a 34-word line
against an 87-word entry. So it never fired on the thing it was aimed at, and
fired 117 times on work nobody thinks is wrong. The distribution is in
[`resources/research/index-line-length-distribution.md`](../../../resources/research/index-line-length-distribution.md).

**No replacement number, and the reason it is a judgment test rather than a
script.** Scoping a cap to entries above some length reintroduces a bare figure,
and absolute length discriminates nothing — the longest lines in the corpus all
point at the longest entries and all read correctly. A mechanical check that
fires against correct work is worse than none, because it is learned past and
then ignored everywhere.

This doubles as a **readiness check** at /plan: if the candidate index entry
can't be written yet because the work isn't specific enough, it isn't ready for
Processed — keep discussing.

## Scope

**Build scope is the active work's described work** — the changes the work items
call for, and nothing past them. That's the definition, enforced by judgment. Its
mechanical approximation, and how /next derives it, is in next.md.

## Routing and discipline

- **Route to artifacts, not memory.** If it belongs in SPEC.md, QUEUE.md or LOG/,
  write it there.
- **Memory boundaries.** The project's records belong in the project's docs:
  ideas and discoveries → Unprocessed; design decisions → QUEUE/SPEC; project
  state → the method docs. Memory doesn't travel with the project and the user
  can't read it. Memory stays right for what no project doc owns: user
  preferences, working style, communication feedback, cross-project facts.
- **Doc routing — four destinations, two confused lines:**

```
SPEC.md      what the project is (what/who/how/why it exists)
QUEUE.md     what to work on next
LOG/         what happened
CLAUDE.md    how Claude should work on THIS project

SPEC vs CLAUDE.md   =  "what it is" vs "how to work on it"
CLAUDE.md vs memory =  "this project" vs "all projects"
```

  Run this as an active self-check on your *own* routing, not just a flag on the
  user's. The two misroutes to catch: writing product truth into CLAUDE.md when
  it belongs in SPEC, and putting into memory what belongs in CLAUDE.md. When the
  user frames something as a behaviour change ("make Claude always do X") that's
  really product truth ("the app does X"), name it as SPEC content and route it
  there.
- **/plan is for planning, /next is for building. Don't cross them.**
- **Executable work lives in the queue as work items — never in a standalone plan
  doc.** /next runs the queue and only the queue; a side doc of steps is
  invisible to /next and silently falls through. A task mixing Claude-work and
  user moments **decomposes into queue items**: build items for Claude's parts,
  `[user]` lines for the user's.

```
a plan of work to be DONE       ->  queue items
a record or finding to be READ  ->  a LOG entry, or a resources/ file
```

- **No planning work in any execution skill.** The boundary is **filing vs
  processing**: filing a capture is open to every session; processing one —
  moving it into Processed, deciding its fate — is /plan's. Two consequences:
  /done's wind-down re-scan is filing, so it's allowed at an execution close;
  and when the user runs a test and judges its outcome, that judging is the test
  work itself, not planning.
- **Mid-session discovery — decide by one rule: is it needed to complete the work
  being built?**

```
needed and minor        ->  ask to add it
needed and significant  ->  propose splitting
NOT needed              ->  capture and continue    # the common case
premise is broken       ->  halt and course-correct
```

  "Capture and continue" means: write it to Unprocessed, report what was filed,
  then confirm-and-resume — a discovery is Claude-raised, so don't close with
  "anything else?". Don't hold it in conversation to deal with later; an
  unrouted discovery survives only in memory.

  **User-only discoveries file as a `[user]` work item, not a plain capture.**
  This also fires **at processing time**: when /plan keeps an item and spots a
  user-only gating action *buried in its rationale prose*, split it out into its
  own `[user]` line with its own slug and reference it by slug from the original.
- **A new build or design directive arising during a close routes out.** /done
  records and commits finished work; it isn't a build session. A redesign, a new
  feature, a change to something that already worked → a fresh /next, or
  Unprocessed. **One exception:** a fix completing the just-built work's own
  verification — a genuine bug in what this build was meant to deliver — folds
  in, because it finishes the build rather than adding scope.
- **Nothing unrouted survives a session.** File or drop before close.
- **One build at a time.** Never start a second while this session's build
  working file exists.
- **Parallel sessions are allowed** — a planning session in one chat and a build
  in another. "One build at a time" forbids a second concurrent *build*;
  "don't cross plan and next" forbids mixing modes *inside one session*. Don't
  refuse a planning chat opened alongside an active build.

  **Which precaution applies depends on the isolation model, and session_start
  says which is in force** — it compares git's `--git-dir` against
  `--git-common-dir`, which differ in a linked worktree and match in a main
  checkout. Don't infer it from a missing directory and don't ask the user.

```
shared tree  ->  two appends to different parts of QUEUE.md don't collide, and
                 the file-modified warning catches it if they do. Avoid two
                 sessions writing QUEUE.md or committing at the same instant.
worktree     ->  sessions cannot collide at all — but a capture filed in one
                 never reaches the other, and the last branch to merge wins.
                 Keep queue edits in one session until a merge lands.
```

  **Under both models: don't interrupt a run to file a capture.** Same advice,
  opposite reasons. On a shared tree no coordination is needed, and the one
  moment worth avoiding is /next's close, which rewrites Processed and moves the
  marker. Under isolation, pausing achieves nothing at all — the capture lands
  in the other session's own copy and cannot reach the running build.

  **What happens to an isolated session's work at close, which is the case that
  loses work.** The harness makes the worktree and its branch and **never merges
  either back**; at exit it asks keep-or-remove, and remove deletes the worktree
  and the branch with everything in them. So an isolated close commits, then says
  which branch the work is on, that it is not merged, and that "remove" would
  delete it. The merge itself cannot happen there — git refuses to update a branch
  checked out in another working tree — so it is offered at a **main-checkout**
  session's start, where session_start reports worktrees carrying unmerged
  commits. Offer, never merge silently; on a conflict leave the branch alone and
  say the work is safe on it.
- **An empty Processed section is normal** — the vetted work is done.

## Consumer feedback channel and cross-project INBOX

A problem with the *method itself* or with *Claude Code itself* is not work on
the user's app; route it by the discriminator, then **read
`${CLAUDE_PLUGIN_ROOT}/docs-b/feedback-and-inbox.md`** for the full procedure
(report format, posting flows, the Claude Code branch's guards, INBOX
mechanics). Fetched on demand — the trigger is a user reporting a problem, or
mail waiting at session start.

```
the discriminator:  which thing is misbehaving?
    my app       ->  an ordinary capture in my QUEUE
    the method   ->  flintcraft.tech/report
    Claude Code  ->  a GitHub issue on anthropics/claude-code
    unsure       ->  ask the user; don't guess between the three
```

**Nothing is ever sent or posted without the user seeing the exact text and
giving an explicit yes** — feedback reports, GitHub issues, and outbound INBOX
messages alike. Inbound INBOX mail is surfaced by session_start and routed
through the three-way triage, then archived.

**When an inbound message changes work here, draft the reply unprompted in the
same session** — never auto-sent, and never left for the user to ask for. The
send stays under the rule above; what this adds is the offer. Confirmed by
recurrence: it shipped once, was lost to a revert, and the user has since had to
ask twice, in near-identical words, whether Claude had anything to send back.

## Dependency ownership

- **Claude owns sequencing** — the order work sits in, and what gets built first.
  Don't defer to the user. Ordering is a judgment call you make and narrate, not
  a question you ask.

  **But most of the queue's order carries no weight, so don't spend turns on
  it.** Everything above the readiness line is built by one /next run, so its
  internal order rarely changes anything; Unprocessed is ordered by the ladder
  at /plan's opening, at the moment the order is used. Don't ask which of two
  cleared items should go first — the answer changes nothing. Reorder when
  something is genuinely wrong, and otherwise leave the file recording when
  things landed.
- **Stable slugs.** Kebab-case, assigned at filing, written at the end of the
  description line. Immutable — reorders and renames don't change them, so a slug
  reference stays grep-able. Cross-references exist only if written as a slug in
  prose; **queue position never encodes a relationship**.
- **Narrate the ordering work.** Any time you exercise ordering judgment — a
  non-default placement, a reorder, an explicit "appending here because nothing
  relates to it" — say why in one short sentence. Silent ownership reads as no
  ownership.
- **The user owns whether an item is kept or deleted**, and whether a build
  expands its scope.

## Reading a whole file before reasoning over it

**Page the whole queue before any queue-wide reasoning, and the same for any
file whose *whole* content the reasoning depends on.** A read that stopped short
is named plainly, never reasoned from quietly. The failure is silent by
construction: a truncated read looks like a complete one to whatever reasons over
it, so nothing downstream can detect it — which is why the check belongs at the
read, not later.

A digest generated from the whole file by code satisfies this more strongly than
paging does, because code cannot silently truncate. Where a skill provides one,
use it.

**A mechanically generated digest covering the whole file satisfies this rule.**
Code that reads the file end to end and prints a fixed set of fields cannot be
silently truncated, so it gives the guarantee paging is trying to give — and
gives it more strongly. What it does not license is a partial read dressed up as
a summary: the digest must be generated from the whole file, by a script, not
assembled by whoever is reading.

## Check our own conformance before blaming the tool

When something appears to misbehave — Claude Code, a hook, the method itself —
read what the tool documents, then look for others reporting it, and only then
suspect the tool. The evidence: one session spent building two detailed theories
about a tool misbehaving when the cause was our own code not matching the
documented contract, findable in about a minute.

## File safety

```
never  git add -A  /  git add .        ->  stage explicitly
never  git push without asking          ->  and never --force
never  git reset --hard
always check for secrets before committing
```

**Undoing a lot of work at once → read `${CLAUDE_PLUGIN_ROOT}/docs-b/recovery.md`
first.** Trigger: the user asks to roll the project back to an earlier state, or
a session opens into the aftermath of one. Reference, fetched on demand.

**A clean `git status` means no UNCOMMITTED change — never that no change was
made.** Before reporting that an edit doesn't exist, check recent commits. The
two look identical from a clean tree, and the difference matters most exactly
when the user is asking "did my change land?" — answered wrongly, they redo work
that already exists.

**Uncommitted changes you didn't make are the user's own work, not breakage.**
Read them as expected handmade work; confirm with the user and fold them in.
Never report them as damage, and never try to undo or reset them.

## Prior decisions

- Before raising a design question, run the throughline retrieve. If **the
  record** shows it's decided, state the prior decision. If the user revisits,
  flag when it was decided.

```
the record, in cheapest-first order:
    decisions recorded earlier in THIS session   # no retrieve needed — you were there
    the item's own rationale in QUEUE.md         # where most decisions live until a close
    SPEC.md
    LOG/index.md, then the one matched entry
```

  **The source is the record, not LOG alone.** Most decisions sit in QUEUE prose
  until a close, so a rule naming only LOG points at the wrong place for the
  common case — and it misses the case where no retrieve is needed at all,
  because the decision was made in this session and you were present for it. A
  question whose answer already follows from a decision made this session is not
  a new question, however differently it is framed; the test is against the
  decision's *reason*, not its wording, since a reframe that resolves to the
  same thing looks different on the surface.
- **When the user proposes a change that would alter or reverse something the
  record already holds** — an existing rule, a shipped feature, a queued or
  logged decision — run the retrieve *before agreeing*: read LOG/index.md, open at
  most the one matched entry, and cite the prior decision rather than agreeing or
  pushing back generically. Trigger stays narrow to bound cost: fire only when
  the proposal touches something already in the record, never on new-work
  suggestions.
