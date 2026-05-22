# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

---

## `research/` folder convention + automatic research persistence

**The question.** Should the method formalise a `research/` folder (scaffolded at `/setup` time) where the agent automatically writes findings as `.md` files whenever it researches something — without requiring the user to ask?

**Why it matters.** Surfaced 2026-05-22, ideation session. Two problems: (1) The method currently tells the agent to "prompt the user to do a Sonnet search" — a Cowork-era workaround. Claude Code has built-in web search; the agent should research directly. (2) Research findings have no designated home. They either vanish with the conversation or get manually pasted somewhere. The sovereign-implementer project's own `research/` folder (one `.md` per topic) has proven the pattern works — `research/platform-capabilities-audit.md`, `research/plugin-marketplace-scoping.md`, etc.

**Design so far.**

- `/setup` scaffolds an empty `research/` folder at project root.
- When the agent hits uncertainty sufficient to research, it researches and writes findings to `research/<topic>.md` automatically. No user prompt needed, no size threshold.
- Build log entries link to relevant research files rather than embedding findings inline.
- The Sonnet-search language across method docs (universal-behaviour, subagent bodies, Crash course) is reworded to "offer to conduct research on anything you're uncertain of" — shifting responsibility from user to agent.
- Research files are reference material: no MANIFEST tracking, no BACKLOG entries. Zero maintenance burden.

**Relationship to existing entries.** Adjacent to Distributed fold-ins + open questions section in BACKLOG (shipped V43, session v47) — the `Inputs:` line for build batches is the natural place to reference research files that inform a specific build. Adjacent to [[Graduate sovereign implementer development onto sovereign implementer]] — the method's own dev project already uses this pattern.

**Next step.** **Promoted to V51** (session v47, 2026-05-22). Scope file at `planning/sessions/V51.md`.

---

## BUILD-LOG restructuring — per-build files in a folder with index

**The question.** Should BUILD-LOG.md be replaced by a `build-log/` folder containing one file per build plus a lightweight index, to reduce how much Claude must read?

**Why it matters.** Surfaced 2026-05-22, ideation session. The current monolithic BUILD-LOG.md grows with every build. Claude reads the entire file to write one entry or to check build history during planning. Per-build files mean the agent reads only the entries it needs. The index preserves scan-the-full-history capability in one place.

**Design so far.**

- `build-log/` folder replaces `BUILD-LOG.md`. `/setup` scaffolds the folder.
- One file per build (naming TBD — `BUILD-001.md`, `BUILD-002.md`, or batch-name-based).
- Lightweight index file at `build-log/INDEX.md` — one line per build with a short summary and link. The after-build subagent writes the build entry and appends the index line in the same pass.
- Research files referenced from build entries are linked, not embedded — research lives in `research/`, build entries point to it.

**Relationship to existing entries.** Prerequisite-adjacent for [[Graduate sovereign implementer development onto sovereign implementer]] — the current dev project's `BUILD-LOG.md` is already unwieldy. Pairs naturally with [[`research/` folder convention + automatic research persistence]] — build entries link to research files.

**Next step.** **Promoted to V52** (session v47, 2026-05-22). Scope file at `planning/sessions/V52.md`.

---

## Red-flag / threat-class marker for security-shaped batches

**The question.** Should BACKLOG batches that touch security-shaped surfaces (auth, secrets, PII, deletion of user data, third-party API keys) carry an explicit *Red flags* or *Caution* marker — as a new batch sub-section, as planning-subagent behaviour that detects security-shaped scope and surfaces a verbal heads-up at scoping time, or both?

**Why it matters.** Surfaced 2026-05-22, ideation session interrogating which V-file scope sections should propagate to consumer-project BACKLOG batches. Walking V-file *Risks / dependencies* as a candidate surfaced a conflation between *build-dependency risk* and *security/threat-class risk*. The interrogation resolved to land only dependency-tracking (as a peer to `Blocks:`) and explicitly scope *Risks* out — but the question of how the method should handle security-shaped warnings is now sitting unhandled. Today no doc has a dedicated carrier for "be paranoid about this part." The universal-behaviour flagging rule covers scope, not threat-class. The Suggestions/Discoveries taxonomy is mid-build observation, not pre-build warning.

