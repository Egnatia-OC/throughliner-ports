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

**Next step.** **Indefinitely shelved** (session v61, 2026-05-23). Previously promoted to 0059; scope file deleted, row moved to V60+ parking lot in PLAN.md. All four prerequisites shipped, but E2E testing (0060) revealed the plugin needs efficiency and correctness fixes (0063–0068) before dogfooding is practical. Restore when the method is stable enough to run its own dev project without burning excessive tokens or hitting missing migration paths.

---

---

## Prose-only rewrite of the method (post-plugin-build)

**The question.** The plugin-based method (V17 onwards) is Claude-Code-specific — hooks, slash commands, and `[PROPOSED EDIT PENDING]` rely on Claude Code primitives. For users wanting the method's discipline in plain chat with Claude, another AI tool, or any context where the plugin shape doesn't fit, we'll eventually need a tool-agnostic prose-only rewrite.

**Why it matters.** Surfaced V20 planning. Without the rewrite, the method is structurally bound to Claude Code: locking via PreToolUse, session-start reads via SessionStart, routing via injected context. None exist elsewhere. Users without Claude Code can't run the method as a working system. Prose-only restores accessibility — but only after the plugin shape stabilises, or the rewrite chases a moving target.

**Working notes.**

- Likely shape: prose-only `NO-CODE-METHOD.md` re-expressing every plugin-enforced rule as a discipline held in conversation. Plain-prose equivalents needed for: SessionStart foundational reads (becomes at-session-start narrative in `CLAUDE.md`), PreToolUse locking (trust-based convention + chat-time flagging), slash commands (operational procedures in prose).
- Plugin still evolving (V32–V35 ahead). Rewriting before it settles means redoing.

**V37, 2026-05-21: rewrite delivered by V32; entry overtaken.** V32's two-write rule split canonical method content into plugin-side (operational) and docs-only (project-agnostic) artefact sets. The docs-only side at the repo root — `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/` — is the prose-only rewrite this entry called for. Ongoing parity is held by the two-write discipline (`BUILD-METHOD.md` → *Two-write rule for canonical docs*), not by a future rewrite session.

**Next step.** **Indefinitely parked** (session v47, 2026-05-22). Kept as last entry in OPEN-QUESTIONS. Promote if a real audience for the prose-only set emerges (public release, non-Claude-Code users).
