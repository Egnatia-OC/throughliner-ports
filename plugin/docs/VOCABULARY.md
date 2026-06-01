# Vocabulary — Sovereign Implementer

Method-specific terms used across the plugin. Cross-references point here. Frozen prose snapshot at repo-root `VOCABULARY.md` (V39 freeze).

- **Planning batch.** Open questions in BACKLOG that must resolve before a build batch can run, or that decide whether one should exist. Resolved by folding answers into the destination source-of-truth doc.

- **Build batch.** Engineering changes in BACKLOG, small enough to build and test in one session. Ends with a `Serves` line naming the source-of-truth entries it implements. May include `Inputs:` line.

- **Files: sub-section.** `- [ ]`→`- [x]` task list of files a build batch will modify, with path and one-sentence summary. Written by `/sovrecap`; ticked during the build. PreToolUse enforces batch boundaries. Full rules: `DOC-STRUCTURE.md` → *Files: sub-section*.

- **Batch-sizing principle.** Right size = verification burden (distinct observable behaviours to test), not lines/files. Split when test list is long; bundle no-behaviour items; never fragment arbitrarily. Applied during `/sovrecap`.

- **Pre-build verification estimate.** Distinct observable behaviours needing testing, stated during `/sovrecap`. Drives batch-sizing splits. If wrong mid-build, re-batching carve-out applies.

- **Suggestion.** During planning: fix or improvement fitting current scope (existing UX.md entry covers it). Routes into a build batch.

- **Discovery.** During planning: bug or improvement outside current scope. Cannot enter a build batch directly. Promoted to planning batch asking "should this be added to UX.md?"

- **Red flag.** Security/privacy/data-integrity/safety concern. Surface in chat; if deferred with no active plan, add to BACKLOG Red flags: `**[RED FLAG]**` [description]. Found during [batch] ([date]). Fix: [fix]. Only deferred items with no UX.md entry.

- **Source-of-truth doc.** Doc describing decided behaviour the build must conform to. `UX.md` is always one. Phase-aware editing: directly editable during planning; locked during build (with `[PROPOSED EDIT PENDING]` carve-out). Full rule: `universal-behaviour.md` → *Editing surfaces — phase-aware*.

- **Additional source-of-truth doc.** Project-specific beyond UX.md — e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`. Same phase-aware rules. Spec: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.

- **`[SECURITY]` marker.** Inline tag on entries touching a sensitive surface (auth, PII, payments, deletion, access control). Applies to UX.md entries, BACKLOG build/planning batches, and BACKLOG OQs. Not MANIFEST or TEST-LOG. Informational — no hook enforcement. Claude uses it to bias security-marked items earlier in BACKLOG ordering. Format spec: `DOC-STRUCTURE.md` → *`[SECURITY]` marker*.

- **Adopted folder.** Project's CLAUDE.md carries the method footer. Safety net silent.

- **Unadopted folder.** No method footer. Safety net fires on folders with substantial content: SessionStart advisory + PreToolUse blocks. Disable via `/plugin` → Installed → toggle off. Empty folders silent.

- **Serves line.** End of a build batch naming source-of-truth entries it implements. `Serves UX.md: [names].` and/or `Serves <DOC>: ...`.

- **Drift check.** Five checks at every planning session start: (1) direct-edit detection (git-diff + per-file confirmation), (2) UX↔build, (3) MANIFEST↔codebase, (4) MANIFEST↔UX (loose), (5) TEST-LOG↔code-touch. Full procedure: `planning.md`.

- **Proposed edit.** Content queued as `[PROPOSED EDIT PENDING]` in a source-of-truth doc's *Proposed edits pending* section because the body is locked during build. User applies by hand. Only used during build — during planning, Claude edits directly. Footer stamps are the one exception to the build-phase lock.

- **Proposed-edits section.** `## Proposed edits pending` at bottom of every source-of-truth doc. Where Claude queues blocks during build. PreToolUse allows edits within this section only. Spec: `DOC-STRUCTURE.md`.

