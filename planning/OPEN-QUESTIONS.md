# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, scope file in `sessions/`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

---

## Red-flag / threat-class marker for security-shaped batches

**The question.** Should BACKLOG batches that touch security-shaped surfaces (auth, secrets, PII, deletion of user data, third-party API keys) carry an explicit *Red flags* or *Caution* marker — as a new batch sub-section, as planning-subagent behaviour that detects security-shaped scope and surfaces a verbal heads-up at scoping time, or both?

**Why it matters.** Surfaced 2026-05-22, ideation session interrogating which V-file scope sections should propagate to consumer-project BACKLOG batches. Walking V-file *Risks / dependencies* as a candidate surfaced a conflation between *build-dependency risk* and *security/threat-class risk*. The interrogation resolved to land only dependency-tracking (as a peer to `Blocks:`) and explicitly scope *Risks* out — but the question of how the method should handle security-shaped warnings is now sitting unhandled. Today no doc has a dedicated carrier for "be paranoid about this part." The universal-behaviour flagging rule covers scope, not threat-class. The Suggestions/Discoveries taxonomy is mid-build observation, not pre-build warning.

**Working notes.** Three possible shapes:

1. **New BACKLOG batch sub-section** — *Red flags:* or *Caution:* line, populated at planning time when the batch's scope crosses a security-shaped surface.
2. **Planning-subagent automatic detection** — subagent identifies security-shaped scope (keyword/pattern triggers: `auth`, `password`, `token`, `secret`, `delete`, `payment`, etc.) and surfaces a verbal heads-up in the planning recap. No persistent doc carrier; the warning lives in the conversation.
3. **Both** — automatic detection at planning time plus persistence in the batch as a section.

**Next step.** **Partially shipped V47 (session v51, 2026-05-22).** Batch-level Red flags sub-section shipped as part of V49's consumer-batch structure overhaul — planning subagent auto-detects security-shaped scope and writes a persistent Red flags section into the batch. The remaining half (threat-class marker on UX.md entries) is unscheduled.

---

## Post-adopt and mid-loop UX friction (V42 smoke-test observations)

**The question.** The adopt → plan → before-build → build → test loop works mechanically, but seven UX friction points surfaced during V42's live smoke test that would frustrate a new non-coder user. Should any be addressed, and if so, how?

**Why it matters.** Surfaced 2026-05-21, V42 smoke test against `~\v42-scratch`. Alex walked the full loop as a user would. Each observation is a moment where the user would be stuck, confused, or doing unnecessary manual work.

**The seven items.**

1. ~~**Jargon in adopt subagent.**~~ **Resolved V44 (session v46, 2026-05-22).** "Scaffold" replaced with "create the method's starter docs" across all user-facing dialogue in `setup.md`.
2. ~~**No next-action prompt after `/setup`.**~~ **Resolved V44 (session v46, 2026-05-22).** All successful-path recaps in `setup.md` (cases 1, 2, 3) now close with guidance on how to start a planning session.
3. **Proposed-edit UX forces manual copy-paste.** The user must open a markdown file in a text editor, find the right section, paste content, and save — repeatedly. This is the single biggest friction point. Users with visual processing difficulties or unfamiliarity with markdown are especially penalised.
4. ~~**Claude Code's permission modes vs. the UX.md lock.**~~ **Resolved by V43 research (session v43, 2026-05-22).** PreToolUse hooks fire in all permission modes, including Auto and bypass — the method's lock is complementary to, not redundant with, Claude Code's permission system. Mode-aware deny messages shipped in V43.
5. ~~**After-build doesn't prompt commit/tag.**~~ **Resolved V46 (session v50, 2026-05-22).** After-build closing sequence now prompts commit/tag before the /clear prompt.
6. ~~**Template carries excessive placeholder content.**~~ **Resolved V47 (session v51, 2026-05-22).** BACKLOG-TEMPLATE's example batches replaced with HTML-comment format specs (matching TEST-LOG-TEMPLATE and MANIFEST-TEMPLATE pattern).
7. ~~**"Pass / Fail / Skipped" not explained.**~~ **Resolved V44 (session v46, 2026-05-22).** Per-row read-back in `planning.md` now includes one-line explanation for each option.

