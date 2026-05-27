# Vocabulary — no-code method

Method-specific terms used across the plugin. Cross-references point here. Frozen prose snapshot at repo-root `VOCABULARY.md` (V39 freeze).

- **Planning batch.** Open questions in BACKLOG that must resolve before a build batch can run, or that decide whether one should exist. Resolved by folding answers into the relevant source-of-truth doc.

- **Build batch.** Engineering changes in BACKLOG, small enough to build and test in one session. Ends with a `Serves` line naming the source-of-truth entries it implements. May include `Inputs:` line.

- **Files: sub-section.** `- [ ]`→`- [x]` task list of files a build batch will modify, with path and one-sentence summary. Written by `/sovrecap`; ticked during the build. PreToolUse enforces batch boundaries. Full rules: `DOC-STRUCTURE.md` → *Files: sub-section*.

- **Batch-sizing principle.** Right size = verification burden (distinct observable behaviours to test), not lines/files. Split when small batch has long test list; bundle no-behaviour items; never fragment arbitrarily. Applied during `/sovrecap`.

- **Pre-build verification estimate.** List of distinct observable behaviours needing testing, stated during `/sovrecap`. Drives batch-sizing splits. If wrong mid-build, re-batching carve-out applies.

- **Suggestion.** During planning: fix or improvement fitting current scope (existing UX.md entry covers it). Routed into a build batch.

- **Discovery.** During planning: bug or improvement outside current scope. Cannot enter a build batch directly. Promoted to a planning batch asking "should this be added to UX.md?"

- **Red flag.** Security/privacy/data-integrity/safety concern. Surface in chat; if deferred with no active plan, add to BACKLOG Red flags: `**[RED FLAG]**` [description]. Found during [batch] ([date]). Fix: [fix]. Only deferred items not needing a UX.md entry.

- **Source-of-truth doc.** Doc describing decided behaviour the build must conform to. `UX.md` is always one. Phase-aware editing: directly editable during planning; locked during build (with `[PROPOSED EDIT PENDING]` carve-out). Full rule: `universal-behaviour.md` → *Editing surfaces — phase-aware*.

- **Additional source-of-truth doc.** Project-specific beyond UX.md — e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`. Same phase-aware rules. Full rules: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.

- **`[SECURITY]` marker.** Inline tag on entries that touch a sensitive surface (auth, PII, payments, deletion, access control). Applies to UX.md entries, BACKLOG build/planning batches, and BACKLOG open questions. Not MANIFEST or TEST-LOG. Informational — no hook enforcement. Claude uses it as a prioritization input when ordering BACKLOG (security-marked items bias earlier). Format spec: `DOC-STRUCTURE.md` → *`[SECURITY]` marker*.

- **Adopted folder.** Project's CLAUDE.md carries the method footer. Safety net stays silent.

- **Unadopted folder.** No method footer. Safety net fires on folders with substantial content: SessionStart advisory + PreToolUse blocks. Disable via `/plugin` → Installed → toggle off. Empty folders stay silent.

- **Serves line.** End of a build batch naming source-of-truth entries it implements. `Serves UX.md: [names].` and/or `Serves <DOC>: ...`.

- **Drift check.** Five checks at every planning session start: (1) direct-edit detection (git-diff + per-file confirmation), (2) UX↔build, (3) MANIFEST↔codebase, (4) MANIFEST↔UX (loose), (5) TEST-LOG↔code-touch. Full procedure: `planning.md`.

- **Proposed edit.** Content queued as `[PROPOSED EDIT PENDING]` in a source-of-truth doc's *Proposed edits pending* section because the main body is locked during build phase. User applies by hand. Origins: intercepted mid-build edit. Only used during build phase — during planning, Claude edits source-of-truth docs directly. Footer stamps are the one exception to the build-phase lock.

- **Proposed-edits section.** `## Proposed edits pending` at bottom of every source-of-truth doc. Where Claude queues blocks during build phase. PreToolUse allows edits within this section only (during build). Full spec: `DOC-STRUCTURE.md`.

- **Inputs line.** Optional bullet list in a build batch of non-standard resources needed. Standard docs omitted. Written by `/sovrecap`; consumed during the build. Full rules: `DOC-STRUCTURE.md`.

- **Open question (BACKLOG).** Non-blocking parking in BACKLOG's Open questions section. Has question, *Why it matters*, *Next step* trigger. Distinct from planning batches (which name what they block). Promoted to planning batch when it blocks something specific.

- **Planning session (not plan mode).** The method's planning phase — confirming tests, drift checks, sorting ideas, editing BACKLOG. Requires Accept edits mode (planning procedure writes to BACKLOG). Distinct from Claude Code's plan mode (Shift+Tab), which blocks all edits.

- **Test type.** Four categories:
  - **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
  - **Run and read** — command execution, read output. Fully automatable.
  - **Trigger and observe** — set up conditions, trigger event, verify response. Fully automatable.
  - **Generate and inspect** — produce artefact, verify contents. Fully automatable.
  Recorded in TEST-LOG Type column. Verifier split is by what's checked, not by type.

- **Verifier.** TEST-LOG column: `Claude` or `User`. Claude rows filled by `/sovclose`; user rows confirmed during planning read-back.

- **Batch status.** Lifecycle state of a build batch, tracked via an optional `Status:` line at the top of the batch body. Four values: `queued` (default — absent means queued), `active` (locked by `/sovbuild`), `parked` (paused by planning), `shipped` (completed by `/sovclose`). The parser and session-start hook skip `shipped` and `parked` batches when finding the top build batch. State machine: `queued → active → shipped`, with `active ↔ parked` via planning. Full spec: `DOC-STRUCTURE.md` → *Status: line*.