- **Inputs line.** Optional bullet list in a build batch of non-standard resources needed. Standard docs omitted. Written by `/sovrecap`; consumed during the build. Full rules: `DOC-STRUCTURE.md`.

- **Open question (BACKLOG).** Unscoped capture in BACKLOG's Open questions section. Two formats: full (question, *Why it matters*, *Next step* trigger) and light (heading, *Surfaced* tag, one sentence). Distinct from planning batches (which name what they block). Promoted when it blocks something specific. `/sovdeliberate` works through accumulated entries.

- **Planning session (not plan mode).** The method's planning phase — confirming tests, drift checks, sorting ideas, editing BACKLOG. Requires Accept edits mode. Distinct from Claude Code's plan mode (Shift+Tab), which blocks all edits.

- **Test type.** Four categories:
  - **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
  - **Run and read** — command execution, read output. Fully automatable.
  - **Trigger and observe** — set up conditions, trigger event, verify response. Fully automatable.
  - **Generate and inspect** — produce artefact, verify contents. Fully automatable.
  Recorded in TEST-LOG Type column. Verifier split is by what's checked, not by type.

- **Verifier.** TEST-LOG column: `Claude` or `User`. Claude rows filled by `/sovclose`; user rows confirmed during planning read-back.

- **Batch status.** Two active values under V99+: `queued` (default — absent = queued) and `parked` (paused by planning). Legacy `active` and `shipped` still recognized by the parser but no longer written. Build-snapshot architecture uses `_method/active-build.md` existence instead of `active`; the build-log entry replaces `shipped` as the completion record — `/sovclose` deletes the snapshot without writing the batch back. State machine: `queued → [snapshotted] → deleted (build-log is the record)`, `parked ↔ queued` via planning. Parser and session-start skip `shipped` (legacy) and `parked`. Spec: `DOC-STRUCTURE.md` → *Status: line*.

- **Scope-context sections.** Four (optionally five) sections framing a build batch: Goal, Outputs, Success criteria, Dependencies, Red flags. First three always present. Full spec: `DOC-STRUCTURE.md`.

- **Changes: delimiter.** Separates scope-context from change list in a build batch. Required for new batches; parser falls back for legacy.

- **Dependencies (batch).** What the batch needs from outside itself. Peer to `Blocks:` — Dependencies points backward, Blocks points forward.

- **Red flags sub-section (batch-level).** Conditional section for security-shaped scope. Distinct from top-level BACKLOG Red flags.

- **`_method/` folder.** Subfolder of project root containing all method spine docs except CLAUDE.md. Underscore prefix signals "method infrastructure, not user content." Created by `/sovsetup`; path block in CLAUDE.md maps logical names to `_method/` paths. Legacy projects may keep docs at root — hooks check both.

- **Proxy file.** Lightweight index in `_method/proxies/` summarizing a source-of-truth doc. Five proxies: `ux.md`, `manifest.md`, `research.md` (summaries — regenerated, not edited), plus `backlog.md` and `build-log.md` (operational indexes — directly edited). Test session index lives inside `backlog.md` → `## Test sessions`. Read proxies first, dip into full docs via offset/limit. Generated by `/sovsetup`; regenerated during planning and `/sovclose`. Missing → fall back to full doc. Spec: `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

- **Research file.** `_method/research/<topic>.md`. Findings from Claude's research. Persists indefinitely, zero maintenance. Valid on `Inputs:` lines. Spec: `DOC-STRUCTURE.md`.

- **Search query file.** `_method/research/search-queries/YYYY-MM-DD-topic-slug.md`. Structured record: trigger, decision it informs, query, good-answer criteria, response, outcome. Created by `/sovresearch`. Distinct from free-form research files. Spec: `DOC-STRUCTURE.md` → *Search query files*.

- **Proactive research.** Claude watches for decisions that would benefit from external information, drafts a search query, proposes it, and executes via MCP search tool, WebSearch, or copyable prompt. `/sovresearch` triggers explicitly; universal-behaviour rule triggers proactively. Full rule: `universal-behaviour.md` → *Proactive research*.

- **Session handoff.** Preparing a batch for clean resume: tick completed, annotate in-progress, record decisions in `Handoff notes:`, notify user. See `universal-behaviour.md` → *Session handoff*.

- **Handoff notes.** `Handoff notes:` block at batch bottom during handoff. Build-time context for resume. Stripped by `/sovclose` on completion.

- **Close handoff.** `## Close handoff` section at bottom of `_method/active-build.md`. One-liner per ticked file noting what changed — new names, renamed concepts, shifted frames, invalidated doc references. Appended incrementally during build; read by `/sovclose` for doc-parity, frame-correction, and build-log narrative. Distinct from session handoff (interrupted builds). Spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

