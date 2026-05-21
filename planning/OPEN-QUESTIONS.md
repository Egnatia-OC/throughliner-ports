# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

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

**Next step.** Park. Promote to its own session in V43+ once V40–V42 ship (those have higher priority — direct-edit drift, vocabulary sweep, /adopt UX). **Promote sooner** if a consumer hits this in normal use, OR if the V40 git-diff drift detection ends up `cd`-ing into subdirectories often enough that the dev project trips again.

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

**Next step.** Promoted to V41 (renumbered from V40; 2026-05-21). Leaning: vocabulary generalisation + guidance section. Bundled with "planning" disambiguation to amortise the parity audit. **Promote sooner** if Alex (or any consumer) starts a non-GUI project with the method before V41 ships.

---

## TEST-LOG row pruning

**The question.** Should `TEST-LOG.md` gain an actual pruning mechanism (deletion-based) to bound the file's growth? Current rule (`DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule*): rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically over a project's life.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Drift check 4 (retest after change — `NO-CODE-METHOD.md` → *During planning*) walks every Pass-confirmed row to judge whether its component has been touched. As a project ages, this scales linearly with batches shipped. Real context cost. Counter-argument: audit trail value — "passed at the time" is worth keeping; deletion risks losing the trail.

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

**Next step.** Promoted to V41 (renumbered from V40; 2026-05-21). Bundled with non-GUI generalisation to amortise the parity audit. **Promote sooner** if first real Taskflow use surfaces the confusion before V41.

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

---

## Method response to direct-edit users (developers)

**The question.** How should the method respond to users who edit code directly — developers who already write code and want the method's planning discipline without ceding all technical work to Claude?

**Why it matters.** Raised in Vibecord — "developers will try to use it." The method assumes Claude does the technical work and the user reviews recaps. A user editing code directly breaks several assumptions: MANIFEST.md drifts because user edits aren't recorded; `Serves UX.md:` discipline gets bypassed; drift checks catch *some* of it (MANIFEST ↔ codebase) but not all. Without addressing this, developers using the method will silently corrupt project state and lose the benefits.

**Working notes — three shapes the response could take.**

- *Tighten drift detection so manual edits get caught.* V21's SessionStart (or a PostToolUse) compares working tree against last-known MANIFEST.md state and surfaces manual changes for triage. Smallest change; catches edits after the fact, doesn't prevent them mid-flow.
- *Add a "developer mode" entry point.* Plugin scaffolds a different doc set — keeps `UX.md` / `BACKLOG.md` discipline, drops the assumption Claude does all the code. Requires deciding what developer-mode equivalents of MANIFEST.md and the build-recap flow look like.
- *Document that the method explicitly doesn't serve direct-edit users.* "Who this is for" section in `NO-CODE-METHOD.md` so developers self-select out. Cheapest; loses an audience.

**Next step.** Think during V21 (SessionStart hook extension). If drift detection covers realistic failure modes, fold there and close. If not, promote to its own session in V22–V26.

**V21 planning, 2026-05-14:** V21 does *not* absorb this. V21 adds foundational reads + template-state + resume + routing — none catch manual code edits. Natural home for the tighten-drift-detection shape is V22 (planning subagent + drift logic inlined), or its own session if the other shapes win. Parked; revisit V22 planning earliest, or sooner if public release approaches.

**V22, 2026-05-14:** shape #1 **partially folded into V22's planning subagent.** Q2 decision: "always run drift checks every planning session; only skip case is 'nothing has been built yet.'" Drift check 2 (MANIFEST ↔ codebase) fires every planning session regardless of whether Claude shipped a batch — catches file-level changes a direct-edit user makes (new files, renames, deletes on tracked components). What it does **not** catch: in-file content changes to existing tracked files (a developer modifying a function inside a still-tracked `.kt` file leaves no MANIFEST-level signal). That gap is the remaining concern. Shapes #2 and #3 still out of scope; would need their own session.

**Promoted to V40 (2026-05-21).** Pre-session planning decided: git-diff detection + per-change confirmation protocol (user confirms each flagged change; Claude checks for build-batch conflicts; accepts + doc catch-up if clean). Shapes #2 (developer-mode entry point) and #3 (explicit non-audience) deferred until a real developer reports friction. V40 scope file has full decisions.
