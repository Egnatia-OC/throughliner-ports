# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

---

## Automated testing / CI for the method's dev project

**The question.** `BUILD-METHOD.md` → *Testing — what we actually do* asserts no automated CI: smoke tests are hand-run by Alex post-session, framed as deliberate — "CI's value is regression-catching across many simultaneous changes; this project ships one tag at a time with full attention." Should the decision be revisited as the plugin's surface grows, and if so, what shape of automation would earn its place?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. The "one tag at a time with full attention" framing assumes Alex hand-verifies everything. As the plugin surface grows, hand-verification scales linearly and becomes both more expensive and more error-prone. V25 and V27 each shipped with bugs that smoke tests caught after the fact; a more systematic pre-flight check might have caught some earlier. The trade-off is between manual-only discipline (defensible while the method is small and single-user) and introducing automation (defensible if the surface keeps growing).

**Working notes.** Three shapes worth considering.

- *Keep as-is.* Status quo. Defensible while the method spec is still churning. Cost: hand-verification scales with surface.
- *Hook-script direct-invocation suite.* Add a `tests/` directory at repo root with scripts that pipe fake hook input into each hook script and assert on stdout. Catches parser / arithmetic bugs pre-smoke-test. Doesn't catch Claude Code integration issues (those still need `--plugin-dir`). Low cost; partial coverage.
- *Fixture-driven integration suite.* Harness that spins up a fixture project, runs `claude --plugin-dir`, and asserts on resulting BACKLOG.md / TEST-LOG.md state. Highest fidelity; highest cost; brittle against Claude Code version changes.

**Next step.** Park. Revisit when (a) the plugin surface stabilises post-V32 E2E test, or (b) a regression slips through hand-verification that automation would have caught. **Promote sooner** if hand-verification scaling becomes a real bottleneck.

---

## UX.md adaptation for non-GUI projects

**The question.** UX.md's structural rules (every entry corresponds to something the user can experience in the current build; the "the user needs this because..." line; user-facing rationale) are built around projects where the user has a UI. For non-GUI projects — CLI tools, backend services, data pipelines, MCP servers, scripts — "user experience" maps imperfectly: the "user" may be a developer integrating, an operator monitoring logs, or a downstream system; the "experience" is request/response, exit codes, file outputs, log lines. Does UX.md's structure adapt cleanly, or does the method need a non-GUI variant?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. The method-wide phrasing "user-observable behaviours" implies a visible UI; for non-GUI projects this either reads strangely or forces the no-coder to abstract their concrete deliverables into ill-fitting "user experiences." The same lean recurs in `NO-CODE-METHOD.md` (the *Pre-build verification estimate* Vocabulary entry, the *After every build* test-session-open step), `DOC-STRUCTURE.md`, and several subagent bodies. Taskflow (a native Android app) doesn't hit this; the method is meant to be general.

**Working notes.** Three shapes worth considering.