- **Opener classification.** UserPromptSubmit hook's keyword detection on first prompt: sovsetup/test notes/resume/deliberate/plan structural. Injected as routing hint. A hint, not a gate.

- **Row pruning (TEST-LOG).** Auto-deletion of rows whose Component has no MANIFEST match, plus `Superseded` rows. Runs at planning step 2c. Cross-component rows exempt.

- **Pre-build sizing.** After Files:/Tests: are populated during `/sovrecap`, heuristic check for session fit. Triggers when Files: has 8+ entries AND unresolved Decisions. Advisory, not blocking. Full rule: `before-build.md` → *Pre-build sizing*.

- **Compact nudge.** Advisory `/compact` recommendation. Two forms: mid-session (15+ exchanges past `/sovbuild` without `/sovclose`) and invocation-prompt (appended to every skill handoff). Neither blocks — both give recovery points before context runs out. Full rule: `universal-behaviour.md` → *Session-length awareness*.

- **Halt-and-confirm.** Pattern for conditions the user must decide on: surface, propose, wait. Used by `/sovrecap` and `/sovbuild`.

- **Build log entry.** Per-build narrative in `build-log/NNN-name.md`. Shape: What shipped / Decisions / Pivots + Performance.

- **Capabilities summary.** MANIFEST section (`## Capabilities summary`) containing one plain-English paragraph summarizing what the project has built. Generated by `/sovclose` step 1b after each build from the current MANIFEST entries. The MANIFEST proxy reproduces it verbatim for session-start orientation. `/sovexplain` "what" questions read it.

- **Build recap.** Ephemeral chat summary from `/sovclose`. Persistent counterpart: build log entry.

- **Performance section.** Structured measures in each build-log file: completion, files, carve-outs, Claude-verified results, user-verified pending. Optional `Session notes:`.

- **Draft.** `_method/planning/drafts/<topic>.md`. Pre-decision carryover content. Written at "good enough to walk away from"; deleted when consumed.

- **Staleness sweep.** After-build check: scan queued/parked BACKLOG batches and OQs for literal references to file paths and names that changed in the build. Pattern-match level — checks strings, not semantics. Complements frame-correction sweep (semantic frame) and doc-parity check (spine docs).

- **Lost-feature check.** After-build check: scan for parked batches whose parking conditions were just met. Judgment-based, not mechanical.

- **Concurrent-build detection.** SessionStart check: `_method/active-build.md` exists with unticked files (or legacy `Status: active`) means a build is mid-progress. Warning asks whether resuming or parallel. Under V90+ snapshot, parallel work is safe — BACKLOG unlocked. Distinct from unclosed-build (all files ticked = build finished, `/sovclose` skipped).

- **Unclosed-build commit guard.** PreToolUse check (V132): blocks `git commit` via Bash/PowerShell when `_method/active-build.md` exists with all Files: entries ticked. Prevents orphaned snapshots from skipping `/sovclose`. Mid-build commits (some files unticked) are not blocked. Mechanical backstop for the "Do not skip the close procedure" prohibition.