**Working notes.** Three possible shapes:

1. **New BACKLOG batch sub-section** — *Red flags:* or *Caution:* line, populated at planning time when the batch's scope crosses a security-shaped surface.
2. **Planning-subagent automatic detection** — subagent identifies security-shaped scope (keyword/pattern triggers: `auth`, `password`, `token`, `secret`, `delete`, `payment`, etc.) and surfaces a verbal heads-up in the planning recap. No persistent doc carrier; the warning lives in the conversation.
3. **Both** — automatic detection at planning time plus persistence in the batch as a section.

**Next step.** **Folded into V49** (session v47, 2026-05-22). Red-flag marker bundled into V49's consumer-batch structure overhaul as a sixth batch section.

---

## Post-adopt and mid-loop UX friction (V42 smoke-test observations)

**The question.** The adopt → plan → before-build → build → test loop works mechanically, but seven UX friction points surfaced during V42's live smoke test that would frustrate a new non-coder user. Should any be addressed, and if so, how?

**Why it matters.** Surfaced 2026-05-21, V42 smoke test against `~\v42-scratch`. Alex walked the full loop as a user would. Each observation is a moment where the user would be stuck, confused, or doing unnecessary manual work.

**The seven items.**

1. ~~**Jargon in adopt subagent.**~~ **Resolved V44 (session v46, 2026-05-22).** "Scaffold" replaced with "create the method's starter docs" across all user-facing dialogue in `setup.md`.
2. ~~**No next-action prompt after `/setup`.**~~ **Resolved V44 (session v46, 2026-05-22).** All successful-path recaps in `setup.md` (cases 1, 2, 3) now close with guidance on how to start a planning session.
3. **Fold-in UX forces manual copy-paste.** The user must open a markdown file in a text editor, find the right section, paste content, and save — repeatedly. This is the single biggest friction point. Users with visual processing difficulties or unfamiliarity with markdown are especially penalised.
4. ~~**Claude Code's permission modes vs. the UX.md lock.**~~ **Resolved by V43 research (session v43, 2026-05-22).** PreToolUse hooks fire in all permission modes, including Auto and bypass — the method's lock is complementary to, not redundant with, Claude Code's permission system. Mode-aware deny messages shipped in V43.
5. **After-build doesn't prompt commit/tag.** After-build tells the user to "/clear and switch back to planning mode" but never mentions committing or tagging. The method recommends tagging (and drift check 1 depends on it), but the user isn't told.
6. **Template carries excessive placeholder content.** BACKLOG-TEMPLATE.md ships with multiple example batches using bracketed placeholders. When `/setup` writes BACKLOG.md, the diff shows a wall of red/green that obscures the real content. Consider stripping examples after real content is written.
7. ~~**"Pass / Fail / Skipped" not explained.**~~ **Resolved V44 (session v46, 2026-05-22).** Per-row read-back in `planning.md` now includes one-line explanation for each option.

**Relationship to existing entries.** Item 3 is adjacent to Distributed fold-ins + open questions section in BACKLOG (shipped V43, session v47) — distributed fold-ins restructure where fold-ins live but don't address the manual-paste UX.

**Next step.** Four of seven items resolved (1, 2, 4, 7). **Remaining items promoted in session v47 (2026-05-22):** item 3 (fold-in UX) bundled into V45; item 5 (after-build commit/tag prompt) bundled into V48; item 6 (template placeholder cleanup) bundled into V49. All seven items now scheduled or resolved.

---

## Six prose directives identified for pluginification

**The question.** An audit of sovereign-implementer's method docs against the current Claude Code plugin surface identified six rules currently enforced only by prose (Claude reads and follows them) that could become plugin automation. Should any or all be scheduled?

**Why it matters.** Surfaced 2026-05-21, ideation session. The plugin uses 3 of 18 available hook events (SessionStart, PreToolUse, Stop) and 1 of 5 hook types (command scripts). Six prose directives were identified where automation would reduce reliance on Claude reading and correctly applying rules from docs.

**The six items.**

