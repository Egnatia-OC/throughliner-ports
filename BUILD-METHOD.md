# BUILD-METHOD.md — How this project ships

This doc describes how the no-code-method development project itself works: how a session opens, what happens in the middle, how it closes, what testing means here, and where each kind of artefact lives. It's the working manual for *this* project — sibling of `BUILD-LOG.md` (the record of what shipped) and `planning/PLAN.md` (the roadmap of what's coming).

It is **not** the no-code method itself. The no-code method is what this project produces — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, and the templates and plugin components under `templates/` and `plugin/`. Those describe how consumers of the method run *their* projects. This doc describes how Alex and Claude run *this* one.

For style, voice, and personal preference rules, see the project root `CLAUDE.md`. That file used to carry most of what's now in this doc; it's been slimmed to focus on orientation, environment, and the personal-collaboration rules. Anything in this doc supersedes older equivalents in `CLAUDE.md`.

---

## The unit of work: a session

**One session = one git commit + one git tag.** A new session starts when Alex wants to mark a new boundary in the work. There is no other definition of a session — not "a Cowork chat," not "a calendar day," not "a continuous block of work." Tag boundaries define sessions.

Session tags are `v17`, `v18`, ... going forward. The current session tag is whatever `git describe --tags --abbrev=0` returns from inside `sovereign-implementer/`.

Versions before V17 live in `Archive/Version 3/` through `Archive/Version 16/` — read-only history kept for reference. Don't edit them.

### Session tag vs. method version — two different things

The session tag (`v17`, `v18`, ...) names the dev project's working state at the end of each session. It increments per session, regardless of what changed.

The **method version** is what consumers see — the `*No-code method — Version N.*` footer at the bottom of every method-side file. It increments only when the method or plugin **substantively changes** (a new mechanism, a renamed component, a shipped plugin feature, a structural rewrite). Dev-internal changes (BUILD-LOG entries, BUILD-METHOD edits, planning artefact rearrangements, TEST-LOG appends) don't change what consumers see, so they don't bump the method version.

This means the session tag and the method-version footer will diverge over time. Session `v25` might ship with method-version footers at `V23` because nothing method-side has substantively changed since V23 was tagged. That's working correctly, not a drift bug — the V21 footer-mismatch tripwire compares loaded footers against `PLUGIN_METHOD_VERSION` in `session_start.py`, both of which stay locked together until a method-changing session bumps them in tandem.

The two numbers are coupled only inside a session that substantively changes the method: that session bumps the method-version footer (and `PLUGIN_METHOD_VERSION` and `plugin.json`) to match its session number. Between such sessions, they drift.

**Historical note.** V18 through V23 conflated the two — every session bumped the method-version footer regardless of whether the method had changed. The convention going forward separates them; the historical mismatches stay in the record (no retroactive corrections).

---

## Session open

At the start of every session, in order:

