# Vocabulary — no-code method

Method-specific terms used across the plugin. Cross-references point here. Frozen prose snapshot at repo-root `VOCABULARY.md` (V39 freeze).

- **Planning batch.** Open questions in BUILD-PLAN that must resolve before a build batch can run, or that decide whether one should exist. Resolved by folding answers into the relevant source-of-truth doc.

- **Build batch.** Engineering changes in BUILD-PLAN, small enough to build and test in one session. Ends with a `Serves` line naming the source-of-truth entries it implements. May include `Inputs:` line.

- **Files: sub-section.** `- [ ]`→`- [x]` task list of files a build batch will modify, with path and one-sentence summary. Written by `/sovrecap`; ticked during the build. PreToolUse enforces batch boundaries. Full rules: `DOC-STRUCTURE.md` → *Files: sub-section*.

- **Batch-sizing principle.** Right size = verification burden (distinct observable behaviours to test), not lines/files. Split when small batch has long test list; bundle no-behaviour items; never fragment arbitrarily. Applied during `/sovrecap`.

- **Pre-build verification estimate.** List of distinct observable behaviours needing testing, stated during `/sovrecap`. Drives batch-sizing splits. If wrong mid-build, re-batching carve-out applies.

- **Suggestion.** During planning: fix or improvement fitting current scope (existing UX.md entry covers it). Routed into a build batch.

- **Discovery.** During planning: bug or improvement outside current scope. Cannot enter a build batch directly. Promoted to a planning batch asking "should this be added to UX.md?"

- **Red flag.** Security/privacy/data-integrity/safety concern. Surface in chat; if deferred with no active plan, add to BUILD-PLAN Red flags: `**[RED FLAG]**` [description]. Found during [batch] ([date]). Fix: [fix]. Only deferred items not needing a UX.md entry.

- **Source-of-truth doc.** Doc describing decided behaviour the build must conform to. `UX.md` is always one. Phase-aware editing: directly editable during planning; locked during build (with `[PROPOSED EDIT PENDING]` carve-out). Full rule: `universal-behaviour.md` → *Editing surfaces — phase-aware*.

- **Additional source-of-truth doc.** Project-specific beyond UX.md — e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`. Same phase-aware rules. Full rules: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.

- **`[SECURITY]` marker.** Inline tag on entries that touch a sensitive surface (auth, PII, payments, deletion, access control). Applies to UX.md entries, BUILD-PLAN build/planning batches, and BUILD-PLAN open questions. Not MANIFEST or TEST-LOG. Informational — no hook enforcement. Claude uses it as a prioritization input when ordering BUILD-PLAN (security-marked items bias earlier). Format spec: `DOC-STRUCTURE.md` → *`[SECURITY]` marker*.

- **Adopted folder.** Project's CLAUDE.md carries the method footer. Safety net stays silent.

- **Unadopted folder.** No method footer. Safety net fires on folders with substantial content: SessionStart advisory + PreToolUse blocks. Disable via `/plugin` → Installed → toggle off. Empty folders stay silent.

- **Serves line.** End of a build batch naming source-of-truth entries it implements. `Serves UX.md: [names].` and/or `Serves <DOC>: ...`.

- **Drift check.** Five checks at every planning session start: (1) direct-edit detection (git-diff + per-file confirmation), (2) UX↔build, (3) MANIFEST↔codebase, (4) MANIFEST↔UX (loose), (5) TEST-LOG↔code-touch. Full procedure: `planning.md`.

- **Proposed edit.** Content queued as `[PROPOSED EDIT PENDING]` in a source-of-truth doc's *Proposed edits pending* section because the main body is locked during build phase. User applies by hand. Origins: intercepted mid-build edit. Only used during build phase — during planning, Claude edits source-of-truth docs directly. Footer stamps are the one exception to the build-phase lock.

- **Proposed-edits section.** `## Proposed edits pending` at bottom of every source-of-truth doc. Where Claude queues blocks during build phase. PreToolUse allows edits within this section only (during build). Full spec: `DOC-STRUCTURE.md`.

- **Inputs line.** Optional bullet list in a build batch of non-standard resources needed. Standard docs omitted. Written by `/sovrecap`; consumed during the build. Full rules: `DOC-STRUCTURE.md`.

- **Open question (BUILD-PLAN).** Non-blocking parking in BUILD-PLAN's Open questions section. Has question, *Why it matters*, *Next step* trigger. Distinct from planning batches (which name what they block). Promoted to planning batch when it blocks something specific.

- **Planning session (not plan mode).** The method's planning phase — confirming tests, drift checks, sorting ideas, editing BUILD-PLAN. Requires Accept edits mode (planning procedure writes to BUILD-PLAN). Distinct from Claude Code's plan mode (Shift+Tab), which blocks all edits.

- **Test type.** Four categories:
  - **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
  - **Run and read** — command execution, read output. Fully automatable.
  - **Trigger and observe** — set up conditions, trigger event, verify response. Fully automatable.
  - **Generate and inspect** — produce artefact, verify contents. Fully automatable.
  Recorded in TEST-LOG Type column. Verifier split is by what's checked, not by type.