- *Generalise the vocabulary.* Replace "user-observable behaviours" with "observable outcomes" or "testable behaviours" across `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, subagent bodies, and Crash course. Lighter lift; doesn't change the structure. Cost: loses the "user" anchor that protects against feature drift.
- *Non-GUI variant of UX.md.* Add a section to `DOC-STRUCTURE.md` → *UX.md structure* explaining how non-GUI projects should shape their entries: name the "user" explicitly (operator, downstream system, integrating developer), let the "experience" be whatever they observe (logs, response, exit code, file). Heavier; clearer for non-GUI no-coders.
- *Separate spine doc for non-GUI projects.* A new template (BEHAVIOUR.md? CONTRACT.md? OUTPUTS.md?) replaces UX.md for non-GUI projects. Heaviest; risks fragmenting the method. Defer unless shapes 1 and 2 prove inadequate.

**Next step.** Promote to a planning session in V31+ once V30 ships and the Crash course excerpt fix is in place. **Promote sooner** if Alex (or any consumer) starts a non-GUI project with the method before V31 ships.

---

## Consumer-method git workflow — tagging, commits, push discipline

**The question.** The method currently leaves git workflow up to the no-coder, with no recommended habits or supporting machinery. The dev project (sovereign-implementer itself) uses a strict "one session = one git commit + one git tag, push commit + tag" convention (`BUILD-METHOD.md` → *The unit of work: a session*). The consumer method makes no equivalent recommendation. Two coupled sub-questions:

1. Should the method recommend or enforce a session-tagging / commit-push discipline for consumer projects?
2. What does graceful integration look like with Claude Code's native git handling — does Claude Code expose any git-workflow hooks or features the plugin should pair with, or should the plugin do its own?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. The dev project hit a recovery-cost incident in V23 — parallel Cowork sessions on the same folder corrupted files, mangled CRLF, partial-wrote, and lost in-flight ideas. Without git discipline as a habit, recovery was harder and the loss was larger. Consumer projects without the dev project's tagging habit are equally exposed to mid-session corruption (Drive sync, parallel sessions, Obsidian locks), with no easy revert path. A method-level "tag and push after every shipped build batch" would give consumer projects the same recovery surface the dev project relies on. Big topic that was missed during V17–V29; deserves its own build session, not a fold-in.

**Working notes.** Web-search complete (V30, 2026-05-20); full notes at `planning/drafts/git-integration-research.md` — V32+ session consumes that draft. Headline findings:

- **No git-specific hooks** in Claude Code (no PreCommit / PostCommit / PrePush). Git awareness happens by intercepting Bash via `PreToolUse` / `PostToolUse`, or by acting at `Stop`.
- **CC has no auto-commit behaviour** and treats git as a tool it calls via Bash. There's nothing native to "pair with" — the plugin either drives git itself or doesn't.
- **Prior art is fragmented**: GitButler ships a `Stop`-hook commit pattern (closest published analogue, but its `but claude stop` command does non-trivial branch management); `git-guardrails` ships a `PreToolUse` skill blocking dangerous git commands; no Anthropic-published git plugin exists.
- **Windows-specific.** `.git/index.lock` contention is real and worse on Windows; CC's background `git status --porcelain` polling is the main contention source. Open issue `anthropics/claude-code` #28546 confirms; proposed fix `--no-optional-locks` (#47721) status unknown. Hooks doing git ops need retry/wait logic; avoid `git status --porcelain` in frequently-firing hooks.
- **Caveat in the research.** One user who tested Stop-hook auto-commits at scale rolled them back as "cost more than they returned." Safer initial position: recommended habit + a `PreToolUse` safety-guard against destructive git commands; Stop-hook auto-commit as opt-in later.

Likely shapes (refined from web-search):

- *Habit + safety-guard.* Add a *Recommended habits* line to `NO-CODE-METHOD.md` ("tag and push after every shipped build batch"). Ship a `PreToolUse` hook blocking `git reset --hard` and `git push --force`. Lowest risk, addresses the V23 recovery-surface gap.
- *Stop-hook auto-commit (opt-in).* Stop-hook tags + pushes after batch-executor's last file ticks. Test in Taskflow before promoting to default.
- *Bundled skill doc.* A skill (`/git-discipline` or similar) explains the method's git habits and walks the no-coder through first-time setup. Pairs with the habit recommendation.

Pre-promote action items (from the research's *Items to verify*):

1. Reproduce the `.git/index.lock` contention on Alex's machine — measure how aggressive retry logic needs to be.
2. Read GitButler's full `but claude stop` implementation before designing any Stop hook.
3. Check current status of `--no-optional-locks` (issue #47721).
4. Confirm plugin-bundled hooks install into `settings.json` automatically vs. require user copy-paste.

**Next step.** Web-search returned; promote to its own session in V32+ (PLAN.md row to be added when V32 scoping starts). The session likely ships: a *Recommended habits* line + a `PreToolUse` safety-guard hook against destructive git commands, plus consumer-side documentation in `Crash course.md`. Stop-hook auto-commit deferred to a later opt-in session. **Promote sooner** if Taskflow's first build cycle suffers a recovery incident.

---

## planning/drafts/ pattern for consumer projects

**The question.** The dev project (sovereign-implementer itself) uses `planning/drafts/<topic>.md` as a destination-agnostic carryover for substantive chat content a future session might start from — drafts, comparison tables, structural sketches, protocol rules, column shapes, option matrices. Files are committed when "good enough to walk away from," consumed by whichever session folds them into a persistent location, and deleted at consumption. Consumer projects under the method have `BACKLOG.md`'s *Fold-ins pending* section (destination-specific — for source-of-truth doc content) but no general home for chat content that doesn't yet belong to a specific doc destination. Should the method add a consumer-side drafts mechanism?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. The pattern that prompted the dev-project drafts/ — substantive chat output worth carrying forward but not yet ready to commit to a specific destination — likely occurs in consumer projects too. Without a drafts location, that content either ends up in chat (lost on `/clear`), in `BACKLOG.md` (where it doesn't fit if it's not yet a planning batch or a fold-in), or in an ad-hoc file somewhere. The drafts/ pattern gives chat content a transient home with a clear lifecycle.

**Working notes.** Touches: `NO-CODE-METHOD.md` (mention drafts/ in *Editing surfaces* or its own sub-section), `DOC-STRUCTURE.md` (folder structure rule, file format, lifecycle), the planning subagent body (when to write a draft), potentially the `/adopt` scaffold script (create the drafts/ directory at scaffold time). Lifecycle should mirror dev project: write when "good enough to walk away from," delete at consumption, with a one-line note in BUILD-LOG (or its consumer-side equivalent — see [[Consumer-side BUILD-LOG.md equivalent]]) for dead-end drafts that get pruned.

**Next step.** Fold into the same V31+ session as [[Consumer-side BUILD-LOG.md equivalent]] — these are coupled (drafts/ needs a place to log dead-end pruning, and that place is the BUILD-LOG entry). **Promote sooner** if first real Taskflow use surfaces the gap acutely.

---

## Consumer-side BUILD-LOG.md equivalent

**The question.** The dev project (sovereign-implementer itself) maintains `BUILD-LOG.md` — a persistent narrative record per session, capturing what shipped, decisions taken and why, pivots and surprises, and items carried forward. Consumer projects under the method have no equivalent. The after-build subagent produces a plain-English build recap, but that recap lives only in chat — lost on `/clear`. The "why" trail across a consumer project's builds is currently missing. Should the method gain a consumer-side `BUILD-LOG.md`?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20, when Alex asked what dev-project practices should be applied back to the method itself. After-build's recap captures plain-English description of what changed, but a project's audit trail beyond that is patchy: UX.md has user-need rationale (intent-level only), MANIFEST.md has element descriptions (no per-build narrative), BACKLOG.md tracks deferred work (forward-looking), TEST-LOG.md tracks test outcomes (one row per behaviour). No single doc captures "this build shipped X because of Y, and surprise Z came up during it." The dev project found this gap large enough to add `BUILD-LOG.md` early; consumer projects likely feel the same gap as they accumulate builds.

**Working notes.** New entry shape would mirror the dev project's `BUILD-LOG.md` (What shipped / Decisions taken and why / Pivots and surprises / Carried forward). Touches:

- `NO-CODE-METHOD.md` → *After every build* — add a step appending an entry to BUILD-LOG.md.
- `DOC-STRUCTURE.md` — add BUILD-LOG.md structure.
- `templates/BUILD-LOG-TEMPLATE.md` and `plugin/templates/BUILD-LOG-TEMPLATE.md` — new templates.
- `plugin/agents/after-build.md` — drafting the entry as part of recap-generation.
- `plugin/skills/adopt/scripts/scaffold.py` → `DESTINATION_FILENAMES` and `TEMPLATE_TO_DESTINATION` — scaffold BUILD-LOG.md alongside the existing spine docs.
- INVENTORY.md, footer-bump list.

Sub-question: where does after-build's existing chat-time recap sit relative to the new BUILD-LOG entry? Likely: BUILD-LOG entry is the persistent record; the chat recap is the in-session announcement. Both happen, one persists.

**Next step.** Promote to a planning session in V31+ once V30 ships. **Promote sooner** if first real Taskflow build cycle surfaces the audit-trail gap acutely.

---

## Frame-correction sweep at session close — consumer-method version

**The question.** The dev project added a frame-correction sweep at session close in V29 (`BUILD-METHOD.md` → *Session close* step 2) after V29's own scope file hit a pre-V23 frame and required rework before substantive work could begin. The sweep audits pending scope files for references to old frames the current session corrected. Consumer projects under the method have no analogous obligation. Should the method gain a session-close frame-correction sweep, and if so, what does it operate on (planning batches in BACKLOG.md, UX.md entries cross-referencing the changed feature, additional source-of-truth doc text)?

**Why it matters.** Surfaced V30 retrospective, 2026-05-20. When a build batch substantively changes how a feature works, planning batches in BACKLOG.md that reference the old behaviour could absorb wrongly when a future planning session reads them. The four drift checks (NO-CODE-METHOD.md → *During planning*) cover code↔doc disagreement but not frame-correction in pending planning content. Same failure mode that hit V29's scope file would hit consumer projects' planning batches at some point — the question is whether to surface it before that happens.

**Working notes.** Touches:

- `NO-CODE-METHOD.md` → *After every build* — add a frame-correction sweep step.
- `plugin/agents/after-build.md` — execute the sweep.
- Possibly `plugin/agents/planning.md` — if the sweep is better placed at the next session's planning open rather than at after-build.

Operating scope candidates: planning batches in BACKLOG.md naming the changed frame; UX.md entries cross-referencing the changed feature (flagged as `[FOLD-IN PENDING]` since UX.md is read-only); pending `[FOLD-IN PENDING]` blocks themselves. Sub-question: who runs the sweep — after-build (right after the build that corrected the frame, while the change is fresh) or planning (next session, with the BACKLOG already settled)? After-build is where the dev project does it; consumer-side may differ depending on what's being swept.

**Next step.** Promote to a planning session in V31+ once V30 ships. **Promote sooner** if first real Taskflow build cycle surfaces a frame-correction miss in BACKLOG.md.

---

## Source-of-truth doc edits with no-coder permission

**The question.** Should Claude be permitted to edit `UX.md` and other source-of-truth docs directly when the no-coder gives explicit permission — during a planning session or `/adopt` — bypassing the `[FOLD-IN PENDING]` mechanism? The current rule (`NO-CODE-METHOD.md` → *Editing surfaces*) says never, even with permission.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. The lock exists to prevent build-session drift — small "clarifying" tidy-ups slipping into source-of-truth docs without deliberation. But planning-session-time and `/adopt`-time are exactly when deliberation is happening. The mechanism currently forces a manual fold-in even when Claude has the proposed text ready and the no-coder explicitly says yes. Friction without clear benefit at those moments.

**Working notes.** Likely shape: a `[PROPOSED EDIT]` chat-time mechanism, distinct from `[FOLD-IN PENDING]`. The no-coder approves explicitly with a non-keystroke confirmation; Claude applies the edit directly. `[FOLD-IN PENDING]` stays for cases where Claude cannot get permission (mid-build edit attempts blocked by the PreToolUse hook). Touches: PreToolUse hook's locked-doc check (V19), the `[FOLD-IN PENDING]` mechanism in `DOC-STRUCTURE.md` → *BACKLOG.md structure → Fold-ins pending*, `/adopt` case 3 migrate flow (`plugin/agents/adopt.md`), planning subagent rules.

**Next step.** Promote to a planning session in V31+ once V30 ships. **Promote sooner** if `/adopt` case 3 migrate friction becomes a real blocker in early Taskflow adoption.

---

## TEST-LOG ordering — newest at top vs bottom

**The question.** Should `TEST-LOG.md` rows append at the top (newest-first), matching `BUILD-LOG.md` ordering, instead of the bottom (current rule per `DOC-STRUCTURE.md` → *TEST-LOG.md structure*)?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Newest-at-top matches the no-coder's intuition and Claude's natural read order (top first, and the most-recent rows are usually the most relevant). `BUILD-LOG.md` is top-first; `TEST-LOG.md` being bottom-first creates a mental-model mismatch between the two living logs. The current bottom-first convention traces to the dev-internal TEST-LOG argument ("queried by 'is X tested?' where ID order matters more than recency") — but the consumer-side TEST-LOG has different access patterns (recency-of-test matters for drift check 4 and for planning's read-back).

**Working notes.** Touches `DOC-STRUCTURE.md` → *TEST-LOG.md structure* (the append rule), `plugin/templates/TEST-LOG-TEMPLATE.md` (HTML format-reminder comment position — moves from bottom to top), `plugin/agents/after-build.md` (where it appends rows), `plugin/agents/planning.md` (where it reads). Low-friction once decided.

**Next step.** Fold into a planning session in V31+ along with the [[TEST-LOG row pruning]] question — sibling concern. **Promote sooner** if first real Taskflow build raises the same intuition.

---

## TEST-LOG row pruning

**The question.** Should `TEST-LOG.md` gain an actual pruning mechanism (deletion-based) to bound the file's growth? Current rule (`DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule*): rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically over a project's life.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. Drift check 4 (retest after change — `NO-CODE-METHOD.md` → *During planning*) walks every Pass-confirmed row to judge whether its component has been touched. As a project ages, this scales linearly with batches shipped. Real context cost. Counter-argument: audit trail value — "passed at the time" is worth keeping; deletion risks losing the trail.