1. **BACKLOG.md parse validation after edits.** PostToolUse hook runs `parse_backlog.py` after each BACKLOG.md edit and surfaces parse failures immediately, rather than silently returning `{}` when the Stop hook or `/build` tries to consume the output later. Rule source: implicit structural assumption across all subagents and the Stop hook.
2. **`Serves <DOC>:` validation for additional source-of-truth docs.** PreToolUse extension. Currently validates `Serves UX.md:` lines only. Consumer projects declaring additional docs in their CLAUDE.md path block get no validation on `Serves <DOC>:` lines. Rule source: DOC-STRUCTURE.md.
3. **Red flags non-empty warning at SessionStart.** SessionStart already reads BACKLOG.md — add a check for non-empty Red flags section and surface prominently. Rule source: DOC-STRUCTURE.md + universal-behaviour.md.
4. **Fold-in aging reminder.** Planning subagent scans `[FOLD-IN PENDING]` blocks for age (using existing `Surfaced [date]` field) and flags any older than 1–2 planning sessions. Rule source: DOC-STRUCTURE.md.
5. **Context preservation before compaction.** PreCompact hook injects a structured summary of current build state (which batch, ticked/unticked files, active subagent) so mid-build context survives compaction. Rule source: none — unaddressed risk not named in any doc.
6. **Opener routing classification.** UserPromptSubmit hook parses the user's first message, classifies it (test notes / feature request / resume / question), and injects the routing decision as structured context. Currently a prose table in universal-behaviour.md that Claude applies from reasoning alone. Rule source: universal-behaviour.md ("Routing main-Claude's openers").

**Relationship to existing build batches.** Checked against V42–V47: no overlap. V45 (distributed fold-ins) is adjacent to item 4 but doesn't address age tracking. None block a scheduled session.

**Full research.** `research/platform-capabilities-audit.md` (2026-05-21). Also catalogues unused hook events, unused hook types (prompt hooks, agent hooks), and platform capabilities (spawn_task, Claude Preview, mark_chapter, scheduled tasks) — reference material for future scoping, not actionable items.

**Next step.** **All six items promoted in session v47 (2026-05-22).** Item 1 (BACKLOG parse validation) → V46 (repurposed slot). Items 2, 3, 4 (Serves-DOC validation, Red flags warning, fold-in aging) → V54. Items 5, 6 (compaction context, opener routing) → V55. Scope files at `planning/sessions/V46.md`, `V54.md`, `V55.md`.

---

## Graduate sovereign implementer development onto sovereign implementer

**The question.** Can the no-code method's own development project switch from its bespoke dev environment (Vxx scope files, BUILD-METHOD.md, OPEN-QUESTIONS.md, two-write rule) to using the method's own plugin — dogfooding sovereign implementer to build sovereign implementer?

**Why it matters.** Surfaced 2026-05-21, discussion session. Dogfooding would surface gaps Taskflow can't (Taskflow only exercises the app-building path), and would validate the method for non-UI project types. The bespoke dev environment has served the project well but diverges from the method it's building — the longer the divergence persists, the more the method's design is informed by building apps rather than by building anything.

**Conclusion from discussion.** Yes, but staged. The current dev environment must ship the prerequisites first; the graduation itself is a managed transition, not a switch-flip.

**Prerequisites (all tracked as separate entries).**

1. **Distributed fold-ins + open questions section in BACKLOG** — **Shipped V43 (session v47, 2026-05-22).** Gave the method a parking lot for unresolved questions (open-questions section in BACKLOG.md) and restructured fold-in blocks to live in destination docs' own `## Fold-ins pending` sections. Includes the Inputs line for build batches.
2. **[[Automated vs. manual test split + non-UI test types]]** — **Promoted to V48 (renumbered V46 → V48 in session v43, 2026-05-22).** The primary blocker. The method's test model must accommodate run-and-read, trigger-and-observe, and generate-and-inspect test types, and support Claude-run automated tests. Without this, the build cycle can't verify plugin work.
3. **[[Shelve the two-write rule and prose-only canonical docs]]** — **Done in session v40, 2026-05-21.** Repo-root docs-only set frozen at V39; plugin side is sole operational source. Restoring two-write maintenance is one OPEN-QUESTIONS promotion away. Removes the maintenance burden that's specific to the current dev environment and has no method-level equivalent.
4. **[[UX.md adaptation for non-GUI projects]]** — **Promoted to V47 (renumbered V43 → V47 in session v43, 2026-05-22).** Vocabulary and doc structure changes so the method's language fits a plugin/method-spec project, not just UI apps.