**Relationship to existing entries.** Item 3 is adjacent to Distributed fold-ins + open questions section in BACKLOG (shipped V43, session v47) — distributed fold-ins restructure where fold-ins live but don't address the manual-paste UX.

**Next step.** Six of seven items resolved (1, 2, 4, 5, 6, 7). **Remaining item:** item 3 (proposed-edit UX) bundled into V45, promoted in session v47.

---

## Six prose directives identified for pluginification

**The question.** An audit of sovereign-implementer's method docs against the current Claude Code plugin surface identified six rules currently enforced only by prose (Claude reads and follows them) that could become plugin automation. Should any or all be scheduled?

**Why it matters.** Surfaced 2026-05-21, ideation session. The plugin uses 4 of 18 available hook events (SessionStart, PreToolUse, PostToolUse, Stop) and 1 of 5 hook types (command scripts). Six prose directives were identified where automation would reduce reliance on Claude reading and correctly applying rules from docs.

**The six items.**

1. ~~**BACKLOG.md parse validation after edits.**~~ **Shipped V44 (session v48, 2026-05-22).** PostToolUse hook at `plugin/hooks/post_tool_use.py`. Fires after Edit/Write/MultiEdit on BACKLOG.md; imports `find_top_unticked_batch` directly; surfaces `additionalContext` warning when unticked file bullets exist but the parser returns `{}`.
2. **`Serves <DOC>:` validation for additional source-of-truth docs.** PreToolUse extension. Currently validates `Serves UX.md:` lines only. Consumer projects declaring additional docs in their CLAUDE.md path block get no validation on `Serves <DOC>:` lines. Rule source: DOC-STRUCTURE.md.
3. **Red flags non-empty warning at SessionStart.** SessionStart already reads BACKLOG.md — add a check for non-empty Red flags section and surface prominently. Rule source: DOC-STRUCTURE.md + universal-behaviour.md.
4. **Deferred build-material aging.** Planning subagent detects BACKLOG items whose origin batch number is behind the current front and surfaces them at the top of planning sessions. Rule source: DOC-STRUCTURE.md.
5. **Context preservation before compaction.** PreCompact hook injects a structured summary of current build state (which batch, ticked/unticked files, active subagent) so mid-build context survives compaction. Rule source: none — unaddressed risk not named in any doc.
6. **Opener routing classification.** UserPromptSubmit hook parses the user's first message, classifies it (test notes / feature request / resume / question), and injects the routing decision as structured context. Currently a prose table in universal-behaviour.md that Claude applies from reasoning alone. Rule source: universal-behaviour.md ("Routing main-Claude's openers").

**Relationship to existing build batches.** Checked against V42–V47: no overlap. V45 (distributed fold-ins) is adjacent to item 4 but doesn't address age tracking. None block a scheduled session.

**Full research.** `research/platform-capabilities-audit.md` (2026-05-21). Also catalogues unused hook events, unused hook types (prompt hooks, agent hooks), and platform capabilities (spawn_task, Claude Preview, mark_chapter, scheduled tasks) — reference material for future scoping, not actionable items.

**Next step.** **All six items promoted in session v47 (2026-05-22).** Item 1 shipped V44 (session v48). Items 2, 3, 4 (Serves-DOC validation, Red flags warning, deferred build-material aging) → 0054. Items 5, 6 (compaction context, opener routing) → 0055. Scope files at `planning/sessions/0054-validation-warnings-bundle.md`, `0055-new-hook-events.md`.

---

## Graduate sovereign implementer development onto sovereign implementer

**The question.** Can the no-code method's own development project switch from its bespoke dev environment (Vxx scope files, BUILD-METHOD.md, OPEN-QUESTIONS.md, two-write rule) to using the method's own plugin — dogfooding sovereign implementer to build sovereign implementer?

**Why it matters.** Surfaced 2026-05-21, discussion session. Dogfooding would surface gaps Taskflow can't (Taskflow only exercises the app-building path), and would validate the method for non-UI project types. The bespoke dev environment has served the project well but diverges from the method it's building — the longer the divergence persists, the more the method's design is informed by building apps rather than by building anything.

