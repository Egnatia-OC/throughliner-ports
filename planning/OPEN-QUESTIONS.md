# Open questions

Method-level questions that have been raised but aren't yet ready to be a session. Each entry stays here until the question resolves — at which point it either folds into an existing session's scope, becomes its own new session (with a row added to `PLAN.md` and a new `sessions/Vxx.md`), or is consciously dropped with a one-line reason recorded in `BUILD-LOG.md` so future-me knows it was considered.

Newest first. Removed when resolved.

For the format and lifecycle, see project `CLAUDE.md` → *Open questions*.

---

## V27 lock-check excludes TEST-LOG.md → test-confirmation gate is structurally inert

**The question.** The PreToolUse hook's locked-source-of-truth check (V19 check (a)) treats every doc declared in `CLAUDE.md`'s path block as locked unless the logical name is in `WRITABLE_LOGICAL_NAMES = {"BACKLOG.md", "MANIFEST.md"}` (`plugin/hooks/pre_tool_use.py:103`). V26 added `TEST-LOG.md` as a fifth spine doc with a path-block entry. V27 shipped the after-build subagent whose canonical mechanism per `NO-CODE-METHOD.md` → *After every build* step 3 is `Write(TEST-LOG.md)` to append blank-Status rows opening a test session. But `TEST-LOG.md` is NOT in `WRITABLE_LOGICAL_NAMES` → V19 check (a) denies every after-build write → no rows are ever opened → the V27 test-confirmation gate has no rows to gate on.