**What doesn't need a prerequisite.** Vxx scope files → BACKLOG batches (the existing batch format already covers the Outputs half; the Inputs line covers the rest). BUILD-LOG.md narrative (already in the consumer method since V33).

**Next step.** **Promoted to V59** (session v47, 2026-05-22). Capstone session — all four prerequisites ship before V59. Scope file at `planning/sessions/V59.md`.

---

## Automated vs. manual test split + non-UI test types

**The question.** The method's after-build test model assumes the user manually verifies everything ("refresh, click through, report what you see"). But Claude Code can run many tests itself — anything with an objective pass/fail. Should the build cycle accommodate automated Claude-run tests alongside manual user-run tests, and should the method formally recognise test types beyond UI interaction?

**Why it matters.** Surfaced 2026-05-21, discussion session. Two compounding problems: (1) The after-build prompt and TEST-LOG row format are shaped around UI testing. Non-UI projects (CLI tools, plugins, APIs, document generators) can't use the test model as written. (2) Many tests — especially non-UI ones — have objective pass/fail criteria that Claude Code can verify without user involvement. The current model pushes ALL verification onto the user, including mechanical checks Claude could handle faster and more reliably. This is the single biggest blocker to using the method on its own development (dogfooding), where nearly all tests are "run a hook script, check the output."

**Four test types identified.** The method currently serves only the first.