- **Scope-context sections.** Five (optionally six) sections framing a build batch: Goal, Outputs, Success criteria, Decisions, Dependencies, Red flags. First three always present. Full spec: `DOC-STRUCTURE.md`.

- **Changes: delimiter.** Separates scope-context from change list in a build batch. Required for new batches; parser falls back for legacy.

- **Decisions to make this batch.** Unresolved scope questions within a batch. Distinct from Open questions (non-blocking) and planning batches (blocking with `Blocks:` line).

- **Dependencies (batch).** What the batch needs from outside itself. Peer to `Blocks:` — Dependencies points backward, Blocks points forward.

- **Red flags sub-section (batch-level).** Conditional section for security-shaped scope. Distinct from top-level BACKLOG Red flags.

- **`_method/` folder.** Subfolder of the project root containing all method spine docs except CLAUDE.md. Keeps the project root clean — underscore prefix signals "method infrastructure, not user content." Created by `/sovsetup`; path block in CLAUDE.md maps logical doc names to `_method/` paths. Legacy projects may keep docs at root — hooks check both locations.

- **Proxy file.** Lightweight index in `_method/proxies/` summarizing a source-of-truth doc. Six proxies: `ux.md`, `manifest.md`, `test-log.md`, `research.md` (summaries — regenerated, not edited), plus `backlog.md` and `build-log.md` (operational indexes — directly edited, carrying the reference lists for their respective folders). Claude reads proxies first, dips into full docs via offset/limit for detail. Generated by `/sovsetup`; regenerated during planning and `/sovclose`. Missing proxies → fall back to full doc. Format spec: `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

- **Research file.** `_method/research/<topic>.md`. Findings from Claude's research. Persists indefinitely, zero maintenance. Valid on `Inputs:` lines. Full rules: `DOC-STRUCTURE.md`.

- **Search query file.** `_method/research/search-queries/YYYY-MM-DD-topic-slug.md`. Structured record of a research query: trigger, decision it informs, query, good-answer criteria, response, outcome. Created by the `/sovresearch` flow. Distinct from free-form research files. Full spec: `DOC-STRUCTURE.md` → *Search query files*.

- **Proactive research.** Claude watches for decisions that would benefit from external information, drafts a search query, proposes it to the user, and executes via MCP search tool, WebSearch, or copyable prompt. `/sovresearch` triggers the flow explicitly; the universal-behaviour rule triggers it proactively. Full rule: `universal-behaviour.md` → *Proactive research*.

- **Session handoff.** Preparing a batch for clean resume: tick completed, annotate in-progress, record decisions in `Handoff notes:`, notify user. Protocol: `universal-behaviour.md` → *Session handoff*.

- **Handoff notes.** `Handoff notes:` block at batch bottom during handoff. Build-time context for resume. Stripped by `/sovclose` when batch completes.

- **Opener classification.** UserPromptSubmit hook's keyword detection on first prompt: sovsetup/test notes/resume. Injected as routing hint. Conservative. A hint, not a gate.

- **Row pruning (TEST-LOG).** Auto-deletion of rows whose Component has no MANIFEST match, plus `Superseded` rows. Runs at planning step 2c. Cross-component rows exempt.

- **Halt-and-confirm.** Pattern for conditions the user must decide on: surface, propose, wait. Used by `/sovrecap` and `/sovbuild`.

- **Build log entry.** Per-build narrative in `build-log/NNN-name.md`. Shape: What shipped / Decisions / Pivots / Carried forward + Performance section.

- **Build recap.** Ephemeral chat summary from `/sovclose`. Persistent counterpart is the build log entry.

- **Performance section.** Structured measures in each build-log file: completion, files, carve-outs, Claude-verified results, user-verified pending. Optional `Session notes:`.

- **Draft.** `_method/planning/drafts/<topic>.md`. Pre-decision carryover content. Written at "good enough to walk away from"; deleted when consumed.

- **Frame-correction sweep.** After-build check: scan BACKLOG and proposed-edit blocks for references to old behaviour when a build changes a feature's frame.

- **Doc-parity check.** After-build step: for each renamed/deleted/moved file in the batch, grep spine docs (UX.md, BACKLOG, MANIFEST.md, CLAUDE.md) for stale references. Scoped to blast radius. Findings flagged in recap.

- **Idea sweep.** After-build step: review the session for ideas, suggestions, or observations raised but not implemented. Each triaged to BACKLOG, build-log *Carried forward*, or recap flag. Nothing left unrouted.

- **Pre-commit checkpoint.** After-build step: verify MANIFEST updated, TEST-LOG rows written, build-log entry written, idea sweep done, doc-parity check done. Complete any missing steps before prompting commit.

- **After-build steps.** Optional `## After-build steps` section in CLAUDE.md. Project-specific close actions executed by `/sovclose` between standard steps and closing prompts. Examples: regenerating an API doc, updating a changelog.

- **Test session.** TEST-LOG state after a build ships. Opened by `/sovclose` (rows written). Closed by next planning session (per-row read-back). Unclosed sessions block next build.

- **Pass / Fail / Skipped.** TEST-LOG Status values. Pass: behaviour matched. Fail: didn't match (Notes required). Skipped: user chose not to test (reason required in Notes); satisfies gate only as "accounted for."

- **Test-confirmation gate.** New batch blocked while any previous-batch TEST-LOG row has `Confirmed Explicitly: No`. Hook side: PreToolUse blocks build-phase file edits. Procedure side: planning's per-row read-back.

---
*No-code method — Version 88.*