**Working notes.** Three approaches worth weighing.

- Time-based: drop Superseded rows older than N versions.
- Component-based: drop rows whose component no longer exists in `MANIFEST.md`.
- Manual: an explicit per-planning-session option to archive rows to an external file (preserving audit, removing from context).

**Next step.** Fold into the same V31+ planning session as the [[TEST-LOG ordering — newest at top vs bottom]] question. **Promote sooner** if Taskflow's TEST-LOG.md crosses a meaningful row count — would benefit from real data first.

---

## "Planning" vocabulary collision with Claude Code's "plan mode"

**The question.** The method uses "planning" as a lifecycle phase name (planning session, planning subagent, planning batch, the planning phase). Claude Code uses "plan mode" for a built-in feature (Shift+Tab toggle that blocks file edits). The two are different concepts the no-coder must distinguish. Should the method's "planning" vocabulary be renamed to remove the ambiguity, or is a vocabulary disambiguation in the docs sufficient?

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. A new reader of the Crash course reads "planning session" and may map it to Claude Code's "plan mode" — misleading because the method's planning session involves editing `BACKLOG.md` (incompatible with plan mode). Worse, plan mode is recommended at two specific moments in the method (pre-method app-idea exploration; before-build batch review), creating a third axis of "planning"-flavoured activity to track.