1. **Look and click (UI interaction).** Open an app or website, interact, observe behaviour. Partially automatable (Claude Code's preview tool can screenshot and check structure), but subjective assessment stays with the user.
2. **Run and read (command execution).** Execute a command in the terminal, read the output. CLI tools, scripts, data pipelines. Fully automatable by Claude — run the command, check stdout/stderr against expected output.
3. **Trigger and observe (integration/trigger).** Do something that should cause the system to respond, verify it did. Plugins, hooks, webhooks, automations, scheduled tasks. Fully automatable by Claude — set up conditions, trigger, check response. This is the shape of sovereign implementer's own tests (run a hook with test input, verify the output).
4. **Generate and inspect (artifact inspection).** Run a process that produces a file, open the file and verify it. Reports, exports, spreadsheets, generated documents. Fully automatable by Claude — run the process, read the output file, check against expectations.

**Design questions to resolve.**

- **Where in the build cycle do automated tests run?** During the build (batch-executor tests as it goes), after the build (after-build runs an automated pass before prompting the user), or both?
- **TEST-LOG format.** Needs to track who verified each row (Claude vs. user) and what type of test was run. Current row format doesn't accommodate this.
- **After-build prompt language.** Currently assumes all testing is user-performed. Needs to distinguish: "Claude has already verified X; please manually check Y."
- **Test specification.** Where does the build batch specify what tests to run and which are automatable? An extension of the Inputs line, or a separate `Tests:` section per batch?

**Next step.** Promoted to V48 (renumbered V46 → V48 in session v43, 2026-05-22). Depends on V47 (non-GUI vocab settled) and V45 (Inputs line; per-batch test spec is the natural peer). After V48 ships, three of four prerequisites for [[Graduate sovereign implementer development onto sovereign implementer]] are done. **Promote sooner** only if dogfooding becomes urgent before V47 ships, since the test-type language would shadow-decide vocabulary that V47 owns.

---

## Bash `cd` inside a session shifts plugin cwd, breaking parent-folder opt-out marker

**The question.** During V39 dev work, a Bash command early in the session (`cd sovereign-implementer/ && git describe --tags --abbrev=0`) shifted Claude Code's session cwd from the parent `No code method/` folder to `sovereign-implementer/`. Subsequent PreToolUse hook invocations received `sovereign-implementer/` as `cwd`, and the V29 adoption gate's `has_opt_out_marker` check (which reads `<cwd>/.no-code-method-skip`) found nothing — the marker that opts out the dev project lives at the parent folder, not inside `sovereign-implementer/`. The gate started blocking every Edit. Workaround: write a second `.no-code-method-skip` at `sovereign-implementer/`. But the deeper question is whether the plugin should be resilient to `cd`-induced cwd drift mid-session.

**Why it matters.** Surfaced V39 mid-session, 2026-05-21. Three flavours of consequence:

1. **Dev-project ergonomics.** The no-code-method's own dev project sits at `No code method/` with the dev subtree at `sovereign-implementer/`. A single Bash `cd` (which Claude will reach for naturally — `git describe`, `git log`, anything subdir-scoped) can deadlock the session against the plugin's own gate. V39 had to recover from this mid-build.
2. **Consumer projects.** Any consumer who opts out via `.no-code-method-skip` at their project root would experience the same break if Claude `cd`s into a sub-folder. Less common (consumer projects are usually opened at the actual root), but possible — e.g. a monorepo with multiple sub-projects.
3. **Mental model.** Users (and Claude itself) reasonably expect the session's project to be the folder they opened, not whichever folder Bash last `cd`'d into. The plugin's current behaviour quietly diverges from that.

**Working notes.** Three shapes worth considering.

- **A. Marker-walk-up.** `has_opt_out_marker` walks from cwd upward to the filesystem root, looking for `.no-code-method-skip` at any ancestor. Smallest change; covers both monorepo sub-projects and the dev-project's cd-drift case. Risk: walking too far could pick up an unrelated opt-out marker (e.g. user has one at `~`). Mitigation: bound the walk by some marker (e.g. the first `.git/` ancestor, or the first ancestor with a `CLAUDE.md`).
- **B. Pin cwd at SessionStart.** SessionStart writes the resolved project root to a session-local cache (the existing transcript/session-id key); subsequent hooks read project_root from there rather than from each call's `cwd`. Eliminates cd drift entirely. Risk: cross-hook coordination via filesystem cache is a new mechanism with its own failure modes.
- **C. Document the gotcha, fix nothing.** Add to `BUILD-METHOD.md` and Crash course: "don't `cd` mid-session; if you must, place opt-out markers at every potential cwd." Cheapest. Pushes the burden onto users and Claude — drift will recur.

Leaning: **A (marker-walk-up, bounded by first `CLAUDE.md`-bearing or `.git/`-bearing ancestor)**. Cheap, covers both real cases (dev project + monorepo), and the bound keeps it from over-reaching into the user's home directory.

**Next step.** **Resolved — V44 removed the `.no-code-method-skip` marker architecture from the public plugin (session v46, 2026-05-22), making the walk-up fix moot.** Original V46 scope closed. The legacy `_LEGACY_SKIP_MARKER` in the dev project's `project_state.py` doesn't need a walk-up — it's a niche escape hatch for `--plugin-dir` users only. V46 slot repurposed for BACKLOG parse validation.

---

## Automated testing / CI for the method's dev project

**The question.** `BUILD-METHOD.md` → *Testing — what we actually do* asserts no automated CI: smoke tests are hand-run by Alex post-session, framed as deliberate — "CI's value is regression-catching across many simultaneous changes; this project ships one tag at a time with full attention." Should the decision be revisited as the plugin's surface grows, and if so, what shape of automation would earn its place?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. The "one tag at a time with full attention" framing assumes Alex hand-verifies everything. As the plugin surface grows, hand-verification scales linearly and becomes both more expensive and more error-prone. V25 and V27 each shipped with bugs that smoke tests caught after the fact; a more systematic pre-flight check might have caught some earlier. The trade-off is between manual-only discipline (defensible while the method is small and single-user) and introducing automation (defensible if the surface keeps growing).

**Working notes.** Three shapes worth considering.

- *Keep as-is.* Status quo. Defensible while the method spec is still churning. Cost: hand-verification scales with surface.
- *Hook-script direct-invocation suite.* Add a `tests/` directory at repo root with scripts that pipe fake hook input into each hook script and assert on stdout. Catches parser / arithmetic bugs pre-smoke-test. Doesn't catch Claude Code integration issues (those still need `--plugin-dir`). Low cost; partial coverage.
- *Fixture-driven integration suite.* Harness that spins up a fixture project, runs `claude --plugin-dir`, and asserts on resulting BACKLOG.md / TEST-LOG.md state. Highest fidelity; highest cost; brittle against Claude Code version changes.

**Next step.** **Promoted to V53** (session v47, 2026-05-22). Hook-script direct-invocation suite shape. Scope file at `planning/sessions/V53.md`.

---

## UX.md adaptation for non-GUI projects

**The question.** UX.md's structural rules (every entry corresponds to something the user can experience in the current build; the "the user needs this because..." line; user-facing rationale) are built around projects where the user has a UI. For non-GUI projects — CLI tools, backend services, data pipelines, MCP servers, scripts — "user experience" maps imperfectly: the "user" may be a developer integrating, an operator monitoring logs, or a downstream system; the "experience" is request/response, exit codes, file outputs, log lines. Does UX.md's structure adapt cleanly, or does the method need a non-GUI variant?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. The method-wide phrasing "user-observable behaviours" implies a visible UI; for non-GUI projects this either reads strangely or forces the no-coder to abstract their concrete deliverables into ill-fitting "user experiences." The same lean recurs in `NO-CODE-METHOD.md` (the *Pre-build verification estimate* Vocabulary entry, the *After every build* test-session-open step), `DOC-STRUCTURE.md`, and several subagent bodies. Taskflow (a native Android app) doesn't hit this; the method is meant to be general.

**Working notes.** Three shapes worth considering.

- *Generalise the vocabulary.* Replace "user-observable behaviours" with "observable outcomes" or "testable behaviours" across `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, subagent bodies, and Crash course. Lighter lift; doesn't change the structure. Cost: loses the "user" anchor that protects against feature drift.
- *Non-GUI variant of UX.md.* Add a section to `DOC-STRUCTURE.md` → *UX.md structure* explaining how non-GUI projects should shape their entries: name the "user" explicitly (operator, downstream system, integrating developer), let the "experience" be whatever they observe (logs, response, exit code, file). Heavier; clearer for non-GUI no-coders.
- *Separate spine doc for non-GUI projects.* A new template (BEHAVIOUR.md? CONTRACT.md? OUTPUTS.md?) replaces UX.md for non-GUI projects. Heaviest; risks fragmenting the method. Defer unless shapes 1 and 2 prove inadequate.

**Next step.** Promoted to V47 (renumbered from V40 → V41 → V42 → V43 → V47 across v40/v41/v43 sessions; 2026-05-22). Leaning: vocabulary generalisation + guidance section. Bundled with "planning" disambiguation to amortise the parity audit. **Promote sooner** if Alex (or any consumer) starts a non-GUI project with the method before V47 ships.

---

## TEST-LOG row pruning

**The question.** Should `TEST-LOG.md` gain an actual pruning mechanism (deletion-based) to bound the file's growth? Current rule (`DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule*): rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically over a project's life.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Drift check 5 (retest after change — `plugin/agents/planning.md` → *Drift checks — always run*) walks every Pass-confirmed row to judge whether its component has been touched. As a project ages, this scales linearly with batches shipped. Real context cost. Counter-argument: audit trail value — "passed at the time" is worth keeping; deletion risks losing the trail.