- **OQ staleness detection.** SessionStart check: OQs with `Surfaced` tags older than 20 sessions are flagged in the status summary, nudging toward a deliberation session.

- **Frame-correction sweep.** After-build check: scan BACKLOG and proposed-edit blocks for references to old behaviour when a build changes a feature's frame.

- **Doc-parity check.** After-build step: for each renamed/deleted/moved file, grep spine docs for stale references. Scoped to blast radius. Findings flagged in recap.

- **Decision sweep.** After-build close step: scan the build-log entry's "Decisions taken and why" for decisions that belong in permanent homes. UX-relevant → flag (UX.md locked). Implementation-relevant → update MANIFEST rationale on the matching existing entry. Catches cross-cutting decisions that apply to MANIFEST entries not in the current batch.

- **Idea sweep.** After-build step: review session for ideas, suggestions, or observations raised but not implemented. Each triaged to BACKLOG (batch or OQ) or recap flag. Nothing left unrouted.

- **Pre-commit checkpoint.** After-build step: verify MANIFEST updated, TEST-LOG rows written, build-log entry written, idea sweep done, doc-parity done. Complete any missing steps before prompting commit.

- **After-build steps.** Optional `## After-build steps` section in CLAUDE.md. Project-specific close actions executed by `/sovclose` between standard steps and closing prompts. Examples: regenerating an API doc, updating a changelog.

- **Test session.** TEST-LOG state after a build ships. Opened by `/sovclose` (rows written). Closed by next planning session (per-row read-back). Unclosed sessions block next build.

- **Pass / Fail / Skipped.** TEST-LOG Status values. Pass: behaviour matched. Fail: didn't match (Notes required). Skipped: user chose not to test (reason required in Notes); satisfies gate only as "accounted for."

- **Test-confirmation gate.** New batch blocked while any previous-batch TEST-LOG row has `Confirmed Explicitly: No`. Hook side: PreToolUse blocks build-phase file edits. Procedure side: planning's per-row read-back.

- **Build snapshot.** `_method/active-build.md`. Extracted from BACKLOG by `/sovbuild`, deleted by `/sovclose`. Contains the active batch's full content. Its existence is the build-in-progress signal. Replaces `Status: active` for phase detection. Full spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

- **Ideas section (BACKLOG, legacy).** Pre-V109 lightest-weight capture. Date + one-liner. Replaced by light OQ format (heading + Surfaced + one sentence). Legacy sections handled gracefully by `/sovdeliberate`.

- **Cowboy test.** Informal testing where the user tests independently and reports results, as opposed to a guided `/sovtest` walkthrough. Cowboy tests are exempt from one-at-a-time walkthrough pacing. Volunteered results accepted per `testing.md` → *Volunteered results*.

- **Deliberation session.** Via `/sovdeliberate`. Works through accumulated OQs and captures new thoughts: promote, drop, re-park, or capture as light OQ. Produces build-log entry recording dispositions.

- **OQ accumulation nudge.** SessionStart and `/sovrecap` check: 3+ OQs or any older than 5 build cycles → nudge toward `/sovdeliberate`. Informational, not blocking.

- **Language setting.** `Language:` field in CLAUDE.md. Language for responses and doc content. Defaults to English. Control tokens (`Status:`, `Changes:`, etc.) stay English — hooks regex-match them. Set during `/sovsetup`; migrated by case 4. Full rule: `universal-behaviour.md` → *Respect the Language: field*.

- **Pre-build blocker gate.** Check during `/sovrecap`: scan top batch for unresolved items that would force mid-build improvisation. If found, halt and nudge `/sovdeliberate` or `/sovplan`. Distinct from pre-build sizing (session-fit risk, not scope completeness). Full rule: `before-build.md` → *Blocker gate*.

---
*Sovereign Implementer — Version 110.*