**Working notes.** Three shapes worth considering.

- **Rename the method's "planning" phase.** Candidates: "design session," "spec session," "decision session." The subagent renames accordingly (`no-code-method:design`?). Heavy lift — every doc, template, subagent body, INVENTORY entry. Lots of footer-bump and parity-audit surface.
- **Vocabulary disambiguation in docs.** Add an explicit "not to be confused with plan mode" note to `NO-CODE-METHOD.md` → *Vocabulary*. Mention in Crash course where plan mode comes up. Low-cost; relies on the reader.
- **Hybrid.** Keep "planning phase" as the lifecycle name but rename the subagent (`no-code-method:planning` → `no-code-method:design`) so the plugin-component name reads distinct. Compromise.

**Next step.** Promote to a planning session in V31+ once V30's Crash course gives concrete sense of how often readers encounter both terms together. **Promote sooner** if first real Taskflow use surfaces the confusion in practice.

---

## NO-CODE-METHOD.md → *During planning* doesn't explicitly assert planning's structural authority over BACKLOG.md

**The question.** V25's *Before build* rewrite removed steps that had Claude regroup BACKLOG.md batches — dead weight, since planning has had full BACKLOG.md edit authority since V22. But *During planning* doesn't explicitly assert "you do the structural batch grouping; before-build doesn't." The assertion is implicit in the planning subagent body's *BACKLOG.md editing — do, then describe* section and in the absence-from-*Before build*. Should *During planning* gain an explicit "structural authority over BACKLOG.md" assertion?