**Working notes.** Three approaches worth weighing.

- Time-based: drop Superseded rows older than N versions.
- Component-based: drop rows whose component no longer exists in `MANIFEST.md`.
- Manual: an explicit per-planning-session option to archive rows to an external file (preserving audit, removing from context).

**Next step.** **Promoted to V56** (session v47, 2026-05-22). Scope file at `planning/sessions/V56.md`.

---

## "Planning" vocabulary collision with Claude Code's "plan mode"

**The question.** The method uses "planning" as a lifecycle phase name (planning session, planning subagent, planning batch, the planning phase). Claude Code uses "plan mode" for a built-in feature (Shift+Tab toggle that blocks file edits). The two are different concepts the no-coder must distinguish. Should the method's "planning" vocabulary be renamed to remove the ambiguity, or is a vocabulary disambiguation in the docs sufficient?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. A new reader of the Crash course reads "planning session" and may map it to Claude Code's "plan mode" — misleading because the method's planning session involves editing `BACKLOG.md` (incompatible with plan mode). Worse, plan mode is recommended at two specific moments in the method (pre-method app-idea exploration; before-build batch review), creating a third axis of "planning"-flavoured activity to track.

**Working notes.** Three shapes worth considering.

- **Rename the method's "planning" phase.** Candidates: "design session," "spec session," "decision session." The subagent renames accordingly (`no-code-method:design`?). Heavy lift — every doc, template, subagent body, INVENTORY entry. Lots of footer-bump and parity-audit surface.
- **Vocabulary disambiguation in docs.** Add an explicit "not to be confused with plan mode" note to `NO-CODE-METHOD.md` → *Vocabulary*. Mention in Crash course where plan mode comes up. Low-cost; relies on the reader.
- **Hybrid.** Keep "planning phase" as the lifecycle name but rename the subagent (`no-code-method:planning` → `no-code-method:design`) so the plugin-component name reads distinct. Compromise.

