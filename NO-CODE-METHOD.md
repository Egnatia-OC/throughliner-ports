# No-Code Method for Claude Code

I build in Claude Code using this workflow. The method requires Claude Code — its mechanisms (read-only enforcement, build orchestration, planning routing) depend on Claude Code primitives (hooks, skills, subagents) and don't run elsewhere.

## At a glance

Each phase loads different files and runs a different sequence. Orientation only; detail in *The build sequence*.

- **Session start.** Read `CLAUDE.md`, then the docs it points at. Route on my opening message: test notes or feature request → planning; "new project," non-conforming docs, or unadopted-folder safety-net advisory → `/adopt`.
- **Planning.** Edit `BACKLOG.md` directly; read `DOC-STRUCTURE.md` when editing source-of-truth docs. Sort changes into Suggestions and Discoveries. Run drift checks. Fold resolved planning batches into `UX.md` (or the relevant source-of-truth doc).
- **Before build.** Reorganise build batches in `BACKLOG.md`. Lock the next batch with file-level detail. Get my OK before switching out of plan mode.
- **After build.** Update `MANIFEST.md`. Provide a build recap. Prompt me to test and `/clear`.

## Meta-markup layers

Three layers of markup, each with a different job:

- **Phase headings** (`At session start`, `During planning`, etc.) organise content by phase.
- **Response-shape tags** (`[SILENT]`, `[BRIEF]`, `[SEQUENCE]`, `[DISCUSS]`, `[PROMPT]`) set verbosity contracts at the rule level.
- **Mode tags** (`Mode: planning, migration`, etc.) declare which phases load which sections. Untagged sections are always-on. Within `The build sequence`, the phase heading acts as the mode tag (no explicit tag added).

## Vocabulary

Method-specific terms used throughout this doc and `DOC-STRUCTURE.md`. Cross-references elsewhere point here rather than redefining inline.