**Why it matters.** Surfaced V25 while drafting the *Before build* rewrite. Future-Claude reading only *During planning* has no way to know before-build deliberately doesn't reorganise. The asymmetry is harmless today but invites drift if either section gets edited later without the other in view.

**Working notes.** Three shapes:

- **A.** One-line assertion in *During planning*'s opening paragraph. Smallest change. Explicit but unobtrusive.
- **B.** A sub-section "Structural authority over BACKLOG.md" under *During planning*. More prominent. Risks over-engineering — the assertion fits in a sentence.
- **C.** Leave as-is. Planning subagent body + absence-in-*Before build* communicate the rule implicitly.

**Next step.** Park. Revisit when *During planning* next needs an edit. **Promote sooner** if a doc-code parity audit flags `plugin/agents/planning.md`'s BACKLOG-authority section as out of step.

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

**Next step.** Park. Revisit once V26–V31 ship and the rate of `NO-CODE-METHOD.md` changes settles. If the spec is stable across consecutive versions, B is fine; if it churns, A; mixed, C. **Promote sooner** if an audit flags meaningful drift in `batch-executor.md`, which forces A.

---

## MANIFEST.md schema gap blocks PreToolUse read-before-edit enforcement

**The question.** `NO-CODE-METHOD.md` → *Required of Claude* says Claude must read MANIFEST.md and the relevant UX.md entry before editing a file with a MANIFEST entry. V25 scoped a PreToolUse check to enforce this, blocked by a schema gap: MANIFEST.md is a flat alphabetical glossary mapping names to descriptions, not paths. A hook firing on `Edit /plugin/foo.py` can't know which MANIFEST entry covers that path. How do we extend the method so hook-level enforcement becomes possible — and is it worth the change?

