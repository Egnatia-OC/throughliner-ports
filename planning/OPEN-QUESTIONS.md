# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

---

## Method rule: ask the user to run a Sonnet web search when uncertain about an external fact

**The question.** Should the no-code method codify an explicit rule — in `plugin/hooks/universal-behaviour.md` → *Required behaviours* and the docs-only `NO-CODE-METHOD.md` → *Required of Claude* (two-write) — that when Claude is uncertain about an external fact (Claude Code's feature surface, an API's behaviour, a library's status, a setting that may have changed, anything Claude could verify rather than infer), it must either run a web search itself (if web-search tools are available in that session) or ask the user to run one in a separate Claude Sonnet chat? Currently this discipline lives only in Alex's personal global CLAUDE.md; the method itself doesn't carry it, so a consumer using the plugin without that personal instruction is back to Claude guessing or hedging.

**Why it matters.** Surfaced V36, 2026-05-21. V36 #3 resolved cleanly precisely because we ran this discipline: the plan-panel writability question went to Sonnet as a paste-ready prompt, came back with a definitive "not writable from outside Claude" plus evidence and caveats, and the V36 outcome handling executed the same session. Without that discipline, the same question would have either (a) been parked indefinitely waiting for "someone to research it," (b) been guessed at by Claude with a fabricated mechanism, or (c) shipped wrong instructions into the spec. The method already has *Ask rather than guess on ambiguity* in `universal-behaviour.md`, but that rule is about ambiguity in the user's *request* — not about external-fact uncertainty Claude could verify. Different shape, different mechanism, different fix.

**Working notes.** Likely shape: a new bullet under *Required behaviours* in `universal-behaviour.md`, mirrored in docs-only `NO-CODE-METHOD.md` → *Required of Claude*. Draft wording: *"When uncertain about an external fact — Claude Code's feature surface, an API's behaviour, a library's status, anything you could verify rather than infer — don't guess or hedge. If web-search tools are available in this session, use them. Otherwise, ask the user to run one for you, formatted as a paste-ready prompt the user can hand to a fresh Claude Sonnet chat: context about the project, the decision the answer turns on, what to look for, any authoritative URLs to check first, and a request to output as markdown. Load-bearing for: decision quality across every phase — silent guessing puts wrong facts into source-of-truth docs, scope files, and BUILD-LOG entries."*

Open shape questions before scoping:

- **Prompt shape templated or freeform?** Alex's global CLAUDE.md specifies the paste-ready-prompt shape in detail (address Sonnet, give context, list authoritative URLs, request markdown output, one fenced block). Should the method codify this shape (a sub-rule listing the required prompt elements), or leave it to Claude's judgment per-case? Templating tightens the contract but adds spec surface.
- **What if the user can't easily run a parallel Sonnet?** Many no-coders won't have a second Claude Sonnet chat readily available alongside their Claude Code session. Should the rule have a fallback ("if the user says they can't run the search, surface the uncertainty plainly in the relevant doc as a `[UNVERIFIED]` marker and proceed conservatively")? Or trust that "ask" is enough and the user's "I can't" is the trigger for downstream behaviour?
- **Scope boundary against existing rules.** The new rule overlaps subtly with *Ask rather than guess on ambiguity* (request ambiguity) and *Red flags — screen and surface* (security/privacy concerns). The new rule covers external-fact uncertainty — a third axis. Confirm the three don't tread on each other when drafted.
- **Crash course mention.** Probably worth a one-line mention in the *Four disciplines that do most of the work* section or alongside the existing "30% drift" headwind — non-coders should know Claude will sometimes hand them a Sonnet prompt and that this is a method discipline, not Claude being lazy.

**Next step.** Fold into a V38+ planning session post-V37 (V37 is the marketplace.json + local install session, already scoped). **Promote sooner** if a session surfaces another moment where guessing-instead-of-searching costs work, ships wrong content, or parks a question that Sonnet could have answered in one round.

---

## Footer-stamp on locked source-of-truth docs routed through [FOLD-IN PENDING]

**The question.** When `/adopt` case 4 (refresh templates) finds a locked source-of-truth doc (UX.md, SYSTEM-PROMPT.md, or any other additional-doc covered by the lock) missing the `*No-code method — Version N.*` footer, the subagent routes the footer addition through `[FOLD-IN PENDING]` in BACKLOG.md and asks the user to add the line by hand at the next planning session. Should there be a narrow carve-out letting the plugin stamp the footer directly on a locked doc, since the footer is version metadata rather than user-facing content?

**Why it matters.** Surfaced V35 E2E test, 2026-05-21. The lock on UX.md and similar source-of-truth docs exists to prevent silent content drift — small "clarifying" edits to user-facing text slipping in without deliberation. A `*No-code method — Version N.*` footer is metadata, not content; adding or refreshing it doesn't change what the doc says about the project. Forcing a manual fold-in here adds friction during `/adopt` without protecting against anything the lock was designed to prevent. In V35's actual run, two of the four "missing footer" docs (UX.md and SYSTEM-PROMPT.md) became `[FOLD-IN PENDING]` blocks the user must apply by hand at the next planning session — a step that exists purely because the carve-out doesn't.

**Working notes.** Likely shape: a single-purpose exception in the PreToolUse locked-doc check that permits an Edit on a locked doc if and only if the diff is exclusively adding or updating the footer line (exact-match pattern, no surrounding content changes). All other edits to locked docs still route through `[FOLD-IN PENDING]`. Touches: `/adopt` case 4 refresh logic (`plugin/agents/adopt.md`), the PreToolUse locked-doc check, and the lock description in `DOC-STRUCTURE.md` / `NO-CODE-METHOD.md` (both sides per the two-write rule).

**Next step.** Fold into a V36+ planning session post-V35, paired with [[Source-of-truth doc edits with no-coder permission]] — both questions touch the same lock rule from different angles and one session can resolve them together. **Promote sooner** if `/adopt` refresh friction with locked-doc footers comes up again in a non-Alex consumer's first run.

---

## /adopt permission-prompt UX and narration for new users

**The question.** The `/adopt` flow in a CLI session (PowerShell via `claude --plugin-dir`) requires the user to approve multiple tool calls — `scaffold.py detect-case`, python one-liners checking file size, grep for the method footer, reads of template files — each surfacing a "Do you want to proceed?" prompt with no explanation of what the step is for or why it matters. A non-coder seeing "Bash: python -c import os; p=r'C:\...CLAUDE.md'; print('size:', os.path.getsize(p))" has no basis for deciding whether to approve. Is the narration sufficient, and does the flow need redesign for the marketplace-installed experience?

**Why it matters.** Surfaced V35 E2E test, 2026-05-21. The `/adopt` subagent's detection steps are mechanically correct but user-opaque. The CLI's `--plugin-dir` path is dev-only and permission-prompt-heavy by nature, so some friction is expected there. But the marketplace-installed experience (once `marketplace.json` exists and the plugin is formally installable) will be the real first-run path for new users — and it's untested. Two concerns: (1) whether marketplace installation changes the permission-prompt surface (it may not — Claude Code's permission model is per-tool, not per-install-method); (2) whether the `/adopt` subagent's narration needs a plain-English preamble at each detection step ("I'm checking whether this folder already uses the method — approving these reads lets me figure out which setup path to offer you").