**Why it matters.** Found 2026-05-17 during V27 Windows smoke testing (see `TEST-LOG.md` #058). Without this fix, V27's entire test-confirmation gate machinery is structurally inert in every consumer project — the gate denies builds against pending rows that can never exist because the mechanism for opening them is blocked. The V27 BUILD-LOG's claim that the gate is "wired end-to-end" is currently false. After-build correctly halted on the deny rather than mis-routing through fold-ins (subagent's diagnosis: fold-ins are for mid-build edits to locked spine docs, not the canonical after-build test-session-open write) — so this is an incomplete-wiring bug at the lock-check layer, not a mis-route bug at the subagent layer.

**Working notes.**

- One-line code fix: add `"TEST-LOG.md"` to `WRITABLE_LOGICAL_NAMES` at `plugin/hooks/pre_tool_use.py:103`.
- The fix also covers planning subagent's Status updates during the per-row read-back (Rule 2 — `Status` flips from blank to Pass/Fail/Skipped) and the drift-check 4 row-append on substantial change (Rule 5). Both legitimately need TEST-LOG to be writable to Claude. Spec-side parity is already correct — `NO-CODE-METHOD.md` → *Editing surfaces* lists `TEST-LOG.md` as read/write to Claude; only the hook is out of sync.
- Adjacent doc edits warranted: update the docstring on `pre_tool_use.py` check (a) to name TEST-LOG.md as writable (currently the docstring at line 9–14 just says "Locked docs are: UX.md, plus any additional source-of-truth docs..." — TEST-LOG.md is a spine doc, not "additional," so calling out the explicit writability matches the new code).
- No template change needed. `templates/CLAUDE-TEMPLATE.md` and `plugin/templates/CLAUDE-TEMPLATE.md` already declare `TEST-LOG.md` in the path block (V26 work); the hook is what needs to catch up.

**Next step.** **Promote to next session's scope as the first item.** V28's `/adopt` scope shouldn't proceed on top of an inert V27 — either expand V28 to include this fix (plus the sibling Stop-hook-vs-tripwire fix below) before shipping `/adopt`, or run a V28-prequel session that fixes V27 first and ships `/adopt` as V29. The fix is one line plus the docstring update.

---

## V27 Stop hook + SessionStart tripwire conflict — Stop hook redirects to batch-executor while a test session is still open

**The question.** When a session opens with both (a) an unticked build batch in `BACKLOG.md` AND (b) unconfirmed previous-batch rows in `TEST-LOG.md`, two enforcement signals fire and conflict:

- SessionStart tripwire (`session_start.py` V27 addition) correctly injects a routing override directing main Claude to invoke the planning subagent first, regardless of opener.
- Stop hook (`stop.py`), after planning subagent's turn ends asking the user about row #001, fires, sees the unticked batch in BACKLOG.md, and redirects to batch-executor anyway. Stop hook doesn't consider TEST-LOG state — it only looks at BACKLOG.md's unticked-batch state.

Result: planning subagent's read-back gets derailed before the user can answer the first row. The PreToolUse gate (check (f)) at this point should fire on the redirected Task → batch-executor invocation and deny — that's the structural backstop. Direct hook-script tests (`TEST-LOG.md` #053, #054, #055) confirm the script-level gate denies correctly. But in the live `claude --plugin-dir` smoke-test session, batch-executor appeared to run anyway with no visible deny in chat. Either the deny fired silently (missed in chat output), the hook didn't fire on the redirected Task call, or Claude Code processed the redirect in a path that bypassed PreToolUse. Needs verification.

**Why it matters.** Found 2026-05-17 during V27 Windows smoke testing G1 attempt. Combined with the sibling `WRITABLE_LOGICAL_NAMES` bug, V27's whole test-confirmation gate flow is broken end-to-end: after-build can't open the test session because of the lock; if it could, the planning subagent's read-back would be interrupted by the Stop-hook redirect; the PreToolUse gate is supposed to be the final backstop but its visibility in the Stop-hook-redirected path is uncertain. Even if the WRITABLE_LOGICAL_NAMES fix lands, the gate flow is still broken without addressing this conflict.

**Working notes.** Two-part fix shape:

1. **Stop hook needs to defer when a test session is open.** `plugin/hooks/stop.py` currently parses BACKLOG.md for unticked batches and redirects to batch-executor. It should additionally read TEST-LOG.md (and BUILD-LOG.md for session narrowing, same as the gate logic in `check_test_confirmation_gate`) — if previous-batch rows are unconfirmed, exit silent (or, more directly, redirect to the planning subagent for the read-back) rather than redirecting to batch-executor. This fixes the conflict at the source rather than relying on the PreToolUse gate as backstop. Helper code is already in `pre_tool_use.py` (`parse_test_log_rows`, `is_row_confirmed`, `identify_previous_session`) — the duplication makes extraction to a shared module the natural co-fix (the V27 BUILD-LOG already names this as a follow-up refactor).

2. **Verify gate fires on Stop-hook-redirected Task calls.** Direct-invocation tests (G1, G2, G3) prove the script-level gate works. The Claude Code observation suggested the gate didn't fire visibly on the Stop-hook-redirected Task call; could be a Claude Code wiring issue, an observation artefact (brief deny indication missed in chat scroll), or the hook fires-but-the-redirect-bypasses-it. Verify by re-running with a clean fixture and explicit attention to chat output between the Stop-hook redirect text and the batch-executor invocation. If the gate IS firing visibly: only fix (1) is needed. If the gate is NOT firing visibly: this is a Claude Code plugin-wiring investigation thread of its own.

**Next step.** **Promote to next session's scope alongside the WRITABLE_LOGICAL_NAMES fix.** Same session can ship both fixes if scope allows; otherwise the WRITABLE_LOGICAL_NAMES fix goes first (one-liner) and this Stop hook fix follows. Retest of TEST-LOG.md rows #059–063 (AB1, AB3, P2, L1, L2 — currently Skipped) is owed after both fixes land.

---

## NO-CODE-METHOD.md → *During planning* doesn't explicitly assert planning's structural authority over BACKLOG.md

**The question.** The V25 *Before build* rewrite removed steps that previously had Claude "Group all our agreed changes and additions into the existing batches" and "Edit `BACKLOG.md` to roll the existing batched changes together with the new ones into reorganised batches." Those steps were dead weight in the subagent flow because planning has full BACKLOG.md edit authority since V22. But *During planning* itself doesn't *explicitly* assert "you do the structural batch grouping; before-build doesn't" — the assertion is implicit in the planning subagent body's *BACKLOG.md editing — do, then describe* section and in the absence of those steps from the rewritten *Before build*. Should *During planning* gain an explicit "structural authority over BACKLOG.md belongs to this phase, including grouping/sizing/splitting" assertion to close the parity loop?

**Why it matters.** Surfaced during V25 while drafting the *Before build* rewrite. Currently a future-Claude reading only *During planning* would have no way to know that before-build deliberately does NOT do reorganisation — the responsibility lives in planning by absence-elsewhere, not by explicit assertion. The asymmetry is harmless today (the planning subagent body handles it) but invites drift if either spec section gets edited later without the other in view.

**Working notes.** Three rough shapes:

- **A. Add a one-line "structural authority" assertion to *During planning*'s opening paragraph.** Smallest change. Explicit but unobtrusive.
- **B. Add a sub-section "Structural authority over BACKLOG.md" under *During planning*.** More prominent. Risks over-engineering — the assertion fits in a sentence.
- **C. Leave as-is.** The planning subagent body and the absence-in-*Before build* together communicate the rule implicitly; explicit assertion is over-documentation.

**Next step.** Park. Revisit when *During planning* next needs an edit anyway (a future session that changes planning behaviour). **Promote sooner** if a doc-code parity audit flags `plugin/agents/planning.md`'s BACKLOG-authority section as out of step with *During planning*.

---

## Subagent rule-loading pattern divergence — inline vs. read-spec-on-entry

**The question.** Subagents in the no-code-method plugin currently use two different patterns for sourcing their behavioural rules:

- **`planning.md` (V22)** and **`before-build.md` (V25)** read `NO-CODE-METHOD.md` (and `DOC-STRUCTURE.md` where relevant) at session start and follow it as the source of truth. Agent body holds operational notes only.
- **`batch-executor.md` (V25)** has the rules inlined in the body. No runtime read of `NO-CODE-METHOD.md`. Intentional per V25 Decision 4.

The two patterns have different doc-code parity profiles. Inline rules drift silently if `NO-CODE-METHOD.md` is updated and the agent body isn't. Read-spec-on-entry picks up spec changes automatically but adds prompt-time read overhead. The question: should the plugin converge on one pattern, or keep the divergence intentional with a documented rule for which agent uses which?

**Why it matters.** Surfaced during V25 before-build subagent design. The original draft proposed inline (matching batch-executor) on the framing "before-build is mechanical, like batch-executor, more than branching like planning." Validation review reframed it as **stable rules vs. fresh rules**: batch-executor inlined rules that hadn't changed in many versions (prerequisite carve-out, recap shape, MANIFEST update protocol), whereas before-build's load-bearing rules were V25-introduced (Batch-sizing principle, Pre-build verification estimate, Mid-build re-batching carve-out trigger) and likely to churn as Alex runs Taskflow builds under them. before-build landed read-spec-on-entry on that basis. Same reasoning would say batch-executor's V25-fresh content (the Two-exceptions framing, the Files: sub-section consumption) is also at parity risk — but batch-executor just shipped and was tested, so flipping it in V25 would churn settled code.

**Working notes.** Three positions:

- **A. Converge on read-spec-on-entry.** Flip batch-executor to match planning and before-build. Doc-code parity drift becomes structurally impossible for runtime behaviour: the spec is always authoritative. Cost: prompt-time read overhead on every batch-executor invocation (4 docs to load before any per-file work); structural refactor on subagent code that just landed.
- **B. Converge on inline.** Flip planning and before-build to match batch-executor. Drops the read overhead. Cost: doc-code parity audit becomes the primary discipline against drift; the audit's cadence would need formalising in `BUILD-METHOD.md`.
- **C. Keep the divergence; document the rule.** Agents whose rules are stable across versions go inline; agents whose rules are still evolving read-spec-on-entry. Re-evaluate per agent at each version bump. Cost: a new method-internal classification that has to be maintained alongside the agents.

**Next step.** Park. Revisit once V26–V31 ship and the rate of `NO-CODE-METHOD.md` changes settles into something predictable. At that point the choice is cheap: if the spec is stable across multiple consecutive versions, B is fine; if it churns, A is the safer call; if some sections are stable and others aren't, C with explicit per-agent classification. **Promote sooner** if a doc-code parity audit flags meaningful drift in `batch-executor.md`, since that would force A as the answer.

---

## MANIFEST.md schema gap blocks PreToolUse read-before-edit enforcement

**The question.** NO-CODE-METHOD.md → Required of Claude says Claude must read MANIFEST.md and the relevant UX.md entry before editing a file with a MANIFEST.md entry. V25 originally scoped a PreToolUse hook check to enforce this. The check is blocked by an architectural gap: MANIFEST.md's current schema is a flat alphabetical glossary mapping element NAMES to descriptions, not paths. A hook firing on `Edit /plugin/foo.py` has no way to know which MANIFEST entry (or which UX.md entry) `/plugin/foo.py` corresponds to. The question: how do we extend the method so hook-level enforcement becomes possible — and is it worth the change?

**Why it matters.** Surfaced in V25 chat while designing the PreToolUse boundary check + read-before-edit check pair. Deferred from V25 because the schema decision is itself method-level (the change ripples to MANIFEST-TEMPLATE.md, the plugin's MANIFEST update logic during After-every-build, and the rule's wording in NO-CODE-METHOD.md). Without resolution, the read-before-edit rule remains convention-only (lives in the SessionStart-injected universal-behaviour and is followed when Claude remembers — the ~30% drift rate per Crash course → Caveats applies).

**Working notes.** Five options sketched in V25 chat (2026-05-16):

- **A. PostToolUse-tracks-Reads + PreToolUse-checks-track.** Real enforcement. Requires a new hook type, a session-scoped state file with SessionStart cleanup, AND a MANIFEST.md schema extension (paths-per-entry) so the check can resolve "which entry covers this file." Largest cost; cleanest behavioural match to the rule.
- **B. Inline deny-with-context.** PreToolUse denies an Edit on a MANIFEST-covered file with the MANIFEST entry and UX.md entry inlined in the deny reason. No state file, no PostToolUse, but still needs the schema extension to know which entry to include. Trade-off: changes the rule's behaviour from "read first" to "have-the-context-by-edit-time." Probably acceptable; worth a separate decision.
- **C. Convention-only.** Status quo: rule lives in NO-CODE-METHOD.md and the injected universal-behaviour; no hook enforcement. No schema change. Accepts the drift rate.
- **D. Hybrid A+B.** Worst of both worlds; not pursued.
- **E. Defer.** What V25 did. Lands the question here for proper design later.

**Next step.** Promote to a planning session in the V26+ range once V25 and V26 ship and the picture is clearer. The session would resolve: (1) does MANIFEST.md gain a path field (and what format)? (2) which of A/B/C is the right enforcement shape given the answer to (1)? **Promote sooner** if direct-edit users (see entry on "Method response to direct-edit users") surface in real use, since path-mapped MANIFEST would also help drift detection for manually edited files.

---

## Stop-hook 8-block cap — only matters if we move to multi-batch-per-turn chains

**The question.** Claude Code's Stop hook applies an 8-consecutive-block cap per user turn: after 8 redirects in one turn, the turn ends with a warning regardless of what the hook returns. Override via env var `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`. The question: does our plugin need defensive design against this cap, or does our `stop_hook_active`-respecting Stop hook design make the cap inert?

**Why it matters.** Surfaced in V25 planning while wiring the Stop hook for auto-continuation. The cap would bite if a user turn produced 9+ Stop-hook redirects back-to-back — a chain of nine or more batches built without a new user turn in between.

**Working notes.** V25's Stop hook design respects `stop_hook_active` and redirects at most once per user turn (V25.md success criterion: "the user can gate between batches with a single keystroke — explicit user gating"). Chain length is always 1; the cap can't trigger. The cap would only matter in a future workflow that intentionally removes the `stop_hook_active` check to enable multi-batch chains within one turn — a different design choice, where the 8-cap would be a useful guardrail for the right reasons. No defensive code in V25.

**Next step.** Park. Revisit if a future session proposes multi-batch-per-turn auto-continuation (no current PLAN.md row for this). The cap's existence is half the design answer for that workflow — "do we chain N batches or stop at 8?" **Promote sooner** if a consumer of the method runs into the cap in normal use, which would indicate `stop_hook_active` isn't doing what we think.

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and the `[FOLD-IN PENDING]` mechanism rely on Claude Code primitives that don't exist in plain chat with Claude or in any other AI tool. For users who want the method's discipline outside the sovereign-implementer plugin entirely — in plain chat with Claude, in a different AI tool, or in any context where the plugin shape doesn't fit — we'll eventually need a prose-only rewrite of the method that works tool-agnostically: same methodology, no plugin scaffolding.

**Why it matters.** Surfaced in V20 planning. Without the rewrite, the method's current shape is structurally bound to Claude Code: source-of-truth-doc locking is enforced by PreToolUse hooks; session-start reads are injected by SessionStart hooks; routing is done by injected context. None of these primitives exist outside Claude Code. Users without Claude Code currently can't use the method as a working system. The prose-only version restores accessibility — but only after the plugin shape stabilizes, or the rewrite chases a moving target.

**Working notes.**

- The likely shape: a prose-only `NO-CODE-METHOD.md` that re-expresses every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart-hook foundational reads (becomes an at-session-start narrative in `CLAUDE.md`), PreToolUse read-only enforcement (becomes a trust-based locking convention plus chat-time flagging), slash commands (become operational procedures Claude follows from prose).
- The pluginified method is still evolving (V25–V31 ahead). Doing the rewrite before the plugin shape settles means re-doing it as the plugin shape changes.

**Next step.** Park until V31 (final E2E Taskflow test) ships and the plugin shape has settled. At that point: list each plugin-specific mechanism, design a prose-only equivalent for each, and schedule the rewrite as one or more sessions. **Promote sooner** if the method moves toward public release before the plugin migration completes — that scenario forces the rewrite onto the critical path.

---

## Track session performance over time? (AEX-style DEX/HEX)

**The question.** Should a future version of the no-code method include a lightweight session-performance log — recording what configuration (model, prompts, hooks, skills) was used in each session and a structured assessment of how it went — so that decisions about the method itself are made against accumulated evidence rather than instinct? Idea borrowed from AEX (a separate protocol — see github.com/ctenidae8/AEX_Protocol): **DEX** as a per-config reliability score earned from logged outcomes, **HEX** as a per-config domain-experience record about what tasks the config has proven good at.

**Why it matters.** Raised externally via a conversation + distilled-question artifact (URLs in V19 chat; share-link content not retrievable, artifact fetched). Worth recording rather than dropping because it points at a real long-term tension: the method develops session-by-session right now and design decisions are made on first-principles intuition. If the method were public, aggregated cross-user session evidence would have obvious value. The question is whether single-user evidence collected against an evolving method is also useful — or whether it's premature and adds noise.

**Working notes — honest assessment from V19.**

1. *Method isn't stable yet.* V19 of ~27 planned sessions plus refinement. Measuring an evolving system captures noise about its evolution, not signal about its working state. Advice fitting this stage: stabilize first (let V27 ship and run a few real project cycles on the stable method), then decide what to measure.

2. *Sample size is unworkable.* One person, one project (Taskflow), with ~30 sessions through V27 — even fully logged, the dataset is small and the variables are confounded ("did the method work?" tangles with "was Alex sharp today?" and "was the task tractable?"). Signal-to-noise per decision is low.

3. *Defining "went well" is the hardest part, and the artifact says so itself.* Without a mechanical, repeatable success criterion, "well" becomes vibes-encoded-as-data — worse than vibes alone, because numeric scores feel objective even when they aren't.

4. *Existing retrospective mechanisms already cover this work qualitatively.* `BUILD-LOG.md` captures what shipped, decisions taken, surprises, carry-forwards. `OPEN-QUESTIONS.md` captures unresolved tensions. Discoveries → planning batches captures emergent needs. These fit small-sample, single-user, evolving-method conditions. If they ever feel insufficient, the cheaper incremental move is to add structured fields to BUILD-LOG entries ("what worked / what didn't / hypothesis for next time"), not to build a separate measurement system.

5. *What current decision would this change?* V17's architecture, V18's hook-event choice, V19's hook-deny-redirect mechanic — none of these would have been called differently with a session-performance log. The artifact's own bar is "does the evidence change my decisions?" and from V19's vantage that bar isn't met.

6. *Where the idea earns its keep eventually.* If the method moves to a public release (Vibe Coding Course revival, published plugin with consumers), aggregated cross-user session data is genuinely valuable — AEX/DEX/HEX patterns are designed for that scale. Single-user, in-development is the wrong scale for the pattern. Public-future status would change the call.

**Next step.** Park. Revisit after V31 (the final E2E Taskflow test) ships and the method has settled into stable use across a few real project cycles. At that point the question becomes concrete: list 2–3 design decisions that have felt like they would have benefited from logged evidence — if non-empty, define the minimal log against those specific decisions; if empty, drop the question and record the reasoning in `BUILD-LOG.md`. **Promote sooner** if the method moves toward a public release before V31 wraps — that's the scenario where the pattern earns its keep.

---

## Cross-version template reconciliation

**The question.** When a user authors their spine docs (`UX.md`, `BACKLOG.md`, etc.) against, say, a V17 template they had locally, and then installs the no-code-method plugin (currently V19), the user's docs carry a V17 footer while the plugin's bundled templates carry V19. The structural rules between versions may differ. What does the plugin do about it?

**Why it matters.** Raised in V19 planning while discussing how bundled templates handle pre-existing user docs. A user might have hand-authored their spine docs against an older method version before installing the plugin (V17 templates downloaded from the repo, for example). When the plugin loads, the user's docs are at one version and the plugin's bundled templates are at another. If the plugin silently treats those docs as current, structural drift compounds invisibly — a V17 `UX.md` running against V19 hooks may pass checks the V19 rules tightened.

**Working notes.**

- The model I'd argue for: **plugin is the runtime source of truth; the user's footer is the version their authoring assumed.** Mismatch is a tripwire, not an error.
- Where each piece would land in the migration roadmap:
  - **V21 (SessionStart extension).** Reads the user's CLAUDE.md / UX.md footers, compares to the plugin's bundled-template versions, surfaces the mismatch (plain English, no auto-fix). One read per session-start; cheap.
  - **V28 (`/adopt` and migration skill-commands).** Does the actual diff-and-propose work — comparing the user's `UX.md` (or whichever doc is mismatched) against the bundled template's structural rules and proposing the edits to bring it up to spec. Already on the roadmap for migrating any non-conformant docs; this just gives it a specific tripwire to react to.
- The V19 piece is done already: every bundled template carries its version footer (already true; the session-close rule keeps them current).

**Next step.** Fold the tripwire half into V21's session scope (the SessionStart extension); the worker half into V28's (`/adopt` and the migration skill-commands). **Tripwire half confirmed 2026-05-14** during V21 planning — the SessionStart hook's foundational reads include the footer-comparison check (see `planning/sessions/V21.md` → *Outputs* → version-footer mismatch tripwire). Confirm during V28 planning that `/adopt` knows how to handle a version-mismatch signal. Remove this entry once the worker half also ships.

---

## Method response to direct-edit users (developers)

**The question.** How should the no-code method respond to users who edit code directly — i.e. developers who already write code and want the method's planning discipline without ceding all technical work to Claude?

**Why it matters.** Raised in Vibecord (vibe-coding Discord) — "developers will try to use it." The method as written assumes Claude does the technical work and the user reviews recaps. A user editing code directly breaks several method assumptions: `MANIFEST.md` drifts because the user's edits aren't recorded; the `BACKLOG.md` build-batch / `Serves UX.md:` discipline gets bypassed; drift checks catch *some* of it (the `MANIFEST.md` ↔ codebase check) but not all. If we don't address this, developers using the method will silently corrupt the project state and lose the benefits the method was supposed to provide.

**Working notes — three rough shapes the response could take.**

- *Tighten drift detection so manual edits get caught.* V21's `SessionStart` hook (or a `PostToolUse` hook) could compare the working tree against the last-known `MANIFEST.md` state and surface manual changes for triage. Smallest change, but only catches edits after the fact — doesn't prevent them mid-flow.
- *Add a "developer mode" entry point.* The plugin scaffolds a different doc set for developers — keeps `UX.md` / `BACKLOG.md` discipline (spec-first), drops the assumption that Claude does all the code. Requires deciding what the developer-mode equivalents of MANIFEST.md (which Claude maintains) and the build-recap flow look like.
- *Document that the method explicitly doesn't serve direct-edit users.* Add a "Who this is for" section to `NO-CODE-METHOD.md` so developers self-select out. Cheapest move but loses an audience.

**Next step.** Think during V21 (SessionStart hook extension). If drift detection covers the realistic failure modes, fold there and close the question. If not, promote to its own session somewhere in the V22–V26 range — add a row to `PLAN.md` and create a `sessions/Vxx.md` with whichever shape lands.

**V21 planning, 2026-05-14:** confirmed V21 does *not* absorb this. V21 adds foundational reads + template-state + resume + routing, none of which catch manual code edits. The natural home for the tighten-drift-detection shape is V22 (planning subagent + drift logic inlined) — or its own session if the developer-mode or "Who this is for" shapes win out instead. Question remains parked; revisit during V22 planning at the earliest, or sooner if the method moves toward public release.

**V22, 2026-05-14:** shape #1 (tighten drift detection) **partially folded into V22's planning subagent.** Q2 decision was "always run drift checks every planning session; the only skip case is 'nothing has been built yet.'" That means drift check 2 (`MANIFEST.md` ↔ codebase) now fires on every planning session regardless of whether Claude shipped a build batch in between — which catches the file-level changes a direct-edit user would make (new files, renames, deletes that touch tracked components). What it does **not** catch: in-file content changes to existing tracked files (a developer modifying a function inside a still-tracked `.kt` file leaves no MANIFEST-level signal). That gap is the remaining concern for direct-edit users. Shapes #2 (developer-mode entry point) and #3 (a "Who this is for" section in `NO-CODE-METHOD.md`) are still out of scope and would need their own session if pursued. Question stays parked: revisit if direct-edit users actually surface in the wild and the file-level coverage proves insufficient; promote sooner if public release approaches.
