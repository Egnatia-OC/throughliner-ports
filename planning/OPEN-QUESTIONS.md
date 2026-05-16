# Open questions

Method-level questions that have been raised but aren't yet ready to be a session. Each entry stays here until the question resolves — at which point it either folds into an existing session's scope, becomes its own new session (with a row added to `PLAN.md` and a new `sessions/Vxx.md`), or is consciously dropped with a one-line reason recorded in `BUILD-LOG.md` so future-me knows it was considered.

Newest first. Removed when resolved.

For the format and lifecycle, see project `CLAUDE.md` → *Open questions*.

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and the `[FOLD-IN PENDING]` mechanism rely on Claude Code primitives that don't exist in plain chat with Claude or in any other AI tool. For users who want the method's discipline outside the sovereign-implementer plugin entirely — in plain chat with Claude, in a different AI tool, or in any context where the plugin shape doesn't fit — we'll eventually need a prose-only rewrite of the method that works tool-agnostically: same methodology, no plugin scaffolding.

**Why it matters.** Surfaced in V20 planning. Without the rewrite, the method's current shape is structurally bound to Claude Code: source-of-truth-doc locking is enforced by PreToolUse hooks; session-start reads are injected by SessionStart hooks; routing is done by injected context. None of these primitives exist outside Claude Code. Users without Claude Code currently can't use the method as a working system. The prose-only version restores accessibility — but only after the plugin shape stabilizes, or the rewrite chases a moving target.

**Working notes.**

- The likely shape: a prose-only `NO-CODE-METHOD.md` that re-expresses every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart-hook foundational reads (becomes an at-session-start narrative in `CLAUDE.md`), PreToolUse read-only enforcement (becomes a trust-based locking convention plus chat-time flagging), slash commands (become operational procedures Claude follows from prose).
- The pluginified method is still evolving (V24–V30 ahead). Doing the rewrite before the plugin shape settles means re-doing it as the plugin shape changes.

**Next step.** Park until V30 (final E2E Taskflow test) ships and the plugin shape has settled. At that point: list each plugin-specific mechanism, design a prose-only equivalent for each, and schedule the rewrite as one or more sessions. **Promote sooner** if the method moves toward public release before the plugin migration completes — that scenario forces the rewrite onto the critical path.

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

**Next step.** Park. Revisit after V27 ships and the method has settled into stable use across a few real project cycles. At that point the question becomes concrete: list 2–3 design decisions that have felt like they would have benefited from logged evidence — if non-empty, define the minimal log against those specific decisions; if empty, drop the question and record the reasoning in `BUILD-LOG.md`. **Promote sooner** if the method moves toward a public release before V27 wraps — that's the scenario where the pattern earns its keep.

---

## Cross-version template reconciliation

**The question.** When a user authors their spine docs (`UX.md`, `BACKLOG.md`, etc.) against, say, a V17 template they had locally, and then installs the no-code-method plugin (currently V19), the user's docs carry a V17 footer while the plugin's bundled templates carry V19. The structural rules between versions may differ. What does the plugin do about it?

**Why it matters.** Raised in V19 planning while discussing how bundled templates handle pre-existing user docs. A user might have hand-authored their spine docs against an older method version before installing the plugin (V17 templates downloaded from the repo, for example). When the plugin loads, the user's docs are at one version and the plugin's bundled templates are at another. If the plugin silently treats those docs as current, structural drift compounds invisibly — a V17 `UX.md` running against V19 hooks may pass checks the V19 rules tightened.

**Working notes.**

- The model I'd argue for: **plugin is the runtime source of truth; the user's footer is the version their authoring assumed.** Mismatch is a tripwire, not an error.
- Where each piece would land in the migration roadmap:
  - **V21 (SessionStart extension).** Reads the user's CLAUDE.md / UX.md footers, compares to the plugin's bundled-template versions, surfaces the mismatch (plain English, no auto-fix). One read per session-start; cheap.
  - **V27 (`/migrate` and migration skill-commands).** Does the actual diff-and-propose work — comparing the user's `UX.md` (or whichever doc is mismatched) against the bundled template's structural rules and proposing the edits to bring it up to spec. Already on the roadmap for migrating any non-conformant docs; this just gives it a specific tripwire to react to.
- The V19 piece is done already: every bundled template carries its version footer (already true; the session-close rule keeps them current).

**Next step.** Fold the tripwire half into V21's session scope (the SessionStart extension); the worker half into V27's (`/migrate` and the migration skill-commands). **Tripwire half confirmed 2026-05-14** during V21 planning — the SessionStart hook's foundational reads include the footer-comparison check (see `planning/sessions/V21.md` → *Outputs* → version-footer mismatch tripwire). Confirm during V27 planning that `/migrate` knows how to handle a version-mismatch signal. Remove this entry once the worker half also ships.

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