**Why it matters.** Surfaced V25 while designing the PreToolUse boundary check + read-before-edit pair. Deferred because the schema decision is itself method-level (ripples to MANIFEST-TEMPLATE.md, the After-every-build update logic, and the rule's wording in NO-CODE-METHOD.md). Without resolution, read-before-edit stays convention-only (followed when Claude remembers — ~30% drift per Crash course → Caveats).

**Working notes.** Five options from V25 chat (2026-05-16):

- **A. PostToolUse tracks Reads + PreToolUse checks track.** Real enforcement. New hook type, session-scoped state file with SessionStart cleanup, AND a paths-per-entry schema extension. Largest cost; cleanest behavioural match.
- **B. Inline deny-with-context.** PreToolUse denies an Edit on a MANIFEST-covered file with the MANIFEST and UX entries inlined in the deny reason. No state file, no PostToolUse, still needs the schema extension. Changes the rule from "read first" to "have-the-context-by-edit-time." Worth a separate decision.
- **C. Convention-only.** Status quo. No schema change. Accepts the drift rate.
- **D. Hybrid A+B.** Worst of both; not pursued.
- **E. Defer.** What V25 did.

**Next step.** Promote to a planning session in V26+ once V25 and V26 ship. The session resolves: (1) does MANIFEST.md gain a path field, and in what format? (2) which of A/B/C given (1)? **Promote sooner** if direct-edit users surface in real use — path-mapped MANIFEST also helps drift detection for manual edits.

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
- Plugin still evolving (V25–V31 ahead). Rewriting before it settles means redoing.

**Next step.** Park until V31 (final E2E Taskflow test) ships. Then: list each plugin-specific mechanism, design a prose-only equivalent, schedule sessions. **Promote sooner** if public release approaches before migration completes — that scenario forces the rewrite onto the critical path.

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

**Next step.** Park. Revisit after V31 ships and the method has settled into stable use across a few real project cycles. The question then becomes concrete: list 2–3 design decisions that would have benefited from logged evidence — if non-empty, define a minimal log against them; if empty, drop and record the reasoning in `BUILD-LOG.md`. **Promote sooner** if the method moves toward public release before V31 wraps.

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

**V22, 2026-05-14:** shape #1 **partially folded into V22's planning subagent.** Q2 decision: "always run drift checks every planning session; only skip case is 'nothing has been built yet.'" Drift check 2 (MANIFEST ↔ codebase) fires every planning session regardless of whether Claude shipped a batch — catches file-level changes a direct-edit user makes (new files, renames, deletes on tracked components). What it does **not** catch: in-file content changes to existing tracked files (a developer modifying a function inside a still-tracked `.kt` file leaves no MANIFEST-level signal). That gap is the remaining concern. Shapes #2 and #3 still out of scope; would need their own session. Parked: revisit if direct-edit users surface and file-level coverage proves insufficient; promote sooner if public release approaches.
