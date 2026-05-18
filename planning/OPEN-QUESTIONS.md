# Open questions

Method-level questions raised but not yet ready to be a session. Each entry stays until it resolves — folded into a session's scope, promoted to its own session (row in `PLAN.md`, `sessions/Vxx.md`), or consciously dropped with a one-line reason in `BUILD-LOG.md`.

Newest first. Removed when resolved.

Format and lifecycle: see project `CLAUDE.md` → *Open questions*.

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

## Cross-version template reconciliation

**The question.** A user authors spine docs (`UX.md`, `BACKLOG.md`, etc.) against, say, a locally-held V17 template, then installs the plugin (currently V19). User's docs carry a V17 footer; plugin's bundled templates carry V19. Structural rules between versions may differ. What does the plugin do?

**Why it matters.** Raised in V19 planning while discussing bundled-template handling of pre-existing docs. If the plugin silently treats older docs as current, structural drift compounds invisibly — a V17 `UX.md` running against V19 hooks may pass checks the V19 rules tightened.

**Working notes.**

- Model to argue for: **plugin is the runtime source of truth; user's footer is the version their authoring assumed.** Mismatch is a tripwire, not an error.
- Migration roadmap placement:
  - **V21 (SessionStart extension).** Reads user's CLAUDE.md / UX.md footers, compares to bundled-template versions, surfaces mismatch in plain English. No auto-fix. One read per session-start; cheap.
  - **V28 (`/adopt` and migration skill-commands).** Diff-and-propose: compares user's doc against the bundled template's structural rules, proposes edits to bring it up to spec. Already on the roadmap; this gives it a specific tripwire to react to.
- V19 piece is done: every bundled template carries its version footer (session-close rule keeps them current).

**Next step.** Fold tripwire half into V21 (SessionStart extension); worker half into V28 (`/adopt` and migration skill-commands). **Tripwire half confirmed 2026-05-14** during V21 planning — SessionStart's foundational reads include the footer-comparison check (see `planning/sessions/V21.md` → *Outputs*). Confirm during V28 planning that `/adopt` handles a version-mismatch signal. Remove this entry once the worker half also ships.

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
