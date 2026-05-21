# Vocabulary — no-code method

Method-specific terms used across the plugin (subagent bodies, hook deny messages, slash commands, templates). Cross-references elsewhere point here rather than redefining inline. A frozen prose snapshot of these definitions exists at `VOCABULARY.md` in the no-code-method repo root (V39 freeze — two-write rule shelved in session v40).

- **Planning batch.** Open questions in `BACKLOG.md` that must resolve before a build batch can run, or that decide whether a build batch should exist (a *scope-existence* question). Resolved by folding answers into the relevant source-of-truth doc.

- **Build batch.** Engineering changes in `BACKLOG.md`, small enough to build and test in one session. Each ends with a `Serves` line naming the source-of-truth doc entries it implements.

- **Files: sub-section.** The list of files a build batch will modify, written as a sub-section of the batch in `BACKLOG.md`. Each entry is a GitHub-style task list bullet (`- [ ]` → `- [x]` when done) with `<path>` and a one-sentence change summary. Written by the before-build subagent during *Before build*; ticked file-by-file by the batch-executor during the build. The PreToolUse hook reads this list at edit-time to enforce batch boundaries — files not on the list are blocked. Full rules: `DOC-STRUCTURE.md` → *Files: sub-section*.

- **Batch-sizing principle.** A batch's right size is set by verification burden (count of distinct user-observable behaviours to test after the build), not by lines or files. Three sub-rules: split when a small batch produces a long test list; bundle unrelated items that introduce no new user-facing behaviour and don't interact; never fragment arbitrarily. Applied during *Before build*; full definition in `before-build.md` → *Batch-sizing principle*.

- **Pre-build verification estimate.** The brief list of distinct user-observable behaviours that will need testing after a build batch lands, stated during *Before build*. Used to apply *Batch-sizing principle*: if the list is long relative to scope, the batch gets split. If the estimate proves wrong mid-build, the re-batching carve-out under *Prohibited behaviours → Two exceptions* applies.

- **Suggestion.** During planning: a fix or improvement that fits current scope (an existing `UX.md` or source-of-truth entry already covers it). May come from the user or from Claude. Routed into a build batch.

- **Discovery.** During planning: a bug or improvement outside current scope — no `UX.md` entry covers it. Cannot enter a build batch directly. Promoted to a planning batch asking "should this be added to `UX.md`?"