1. **Run `git describe --tags --abbrev=0`** from `sovereign-implementer/` to confirm the current version.
2. **Read `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, and `Crash course.md`** at the current state — i.e. as they are at `HEAD`. This is the active method.
3. **Scan `planning/OPEN-QUESTIONS.md`** for entries whose *Next step* line mentions the current session by name (e.g. "fold into V24"). Those need attention this session.
4. **Read `planning/sessions/V<N>.md`** if one exists for the session being planned — it's the provisional scope, not a contract.

Then read Alex's opening message and route. The CLAUDE.md *Working with me* section governs interaction shape. If the task isn't clear from her opener, report what was loaded and ask. Don't draft.

---

## Session middle: planning, building, or both

Sessions land in one of three shapes, often blended:

**Implementation sessions** ship plugin code (hook scripts, subagent bodies, slash commands, skill scripts) or method-doc structural changes. They end with a smoke test (see *Testing — what we actually do* below) and the matching doc-parity edits in the same commit.

**Doc-only sessions** ship rewrites of the method spec docs without testable code — a terminology sweep (V23), a parity catch-up (V20), or an OPEN-QUESTIONS resolution that lands as prose. No smoke test needed; the doc-code parity audit still runs at close.

**Planning sessions** rescope the roadmap — split or merge upcoming sessions, write or revise `planning/sessions/Vxx.md` scope files, add or resolve OPEN-QUESTIONS entries, or restructure PLAN.md. A planning session might or might not produce a tagged commit; typically it does, because rescoping is itself a version-worthy change.

The work of the session is whatever Alex directs. Claude's job during the middle is to do the work, surface concerns, and propose. The session's own rules below (close, parity, testing) bind regardless of which shape the middle takes.

---

## Session close: 8 steps

Before committing and tagging:

1. **Verify doc-code parity.** Run the audit in *Doc-code parity* below. If this session's changes introduced anything the descriptive docs don't accurately describe, update the docs first, in this session. Footer bumps and BUILD-LOG entry come after the doc edits land, so they reflect the now-current state.

2. **Bump method-version footers** *only if* this session substantively changed the method or plugin. Dev-internal-only sessions (BUILD-METHOD edits, BUILD-LOG entries, TEST-LOG appends, planning artefact reshuffles) skip this step entirely. When a bump is warranted, update every method-side file and template `*No-code method — Version N.*` footer to match the new session number, plus `plugin.json` `version` and `PLUGIN_METHOD_VERSION` in `session_start.py`. See *Footer bumps: the full list* below for the file list.

3. **Add an entry to `BUILD-LOG.md`** for this session, using the entry shape in *BUILD-LOG entry shape* below. Newest first.

4. **Sweep ideas raised but not implemented.** Look back over the chat for anything that came up but wasn't acted on. For each: add to a future `planning/sessions/Vxx.md` if it belongs there; create a new `Vxx.md` + PLAN.md row if it's its own session; note in the BUILD-LOG entry as "not pursued, reason: ..." if rejected; add to `OPEN-QUESTIONS.md` if it's not session-ready yet.

5. **Commit** with a clear `V<N>:` message describing what shipped.

6. **Tag** the commit: `git tag v<N>`.

7. **Delete the session's `planning/sessions/Vxx.md` scope file** as part of the commit. Cowork's bash mount can refuse on file ACLs — if so, hand-delete via Windows Explorer before staging. (Session scopes are transient — see *Planning artefacts: what lives where* below.)

8. **Push commit + tag.** `git push origin main` and `git push origin v<N>`. Pause only if something in the commit shouldn't be public (secrets, credentials, personal information); otherwise push by default.

---

## Doc-code parity

The plugin's code (hooks, agents, skills, slash commands, bundled artefacts) and the descriptive docs (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, the templates, `planning/INVENTORY.md`) must stay in alignment. Whenever a session ships a code change that introduces a new concept, mechanism, section, marker, location, or rule, the same session updates the descriptive docs to match. Don't ship code referring to something the docs don't describe; don't leave docs describing something the code no longer does.

The cost of catching a gap in the session that created it is small. The cost of catching it three sessions later is large. Silent drift compounds across sessions until the docs and the code describe two different methods.

**During the session.** As you write code that depends on something existing in the docs — a hook deny message that names a section, a skill body that points at a *Where the docs live* block, a subagent prompt that references a marker — check that the dependency is documented. If it isn't, the doc update is part of *this* session, not a future one.

**At session close.** Before bumping footers and writing the BUILD-LOG entry, audit this session's code changes against the descriptive docs. The audit is scoped to what changed this session — not a full re-read of every doc — but it's explicit:

1. **Vocabulary.** If the session introduced a new named concept, `NO-CODE-METHOD.md → Vocabulary` defines it.

2. **Mechanism descriptions.** If the session changed how something works (a new route, a different fold-in destination, a new enforcement point, a renamed marker), `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` describe the new mechanism, not the old one. Use `Grep` to find every reference to the old mechanism — section names, counts (`Three sections...` after introducing a fourth), location phrases, internal cross-references — and update each. Read each match; confirm the surrounding sentence still parses with the new wording.

3. **Templates.** If the session introduced a new section, marker, or canonical format, the relevant template carries it. If a hook or skill tells Claude to write to a section, that section is in the template — verifiable by reading the template. **Templates live in two locations** (`templates/` and `plugin/templates/`); both copies update together.

4. **Inventory.** If the session added a new plugin component or changed a component's responsibility, `planning/INVENTORY.md` reflects the current architecture (it's a living document — see *Planning artefacts* below).

5. **Crash course.** If the session changed a load-bearing concept, mechanism, or named element of the method, `Crash course.md` reflects the change at narrative altitude. Crash course is the readable summary of the method — when the method changes, the summary changes. Preserve the narrative voice; this isn't the place to mirror the spec's exact structure.

6. **Ghost references.** Audit for paragraphs that assert state contradicted by `BUILD-LOG.md` or by the actual code on disk. The V22 case was INVENTORY listing future slash commands as if shipped; the V23-era case was `CLAUDE.md` asserting "the plugin has never been installed in Claude Code" while V18/V19/V21/V22 BUILD-LOG entries all describe `claude --plugin-dir` smoke tests with hooks firing. Both are recording errors that lead future Claude to wrong conclusions. The catch is: when a doc paragraph makes a state claim, cross-check against BUILD-LOG; when BUILD-LOG and the doc disagree, BUILD-LOG wins.

**The escape clause.** If the audit surfaces a gap whose doc work would dominate the session's actual scope — a structural rewrite touching many sections of `NO-CODE-METHOD.md`, or a re-org of the whole Vocabulary, or anything where the doc change is itself a method-level design decision — the rule is *not* "force it in." Surface the scope in chat, weigh fold-in-now vs. new-session-for-the-rewrite, and decide together. **The default lean is fold-in-now** — the cost is usually overstated, and shipping inconsistency is worse than over-running a session by 15 minutes. `OPEN-QUESTIONS.md` is for the genuinely large rewrites where the doc work warrants its own design pass.

---

## Testing — what we actually do

Testing in this project means **smoke-testing the plugin in Claude Code** using `claude --plugin-dir <path>` against a scratch directory (typically `~/v<N>-scratch`) or against Taskflow. This *is* live testing. Hooks register and fire; slash commands are visible in `/hooks` and `/agents`; subagents are invoked through Claude Code's normal mechanism; the SessionStart hook injects `additionalContext`; the PreToolUse hook denies edits with reason text; `/init-project` scaffolds templates. V18, V19, V21, and V22 each shipped with a smoke test of this shape (V20 and V23 were doc-only — no testable behaviour). Outcomes go into `TEST-LOG.md`; see *Where test outcomes are recorded* below.

**Pre-install testing options — these are what we use:**

- **Smoke test in Claude Code via `--plugin-dir`.** As above. The session-scoped install. This is the highest-fidelity test available without a global plugin install — hooks, agents, slash commands, subagent invocations, and the surrounding Claude Code session behaviour all run through Claude Code's real machinery. Standard for any session shipping testable code.

- **Hook script direct invocation.** `echo '{"cwd": "/path/to/test/folder", "session_id": "test"}' | python plugin/hooks/session_start.py`. Validates the script's input parsing, file reads, and stdout shape. Useful for catching syntax errors and arithmetic mistakes before the smoke test, or for fast iteration during development. Doesn't validate that Claude Code actually triggers the hook.

- **Parser script CLI run.** Call a script that exposes a CLI directly: `python plugin/scripts/parse_backlog.py <BACKLOG.md path>`, inspect the output. Validates parser behaviour against real input files.

- **Code review.** Read the hook / subagent / skill code and reason about it. Catches structural and wiring errors; misses runtime issues that only surface in a live session.

**What we don't do (and why "not doing X" doesn't mean "untested"):**

- **No global plugin install** via `~/.claude/plugins/` or a marketplace. The plugin has never been installed that way. This is a real limitation — `--plugin-dir` is per-session — but it doesn't make the smoke test less of a real test. Future sessions might add a global-install step (e.g. as part of a release process); for now, `--plugin-dir` is the operational mode.

- **No marketplace publication.** The plugin isn't published anywhere a user can install from. That's a packaging task, not a testing task.

- **No automated CI.** Smoke tests are hand-run by Alex post-session in a Claude Code window on her Windows machine. No GitHub Actions, no scripted regression suite. This is deliberate at this stage — the value of CI is in catching regressions across many simultaneous changes, and the project ships one tag at a time with full attention.

**Where test outcomes are recorded.** Each smoke-test check goes into `sovereign-implementer/TEST-LOG.md` as one row, with a stable ID, the session it ran in, the component exercised, status (Pass / Fail / Skipped — with reason if skipped), and notes. The `BUILD-LOG.md` *What shipped* paragraph references the TEST-LOG row range for the session ("see TEST-LOG #045-052") rather than restating individual test outcomes. TEST-LOG is the canonical, queryable record; BUILD-LOG carries the prose narrative around it.

This separation exists because the previous arrangement — inline test prose in BUILD-LOG "What shipped" paragraphs — turned out to be unsearchable by future sessions. The CLAUDE.md *Plugin install status* paragraph asserting "the plugin has never been installed in Claude Code" went unchallenged for three sessions while BUILD-LOG entries V18, V19, V21, V22 each described `claude --plugin-dir` smoke tests with hooks firing. The information was there; it just wasn't in a shape future-Claude could read at session start. TEST-LOG is.

**The V25 consumer-side TEST-LOG is different.** V25 is building a `TEST-LOG.md` mechanism for projects that *use* the method — tracking what tests have run against a consumer's app. This project's TEST-LOG (at `sovereign-implementer/TEST-LOG.md`) is dev-internal and predates that work. They're siblings, not the same thing.

**One pitfall to name explicitly.** "Live install + back-test" as a single-session deliverable keeps surfacing as a proposal and is **not viable in the current state** because the plugin hasn't been packaged for global install. `--plugin-dir` smoke tests are the working substitute and they ARE happening per session. Don't conflate the two. If a session genuinely needs global-install testing, it needs a packaging session first; that's its own work.

---

## Footer bumps: the full list

When a session substantively changes the method or plugin (see *Session tag vs. method version* above for the test), the `*No-code method — Version N.*` footer at the bottom of every method-side file gets bumped to match the new session number. **Dev-internal-only sessions skip this entirely** — no footer bumps, no `plugin.json` change, no `PLUGIN_METHOD_VERSION` change.

Method-side means files that describe how the consumer method works. Dev-internal files (`BUILD-LOG.md`, `TEST-LOG.md`, `PLAN.md`, `OPEN-QUESTIONS.md`, this file) don't carry the footer.

When a bump is warranted, the list as of V23:

- `NO-CODE-METHOD.md`
- `DOC-STRUCTURE.md`
- `Crash course.md`
- `templates/CLAUDE-TEMPLATE.md`
- `templates/UX-TEMPLATE.md`
- `templates/BACKLOG-TEMPLATE.md`
- `templates/MANIFEST-TEMPLATE.md`
- `templates/TEST-LOG-TEMPLATE.md`
- `templates/ADDITIONAL-DOC-TEMPLATE.md`
- `plugin/templates/CLAUDE-TEMPLATE.md`
- `plugin/templates/UX-TEMPLATE.md`
- `plugin/templates/BACKLOG-TEMPLATE.md`
- `plugin/templates/MANIFEST-TEMPLATE.md`
- `plugin/templates/TEST-LOG-TEMPLATE.md`
- `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`
- `planning/INVENTORY.md`
- Every subagent body under `plugin/agents/` that carries a footer (currently `planning.md`, `before-build.md`, `batch-executor.md`)
- New files added in this session that describe the method

Plus the version trackers:

- `plugin/.claude-plugin/plugin.json` — `version` field bumps to `0.<N>.0`
- `plugin/hooks/session_start.py` — `PLUGIN_METHOD_VERSION` constant bumps to `N`

V21's smoke test caught a footer miss via the SessionStart hook's version-footer tripwire — the `plugin/templates/*.md` copies hadn't been bumped while the `templates/*.md` originals had. The two-location rule is easy to miss; the tripwire backstops it. New files that get added to the bump list should be added to this section as part of the session that creates them.

---

## Planning artefacts: what lives where, and for how long

| File | Lifecycle | When it's deleted |
|---|---|---|
| `planning/sessions/Vxx.md` | **Transient.** Provisional scope for one specific session. Once the session ships, the commit + code + doc edits become the source of truth and the scope doc is a stale snapshot. | When the session ships and is committed (step 7 of session close). |
| `planning/drafts/<topic>.md` | **Transient.** Substantive content generated in chat that a future session might want to start from — drafts, comparison tables, structural sketches, protocol rules, column shapes, option matrices. Committed by the drafting session the moment it's "good enough to walk away from." | When consumed (folded into a spec, scope file, or other persistent location), in the commit of whichever session consumes the draft. Dead-end drafts pruned with a one-line note in `BUILD-LOG.md`. |
| `planning/INVENTORY.md` | **Living document.** Always describes the current plugin architecture. Updated in place as decisions resolve. | Never. |
| `planning/PLAN.md` | **Living document.** Rolling roadmap. Completed sessions removed; new sessions added as discovered. | Never. |
| `planning/OPEN-QUESTIONS.md` | **Living document.** Method-level questions raised but not yet ready to be a session. Each entry has a *Next step* line. | Per entry: when the question resolves. The file itself: never. |
| `planning/claude-code-plugin-feasibility-response.md`, `planning/OPUS-FEASIBILITY-PROMPT.md` | **Historical record.** Why V17 made specific architectural decisions. | Never. Could move to `planning/archive/` if `planning/` gets cluttered. |
| `BUILD-LOG.md` | **Historical record.** Append-only at the top (newest first). | Never. |
| `TEST-LOG.md` | **Living record.** One row per smoke-test check, newest at the bottom. Status may flip (Pass → Fail) if a later session breaks something previously verified, then back to Pass when the regression is fixed. | Never. Rows are not removed when components change substantially; instead the row is marked Superseded and a new row records the post-change retest. |
| `BUILD-METHOD.md` (this file) | **Living document.** Working manual. Updated in place when the project's working method changes. | Never. |

### Drafts in flight

`planning/drafts/<topic>.md` is where substantive content generated in chat lands as soon as a future session might want to start from it — drafts, comparison tables, structural sketches, protocol rules, column shapes, option matrices, anything that took real thinking and could seed a later spec change. The drafting session commits the file as part of its own commit; "good enough to walk away from" is the bar, not "finished and polished." Files are deleted in the commit of whichever session consumes the draft (folding the content into a spec, a `Vxx.md` scope file, or another persistent location). If a draft turns out to be a dead end, prune it with a one-line note in the next `BUILD-LOG.md` entry explaining why.

**Corollary.** If a `Vxx.md` scope file's *Inputs* section names content that isn't reachable from the committed repo — phrasings like "Alex has the file locally," "from the previous chat," "see the artefact at [external location]," or "the [X] draft" with no committed path — that's a bug, not a workflow. Fix at the source: get the content into `planning/drafts/` retroactively if it still exists in chat history, or restate the input as something the next session can rebuild from what is in the repo. Don't hunt at the destination. The session-open scan rule in `CLAUDE.md` → *Vxx.md inputs must be in the repo* catches the reading side of this; this rule prevents the writing side.

Worked example: the V20 → V26 failure. A "Sonnet draft" with a canonical TEST-LOG column shape and protocol rules was generated in V20 planning chat. It was never committed. V20's session-close wrote "Alex has the file locally; pull it into this session as the starting shape" into `V26.md` as an input. V26 session-open then halted on a reference to content that no longer existed in retrievable form. The `planning/drafts/` convention exists to make this impossible going forward.

---

## BUILD-LOG entry shape

`BUILD-LOG.md` is the project's running record of decisions, changes, and reasoning, ordered newest-first. It exists so Alex can talk about progress with vibe-coding friends without making them read every commit and planning doc, and so future-Alex (and future-Claude) can reconstruct *why* a decision was made (commit messages capture *what*).

Each session adds one entry at the top of the file, in this shape:

```markdown
## V<N> — YYYY-MM-DD — One-line summary of the session

**What shipped.** A short paragraph in plain English describing the concrete deliverables. Files added, files changed structurally, plugin components installed, smoke-test outcomes inline.

**Decisions taken and why.** Two or three bullets covering the load-bearing decisions of the session — what was chosen, what alternatives were considered, what tipped the call. Skip housekeeping (footer bumps, README touch-ups); focus on choices that shape future sessions.

**Pivots and surprises.** Anything that turned out differently than the session scope expected — a bug, a wrong assumption in INVENTORY, an external fact discovered mid-session. Reference issue numbers / docs where relevant.

**Carried forward.** Items that came up but weren't done this session, with their destination (which future `Vxx.md` or PLAN.md row, or "not pursued — reason").
```

Don't pad. A good entry is half a page; a great entry is shorter. The audience is a friend skimming, not an auditor.

---

## OPEN-QUESTIONS entry shape

`planning/OPEN-QUESTIONS.md` is the parking lot for method-level questions that have been raised but aren't yet ready to be a session. The file exists because PLAN.md is for sessions whose shape we already know, INVENTORY.md is for current architecture, and BUILD-LOG.md is historical — there was previously no home for "a real concern was raised and we need to think about it before scoping a session."

Each entry has this shape:

```markdown
## One-line question title

**The question.** A paragraph framing the question clearly.

**Why it matters.** Brief context — who raised it, what assumption(s) it breaks, what's at risk if we don't address it.

**Working notes.** Optional. Rough shapes the response could take, alternatives being weighed, partial thinking. Skip if nothing useful to record yet.

**Next step.** Where this is going — "fold into Vxx if [condition]", "promote to new session after Vyy ships", "decide by [date]", or "park". Every entry has one.
```

Newest first. Entries are **removed** when resolved — when the answer folds into a session's scope (or a new session is created and added to `PLAN.md`), the entry leaves `OPEN-QUESTIONS.md`. If the question is consciously dropped without action, note the reason in `BUILD-LOG.md` for that session so future-Alex knows it was considered, then remove from `OPEN-QUESTIONS.md`.

**At session start**, the routine scan picks up entries whose *Next step* mentions the current session — those need attention this session.

---

## TEST-LOG entry shape

`sovereign-implementer/TEST-LOG.md` is the project's smoke-test record. Each row is one distinct check ran in one session. The table:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID (`001`, `002`, ...). Never reused. |
| **Date** | YYYY-MM-DD of the session. |
| **Session** | Session tag (`V18`, `V19`, ...). |
| **Test** | What was checked, in one sentence. Specific enough that someone can re-run it from this description alone. |
| **Component** | Which plugin component(s) the test exercised. |
| **Status** | `Pass`, `Fail`, or `Skipped`. Skipped requires a reason in *Notes*. |
| **Notes** | Observations, surprises, the discovery the test surfaced, or the reason if skipped. Keep tight. |

**When to add a row.** During or immediately after a smoke test, while the outcome is fresh. Append at the bottom (newest at the bottom — opposite of BUILD-LOG, because TEST-LOG is queried for "is X tested?" where ID order matters more than recency).

**When a status flips.** If a later session shows a previously-Pass check now Fails, *append a new row* with the same Test description, today's session, and `Fail` — don't edit the old row. The same applies in reverse when the fix lands: a new row with `Pass` after the fix. The row-per-event pattern keeps the historical record intact.

**When a component changes substantially.** The old row's Status is changed to `Superseded` with a note pointing at the session that changed the component. New rows then record the retest in the post-change shape. This is rarer than a Pass/Fail flip — only triggered when the test description itself no longer makes sense against the new component.

**Linking from BUILD-LOG.** Each BUILD-LOG entry that ran a smoke test names the TEST-LOG row range in *What shipped* (e.g. "smoke-tested in `~\v24-scratch`; see TEST-LOG #023-028"). The prose narrative around the tests stays in BUILD-LOG; the per-check record stays in TEST-LOG. Don't duplicate.

---

## Plugin migration context

From V17 onwards, this project is engaged in a **plugin migration** — distributing the no-code method's rules across Claude Code plugin components (hooks, subagents, skills, slash commands) so adherence becomes structural rather than prompt-based. The design and roadmap live in `planning/INVENTORY.md`, `planning/PLAN.md`, and `planning/claude-code-plugin-feasibility-response.md`. The "method" going forward includes plugin components, not just markdown.

This is context for working in the project, not a procedural rule. The session structure, doc-code parity, and testing semantics above apply whether the session ships plugin code or method-doc prose.