**Next step.** Promoted to V47 (renumbered from V40 → V41 → V42 → V43 → V47 across v40/v41/v43 sessions; 2026-05-22). Bundled with non-GUI generalisation to amortise the parity audit. **Promote sooner** if first real Taskflow use surfaces the confusion before V47.

---

## Subagent rule-loading pattern divergence — inline vs. read-spec-on-entry

**The question.** Subagents currently use two patterns:

- **`planning.md` (V22)** and **`before-build.md` (V25)** read `NO-CODE-METHOD.md` (and `DOC-STRUCTURE.md` where relevant) at session start. Agent body holds operational notes only.
- **`batch-executor.md` (V25)** has rules inlined. No runtime spec read. Per V25 Decision 4.

Inline drifts silently if the spec is updated and the agent body isn't. Read-spec-on-entry picks up spec changes automatically but adds prompt-time read overhead. Converge, or document the divergence?

**Why it matters.** Surfaced during V25 before-build design. Original draft proposed inline (matching batch-executor) on the framing "before-build is mechanical, like batch-executor." Review reframed it as **stable vs. fresh rules**: batch-executor inlined rules unchanged for many versions, whereas before-build's load-bearing rules were V25-introduced and likely to churn. Same reasoning applies to batch-executor's V25-fresh content (Two-exceptions framing, Files: sub-section consumption) — but it just shipped and was tested, so flipping it in V25 would churn settled code.

**Working notes.** Three positions:

- **A. Converge on read-spec-on-entry.** Flip batch-executor. Parity drift becomes impossible. Cost: prompt-time overhead (4 docs) per batch-executor invocation; refactor on code that just landed.
- **B. Converge on inline.** Flip planning and before-build. Drops the read overhead. Cost: doc-code parity audit becomes primary discipline against drift; cadence needs formalising in `BUILD-METHOD.md`.
- **C. Keep the divergence; document the rule.** Stable rules go inline; evolving rules read-spec-on-entry. Re-evaluate per agent per version. Cost: new internal classification to maintain.

**Next step.** **Promoted to V57** (session v47, 2026-05-22). Direction decided at session start based on spec stability across V45–V56. Scope file at `planning/sessions/V57.md`.

**V37, 2026-05-21: targets shifted, tension unchanged.** V32's two-write rule moved the runtime spec targets from `NO-CODE-METHOD.md` to `plugin/docs/DOC-STRUCTURE.md` and `plugin/docs/VOCABULARY.md`; `adopt.md` joins `planning.md` and `before-build.md` as a read-at-entry subagent. The underlying inline-vs-read-at-entry question is the same shape, just against the new targets. Stays parked at the same threshold: promote if `plugin/docs/` churns enough (or stabilises enough) to make convergence the obviously right call, or if a parity audit flags meaningful drift in `batch-executor.md`.

---

## Track session performance over time? (AEX-style DEX/HEX)