- **Red flag.** A security, privacy, data integrity, or safety concern. Surface in chat first; if the user defers with no active plan, add to the Red flags section of `BACKLOG.md` in canonical format: `**[RED FLAG]**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Red flags are the only deferred items that don't need a `UX.md` entry behind them.

- **Source-of-truth doc.** A doc describing decided behaviour the build must conform to. `UX.md` is one in every project. Projects may add others (see *Additional source-of-truth doc* below). Read-only to Claude; edited by the user during planning sessions (full rule in `universal-behaviour.md` → *Editing surfaces*).

- **Additional source-of-truth doc.** A project-specific source-of-truth doc beyond `UX.md` — e.g. `SYSTEM-PROMPT.md` for a Claude/MCP integration project, or `COPY.md` for a project whose user-facing text is the deliverable. Same locking rules as `UX.md`. Full rules: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.

- **Adopted folder.** A folder where the no-code method is active — the project's `CLAUDE.md` carries the method footer (`*No-code method — Version N.*`). The footer is written by `/adopt` during its scaffold or migrate paths. The safety net (SessionStart advisory + PreToolUse enforcement) stays silent on adopted folders.

- **Unadopted folder.** A folder where the method is not active — no method footer in `CLAUDE.md`. The safety net fires on unadopted folders **with substantial existing content** (see `plugin/hooks/session_start.py` for the canonical detection thresholds): SessionStart emits an advisory pointing at `/adopt`; PreToolUse blocks `Edit` / `Write` / `MultiEdit` and `Task` → method-subagent calls until the folder becomes adopted or the user writes a `.no-code-method-skip` opt-out marker at root. Genuinely-empty unadopted folders and opted-out folders stay silent.

- **Serves line.** The line at the end of a build batch in `BACKLOG.md` naming the source-of-truth doc entries the batch implements. Format: `Serves UX.md: [entry name(s)].` (and/or `Serves <DOC>: ...` for additional docs).

- **Drift check.** Five checks Claude runs at the start of every planning session: direct-edit detection (git-diff against last build, with a per-file confirmation protocol — V42 addition), `UX.md` ↔ what's built, `MANIFEST.md` ↔ the codebase, `MANIFEST.md` ↔ `UX.md` (loose), and `TEST-LOG.md` ↔ what's been touched since each row was recorded (Rule 5 — retest after change). The first is file-level temporal and walks per-file with the user; the next three are pairwise doc-vs-state comparisons; the fifth is a per-row code-touch check. Full procedure: `planning.md` → *Drift checks — always run* and *Drift check 1 — direct-edit detection*.

- **Fold-in.** Moving proposed source-of-truth content from `BACKLOG.md` into the destination doc (usually `UX.md`). Claude queues content as `[FOLD-IN PENDING]` blocks in the *Fold-ins pending* section of `BACKLOG.md` because source-of-truth docs are read-only; the user does the actual fold-in by hand during a planning session. Origins: planning-batch resolution, `/adopt case 1` (new-project prompts), `/adopt case 3` (migration), or a mid-build edit attempt intercepted by the PreToolUse hook. Once folded in, the block is removed; if a planning batch produced the fold-in, the user also removes that batch in the same session. During planning and `/adopt`, the **preview-then-fold-in convention** applies: the subagent previews the complete section in chat before writing the fold-in block, waits for approval, then prompts the user to fold in now rather than deferring. Full convention: `universal-behaviour.md` → *Editing surfaces*. One exception to the lock: method-version footer stamps (`*No-code method — Version N.*`) are metadata, not content, and the PreToolUse hook allows footer-only edits on locked docs directly.

- **Halt-and-confirm protocol.** Pattern subagents use when they hit a condition the user must decide on: surface in chat, propose the action (or list options), wait for response before proceeding. Used by before-build (validation failure, vague change list, verification burden triggers a split) and batch-executor (prerequisite and re-batching carve-outs).

- **Build log entry.** Persistent per-build narrative in `BUILD-LOG.md`, written by the after-build subagent. Shape: What shipped / Decisions taken and why / Pivots and surprises / Carried forward. Newest-first. The chat recap (see *Build recap* below) is the ephemeral counterpart.

- **Build recap.** Plain-English summary the after-build subagent provides at the end of every build in chat. Not persisted — lives in chat only. The persistent per-build record is the build log entry (see above), written to `BUILD-LOG.md` by the same after-build phase. Used by the user to decide whether to test, push back, or accept.

- **Draft.** A `planning/drafts/<topic>.md` file holding substantive content not yet ready for a specific doc. Complements `BACKLOG.md`'s *Fold-ins pending* (destination-specific, for source-of-truth doc content); drafts hold everything else — comparison tables, structural sketches, protocol rules, option matrices. Written at "good enough to walk away from"; deleted when consumed (folded into a spec, a source-of-truth doc, or a BACKLOG batch); dead-end drafts pruned with a one-line note in the next build log entry. Full rules: `DOC-STRUCTURE.md` → *planning/drafts/ folder*.

- **Frame-correction sweep.** After-build check: when a build substantively changes how a feature works, scan `BACKLOG.md` planning batches and `[FOLD-IN PENDING]` blocks for entries that reference the old behaviour. Candidates flagged in chat for review at the next planning session. `UX.md` drift is not part of the sweep — already caught by drift check 2 (UX.md ↔ what's built) during planning.

- **Test session.** The state `TEST-LOG.md` enters after a build ships. *Opened* during *After every build* by writing one row per user-observable behaviour the recap names, with blank `Status` and `Confirmed Explicitly: No`. *Closed* during the next planning session's first sub-step by per-row read-back: the user names each pending row and gives its outcome (Pass / Fail / Skipped). An unclosed test session blocks the next build batch (test-confirmation gate).

- **Pass.** A `TEST-LOG.md` row `Status` meaning: the user ran the test and the behaviour matched. Pass with `Confirmed Explicitly: Yes` is the only outcome that closes a row positively.

- **Fail.** Row `Status` meaning: the user ran the test and the behaviour did not match. Requires a `User Notes` line describing what actually happened, so the regression has context in future sessions.

- **Skipped.** Row `Status` meaning: the user did not run the test this round, by explicit choice. Requires a reason in `User Notes` (a Skipped without a reason is a Fail or a blank). Skipped satisfies the test-confirmation gate only as an "accounted for" outcome, not a passing one. The row stays in TEST-LOG and may be retested in a future session (typically promoted via Rule 5's drift check).

- **Test-confirmation gate.** Structural enforcement that a new build batch cannot start while any row in `TEST-LOG.md` from the previous batch has `Confirmed Explicitly: No`. Hook side (load-bearing): PreToolUse on `Task` targeting batch-executor reads TEST-LOG and refuses invocation if unconfirmed rows exist from the previous batch's session — falling back to "any unconfirmed row blocks" if the project doesn't keep `BUILD-LOG.md` for session identification. Subagent side (UX): the planning subagent's first sub-step walks the user through per-row read-back. Defined by the *Do not invoke the batch-executor* rule in `universal-behaviour.md` → *Prohibited behaviours*, made trustworthy by the *Never infer completion* rule in *Required behaviours*, and made retestable over time by drift check 5 (retest after change).

---
*No-code method — Version 41.*