**Working notes.** Three things to test once `marketplace.json` exists:

- Does a marketplace-installed plugin get a different permission surface than `--plugin-dir`? If the user has already approved the plugin at install time, do individual tool calls still prompt?
- Walk through `/adopt` on a fresh app project (not Taskflow — a genuinely new folder) and review each prompt from a new-user perspective. Is the narration self-explanatory, or does the user need the Crash course open beside them?
- **CLI vs. desktop app input differences.** The CLI (`claude` in a terminal) pre-fills suggested responses at the prompt — the user can see a proposed answer and press Enter to accept or edit it. The Claude Code desktop app (Claude Code tab in the Claude Windows/Mac app) has no pre-fill; the user sees an empty prompt and must type from scratch. The plugin's dialogue flows (especially `/adopt`'s multi-step sequences and planning's per-row read-backs) may rely on pre-filled suggestions to guide non-coders through choices. Verify during the desktop-app test that every dialogue step is navigable without pre-fills — if not, the subagent narration needs to compensate by spelling out what to type.

**Next step.** Park until the plugin has a `marketplace.json` and a packaging session ships (no current PLAN.md row for packaging). Then test `/adopt` end-to-end via marketplace install on a fresh project. **Promote sooner** if a non-Alex user tries the plugin before packaging ships and reports confusion.

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