**The question.** Should a future version include a lightweight session-performance log — configuration used (model, prompts, hooks, skills) plus structured assessment of how the session went — so method decisions rest on evidence rather than instinct? Borrowed from AEX (github.com/ctenidae8/AEX_Protocol): **DEX** = per-config reliability score from logged outcomes; **HEX** = per-config record of what tasks the config has proven good at.

**Why it matters.** Raised externally via conversation + distilled-question artifact (V19 chat; share-link content unretrievable). Worth recording because it points at a real long-term tension: the method develops session-by-session, decisions made on first-principles intuition. Public-scale aggregated evidence has obvious value. Single-user evidence against an evolving method — useful, or premature noise?

**Working notes — honest assessment from V19.**

1. *Method isn't stable yet.* V19 of ~27 planned sessions plus refinement. Measuring an evolving system captures noise about its evolution, not signal about its working state. Stabilise first, then decide what to measure.

2. *Sample size is unworkable.* One person, one project, ~30 sessions through V27 — even fully logged, variables are confounded ("did the method work?" tangles with "was Alex sharp today?" and "was the task tractable?"). Signal-to-noise per decision is low.

3. *Defining "went well" is the hardest part, and the artifact says so itself.* Without a mechanical success criterion, "well" becomes vibes-encoded-as-data — worse than vibes, because numeric scores feel objective when they aren't.

4. *Existing retrospective mechanisms already cover this qualitatively.* `BUILD-LOG.md` captures what shipped, decisions, surprises, carry-forwards. `OPEN-QUESTIONS.md` captures unresolved tensions. Discoveries → planning batches captures emergent needs. These fit small-sample, single-user, evolving-method conditions. If insufficient later, cheaper incremental move is structured fields in BUILD-LOG entries ("what worked / what didn't / hypothesis for next time"), not a separate measurement system.

5. *What current decision would this change?* V17's architecture, V18's hook-event choice, V19's hook-deny-redirect mechanic — none would have been called differently with a session-performance log. The artifact's own bar is "does the evidence change my decisions?" From V19's vantage, no.

6. *Where the idea earns its keep eventually.* If the method goes public (course revival, published plugin with consumers), aggregated cross-user session data is genuinely valuable — AEX/DEX/HEX are designed for that scale. Single-user, in-development is the wrong scale.

**Next step.** **Promoted to V58** (session v47, 2026-05-22). Scope file at `planning/sessions/V58.md`. Focus on mechanical measures (regression count, intervention count, turn count) to avoid vibes-as-data.

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and `[FOLD-IN PENDING]` rely on Claude Code primitives. For users wanting the method's discipline in plain chat with Claude, another AI tool, or any context where the plugin shape doesn't fit, we'll eventually need a tool-agnostic prose-only rewrite.

**Why it matters.** Surfaced V20 planning. Without the rewrite, the method is structurally bound to Claude Code: locking via PreToolUse, session-start reads via SessionStart, routing via injected context. None exist elsewhere. Users without Claude Code can't run the method as a working system. Prose-only restores accessibility — but only after the plugin shape stabilises, or the rewrite chases a moving target.

**Working notes.**

- Likely shape: prose-only `NO-CODE-METHOD.md` re-expressing every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart foundational reads (becomes at-session-start narrative in `CLAUDE.md`), PreToolUse locking (trust-based convention + chat-time flagging), slash commands (operational procedures in prose).
- Plugin still evolving (V32–V35 ahead). Rewriting before it settles means redoing.

**V37, 2026-05-21: rewrite delivered by V32; entry overtaken.** V32's two-write rule split canonical method content into plugin-side (operational) and docs-only (project-agnostic) artefact sets. The docs-only side at the repo root — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/` — is the prose-only rewrite this entry called for. Ongoing parity is held by the two-write discipline (`BUILD-METHOD.md` → *Two-write rule for canonical docs*), not by a future rewrite session.

**Next step.** **Indefinitely parked** (session v47, 2026-05-22). Kept as last entry in OPEN-QUESTIONS. Promote if a real audience for the prose-only set emerges (public release, non-Claude-Code users).
