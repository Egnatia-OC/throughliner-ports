# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

---

## Post-adopt and mid-loop UX friction (V42 smoke-test observations)

**The question.** The adopt → plan → before-build → build → test loop works mechanically, but seven UX friction points surfaced during V42's live smoke test that would frustrate a new non-coder user. Should any be addressed, and if so, how?

**Why it matters.** Surfaced 2026-05-21, V42 smoke test against `~\v42-scratch`. Alex walked the full loop as a user would. Each observation is a moment where the user would be stuck, confused, or doing unnecessary manual work.

**The seven items.**

1. **Jargon in adopt subagent.** `/adopt` says "One more, then I'll scaffold" — "scaffold" is jargon. Should say something like "create your project's starter docs." Violates the universal-behaviour "Plain English over jargon" rule.
2. **No next-action prompt after `/adopt`.** Adopt finishes by telling the user to fold pending blocks into UX.md "during the next planning session" but doesn't say how to start one. A new user would be stuck at the prompt with no idea what to type.
3. **Fold-in UX forces manual copy-paste.** The user must open a markdown file in a text editor, find the right section, paste content, and save — repeatedly. This is the single biggest friction point. Users with visual processing difficulties or unfamiliarity with markdown are especially penalised.
4. **Claude Code's permission modes vs. the UX.md lock.** Claude Code has its own graduated permission model (Ask permissions → Accept edits → Auto mode). The method's UX.md lock is a second, harsher layer on top. Research needed: does the plugin's PreToolUse hook fire regardless of which Claude Code mode is active? If the mode already provides the safety guarantee, the manual fold-in may be unnecessary.
5. **After-build doesn't prompt commit/tag.** After-build tells the user to "/clear and switch back to planning mode" but never mentions committing or tagging. The method recommends tagging (and drift check 1 depends on it), but the user isn't told.
6. **Template carries excessive placeholder content.** BACKLOG-TEMPLATE.md ships with multiple example batches using bracketed placeholders. When `/adopt` writes BACKLOG.md, the diff shows a wall of red/green that obscures the real content. Consider stripping examples after real content is written.
7. **"Pass / Fail / Skipped" not explained.** TEST-LOG read-back asks "Pass, Fail, or Skipped?" with no context for what each means or when to use which. A one-line explanation per option would help.

**Relationship to existing entries.** Item 3 is adjacent to [[Distributed fold-ins + open questions section in BACKLOG]] (V45) — distributed fold-ins restructure where fold-ins live but don't address the manual-paste UX. Item 4 is new research with no existing entry. Items 1, 2, 5, 6, 7 are subagent/template fixes that could land independently.

**Next step.** Bring to V43 planning. Items 1, 2, 5, 6, 7 are small fixes that could bundle into a build batch. Item 4 needs empirical research (test PreToolUse under different Claude Code modes). Item 3 is a larger design question that may feed into or follow V45.

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

**Next step.** Park. Revisit after V45 ships (fold-in restructuring may change item 4's shape; BACKLOG.md structural changes may affect item 1's hook target). Items are independent of each other and can be promoted individually. **Promote sooner** if a consumer project hits a routing misclassification (item 6), a silent BACKLOG parse failure (item 1), or a compaction-loses-build-state incident (item 5) — those are the three with the highest consequence-of-inaction.

---

## Graduate sovereign implementer development onto sovereign implementer

**The question.** Can the no-code method's own development project switch from its bespoke dev environment (Vxx scope files, BUILD-METHOD.md, OPEN-QUESTIONS.md, two-write rule) to using the method's own plugin — dogfooding sovereign implementer to build sovereign implementer?

**Why it matters.** Surfaced 2026-05-21, discussion session. Dogfooding would surface gaps Taskflow can't (Taskflow only exercises the app-building path), and would validate the method for non-UI project types. The bespoke dev environment has served the project well but diverges from the method it's building — the longer the divergence persists, the more the method's design is informed by building apps rather than by building anything.

**Conclusion from discussion.** Yes, but staged. The current dev environment must ship the prerequisites first; the graduation itself is a managed transition, not a switch-flip.

**Prerequisites (all tracked as separate entries).**