**Next step.** Promote to a planning session in V36+ post-E2E (V35) once Taskflow evidence informs whether the structural rules need a non-GUI variant or only vocabulary generalisation. **Promote sooner** if Alex (or any consumer) starts a non-GUI project with the method before V35 ships.

---

## Source-of-truth doc edits with no-coder permission

**The question.** Should Claude be permitted to edit `UX.md` and other source-of-truth docs directly when the no-coder gives explicit permission — during a planning session or `/adopt` — bypassing the `[FOLD-IN PENDING]` mechanism? The current rule (`NO-CODE-METHOD.md` → *Editing surfaces*) says never, even with permission.

**Why it matters.** Surfaced V30 Crash course review, 2026-05-20. The lock exists to prevent build-session drift — small "clarifying" tidy-ups slipping into source-of-truth docs without deliberation. But planning-session-time and `/adopt`-time are exactly when deliberation is happening. The mechanism currently forces a manual fold-in even when Claude has the proposed text ready and the no-coder explicitly says yes. Friction without clear benefit at those moments.

**Working notes.** Likely shape: a `[PROPOSED EDIT]` chat-time mechanism, distinct from `[FOLD-IN PENDING]`. The no-coder approves explicitly with a non-keystroke confirmation; Claude applies the edit directly. `[FOLD-IN PENDING]` stays for cases where Claude cannot get permission (mid-build edit attempts blocked by the PreToolUse hook). Touches: PreToolUse hook's locked-doc check (V19), the `[FOLD-IN PENDING]` mechanism in `DOC-STRUCTURE.md` → *BACKLOG.md structure → Fold-ins pending*, `/adopt` case 3 migrate flow (`plugin/agents/adopt.md`), planning subagent rules.

**Next step.** Promote to a planning session in V36+ post-E2E (V35). **Promote sooner** if `/adopt` case 3 migrate friction becomes a real blocker in early Taskflow adoption.

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

**Next step.** Promote to a planning session in V36+ post-E2E (V35) once Taskflow use gives concrete sense of how often readers encounter both terms together. **Promote sooner** if first real Taskflow use surfaces the confusion before V35.

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

**Next step.** Promote to a planning session in V36+ post-E2E (V35). The session resolves: (1) does MANIFEST.md gain a path field, and in what format? (2) which of A/B/C given (1)? Originally tagged V26+ — held through V26–V31 because it's a heavy method-level decision (schema change ripples to MANIFEST-TEMPLATE.md, after-build update logic, the rule's wording in spec docs) and earlier sessions had higher-priority work. Post-V35 evidence may shift the relative priority. **Promote sooner** if direct-edit users surface in real use — path-mapped MANIFEST also helps drift detection for manual edits.

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

**V22, 2026-05-14:** shape #1 **partially folded into V22's planning subagent.** Q2 decision: "always run drift checks every planning session; only skip case is 'nothing has been built yet.'" Drift check 2 (MANIFEST ↔ codebase) fires every planning session regardless of whether Claude shipped a batch — catches file-level changes a direct-edit user makes (new files, renames, deletes on tracked components). What it does **not** catch: in-file content changes to existing tracked files (a developer modifying a function inside a still-tracked `.kt` file leaves no MANIFEST-level signal). That gap is the remaining concern. Shapes #2 and #3 still out of scope; would need their own session. Parked: revisit if direct-edit users surface and file-level coverage proves insufficient; promote sooner if public release approaches.