- **Verifier.** TEST-LOG column: `Claude` or `User`. Claude rows filled by `/sovclose`; user rows confirmed during planning read-back.

- **Batch status.** Lifecycle state of a build batch. Three values under V90+: `queued` (default — absent means queued), `parked` (paused by planning), `shipped` (completed by `/sovclose`). Legacy `active` value still recognized for pre-V90 projects — replaced by the build-snapshot architecture where `_method/active-build.md` existence signals an active build. The parser and session-start hook skip `shipped` and `parked` batches. State machine: `queued → [snapshotted] → shipped`, with `parked ↔ queued` via planning. Full spec: `DOC-STRUCTURE.md` → *Status: line*.

- **Scope-context sections.** Five (optionally six) sections framing a build batch: Goal, Outputs, Success criteria, Decisions, Dependencies, Red flags. First three always present. Full spec: `DOC-STRUCTURE.md`.

- **Changes: delimiter.** Separates scope-context from change list in a build batch. Required for new batches; parser falls back for legacy.

- **Decisions to make this batch.** Unresolved scope questions within a batch. Distinct from Open questions (non-blocking) and planning batches (blocking with `Blocks:` line).

- **Dependencies (batch).** What the batch needs from outside itself. Peer to `Blocks:` — Dependencies points backward, Blocks points forward.

- **Red flags sub-section (batch-level).** Conditional section for security-shaped scope. Distinct from top-level BUILD-PLAN Red flags.

- **`_method/` folder.** Subfolder of the project root containing all method spine docs except CLAUDE.md. Keeps the project root clean — underscore prefix signals "method infrastructure, not user content." Created by `/sovsetup`; path block in CLAUDE.md maps logical doc names to `_method/` paths. Legacy projects may keep docs at root — hooks check both locations.

- **Proxy file.** Lightweight index in `_method/proxies/` summarizing a source-of-truth doc. Six proxies: `ux.md`, `manifest.md`, `test-log.md`, `research.md` (summaries — regenerated, not edited), plus `build-plan.md` and `build-log.md` (operational indexes — directly edited, carrying the reference lists for their respective folders). Claude reads proxies first, dips into full docs via offset/limit for detail. Generated by `/sovsetup`; regenerated during planning and `/sovclose`. Missing proxies → fall back to full doc. Format spec: `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

- **Research file.** `_method/research/<topic>.md`. Findings from Claude's research. Persists indefinitely, zero maintenance. Valid on `Inputs:` lines. Full rules: `DOC-STRUCTURE.md`.

- **Search query file.** `_method/research/search-queries/YYYY-MM-DD-topic-slug.md`. Structured record of a research query: trigger, decision it informs, query, good-answer criteria, response, outcome. Created by the `/sovresearch` flow. Distinct from free-form research files. Full spec: `DOC-STRUCTURE.md` → *Search query files*.

- **Proactive research.** Claude watches for decisions that would benefit from external information, drafts a search query, proposes it to the user, and executes via MCP search tool, WebSearch, or copyable prompt. `/sovresearch` triggers the flow explicitly; the universal-behaviour rule triggers it proactively. Full rule: `universal-behaviour.md` → *Proactive research*.

- **Session handoff.** Preparing a batch for clean resume: tick completed, annotate in-progress, record decisions in `Handoff notes:`, notify user. Protocol: `universal-behaviour.md` → *Session handoff*.

- **Handoff notes.** `Handoff notes:` block at batch bottom during handoff. Build-time context for resume. Stripped by `/sovclose` when batch completes.

- **Close handoff.** `## Close handoff` section at the bottom of `_method/active-build.md`. One-liner per ticked file noting what changed — new consumer-facing names, renamed concepts, shifted frames, invalidated doc references. Appended incrementally by the build procedure; read by `/sovclose` for doc-parity, frame-correction, and build-log narrative. Distinct from session handoff (which is for interrupted builds resuming in a new session). Format spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

- **Opener classification.** UserPromptSubmit hook's keyword detection on first prompt: sovsetup/test notes/resume/deliberate/ideate/plan structural. Injected as routing hint. Conservative. A hint, not a gate.

- **Row pruning (TEST-LOG).** Auto-deletion of rows whose Component has no MANIFEST match, plus `Superseded` rows. Runs at planning step 2c. Cross-component rows exempt.

- **Pre-build sizing.** After Files:/Tests: are populated during `/sovrecap`, a heuristic check for whether the batch fits in one session. Triggers when Files: has 8+ entries AND the batch has unresolved Decisions. Advisory warning — not blocking. Full rule: `before-build.md` → *Pre-build sizing*.

- **Compact nudge.** Advisory recommendation to run `/compact` before the next skill invocation. Two forms: mid-session (15+ exchanges past `/sovbuild` without `/sovclose`) and invocation-prompt (appended to every skill handoff message). Neither blocks — both give recovery points before context runs out. Full rule: `universal-behaviour.md` → *Session-length awareness*.

- **Halt-and-confirm.** Pattern for conditions the user must decide on: surface, propose, wait. Used by `/sovrecap` and `/sovbuild`.