1. **[[Distributed fold-ins + open questions section in BACKLOG]]** — **Promoted to V45 (session v41, 2026-05-21).** Gives the method a parking lot for unresolved questions (replaces this project's bespoke OPEN-QUESTIONS.md) and restructures BACKLOG.md. Includes the Inputs line for build batches (replaces Vxx Inputs sections).
2. **[[Automated vs. manual test split + non-UI test types]]** — **Promoted to V46 (session v41, 2026-05-21).** The primary blocker. The method's test model must accommodate run-and-read, trigger-and-observe, and generate-and-inspect test types, and support Claude-run automated tests. Without this, the build cycle can't verify plugin work.
3. **[[Shelve the two-write rule and prose-only canonical docs]]** — **Done in session v40, 2026-05-21.** Repo-root docs-only set frozen at V39; plugin side is sole operational source. Restoring two-write maintenance is one OPEN-QUESTIONS promotion away. Removes the maintenance burden that's specific to the current dev environment and has no method-level equivalent.
4. **[[UX.md adaptation for non-GUI projects]]** — **Promoted to V43 (renumbered from V40 → V41 → V42 → V43 across v40/v41 sessions).** Vocabulary and doc structure changes so the method's language fits a plugin/method-spec project, not just UI apps.

**What doesn't need a prerequisite.** Vxx scope files → BACKLOG batches (the existing batch format already covers the Outputs half; the Inputs line covers the rest). BUILD-LOG.md narrative (already in the consumer method since V33).

**Next step.** Park. This entry is the meta-goal; the prerequisites have their own promotion triggers. As of session v41 (2026-05-21), all four prerequisites have been scheduled (V43 vocab, V45 fold-ins, V46 test split; #3 already done in v40) and after V46 ships, graduation becomes promotable on its own evaluation. Graduate when all four prerequisites have shipped and been verified in at least one build cycle. **Promote sooner** if an external reason (public release, new contributor) makes dogfooding urgent before all prerequisites land.

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

**Next step.** Promoted to V46 (session v41, 2026-05-21). Depends on V43 (non-GUI vocab settled) and V45 (Inputs line; per-batch test spec is the natural peer). After V46 ships, three of four prerequisites for [[Graduate sovereign implementer development onto sovereign implementer]] are done. **Promote sooner** only if dogfooding becomes urgent before V43 ships, since the test-type language would shadow-decide vocabulary that V43 owns.

---

## Distributed fold-ins + open questions section in BACKLOG

**The question.** Should fold-ins move from a centralised section in BACKLOG.md to the bottom of each destination doc (UX.md, MANIFEST.md, BACKLOG.md itself), and should BACKLOG.md gain an open-questions section scanned during planning?

**Why it matters.** Surfaced 2026-05-21, discussion session. Two related design problems: (1) BACKLOG.md currently houses source-of-truth content destined for other docs (UX.md entries, MANIFEST.md entries) alongside build batches — semantically wrong, since BACKLOG is about what gets built, not about parking SOT content for unrelated docs. (2) The method has no parking lot for unresolved questions that aren't blocking a specific build batch. This project's own OPEN-QUESTIONS.md has been load-bearing (10 entries with trigger conditions), but consumer projects have no equivalent.

**Design so far.**

- Each spine doc gains a fold-in section at its bottom. Claude appends proposed content there; the user folds it into the main body during planning. Content lives next to its destination instead of being routed through BACKLOG.
- Locked docs (UX.md, MANIFEST.md) need an **append-only carve-out** in PreToolUse — same pattern as V38's footer-stamp carve-out (`is_footer_only_edit()`), but for appending to the fold-in section.
- BACKLOG.md structure becomes: Red flags → Build batches → BACKLOG-specific fold-ins (resolved features not yet batched) → Open questions.
- Open questions are scanned by the planning subagent during its existing drift-check sweep at the top of every planning session — not left to chance.
- Planning batches (the current `Blocks:` mechanism) — relationship to the new open-questions section not yet resolved. May merge, may coexist.
- **Inputs line for build batches.** Each batch gains an `Inputs:` line listing non-standard reads specific to that batch — an OPEN-QUESTIONS entry, a specific additional doc, a research artifact, an external reference. Foundational docs (UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md) are already read every session by SessionStart, so `Inputs:` only lists what's beyond the standard set. Closes the gap left by Vxx scope files' Inputs sections: without it, Claude has to guess what to read before starting a batch.

**Next step.** Promoted to V45 (session v41, 2026-05-21). Placed ahead of V46 because V46 (test split) needs both the open-questions section as a parking lot for between-session design decisions and the `Inputs:` line as the natural carrier for per-batch test specs. Prerequisite #1 for [[Graduate sovereign implementer development onto sovereign implementer]]. **Promote sooner** only if real Taskflow use surfaces the "nowhere to park unresolved questions" gap before V42–V44 ship.

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

**Next step.** Promoted to V47 (session v41, 2026-05-21). Decisions pre-made (shape A marker-walk-up, bounded by first `CLAUDE.md`/`.git/`-bearing ancestor); shapes B and C rejected. Smallest of V45–V47. **Promote sooner** only if a consumer hits this in normal use, OR if V42's git-diff drift detection trips the dev project again before V47 ships.

---

## Automated testing / CI for the method's dev project

**The question.** `BUILD-METHOD.md` → *Testing — what we actually do* asserts no automated CI: smoke tests are hand-run by Alex post-session, framed as deliberate — "CI's value is regression-catching across many simultaneous changes; this project ships one tag at a time with full attention." Should the decision be revisited as the plugin's surface grows, and if so, what shape of automation would earn its place?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. The "one tag at a time with full attention" framing assumes Alex hand-verifies everything. As the plugin surface grows, hand-verification scales linearly and becomes both more expensive and more error-prone. V25 and V27 each shipped with bugs that smoke tests caught after the fact; a more systematic pre-flight check might have caught some earlier. The trade-off is between manual-only discipline (defensible while the method is small and single-user) and introducing automation (defensible if the surface keeps growing).

**Working notes.** Three shapes worth considering.

- *Keep as-is.* Status quo. Defensible while the method spec is still churning. Cost: hand-verification scales with surface.
- *Hook-script direct-invocation suite.* Add a `tests/` directory at repo root with scripts that pipe fake hook input into each hook script and assert on stdout. Catches parser / arithmetic bugs pre-smoke-test. Doesn't catch Claude Code integration issues (those still need `--plugin-dir`). Low cost; partial coverage.
- *Fixture-driven integration suite.* Harness that spins up a fixture project, runs `claude --plugin-dir`, and asserts on resulting BACKLOG.md / TEST-LOG.md state. Highest fidelity; highest cost; brittle against Claude Code version changes.

**Next step.** Park. Revisit when (a) the plugin surface stabilises post-V35 E2E test, or (b) a regression slips through hand-verification that automation would have caught. **Promote sooner** if hand-verification scaling becomes a real bottleneck.

---

## UX.md adaptation for non-GUI projects

**The question.** UX.md's structural rules (every entry corresponds to something the user can experience in the current build; the "the user needs this because..." line; user-facing rationale) are built around projects where the user has a UI. For non-GUI projects — CLI tools, backend services, data pipelines, MCP servers, scripts — "user experience" maps imperfectly: the "user" may be a developer integrating, an operator monitoring logs, or a downstream system; the "experience" is request/response, exit codes, file outputs, log lines. Does UX.md's structure adapt cleanly, or does the method need a non-GUI variant?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. The method-wide phrasing "user-observable behaviours" implies a visible UI; for non-GUI projects this either reads strangely or forces the no-coder to abstract their concrete deliverables into ill-fitting "user experiences." The same lean recurs in `NO-CODE-METHOD.md` (the *Pre-build verification estimate* Vocabulary entry, the *After every build* test-session-open step), `DOC-STRUCTURE.md`, and several subagent bodies. Taskflow (a native Android app) doesn't hit this; the method is meant to be general.

**Working notes.** Three shapes worth considering.

- *Generalise the vocabulary.* Replace "user-observable behaviours" with "observable outcomes" or "testable behaviours" across `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, subagent bodies, and Crash course. Lighter lift; doesn't change the structure. Cost: loses the "user" anchor that protects against feature drift.
- *Non-GUI variant of UX.md.* Add a section to `DOC-STRUCTURE.md` → *UX.md structure* explaining how non-GUI projects should shape their entries: name the "user" explicitly (operator, downstream system, integrating developer), let the "experience" be whatever they observe (logs, response, exit code, file). Heavier; clearer for non-GUI no-coders.
- *Separate spine doc for non-GUI projects.* A new template (BEHAVIOUR.md? CONTRACT.md? OUTPUTS.md?) replaces UX.md for non-GUI projects. Heaviest; risks fragmenting the method. Defer unless shapes 1 and 2 prove inadequate.

**Next step.** Promoted to V43 (renumbered from V40 → V41 → V42 → V43 across v40/v41 sessions; 2026-05-21). Leaning: vocabulary generalisation + guidance section. Bundled with "planning" disambiguation to amortise the parity audit. **Promote sooner** if Alex (or any consumer) starts a non-GUI project with the method before V43 ships.

---

## TEST-LOG row pruning

**The question.** Should `TEST-LOG.md` gain an actual pruning mechanism (deletion-based) to bound the file's growth? Current rule (`DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule*): rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically over a project's life.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Drift check 5 (retest after change — `plugin/agents/planning.md` → *Drift checks — always run*) walks every Pass-confirmed row to judge whether its component has been touched. As a project ages, this scales linearly with batches shipped. Real context cost. Counter-argument: audit trail value — "passed at the time" is worth keeping; deletion risks losing the trail.

**Working notes.** Three approaches worth weighing.

- Time-based: drop Superseded rows older than N versions.
- Component-based: drop rows whose component no longer exists in `MANIFEST.md`.
- Manual: an explicit per-planning-session option to archive rows to an external file (preserving audit, removing from context).

**Next step.** **V34, 2026-05-21: unpaired from [[TEST-LOG ordering — newest at top vs bottom]] after V36 promotion.** Ordering doesn't need real row-count data and ships in V36; pruning still does. Fold into a V37+ planning session post-V35 once Taskflow's TEST-LOG.md has enough rows to inform the cutoff rule — likely after several batches have shipped through real use. **Promote sooner** if Taskflow's TEST-LOG.md crosses a meaningful row count before V37 — would benefit from real data first.

---

## "Planning" vocabulary collision with Claude Code's "plan mode"

**The question.** The method uses "planning" as a lifecycle phase name (planning session, planning subagent, planning batch, the planning phase). Claude Code uses "plan mode" for a built-in feature (Shift+Tab toggle that blocks file edits). The two are different concepts the no-coder must distinguish. Should the method's "planning" vocabulary be renamed to remove the ambiguity, or is a vocabulary disambiguation in the docs sufficient?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. A new reader of the Crash course reads "planning session" and may map it to Claude Code's "plan mode" — misleading because the method's planning session involves editing `BACKLOG.md` (incompatible with plan mode). Worse, plan mode is recommended at two specific moments in the method (pre-method app-idea exploration; before-build batch review), creating a third axis of "planning"-flavoured activity to track.

**Working notes.** Three shapes worth considering.

- **Rename the method's "planning" phase.** Candidates: "design session," "spec session," "decision session." The subagent renames accordingly (`no-code-method:design`?). Heavy lift — every doc, template, subagent body, INVENTORY entry. Lots of footer-bump and parity-audit surface.
- **Vocabulary disambiguation in docs.** Add an explicit "not to be confused with plan mode" note to `NO-CODE-METHOD.md` → *Vocabulary*. Mention in Crash course where plan mode comes up. Low-cost; relies on the reader.
- **Hybrid.** Keep "planning phase" as the lifecycle name but rename the subagent (`no-code-method:planning` → `no-code-method:design`) so the plugin-component name reads distinct. Compromise.

**Next step.** Promoted to V43 (renumbered from V40 → V41 → V42 → V43 across v40/v41 sessions; 2026-05-21). Bundled with non-GUI generalisation to amortise the parity audit. **Promote sooner** if first real Taskflow use surfaces the confusion before V43.

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

**Next step.** Park. Revisit once V26–V35 ship and the rate of `NO-CODE-METHOD.md` changes (or its post-V32 successor location) settles. If the spec is stable across consecutive versions, B is fine; if it churns, A; mixed, C. **Promote sooner** if an audit flags meaningful drift in `batch-executor.md`, which forces A.

**V37, 2026-05-21: targets shifted, tension unchanged.** V32's two-write rule moved the runtime spec targets from `NO-CODE-METHOD.md` to `plugin/docs/DOC-STRUCTURE.md` and `plugin/docs/VOCABULARY.md`; `adopt.md` joins `planning.md` and `before-build.md` as a read-at-entry subagent. The underlying inline-vs-read-at-entry question is the same shape, just against the new targets. Stays parked at the same threshold: promote if `plugin/docs/` churns enough (or stabilises enough) to make convergence the obviously right call, or if a parity audit flags meaningful drift in `batch-executor.md`.

---

## Stop-hook 8-block cap — only matters if we move to multi-batch-per-turn chains

**The question.** Claude Code's Stop hook caps at 8 consecutive blocks per user turn; the 9th ends the turn with a warning regardless. Override via `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`. Does the plugin need defensive design against this, or does our `stop_hook_active`-respecting design make the cap inert?

**Why it matters.** Surfaced V25 while wiring the Stop hook for auto-continuation. The cap would bite if a user turn produced 9+ redirects back-to-back.

**Working notes.** V25's Stop hook respects `stop_hook_active` and redirects at most once per user turn (V25 success criterion: explicit user gating between batches). Chain length is always 1; the cap can't trigger. It would only matter in a future workflow that drops the `stop_hook_active` check — where the 8-cap becomes a useful guardrail for the right reasons. No defensive code in V25.

**Next step.** Park. Revisit if a future session proposes multi-batch-per-turn auto-continuation (no current PLAN.md row). **Promote sooner** if a consumer hits the cap in normal use — that means `stop_hook_active` isn't doing what we think.

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and `[FOLD-IN PENDING]` rely on Claude Code primitives. For users wanting the method's discipline in plain chat with Claude, another AI tool, or any context where the plugin shape doesn't fit, we'll eventually need a tool-agnostic prose-only rewrite.

**Why it matters.** Surfaced V20 planning. Without the rewrite, the method is structurally bound to Claude Code: locking via PreToolUse, session-start reads via SessionStart, routing via injected context. None exist elsewhere. Users without Claude Code can't run the method as a working system. Prose-only restores accessibility — but only after the plugin shape stabilises, or the rewrite chases a moving target.

**Working notes.**

- Likely shape: prose-only `NO-CODE-METHOD.md` re-expressing every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart foundational reads (becomes at-session-start narrative in `CLAUDE.md`), PreToolUse locking (trust-based convention + chat-time flagging), slash commands (operational procedures in prose).
- Plugin still evolving (V32–V35 ahead). Rewriting before it settles means redoing.

**Next step.** Park until V35 (final E2E Taskflow test) ships. Then: list each plugin-specific mechanism, design a prose-only equivalent, schedule sessions. **Promote sooner** if public release approaches before migration completes — that scenario forces the rewrite onto the critical path.

**V37, 2026-05-21: rewrite delivered by V32; entry overtaken.** V32's two-write rule split canonical method content into plugin-side (operational) and docs-only (project-agnostic) artefact sets. The docs-only side at the repo root — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/` — is the prose-only rewrite this entry called for. Ongoing parity is held by the two-write discipline (`BUILD-METHOD.md` → *Two-write rule for canonical docs*), not by a future rewrite session. **Revised next step:** consciously drop with a one-line `BUILD-LOG.md` note pointing at V32. A future major prose-only sweep, if ever needed (e.g. ahead of a public release), will earn its own session driven by concrete need rather than this parked entry.

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

**Next step.** Park. Revisit after V35 ships and the method has settled into stable use across a few real project cycles. The question then becomes concrete: list 2–3 design decisions that would have benefited from logged evidence — if non-empty, define a minimal log against them; if empty, drop and record the reasoning in `BUILD-LOG.md`. **Promote sooner** if the method moves toward public release before V35 wraps.