**Conclusion from discussion.** Yes, but staged. The current dev environment must ship the prerequisites first; the graduation itself is a managed transition, not a switch-flip.

**Prerequisites (all tracked as separate entries).**

1. **Distributed fold-ins + open questions section in BACKLOG** — **Shipped V43 (session v47, 2026-05-22).** Gave the method a parking lot for unresolved questions (open-questions section in BACKLOG.md) and restructured proposed-edit blocks to live in destination docs' own `## Proposed edits pending` sections (then named `## Fold-ins pending`). Includes the Inputs line for build batches.
2. ~~**[[Automated vs. manual test split + non-UI test types]]**~~ — **Shipped V46 (session v50, 2026-05-22).** Four named test types (Look and click, Run and read, Trigger and observe, Generate and inspect), Claude/User verifier split, 10-column TEST-LOG, Tests: sub-section in build batches, Claude-automated test pass in after-build.
3. **[[Shelve the two-write rule and prose-only canonical docs]]** — **Done in session v40, 2026-05-21.** Repo-root docs-only set frozen at V39; plugin side is sole operational source. Restoring two-write maintenance is one OPEN-QUESTIONS promotion away. Removes the maintenance burden that's specific to the current dev environment and has no method-level equivalent.
4. **[[UX.md adaptation for non-GUI projects]]** — **Promoted to V47 (renumbered V43 → V47 in session v43, 2026-05-22).** Vocabulary and doc structure changes so the method's language fits a plugin/method-spec project, not just UI apps.

**What doesn't need a prerequisite.** Vxx scope files → BACKLOG batches (the existing batch format already covers the Outputs half; the Inputs line covers the rest). Build-log narrative (folder-mode since V50; already in the consumer method since V33).

**Next step.** **Promoted to 0059** (session v47, 2026-05-22). Capstone session — all four prerequisites ship before 0059. Scope file at `planning/sessions/0059-graduation-dev-onto-method.md`.

---

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

## ~~Automated testing / CI for the method's dev project~~ — RESOLVED v55

Resolved by v55 (scope 0053). The hook-script direct-invocation suite shipped as `tests/` at repo root: pytest-based, 124 tests, fixture-driven, covering all hooks and shared helpers. See `BUILD-METHOD.md` → *Automated test suite (V53 — pytest)* for docs. Automated CI pipeline remains deliberately absent — the suite runs locally before commits.

---

## TEST-LOG row pruning

**The question.** Should `TEST-LOG.md` gain an actual pruning mechanism (deletion-based) to bound the file's growth? Current rule (`DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule*): rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically over a project's life.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Drift check 5 (retest after change — `plugin/agents/planning.md` → *Drift checks — always run*) walks every Pass-confirmed row to judge whether its component has been touched. As a project ages, this scales linearly with batches shipped. Real context cost. Counter-argument: audit trail value — "passed at the time" is worth keeping; deletion risks losing the trail.

**Working notes.** Three approaches worth weighing.

- Time-based: drop Superseded rows older than N versions.
- Component-based: drop rows whose component no longer exists in `MANIFEST.md`.
- Manual: an explicit per-planning-session option to archive rows to an external file (preserving audit, removing from context).

**Next step.** **Promoted to 0056** (session v47, 2026-05-22). Scope file at `planning/sessions/0056-test-log-row-pruning.md`.

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

**Next step.** **Promoted to 0057** (session v47, 2026-05-22). Direction decided at session start based on spec stability across 0045–0056. Scope file at `planning/sessions/0057-subagent-rule-loading-convergence.md`.

**V37, 2026-05-21: targets shifted, tension unchanged.** V32's two-write rule moved the runtime spec targets from `NO-CODE-METHOD.md` to `plugin/docs/DOC-STRUCTURE.md` and `plugin/docs/VOCABULARY.md`; `adopt.md` joins `planning.md` and `before-build.md` as a read-at-entry subagent. The underlying inline-vs-read-at-entry question is the same shape, just against the new targets. Stays parked at the same threshold: promote if `plugin/docs/` churns enough (or stabilises enough) to make convergence the obviously right call, or if a parity audit flags meaningful drift in `batch-executor.md`.