- **Build log entry.** Per-build narrative in `build-log/NNN-name.md`. Shape: What shipped / Decisions / Pivots + Performance section.

- **Build recap.** Ephemeral chat summary from `/sovclose`. Persistent counterpart is the build log entry.

- **Performance section.** Structured measures in each build-log file: completion, files, carve-outs, Claude-verified results, user-verified pending. Optional `Session notes:`.

- **Draft.** `_method/planning/drafts/<topic>.md`. Pre-decision carryover content. Written at "good enough to walk away from"; deleted when consumed.

- **Staleness sweep.** After-build check (close step 9): scan queued and parked BUILD-PLAN batches and open questions for literal references to file paths and names that changed in the build. Pattern-match level — checks strings, not semantics. Complements the frame-correction sweep (which checks semantic frame) and doc-parity check (which checks spine docs).

- **Lost-feature check.** After-build check (close step 10): scan for items that silently fell off the roadmap — parked batches whose parking conditions were just met. Judgment-based, not mechanical.

- **Concurrent-build detection.** SessionStart check: when `_method/active-build.md` exists with unticked files (or legacy: `Status: active` with unticked files), a build is mid-progress. Warning asks the user whether they're resuming or working in parallel. Under V90+ snapshot architecture, parallel work is safe — BUILD-PLAN is unlocked. Distinct from unclosed-build detection (all files ticked = build finished, `/sovclose` skipped).

- **OQ staleness detection.** SessionStart check: open questions with `Surfaced` session tags older than a configurable threshold (default: 20 sessions) are flagged in the status summary, nudging the user toward a deliberation session.

- **Frame-correction sweep.** After-build check: scan BUILD-PLAN and proposed-edit blocks for references to old behaviour when a build changes a feature's frame.

- **Doc-parity check.** After-build step: for each renamed/deleted/moved file in the batch, grep spine docs (UX.md, BUILD-PLAN, MANIFEST.md, CLAUDE.md) for stale references. Scoped to blast radius. Findings flagged in recap.

- **Idea sweep.** After-build step: review the session for ideas, suggestions, or observations raised but not implemented. Each triaged to BUILD-PLAN (batch or open question) or recap flag for user to decide. Nothing left unrouted.

- **Pre-commit checkpoint.** After-build step: verify MANIFEST updated, TEST-LOG rows written, build-log entry written, idea sweep done, doc-parity check done. Complete any missing steps before prompting commit.

- **After-build steps.** Optional `## After-build steps` section in CLAUDE.md. Project-specific close actions executed by `/sovclose` between standard steps and closing prompts. Examples: regenerating an API doc, updating a changelog.

- **Test session.** TEST-LOG state after a build ships. Opened by `/sovclose` (rows written). Closed by next planning session (per-row read-back). Unclosed sessions block next build.

- **Pass / Fail / Skipped.** TEST-LOG Status values. Pass: behaviour matched. Fail: didn't match (Notes required). Skipped: user chose not to test (reason required in Notes); satisfies gate only as "accounted for."

- **Test-confirmation gate.** New batch blocked while any previous-batch TEST-LOG row has `Confirmed Explicitly: No`. Hook side: PreToolUse blocks build-phase file edits. Procedure side: planning's per-row read-back.

- **Build snapshot.** `_method/active-build.md`. Extracted from BUILD-PLAN by `/sovbuild`, deleted by `/sovclose`. Contains the active batch's full content. Its existence is the build-in-progress signal. Replaces `Status: active` for phase detection. Full spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

- **Ideas section (BUILD-PLAN).** Lightest-weight capture for raw ideas. Date + one-liner. Writable during any phase. Promoted to OQs or batches by `/sovideate` or `/sovdeliberate`.

- **Deliberation session.** Session type invoked via `/sovdeliberate`. Works through accumulated open questions: promote, drop, or re-park each one. Produces a build-log entry recording dispositions.

- **Ideation session.** Session type invoked via `/sovideate`. Explores a fresh concept: discuss, assess fit, route to OQ/batch/idea/drop. Lighter than planning — no drift checks, no test read-back.

- **OQ accumulation nudge.** SessionStart and `/sovrecap` check: when 3+ open questions exist or any are older than 5 build cycles, nudge toward `/sovdeliberate`. Informational, not blocking.

- **Language setting.** `Language:` field in CLAUDE.md. Tells Claude what language to use for responses and doc content. Defaults to English. Control tokens (`Status:`, `Changes:`, etc.) stay English regardless — hooks regex-match them. Set during `/sovsetup`; migrated by case 4 refresh. Full rule: `universal-behaviour.md` → *Respect the Language: field*.

- **Pre-build blocker gate.** Check during `/sovrecap`: scan the top batch for unresolved open questions or ideas that would force mid-build improvisation. If blockers found, halt and nudge `/sovdeliberate` or `/sovplan`. Distinct from pre-build sizing (which checks session-fit risk, not scope completeness). Full rule: `before-build.md` → *Blocker gate*.

---
*No-code method — Version 96.*
