# BUILD-METHOD.md — How this project ships

How the no-code-method dev project runs: session open, middle, close, testing, where artefacts live. Sibling of `BUILD-LOG.md` (what shipped) and `planning/PLAN.md` (what's coming).

This is **not** the no-code method itself — that's what this project produces (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, `templates/`, `plugin/`). Those describe how consumers run *their* projects; this describes how Alex and Claude run *this* one.

Personal and collaboration rules live in root `CLAUDE.md`. Anything here supersedes older equivalents in that file.

---

## The unit of work: a session

**One session = one git commit + one git tag.** A new session starts when Alex marks a new boundary. Not a calendar day, not a continuous block, not one chat conversation — tag boundaries define sessions.

Tags are `v17`, `v18`, ... Current tag is `git describe --tags --abbrev=0` from `sovereign-implementer/`. Pre-V17 lives read-only in `Archive/Version 3/` through `Archive/Version 16/`. Don't edit.

### Session tag vs. method version

Session tag (`v17`, ...) names the dev project's working state — increments per session.

**Method version** is what consumers see — the `*No-code method — Version N.*` footer on every method-side file. Increments only when the method or plugin **substantively changes** (new mechanism, renamed component, shipped plugin feature, structural rewrite). Dev-internal changes (BUILD-LOG, BUILD-METHOD, planning, TEST-LOG) don't bump it.

So the two numbers diverge. Session `v25` may ship with V23 footers because nothing method-side has substantively changed since V23. That's correct, not drift — the V21 tripwire compares loaded footers against `PLUGIN_METHOD_VERSION` in `session_start.py`; both stay locked together until a method-changing session bumps them in tandem.

**Historical note.** V18–V23 conflated the two — every session bumped the footer regardless. Going forward they're separated; historical mismatches stay (no retroactive corrections).

---

## Session open

In order:

1. `git describe --tags --abbrev=0` from `sovereign-implementer/` — confirm current version.
2. Read `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md` at `HEAD` — the active method.
3. Scan `planning/OPEN-QUESTIONS.md` for entries whose *Next step* names the current session.
4. Read the active scope file at `planning/sessions/V<N>.md` — provisional scope, not a contract. `<N>` is the lowest version number present in that folder above the current tag from step 1 (i.e. the next session up, not the furthest-out one). Use the absolute path (see `CLAUDE.md → Current state` for why). If no scope file exists above the current tag, say so in the session opener and wait for direction — don't invent a scope. Don't wait to be asked.

Then read Alex's opener and route. `CLAUDE.md → Working with me` governs interaction shape. If the task isn't clear, report what was loaded and ask. Don't draft.

---

## Session middle: planning, building, or both

Three shapes, often blended:

**Implementation sessions** ship plugin code (hooks, subagents, slash commands, skills) or method-doc structural changes. End with a smoke test plus doc-parity edits in the same commit.

**Doc-only sessions** ship rewrites without testable code — terminology sweep (V23), parity catch-up (V20), OPEN-QUESTIONS resolution as prose. No smoke test; doc-code parity audit still runs at close.

**Planning sessions** rescope the roadmap — split or merge sessions, write or revise `Vxx.md` scope files, add or resolve OPEN-QUESTIONS, restructure PLAN.md. Usually still produce a tagged commit because rescoping is version-worthy.

Claude's job mid-session: do the work, surface concerns, propose. Close, parity, and testing rules apply regardless of middle shape.

---

## Session close: 9 steps

1. **Verify doc-code parity** (audit below). If this session introduced anything the docs don't accurately describe, fix docs first. Footer bumps and BUILD-LOG entry come after, reflecting the now-current state.

2. **Frame-correction sweep.** If this session substantively corrected a load-bearing frame — something the next-session Claude reading old scope files would absorb wrongly — audit `planning/sessions/Vxx.md` for references to the old frame. Fix in this session's commit. The bar isn't "anything changed" but "the change rewrites how future-Claude should think about [X]." Examples: V23 settling that `--plugin-dir` smoke tests ARE live testing (implicit reframe of the live-install dependency carried in pre-V23 scope files); V29's pivot from `systemMessage` halt to SessionStart advisory + PreToolUse enforcement. Both broke prior scope files that referenced the old frame. Frame corrections aren't always self-identifying — the audit prompt is the trigger, not pre-detection. Added V29 after V29's own open hit a pre-V23 frame in its scope file and required rework before substantive work could begin.

3. **Bump method-version footers** — only if the session substantively changed the method or plugin. Dev-internal-only sessions skip entirely. When warranted: every method-side file and template footer matches the new session number, plus `plugin.json` `version` and `PLUGIN_METHOD_VERSION` in `session_start.py`. Full list in *Footer bumps* below.

4. **Add a `BUILD-LOG.md` entry** for this session, shape in *BUILD-LOG entry shape*. Newest first.

5. **Sweep ideas raised but not implemented.** For each: add to a future `Vxx.md`; create a new `Vxx.md` + PLAN.md row; note in BUILD-LOG as "not pursued, reason: ..."; or add to `OPEN-QUESTIONS.md`.

6. **Commit** with a clear `V<N>:` message.

7. **Tag** `git tag v<N>`.

8. **Delete this session's `planning/sessions/Vxx.md`** as part of the commit. If bash refuses on Windows ACLs, hand-delete via Windows Explorer first. (Session scopes are transient — see *Planning artefacts* below.)

9. **Push commit + tag.** `git push origin main` and `git push origin v<N>`. Pause only for secrets, credentials, or personal info; otherwise push by default.

---

## Doc-code parity

Plugin code (hooks, agents, skills, slash commands, bundled artefacts) and descriptive docs (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, templates, `planning/INVENTORY.md`) must stay aligned. When a session ships code introducing a new concept, mechanism, section, marker, location, or rule, the same session updates the docs. Don't ship code referring to something the docs don't describe; don't leave docs describing what the code no longer does.

Catching a gap in the session that created it is cheap. Three sessions later it's expensive. Silent drift compounds.

**During the session.** As code depends on something existing in the docs — a hook deny message naming a section, a skill body pointing at a docs block, a subagent referencing a marker — check the dependency is documented. If not, the doc update is part of *this* session.

**At session close.** Audit this session's code changes against the docs — scoped to what changed, not a full re-read:

1. **Vocabulary.** New named concepts are defined in `NO-CODE-METHOD.md → Vocabulary`.

2. **Mechanism descriptions.** If something works differently (new route, different fold-in destination, new enforcement point, renamed marker), `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` describe the new mechanism. Grep every reference to the old — section names, counts (`Three sections...` after a fourth lands), location phrases, cross-references — and update. Read each match; confirm surrounding sentences still parse.

3. **Templates.** New sections, markers, or canonical formats land in the relevant template. If a hook or skill writes to a section, that section is in the template. **Two locations** (`templates/`, `plugin/templates/`) — both update together.

4. **Inventory.** New plugin components or changed responsibilities → `planning/INVENTORY.md` (living — see *Planning artefacts*).

5. **Crash course.** Load-bearing concept, mechanism, or named element changes → `Crash course.md` reflects it at narrative altitude. Preserve narrative voice; don't mirror the spec's structure.

6. **Ghost references.** Audit for paragraphs asserting state contradicted by `BUILD-LOG.md` or actual code. V22: INVENTORY listed future slash commands as if shipped. V23-era: `CLAUDE.md` asserted "the plugin has never been installed in Claude Code" while V18/V19/V21/V22 BUILD-LOG entries each described `claude --plugin-dir` smoke tests with hooks firing. Recording errors lead future-Claude wrong. When a doc paragraph makes a state claim, cross-check against BUILD-LOG; on disagreement, BUILD-LOG wins.

**Escape clause.** If the audit surfaces a gap whose doc work would dominate the session's scope — a structural rewrite touching many sections, a Vocabulary re-org, anything where the doc change is itself a method-level design decision — surface in chat, weigh fold-in-now vs. new-session, decide together. **Default lean: fold in now.** Cost is usually overstated; shipping inconsistency is worse than overrunning by 15 minutes. `OPEN-QUESTIONS.md` is for the genuinely large rewrites.

---

## Two-write rule for canonical docs

V32 split canonical method content into two parallel artefact sets:

- **Plugin-side canonical docs** (the operational system). Live inside `plugin/` — `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/universal-behaviour.md`, the bundled templates at `plugin/templates/`, plus the agent bodies that inline operating procedures (`planning.md`, `before-build.md`, `after-build.md`, `batch-executor.md`, `adopt.md`). These are what the plugin runtime reads. **The plugin is the leader** — when the method substantively changes, the plugin gets edited first.

- **Docs-only canonical docs** (the project-agnostic system). Live at the repo root — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, the templates at `templates/`. Maintained as the prose-only / no-plugin version of the method for chat-with-Claude or other AI-tool contexts where the plugin shape doesn't fit. The docs-only set follows the plugin's lead — kept as fresh as the plugin via the two-write discipline below.

`Crash course.md` (repo root) is plugin-side only — it documents how to install and use the plugin. It does not appear in the docs-only set.

### The two-write discipline

When a session substantively changes a method rule (a new step in *During planning*, a new flag-taxonomy row, a renamed concept in *Vocabulary*, etc.), update both copies of every affected canonical doc. Doc-code parity audits at session close must check both sides. Drift between the two sides is the risk this arrangement carries — the discipline is the defence.

Cross-references inside the two copies legitimately diverge:

- **Plugin-side** cross-refs point at plugin homes (`universal-behaviour.md`, `VOCABULARY.md`, `planning.md`, etc.). The plugin's subagents read these at runtime.
- **Docs-only side** cross-refs point at sibling sections of `NO-CODE-METHOD.md` (and the docs-only `DOC-STRUCTURE.md` / `VOCABULARY.md`). A no-plugin reader follows references inside the prose spec without needing to know about plugin internals.

The substance — the actual rules, definitions, structural specs — stays identical across both sides. Cross-references are the explicit exception.

### Don't propose re-coupling

Future sessions might be tempted to re-introduce a "subagents read NO-CODE-METHOD.md at runtime" pattern as a parity defence. That's exactly what V32 dismantles. The discipline of the two-write rule is the intended defence, not runtime coupling.

---

## Testing — what we actually do

Testing here means **smoke-testing in Claude Code** via `claude --plugin-dir <path>` against a scratch directory (`~/v<N>-scratch`) or Taskflow. This *is* live testing. Hooks register and fire; slash commands appear in `/hooks` and `/agents`; subagents invoke through normal mechanism; SessionStart injects `additionalContext`; PreToolUse denies with reason text; `/adopt` (V29 — formerly `/init-project`) scaffolds templates and handles its other case branches. V18, V19, V21, V22 each shipped with smoke tests (V20, V23 were doc-only). Outcomes go to `TEST-LOG.md`.

**Pre-install testing options:**

- **Smoke test via `--plugin-dir`.** Session-scoped install. Highest fidelity available without global install — hooks, agents, slash commands, subagents, and surrounding Claude Code session behaviour all run through real machinery. Standard for any session shipping testable code.

- **Hook script direct invocation.** `echo '{"cwd": "/path/to/test/folder", "session_id": "test"}' | python plugin/hooks/session_start.py`. Validates input parsing, file reads, stdout shape. Useful for catching syntax errors and arithmetic mistakes pre-smoke-test, or for fast iteration. Doesn't validate that Claude Code actually triggers the hook.

- **Parser script CLI run.** `python plugin/scripts/parse_backlog.py <BACKLOG.md path>` — inspect output. Validates parser behaviour against real input.

- **Code review.** Read and reason. Catches structural and wiring errors; misses runtime issues.

**What we don't do** (and why "not doing X" ≠ "untested"):

- **No global install** via `~/.claude/plugins/` or a marketplace. Real limitation but doesn't make the smoke test less real. Future sessions may add it (e.g. release process); for now `--plugin-dir` is operational.

- **No marketplace publication.** Packaging task, not testing.

- **No automated CI.** Smoke tests are hand-run by Alex post-session on her Windows machine. Deliberate — CI's value is regression-catching across many simultaneous changes; this project ships one tag at a time with full attention.

**Where outcomes go.** Each check goes to `sovereign-implementer/TEST-LOG.md` as one row: stable ID, session, component, status (Pass / Fail / Skipped + reason), notes. `BUILD-LOG.md` *What shipped* references the TEST-LOG row range ("see TEST-LOG #045-052") rather than restating outcomes. TEST-LOG is canonical and queryable; BUILD-LOG carries prose narrative.

The separation exists because inline test prose in BUILD-LOG turned out unsearchable. The `CLAUDE.md` paragraph asserting "the plugin has never been installed in Claude Code" went unchallenged for three sessions while V18/V19/V21/V22 BUILD-LOG entries each described `claude --plugin-dir` smoke tests with hooks firing. The information was there; it wasn't in a shape future-Claude could read at session start. TEST-LOG is.

**The V25 consumer-side TEST-LOG is different.** V25 builds a `TEST-LOG.md` mechanism for projects that *use* the method — tracking tests against a consumer's app. This project's TEST-LOG is dev-internal and predates that. Siblings, not the same thing.

**Pitfall.** "Live install + back-test" as a single-session deliverable keeps resurfacing and is **not viable** because the plugin isn't packaged for global install. `--plugin-dir` smoke tests are the working substitute and they ARE happening per session. Don't conflate. A session genuinely needing global-install testing needs a packaging session first.

---

## Footer bumps: the full list

When a session substantively changes the method or plugin (test in *Session tag vs. method version*), every method-side `*No-code method — Version N.*` footer bumps to match. **Dev-internal-only sessions skip entirely** — no footer bumps, no `plugin.json`, no `PLUGIN_METHOD_VERSION`.

Method-side = describes how the consumer method works. Dev-internal files (`BUILD-LOG.md`, `TEST-LOG.md`, `PLAN.md`, `OPEN-QUESTIONS.md`, this file) don't carry the footer.

The list splits in V32 along the two-write architecture (see *Two-write rule for canonical docs* above). Both sides bump together.

### Plugin-side (the leader)

- `plugin/docs/DOC-STRUCTURE.md`
- `plugin/docs/VOCABULARY.md`
- `plugin/hooks/universal-behaviour.md`
- `plugin/templates/CLAUDE-TEMPLATE.md`
- `plugin/templates/UX-TEMPLATE.md`
- `plugin/templates/BACKLOG-TEMPLATE.md`
- `plugin/templates/BUILD-LOG-TEMPLATE.md`
- `plugin/templates/MANIFEST-TEMPLATE.md`
- `plugin/templates/TEST-LOG-TEMPLATE.md`
- `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`
- Every footer-carrying subagent under `plugin/agents/` (currently `planning.md`, `before-build.md`, `batch-executor.md`, `after-build.md`, `adopt.md`)
- `Crash course.md` (repo root, but plugin-side audience — documents how to install and use the plugin)

### Docs-only side (the follower)

- `NO-CODE-METHOD.md` (repo root)
- `DOC-STRUCTURE.md` (repo root)
- `VOCABULARY.md` (repo root)
- `templates/CLAUDE-TEMPLATE.md`
- `templates/UX-TEMPLATE.md`
- `templates/BACKLOG-TEMPLATE.md`
- `templates/BUILD-LOG-TEMPLATE.md`
- `templates/MANIFEST-TEMPLATE.md`
- `templates/TEST-LOG-TEMPLATE.md`
- `templates/ADDITIONAL-DOC-TEMPLATE.md`

### Cross-cutting (dev-internal but version-tagged)

- `planning/INVENTORY.md` — carries the footer for sync purposes, even though it's dev-internal.

### New files added this session

Add new method-describing files to the right column above as part of the session creating them.

### Version trackers

- `plugin/.claude-plugin/plugin.json` — `version` → `0.<N>.0`
- `plugin/hooks/session_start.py` — `PLUGIN_METHOD_VERSION` → `N`

V21's smoke test caught a footer miss via the SessionStart tripwire — `plugin/templates/*.md` hadn't been bumped while `templates/*.md` had. The two-location rule is easy to miss; the tripwire backstops it.

**`universal-behaviour.md` does not carry the `*No-code method — Version N.*` footer** — it carries a longer signature paragraph instead (see the file). It's listed in the plugin-side bump list above because its substance is method-canonical and must move in lockstep with the version trackers.

---

## Planning artefacts: what lives where, and for how long

| File | Lifecycle | When deleted |
|---|---|---|
| `planning/sessions/Vxx.md` | **Transient.** Provisional scope for one session. Once shipped, the commit + code + doc edits are source of truth; the scope doc is stale. | When the session ships (step 7). |
| `planning/drafts/<topic>.md` | **Transient.** Substantive chat content a future session might start from — drafts, comparison tables, structural sketches, protocol rules, column shapes, option matrices. Committed when "good enough to walk away from." | When consumed (folded into spec/scope/other persistent location), in the commit of whichever session consumes it. Dead-ends pruned with a one-line note in `BUILD-LOG.md`. |
| `planning/INVENTORY.md` | **Living.** Current plugin architecture. Updated in place. | Never. |
| `planning/PLAN.md` | **Living.** Rolling roadmap. | Never. |
| `planning/OPEN-QUESTIONS.md` | **Living.** Method-level questions not yet session-ready. Each entry has a *Next step*. | Per entry: when resolved. File: never. |
| `planning/claude-code-plugin-feasibility-response.md`, `planning/OPUS-FEASIBILITY-PROMPT.md` | **Historical.** Why V17 made specific architectural decisions. | Never. Could move to `planning/archive/` if `planning/` clutters. |
| `BUILD-LOG.md` | **Historical.** Append-only at top (newest first). | Never. |
| `TEST-LOG.md` | **Living.** One row per smoke-test check, newest at bottom. Status may flip if a later session breaks something, then back when fixed. | Never. Rows aren't removed when components change substantially; marked Superseded with a new row recording the post-change retest. |
| `BUILD-METHOD.md` (this file) | **Living.** Working manual. Updated in place. | Never. |

### Drafts in flight

`planning/drafts/<topic>.md` is where substantive chat content lands as soon as a future session might start from it. The drafting session commits the file as part of its own commit; "good enough to walk away from" is the bar, not "polished." Files are deleted in the commit of whichever session consumes them (folding into a spec, `Vxx.md`, or persistent location). Dead-end drafts: prune with a one-line note in next `BUILD-LOG.md`.

**Corollary.** If a `Vxx.md` *Inputs* names content not reachable from the committed repo — phrasings like "Alex has the file locally," "from the previous chat," "see the artefact at [external location]," or "the [X] draft" without a committed path — that's a bug. Fix at the source: get the content into `planning/drafts/` retroactively if it still exists in chat history, or restate the input as something the next session can rebuild from what is in the repo. Don't hunt at the destination. The session-open scan in `CLAUDE.md → Vxx.md inputs must be in the repo` catches the reading side; this catches the writing side.

Worked example: V20 → V26 failure. A "Sonnet draft" with canonical TEST-LOG column shape and protocol rules was generated in V20 planning chat. Never committed. V20's session-close wrote "Alex has the file locally; pull it into this session as the starting shape" into `V26.md`. V26 session-open halted on a reference to content that no longer existed in retrievable form. `planning/drafts/` makes this impossible going forward.

---

## BUILD-LOG entry shape

`BUILD-LOG.md` is the running record of decisions, changes, and reasoning, newest-first. It exists so Alex can talk progress with vibe-coding friends without making them read every commit, and so future-Alex (and future-Claude) can reconstruct *why* (commit messages cover *what*).

One entry per session at the top:

```markdown
## V<N> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Files added, files changed structurally, plugin components installed, smoke-test outcomes inline.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping (footer bumps, README touch-ups); focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the scope expected — a bug, a wrong assumption in INVENTORY, an external fact discovered mid-session. Reference issue numbers / docs.

**Carried forward.** Items raised but not done, with destination (which future `Vxx.md` or PLAN.md row, or "not pursued — reason").
```

Don't pad. A good entry is half a page; a great one is shorter. Audience: a friend skimming, not an auditor.

---

## OPEN-QUESTIONS entry shape

`planning/OPEN-QUESTIONS.md` is the parking lot for method-level questions raised but not yet session-ready. PLAN.md is for sessions with known shape; INVENTORY.md for current architecture; BUILD-LOG.md is historical — there was no home for "a real concern was raised; think before scoping."

Each entry:

```markdown
## One-line question title

**The question.** A paragraph framing it clearly.

**Why it matters.** Brief context — who raised it, what assumption(s) it breaks, what's at risk.

**Working notes.** Optional. Rough shapes the response could take, alternatives weighed, partial thinking. Skip if nothing useful yet.

**Next step.** Where this is going — "fold into Vxx if [condition]", "promote to new session after Vyy ships", "decide by [date]", or "park". Every entry has one.
```

Newest first.

### Graduation paths — four ways an entry leaves

Entries resolve and leave the file via one of four paths. The *Next step* line on each entry names a trigger that, when fired, points the entry toward one of these paths.

1. **Folded into an upcoming session's scope.** The most common path. *Next step* names a condition like "fold into Vxx if X" or "promote to a planning session in V31+." At session-open time, the routine scan (*Session open* → step 3) looks for entries whose *Next step* names the current session. When matched, the entry's question becomes part of that session's `planning/sessions/Vxx.md` scope file; the work happens within the session. Entry removed at session close, alongside `Vxx.md`'s own deletion (*Session close* step 8).

2. **Promoted to its own session.** A new row is added to `planning/PLAN.md`, a new `planning/sessions/Vxx.md` scope file is created, and the question becomes the basis for a future session. Entry removed from `OPEN-QUESTIONS.md` at promotion (not later, at the session's ship — the entry's role is over once a session exists for it).

3. **Partial fold-in.** Some entries resolve only partly — a session addresses one shape of the question while leaving others parked. The entry stays in `OPEN-QUESTIONS.md` with a date-tagged update note recording what was folded ("V22, 2026-05-14: shape #1 partially folded into V22's planning subagent."). The *Next step* may be revised at the same time to reflect what's still open. Real example: the *Method response to direct-edit users* entry, which V22 partially folded but kept open for the remaining shapes.

4. **Consciously dropped.** Entry deemed no longer relevant — drift, scope change, idea proven wrong. One-line reason recorded in `BUILD-LOG.md` for the session that drops it; entry removed.

The session-open scan (step 3 of *Session open*) is what makes graduation triggers fire. There is no fixed schedule — graduation happens when conditions written in the entry's *Next step* match the current session's context.

---

## TEST-LOG entry shape

`sovereign-implementer/TEST-LOG.md` is the smoke-test record. One row per check per session:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID (`001`, `002`, ...). Never reused. |
| **Date** | YYYY-MM-DD of the session. |
| **Session** | Session tag (`V18`, `V19`, ...). |
| **Test** | What was checked, one sentence. Specific enough to re-run from this description. |
| **Component** | Plugin component(s) exercised. |
| **Status** | `Pass`, `Fail`, or `Skipped`. Skipped requires a reason in *Notes*. |
| **Notes** | Observations, surprises, the discovery the test surfaced, or skip reason. Keep tight. |

**When to add.** During or immediately after the smoke test, while outcome is fresh. Append at bottom (opposite of BUILD-LOG — TEST-LOG is queried by "is X tested?" where ID order matters more than recency).

**When status flips.** Previously-Pass now Fails: *append a new row* with the same Test description, today's session, `Fail` — don't edit the old. Same in reverse when the fix lands. Row-per-event keeps history intact.

**When a component changes substantially.** Old row's Status → `Superseded` with a note pointing at the session that changed the component. New rows record the retest in post-change shape. Rarer than a Pass/Fail flip — only when the test description itself no longer makes sense.

**Linking from BUILD-LOG.** Each BUILD-LOG entry running a smoke test names the TEST-LOG row range in *What shipped* ("smoke-tested in `~\v24-scratch`; see TEST-LOG #023-028"). Prose narrative in BUILD-LOG; per-check record in TEST-LOG. Don't duplicate.

---

## Plugin migration context

From V17, this project is engaged in a **plugin migration** — distributing the no-code method's rules across Claude Code plugin components (hooks, subagents, skills, slash commands) so adherence becomes structural rather than prompt-based. Design and roadmap: `planning/INVENTORY.md`, `planning/PLAN.md`, `planning/claude-code-plugin-feasibility-response.md`. The "method" now includes plugin components, not just markdown.

Context for working in the project, not a procedural rule. Session structure, doc-code parity, and testing semantics apply whether the session ships plugin code or method-doc prose.