---

## Track session performance over time? (AEX-style DEX/HEX)

**The question.** Should a future version include a lightweight session-performance log — configuration used (model, prompts, hooks, skills) plus structured assessment of how the session went — so method decisions rest on evidence rather than instinct? Borrowed from AEX (github.com/ctenidae8/AEX_Protocol): **DEX** = per-config reliability score from logged outcomes; **HEX** = per-config record of what tasks the config has proven good at.

**Why it matters.** Raised externally via conversation + distilled-question artifact (V19 chat; share-link content unretrievable). Worth recording because it points at a real long-term tension: the method develops session-by-session, decisions made on first-principles intuition. Public-scale aggregated evidence has obvious value. Single-user evidence against an evolving method — useful, or premature noise?

**Working notes — honest assessment from V19.**

1. *Method isn't stable yet.* V19 of ~27 planned sessions plus refinement. Measuring an evolving system captures noise about its evolution, not signal about its working state. Stabilise first, then decide what to measure.

2. *Sample size is unworkable.* One person, one project, ~30 sessions through V27 — even fully logged, variables are confounded ("did the method work?" tangles with "was Alex sharp today?" and "was the task tractable?"). Signal-to-noise per decision is low.

3. *Defining "went well" is the hardest part, and the artifact says so itself.* Without a mechanical success criterion, "well" becomes vibes-encoded-as-data — worse than vibes, because numeric scores feel objective when they aren't.

4. *Existing retrospective mechanisms already cover this qualitatively.* The build log captures what shipped, decisions, surprises, carry-forwards. `OPEN-QUESTIONS.md` captures unresolved tensions. Discoveries → planning batches captures emergent needs. These fit small-sample, single-user, evolving-method conditions. If insufficient later, cheaper incremental move is structured fields in build-log entries ("what worked / what didn't / hypothesis for next time"), not a separate measurement system.

5. *What current decision would this change?* V17's architecture, V18's hook-event choice, V19's hook-deny-redirect mechanic — none would have been called differently with a session-performance log. The artifact's own bar is "does the evidence change my decisions?" From V19's vantage, no.

6. *Where the idea earns its keep eventually.* If the method goes public (course revival, published plugin with consumers), aggregated cross-user session data is genuinely valuable — AEX/DEX/HEX are designed for that scale. Single-user, in-development is the wrong scale.

**Next step.** **Promoted to 0058** (session v47, 2026-05-22). Scope file at `planning/sessions/0058-session-performance-tracking.md`. Focus on mechanical measures (regression count, intervention count, turn count) to avoid vibes-as-data.

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and `[PROPOSED EDIT PENDING]` rely on Claude Code primitives. For users wanting the method's discipline in plain chat with Claude, another AI tool, or any context where the plugin shape doesn't fit, we'll eventually need a tool-agnostic prose-only rewrite.

**Why it matters.** Surfaced V20 planning. Without the rewrite, the method is structurally bound to Claude Code: locking via PreToolUse, session-start reads via SessionStart, routing via injected context. None exist elsewhere. Users without Claude Code can't run the method as a working system. Prose-only restores accessibility — but only after the plugin shape stabilises, or the rewrite chases a moving target.

**Working notes.**

- Likely shape: prose-only `NO-CODE-METHOD.md` re-expressing every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart foundational reads (becomes at-session-start narrative in `CLAUDE.md`), PreToolUse locking (trust-based convention + chat-time flagging), slash commands (operational procedures in prose).
- Plugin still evolving (V32–V35 ahead). Rewriting before it settles means redoing.

**V37, 2026-05-21: rewrite delivered by V32; entry overtaken.** V32's two-write rule split canonical method content into plugin-side (operational) and docs-only (project-agnostic) artefact sets. The docs-only side at the repo root — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/` — is the prose-only rewrite this entry called for. Ongoing parity is held by the two-write discipline (`BUILD-METHOD.md` → *Two-write rule for canonical docs*), not by a future rewrite session.

**Next step.** **Indefinitely parked** (session v47, 2026-05-22). Kept as last entry in OPEN-QUESTIONS. Promote if a real audience for the prose-only set emerges (public release, non-Claude-Code users).