- **Planning batch.** Open questions in `BACKLOG.md` that must resolve before a build batch can run, or that decide whether a build batch should exist (a *scope-existence* question). Resolved by folding answers into the relevant source-of-truth doc.
- **Build batch.** Engineering changes in `BACKLOG.md`, small enough to build and test in one session. Each ends with a `Serves` line naming the source-of-truth doc entries it implements.
- **Files: sub-section.** The list of files a build batch will modify, written as a sub-section of the batch in `BACKLOG.md`. Each entry is a GitHub-style task list bullet (`- [ ]` → `- [x]` when done) with `<path>` and a one-sentence change summary. Written by the before-build subagent during *Before build*; ticked file-by-file by the batch-executor during the build. The PreToolUse hook reads this list at edit-time to enforce batch boundaries — files not on the list are blocked. Full rules: `DOC-STRUCTURE.md` → *Files: sub-section*.
- **Batch-sizing principle.** A batch's right size is set by verification burden (count of distinct user-observable behaviours to test after the build), not by lines or files. Three sub-rules: split when a small batch produces a long test list; bundle unrelated items that introduce no new user-facing behaviour and don't interact; never fragment arbitrarily. Applied during *Before build*; full definition there.
- **Pre-build verification estimate.** The brief list of distinct user-observable behaviours that will need testing after a build batch lands, stated during *Before build*. Used to apply *Batch-sizing principle*: if the list is long relative to scope, the batch gets split. If the estimate proves wrong mid-build, the re-batching carve-out under *Prohibited of Claude → Two exceptions* applies.
- **Suggestion.** During planning: a fix or improvement that fits current scope (an existing `UX.md` or source-of-truth entry already covers it). May come from me or you. Routed into a build batch.
- **Discovery.** During planning: a bug or improvement outside current scope — no `UX.md` entry covers it. Cannot enter a build batch directly. Promoted to a planning batch asking "should this be added to `UX.md`?"
- **Red flag.** A security, privacy, data integrity, or safety concern. Surface in chat first; if I defer with no active plan, add to the Red flags section of `BACKLOG.md` in canonical format: `**`[RED FLAG]`**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Red flags are the only deferred items that don't need a `UX.md` entry behind them.
- **Source-of-truth doc.** A doc describing decided behaviour the build must conform to. `UX.md` is one in every project. Projects may add others (see *Additional source-of-truth doc*). Read-only to Claude; edited by the user during planning sessions (full rule in *Editing surfaces*).
- **Additional source-of-truth doc.** A project-specific source-of-truth doc beyond `UX.md` — e.g. `SYSTEM-PROMPT.md` for a Claude/MCP integration project, or `COPY.md` for a project whose user-facing text is the deliverable. Same locking rules as `UX.md`. Full rules: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.
- **Adopted folder.** A folder where the no-code method is active — the project's `CLAUDE.md` carries the method footer (`*No-code method — Version N.*`). The footer is written by `/adopt` during its scaffold or migrate paths. The safety net (SessionStart advisory + PreToolUse enforcement) stays silent on adopted folders.
- **Unadopted folder.** A folder where the method is not active — no method footer in `CLAUDE.md`. The safety net fires on unadopted folders **with substantial existing content** (per the *Detect unadopted folder* rule in *At session start*): SessionStart emits an advisory pointing at `/adopt`; PreToolUse blocks `Edit` / `Write` / `MultiEdit` and `Task` → method-subagent calls until the folder becomes adopted or the user writes a `.no-code-method-skip` opt-out marker at root. Genuinely-empty unadopted folders and opted-out folders stay silent.
- **Serves line.** The line at the end of a build batch in `BACKLOG.md` naming the source-of-truth doc entries the batch implements. Format: `Serves UX.md: [entry name(s)].` (and/or `Serves <DOC>: ...` for additional docs).
- **Drift check.** Four checks Claude runs at the start of every planning session: `UX.md` ↔ what's built, `MANIFEST.md` ↔ the codebase, `MANIFEST.md` ↔ `UX.md` (loose), and `TEST-LOG.md` ↔ what's been touched since each row was recorded (Rule 5 — retest after change). First three are pairwise; the fourth is a code-touch check per row.
- **Fold-in.** Moving proposed source-of-truth content from `BACKLOG.md` into the destination doc (usually `UX.md`). Claude queues content as `[FOLD-IN PENDING]` blocks in the *Fold-ins pending* section of `BACKLOG.md` because source-of-truth docs are read-only; the user does the actual fold-in by hand during a planning session. Origins: planning-batch resolution, `/adopt case 1` (new-project prompts), `/adopt case 3` (migration), or a mid-build edit attempt intercepted by the PreToolUse hook. Once folded in, the block is removed; if a planning batch produced the fold-in, the user also removes that batch in the same session.
- **Halt-and-confirm protocol.** Pattern subagents use when they hit a condition the user must decide on: surface in chat, propose the action (or list options), wait for response before proceeding. Used by before-build (validation failure, vague change list, verification burden triggers a split) and batch-executor (prerequisite and re-batching carve-outs).
- **Build recap.** Plain-English summary Claude provides at the end of every build (per *After every build*). Not persisted — lives in chat. Used by me to decide whether to test, push back, or accept.
- **Test session.** The state `TEST-LOG.md` enters after a build ships. *Opened* during *After every build* by writing one row per user-observable behaviour the recap names, with blank `Status` and `Confirmed Explicitly: No`. *Closed* during the next planning session's first sub-step (Rule 2) by per-row read-back: the user names each pending row and gives its outcome (Pass / Fail / Skipped). An unclosed test session blocks the next build batch (Rule 3).
- **Pass.** A `TEST-LOG.md` row `Status` meaning: the user ran the test and the behaviour matched. Pass with `Confirmed Explicitly: Yes` is the only outcome that closes a row positively.
- **Fail.** Row `Status` meaning: the user ran the test and the behaviour did not match. Requires a `User Notes` line describing what actually happened, so the regression has context in future sessions.
- **Skipped.** Row `Status` meaning: the user did not run the test this round, by explicit choice. Requires a reason in `User Notes` (a Skipped without a reason is a Fail or a blank). Skipped satisfies Rule 3's gate only as an "accounted for" outcome, not a passing one. The row stays in TEST-LOG and may be retested in a future session (typically promoted via Rule 5's drift check).
- **Test-confirmation gate.** Structural enforcement that a new build batch cannot start while any row in `TEST-LOG.md` from the previous batch has `Confirmed Explicitly: No`. Hook side (load-bearing): PreToolUse on Task targeting batch-executor reads TEST-LOG and refuses invocation if unconfirmed rows exist from the previous batch's session — falling back to "any unconfirmed row blocks" if the project doesn't keep `BUILD-LOG.md` for session identification. Subagent side (UX): the planning subagent's first sub-step walks the user through per-row read-back. Defined by Rule 3 (*Prohibited*), made trustworthy by Rule 1 (*Required*), made retestable over time by Rule 5 (fourth drift check).

## Method contract

The items below read like personal preferences but the machinery depends on them. If you adapt the phrasing to your voice, do not delete the substance. Each names which part of the method would break without it.

### Required of Claude

- I'd rather be told I'm wrong than agreed with. Check whether my assumptions hold before building on them. Flag concerns plainly; don't soften unnecessarily.
  *Load-bearing for: drift checks and red-flag surfacing — both require pushback rather than agreement.*

- Explain what you're doing in plain English so I can understand as a non-coder.
  *Load-bearing for: the build recap — assumes plain-English output; without that I can't verify the build.*

- If a build fails or causes a regression, don't apologize or "stealth-fix" it next turn. State plainly: "The previous change broke [Feature X], I am now reverting/fixing it."
  *Load-bearing for: the build recap — assumes regressions are stated plainly, not silently fixed.*

- If something seems improvable outside the current request's scope, flag it rather than silently fixing. (See *Where each kind of flag goes*.)
  *Load-bearing for: the Suggestions / Discoveries flag taxonomy — relies on flagging out-of-scope rather than fixing.*

- **Red flags — screen and surface.** Whenever you notice a security, privacy, data integrity, or safety concern — in the code, in a proposed change, or in something I've described — surface it explicitly. Three outcomes: address now → slot into a build batch; concern attaches to a feature being planned → fold into that planning batch as a question; defer with no active plan → add to the Red flags section of `BACKLOG.md` in canonical format (see *Vocabulary → Red flag*). Remove when addressed. Do not silently let a flagged concern slip past.
  *Load-bearing for: the Red flags section and flag taxonomy — both assume proactive surfacing.*

- Before working on a feature, check `MANIFEST.md` and `UX.md` first. It may already exist or be specified, and the `UX.md` entry tells you the user concern it serves. Look in the code only if those don't settle it.
  *Load-bearing for: the "How a new feature enters the project" pipeline (known features aren't treated as new) and every change touching an existing feature (the user concern stays in view).*

- If a request is ambiguous, ask rather than guess.
  *Load-bearing for: planning and pre-build discussions — they exist to surface and resolve ambiguity; a guess bypasses them.*

- If I push back on a suggestion, don't immediately fold and don't immediately dig in. Ask for my reasoning if not given, weigh it against your original case and any new information, then either restate your view or change your mind.
  *Load-bearing for: planning recaps — assume engagement with disagreement, not collapse into either position.*

- For multi-step procedures where my next action depends on you finishing the previous one — smoke tests, debug sequences, procedures I have to execute, questions where each answer informs the next — deliver one step per message. Open by stating the count ("Three steps coming. First: …") and then stop. Don't preview steps 2 and 3, even briefly — previewing is bundling. The inverse for alternatives I'm choosing between: comparisons need everything visible at once. Default for alternatives is a recommended option with a one-line "want me to walk the others?" escape, or a short comparison table.
  *Load-bearing for: formally `[SEQUENCE]`-tagged routes (`/adopt` cases 1 and 3) where each prompt's answer informs the next; ad-hoc walkthroughs (debugging, recovery, command-line sequences); and the planning flow's discuss-and-suggest step, which presents alternatives in full-comparison shape.*

- **Never infer completion.** A `TEST-LOG.md` row's `Status` is never inferred from absence-of-information. If the user has not explicitly named this specific row in a planning-session read-back, the row's `Confirmed Explicitly` stays `No` regardless of how strongly context implies "looks fine." Bulk confirmations ("all others good," "looks like everything's working," "the rest are fine") don't count for any specific row.
  *Load-bearing for: the test-confirmation gate (Rule 3) and `TEST-LOG.md`'s integrity. Without this, a single "yeah it's fine" silently confirms a dozen rows and the gate becomes a paper tiger. Mechanical correlate: Rule 2 names what to do instead — per-row read-back.*

### Prohibited of Claude

- Do not add features not listed in the current batch prompt. If you notice one that ought to be added, flag in chat at the end of your response — not in the build (see *Where each kind of flag goes*).
  *Load-bearing for: build-batch boundaries — *Before build* assumes batch scope is fixed once agreed.*

- Do not refactor, rename, or restructure anything not in the agreed plan. Not "while you're in there" mid-build. If I ask for new scope mid-build, decline politely, remind me we're in build mode, finish the current batch, then route through planning (Suggestion if it fits current `UX.md` scope, Discovery if not). **Two exceptions.** (1) **Prerequisite carve-out** — if the batch genuinely cannot complete or be tested cleanly without an unplanned change (a prerequisite only visible at implementation time), halt, surface with a one-line justification, wait for my okay; label `[Prerequisite, not in plan]` in the recap. (2) **Re-batching carve-out** — if implementation reveals verification burden is much higher than estimated (per *Pre-build verification estimate*), halt, surface with a one-line justification, propose a split, wait for my okay; label the split `[Re-batch, not in plan]` in the recap.
  *Load-bearing for: build-batch boundaries — protects the agreed batch from creep and routes new scope through planning; carve-outs keep the batch unblockable when implementation reveals a dependency, and keep the verification signal clean when burden exceeds the estimate.*

- Do not describe a `BACKLOG.md` edit as something for me to apply. Make the edit, then tell me what changed.
  *Load-bearing for: `BACKLOG.md` maintenance — Claude edits, user reviews, never the inverse.*

- **Do not invoke the batch-executor subagent — or any equivalent action that would start a new build batch — while any row in `TEST-LOG.md` from the previous batch has `Confirmed Explicitly: No`.** The hook gate (PreToolUse on Task with `subagent_type=no-code-method:batch-executor`) is the structural enforcement, but the rule lives here at the prompt level too so it bites in environments without the hook (the prose-only rewrite per `OPEN-QUESTIONS.md` relies on the prompt-level rule alone). After-build's recap *opens* the test session (blank-Status rows per *After every build*); the planning subagent's first sub-step *closes* it (per-row read-back). The hook fires between those two phases. **Hook fallback:** if the project doesn't keep `BUILD-LOG.md` and the hook can't identify the previous batch's session, fall back to "any row with `Confirmed Explicitly: No` blocks" — strict but safe.
  *Load-bearing for: the test-confirmation gate that makes `TEST-LOG.md` a record of decided outcomes rather than half-tested intentions. Without this, a new batch ships on top of unconfirmed tests and the record becomes meaningless.*

### Where each kind of flag goes

Three flagging mechanisms with different homes:

| Concern | When raised | Where it goes |
|---|---|---|
| Security, privacy, data integrity, safety | Any time | `BACKLOG.md` Red flags section (if deferred with no active plan). Surface in chat first either way. If attached to a feature being planned, becomes a question inside the planning batch. |
| Improvement outside the current request's scope | During a build | End of response, in chat. If I want it actioned, becomes a Discovery in the next planning recap. |
| User-facing behaviour changed in a way `UX.md` should reflect | During a build | End of response, in chat, suggesting a `UX.md` change. Don't edit `UX.md` mid-build. Discussed in the next planning session. |

If a single observation matches more than one row (e.g. a proposed feature with privacy implications), apply both rules — red-flag treatment never gets skipped just because the concern is captured elsewhere.

## Recommended habits

Starting points; adapt to fit how you actually work.

### Generally

- I will consider all your points put forward.

### During planning

- I will share test results from the last build, plus any further notes on changes I think are needed.

### Before building

- I review all upcoming changes in the next build, including the edits you have already made to `BACKLOG.md`.

### After building

- I will `/clear`.
- I will run all tests given in the last build, noting any other items at the end as possible future changes.
- I will prepare all test results and notes as pasteable text.

## The documents that describe my projects

Four files with different jobs. Read the one relevant to what you're doing.

- `UX.md` — user-facing description of the app: every feature and behaviour visible in the UI, plus why the user needs it. Read-only to Claude (full rule in *Editing surfaces*); user maintains it directly during planning sessions.
- `MANIFEST.md` — a flat, alphabetical glossary of every named element in the codebase I might want to look up (components, screens, services, files with a discrete purpose). One-line plain-English entries. You maintain it during builds. Lookup reference, not cover-to-cover reading — when I need to refresh on something, point me to UX.md, not MANIFEST.md.
- `TEST-LOG.md` — row-per-test record of every shipped build batch's outcomes (eight columns: # / Date / Session / Component / Test Description / Status / Confirmed Explicitly / User Notes). Maintained by Claude during builds (blank-`Status` rows added when a batch ships) and planning (rows confirmed via per-row read-back). See `DOC-STRUCTURE.md` → *TEST-LOG.md structure* for column shape and pruning.
- `BACKLOG.md` — deferred changes not yet built, organised as batches. Maintained by Claude (not me) during planning; see `DOC-STRUCTURE.md` → *BACKLOG.md structure*.

### Editing surfaces

Some docs are read-only to Claude and edited only by the user, by hand, during planning sessions. If you think one should be reworded or reorganised, flag in chat at the end of your response. Never edit them.

**Read-only to Claude:** `UX.md`, any additional source-of-truth doc, `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`.
**Read/write to Claude:** `BACKLOG.md`, `MANIFEST.md`, `TEST-LOG.md`, `CLAUDE.md`.

For `BACKLOG.md` (highest edit volume), the protective rule is the discussion contract built into the build sequence — every change must be discussed at the appropriate stage. The recap rules under *During planning*, *Before build*, and *After every build* make this explicit.

**The `[FOLD-IN PENDING]` mechanism.** Whenever Claude would otherwise write content into a read-only source-of-truth doc, it's instead queued as a `[FOLD-IN PENDING]` block in the *Fold-ins pending* section of `BACKLOG.md`. The user folds it into the destination doc (or drops it) by hand during their next planning session. `BACKLOG.md` and `MANIFEST.md` edits stay direct.

The mechanism is the same regardless of origin:

- **Planning-batch resolution.** When a planning batch is resolved during a planning session, Claude appends the resolved answer to the planning batch in place, and also adds a corresponding `[FOLD-IN PENDING]` block to *Fold-ins pending* naming this batch in its *origin* field. The user folds the answer in and removes the planning batch in the same session.
- **`/adopt` case 1, `/adopt` case 3, mid-build PreToolUse intercept.** No preceding planning batch exists; the block goes straight into *Fold-ins pending* with the appropriate origin (`/adopt case 1`, `/adopt case 3`, or `mid-build edit attempt — <date>`).

Canonical block format and section placement: `DOC-STRUCTURE.md` → *BACKLOG.md structure → Fold-ins pending*.

### When to read or edit each document

**`UX.md` (and any additional source-of-truth doc).** Read-only. Read the relevant entry before any change, to understand the user concern it serves. If behaviour has changed in a way the doc should reflect, flag in chat at the end of your response. Do not edit.

**`BACKLOG.md`.** Read/write. Read at the start of every planning session so edits build on its current state, not memory of a previous one. Edit when planning batches are added or resolved, when build batches are reordered or split, when red flags are surfaced, and when completed batches are cleared. Every edit must be discussed in chat at the appropriate stage — never silently.

**`MANIFEST.md`.** Read/write. Look up entries on demand when you encounter a name you want context on. Read the full file at the start of every planning session for the drift checks. Update during *After every build* for anything created, renamed, or removed.

**`TEST-LOG.md`.** Read/write. Read at the start of every planning session to find rows with `Confirmed Explicitly: No` from the previous build batch (test-session-close read-back, Rule 2) and to run the fourth drift check (Rule 5). Write rows during *After every build* (one per user-observable behaviour the recap names) and during the planning-session read-back (updating `Status` and `Confirmed Explicitly`). Same discussion contract as `BACKLOG.md`.

**`NO-CODE-METHOD.md` and `DOC-STRUCTURE.md`.** Read-only. Method spec, shared verbatim across every project, updated in the method's own development project. Read `DOC-STRUCTURE.md` when migrating an existing project's docs onto this method, or when consulting structural rules for source-of-truth docs.

**`CLAUDE.md`.** Read/write. Read first at session start. Update its *Where the docs live* path block on path mismatch, with user confirmation per the rule under *At session start*.

## The build sequence

**Response shapes used below.** Each bullet is tagged with one or more of:

- **[SILENT]** — Perform the action with no narration. One sentence max if acknowledgment is unavoidable.
- **[BRIEF]** — Output in chat, capped at 1–3 sentences or a tight list.
- **[SEQUENCE]** — Deliver as a series of prompts, one at a time. Open by stating how many prompts are coming, then ask the first and wait. Don't bundle; don't preview steps 2 and 3 even briefly. Each intermediate prompt carries its own implicit "answer this next" — [PROMPT] fires only after the final question. The tag formally marks sections of this doc, but the rule applies to any inherently-sequential exchange whether tagged or not (per *Method contract → Required of Claude*).
- **[DISCUSS]** — Full reasoning expected. Ask, weigh options, push back.
- **[PROMPT]** — End the response by telling me what to do next, in clear plain English. Hard requirement; do not skip.

Labels stack — `[BRIEF, PROMPT]` means a short explanation then a user prompt. Tags compose freely when meanings don't conflict. Genuine tension (e.g. `[SILENT, PROMPT]` — no output vs end-with-prompt) is a doc bug — flag in chat rather than improvising.

### At session start

Every Claude Code chat is a new session by definition — these instructions apply at the top of each.

- **[SILENT]** Read CLAUDE.md before responding to anything else. From its *Where the docs live* section, resolve the paths for `UX.md`, `BACKLOG.md`, `MANIFEST.md`, and any additional source-of-truth docs. Read each from its declared path. Those docs hold the project state. (`NO-CODE-METHOD.md` is the doc you're reading now; always loaded. `DOC-STRUCTURE.md` is mode-tagged for planning and migration only — don't read it during build sessions.)
- **[BRIEF]** If a declared path doesn't resolve, search the project for a file with that name. If found at a different path, surface the mismatch — name the declared path, name the path you found, propose updating CLAUDE.md's *Where the docs live* section. If multiple files match, surface all candidates and ask which is correct. Wait for my confirmation before editing CLAUDE.md. If no file is found, treat the doc as genuinely missing.
- **[BRIEF]** If a doc is genuinely missing from the project, say so plainly. Same for any doc present but empty.
- **[BRIEF] Detect template state.** If the spine docs are present at their declared paths but still in template form (placeholder strings like `[Project Name]`, `[Feature name]` intact, no real entries in BACKLOG.md, MANIFEST.md empty), the project hasn't been kicked off yet. Recommend `/adopt` — case 4 (already method-managed) detects the template state and offers to walk you through case 1's four new-project prompts to seed `UX.md`, `BACKLOG.md`, and the first build batch. Wait for my okay.
- **[BRIEF] Detect unadopted folder.** If the SessionStart hook injected an advisory about the folder being unadopted — no method footer in `CLAUDE.md`, substantial existing content present, no `.no-code-method-skip` marker at root — surface it and recommend `/adopt` before any other work. PreToolUse is already blocking destructive calls (`Edit` / `Write` / `MultiEdit` and method-subagent `Task` invocations); don't attempt them. Full mechanism: *Safety net mechanism* below.

Then read my first prompt and route:

- Test notes → continue to "During planning."
- User wants to (re-)initialise project structure ("new project," "set this up," "let's start") → recommend `/adopt`. Wait for my okay.
- Existing project docs are non-conforming to `DOC-STRUCTURE.md` (e.g. UX.md has no "user needs this because..." lines, BACKLOG.md has no batches, MANIFEST.md isn't alphabetical) → recommend `/adopt`. Wait for my okay.
- Feature request, scope question, or structural change with no test notes → continue to "During planning" with that input as planning seed.
- Top batch in `BACKLOG.md` left unfinished from previous session and opener doesn't trigger another route → default to resume. Confirm before continuing the build.
- Otherwise (a question, status check, something conversational) → **[DISCUSS]** respond using loaded doc state as context. No need to scan the whole codebase yet. (`[DISCUSS]` doesn't override the ask-rather-than-guess rule — if discussion hits genuine ambiguity, ask.)

**Routing priority for mixed-input openers.** If the opening triggers more than one route, higher-priority wins and lower-priority items fold in as the route's sequence handles them. Priority: `/adopt` > resume > planning seed (test notes, feature requests, scope questions, structural changes all live here). Example: an opener with test notes *and* a brand-new feature idea routes to planning — the feature idea gets sorted into Suggestions or Discoveries during the sort, not handled separately. `/adopt`-triggering openers wait for adoption to resolve before any of the lower-priority routes run.

**Handoff to the planning subagent.** "Continue to *During planning*" means invoking the planning subagent (`no-code-method:planning`) via the Task tool. It runs in its own context window; you receive its recap and relay it. The invocation prompt must include a `primary_intent` line classifying the opener, followed by my full opening message. The four values:

- `test notes` — I pasted output from a previous build's tests.
- `feature request` — proposing a new feature or scope addition with no test notes attached.
- `scope question` — raising a scope-existence question (e.g. "should this app even have X?").
- `mixed (primary: <one of the above>)` — primary named per the routing-priority rule; the subagent catches secondary items during its own sort.

Trust the planning subagent's recap as the source of truth for the session's `BACKLOG.md` changes — don't re-do its work or second-guess. If I push back on something in the recap, relay it back to the planning subagent for resolution rather than answering yourself.

**Handoff to before-build.** When I invoke `/before-build` (or otherwise signal I'm ready to lock the next batch), invoke the before-build subagent (`no-code-method:before-build`) via the Task tool. It runs *Before build* in its own context; you relay its recap. The invocation prompt is short prose announcing the route — no structured payload required; the subagent reads BACKLOG.md and project state itself.

Trust the before-build subagent's recap. If a halt-and-confirm surfaces (no top batch, malformed `BACKLOG.md`, change list too vague, verification burden triggers a split), relay verbatim and wait for my response before re-spawning. Don't answer halt-and-confirm requests on the subagent's behalf.

**Handoff to batch-executor.** When I invoke `/build` (or when the Stop hook redirects after one completes), invoke the batch-executor (`no-code-method:batch-executor`) via the Task tool. The invocation prompt must include the JSON payload from `plugin/scripts/parse_backlog.py` for the current top unticked batch — see the `/build` slash-command body for the parser CLI. The subagent runs one batch in its own context, ticking each file as it completes, and ends with a brief completion note when the last file ticks. You relay it. The build recap is produced separately by the after-build subagent.

Trust the batch-executor's completion note. If a halt-and-confirm surfaces (prerequisite or re-batching carve-out), relay verbatim and wait. Don't answer halt-and-confirm requests on the subagent's behalf.

**Handoff to after-build.** When batch-executor's last file ticks, the Stop hook detects the transition (BACKLOG.mtime > TEST-LOG.mtime + a fully-ticked batch in BACKLOG.md) and emits a redirect routing you to the after-build subagent (`no-code-method:after-build`). Invoke via Task tool. The invocation prompt is short prose announcing the route — no structured payload required. The subagent runs *After every build* in its own context: silent MANIFEST.md update, plain-English recap with `[Requested]`/`[Suggested]` labels read off BACKLOG.md, test-session-open (blank-Status rows appended to TEST-LOG.md), and user prompts to refresh, test, and bring per-row outcomes to next planning. You relay the recap.

After-build is idempotent — if invoked when the test session is already open (rows already exist), it exits with a short "test session already open" note. This covers Stop-hook re-fires when the user continues a conversation after after-build's first run. Trust the recap; don't re-do or re-summarise.

- **[PROMPT]** Once the route's work is done, prompt me to continue to "During planning." (Skip if you took the test-notes route or planning-seed route — you're already there. `/adopt`'s case 1 and case 3 close with their own prompts; don't double up.)

#### Safety net mechanism

Two-hook architecture protecting user files in unadopted folders (per *Vocabulary*):

- **SessionStart hook** detects the unadopted condition and emits an advisory via `systemMessage` (user-visible warning) plus `additionalContext` (directive into Claude's context). Informational — SessionStart has no halt mechanism. Adopted folders, genuinely-empty folders, and folders carrying `.no-code-method-skip` stay silent.
- **PreToolUse hook** enforces. When the folder is unadopted (no method footer, substantial content, no opt-out marker) and main Claude attempts `Edit` / `Write` / `MultiEdit` or `Task` → method-subagent (planning / before-build / batch-executor / after-build), the call is denied with reason text directing the user to `/adopt`. The `/adopt` subagent's own tool calls pass through — the gate discriminates by invoker so case 1 scaffolding and case 3 migration aren't blocked.

**Detection thresholds** ("substantial existing content"): any of (a) a build-manifest file at root (`package.json` / `pyproject.toml` / `Cargo.toml` / `build.gradle[.kts]` / `Gemfile` / `pom.xml` / `go.mod` / `composer.json` / `requirements.txt` / `setup.py`); (b) a recognised source directory at root (`src/` / `lib/` / `app/`); (c) a foreign `CLAUDE.md` (no method footer); (d) more than 5 files at root, counting everything except `.git/` / `.gitignore` / `README.md` / `LICENSE[.md]` / `.obsidian/`. Canonical list lives in `plugin/hooks/session_start.py`. Conservative bias: false positives are minor friction (`/adopt`'s case 1 handles empty folders); false negatives are catastrophic.

**Self-clearing.** Once `/adopt`'s scaffold or migrate path writes a method-footered `CLAUDE.md`, the next hook fires return through cleanly. The opt-out marker (`.no-code-method-skip`) clears the gate without adopting — `/adopt`'s cancel and leave-alone options write it. Removing the marker by hand brings the safety net back; `/adopt` invoked against an opted-out folder (case 5) offers to clear it.

#### /adopt route

`/adopt` is the single entry point for getting a folder onto (or off of) the no-code method. It detects folder state and routes to one of five cases. Subagent body: `plugin/agents/adopt.md`. Slash-command entry: `plugin/skills/adopt/SKILL.md`. Cases 1 and 3 carry forward the substance of the pre-V29 new-project and migration routes.

**Case 1 — Empty folder.** **[SEQUENCE]** Folder has no method footer in `CLAUDE.md` AND no substantial existing content (per *Safety net mechanism → Detection thresholds*). `/adopt` scaffolds the spine templates (`CLAUDE.md`, `UX.md`, `BACKLOG.md`, `MANIFEST.md`, `TEST-LOG.md`) with method-version footers, then walks me through four prompts in order. Skip any I've substantively answered in my opening message — acknowledge and move on. For partially-answered prompts, acknowledge what was given and ask only the remainder, treating it as one prompt for the count.

1. **Project context.** What does this app do, and what makes it distinct from existing apps in the space? (Goes into UX.md "Project context" paragraph.)
2. **UX principles.** What 3–6 principles should guide every design decision? Ask one at a time if needed.
3. **Core functionalities — first pass.** What 3–5 features must the app have to be itself? For each, the user-experience description and the "user needs this because..." line.
4. **First build batch sketch.** Of the functionalities above, which is the smallest end-to-end thing we can build and test first?

After the sequence, write all four answers into *Fold-ins pending* as a single `[FOLD-IN PENDING]` block, origin `/adopt case 1` — the user folds UX content into `UX.md` (Project context, UX principles, Functionalities) by hand and converts the first-build sketch into a proper build batch with a `Serves UX.md:` line, in the same session. Leave `CLAUDE.md` alone beyond the scaffolded template — its path block and project-specific notes are user-maintained; path mismatches are handled at session start. Prompt me to review the block and do the fold-in.

**Case 2 — Existing code, no docs.** **[BRIEF, DISCUSS]** Folder has substantial existing content (per *Safety net mechanism → Detection thresholds*) but no `CLAUDE.md`. `/adopt` confirms a backup of the folder is in place (or offers to make one), then offers two options:

- **Scaffold fresh docs alongside the existing code.** Spine templates land with footers; templates start empty (not filled). When the user runs `/adopt` again in this folder, case 4 detects the template state and offers to walk them through case 1's prompt sequence.
- **Cancel.** Write `.no-code-method-skip` at root and leave the folder alone. The safety net stops firing immediately.

Reverse-engineering docs from existing code is out of scope for V29 case 2 — scheduled for a follow-up session.

**Case 3 — Existing code, foreign docs.** **[BRIEF, then SEQUENCE]** Folder has a `CLAUDE.md` but no method footer (e.g. the user ran Claude Code's built-in `/init`, or has hand-written docs from another methodology). `/adopt` confirms a backup is in place, then offers three options:

- **Migrate (recommended).** Walk through structural gaps and queue `[FOLD-IN PENDING]` blocks for the user to fold into the destination docs (sequence below).
- **Overwrite.** Replace the existing `CLAUDE.md` (and any other docs at canonical paths) with method templates. Requires explicit confirmation in the dialogue ("yes overwrite," or similar — single-keystroke confirmations don't count).
- **Leave alone.** Write `.no-code-method-skip` at root and exit.

The dialogue explicitly anticipates the `/init` case so users don't feel punished for trying a built-in command first.

If the user picks Migrate, run the sequence:

- **[BRIEF]** State which docs are present (three spine docs and any additional source-of-truth docs the project declares) and the path each was read from, and for each, the specific structural gaps you can see (missing sections, missing fields, wrong abstraction level). One line per gap. Don't start fixing yet.
- **[SEQUENCE]** Walk through the gaps in this order: UX.md first (source of truth the others depend on), then any additional source-of-truth docs (peers to UX.md as fold-in destinations), then BACKLOG.md, then MANIFEST.md. For each doc:
  1. Confirm which existing content stays as-is.
  2. Propose, in plain English, the smallest set of edits to bring it up to spec. For an additional source-of-truth doc, *spec* means the rules in `DOC-STRUCTURE.md` → *Additional source-of-truth docs* — there's no fixed shape, only structural rules.
  3. After my okay, make the edits. For `BACKLOG.md` and `MANIFEST.md` (read/write), edit directly. For `UX.md` and any additional source-of-truth doc (read-only), write the proposed edits as `[FOLD-IN PENDING]` blocks in *Fold-ins pending*, origin `/adopt case 3`. Don't describe edits for me to apply.
- After all docs are migrated (`UX.md` and additional-source-of-truth edits queued as `[FOLD-IN PENDING]` blocks; `BACKLOG.md` and `MANIFEST.md` edited directly), prompt me to do the fold-ins by hand, then continue to "During planning."

**Case 4 — Already method-managed.** **[DISCUSS]** Folder's `CLAUDE.md` carries a method footer. `/adopt` was invoked anyway. Offer me three options:

- **Walk me through the new-project prompts.** Offered when *Detect template state* matched (footer present, content unfilled). Re-uses case 1's four-prompt sequence to seed the docs without re-scaffolding templates that are already in place.
- **Refresh templates to current version.** Replaces canonical-path templates with current-version templates. The dialogue surfaces the version gap explicitly ("Your `CLAUDE.md` is on V25; templates are on V29 — want me to walk you through the structural changes?") rather than refreshing silently.
- **Did you mean to run this elsewhere?** Exit option for the common case of running `/adopt` in the wrong folder.

**Case 5 — Opted out.** **[DISCUSS]** Folder has a `.no-code-method-skip` marker at root. `/adopt` was invoked anyway. Two options:

- **Clear the marker.** Folder becomes unadopted again; the next prompt will trigger the safety-net advisory and the user can adopt or re-opt-out from there.
- **Cancel.** Folder stays opted out, nothing changes.

Read deliberately neutral — opting out is a legitimate state, not a stuck one.

### During planning

Planning sessions can start in different ways: pasted test notes, an open question, a new feature, or a fresh project needing first batches sketched out. Steps below are the same in spirit — skip what doesn't apply.

- **[BRIEF, SEQUENCE]** **Close the previous build's test session.** Per *Method contract → Required → Never infer completion* (Rule 1) and *Prohibited → Test-confirmation gate* (Rule 3). If `TEST-LOG.md` has any rows from the previous build batch with `Confirmed Explicitly: No`, walk them one row at a time before any other planning work. For each: read the `Test Description`, ask Pass / Fail / Skipped, record in `Status`, set `Confirmed Explicitly: Yes (<today>)`, move to the next. Don't bulk-ask ("how did the rest go?") — read-back is per-row by design. If the user gives a bulk answer, push back with the next pending row's `Test Description` and ask for that specific outcome. Phase cannot proceed until every previous-batch row is `Confirmed Explicitly: Yes`. If all previous rows are already `Yes` (or `TEST-LOG.md` is empty / first batch not shipped), the session is already closed — proceed.
- **[SILENT]** Remove from `BACKLOG.md` any build batches completed since the last planning session. (Dedupe's first move.)
- **[BRIEF]** Check for drift. Four checks (don't try to compare them all at once):
  1. **`UX.md` ↔ what's built.** Every `UX.md` entry has a working implementation; every user-facing behaviour in the build is described in `UX.md`. Flag mismatches.
  2. **`MANIFEST.md` ↔ the codebase.** Every `MANIFEST.md` entry exists in code; every named element worth tracking is in `MANIFEST.md`.
  3. **`MANIFEST.md` ↔ `UX.md` (loose only).** Every `MANIFEST.md` entry should plausibly serve some `UX.md` entry, with infrastructure as the obvious exception. They're not at the same abstraction level — flag entries that don't fit any user-facing purpose.
  4. **`TEST-LOG.md` ↔ what's been touched since each row was recorded (Rule 5 — retest after change).** For each row with `Status: Pass` and `Confirmed Explicitly: Yes`, judge whether the component the row covers has been substantially changed since its `Date`. "Substantially changed" = a code or config change that could plausibly affect the behaviour the test verified. Trivial changes (comments, formatting, unrelated refactors elsewhere in the file) don't count. Produce a brief reasoning trail per flagged row: "Row 014 (Component: TaskCard) — flagged because TaskCard.kt was edited in v27 and the change touched the touch-handling path Row 014 tested. Reasoning: <one or two lines>." Flagged rows get `Status` set to `Skipped` (append a new row with today's date, `Confirmed Explicitly: No`, `User Notes` naming the change), and the user is asked to retest in the current build cycle. Original row stays intact.

  Run on every planning session. Only skip case is "nothing has been built yet." Don't skip on "nothing has been built since last planning session": there's no reliable signal for that, and skipping would miss code changes made outside Claude Code's awareness.
- **[BRIEF]** If I shared test notes, review them. Sort into two piles before discussing:
  1. **Bugs and issues against existing `UX.md` entries** — candidates for the **Suggestions** list (current scope).
  2. **Brand-new feature ideas with no `UX.md` backing** — candidates for the **Discoveries** list (out of scope until `UX.md` is updated).
- **[DISCUSS]** Discuss changes. Always suggest better options if available, per *Method contract*.
- **[SILENT]** Dedupe and reclassify — every candidate change discussed this session (test notes, drift findings, anything I've raised) goes through this filter: already covered by an existing batch (skip), genuine new addition fitting `UX.md` (slot into a build batch), or out of scope (flag for Discoveries).
- **[BRIEF]** Provide a **Suggestions** list — fixes or improvements fitting current scope (`UX.md`), whether you spotted them or I asked. For each, explain the benefit in plain English, label `[Requested]` or `[Suggested]`, and ask whether it goes in the next build or in `BACKLOG.md`.
- **[BRIEF]** Provide a **Discoveries** list at the bottom — bugs or improvements outside current project scope (`UX.md`). Don't fix these. They need a `UX.md` update before entering the build pipeline.
- For every proposed change, label `[Requested]` (I asked) or `[Suggested]` (you proposed). When a change enters a build batch in `BACKLOG.md`, write the label inline as a prefix on the change-list bullet — `- [Requested] Fix drag-to-postpone overshoot on tablet` — so after-build can read it at recap time. Structural rules: `DOC-STRUCTURE.md` → *Build batches → Change list — `[Requested]`/`[Suggested]` labels*.
- **[SILENT]** Whenever a decision changes `BACKLOG.md` — adding, removing, reordering, splitting, reclassifying — edit it immediately. Don't describe the change as something for me to do. I review afterwards; I don't apply.
- **[SILENT]** When a planning batch's questions are resolved during this session, append the resolved answer in place, and add a corresponding `[FOLD-IN PENDING]` block to *Fold-ins pending* naming this batch in its *origin* field. Don't remove the planning batch — the user removes it in the same session in which they fold the answer into `UX.md` (or the relevant source-of-truth doc) by hand. (Detail: *Editing surfaces*.)
- **[SILENT]** Promote each Discovery I haven't explicitly dropped into a planning batch in `BACKLOG.md` before the session ends. The batch's question is "should this be added to `UX.md`?" — so no Discovery survives `/clear` unrecorded. If I want one dropped, I'll tell you.
- **[BRIEF]** When wrapping a planning session, your recap describes what you have **already changed** in `BACKLOG.md`. It does not list pending edits for me to apply. If a decision was deferred, say so explicitly and name the question.

#### How a new feature enters the project

A new feature idea cannot go straight into a build batch. Fixed pipeline:

1. The idea is raised — by me, you, a test note, or a Discovery from a previous session.

   If the idea conflicts with an existing UX principle, surface the conflict in chat as the first response — don't quietly route it into a planning batch and hope the principle survives. The planning batch still happens (step 2), and the conflict becomes one of its questions. Push-back-in-chat and the planning batch are layered, not alternatives — chat surfaces the tension immediately so the user can react; the batch records and resolves it.

2. It enters `BACKLOG.md` as a **planning batch** — new, or folded into an existing planning batch on a related topic — asking the questions needed to decide whether and how it joins `UX.md`.
3. We answer in a planning session. If decided, Claude appends the resolved answer to the batch and adds a corresponding `[FOLD-IN PENDING]` block to *Fold-ins pending* (per *Editing surfaces*).
4. Fold-in to `UX.md` happens by hand in the same planning session (or next, if deferred). The `UX.md` entry is added or updated, the `[FOLD-IN PENDING]` block is removed, and the planning batch is removed.
5. Only then does the engineering work enter `BACKLOG.md` as a **build batch** with a "Serves UX.md: ..." line pointing to that entry.

If you find yourself proposing a build batch for something with no matching `UX.md` entry, stop and check whether you've skipped a step.

When I phrase a request as immediate build ("let's add X"), frame the planning-first response as routing, not refusal: explain why the planning step exists, not just that it does.

### Before build

- **[SILENT]** Validate the top build batch. Confirm `BACKLOG.md` parses and the top batch's `Serves UX.md:` names resolve in `UX.md`'s Functionalities section (case-insensitive after whitespace-trim — same matching the PreToolUse hook enforces). Halt and surface if (a) no top build batch, (b) `BACKLOG.md` is structurally malformed, or (c) a `Serves UX.md:` name doesn't resolve. The third case means a planning fold-in step was skipped — route me back to planning rather than proposing the entry yourself.
- **[SILENT]** Enumerate the Files: list. For each bullet in the top batch's change list, identify the file(s) it requires modifying. Write the result as a `Files:` sub-section into `BACKLOG.md` per `DOC-STRUCTURE.md` → *Files: sub-section*. If a file needs a rewrite rather than a surgical edit, the per-file summary says so.
- **[BRIEF]** Show me the top batch for review — heading, change list, and the Files: list you just wrote. The top batch is the next build.
- **[BRIEF]** State the expected verification burden — a brief list of distinct user-observable behaviours that will need testing after the build.
- **[BRIEF]** Apply the *Batch-sizing principle*. If the verification list is long relative to scope, halt and propose a split. On my okay, edit `BACKLOG.md` to split: current batch keeps changes whose verification surface forms one coherent unit; the rest moves to a new batch (or batches) created immediately below in priority. New batches inherit the current batch's `Serves` line(s) unless the split crosses serve-line boundaries. Then re-run Files: enumeration on whichever batch is now top.
- **[SILENT]** Make any further edits to `BACKLOG.md` requested in batch review directly. Don't ask me to edit.
- **[BRIEF]** Flag any conflicts or concerns before proceeding.
- **[PROMPT]** Prompt me to run `/build` (or wait for the Stop hook to auto-continue) to start this batch. If I'm in plan mode for any reason, ask me to switch out first — `/build` invokes file edits that plan mode blocks.

#### Batch-sizing principle

A batch's right size is set by **how much you'll have to verify**, not how many lines or files it changes. Verification burden = count of distinct user-observable behaviours you'll need to test after the build to confirm it landed correctly. Three sub-rules:

- **Split when a small batch produces a long test list.** A change set that touches few files but ships behaviour across multiple unrelated surfaces carries a long test list. Long test lists in one batch make regression signals ambiguous — if something breaks, you don't know which change to suspect. Split into batches whose test lists each fit a single surface.

- **Bundle unrelated items when they introduce no new user-facing behaviour and don't interact.** Refactors with no semantic change, renames, comment cleanups, configuration normalisations — these have empty (or identical-trivial) test lists. Forcing each into its own batch fragments work without buying clarity. Bundle them.

- **Never fragment arbitrarily.** "Smaller is always safer" is not a rule of this method. A batch trimmed below its natural verification unit makes the next batch's job harder (it has to re-verify the same surface) and dilutes the test signal across more sessions.

The existing "small enough to build and test in one session" rule still applies; it now means **one session's worth of verification**, not one session's worth of keystrokes.

### After every build

- **[SILENT]** Update `MANIFEST.md`: add entries for anything created, update for anything renamed or changed, remove for anything deleted.
- **[BRIEF]** Provide a build recap. Plain English, no jargon ("I am adding a check to the age field so people can't enter negative numbers"). For every change, label `[Requested]` (I asked) or `[Suggested]` (you proposed). For any carve-out additions made during the build, also label `[Prerequisite, not in plan]` or `[Re-batch, not in plan]` per *Prohibited → Two exceptions*.
- **[BRIEF]** Surface end-of-recap flags per *Where each kind of flag goes*: out-of-scope improvements noticed but not acted on; user-facing changes the build implies `UX.md` should reflect; any Red flag concerns surfaced during the build (with the BACKLOG.md entry confirmed if I deferred it).
- **[SILENT]** **Open the test session.** Enumerate the user-observable behaviours the recap names as needing testing. For each, append a row to `TEST-LOG.md` with: today's `Date`, the build's `Session` (project's session tag if it keeps tags, today's `YYYY-MM-DD` otherwise), the `Component` (matching `MANIFEST.md` where possible, plain English if cross-component), a one-sentence `Test Description`, blank `Status`, `Confirmed Explicitly: No`, blank `User Notes`. These blank-Status rows define the test session that next planning's first sub-step will close. Per *Method contract → Prohibited → Test-confirmation gate*, the next build batch is gated on these rows being confirmed.
- **[PROMPT]** Prompt me to refresh my download of the project and begin testing — and to bring per-row test outcomes (Pass / Fail / Skipped) to the next planning session, where the planning subagent will walk the read-back row by row.
- **[PROMPT]** Prompt me to `/clear` and switch back to planning mode when testing is complete.


---
*No-code method — Version 32.*
