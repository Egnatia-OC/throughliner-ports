# Build log

Running record of decisions, changes, and reasoning. Newest first. Written for a friend skimming — half a page per session, less when possible.

For format details, see `BUILD-METHOD.md` → *BUILD-LOG entry shape*.

---

## v59 — 2026-05-23 — Subagent rule-loading convergence

**What shipped.** Scope 0057. Converged all subagents on the read-spec-on-entry pattern. `batch-executor.md` was the sole outlier — it had spec-derived rules inlined in its body (V25 Decision 4) rather than reading `DOC-STRUCTURE.md` at runtime like planning, before-build, and after-build. (1) Added step 7 to batch-executor's "First action — load the project's current state" list: reads `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *BACKLOG structure → Files: sub-section* and *BACKLOG structure → Red flags* at runtime. (2) Added framing note ("The body of this file holds operational notes — the docs themselves are the source of truth") matching the other three subagents. (3) Added closing note explaining operational procedure is inlined but spec formats come from runtime reads. (4) Removed the trailing "Spec references" section — its DOC-STRUCTURE pointers are now runtime reads; its universal-behaviour pointers are hook-enforced and don't need agent-side lookup. (5) Updated inline DOC-STRUCTURE reference in the Red flags bullet to use `${CLAUDE_PLUGIN_ROOT}` path prefix. (6) OPEN-QUESTIONS "Subagent rule-loading pattern divergence" entry removed (shipped). (7) INVENTORY.md batch-executor entry updated to reflect the convergence. All 147 tests pass. Footer bumps V53 → V54; plugin 0.53.0 → 0.54.0; PLUGIN_METHOD_VERSION 53 → 54.

**Decisions taken and why.** Option A (read-spec-on-entry) chosen over Option B (inline) and Option C (documented divergence). Evidence: `DOC-STRUCTURE.md` and `VOCABULARY.md` changed in every version from V50 through V53 — the specs are still churning, so inlined copies would silently drift. The prompt-time overhead of reading two spec docs (402 lines total) is marginal given the subagent already reads CLAUDE.md, UX.md, BACKLOG, MANIFEST.md, and TEST-LOG.md every invocation. Setup subagent excluded from the convergence — it doesn't reference DOC-STRUCTURE or VOCABULARY at all (works with templates and the scaffold script).

**Pivots and surprises.** None. Straightforward refactor — the scope file's open questions both resolved cleanly from the evidence (specs churning → Option A; overhead small → no concern).

**Carried forward.** Deferred smoke tests: add V54 subagent rule-loading convergence to the list (verify batch-executor reads DOC-STRUCTURE.md at runtime in a desktop-app burner session). All prior deferred smoke tests unchanged.

---

## v58 — 2026-05-23 — TEST-LOG row pruning

**What shipped.** Scope 0056. Automatic TEST-LOG row pruning — the planning subagent now deletes rows whose Component no longer exists in MANIFEST.md, plus any rows with legacy Status `Superseded`, before drift checks run. (1) New step 2c in the planning procedure (between aging detection and drift checks) collects MANIFEST entry names, walks TEST-LOG rows, deletes orphaned-component rows and Superseded rows, exempts cross-component descriptions (rows not matching any single MANIFEST entry are kept). Surfaces what was pruned in the planning recap. (2) DOC-STRUCTURE.md pruning rule updated: "component removed → rows deleted by the planning subagent" replaces "component removed → row marked Superseded." (3) VOCABULARY.md new entry: *Row pruning (TEST-LOG)*. (4) Crash course updated with pruning sentence in TEST-LOG description. (5) INVENTORY.md planning subagent entry updated with pruning responsibility. (6) BUILD-METHOD.md stale reference fixed: planning-artefacts table had "rows never removed / marked Superseded" — corrected to reflect V53 behaviour; also fixed "newest at bottom" → "newest at top" ordering description. No Python hook changes — all edits are markdown (subagent instructions and docs). All 147 tests pass. Footer bumps V52 → V53; plugin 0.52.0 → 0.53.0; PLUGIN_METHOD_VERSION 52 → 53.

**Decisions taken and why.** Component-based pruning chosen over time-based or manual archive — cleanest signal (component gone = test row meaningless). Pruned rows are deleted outright (no archive file) because git history preserves them and an archive file would grow without bound, trading one unbounded file for another. Pruning placed at planning step 2c (before drift checks, not at after-build) so after-build stays focused on its existing job and the planning subagent — which already reads MANIFEST for drift checks — handles cleanup naturally. Cross-component rows exempted from pruning since they span multiple components and can't be matched to a single MANIFEST entry.

**Pivots and surprises.** Scope file leaned toward an archive file; pushed back and user accepted deletion (git-as-archive). No other surprises — the build was straightforward markdown edits. Doc-code parity audit at session close caught a stale reference in BUILD-METHOD.md's planning-artefacts table (still said "never removed" / "marked Superseded").

**Carried forward.** Deferred smoke tests unchanged from v57. OPEN-QUESTIONS "TEST-LOG row pruning" entry removed (shipped).

---

## v57 — 2026-05-22 — New hook events (compaction guard + opener routing)

**What shipped.** Scope 0055. Two new Claude Code hook events the plugin hadn't used before: PreCompact (compaction guard) and UserPromptSubmit (opener classification). (1) PreCompact hook at `plugin/hooks/pre_compact.py` — blocks context compaction when a build batch is in progress (unticked files in BACKLOG), surfaces a user-facing reason (long sessions cost tokens and adherence degrades) plus a paste-ready prompt the user can give Claude to prepare a handoff. Allows silently when no active build. (2) UserPromptSubmit hook at `plugin/hooks/user_prompt_submit.py` — keyword-based classification of the user's first prompt each session (setup, test notes, resume), injected as `additionalContext` routing hint. Conservative: test notes need 2+ keyword hits; ambiguous prompts produce no classification. First-prompt detection via transcript marker search. (3) Session handoff protocol added to `universal-behaviour.md` — 4-step process (tick files, annotate in-progress, record decisions in Handoff notes: block, tell user). (4) Hook-assisted classification paragraph added to routing table in `universal-behaviour.md`. Both hooks registered in `hooks.json`. Doc-code parity: DOC-STRUCTURE (Handoff notes block in batch structure), VOCABULARY (session handoff, handoff notes, opener classification), Crash course (both hooks in "What's inside the plugin"), INVENTORY (both hook entries). OPEN-QUESTIONS "six prose directives" entry fully resolved (all 6 items shipped). Footer bumps V51 → V52; plugin 0.51.0 → 0.52.0; PLUGIN_METHOD_VERSION 51 → 52. Tests: 17 new tests (6 PreCompact + 11 UserPromptSubmit); full suite 147 passed.

**Decisions taken and why.** PreCompact cannot inject `additionalContext` (platform limitation — only `decision` + `reason`), so the design reframed from "preserve context through compaction" to "block compaction and recommend handoff." The user's real motivation is token cost and adherence, not state loss — the block reason reflects that. Handoff notes live in the batch itself (no separate file) because the batch already carries tick state and the next session reads it via SessionStart. UserPromptSubmit uses a self-referential transcript marker for first-prompt detection — same pattern as PreToolUse's V39 block-once, naturally resets on `/clear`.

**Pivots and surprises.** The scope file assumed PreCompact could inject `additionalContext` — research confirmed it cannot. Complete design reframe from context injection to compaction blocking + handoff protocol.

**Carried forward.** Deferred smoke tests unchanged from v56.

---

## v56 — 2026-05-22 — Validation + warnings bundle

**What shipped.** Scope 0054. Four items from the "six prose directives" OPEN-QUESTIONS entry (items 2, 3, 4) plus the `[FOLD-IN PENDING]` → `[PROPOSED EDIT PENDING]` rename. (1) `Serves <DOC>:` validation extended to additional source-of-truth docs — PreToolUse now reads all docs declared in the path block (not just UX.md), matches `Serves <DOC>:` entries against `##` headings (excluding structural sections like Proposed edits pending), and denies with a doc-specific message on mismatch. (2) Red flags non-empty warning at SessionStart — when BACKLOG's Red flags section has entries, they're surfaced prominently in the session-start advisory with a per-flag list and an instruction to acknowledge each one. (3) Deferred build-material aging in planning subagent — folder-mode detection of BACKLOG batches whose allocation number predates completed batches, surfaced at planning step 2b. (4) `[FOLD-IN PENDING]` renamed to `[PROPOSED EDIT PENDING]` and `Fold-ins pending` renamed to `Proposed edits pending` across all live plugin files — subagent bodies, hook scripts, templates, DOC-STRUCTURE, VOCABULARY, Crash course. Footer bumps V50 → V51; plugin 0.50.0 → 0.51.0; PLUGIN_METHOD_VERSION 50 → 51. Tests extended: 8 new tests for Serves-DOC validation + red-flag detection in session_start. Scope file 0060 (Taskflow E2E prep and testing) created.

**Decisions taken and why.** Additional-doc entries matched against `##` headings (not `###`) because additional docs use `##` for their content sections, unlike UX.md which nests entries under `### Functionalities`. Structural sections (`Proposed edits pending`) excluded from the match set by a frozen set in the hook — extensible if more structural section names emerge. The `[FOLD-IN PENDING]` → `[PROPOSED EDIT PENDING]` rename was bundled here because the four items already touched the same files.

**Pivots and surprises.** None.

**Carried forward.** Deferred smoke tests unchanged from v55. OPEN-QUESTIONS "six prose directives" entry: items 2, 3, 4 resolved; items 5, 6 remain (→ 0055).

---

## v55 — 2026-05-22 — Automated test suite for dev project

**What shipped.** Scope 0053 (dev-internal, no method version bump). Pytest-based test suite at `tests/` covering all hook scripts and shared helper modules. 124 tests, 2.7 seconds, zero failures.

Files created: `tests/conftest.py` (shared helpers: `run_hook()`, `run_script()`, fixture-path resolver, pytest fixtures), `tests/test_project_state.py` (unit tests for `project_state.py` — footer detection, path-block parsing, tier classification, adopt-case detection, TEST-LOG parsing, build-log session identification, BACKLOG helpers), `tests/test_parse_backlog.py` (unit tests for `parse_backlog.py` — file bullet parsing, batch body parsing, single-file and folder mode, CLI invocation), `tests/test_session_start.py` (tier 1/2/3 classification, V29 unadopted advisory, malformed input), `tests/test_pre_tool_use.py` (V29 adoption gate, locked-doc enforcement incl. V38/V45 carve-outs, serves-line check, batch boundary, V39 read-before-edit, V27 test-confirmation gate, V43 mode-aware messaging), `tests/test_pre_tool_use_git_guard.py` (V34 git safety guard — reset hard, push force, force-with-lease allowed), `tests/test_post_tool_use.py` (BACKLOG format validation, silent cases), `tests/test_stop.py` (batch-executor redirect, after-build detection, silent cases, stop_hook_active loop prevention).

Fixture directories at `tests/fixtures/`: `empty/` (tier 1), `tier2_no_claude/` (spine docs without CLAUDE.md), `tier2_bad_pathblock/` (CLAUDE.md without parseable path block), `adopted_folder/` (tier 3 folder-mode BACKLOG with build-log/ folder), `adopted_single_file/` (tier 3 legacy single-file BACKLOG), `unadopted_foreign_claude/` (foreign CLAUDE.md + package.json — triggers V29 unadopted-with-work).

Other files touched: `BUILD-METHOD.md` (added *Automated test suite (V53 — pytest)* section, updated "No automated CI" bullet), `planning/OPEN-QUESTIONS.md` (marked "Automated testing / CI" entry resolved), `planning/PLAN.md` (marked V53 shipped v55).

**Decisions taken and why.** Subprocess-based hook tests (not import) — tests the same stdin/stdout protocol Claude Code uses, catches JSON encoding issues that import-based tests wouldn't. Committed fixtures (not tmpdir) — deterministic and inspectable. Manual-only CI — pytest runs locally, no GitHub Actions.

**Pivots and surprises.** V38/V45 carve-out tests (footer-only and fold-in section edits on UX.md) initially expected clean allow, but the batch-boundary check runs downstream and denies because UX.md isn't on the active batch's Files: list. That's correct production behaviour — the carve-outs pass the locked-doc check, confirmed by asserting the deny reason is "not on the current build batch" (not "locked source-of-truth").

**Carried forward.** Deferred smoke tests unchanged from v54.

---

## v54 — 2026-05-22 — BUILD-LOG restructured to build-log/ folder

**What shipped.** V50 scope (0052). Replaced monolithic `BUILD-LOG.md` with a `build-log/` folder containing one file per build plus an `INDEX.md` carrying the newest-first reference list. Same folder-mode pattern as BACKLOG/ (V48). `/setup` scaffolds `build-log/` with `INDEX-TEMPLATE.md`. Path block key stays `"BUILD-LOG.md"` but points to `build-log/INDEX.md`. Session identification updated across all hooks and subagents for folder mode with legacy single-file fallback. Old `BUILD-LOG-TEMPLATE.md` deleted.

Files touched: `plugin/templates/build-log/INDEX-TEMPLATE.md` (created), `plugin/templates/BUILD-LOG-TEMPLATE.md` (deleted), `plugin/templates/CLAUDE-TEMPLATE.md` (path block), `plugin/skills/setup/scripts/scaffold.py` (folder scaffold), `plugin/scripts/project_state.py` (folder-mode session identification), `plugin/hooks/session_start.py` (folder-mode session identification + SPINE_FOLDER_PATHS + version bump), `plugin/hooks/pre_tool_use.py` (SCAFFOLD_DIRS + user-facing messages), `plugin/hooks/stop.py` (docstring), `plugin/docs/DOC-STRUCTURE.md` (full section rewrite), `plugin/docs/VOCABULARY.md` (definitions), `plugin/hooks/universal-behaviour.md` (editing surfaces), all 5 subagent bodies (session identification, load lists, scaffold references), `Crash course.md` (references throughout), `planning/INVENTORY.md` (project-side docs, bundled artefacts, component descriptions), `planning/OPEN-QUESTIONS.md` (removed resolved entry). Footer bumps V49 → V50 across all 16 plugin-side files + Crash course + INVENTORY. Plugin 0.49.0 → 0.50.0; PLUGIN_METHOD_VERSION 49 → 50.

**Decisions taken and why.**

- **3-digit sequential numbers for build-log entries.** Scope file framed `BUILD-001.md` originally. Matches the pattern from allocate_number.py. 3 digits vs BACKLOG's 4 digits because consumer projects will have far fewer builds than BACKLOG batches.
- **No case 4 migration logic.** User pointed out no consumer project has ever used sovereign implementer for real — there are no existing BUILD-LOG.md files to migrate. Eliminated a chunk of planned work.
- **Bullet list for INDEX.md, not a markdown table.** Matches BACKLOG/INDEX.md's reference-list pattern. Easier to parse, easier to prepend.
- **Path block key stays `"BUILD-LOG.md"`.** Changing the key would break existing path-block parsing across all hooks. The value changes to `build-log/INDEX.md`.
- **One-line research cross-reference convention.** Build entries link to `research/<topic>.md` by path rather than embedding content — consistent with research/ folder spec from V49.

**Pivots and surprises.** None.

**Carried forward.** Deferred smoke tests accumulating: V43 mode-aware messaging, V45 fold-in carve-out, V46 automated test pass, V48 BACKLOG folder-split, V49 batch structure, V49 research folder, V50 build-log folder — all testable in a single desktop-app burner session via local marketplace.

---

## v53 — 2026-05-22 — Research folder convention + Sonnet-search reword

**What shipped.** V51 scope (0051). Two changes: (1) `/setup` now scaffolds a `research/` folder at project root, and all "prompt the user to do a Sonnet search" language replaced with "research it directly and save findings to `research/<topic>.md`" — shifting research responsibility from the user to the agent. (2) New `research/` folder spec in DOC-STRUCTURE.md (Location, Purpose, Naming convention, Lifecycle, Referencing from build batches, Access) and "Research file" definition in VOCABULARY.md.

Files touched: `plugin/skills/setup/scripts/scaffold.py` (mkdir `research/`, updated emit payload), `plugin/agents/setup.md` (research/ mentions in cases 1–3 recaps), `plugin/hooks/universal-behaviour.md` (rewrote "Verify external facts" required behaviour — agent researches directly, writes to `research/<topic>.md`, falls back to `[UNVERIFIED]` tag), `plugin/docs/DOC-STRUCTURE.md` (new `## research/ folder` section), `plugin/docs/VOCABULARY.md` (new "Research file" entry), `Crash course.md` (scaffold description + research/ paragraph + Sonnet-search caveat rewrite), `planning/INVENTORY.md` (updated `/setup` description). Plus footer bumps on all 18 plugin-side files. Method version V48 → V49; plugin 0.48.0 → 0.49.0; PLUGIN_METHOD_VERSION 48 → 49.

**Decisions taken and why.**

- **Free-form naming for research files.** `<topic>.md` with kebab-case, not numbered or date-stamped. Research files are reference material, not a sequence — alphabetical folder listing is the natural browse mode. Consistent with the dev project's existing research folder.
- **Brief mention when writing research, not a multi-line recap.** One sentence in chat ("I'm saving these findings to `research/<topic>.md` for future reference") keeps the user informed without cluttering the conversation. The file itself is the artefact.
- **`[UNVERIFIED: <what>]` fallback.** When research tools aren't available, the agent marks the claim inline. This makes uncertainty visible in the build artefacts rather than silently passing unverified assumptions.

**Pivots and surprises.**

- Grep sweep confirmed only two files contained Sonnet-search language (universal-behaviour.md, Crash course.md). No subagent bodies needed rewriting — they already referenced research files correctly in their Inputs-line context.
- Session spanned two context windows due to the footer-bump volume.

**Carried forward.**

- Smoke tests deferred: V43 mode-aware messaging + V45 fold-in section carve-out + V46 automated test pass + V49 batch structure + V51 research folder — all testable against Taskflow in a desktop-app burner session with the plugin installed via local marketplace.
- OPEN-QUESTIONS: V51 entry removed. Remaining entries unchanged.

---

## v52 — 2026-05-22 — ADR-style numbering + per-batch BACKLOG file-split

**What shipped.** V50 scope (0050). Two structural overhauls in one session: dev-side scope files renamed from `V*.md` to `NNNN-kebab-title.md` format (0051–0059 created; V50.md retained as current session's file, deleted at close); consumer-side BACKLOG split from a single `BACKLOG.md` into a `BACKLOG/` folder with `INDEX.md` (carrying Red flags, Planning batches, Build batch reference list, Open questions) plus per-batch files (`NNNN-batch-name.md`). Shared `allocate_number.py` for 4-digit number allocation across both dev and consumer sides. All four hook scripts updated for folder-aware BACKLOG detection (`is_backlog_file()`, `resolve_backlog_dir()` helpers in `project_state.py`). Parser auto-detects folder vs single-file mode. `/setup` case 4 migrates old single-file BACKLOG.md to folder format. All five subagent bodies updated for two-format BACKLOG handling. Scaffold script extended to create `BACKLOG/` directory with `INDEX-TEMPLATE.md`. `Crash course.md` updated to describe folder structure. `BUILD-METHOD.md` updated with triple-distinction (session tag / scope-file number / method version) and allocation rule. PLAN.md and OPEN-QUESTIONS.md references updated from V-number format to NNNN format. INVENTORY.md updated with new components. All plugin-side footers bumped. Method version V47 → V48; plugin 0.47.0 → 0.48.0; PLUGIN_METHOD_VERSION 47 → 48.

**Decisions taken and why.**

- **All at once rather than split dev/consumer.** User chose to combine dev-side rename + consumer-side file-split into one session despite recommendation to split. The two halves share the allocation concept and `allocate_number.py`; shipping them together avoids a half-baked intermediate state where dev uses NNNN format but consumer still uses inline batches.
- **4-digit zero-padded numbers (0001, not 001).** Future-proof; conventional ADR practice. No realistic project hits 10,000 batches, but the padding is cheap insurance.
- **INDEX.md, not README.md.** Explicit purpose; no collision with GitHub's README convention (which would render as the folder's landing page on GitHub, conflating navigation with BACKLOG content).
- **Numbers frozen at allocation; splits create new files.** Per ADR convention — numbers are stable identifiers, not position markers. Reordering means moving lines in INDEX.md, not renaming files. Splits create new files with new numbers; the old file stays.
- **Legacy single-file format kept working.** Parser falls back to single-file extraction when it detects `### Batch:` headings (not `INDEX.md`). Projects that haven't run `/setup` case 4 continue working.

**Pivots and surprises.**

- Session spanned two context windows due to the volume of files touched (4 hooks, 5 subagents, scaffold script, parser, project_state, 2 canonical docs, 8 templates, Crash course, BUILD-METHOD, PLAN, OPEN-QUESTIONS, INVENTORY, CLAUDE.md, plugin.json, session_start.py).
- `stop.py` docstring edit failed on string match — skipped as non-critical; the code changes are correct.

**Carried forward.**

- Smoke tests deferred: all previous deferrals plus V48 BACKLOG folder-split — testable against Taskflow in a desktop-app burner session with the plugin installed via local marketplace.
- OPEN-QUESTIONS: "Red-flag / threat-class marker" remaining half (UX.md marker) still unscheduled.

---

## v51 — 2026-05-22 — Consumer-batch structure overhaul

**What shipped.** V49 scope. Adds five scope-context sections to consumer-project BACKLOG build batches — Goal, Outputs, Success criteria, Decisions to make this batch, Dependencies — plus a conditional Red flags sub-section and the `Changes:` delimiter that separates scope-context from build-operations content. The batch now has two regions: scope context (everything between the `### Batch:` heading and `Changes:`) and build operations (`Changes:` through `Serves`). Template placeholder cleanup (UX friction item 6): BACKLOG-TEMPLATE's example batches replaced with HTML-comment format specs. `/setup` case 4 extended to detect old-format batches and insert stub scope-context sections + `Changes:` delimiter.

Files touched: `plugin/scripts/parse_backlog.py` (backwards-compatible `Changes:` delimiter support — new `CHANGES_LINE_PATTERN`, updated `parse_batch_body()` to bound change-list extraction), `plugin/docs/DOC-STRUCTURE.md` (two-region batch structure, scope-context sections, Red flags sub-section, `Changes:` delimiter — full rewrite of Build batches sub-section), `plugin/docs/VOCABULARY.md` (5 new entries: Scope-context sections, Changes: delimiter, Decisions to make this batch, Dependencies (batch section), Red flags sub-section (batch-level)), `plugin/templates/BACKLOG-TEMPLATE.md` (example batches replaced with HTML-comment format spec), `plugin/agents/planning.md` (new "Scaffolding new build batches" section for scope-context + red-flag detection), `plugin/agents/before-build.md` (Changes: references in work loop steps 1–3, scope-context inheritance in halt C), `plugin/agents/after-build.md` (Changes: delimiter reference for label reading), `plugin/agents/batch-executor.md` (scope-context inheritance in re-batching carve-out), `plugin/agents/setup.md` (case 4 old-format batch migration), `plugin/hooks/post_tool_use.py` (warning message updated for Changes: anchor), `Crash course.md` (BACKLOG bullet updated, two new sections — "The method absorbs mid-stream ideation" + "Anatomy of a batch", walkthrough step 5 updated). Plus footer bumps on all 16 plugin-side files. Method version V46 → V47; plugin 0.46.0 → 0.47.0; PLUGIN_METHOD_VERSION 46 → 47.

**Decisions taken and why.**

- **`Changes:` delimiter rather than scope-context fence.** The parser extracts change-list bullets by matching `- ` lines before `Files:`. Scope-context sections (especially Dependencies) can contain `- ` bullets that would pollute the change list. A `Changes:` delimiter bounding the extraction region was cheaper and more robust than trying to detect and exclude scope-section bullets. Backwards compatible: parser falls back to the legacy "everything before `Files:`" behaviour when no `Changes:` line is present.
- **Red flags as auto-detected conditional section, not always-present.** Planning subagent detects security-shaped scope (auth, secrets, PII, deletion, payment, third-party API keys) and writes the Red flags sub-section only when triggered. Non-security batches don't carry an empty Red flags section.
- **HTML-comment format specs in BACKLOG-TEMPLATE (UX friction item 6).** The old template had two rendered example batches with full placeholder content — a wall of red/green diff when `/setup` wrote real content over them. HTML comments (matching the pattern TEST-LOG-TEMPLATE and MANIFEST-TEMPLATE already use) are invisible in rendered markdown and don't create diff noise.
- **Stub scope-context for `/setup` case 4 migration.** Old-format batches get `[To be filled in during the next planning session.]` stubs for Goal, Outputs, and Success criteria, plus the `Changes:` delimiter. Decisions, Dependencies, and Red flags omitted (they're conditional). Fills enough structure for the parser to work correctly without inventing scope that planning should decide.

**Pivots and surprises.**

- PowerShell's string handling mangled em dash (U+2014) and backtick characters when attempting inline Python parser tests. Solved by writing a proper `test_parser.py` with test content in Python strings (cleaned up post-test).
- This session spans two context windows. The previous chat completed all substantive edits; this continuation ran the parser test, cleaned up temp files, and handled the close-out steps.

**Carried forward.**

- OPEN-QUESTIONS: "Post-adopt UX friction" item 6 (template placeholder cleanup) resolved (6 of 7 now done). "Red-flag / threat-class marker" entry should note partial resolution (batch-level Red flags shipped; threat-class marker for UX.md entries is the remaining half).
- Smoke tests deferred: V43 mode-aware messaging + V45 fold-in section carve-out + V46 automated test pass + V49 batch structure — all testable against Taskflow with the plugin installed via local marketplace.

---

## v50 — 2026-05-22 — Automated vs. manual test split + non-UI test types

**What shipped.** V48 scope — the single biggest method-level change to the build cycle since V27. Introduces four named test types (Look and click, Run and read, Trigger and observe, Generate and inspect), a per-row Claude/User verifier split, 10-column TEST-LOG format (adding Type and Verifier columns, renaming User Notes → Notes), a Tests: sub-section in BACKLOG.md build batches, Claude-automated test execution during after-build, a two-section build recap ("Claude has verified" / "Please manually check"), and a commit/tag prompt in after-build's closing sequence (UX friction item 5). Backwards-compatible: the shared regex in project_state.py handles both 10-column and legacy 8-column rows; `/setup` case 4 backfills defaults for 8-column projects.

Files touched: `plugin/docs/VOCABULARY.md` (test type + verifier definitions, test session updated, Fail/Skipped "User Notes" → "Notes"), `plugin/docs/DOC-STRUCTURE.md` (10-column table spec, Tests: sub-section spec, backwards-compat paragraph, pruning-rule "User Notes" → "Notes"), `plugin/templates/TEST-LOG-TEMPLATE.md` (complete rewrite to 10-column), `plugin/templates/BACKLOG-TEMPLATE.md` (Tests: sub-section added to example batches), `plugin/agents/after-build.md` (step 3 rewritten for 10-column rows + automated test pass, step 4 three-part recap, step 8 commit/tag prompt), `plugin/agents/before-build.md` (step 4 Tests: population, step 5 updated reference), `plugin/agents/planning.md` (Claude-verified skip note, "User Notes" → "Notes"), `plugin/agents/setup.md` (case 4 TEST-LOG 8→10-column migration), `plugin/scripts/project_state.py` (10-column regex with optional Type/Verifier groups, parse_test_log_rows returns 10-field dicts), `plugin/hooks/session_start.py` (removed duplicate 8-column regex + parse_test_log_rows, now imports shared versions from project_state.py), `plugin/hooks/stop.py` (docstring + format_after_build_reason updated for 10-column), `Crash course.md` (10-column description, new "Four test types and the Claude/user split" section, subagent + test-session-read-back updates), `planning/INVENTORY.md` (after-build entry updated), `plugin/hooks/universal-behaviour.md` ("Why the rules" test-session entry updated for Claude-verified rows). Plus footer bumps on all 16 plugin-side files. Method version V45 → V46; plugin 0.45.0 → 0.46.0; PLUGIN_METHOD_VERSION 45 → 46.

**Decisions taken and why.**

- **Tests run after the build (after-build), not during (batch-executor).** Batch-executor's job is to implement; testing during implementation creates mid-build interruptions that can derail the session. After-build already writes TEST-LOG rows and produces the recap — adding the automated test pass there keeps the boundary clean.
- **Verifier is per-row, not per-type.** A Look-and-click test checking "does the button exist?" is structural (Claude can verify); the same type checking "does the layout feel right?" is judgement (user). Tying verifier to type would force false assignments.
- **Optional non-capturing group in the regex for backwards compatibility.** The `(?:...|...)?` pattern lets the same regex match both 10-column (V48+) and 8-column (pre-V48) rows without separate patterns or a migration gate.
- **Extracted session_start.py's local 8-column regex and parse_test_log_rows.** Frame-correction sweep caught a real bug: session_start.py's 8-column regex would misparse 10-column rows (Type and Verifier columns shift all subsequent group indices), making the SessionStart tripwire flag every 10-column row as unconfirmed. Now imports the shared version from project_state.py.

**Pivots and surprises.**

- The session_start.py misparse bug was not in V48's scope — surfaced during the frame-correction sweep. A 10-column TEST-LOG row matched by the old 8-column regex would assign the Verifier column's value ("Claude" or "User") to the `confirmed_explicitly` field, which would never start with "Yes", falsely flagging every row as unconfirmed.

**Carried forward.**

- OPEN-QUESTIONS: "Automated vs. manual test split" entry removed (shipped). "Post-adopt UX friction" item 5 marked resolved (5 of 7 now done). "Graduate sovereign implementer" prerequisite 2 marked shipped (3 of 4 prerequisites done).

---

## v49 — 2026-05-22 — Non-GUI vocabulary generalisation + planning/plan-mode disambiguation

**What shipped.** V47 scope (both questions bundled). (1) Replaced "user-observable behaviours" with "observable behaviours" across all plugin-side operational docs — VOCABULARY.md (3 definitions), before-build.md (4 instances), after-build.md (1), planning.md (2), stop.py (1 string literal), Crash course.md (1), INVENTORY.md (1). Added a "Non-GUI projects" guidance paragraph to DOC-STRUCTURE.md under UX.md structure, explaining how non-GUI projects (CLI tools, backend services, MCP servers, plugins, scripts) adapt the "user" and "experience" concepts. (2) Added a "Planning session (not plan mode)" vocabulary entry to VOCABULARY.md clarifying the distinction. Added a "Which mode for which phase" subsection to Crash course.md's "Two layers of permission" section — a per-phase permission-mode recommendation table covering planning, before-build, build, after-build, pre-method ideation, and batch review. Researched programmatic permission-mode switching as an alternative — confirmed not possible from plugin hooks.

Files touched: `plugin/docs/VOCABULARY.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/agents/before-build.md`, `plugin/agents/after-build.md`, `plugin/agents/planning.md`, `plugin/hooks/stop.py`, `Crash course.md`, `planning/INVENTORY.md`. Plus footer bumps on all plugin-side files. Method version V44 → V45; plugin 0.44.0 → 0.45.0.

**Decisions taken and why.**

- **"Observable behaviours" rather than "observable outcomes" or "testable behaviours."** Keeps "behaviours" (consistent with existing method language) while dropping only the "user-" prefix that assumed GUI. "Outcomes" would have shifted the meaning toward results rather than actions; "testable" would have narrowed to verification-time phrasing only.
- **Vocabulary note rather than full rename of the planning phase.** The rename (to "design session," "discussion session," etc.) would have touched every doc, subagent body, INVENTORY entry, and the subagent type name. A vocabulary note plus per-phase mode table addresses the confusion directly at lower cost. The rename was explored in conversation — Alex considered "discussion" then stepped back; the per-phase table emerged as a more practical resolution.
- **Guidance paragraph in DOC-STRUCTURE.md rather than a separate non-GUI template.** A new template (BEHAVIOUR.md, CONTRACT.md) would fragment the method. The guidance paragraph preserves UX.md as the universal spine doc while explaining how to adapt it.

**Pivots and surprises.**

- Alex proposed collapsing the method's planning phase with Claude Code's plan mode by having the plugin programmatically enable plan mode during planning. Research confirmed plugins cannot switch permission modes mid-session — only the user can (Shift+Tab, CLI flag, or settings.json). The per-phase mode table was the outcome.
- Frozen repo-root docs (NO-CODE-METHOD.md, VOCABULARY.md, DOC-STRUCTURE.md at repo root) retain the old "user-observable" phrasing — correct per the V39 freeze, not drift.

**Carried forward.**

- Two OPEN-QUESTIONS entries resolved: "UX.md adaptation for non-GUI projects" and "'Planning' vocabulary collision with Claude Code's plan mode."

---

## v48 — 2026-05-22 — BACKLOG.md PostToolUse parse validation hook

**What shipped.** V46 scope. New PostToolUse hook (`plugin/hooks/post_tool_use.py`) — the plugin's first use of the PostToolUse hook event. Fires after every Edit/Write/MultiEdit via hooks.json matcher; filters for BACKLOG.md edits by resolving the target path through CLAUDE.md's path block. When the edit targeted BACKLOG.md, imports `find_top_unticked_batch` directly from `parse_backlog.py` (no subprocess overhead) and validates the file's structural format. Detection heuristic: if the file contains unticked file bullets with non-placeholder paths but the parser returns `{}`, the format is broken — surfaces an immediate `additionalContext` warning naming common causes. Template-placeholder paths excluded via `TEMPLATE_PLACEHOLDER_PATTERN` to avoid false positives on freshly-scaffolded projects. Full-file search rather than section-bounded, so corrupted `## Build batches` headings are themselves caught.

Files touched: `plugin/hooks/post_tool_use.py` (new), `plugin/hooks/hooks.json`, `plugin/scripts/parse_backlog.py` (docstring), `planning/INVENTORY.md`, `Crash course.md`. Plus footer bumps on all plugin-side files. Method version V43 → V44; plugin 0.43.0 → 0.44.0.

**Decisions taken and why.**

- **Direct import of `find_top_unticked_batch` rather than subprocess.** The PostToolUse hook fires on every writing-tool call (pre-filtered by matcher to Edit/Write/MultiEdit). Subprocess overhead on every edit would be noticeable. Direct import into the same Python process is faster and the parser is already designed as a pure function on text input.
- **Full-file search for unticked bullets rather than section-bounded.** First implementation used `## Build batches` section boundaries (matching the parser's own detection), but testing revealed a blind spot: when a corrupted heading (`## Batch:` instead of `### Batch:`) truncates the section, the pre-check can't find the bullets any more than the parser can. Full-file search catches this.
- **Non-blocking warning via `additionalContext`, not a deny.** PostToolUse hooks can't deny (the tool already ran). The warning tells Claude what went wrong and what to fix. Claude reads it as part of the next context injection.

**Pivots and surprises.**

- V46 scope file named `plugin/hooks/stop_hook.py` as an input reference, but the actual file is `plugin/hooks/stop.py`. Minor discrepancy in the scope file, not a functional issue.

**Carried forward.**

- OPEN-QUESTIONS "Six prose directives" item 1 resolved. Items 2–6 remain on their scheduled scope files (V54, V55).
- Smoke test via `--plugin-dir`: edit BACKLOG.md with a malformed batch header in a test project and verify the warning fires in a live Claude Code session. Deferred to a future E2E testing session.

---

## v47 — 2026-05-22 — Distributed fold-ins + BACKLOG open-questions + batch Inputs line

**What shipped.** V45 scope. Three structural changes to the method's document architecture: (1) **Distributed fold-ins** — `[FOLD-IN PENDING]` blocks moved from a centralized section in BACKLOG.md to a `## Fold-ins pending` section at the bottom of each destination source-of-truth doc (UX.md, MANIFEST.md, additional SOT docs). PreToolUse hook gained `is_fold_in_section_edit()` — a new carve-out allowing edits within the fold-in section while keeping the rest of locked docs protected (same pattern as V38's footer-stamp carve-out). Templates (UX, MANIFEST, ADDITIONAL-DOC) each gained the new section. (2) **Open questions section in BACKLOG.md** — new fourth section (Red flags → Planning batches → Build batches → Open questions) for non-blocking parking-lot items. Planning subagent scans all entries with one-line summaries every session. Distinct from planning batches (blocking) — coexist, don't merge. (3) **Batch Inputs line** — optional `Inputs:` bullet list in build batches listing non-standard resources needed before starting work. Before-build subagent populates during batch lock-in; batch-executor reads before starting work. Standard docs omitted.

Files touched: `plugin/templates/BACKLOG-TEMPLATE.md`, `plugin/templates/UX-TEMPLATE.md`, `plugin/templates/MANIFEST-TEMPLATE.md`, `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/pre_tool_use.py`, `plugin/hooks/universal-behaviour.md`, `plugin/agents/planning.md`, `plugin/agents/before-build.md`, `plugin/agents/batch-executor.md`, `plugin/agents/after-build.md`, `plugin/agents/setup.md`, `Crash course.md`. Plus footer bumps on all plugin-side files. Method version V42 → V43; plugin 0.42.0 → 0.43.0.

**Decisions taken and why.**

- **Fold-in sections go at the end of locked docs, before the footer.** The PreToolUse hook detects edits within the section by checking whether `old_string`'s position falls at or after the `## Fold-ins pending` heading. End-of-doc placement makes position detection simple and reliable.
- **Open questions coexist with planning batches rather than replacing them.** Planning batches are blocking (they name what they block via a `Blocks:` line); open questions are non-blocking parking. Different purposes, different lifecycles. Open questions mature into planning batches when they start blocking something specific.
- **No BACKLOG-specific fold-ins section.** Originally considered, then dropped. BACKLOG.md is writable by Claude — no fold-in mechanism needed for it. Keeps BACKLOG at four sections.
- **Planning subagent handles migration from old centralized fold-ins.** No `/setup` run needed. During normal planning-session work, if the planning subagent finds fold-in blocks in the old BACKLOG.md location, it redistributes them to destination docs.
- **Inputs line between change list and Files sub-section.** Natural reading order: what the batch does (change list) → what it needs to read first (Inputs) → what files it will edit (Files).

**Pivots and surprises.**

- Context compaction mid-session. No work lost — continuation picked up cleanly at subagent updates.
- Two additional subagents (after-build.md, setup.md) needed fold-in destination updates beyond the three originally scoped.

**Carried forward.**

- Smoke test: trigger the fold-in section carve-out against a test project — write a `[FOLD-IN PENDING]` block to UX.md's fold-in section and verify the hook allows it while blocking a main-body edit. Testable against Taskflow via `--plugin-dir`.
- `Crash course.md` → *When you need more* references `plugin/docs/NO-CODE-METHOD.md` which doesn't exist — the behavioural rules live in `plugin/hooks/universal-behaviour.md`. Pre-existing issue, not introduced this session.

---

## v46 — 2026-05-22 — /setup UX + per-project opt-out

**What shipped.** V44 scope. Three major changes: (1) `.no-code-method-skip` marker architecture removed from the public plugin — `OPT_OUT_MARKER_NAME`, `has_opt_out_marker()`, and case 5 (opted out) removed from `project_state.py`, `pre_tool_use.py`, `session_start.py`, `setup.md` (formerly `adopt.md`), `scaffold.py`, `SKILL.md`, `universal-behaviour.md`, `VOCABULARY.md`, and `Crash course.md`. Per-project opt-out is now Claude Code's built-in `/plugin` → Installed → toggle off. Dev-project's `.no-code-method-skip` stays as a legacy escape hatch (`_LEGACY_SKIP_MARKER`). (2) `/adopt` renamed to `/setup` across the entire plugin surface — skill directory (`plugin/skills/adopt/` → `plugin/skills/setup/`), subagent body (`adopt.md` → `setup.md`), subagent type (`no-code-method:adopt` → `no-code-method:setup`), all hook references, all doc references, Crash course, planning artefacts. (3) Three OPEN-QUESTIONS UX friction items resolved: "scaffold" jargon replaced with plain English in user-facing `/setup` dialogue; next-action prompt added to successful-path recaps (cases 1, 2, 3); Pass/Fail/Skipped one-line explanations added to planning subagent's per-row read-back. V46 scope (cd-shifts-cwd marker walk-up) closed — marker removal made it moot. Permission-prompt surface researched: no difference between marketplace and `--plugin-dir` (written to `research/marketplace-install-permission-surface.md`). Method version V41 → V42; plugin 0.41.0 → 0.42.0.

**Decisions taken and why.**

- **Marker removal before rename.** The marker architecture touched the same files the rename would touch. Removing markers first simplified the rename pass — fewer code paths, cleaner diffs. The v46 session ran the marker removal; the continuation session ran the rename.
- **V46 closed rather than reworked.** V46's scope was "walk up parent directories to find the opt-out marker when `cd` shifts cwd." With the marker architecture removed from the public plugin, the only surviving marker is the dev project's legacy `_LEGACY_SKIP_MARKER` — not worth a walk-up mechanism for one project's internal compat.
- **`detect_adopt_case` function name and `ADOPT_CASE_*` constants kept.** These are internal API imported by `scaffold.py`. Renaming them would be churn with no user-visible benefit — they're never surfaced in dialogue or docs.
- **Narration improvements (V44 output 4) covered by items 1/2.** The jargon fix and next-action prompt address the concrete narration gaps surfaced in the V42 smoke test. No additional narration work needed.
- **CLI vs. desktop-app parity (V44 output 5) deferred.** Requires hands-on testing in both environments. Not a code change — needs Alex to run `/setup` in both and report back.

**Pivots and surprises.**

- Session ran out of context mid-v46 (after marker removal, before rename). Continuation session picked up cleanly from the handoff notes in V44.md.
- OPEN-QUESTIONS entry for the UX friction items now has four of seven items resolved (1, 2, 4, 7); three remain (fold-in UX, after-build commit/tag prompt, template placeholder cleanup).

**Carried forward.**

- CLI vs. desktop-app parity testing — Alex runs `/setup` in both CLI and desktop app against a fresh folder and reports back.
- Remaining OPEN-QUESTIONS UX friction items 3, 5, 6 — can bundle into future sessions touching the relevant components.
- V43 + V44 smoke test still deferred — mode-aware deny messages (V43) and `/setup` rename (V44) both testable against Taskflow via `--plugin-dir`.

---

## v45 — 2026-05-22 — Permission-mode UX harmonization

**What shipped.** Mode-aware deny messages across all seven PreToolUse deny paths. Every deny now carries a `[No-code method]` prefix and a `What to do:` closing line. Four of seven paths (locked-doc lock, batch boundary, adoption gate, destructive git guard) add a mode-aware suffix in permissive Claude Code modes (Accept edits, Auto, Bypass) clarifying that changing permission mode won't help. Three paths (serves-line, test-confirmation gate, MANIFEST read-before-edit) get format standardisation only — their denies are sequencing or fix-it-yourself issues, not mode-sensitive. `permission_mode` field read defensively from hook input JSON; absent or unrecognised values produce no mode-aware text. SessionStart hook now prepends a two-layer-permission-model preamble to the universal-behaviour context injection (tiers 2 and 3). Crash course gains a new *Two layers of permission* section. INVENTORY.md updated with V43 annotations across all three affected hook entries. Method version V40 → V41; plugin version 0.40.0 → 0.41.0.

**Decisions taken and why.**

- **Format standardisation bundled with mode-awareness** rather than deferred as a separate session. The prefix and closing-line format are low-cost and make every deny identifiable as method-originated regardless of mode — splitting them would have delivered mode-awareness without the identity signal.
- **Zero behaviour changes shipped.** Two candidates evaluated: Plan mode + edit denies (return `defer` to avoid double-deny noise) and MANIFEST read-before-edit in Auto mode (allow with inlined context on first attempt). Both deferred. Plan mode needs a smoke test to determine whether hooks fire on plan-mode tool calls. MANIFEST's "allow with context" would require the hook protocol to support injecting context into an allow decision, which it doesn't.
- **Substring-based mode detection** (`"auto" in mode.lower()`) rather than exact enum matching. The `permission_mode` field's exact string values are unverified. Substring matching tolerates casing/formatting variation. False-positive risk low — suffix is informational, not behaviour-changing.

**Pivots and surprises.**

- Context compaction mid-session. No work lost — compacted summary captured the full design agreement and all file paths.

**Carried forward.**

- Smoke test deferred: trigger each deny path in at least two permission modes (default + one permissive) and verify the deny message is mode-appropriate. Testable against Taskflow via `--plugin-dir`.
- Plan mode investigation: whether PreToolUse hooks fire on plan-mode tool calls is unverified. Testable during the smoke-test session.
- V45 forward dependency: the distributed-fold-ins session will add an append-only carve-out on locked docs. Its new "partial allow" path needs its own `[No-code method]`-prefixed, `What to do:`-terminated message using the `_mode_suffix` helper V43 ships.

---

## v44 — 2026-05-22 — Consumer-batch structure ideation + V49/V50 scoping

**What shipped.** Dev-internal ideation session. Two threads ran:

1. **Doc-structure inventory of V-files.** Interrogated which of the six V-file scope sections (`Goal`, `Inputs`, `Outputs`, `Success criteria`, `Open questions for this session`, `Risks / dependencies`) should propagate to consumer-project BACKLOG batches. All five non-`Inputs` sections landed (`Inputs` already coming via V45), with two renames: *Open questions for this session* → *Decisions to make this batch* (disambiguates from V45's BACKLOG open-questions section); *Risks / dependencies* split into *Risks* (scoped out — degrades to hand-waving for non-coder users) and *Dependencies* (kept, peer to existing `Blocks:` field). Re-framing surfaced mid-interrogation: consumer batches will skew V-file-sized, not sprint-slice-sized, because the method exists for non-coder users who absorb ideas mid-stream — so the structural symmetry holds.

2. **File-naming convention + numbering churn.** Current V-numbering causes rename churn whenever priority shifts. Web search confirmed ADR-style (`NNNN-kebab-title.md`) as the conventional fix: number allocated at creation by filesystem scan, never renumbered; build order moves to a separate index (PLAN.md dev-side, BACKLOG/INDEX.md consumer-side). Scope split into V49 (consumer-batch structure overhaul) and V50 (ADR-style numbering + per-batch file-split + migration) — V50's file-split only makes sense after V49's batch structure exists.

**Files created/edited:**
- `planning/sessions/V49.md` — consumer-batch structure overhaul scope.
- `planning/sessions/V50.md` — ADR-style numbering + per-batch file-split scope.
- `PLAN.md` — V49, V50 rows added; `V49+` placeholder updated to `V51+`; session count 31 → 33.
- `planning/OPEN-QUESTIONS.md` — new entry parked at top: *Red-flag / threat-class marker for security-shaped batches* (surfaced when separating dependency-risk from security-risk in the Risks/Dependencies interrogation).

**Decisions taken and why.**

- **Split overhaul into V49 then V50** rather than bundle. V49 ships section-additions inside the current single-file BACKLOG.md (lower risk, immediate value). V50 then splits batches into files and adopts ADR-style numbering across both dev-side V-files and consumer-side batches. Decouplable: V49 doesn't need file-split; V50's file-split would be wasteful without V49's structure.
- **Retroactive rename in V50, not partial cutover.** When V50 runs, all V-files `V18.md`–`V49.md` get renamed to ADR-style and references are swept across BUILD-LOG, OPEN-QUESTIONS, INVENTORY, project CLAUDE.md, plugin docs. Cleaner long-term than living with a two-system mix. Cost is the reference sweep — accepted.
- **No new slash command for session creation in V50.** Allocation rule alone (filesystem scan, baked into subagent + `BUILD-METHOD.md`) is sufficient. Slash command parked as optional follow-up if friction emerges.
- **Risks section explicitly scoped out of V49's consumer-batch structure.** For non-coder users, "what could go wrong with this batch?" tends to produce either obvious-and-already-handled concerns or vague-and-imaginary anxieties. Planning subagent can surface concrete risks verbally in the recap without a forced section.
- **Red-flag/threat-class concern parked separately** rather than bundled into V49. Conflation between build-dependency risk and security/threat-class risk surfaced mid-interrogation; pulling threat-class into V49 would stretch its scope. Parked in OPEN-QUESTIONS with three possible shapes.

**Pivots and surprises.**

- **Re-framing on session size.** Initial framing assumed consumer batches would skew smaller than V-files because consumer projects are "less complex." Alex pushed back: the method exists precisely because non-coder users absorb ideas mid-stream and need a scoping moment to batch them. That recalibrated the entire interrogation — five sections landed instead of being filtered down to two or three.
- **Crash course addition surfaced mid-interrogation.** The "method absorbs mid-stream ideation" framing earned its own slot in Crash course. Filed as a deliverable of V49 (it's the *why* underneath V49's *what*).

**Carried forward.**

- V49 and V50 await build.
- Red-flag / threat-class OPEN-QUESTIONS entry awaits trigger (Taskflow batch with security-shaped scope, OR subsequent batch-structure ideation that bundles it).

---

## v43 — 2026-05-22 — Permission-mode research + roadmap rescope V43–V48

**What shipped.** Dev-internal. Web research confirmed that Claude Code's PreToolUse hooks fire in every permission mode (Ask permissions, Accept edits, Plan mode, Auto mode, bypass) — the `permission_mode` field is delivered in hook input JSON, and a hook returning `deny` blocks the tool call regardless of mode. This resolves OPEN-QUESTIONS item 4 (permission modes vs. UX.md lock) from the post-adopt UX friction entry: the method's lock is complementary to Claude Code's permission system, not redundant. The finding motivated a new session: **V43 (permission-mode UX harmonization)** — audit every deny path against every permission mode, design mode-aware deny messages and behaviour changes so users in permissive modes don't mistake method blocks for broken permissions. Roadmap renumbered V43–V48 to accommodate: old V43 (vocab sweep) → V47, old V46 (test split) → V48, old V47 (cd fix) → V46. V44 and V45 unchanged. All cross-references updated across scope files, PLAN.md, OPEN-QUESTIONS.md, CLAUDE.md, research/platform-capabilities-audit.md. Pattern follows v41 (rescoping session takes the slot, existing scope files shift).

**Decisions taken and why.** Permission-mode session placed at V43 (top of the queue) because the UX gap affects every user in every permissive mode from day one — higher impact than vocabulary polish or cd-fix plumbing. Vocab sweep displaced to V47 rather than dropped because V48 (test split) depends on it. Cd fix moved to V46 (filling the gap) because it's small with no dependencies.

**Pivots and surprises.** Session opened expecting to run V43 (vocab sweep). Alex redirected to permission-mode research after recalling the OPEN-QUESTIONS item about permission modes vs. UX.md lock. The research answer was clear enough to scope a full session rather than park as a note.

**Carried forward.** OPEN-QUESTIONS post-adopt UX friction items 1, 2, 5, 6, 7 (small subagent/template fixes) — noted in the updated *Next step* as candidates for V44 or a standalone batch. Item 3 (fold-in UX) remains tied to V45.

---

## v42 — 2026-05-21 — Git-diff drift detection + direct-edit confirmation protocol

**What shipped.** New **drift check 1 — direct-edit detection** in the planning subagent (`plugin/agents/planning.md`). At planning-session start, Claude runs `git diff <last-tag>...HEAD` plus working-tree diff (or `git diff HEAD` if the project is untagged) to surface files touched outside the build cycle. Files in the previous batch's `Files:` sub-section and the method's writable surface (`MANIFEST.md`, `BUILD-LOG.md`, `TEST-LOG.md`, `BACKLOG.md`, `CLAUDE.md`) pass silently. Everything else triggers a per-file confirmation walk — Claude shows the path + change summary + any matching MANIFEST entry, asks *"Was this you (direct edit)? Yes / No / not sure"*, and routes on the answer:

- **Yes** → check upcoming `BACKLOG.md` batches for `Files:` conflicts; if none, accept (MANIFEST entry stands as-is, or propose an addition for the next build); if the edit implies a UX.md update, queue a standard `[FOLD-IN PENDING]` via the preview-then-fold-in convention.
- **No** / **Not sure** → flag as unexpected, pause planning until the source is identified.

Existing checks renumbered 2–5 (UX↔build, MANIFEST↔code, MANIFEST↔UX loose, retest-after-change). Per-file walk, no bulk-confirm — pattern mirrors the per-row TEST-LOG read-back for the same "never infer" reason. Resolves the remaining shapes from V22's partial fold-in of *Method response to direct-edit users*; shapes #2 (developer-mode entry point) and #3 (explicit non-audience) deferred until a real developer reports friction. **Doc-code parity:** VOCABULARY's *Drift check* definition updated (four → five); DOC-STRUCTURE's TEST-LOG pruning rule reference renumbered (check 4 → check 5); after-build.md and VOCABULARY's *Frame-correction sweep* references renumbered (check 1 → check 2); Crash course's drift-checks section expanded to five with a new bullet for direct-edit detection; INVENTORY's planning-subagent entry annotated. Method version V39 → V40; plugin 0.39.0 → 0.40.0; `PLUGIN_METHOD_VERSION` → 40; all plugin-side footers bumped. Repo-root docs-only set stays frozen at V39 (v40 shelving). OPEN-QUESTIONS entry *Method response to direct-edit users* removed. No smoke test yet — see *Carried forward*.

**Decisions taken and why.**

- **Numbered as drift check 1, not check 5.** The V42 scope file leaned "fifth check that runs first." Renumbered instead so order-of-execution and order-of-listing match — cleaner mental model, smaller cognitive load on the future-Claude reading the procedure mid-session. Cost: small parity sweep across VOCABULARY, DOC-STRUCTURE, after-build.md, Crash course, INVENTORY for the "drift check N" references. Worth it.
- **Per-file walk, no threshold mechanism.** Scope file raised "threshold for noisy diffs" as an open question. Skipped: shipped per-file always, on the same logic as the TEST-LOG per-row read-back — bulk confirmation is the failure mode the protocol exists to prevent. If real use makes the per-file walk painful on large diffs, a deferral mechanism ("walk the remainder next session") is the natural follow-up. The user can already pause mid-walk; that may be enough.
- **No-tag fallback: working-tree-only.** Method recommends but doesn't require tagging. Without a tag we diff working tree vs. `HEAD` — catches uncommitted direct edits (the most common case) and surfaces a one-line "consider tagging" note. Committed-but-out-of-band edits in untagged projects are out of scope for V42. Acceptable: the no-coder method assumes tagging, and the fallback at least catches the uncommitted case without erroring out.
- **Lightweight UX fold-in: standard `[FOLD-IN PENDING]` block.** No reason to invent a thinner shape; the existing mechanism already covers small edits cleanly.
- **No new Required behaviour added.** Considered a *Never auto-attribute manual edits* analog to *Never infer completion*. Decided against — the new logic is concrete procedure (where to look, what to ask) rather than abstract principle, and lives cleanly in `planning.md`. If real use shows prompt-level reinforcement matters, V42 follow-up can promote it.

**Pivots and surprises.**

- None mid-session. Decisions pre-made in scope file held up.

**Carried forward.**

- **Smoke test pending.** Direct-edit detection is the kind of change that wants a real planning-session walkthrough against a fixture with manual edits to validate. Alex to run via `claude --plugin-dir` against a scratch fixture before the session is considered closed. See *Smoke-test instructions* at the bottom of this entry.
- **`plugin/hooks/pre_tool_use.py` deny-message citations of `NO-CODE-METHOD.md`** — still unfixed from v40's carried-forward note (out of scope here).

**Smoke-test instructions (for Alex, post-session).**

1. Create a fresh scratch folder (e.g. `~/v42-scratch`) and run `git init` in it.
2. Run `claude --plugin-dir <path-to-this-repo>/plugin` from inside it. Run `/adopt` to scaffold the spine docs (case 1, empty folder), seed a first build batch, ship it (`/before-build` then `/build`), and tag (`git tag v1`).
3. `/clear`. Outside Claude Code, manually edit one of the files the batch touched — change a function body inside a file in the previous batch's `Files:` list, or add a new file unrelated to any batch.
4. Open a new Claude Code session with `--plugin-dir` and paste test notes from the previous build (or just say "let's plan").
5. **Expected:** planning subagent runs drift check 1, surfaces the manually-edited file, walks the confirmation prompt (*Was this you? Yes / No / not sure*). On *Yes*, it accepts and (depending on the edit) proposes a MANIFEST update or queues a `[FOLD-IN PENDING]`. On *No*, it pauses.

If anything doesn't fire as expected, append a TEST-LOG row with `Fail` status and bring it to the next planning session.

---

## v41 — 2026-05-21 — Rescope OPEN-QUESTIONS into V45–V47

**What shipped.** Dev-internal. Three major OPEN-QUESTIONS entries (plus one V39-surfaced entry) scoped into future build sessions with full scope files. Pattern follows V31 (rescoping session). No plugin code, no method-version bump. Existing V41–V43 renumbered to V42–V44 (following V31 precedent — scoping session takes the slot, existing scope files shift up).

- **V45 scope file** (`planning/sessions/V45.md`) — distributed fold-ins + BACKLOG open-questions section + batch `Inputs:` line. Largest structural rewrite of V45–V47. Prerequisite #1 for the graduation meta-goal.
- **V46 scope file** (`planning/sessions/V46.md`) — automated vs. manual test split + four non-UI test types. Depends on V43 (non-GUI vocab) and V45 (`Inputs:` line as carrier for per-batch test spec). Prerequisite #2 for the graduation meta-goal; after V46, graduation becomes promotable.
- **V47 scope file** (`planning/sessions/V47.md`) — `cd`-shifts-cwd opt-out marker fix. Decisions pre-made (shape A marker-walk-up, bounded by first `CLAUDE.md`/`.git`-bearing ancestor). Smallest of the three.
- **PLAN.md** — v41 scoping row added; V42–V47 rows updated (renumbered from V41–V46); V48+ parked grab-bag retargeted; session count 26→30.
- **OPEN-QUESTIONS.md** — *Next step* lines updated on distributed fold-ins (→V45), test split (→V46), cd-cwd (→V47), UX.md adaptation (→V43), planning-vocab collision (→V43), direct-edit users (→V42). Meta-goal entry's prerequisites list annotated: all four now scheduled; graduation promotable after V46 ships + one verification cycle.
- **CLAUDE.md** — *Current state* bumped to v41; *What's next* expanded through V47.
- **V44.md** (was V43) — added a Risks note to consider folding V47 into V44 at session start (both touch adoption-gate hook logic; V47 is small enough to bundle if V44's surface is light).

**Decisions taken and why.**

- **V45 before V46.** V46's per-batch test spec needs V45's `Inputs:` line as its natural carrier. V45's open-questions section also gives V46's between-session design decisions a place to park. Dependency is soft — V46 could ship without V45 by inventing an isolated `Tests:` sub-section — but the surface is cleaner together.
- **V47 kept separate from V44.** Both touch adoption-gate hook logic, but V44 is user-facing UX and V47 is internal plumbing. V44 is already 5-outputs heavy. Note added to V44.md's Risks to reconsider at V44 session start.
- **Renumbering applied (fix commit).** Initially shipped without renumbering (appended V44–V46 after existing V41–V43). Session tag v41 collided with scope file V41.md — next session's scope-file lookup skipped V41 and jumped to V42. Fixed by shifting V41→V42 through V46→V47, following the V31 precedent.

**Pivots and surprises.**

- **Numbering collision caught post-push.** The initial commit shipped without renumbering; Alex discovered the next session skipped to V42. Root cause: session tag v41 consumed the V41 slot, so the session-open rule ("lowest V# above current built version") bypassed V41.md. Fix: follow the V31 pattern (scoping session takes the slot; existing scope files shift up by one). Amend commit added.

**Carried forward.**

- **No `Vxx.md` scope file** was created for v41 — the session was ad-hoc, like v40.
- **No smoke test** — pure planning-artefact change.
- **`plugin/hooks/pre_tool_use.py` deny-message citations of `NO-CODE-METHOD.md`** — still unfixed from v40's carried-forward note.

---

## V40 — 2026-05-21 — Shelve the two-write rule for canonical docs

**What shipped.** Dev-internal. The V32 two-write rule (parallel plugin-side and docs-only canonical doc sets, both bumped on every method version change) is shelved. The repo-root prose-only set (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`) and the repo-root `templates/` mirror are frozen at method version V39 with a notice at the top of each file. Plugin-side becomes the sole operational source. Method version stays at V39; no footer bump.

- **Repo-root prose docs.** Added a FROZEN notice (top of file) to `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`. Each notice names the V39 freeze, points at the plugin-side live equivalents, and links the resume path back through OPEN-QUESTIONS.
- **Repo-root templates.** Added matching FROZEN notices to all seven (`CLAUDE-TEMPLATE.md`, `BACKLOG-TEMPLATE.md`, `MANIFEST-TEMPLATE.md`, `UX-TEMPLATE.md`, `TEST-LOG-TEMPLATE.md`, `BUILD-LOG-TEMPLATE.md`, `ADDITIONAL-DOC-TEMPLATE.md`). Each notice names the live template at `plugin/templates/<filename>` — that's what `/adopt` scaffolds.
- **BUILD-METHOD.md** — four edits. *Session open* step 2 switched from `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md` to `plugin/hooks/universal-behaviour.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`. *Doc-code parity* step 3 "Two locations" requirement collapsed to plugin-side. *Two-write rule for canonical docs* section annotated as shelved at top, body retained for resume-ability. *Footer bumps* docs-only subsection renamed to "Docs-only side — SHELVED in v40 (no longer bumped)" with a non-bump notice.
- **Project root CLAUDE.md** — Inside-the-repo bullets and terminology cheat sheet updated to mark the docs-only set and `templates/` as frozen at V39. *Current state* section advanced to v40 with the dev-internal note.
- **Plugin-side prose references.** Updated the docs-only-spec-maintained-alongside wording in `plugin/agents/planning.md`, `before-build.md`, `after-build.md`; `plugin/hooks/universal-behaviour.md` (two sites); `plugin/docs/VOCABULARY.md`; `plugin/templates/CLAUDE-TEMPLATE.md`. All now describe the repo-root set as a frozen V39 snapshot rather than a parity-tracked twin.
- **Planning artefacts.** `planning/INVENTORY.md` — three doc-fate rows (`DOC-STRUCTURE.md`, `VOCABULARY.md`, `NO-CODE-METHOD.md`) rewritten. `planning/OPEN-QUESTIONS.md` — removed the *Shelve the two-write rule* entry (resolved); updated the *Graduate sovereign-implementer dev onto sovereign-implementer* meta-entry's prerequisite 3 to "Done in session v40." `planning/PLAN.md` — new V40 row for this session; renumbered original V40→V41, V41→V42, V42→V43; updated counts ("26 sessions through V43"); V43+ catch-all gained a "restoration of two-write maintenance" line.
- **Scope files.** `planning/sessions/V42.md` → `V43.md`, `V41.md` → `V42.md`, `V40.md` → `V41.md` (via `git mv`). Internal H1 headings updated to match. V41 (was V40, drift detection) trimmed: dropped `NO-CODE-METHOD.md (docs-only)` from Inputs/Outputs, dropped "both sides" from Success criteria. V42 (was V41, vocab sweep) — bundling-rationale note added at the top flagging that the parity-audit-amortisation argument dissolves; Inputs/Outputs/Success criteria collapsed to plugin-side.
- **README.md** — repo-root prose docs and `templates/` lines updated to reflect the freeze.

**Decisions taken and why.**

- **Freeze rather than archive or delete.** Per OPEN-QUESTIONS's leaning. Lowest blast radius — the docs continue to exist for anyone who already linked at them (notably `plugin/templates/CLAUDE-TEMPLATE.md` and `plugin/hooks/universal-behaviour.md`'s signature footer, which point at `NO-CODE-METHOD.md`). Resume path is one OPEN-QUESTIONS promotion away. Archive folder added overhead without payoff; deletion was destructive for hypothetical gain.
- **Annotate `BUILD-METHOD.md` → *Two-write rule* in place rather than removing the section.** Same resume-ability logic. If we restore the rule later, the body's still there; the annotation just suspends enforcement.
- **Own session (v40) rather than folding into V40-drift-detection.** Mixing scope muddies BUILD-LOG. Renumbering three scope files cost ~five edits; merging would have cost discipline. Per BUILD-METHOD's "one tag at a time" principle.
- **Method version stays at V39.** Dev-internal change — no plugin or method-substance change. Per BUILD-METHOD *Session tag vs. method version*: dev-internal sessions don't bump the footer. The frozen repo-root docs retain their V39 footers in perpetuity (until two-write is restored, if ever).

**Pivots and surprises.**

- **`plugin/templates/CLAUDE-TEMPLATE.md` references `NO-CODE-METHOD.md`** — discovered during the plugin-side reference sweep. The template's intro paragraph points the no-coder at the GitHub URL of `NO-CODE-METHOD.md` as the "full project-agnostic method spec." With the file frozen, that link now points at a V39 snapshot rather than live spec. Wording adjusted to call it a "frozen prose snapshot" and explain the shelving. No URL change.
- **Plugin hook deny messages still cite `NO-CODE-METHOD.md` → Section X** at four sites in `plugin/hooks/pre_tool_use.py`. Left as-is per the chat-time decision to flag rather than fix. Future cleanup: repoint to `plugin/hooks/universal-behaviour.md` and `plugin/docs/VOCABULARY.md` as appropriate. Not blocking — the cited sections still exist in the frozen file.
- **V42 (renumbered vocab sweep) bundling rationale dissolves.** The session was bundled because two questions both needed a grep-and-rewrite across both sides of the two-write rule, amortising the parity audit. With v40's shelving, only the plugin side gets touched — bundling is now defensible on surface-area grounds (one sweep cheaper than two) but no longer compelling. Note added at the top of `V42.md` flagging the bundling re-decision.

**Carried forward.**

- **No `Vxx.md` scope file** was created for v40 — the decision was made and executed in chat directly. No file to delete at close.
- **`plugin/hooks/pre_tool_use.py` deny-message citations of `NO-CODE-METHOD.md`** — flagged but not fixed. Add to V41+ work or a future tidy-up session.
- **No smoke test** for this session — pure doc / planning-artefact change, no plugin code touched.
- **Three pre-v40 OPEN-QUESTIONS entries swept in.** An earlier discussion session today (2026-05-21) drafted four new OPEN-QUESTIONS entries that sat uncommitted before v40 opened: the *Graduate sovereign-implementer development onto sovereign-implementer* meta-entry plus its three prerequisites — *Distributed fold-ins + open questions section in BACKLOG*, *Automated vs. manual test split + non-UI test types*, and *Shelve the two-write rule*. The fourth (Shelve) is resolved by v40 and was removed; the remaining three are committed alongside v40 since they're part of the same thinking arc.

---

## V39 — 2026-05-21 — MANIFEST paths field + read-before-edit hook gate

**What shipped.** MANIFEST.md gains an optional `(path)` field on each entry; the V25-deferred read-before-edit rule becomes hook-enforced via shape B (inline deny-with-context, transcript-scan retry). Touches both canonical doc sets, both template sides, `after-build.md`, `pre_tool_use.py`, INVENTORY, and resolves one OPEN-QUESTIONS entry.

- **Schema change.** MANIFEST entries now: `- **Name** (\`path/to/file.ext\`) — description`. Three path shapes — single file inline; multi-file as `` (`a.kt`, `b.kt`) ``; directory-level as `` (`dir/`) ``. Paths field is optional, legacy entries skip the gate silently. Documented in both DOC-STRUCTURE.md sides + both MANIFEST-TEMPLATE.md sides.
- **PreToolUse check (6) shipped.** Parses MANIFEST entries, matches target file against paths fields, denies first attempt with the matching MANIFEST entry + UX.md Functionalities entry headings inlined. Retry via transcript scan: deny embeds `BLOCKED [V39 read-before-edit]: <abs path>` marker; subsequent invocations check the session transcript for that marker and allow when present. No state file, no PostToolUse tracking. Spine docs (BACKLOG, MANIFEST, TEST-LOG, BUILD-LOG, CLAUDE) explicitly exempt — defensive guard against an accidental MANIFEST entry deadlocking the build cycle.
- **`after-build.md` MANIFEST update step extended** to populate the paths field when creating, renaming, or first-touching an entry — drives the incremental migration on touch.
- **Read-before-edit rule rewritten** in `universal-behaviour.md` (plugin-side) and `NO-CODE-METHOD.md` (docs-only). Frame shifts from "check first" to "have the context by edit time" — the hook delivers context via the inline deny if Claude doesn't already have it.
- **Crash course updated.** MANIFEST description mentions the paths field; the hooks paragraph adds the V39 inline-deny clause.
- **OPEN-QUESTIONS entry removed** — "MANIFEST.md schema gap blocks PreToolUse read-before-edit enforcement" (V25-era, promoted to V39, now resolved).
- **INVENTORY.md** PreToolUse check (d) updated from "Deferred from V25 — blocked by schema gap" to the V39 shipped wording.
- **Smoke-tested via direct hook invocation** — 7 cases all Pass; see TEST-LOG #116–122. Covered: single-path match, multi-path list match, directory-prefix match, no-match-allow, legacy-entry-skip, spine-doc-exempt, retry-after-prior-deny.
- **Method-version bump 38 → 39** across all 26 footer-carrying files, `plugin.json` (0.38.0 → 0.39.0), `PLUGIN_METHOD_VERSION` (38 → 39).

**Decisions taken and why.**

- **Shape B over shape A.** Pre-session planning settled this. Shape A (PostToolUse Read-tracking + PreToolUse check + session state file) required two new mechanisms (state file + cross-hook coordination). Shape B needs only the paths field — the deny output IS the state, lives in the conversation transcript Claude Code already maintains. Cost-of-implementation half of A, behavioural guarantee the same: Claude can't blindly edit a MANIFEST-covered file. The framing softens (from "read first" to "have-the-context-by-edit-time") but the user-observable effect is identical.
- **Paths field is optional.** Forcing every legacy MANIFEST entry to have a path would break adoption for projects mid-flight. Incremental migration on touch (via after-build) lets the gate grow with the project — no flag-day rewrites. `/adopt` case 4 (refresh) offers one-time backfill for projects wanting full coverage immediately.
- **Three path shapes (single / list / directory).** Single covers the common case. Directory (trailing slash) covers settings-screen-style entries where the scope is genuinely a folder. List shape covers the in-between case (2–3 related files that don't fit a directory). Avoids forcing artificial entries-per-file or imprecise directory matches.

**Pivots and surprises.**

- **Plugin's own adoption gate fired against the dev project mid-session.** Early Bash command `cd sovereign-implementer/ && git describe --tags --abbrev=0` shifted the cwd Claude Code passes to subsequent hooks; the `.no-code-method-skip` marker at the parent `No code method/` folder was no longer at the hook's view of project_root, so the V29 gate started denying every Edit. Recovered by writing a second `.no-code-method-skip` at `sovereign-implementer/` root (which is in SCAFFOLD_NAMES, so the gate allowed even while firing). Both markers stay committed; the new marker also covers any future session that opens with cwd inside the dev project subtree. The deeper issue — Bash `cd` inside a session shifting Claude Code's cwd globally and breaking opt-out markers placed at the original cwd — is logged as a new OPEN-QUESTIONS entry.
- **No smoke test via `--plugin-dir`.** The V39 hook check requires a real Claude Code session transcript to exercise the retry semantics, and the fixture-based direct invocation covered all 7 cases including the retry (via a hand-written fake transcript). A `--plugin-dir` test would add fidelity but the direct-invocation evidence is sufficient for V39 — V40+ Taskflow work will exercise this naturally.

**Carried forward.**

- **V39 scope file deleted** in this commit per the transient-scope rule.
- **New OPEN-QUESTIONS entry** — "Bash `cd` inside a session shifts plugin cwd and breaks the parent-folder opt-out marker." See `OPEN-QUESTIONS.md`.
- **No frame-correction candidates in BACKLOG.md.** V39 added a new gate rather than substantively changing how a feature works. Scope files V40–V42 audited — V40 references the V39 paths field as input and is compatible; V41/V42 don't depend on V39 substance.
- **`.no-code-method-skip` at `sovereign-implementer/` root** — committed alongside the V39 changes so future sessions opening with cwd inside the dev subtree stay silent. Removable by hand if dev-project E2E plugin testing requires the gate to fire.

---

## V38 — 2026-05-21 — Locked-doc edit rules + Sonnet-search discipline

**What shipped.** Three method-discipline changes resolving three OPEN-QUESTIONS entries, touching the PreToolUse hook, both canonical doc sets, all five subagent bodies, and both VOCABULARY files.

- **Footer-stamp carve-out in PreToolUse hook.** New `is_footer_only_edit()` function + `FOOTER_LINE_PATTERN` regex. An `Edit` call that changes nothing except the `*No-code method — Version N.*` footer line now passes through the locked-doc check. `Write` and `MultiEdit` remain blocked (too broad to verify as footer-only). Simplifies `/adopt` case 4 — footer refreshes go through directly, no fold-in blocks needed.
- **Preview-then-fold-in convention.** New `[PROPOSED EDIT]` workflow: during planning and `/adopt`, subagents preview proposed source-of-truth edits in chat (full section with heading and tags), wait for explicit approval, write the `[FOLD-IN PENDING]` block, then prompt the user to fold in *now* rather than deferring. Block specifies replace vs. add. Landed in `universal-behaviour.md` → Editing surfaces, `NO-CODE-METHOD.md` → Editing surfaces, `planning.md` (6-step inline sequence), `adopt.md` case 3, both VOCABULARY Fold-in entries, and `Crash course.md`.
- **Sonnet-search / verify-external-facts rule.** New Required behaviour: don't guess or hedge on external facts — use web-search tools if available, otherwise hand the user a paste-ready Sonnet prompt. Fallback if search can't happen: mark the claim `[UNVERIFIED: <what>]` inline. Landed in `universal-behaviour.md`, `NO-CODE-METHOD.md`, `Crash course.md`.
- **Three OPEN-QUESTIONS entries removed** — "Footer-stamp on locked source-of-truth docs," "Source-of-truth doc edits with no-coder permission," and "Method rule: ask the user to run a Sonnet web search." All resolved by V38's changes.
- **Method-version bump 37 → 38** across all 26 footer-carrying files, `plugin.json` (`0.37.0` → `0.38.0`), `PLUGIN_METHOD_VERSION` (`37` → `38`).

**Decisions taken and why.**

- **Preview convention instead of a PreToolUse planning-context carve-out.** The hook can't identify which subagent made a tool call (no caller identity in hook protocol), so a "planning subagent may edit locked docs" exception would require a state-file mechanism. Keeping the lock intact and improving fold-in UX (preview → approve → fold in now) was simpler and preserved the lock's safety guarantee.
- **`[UNVERIFIED: <what>]` as fallback, not a hard block.** The user can't always run a Sonnet search (no second window, mid-flow, etc.). Marking uncertain claims inline lets work continue while making the uncertainty visible and retestable.
- **Footer-stamp carve-out scoped to `Edit` only.** `Write` replaces the entire file (can't verify it's footer-only), `MultiEdit` can bundle footer + content changes. `Edit` with the strip-and-compare check is the tightest guarantee.

**Pivots and surprises.**

- **adopt.md case 4 recap template was stale.** After adding the footer-stamp carve-out to case 4's procedure, the recap template still referenced `[FOLD-IN PENDING]` blocks for locked docs. Caught in parity audit and fixed.
- **Context window ran out mid-session.** Session continued via summary-and-resume. The summary was accurate — no rework needed on resume.

**Carried forward.**

- **V38 scope file deleted** in this commit per the transient-scope rule.
- **No new OPEN-QUESTIONS entries** — no ideas raised that aren't already tracked.
- **No smoke test** — no new hook logic exercisable without a consumer project build cycle. The footer-stamp carve-out and preview convention will get real exercise in Taskflow's first batch under V38+.

---

## V37 — 2026-05-21 — Marketplace.json + local install + first globally-installed smoke test

**What shipped.** Plugin packaging for marketplace distribution and local install, plus the first smoke test running the plugin without `--plugin-dir`.

- **`.claude-plugin/marketplace.json`** at repo root. Single-plugin marketplace named `sovereign-implementer`, owner `FlintCraftTech`, relative-path source `./plugin`. Validates clean via `claude plugin validate .`. Same file works for local install (`/plugin marketplace add ./`) and public `git clone` distribution with no restructuring at publication time.
- **Local install completed.** `claude plugin marketplace add ./` + `claude plugin install no-code-method@sovereign-implementer` — plugin persists across sessions at user scope without `--plugin-dir`.
- **Smoke test against `~\v37-scratch`** (empty folder, no `--plugin-dir`): SessionStart tier 1 silent (correct), `/hooks` shows both `[Plugin]` PreToolUse hooks, `/adopt` case 1 fires and delivers first prompt, `/reload-plugins` loads full surface (1 plugin · 2 skills · 11 agents · 4 hooks). See TEST-LOG #109–115.
- **`README.md` updated** — install instructions (marketplace path), license reference corrected from MIT to PolyForm Noncommercial 1.0.0, streamlined structure with pointer to `Crash course.md`.
- **Method-version bump 36 → 37** across all 26 footer-carrying files, `plugin.json` (`0.36.0` → `0.37.0`), `PLUGIN_METHOD_VERSION` (`36` → `37`). Plugin-side packaging change warrants the bump.

**Decisions taken and why.**

- **Marketplace name `sovereign-implementer`** — matches the repo name, distinct from reserved names, reads cleanly in install command (`/plugin install no-code-method@sovereign-implementer`).
- **License stays PolyForm Noncommercial 1.0.0** (already present in `LICENSE` from a prior session). README's MIT reference was stale; corrected.
- **No version in marketplace.json plugin entry.** With `strict: true` (default), `plugin.json` is authoritative for version. Avoids conflict where both declare version and `plugin.json` silently wins. The `PLUGIN_METHOD_VERSION` tripwire in `session_start.py` reads from `plugin.json`; keeping version there keeps the chain intact.
- **Marketplace `description` added** after first validation surfaced a warning. One-line summary matching the README opener.

**Pivots and surprises.**

- **`/hooks` display difference between `--plugin-dir` and globally-installed.** Previous smoke tests (#035, #091) via `--plugin-dir` showed 3 plugin event types (SessionStart, PreToolUse, Stop). V37's globally-installed test showed only PreToolUse in `/hooks`, though SessionStart and Stop demonstrably fired (tier 1 silence = SessionStart ran; `/adopt` subagent completion = Stop hook domain). The display gap is cosmetic — hook behaviour is identical. Worth noting for the `/adopt` permission-prompt UX OPEN-QUESTIONS entry.
- **`claude -p "~\v37-scratch"` misfire.** `-p` sends a prompt, doesn't set project directory. Session ran against `sovereign-implementer/` instead of the scratch folder. Corrected by `cd ~\v37-scratch && claude`. Minor — but worth documenting since Alex's command-line experience is limited and future smoke-test instructions should use `cd` + `claude`, not `-p`.

**Carried forward.**

- **V37 scope file deleted** in this commit per the transient-scope rule.
- **`~\v37-scratch` can be deleted** — served its purpose as a smoke-test fixture.
- **OPEN-QUESTIONS entries unchanged** — no V37-specific entries added; no existing entries' conditions triggered this session.

---

## V36 — 2026-05-21 — OPEN-QUESTIONS doc-only bundle: TEST-LOG newest-first, BACKLOG authority, plan-panel resolved

**What shipped.** Three doc-only items scoped by `V36.md`, plus the method-version bump that catches up from V35's no-bump close.

- **TEST-LOG.md flipped to newest-first** across both `DOC-STRUCTURE.md` copies (new *Ordering* paragraph added, *Template* and *Pruning rule* paragraphs revised to reference it), both `TEST-LOG-TEMPLATE.md` files (HTML format-reminder comment moved above the empty table; the comment now carries the ordering note inline), `plugin/agents/after-build.md` step 3 (specifies top-of-table-body position with within-batch recap order), and `plugin/agents/planning.md` *Order* paragraph (cross-refs the new ordering). Transition stance — existing rows in projects whose `TEST-LOG.md` predates this rule stay where they are — landed as an italicised sentence inside the *Ordering* paragraph.
- **BACKLOG-authority sentence** added to *During planning*'s opening paragraph in root `NO-CODE-METHOD.md` and to `plugin/agents/planning.md`'s opening (two-write). One sentence asserting planning holds structural authority over `BACKLOG.md` — every change is Claude's to make directly, user reviews after rather than applying edits described to them.
- **Plan-panel question resolved.** Sonnet research (`research/claude-code-plan-panel-research.md`, written this session) confirmed Claude Code's plan-mode panel is not programmatically writable from outside Claude — no hook output field, MCP tool, file convention, CLI flag, or env var populates it; it's exclusively driven by Claude's native `ExitPlanMode` flow. Per V36.md's "not writable" outcome handling, the question collapsed to a caveat paragraph in `Crash course.md` (under the existing CLAUDE.md-instruction-headwind paragraph) explaining the limitation and pointing readers to `BACKLOG.md` → Build batches for the real sequence. OPEN-QUESTIONS *Surface the current build sequence in Claude Code's plan panel* entry removed (graduation path 4 — substantively resolved by research, not dropped as irrelevant).
- **Method-version bump 34 → 36** across all 26 footer-carrying canonical doc files (both two-write sides), plus `plugin.json` (`0.34.0` → `0.36.0`) and `PLUGIN_METHOD_VERSION` in `session_start.py` (`34` → `36`). V35 was dev-internal-only and didn't bump; V36's spec change (TEST-LOG ordering) is the trigger that catches the version up. Footers move 34 → 36, skipping 35.

No smoke test — doc-only session per `BUILD-METHOD.md` → *Doc-only sessions*. Doc-code parity audit clean: the TEST-LOG parser (`plugin/scripts/project_state.py` → `parse_test_log_rows`) filters by `Session` column + confirmation status, both ordering-agnostic, so the ordering flip needs no code change. Frame-correction sweep found only dev-internal "newest at bottom" references (`BUILD-METHOD.md` lines 229 + 314, `TEST-LOG.md` line 3) — all legitimately stay newest-at-bottom under the explicit dev-vs-consumer separation; zero consumer-side candidates for change.

**Decisions taken and why.**

- **BACKLOG-authority sentence lives in `plugin/agents/planning.md`, not `plugin/hooks/universal-behaviour.md`.** V36.md's input list (written at V34) named universal-behaviour.md as the plugin-side target, but that file holds cross-phase rules with no *During planning* section — the phase-specific operating procedure for planning lives in `planning.md` per V32's split. The deviation was caught at edit time, surfaced to Alex, and confirmed: substance went into planning.md, scope-file path was wrong. Substance identical across both two-write copies; only the file location differs from what V36.md named.
- **Plan-panel resolved as a caveat in `Crash course.md`'s existing Caveats section** (alongside the "30% CLAUDE.md instruction-following" headwind). Same section, same "known limitation, here's how to work around it" register. Avoided creating a standalone section for a single-paragraph note. Pointer to `BACKLOG.md` → Build batches gives the no-coder the right place to look when the panel reads empty mid-build.
- **Method version 34 → 36 in one jump** (skipping 35). V35 was dev-internal-only per `BUILD-METHOD.md` → *Session tag vs. method version* — no method-side substance changed in V35, so its footers stayed at 34. V36's TEST-LOG ordering flip is substantive, so this session catches the footer up. Session tag (`v36`) and method version (`36`) re-lock — both move together going forward until another dev-internal-only session de-syncs them.

**Pivots and surprises.**

- **V36.md drafting error caught at edit time.** The scope file's Inputs / Outputs sections named `plugin/hooks/universal-behaviour.md` as the plugin-side target for #2's BACKLOG-authority sentence. That file holds the universal cross-phase rules (push back, plain English, ask rather than guess, etc.) — no *During planning* section, by V32's design. The actual plugin-side home for *During planning*'s operating procedure is `plugin/agents/planning.md`. The mistake went undetected when V36.md was drafted at V34 because the writer (me) didn't cross-check the file content against the new architecture. Pattern flag for future scope-file writers: when naming a plugin-side file in a scope's Inputs, open it and confirm the named section actually exists in the post-V32 layout.
- **Footer-bump parallelism hit "File has not been read yet" on 16 files.** Edit requires a prior Read in the same session; bumping footers across the full canonical doc set needs a batch read first. Resolved with parallel one-line reads then re-running the failed edits. Worth noting for future version-bumping sessions: batch-read all footer-carrying files before the bump loop.

**Carried forward.**

- **V37 scope (`planning/sessions/V37.md`) unchanged** — marketplace.json + local install + smoke test queued post-V36 per V35's planning.
- **Remaining OPEN-QUESTIONS entries (11) stay parked** per their existing *Next step* lines — most pending V35 evidence + first real Taskflow use. The plan-panel entry's design-half pairing with the vocabulary-collision question is dissolved by the plan-panel resolution; vocabulary-collision now stands alone and its own *Next step* ("promote to a planning session in V36+ post-E2E (V35) once Taskflow use gives concrete sense of how often readers encounter both terms together") is unaffected.
- **`research/claude-code-plan-panel-research.md` retained** as the basis-of-decision record for V36's plan-panel resolution, in the same convention as V35's `research/plugin-marketplace-scoping.md`. Sonnet research outputs stay alongside the BUILD-LOG entry that consumed them.
- **V36 scope file deleted** in this commit per the transient-scope rule.

---

## V35 — 2026-05-21 — E2E Taskflow test — `/adopt` validated; planning-subagent first contact

**What shipped.** Dev-internal only — no plugin code or method-doc structural changes. Three planning artefacts plus a research file.

- **First plugin run against real Taskflow** (not a synthetic fixture). Two `claude --plugin-dir` sessions: a previous one (since blown up) that took `/adopt` case 1 cleanly through migrate on `Taskflowapp/` with foreign CLAUDE.md, scaffolded BUILD-LOG.md + TEST-LOG.md; and this session's `/adopt` case 4 refresh after real Taskflow planning docs were dropped in from `Taskflowapp/New-docs/`. Case 4 correctly bumped footers on BACKLOG.md + MANIFEST.md (writable per V29 #083 fix), recognised CLAUDE/BUILD-LOG/TEST-LOG as already-V34, and routed UX.md + SYSTEM-PROMPT.md footer additions through `[FOLD-IN PENDING]`. See TEST-LOG #104–108.
- **Two new OPEN-QUESTIONS entries** (newest first):
  - *Footer-stamp on locked source-of-truth docs routed through [FOLD-IN PENDING]* — surfaced by case 4 refresh forcing manual fold-in for a footer line (metadata, not content). Paired with the existing *Source-of-truth doc edits with no-coder permission* entry for a future joint session.
  - */adopt permission-prompt UX and narration for new users* — added in the blown-up prior session, picked up in this commit. CLI `--plugin-dir` permission prompts are user-opaque; marketplace-installed surface untested; CLI vs. desktop pre-fill differences captured as a sub-bullet.
- **Marketplace path researched.** Sonnet output at `research/plugin-marketplace-scoping.md` confirmed: manifest is `.claude-plugin/marketplace.json` at repo root; relative `source: "./plugin"` works for both local install and public GitHub distribution; minimal manifest is ~15 lines. `/plugin marketplace add ./<repo>` is the recommended local-install path — no hosting, persists across sessions, `/reload-plugins` picks up edits.
- **V37 scope created** at `planning/sessions/V37.md` — marketplace.json + local install + smoke test.

**Decisions taken and why.**

- **V35 closes as planning/observational, not full E2E.** Scope expected a planning → before-build → build → after-build cycle. We got SessionStart safety net + `/adopt` (cases 1 and 4) + planning subagent into question 1 of 5 of a [SEQUENCE] before halting (the plugin's questions clashed with decisions already settled in Alex's separate Taskflow Planning project). Rather than walk synthetic continuation, the remaining-phase coverage will arrive naturally as real Taskflow batches go through.
- **No method-version bump.** Two OPEN-QUESTIONS entries + a research file + a new V37 scope + a BUILD-LOG entry + TEST-LOG rows. No plugin code, no method-doc structural change. Dev-internal only per `BUILD-METHOD.md` → *Session tag vs. method version*.
- **V37 = marketplace.json as its own session, not folded.** V35 is already in an awkward state; V36 is doc-only OPEN-QUESTIONS bundle. Marketplace.json is plugin-side packaging — warrants its own footer bump and a clean smoke test.
- **Local marketplace install over `~/.claude/plugins/` copying.** Sonnet research §6 explicitly recommends `/plugin marketplace add` over manual cache writes. Same `marketplace.json` serves local and public distribution; the trade-off I'd initially flagged ("two configurations of the same file") was wrong — relative `./plugin` source works for both.

**Pivots and surprises.**

- **Previous session blew up mid-planning-subagent.** First `claude --plugin-dir` run reached the planning subagent's [SEQUENCE] for the "Unassigned dated tasks" planning batch and stopped because the questions clashed with already-resolved Taskflow decisions. Handoff prompt captured the state; the V35 commit picks up the OPEN-QUESTIONS entry the prior session added but never committed.
- **`/adopt` first run launched from `C:\Users\Alex` (home dir).** Subagent's sanity check caught it — detected Windows user profile as adoption target, refused to scatter spine docs there. Real-world catch that would have been a disaster without it.
- **Marketplace path was much shorter than originally framed.** I'd previously called this a separate packaging session blocked on schema uncertainty. Sonnet research surfaced `/plugin marketplace add ./<repo>` as a single-command local install — no hosting, no publication. V37 is now small and concrete.
- **My "two configurations" framing on local vs public marketplace was wrong.** Alex pushed back ("How does this affect the way we publish later?"); re-reading the research showed relative-path source works for both audiences. Correction recorded; no OPEN-QUESTIONS entry needed.

**Carried forward.**

- **Full E2E cycle (planning → before-build → build → after-build) remains owed.** V35's scope expected it; V35 closes without it. Folds into normal Taskflow use rather than a dedicated retest session — real batches will exercise the remaining subagents naturally.
- **V37 (marketplace.json + local install)** scope file created; queued post-V36.
- **V35 scope file deleted** this commit per the transient-scope rule.

---

## V34 — 2026-05-21 — Consumer-method git workflow + OPEN-QUESTIONS promotion

**What shipped.** Two deliverables scoped by `V34.md`, plus an OPEN-QUESTIONS promotion and a Cowork drift cleanup folded in.

- **Recommended habits line** in docs-only `NO-CODE-METHOD.md` → *After building*: "tag and push after every shipped build batch." Windows-specific sub-bullet warns about `.git/index.lock` contention from Claude Code's background `git status` polling, with `del .git\index.lock` as recovery. Crash course updated with a mention in the habits-layer paragraph.
- **PreToolUse git safety-guard hook** at `plugin/hooks/pre_tool_use_git_guard.py`. New file, new `hooks.json` entry with `Bash` matcher (separate from the existing `Edit|Write|MultiEdit|Task` PreToolUse hook — different matcher, different concern domain). Denies `git reset --hard` and `git push --force` / `git push -f`; allows `git push --force-with-lease`, `git reset` without `--hard`, `git commit`, `git tag`, and all other git operations. Deny messages name the blocked command, explain why, and list safer alternatives. Smoke-tested via direct Python invocation (14 cases: 5 deny, 9 allow, all pass). Regex bug caught and fixed pre-ship (`\b` before `--hard` doesn't fire because both the preceding space and the leading `-` are non-word characters).
- **V36 session scope created** (`planning/sessions/V36.md`) — OPEN-QUESTIONS doc-only bundle: TEST-LOG ordering (newest-first), planning's BACKLOG authority (one-line assertion), plan-panel writability research. Two OPEN-QUESTIONS entries fully promoted (graduation path 2, removed); two entries date-tagged with partial-fold-in notes (path 3). PLAN.md V36 row added; V37+ renumbered.
- **Cowork drift cleanup** — 4 line-level edits across 3 files (`plugin/agents/adopt.md`, `BUILD-METHOD.md`, `planning/drafts/claude-cli-headless-feasibility.md`). Remnant references from V23's sweep.

**Decisions taken and why.**

- **New file for the git guard, not an extension of `pre_tool_use.py`.** Existing hook matches `Edit|Write|MultiEdit|Task`; git guard needs `Bash`. Different matcher, different concern domain (destructive-command prevention vs method-doc integrity). A 95-line focused script beats adding branches to an 841-line file.
- **`--no-optional-locks` not recommended.** Web search confirmed it's a `git` flag, not a `claude` CLI argument. Can't be passed as a Claude Code launch flag. Only mitigation for `.git/index.lock` contention is manual `del` — documented as a Windows sub-bullet in the habits line.
- **`/git-discipline` skill deferred.** Adds polish (walking the no-coder through first-time git setup) but isn't load-bearing for V34's safety guard. Can be a small standalone session.
- **Lock-contention reproduction deferred** to future Stop-hook session. V34's hook doesn't perform git ops itself, so measuring retry-logic aggressiveness doesn't shape any V34 deliverable.

**Pivots and surprises.**

- **Regex `\b` doesn't work before `--flags`.** `\b` requires a transition between word and non-word characters; both the preceding space and the leading `-` in `--hard` are non-word characters, so no boundary fires. Caught by automated testing before ship. Would have been a silent pass-through in production.
- **Automated hook testing worked well.** Direct Python invocation via stdin/stdout pipe tested the full hook logic with zero API cost and deterministic results. Validated the approach documented in `BUILD-METHOD.md` → *Hook script direct invocation*. No need for a full `claude --plugin-dir` session for this hook.
- **Context compaction mid-session.** Conversation hit limits and was continued from a summary. All task state and design decisions survived accurately.

**Carried forward.**

- **Stop-hook auto-commit** remains deferred (V34.md explicitly parks it). One researched user who tested hook-driven auto-commits rolled it back. Revisit after Taskflow's first build cycles surface evidence.
- **`.git/index.lock` contention reproduction** deferred to the future Stop-hook session, which will need to measure retry-logic aggressiveness for any git ops the hook performs.
- **`planning/drafts/git-integration-research.md` consumed** and deleted in this commit per drafts/ lifecycle.

---

## V33 — 2026-05-20 — Consumer-side BUILD-LOG, planning/drafts/, and frame-correction sweep

**What shipped.** Three coupled additions to the consumer method's *After every build* phase, all landing in `plugin/agents/after-build.md` → *Work loop* (and mirrored in docs-only `NO-CODE-METHOD.md`).

- **BUILD-LOG.md as 6th spine doc.** New `BUILD-LOG-TEMPLATE.md` (both template locations). `scaffold.py` scaffolds it alongside the other five. After-build writes one entry per build — What shipped / Decisions taken and why / Pivots and surprises / Carried forward. Session identification reads the latest `## <token>` heading (existing mechanism, now always present). CLAUDE-TEMPLATE path block gained the `BUILD-LOG.md` entry. Both DOC-STRUCTURE copies gained a *BUILD-LOG.md structure* section.
- **`planning/drafts/` folder.** Destination-agnostic carryover for substantive chat content not yet doc-ready. `scaffold.py` creates the directory at `/adopt` time. Lifecycle documented in both DOC-STRUCTURE copies (*planning/drafts/ folder* section). Three new Vocabulary terms: *Build log entry*, *Draft*, *Frame-correction sweep*.
- **Frame-correction sweep.** After-build step 6 (new): when a build substantively changes a feature, scan BACKLOG.md planning batches and `[FOLD-IN PENDING]` blocks for old-behaviour references. Flag candidates in chat; silent if none. Scope is BACKLOG only — UX.md drift already caught by planning's drift check 1.
- **Parity sweep caught ~8 files beyond the 11-file plan.** `session_start.py` (`SPINE_FILENAMES`), `pre_tool_use.py` (`WRITABLE_LOGICAL_NAMES`, `SCAFFOLD_NAMES`), `planning.md` (load list), `before-build.md` (load list), `adopt.md` (Case 1/2/3 scaffold lists), `CLAUDE-TEMPLATE.md` (path block, both copies), `BUILD-METHOD.md` (footer-bump list). The plan had said "no changes" to several of these — wrong.

**Decisions taken and why.**

- **Both chat recap and BUILD-LOG entry (not either/or).** Chat recap is the ephemeral in-session announcement; BUILD-LOG entry is the persistent audit trail. Different audiences, different lifecycles — no reason to collapse.
- **Frame-sweep scope: BACKLOG.md only.** UX.md drift is already caught by planning's drift check 1 at next session open. Sweeping UX.md here would duplicate that work and blur ownership.
- **Frame-sweep ownership: after-build (not planning).** Build context is freshest right after the build. Dev-project does it at session-close for the same reason. Consumer-side mirrors that.
- **Drafts as own DOC-STRUCTURE section (not sub-section of Editing surfaces).** Drafts have lifecycle, format, and access rules — enough substance to warrant a standalone section rather than a cramped bullet under Editing surfaces.

**Pivots and surprises.**

- **Context compaction mid-session.** The conversation hit context limits and was continued from a summary. All in-flight work survived — the compaction summary accurately captured the pending `SCAFFOLD_NAMES` edit and the parity sweep state. No work lost.
- **Plan underestimated the blast radius.** The plan listed 11 files; actual edits touched ~19 distinct files (excluding footer bumps). Every new spine doc propagates to: template (×2), scaffold script, hook constants (×2), subagent load lists (×3), CLAUDE-TEMPLATE path block (×2), INVENTORY, Crash course, NO-CODE-METHOD, BUILD-METHOD footer list. Worth remembering for future "add a spine doc" sessions.

**Carried forward.**

- **Smoke test owed.** Plan §5 specifies `claude --plugin-dir` against `~/v33-scratch` — `/adopt` scaffolds BUILD-LOG.md + `planning/drafts/`, then a build batch fires after-build which writes the BUILD-LOG entry and runs the frame sweep. Not done this session.
- **Docs-only NO-CODE-METHOD.md still uses plugin-specific phrasing** (carried from V32). Substance correct, framing wrong for project-agnostic audience. Slot for a future session or a dedicated docs-only rewrite.

---

## V32 — 2026-05-20 — NO-CODE-METHOD.md retired from plugin; two-write architecture established

**What shipped.** The "retirement" reframe (see *Pivots and surprises*) split the canonical method content into two parallel artefact sets: plugin-side (operational) and docs-only (project-agnostic prose).

- **Docs-only set bootstrapped at repo root.** `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md` (new) — the prose-only / no-plugin version of the method, byte-identical to the plugin-side at this V32 commit. `templates/` was already there from earlier; now formally the docs-only template set. `Crash course.md` stays at repo root but is plugin-side audience (per Alex).
- **`plugin/docs/NO-CODE-METHOD.md` retired from plugin runtime.** Subagent bodies stopped reading it at session start. Operating procedures inlined: `planning.md` gained a *Procedure order* section + *How a new feature enters the project* (with the UX-principle-conflict rule from coverage-map §17); `before-build.md` inlined the *Batch-sizing principle* sub-rules; `after-build.md` was already complete inline. `batch-executor.md` kept its in-place inlines; only cross-references redirected.
- **`plugin/hooks/universal-behaviour.md` absorbed the orphans** from the coverage map: §13 main-Claude routing logic (highest-stakes orphan); §5 Rule 1 *Never infer completion*; §6 Prohibited block + *Two exceptions*; §7 flag taxonomy table; §3 response-shape tags glossary; §10 *Editing surfaces*. SessionStart now injects all the cross-cutting rules main Claude needs.
- **`plugin/docs/VOCABULARY.md`** — new file, holds the §4 Vocabulary content (planning batch, build batch, test session, Pass/Fail/Skipped, etc.). Mirrored at repo root for the docs-only set.
- **Cross-reference cleanup, plugin-wide.** Every "see `NO-CODE-METHOD.md` → X" reference in plugin code (subagents, hooks, INVENTORY, templates, the plugin-side DOC-STRUCTURE.md, the slash-command body) redirected to its new home. User-visible deny messages in PreToolUse kept their NO-CODE-METHOD.md references intact — those point at the docs-only spec on GitHub, which the user can read.
- **`BUILD-METHOD.md`** gained a *Two-write rule for canonical docs* section + split the *Footer bumps* list into plugin-side, docs-only-side, and cross-cutting (INVENTORY.md alone). Documents the architecture, the two-write discipline, and the legitimate cross-reference divergence between the two sides.
- **`CLAUDE.md` (dev-project, repo root)** file-inventory rewrite reflecting the two parallel doc sets. Terminology cheat sheet updated — NO-CODE-METHOD.md / DOC-STRUCTURE.md / VOCABULARY.md rows now describe their post-V32 status (not present in consumer-project trees; plugin homes named).
- **`planning/INVENTORY.md`** doc-fates table updated; subagent and bundled-artefacts rows updated to note V32 inline status; `plugin/docs/NO-CODE-METHOD.md` row removed; VOCABULARY.md row added; universal-behaviour.md row added.
- **Frame-correction sweep on `V33.md / V34.md / V35.md`** per BUILD-METHOD step 2. V33 inputs/outputs/risks rewritten to name concrete post-V32 destinations (`plugin/agents/after-build.md` → *Work loop* instead of "wherever V32 distributed those rules"). V34 *Recommended habits* destination clarified to docs-only `NO-CODE-METHOD.md` at repo root. V35 framing of the V32 dependency tightened.
- **Footers V30 → V32** across all method-side files (both plugin-side and docs-only-side — see BUILD-METHOD's new split). `plugin.json` → `0.32.0`; `PLUGIN_METHOD_VERSION` → `32`. V31 was dev-internal-only so footers had stayed at V30; V32's substantive method change makes this the next real bump.
- `planning/drafts/v32-coverage-map.md` consumed at close (deleted in commit).

**Decisions taken and why.**

- **Shape A + repo-root home (not Shape B "trim" or Shape C "pointer").** Coverage map flagged three retirement shapes. Shape A (full retirement, inline everything) won because: (a) Alex's framing made it clear the rules live in the plugin, not in a docs read; (b) trimming-not-retiring would keep the divergence question alive (the OPEN-QUESTIONS entry on subagent rule-loading divergence settles cleanly to "inline" with Shape A); (c) the runtime reads were a belt-and-braces measure that's no longer needed once the inlines are verified.
- **Plugin is the leader; docs-only follows.** Two-write discipline keeps both copies aligned; legitimate divergence is allowed for cross-references (each copy points at its own siblings). The plugin-edits-first-then-docs-only-catches-up rule prevents the docs-only side from drifting toward a different operational model.
- **`VOCABULARY.md` as its own file** vs. lumping into universal-behaviour.md. ~20 entries, frequently cross-referenced (`see Vocabulary → Skipped` from multiple subagents), structurally distinct from universal behavioural rules. Lumping would make universal-behaviour.md a kitchen sink and obscure the rules that ARE behavioural. Cost: one more file in the two-write pair list.

**Pivots and surprises.**

- **Session was a continuation after the previous chat glitched out.** Coverage map at `planning/drafts/v32-coverage-map.md` survived (substantive design work for V32, completed pre-glitch). No implementation work had landed before the glitch. Memory file `project_no_code_method_canonical.md` carried the framing decision (retirement is from plugin only; file lives on as docs-only) into this session, preventing a re-litigation. This is the second time auto-memory has materially saved continuity (first was the Crash course rewrite in V30); worth noting as a positive pattern.
- **V32.md scope file was stale relative to the framing decision.** Read "Retire the file or replace with a one-line pointer" — pre-docs-only framing. Flagged at session open; substantive direction (Shape A + docs-only relocation) carried by memory + Alex's confirmation, not by the scope file. Frame-correction sweep at close updated V33/V34/V35 scope files to use post-V32 references.
- **Cowork mount stale-view issues, twice.** (a) `bash cp` of `templates/CLAUDE-TEMPLATE.md` and `templates/ADDITIONAL-DOC-TEMPLATE.md` from `plugin/templates/` produced truncated copies — file ended mid-sentence at line 24 instead of 28. Recovered via `Write` through the canonical Windows path. (b) `bash tail -n 2` and `bash awk` on long-line files returned truncated output that masked footer presence. Both behaviours documented in memory `reference_cowork_git_mount_phantoms.md` — re-confirmed today. **Going forward,** verify any bash-copied file's integrity via `Read` (Windows path), not via bash inspection.
- **Bash `rm` of `plugin/docs/NO-CODE-METHOD.md` blocked by Windows ACLs.** Predicted by the memory file. Alex to delete via PowerShell `Remove-Item` or Windows Explorer at close.
- **Subagent inline gaps were larger than coverage map suggested.** Coverage map said `planning.md` was "Partial → Covered if read is removed" because the read was a safety net. Audit revealed real procedural gaps the read had been providing: remove-completed-batches, discuss-step, dedupe filter, Suggestions list shape, Discoveries list framing. All lifted into a new *Procedure order* section before the reads dropped. `before-build.md` similarly relied on the read for the three Batch-sizing sub-rules. `after-build.md` was the only one fully complete inline pre-V32.

**Carried forward.**

- **`plugin/docs/NO-CODE-METHOD.md` deletion** owed to Alex via PowerShell `Remove-Item` or Windows Explorer — Cowork bash `rm` returned "Operation not permitted" (Windows ACLs, predicted by memory). Has to happen before the V32 commit.
- **Docs-only `NO-CODE-METHOD.md` still uses plugin-specific phrasing** ("you're reading now; always loaded," "the SessionStart hook," "the PreToolUse hook"). Substance is correct but framing is wrong for the project-agnostic role. Per the coverage-map escape clause, folded forward rather than rewritten this session — the rewrite would be a substantial prose pass dominating session scope. Slot for V33+ or a dedicated docs-only-rewrite session.
- **Smoke test in `~/v32-scratch` owed.** Removing the runtime reads is the V32 risk surface — any inline gap from step 2's lift would surface as a runtime regression. Smoke run validates planning / before-build / after-build still behave per spec against a fixture project.
- **`Recommended habits` orphan (coverage-map §8)** — consciously accepted as no-op. Crash course narrative covers the habits at install time; the rule itself stays only in the docs-only `NO-CODE-METHOD.md`. If V34 (Recommended-habits "tag and push") surfaces a need to promote habits into the plugin, revisit.

---

## V31 — 2026-05-20 — Planning: rescope OPEN-QUESTIONS into V33/V34; V32–V35 numbering shifted

**What shipped.** Planning session over `OPEN-QUESTIONS.md` (foreshadowed in V30's *Carried forward*). Four promotion-ready entries folded into two new sessions; V31's own work claims the v31 tag; everything else shifts by one.

- **Renames.** `planning/sessions/V31.md` (NO-CODE-METHOD.md retirement) → `V32.md`; old `V32.md` (E2E Taskflow test) → `V35.md`. Internal refs in both files updated (titles, commit-tag lines, input dependencies — V18–V31 → V18–V34 in the E2E scope file).
- **New session-scope files.** `planning/sessions/V33.md` — consumer-side audit trail + frame-correction sweep; combines three OPEN-Qs ([[Consumer-side BUILD-LOG.md equivalent]], [[planning/drafts/ pattern for consumer projects]], [[Frame-correction sweep — consumer-method version]]) into one session because all three touch *After every build* and would otherwise sweep the same docs three times. `planning/sessions/V34.md` — consumer-method git workflow; promotes [[Consumer-method git workflow]] with Stop-hook auto-commit explicitly deferred to a later opt-in session. Both scope files note V32 dependency (the *After every build* edits land wherever V32 distributes those rules post-NO-CODE-METHOD-retirement).
- **`planning/PLAN.md`.** Row inserted for V31 (this session). Row inserted for V33 and V34. V32 → V35 shifted. New V36+ row pointing at the five still-parked promotion-ready entries. Count line updated from "15 sessions" to "18 sessions through V35, plus V36+ TBD."
- **`planning/OPEN-QUESTIONS.md`.** Four promoted entries removed (graduation path 2: removal at promotion, not at session ship). Five remaining promotion-ready entries' *Next step* lines retargeted from "V31+ once V30 ships" to "V36+ post-E2E (V35)" — UX.md non-GUI, SoT doc edits with permission, TEST-LOG ordering, TEST-LOG row pruning, "planning" vocabulary collision, MANIFEST.md schema gap. Stale V31 references in three parked entries updated to V35 — Automated testing/CI ("post-V32 E2E test" → "post-V35"), Prose-only rewrite ("V31 (final E2E Taskflow test) ships" → "V35"), AEX-style performance log ("after V31 ships" → "after V35"). Subagent rule-loading-divergence entry's "V26–V31 ship" window extended to "V26–V35 ship (or its post-V32 successor location)" since V32 retires NO-CODE-METHOD.md and that affects what stability the question measures. 13 entries remaining, down from 17.
- **Dev-internal-only session.** No method-version footer bumps; `plugin.json` and `PLUGIN_METHOD_VERSION` unchanged.

**Decisions taken and why.**

- **Re-order rather than append.** Two of the four promoted sessions ship discipline V35's E2E test exercises (consumer BUILD-LOG, frame-sweep, git safety-guard). Landing them after E2E means the test runs without the discipline it'll then validate; landing them before is what makes E2E meaningful. UX.md non-GUI, TEST-LOG order/prune, SoT permission, planning-vocab, and MANIFEST schema all wait for E2E evidence (none get useful signal from a single-user GUI-project test ahead of time).
- **Combine three open questions into V33.** Consumer BUILD-LOG, drafts/ pattern, and frame-correction sweep all touch *After every build*. Three separate sessions = three sweeps of the same docs + three footer-bump cycles. One combined session lets related additions share a smoke test.
- **Stop-hook auto-commit explicitly deferred from V34.** Web-search draft flagged one user who rolled it back at scale ("cost more than they returned"). V34 ships *Recommended habits* line + PreToolUse safety-guard against `git reset --hard` / `git push --force`; auto-commit becomes a later opt-in session once Taskflow's cycles produce evidence.
- **MANIFEST schema gap surfaced honestly rather than silently moved.** Promotable since V25–V26 (its *Next step* trigger fired in V25). Held through V26–V31 because it's a heavy method-level decision (path-field schema + behaviour choice across A/B/C/E options) and earlier sessions consistently had higher-priority work. Calling that out in the entry's revised *Next step* so future-Claude doesn't read "promote V26+" as a fresh decision.

**Pivots and surprises.**

- **Tag-numbering shift mid-discussion.** Initial proposal had V31 staying as NO-CODE-METHOD retirement; Alex approved the table. Then BUILD-METHOD's "one session = one tag" forced this planning session to claim its own v31, pushing everything else by one. Settled inline with a recommend-one + escape-line proposal; she went with the shift. Cost: re-approval on numbers she'd already signed off on. Worth noting because the tension between "what's already approved" and "what the convention requires" is the kind of thing a future planning session could hit again.
- **Nothing else surprised.** The OPEN-Q entries' own *Working notes* sections did most of the scope-design work — this session was assembly, not invention. That's a positive signal about how the entry shape (per BUILD-METHOD → *OPEN-QUESTIONS entry shape*) is doing its job: notes captured at the time of raising prove load-bearing later.

**Carried forward.**

- **Five promotion-ready entries still in OPEN-QUESTIONS for V36+.** UX.md non-GUI adaptation; TEST-LOG ordering + row pruning (paired); SoT doc edits with no-coder permission; "planning" vocabulary collision; MANIFEST.md schema gap. Each becomes its own PLAN.md row + Vxx.md scope file when promoted post-E2E.
- **Eight parked entries unchanged in shape.** Triggers retargeted from V31/V32 to V35 where they referenced E2E; activation conditions otherwise intact.
- **Next session is V32: NO-CODE-METHOD.md retirement** as previously scoped. Scope file already renamed; internal refs already updated.
- **Further Crash course review pass still parked** (carried over from V30). The promised "after the OPEN-Q planning session" trigger from V30's *Carried forward* has now fired — pass can be picked up next time it lands naturally, likely in V32 alongside the retirement work since both touch the same spec docs.

---

## V30 — 2026-05-20 — Method docs relocated into plugin; Crash course rewritten as standalone primer

**What shipped.**

- **`plugin/docs/NO-CODE-METHOD.md`** and **`plugin/docs/DOC-STRUCTURE.md`** — relocated from repo root via PowerShell `git mv` (the bash mount + Drive sync corrupted `.git/index` on first attempt; recovered via PowerShell `git read-tree HEAD`). Subagent bodies (`planning.md`, `before-build.md`, `after-build.md`) updated to read them via `${CLAUDE_PLUGIN_ROOT}/docs/...`. Substitution behaviour verified against Claude Code's plugins-reference docs. `batch-executor.md` and `adopt.md` keep bare-filename citations by design (conversational refs that don't depend on substitution).
- **`Crash course.md`** — fully rewritten as a standalone primer (a first-time reader can install the plugin and use the method without opening NO-CODE-METHOD.md). Install + first session moves up front; new *When you need more* closing pointer; *Why the rules* reframed standalone. *The session shape*'s planning-input paragraph tightened mid-review to remove an implied pre-subagent iteration phase that diverged from the spec — the no-coder's reassurance that planning stays conversational was preserved but folded inside the subagent-runs description. Same section's before-build sentence reworded to drop "user-observable behaviours" (GUI-centric phrasing — see the V30 OPEN-Q on UX.md adaptation for non-GUI projects) in favour of plainer "things that will need testing once the batch ships." *Walkthrough — Taskflow Day 1* → *A first UX entry — Risk accepted in action*'s Risk-accepted example reworded — the previous text ("Users cannot plan around upcoming busy periods or anticipate scheduling conflicts") misrepresented Taskflow's actual approach (calendar integration handles time-bound commitments); the rewrite frames the trade-off correctly as task-load visibility, not time-conflict awareness.
- **`plugin/README.md`** — gains a *Read this first* link to Crash course at its GitHub URL.
- **`plugin/docs/NO-CODE-METHOD.md`** — *Before build* closing prompt reframed defensively. Replaces the old "switch out of plan mode, then run `/build`" line (which implied plan mode was a build-cycle step) with "Prompt me to run `/build` … If I'm in plan mode for any reason, ask me to switch out first — `/build` invokes file edits that plan mode blocks."
- **`BUILD-METHOD.md`** — *OPEN-QUESTIONS entry shape* augmented with a *Graduation paths — four ways an entry leaves* sub-section (full fold-in / own-session promotion / partial fold-in / conscious drop). Cross-refs the session-open scan as trigger mechanism; V22's partial-fold serves as worked example.
- **`templates/CLAUDE-TEMPLATE.md`** + **`plugin/templates/CLAUDE-TEMPLATE.md`** — line 3 rewritten to acknowledge the plugin-bundled location and point humans at the GitHub URL. Other templates' bare-filename refs to `DOC-STRUCTURE.md` / `NO-CODE-METHOD.md` left intact — they resolve cleanly for Claude (subagents already read the spec on entry) and for humans (CLAUDE.md's new wording covers location).
- **`planning/INVENTORY.md`** — Crash course row flipped to "Method-dev repo root / Linked from plugin README"; DOC-STRUCTURE.md row settled at `plugin/docs/DOC-STRUCTURE.md`; NO-CODE-METHOD.md row gained the `plugin/docs/NO-CODE-METHOD.md` path mention for sister-doc symmetry; *Bundled artefacts* section lists both `plugin/docs/` files (Crash course line removed).
- **`planning/sessions/V31.md`** and **`V32.md`** — frame-correction sweep applied. V31 input list updated (V30 relocated *both* docs, not just DOC-STRUCTURE); two success-criteria lines and one open-question line de-frame-corrected (the "project no longer needs NO-CODE-METHOD.md" phrasing assumed a per-project-root frame). V32 input list updated.
- **`planning/OPEN-QUESTIONS.md`** — *Consumer-method git workflow* entry refreshed: web-search returned (Sonnet, this session), full notes committed to `planning/drafts/git-integration-research.md`. Headline findings + four pre-promote action items folded into the entry's *Working notes*. *Next step* dropped the "web-search first" gating; promotion path sharpened to "habit line + `PreToolUse` safety-guard against destructive git commands, with Stop-hook auto-commit deferred to a later opt-in session." **Ten OPEN-Q entries surfaced this session** — five from V30 retrospective (consumer-method git workflow, `planning/drafts/` pattern for consumer projects, consumer-side BUILD-LOG equivalent, frame-correction sweep for consumer projects, automated testing/CI for the method's dev project), five from Crash course review (source-of-truth doc edits with no-coder permission, TEST-LOG ordering, TEST-LOG row pruning, "planning" vocabulary collision with Claude Code's plan mode, UX.md adaptation for non-GUI projects). All parked for V31+ planning sessions per their *Next step* lines.
- **`planning/drafts/git-integration-research.md`** — new. Sonnet web-search response on Claude Code's git handling. Consumed by the V32+ session that promotes the git-workflow OPEN-Q.
- **21 method-version footers bumped V29 → V30**; `plugin.json` → `0.30.0`; `PLUGIN_METHOD_VERSION` → `30`.

**Decisions taken and why.**

- **Bundled doc + sister-doc symmetry (Q1+Q2).** `DOC-STRUCTURE.md` lands as a bundled reference doc, not a skill body — same audience (subagents at session start), same access pattern (read-on-entry by name). Scope expanded to relocate NO-CODE-METHOD.md alongside so the symmetry holds from the start. Skill model is user/intent-facing, doesn't fit a structural-spec reference.
- **Full Crash course rewrite, not a surgical pass (Q2).** The standalone-primer success criterion (use the method without `NO-CODE-METHOD.md`) reads strongly enough to require it. Structural reorder, not just polish.
- **Crash course stays at repo root, not in `plugin/docs/` (Q3).** Audience is humans; plugin runtime doesn't consume it; web-shareable URL stays clean. Symmetry-break with the spec docs is intentional and tracks the different audience.

**Pivots and surprises.**

- **Subagent read-spec-on-entry was silently failing pre-V30.** Discovered while scoping the relocation's text-replacement work — plugin behaviour relied on inline rules + SessionStart's universal-behaviour injection alone; the "Read NO-CODE-METHOD.md → *During planning*" line in subagent bodies wasn't actually firing because subagents see `CLAUDE_PLUGIN_ROOT` only as a substitutable token in their body. Resolved via `${CLAUDE_PLUGIN_ROOT}/docs/...` substitution (Claude Code substitutes this at agent-definition time, per plugins-reference docs). Real correctness gain — three subagents now actually read their spec at session start. The relocation incidentally surfaced this; without it, the silent failure would have persisted.
- **Mid-Phase-2 git index corruption** during the first `git mv` attempt from the Cowork bash mount + Drive sync. Recovered via PowerShell `git read-tree HEAD`. Reaffirms: git operations on this folder from PowerShell only.
- **Plan-mode-vs-build-cycle ambiguity.** Spec line about switching out of plan mode before `/build` was misleading — plan mode isn't used by any build-cycle phase. Tightened to defensive framing (only matters *if* the user is in plan mode for unrelated reasons).
- **The standalone-primer ambition surfaced ten OPEN-Q entries** (named in *What shipped*) — substantive method-level concerns the rewrite forced into the open. Largest blind-spots: the method has no consumer-side audit trail equivalent of `BUILD-LOG.md`; consumer projects have no recommended git workflow or `drafts/` pattern; "user-observable behaviours" assumes a GUI everywhere; "planning" collides with Claude Code's plan mode; the dev project's "no automated CI" line deserves a deliberate revisit as the plugin surface grows.
- **Session split across two Cowork conversations.** Phase 4 hit length limits mid-Crash-course review; continuation routed via `planning/drafts/V30-handoff.md`. Session 2 closed Phase 4's review (one substantive item — *The session shape*'s planning-input paragraph), ran Phase 5 (INVENTORY + templates + frame-correction sweep on V31/V32 + git-research fold-in), ran Phase 6 (21 footer bumps + two version trackers), closes out Phase 7 now.

**Carried forward.**

- **Ten OPEN-QUESTIONS entries newly surfaced**, all parked for V31+ sessions per their *Next step* lines.
- **Git workflow research at `planning/drafts/git-integration-research.md`.** Consumed by the V32+ session that promotes the *Consumer-method git workflow* OPEN-Q.
- **Further Crash course review pass parked.** Alex stopped mid-read after surfacing the verification-burden, Section 4 planning-input paragraph, and Risk-accepted example items. Next pass scheduled after the OPEN-QUESTIONS planning session described below — the planning session is likely to surface more Crash course implications worth folding in together.
- **Next session is a planning session over `OPEN-QUESTIONS.md`** (not V31 directly), batching the ten newly-surfaced entries into upcoming `Vxx.md` scope files and updating `PLAN.md`. Decision driven by the volume of OPEN-Qs from V30 — going straight into V31 (NO-CODE-METHOD.md retirement) without sequencing the rest first would lose visibility on which entries pair, which promote alone, and what order earns the test ground first.
- **V31 (`NO-CODE-METHOD.md` retirement / cleanup) and V32 (E2E Taskflow test)** — planned sessions, scope files de-frame-corrected this session and ready to load whenever the OPEN-Q planning session decides their ordering relative to the new entries.

---

## V29 — 2026-05-19 — Safety net (SessionStart advisory + PreToolUse enforcement) + unified `/adopt`

**What shipped.** The two-hook safety net plus the `/adopt` skill-command, unifying `/new-project` + `/init-project` (V19) + `/migrate` into one command branching across 5 folder states. Smoke-tested live across 5 fixture folders at `C:\Users\Alex\v29-fixtures\`; see TEST-LOG #071–089.

- **`plugin/hooks/session_start.py`** — V29 unadopted-folder detection (Q2 rule: build-manifest / recognized source-dir / foreign CLAUDE.md / >5 files), emits `systemMessage` advisory on unadopted-with-work folders pointing at `/adopt`; silent on empty / adopted / opted-out (`.no-code-method-skip` marker). Wording narrowed mid-session from "Tool calls will be denied" to "Edit/Write/MultiEdit calls will be denied" per smoke-test finding (TEST-LOG #077).
- **`plugin/hooks/pre_tool_use.py`** — V29 unadopted-folder gate denies Edit/Write/MultiEdit + Task→method-subagent from main Claude on unadopted folders; `/adopt`'s own calls pass through (V22/V27 invoker discrimination). Self-clears once method footer or `.no-code-method-skip` marker is written.
- **`plugin/agents/adopt.md`** — new subagent, five-case dialogue (empty / existing code, no docs / existing code, foreign docs / already method-managed / opted out). Case 4 runs a *detect template state* first-action (reads `user_v` from CLAUDE.md, `plugin_v` from `PLUGIN_METHOD_VERSION`), then opens with versions-match or version-mismatch dialogue. Option-1 walkthrough explicitly classifies CLAUDE.md/BACKLOG/MANIFEST/TEST-LOG as writable and UX.md (+ additional SoT) as locked — clarification added mid-session after smoke test caught the subagent over-locking (TEST-LOG #083).
- **`plugin/skills/adopt/SKILL.md`** + **`plugin/skills/adopt/scripts/scaffold.py`** — entry point + `detect-case`/`check`/`write` script.
- **`plugin/README.md`** — new. One line directing users to `/plugins` after install. Originally `/plugin` — corrected mid-session after smoke test caught the actual command name.
- **`Crash course.md`** — new *The safety net — installing on a folder that isn't empty* section at narrative altitude; new-project-route and migration-route language replaced with `/adopt`.
- **`NO-CODE-METHOD.md`** — adoption-state Vocabulary entries (*adopted* / *unadopted folder*); *Detect unadopted folder* rule added at *At session start*; two-hook architecture documented.
- **`BUILD-METHOD.md`** — *Session close* extended from 8 steps to 9; new step 2 *Frame-correction sweep* (audit `planning/sessions/Vxx.md` for stale references when this session corrected a load-bearing frame). Footer-bumps list adds `adopt.md`.
- **20 footers bumped V27 → V29** (NO-CODE-METHOD, DOC-STRUCTURE, Crash course, 6 root templates, 6 plugin templates, INVENTORY, 4 existing subagents). `adopt.md` gains its first V29 footer. `plugin.json` → 0.29.0.
- **`planning/OPEN-QUESTIONS.md`** — *Frame-update sweep rule* (resolved option A) and *Cross-version template reconciliation* (worker half shipped) removed.
- **`TEST-LOG.md`** — rows #071–089. One Fail (#083), one Skipped (#089); fixes for both applied this commit, retests owed.
- **Memory file `reference_userpromptsubmit_plugin_bug.md`** — updated with #10225 → #12151 progression, V29 confirmation that the bug still bites, and the cumulative impact on V18's and V29's architectural pivots.

**Decisions taken and why.**

- **Frame-correction sweep rule: option A (audit step in BUILD-METHOD), not B (shorten planning horizon).** A is cheap to add and cheap to execute when triggered; B permanently costs the roadmap-visibility benefit (V28's prequel restructure depended on scope-ahead files). Asymmetric trade-off favours A; B is the right escalation only if A's "did this session do a frame correction?" trigger keeps misfiring. The audit ran against V30/V31/V32 immediately after the rule landed — clean.
- **Cross-version-template-reconciliation worker half lives in `/adopt` case 4, not a separate skill-command.** Single user-facing entry point; avoids inventing a `/refresh` command. Cost: the version-mismatch isn't user-visible at session start because the V21 tripwire emits to `additionalContext`, not `systemMessage` — only surfaces when `/adopt` runs.
- **Plugin README, not statusline, for "is the plugin loaded" UX.** `${CLAUDE_PLUGIN_ROOT}` doesn't expand in user `settings.json`; absolute paths with cache-hashes are too fragile for non-developer consumers across plugin updates. One README line pointing at `/plugins` is the working substitute.

**Pivots and surprises.**

- **PreToolUse gate is Edit/Write/MultiEdit only — Bash bypasses by design.** Discovered when Claude creatively wrote `.no-code-method-skip` via PowerShell `New-Item` during case-2 smoke. Threat model is accidental edits via the Edit family, not creative shell circumvention — gate is correctly scoped, but the advisory wording overstated the protection. Wording fix landed same commit (TEST-LOG #077).
- **`/adopt` case-4 subagent over-locked the spine docs during refresh.** Treated BACKLOG/MANIFEST/TEST-LOG as locked source-of-truth (they're writable per spec); only CLAUDE.md got bumped. The subagent even surfaced its own contradiction in the recap. Adopt.md case-4 option-1 section rewritten same commit with explicit writable/locked classification and a "do NOT route writable through fold-in pending" warning. Retest owed (TEST-LOG #083).
- **Case-4 pre-edit walkthrough text either skipped or scrolled past — couldn't determine which.** My adopt.md edit prescribed surfacing a writable/locked plan before any Edit; in the smoke run the Edit diff appeared with no walkthrough visible above it. Worth a `ctrl+o` transcript dive or a re-run (TEST-LOG #089).
- **V21 SessionStart tripwire isn't user-visible.** Likely emits to `additionalContext` (Claude-side) rather than `systemMessage` (terminal-visible). Subagent correctly adapted its case-4 opener ("may have flagged" rather than "did flag") — adaptive, not buggy. Code read pending if user-visible mismatch advisory is wanted.

**Carried forward.**

- TEST-LOG #083 retest (case-4 refresh writable/locked classification after adopt.md fix) — slot into next plugin-touching session.
- TEST-LOG #089 retest (case-4 walkthrough text visibility) — needs `ctrl+o` transcript dive or fresh smoke run with explicit observation of subagent output before the first Edit.
- `uploads/sessionstart-hook-research.md` + `uploads/issue-10225-status.md` referenced in V29.md but never committed to `planning/drafts/` — same failure mode as V20→V26 *Sonnet draft* incident. Per `BUILD-METHOD.md` → *Drafts in flight*. Sibling-bug detail on `UserPromptSubmit`-in-plugins is lost; flagged in memory file.
- V21 SessionStart tripwire user-visibility (`additionalContext` vs `systemMessage`) — code read pending before deciding whether to surface mismatch user-visibly at session start.

---

## V28 — 2026-05-18 — V27 fix sweep: test-confirmation gate becomes functional

**What shipped.** Three V27 bugs found in same-day Windows smoke testing, all fixed and live-tested end-to-end.

- `plugin/hooks/pre_tool_use.py` — `WRITABLE_LOGICAL_NAMES` extended with `"TEST-LOG.md"` (the one-line fix that unblocks everything else). Check (a) docstring names TEST-LOG.md as a spine doc explicitly. After-build's `Write(TEST-LOG.md)` now succeeds; the V27 gate has rows to gate on. Duplicated helpers extracted (see next item) — file shrinks ~150 lines.
- `plugin/scripts/project_state.py` — new shared module (the V27 BUILD-LOG-named co-fix). Holds the helpers previously duplicated in `pre_tool_use.py` and `stop.py` (`safe_read_text`, `extract_path_block`, `resolve_path_block_entry`, `run_parser`, `parse_test_log_rows`, `is_row_confirmed`, `identify_previous_session`) plus new `get_unconfirmed_previous_session_rows` and `is_test_session_open` extracted from `check_test_confirmation_gate`.
- `plugin/hooks/stop.py` — imports from `project_state`. New V28 check: `if is_test_session_open(project_root): return emit_silent()` before `run_parser` — defers the batch-executor redirect when previous-session rows are unconfirmed. Docstring rewritten for four outcomes (was three).
- `planning/sessions/V28.md` (this session's scope) with V28→V29→V30→V31→V32 renumbering of pre-existing scope files (V28-prequel restructure — `/adopt` moves from V28.md to V29.md, etc.).
- `planning/OPEN-QUESTIONS.md` — V27 WRITABLE_LOGICAL_NAMES + Stop-hook-vs-tripwire entries removed (both resolved this session).
- `planning/PLAN.md` — V28 row replaced with the fix sweep. Walkthrough-mode-for-non-UI-testing (PLAN.md's prior V28) dropped: never had a matching `sessions/V28.md`, V27's after-build "What to test" covers the use case at narrative altitude.
- `TEST-LOG.md` — V28 section with rows #064–070. Implicitly flips #059 (AB1) and #060 (AB3) to Pass via the after-build flow; explicitly retests #057 (P1) post-refactor.

Smoke-tested live in `claude --plugin-dir` against a freshly rebuilt `v27-smoke-fixtures/g4` (V27 fixture was empty — rebuilt 7 files via the Write tool). Two-run sequence: after-build → row opened + MANIFEST update + recap; `/exit` + restart → SessionStart tripwire → planning read-back → "Pass" → test session closed + drift checks clean. All rows Pass; see TEST-LOG #064–070.

**Method-version footers NOT bumped this session.** V28 restores V27's *intended* behaviour — consumers reading the V27 footer get what V27 claimed to ship. Bumping would over-signal a structural change for a bug-fix sweep. (V28.md's open question on this resolved deliberately to no-bump.)

**Decisions taken and why.**

- **V28-prequel restructure over expanding V28's `/adopt` scope.** V27's bugs made the gate inert; shipping `/adopt`'s safety net on top of inert machinery would have buried the foundation issue. Renamed pre-existing scope files (V28→V29→V30→V31→V32) and inserted a new V28 for the fix sweep. Each session keeps one focus.
- **Shared helpers module: `plugin/scripts/project_state.py`.** Considered `shared_state.py` (vague), `test_log.py` (too narrow), `plugin/lib/state.py` (new directory). `project_state.py` describes what's inside (path-block reads, BACKLOG parser invocation, TEST-LOG parsing, BUILD-LOG session-narrowing). `plugin/scripts/` is the existing neighbour for `parse_backlog.py`; hooks add scripts/ to sys.path on import. No new directory needed.
- **Stop hook defers via silent exit, not redirect-to-planning.** Two viable shapes. Silent exit relies on the SessionStart tripwire (already shipped + confirmed working in V27 #056) to do the routing; redirect-to-planning duplicates intent. Critically, a redirect-to-planning during planning's read-back-turn-end would re-invoke planning and re-ask the same question — worse UX than the bug we're fixing.
- **Walkthrough-mode-for-non-UI-testing dropped, not deferred.** PLAN.md row never had a matching `sessions/V28.md`. V27's after-build recap already names "What to test" with one bullet per user-observable behaviour — at narrative altitude, the walkthrough need is covered. If a structured step-by-step format is missed in practice, it'll surface as an OPEN-QUESTIONS entry naturally.

**Pivots and surprises.**

- **Cowork parallel-session corruption hit at session open.** Working tree showed hundreds of spurious modifications (Archive folders, every method-side doc, both V30.md and V31.md scope files) plus a phantom `.git/index.lock` that bash couldn't delete. Recovery: Alex deleted the lock via Windows Explorer, `git reset --hard HEAD` in PowerShell restored the V27 commit state. All subsequent git operations went through PowerShell (file edits stayed in Cowork via Read/Edit/Write — those use the canonical Windows path).
- **V27 g4 fixture was empty.** Initial premise "fixture intact" was wrong; `ls` showed only `.` and `..`. Cause unknown — wasn't V27, `git reset` (fixture sits outside the git repo), or Alex's doc compaction (which she'd confirmed didn't touch this folder). Rebuilt 7 files (CLAUDE.md, UX.md, BACKLOG.md with fully-ticked batch, MANIFEST.md, TEST-LOG.md, BUILD-LOG.md, index.html) via Write tool in mtime-sensitive order so `BACKLOG.mtime > TEST-LOG.mtime` and the Stop hook's after-build trigger fired correctly.
- **Stop-hook V28 fix not uniquely distinguished from natural fallthrough in the live test.** Fixture batch was fully ticked, so `run_parser` would have returned empty even without V28's check — both paths yield silent exit. V28's check definitely fired (`is_test_session_open` returned True given the unconfirmed row), but the bug-trigger scenario (unticked batch + unconfirmed rows simultaneously) wasn't replicated. The one-line fix is mechanically straightforward; TEST-LOG #069 records the caveat. Uniquely-V28 verification owed if doubt arises (direct hook-script test).
- **Compacted planning docs landed with `(1)` suffixes.** Windows save-as artifact from Alex's mid-session doc compaction. `OPEN-QUESTIONS (1).md`, `INVENTORY (1).md`, `OPUS-FEASIBILITY-PROMPT (1).md`, `claude-code-plugin-feasibility-response-terse.md` — renamed back to canonical names in PowerShell.

- **Mid-session compaction pass folded into V28's commit.** While Claude worked on the code, Alex compacted the language in `BUILD-METHOD.md`, `Crash course.md`, `DOC-STRUCTURE.md`, `NO-CODE-METHOD.md`, `README.md`, and the four `planning/` docs (`INVENTORY.md`, `OPEN-QUESTIONS.md`, `OPUS-FEASIBILITY-PROMPT.md`, `claude-code-plugin-feasibility-response.md`). Language tightening only — no meaning, rules, paths, file names, or decisions changed. Folded into V28's commit as the natural session boundary; a separate compaction commit would have added churn without value.

**Carried forward.**

- **V27 Skipped TEST-LOG rows #061 (P2), #062 (L1), #063 (L2)** remain Skipped — each needs a narrower fixture (multiple unconfirmed rows for P2's push-back-on-bulk-confirmations; a planning session writing `[Requested]`/`[Suggested]` labels on BACKLOG.md change-list bullets for L1; a halt-C verification-burden split in before-build for L2). Slot into a future session if regression-risk warrants direct verification; otherwise let them retest opportunistically in real Taskflow work.
- **Stop-hook V28 unique-verification** (direct hook-script test against a fixture with unticked batch + unconfirmed rows simultaneous). Cheap; not blocking V28's ship.
- **PLAN.md ↔ scope-file numbering convention** to enforce going forward — drift caught at session-open this time (PLAN.md V28 named walkthrough-mode, V28.md held `/adopt`).

---

## V27 — 2026-05-17 — After-build subagent + test-confirmation gate hook + SessionStart TEST-LOG tripwire + [Requested]/[Suggested] labels in BACKLOG.md

**What shipped.** The V26 test-confirmation gate prose, now wired end-to-end.

- `plugin/agents/after-build.md` — new subagent owning *After every build*: silent MANIFEST update (Q2), recap with `[Requested]`/`[Suggested]` labels read from BACKLOG.md (Q3), test-session-open by appending blank-Status rows to TEST-LOG.md, prompts to refresh-test-and-return. Idempotent — exits with a brief note if TEST-LOG rows for the current session already exist (covers Stop-hook re-fires).
- `plugin/agents/batch-executor.md` — V25's *After every build* responsibilities stripped. Turn now ends with a brief completion note; Stop hook routes to after-build from there.
- `plugin/agents/planning.md` — two additions: per-row read-back of pending TEST-LOG rows as first sub-step of *During planning* (Rule 2, push-back-on-bulk-confirmations + Skipped-requires-reason); inline-label-writing on every change-list bullet (`- [Requested] Fix drag-to-postpone overshoot`).
- `plugin/agents/before-build.md` — label-preservation rule for halt-C splits: labels travel with their items; no re-classifying to `[Suggested]`.
- `plugin/hooks/pre_tool_use.py` — gained check (f): test-confirmation gate on Task → batch-executor. `hooks.json` PreToolUse matcher extended from `Edit|Write|MultiEdit` to `...|Task`; script dispatches on `tool_name`. Reads TEST-LOG, identifies previous batch's session from BUILD-LOG (path-block → project-root → strict fallback when BUILD-LOG missing OR unparseable — per Q4, the distinction is named in the deny message).
- `plugin/hooks/session_start.py` — TEST-LOG tripwire (Q5): when previous-batch rows have `Confirmed Explicitly: No`, `additionalContext` injects a routing override directing main Claude to planning regardless of opener, with row IDs and Test Descriptions inline. `SPINE_FILENAMES` extended for `TEST-LOG.md`; `PLUGIN_METHOD_VERSION` bumped to 27; comment rewritten for V20+ session-tag/method-version decoupling.
- `plugin/hooks/stop.py` — after-build routing path: when parser returns no top unticked batch but Build batches has a `- [x]` bullet, compare BACKLOG.mtime to TEST-LOG.mtime. If BACKLOG newer, redirect to after-build; otherwise silent.
- `plugin/commands/build.md` — updated for the batch-executor-completion-note vs. after-build-recap split.
- DOC-STRUCTURE.md → *Build batches* — new sub-section *Change list — `[Requested]`/`[Suggested]` labels*: the inline-prefix shape, planning/before-build/after-build chain, why labels attach to changes-not-files.
- NO-CODE-METHOD.md — new *Handoff to after-build* paragraph in *At session start* (also tightened batch-executor handoff to say "completion note"); *During planning* labels rule extended with BACKLOG.md-inline persistence + DOC-STRUCTURE cross-reference.
- Crash course.md — *After build* paragraph in *The session shape* attributes recap to after-build with labels-read-off-BACKLOG; *Four disciplines* test-confirmation-gate paragraph updated to describe both hooks.
- INVENTORY.md — full sweep: SessionStart gains TEST-LOG tripwire; PreToolUse (f) promoted from spec to Shipped V27; Stop hook gains after-build routing; planning, before-build, batch-executor, after-build entries updated; stale "NO-CODE-METHOD.md retired in V27" entry corrected (prose file stays).
- BACKLOG-TEMPLATE.md (×2) — examples show `[Requested]`/`[Suggested]` labels.
- BUILD-METHOD.md — *Footer bumps* list adds `after-build.md`.
- Version 26 → 27 across 19 files. `plugin.json` 0.26.0 → 0.27.0.
- Three V26 carry-forwards (SPINE_FILENAMES, PLUGIN_METHOD_VERSION comment, pre_tool_use.py docstring count) absorbed.

**No smoke tests run this session** — Windows integration via `claude --plugin-dir` owed to Alex post-commit. ~13 distinct checks the V27 design implies (5 around the gate, 3 after-build, 2 planning extension, 2 labels, 1 DOC-STRUCTURE) get logged to TEST-LOG when run.

**Decisions taken and why.**

- **Q3 placement correction: labels live on change-list items, not Files: sub-section.** V27.md's scope said "small label addition in *Files: sub-section* item shape" — pushed back at design-lock as a category error. `[Requested]`/`[Suggested]` describes the provenance of a *change*, not a file: one change touches many files; one file absorbs many changes. Files-level labels would force an arbitrary call when `[Requested]` and `[Suggested]` changes touch the same file. Moved up to change-list level; DOC-STRUCTURE got an explicit sub-section.

- **Mid-session scope expansion: fold the label work into V27 rather than a follow-up.** Q3's resolution implied three small touches beyond after-build (DOC-STRUCTURE, planning label-write, before-build label-preserve). Considered V27a/V27b split. Folded in: those files were already in scope for other reasons, so additional edits cost less than reopening them, and shipping after-build without labels would have meant a dead-code "fallback for missing labels" branch covering a state that should never exist.

- **Scope discovery: batch-executor must shed *After every build*.** V27.md listed after-build as a new subagent but didn't note that batch-executor's V25-era completion path *also* does MANIFEST + recap + prompts. Surfaced while designing after-build's prompt — leaving both would mean duplicate work. Added the scope-reduction edit.

- **Stop hook "after-build pending" heuristic: BACKLOG.mtime vs. TEST-LOG.mtime.** Considered state file, session-tag comparison, "no rows for today" check — each had same-day second-batch failure modes. Mtime comparison is simple, robust to same-day (planning advances BACKLOG when removing the completed batch; second batch advances it again; TEST-LOG stays at first batch's after-build write — BACKLOG > TEST-LOG when second batch completes), and lenient on stat failures.

- **TEST-LOG tripwire as `additionalContext` routing override, not just a status flag.** SessionStart's state summary *informs* main Claude's routing; the tripwire *overrides* it — "regardless of opener, spawn planning with this prompt." Necessary because a feature-request opener while pending rows exist would otherwise route to planning-as-feature-request, not read-back-first. Carries row IDs and Test Descriptions so the subagent can open with a specific row immediately.

**Pivots and surprises.**

- **Stale "NO-CODE-METHOD.md retired in V27" in INVENTORY.** Aspirational note from earlier sessions, not actual V27 scope. Updated: NO-CODE-METHOD.md is source-of-truth prose; subagents read it via read-spec-on-entry.
- **batch-executor's "Flags surfaced in your response" section needed restructuring.** Originally assumed batch-executor produces the recap. Post-V27 it doesn't, so flags need a different surface: red flags written to BACKLOG.md's Red flags section (where after-build picks them up); out-of-scope improvements need to be prominent in batch-executor's in-turn output (chat-only signal after-build can't see).
- **Crash course's "A hook is the load-bearing gate"** was aspirational at V26 (hook not yet shipped). True with V27. Tightened to name both hooks.

**Carried forward.**

- **Smoke testing in `claude --plugin-dir` on Windows** — Alex runs the 13-check sweep post-commit.
- **`planning/sessions/V27.md`** deleted in this commit per transient lifecycle.
- **OPEN-QUESTIONS.md entries** — none added; no existing entries named V27 as fold-in target.
- **Helper-code duplication across `pre_tool_use.py` and `session_start.py`.** Both carry near-identical `parse_test_log_rows`, `is_row_confirmed`, and BUILD-LOG identification logic. Extract to a shared module (same pattern as `parse_backlog.py`). Not pursued — duplication is mechanical, refactor deserves its own session. → future packaging/refactor session.
- **Q3 correction takeaway** — V27.md's category error wouldn't have been caught without the design-lock walk. Worth keeping the design-lock-first rhythm where the scope file calls a specific structural location.

---

## V26 — 2026-05-17 — TEST-LOG.md mechanism + Drafts in flight convention + V25 carry-over bugfixes

**What shipped.** New consumer-side TEST-LOG.md doc class (8 columns: # / Date / Session / Component / Test Description / Status / Confirmed Explicitly / User Notes; phase-based pruning), with templates in both `templates/` and `plugin/templates/`, and structural spec in DOC-STRUCTURE.md.

Five protocol rules placed across NO-CODE-METHOD.md phases:
- Rule 1 (Never infer completion) → *Required of Claude*
- Rule 2 (test-session-close read-back) → first sub-step of *During planning*
- Rule 3 (No new build until test session closed, hybrid hook+subagent) → *Prohibited of Claude*
- Rule 4 (Pass/Fail/Skipped definitions) → *Vocabulary*
- Rule 5 (Retest after change, judgement + reasoning trail) → fourth drift check in *During planning*

Phase edits: *After every build* gains test-session-open step; *During planning* gains test-session-close read-back. CLAUDE-TEMPLATE.md (×2) gains TEST-LOG.md in the JSON path block; scaffold.py extended for fifth spine template. Crash course updated (TEST-LOG bullet in *The files*; *Three disciplines* → *Four*). V27.md scope reframed into 3 components plus main-Claude session-open TEST-LOG tripwire.

**Three V25 carry-over bugfixes** absorbed: parse_backlog.py placeholder detection (#041); BACKLOG-TEMPLATE.md de-collision in both copies (#042); before-build.md parser invocation fix (#044). Sweep bonus: `plugin/commands/build.md` had the same parser-path bug — fixed inline.

**Session-open recovery:** dev-side `CLAUDE.md` (No-code-method project root, not part of this commit) gained *Vxx.md inputs must be in the repo* session-open scan rule; BUILD-METHOD.md gained *Drafts in flight* under *Planning artefacts* (close-time prevention); `planning/drafts/` folder created with V26 as inaugural example via `planning/drafts/test-log-mechanism.md` (consumed and deleted at session close).

Doc-code parity audit: 17 edits across 8 files closing gaps from TEST-LOG additions (doc-listing updated in NO-CODE-METHOD + Crash course; "three drift checks" → four; INVENTORY after-build entry rewritten for V27 revival; INVENTORY PreToolUse gains (f); pre-existing "5 templates" off-by-one in INVENTORY + SKILL.md fixed). Footer bumps V25→V26 across 21 files; BUILD-METHOD's *Footer bumps* list extended for the two new TEST-LOG-TEMPLATE files. No smoke tests — V26 is doc-only on the gate; real test runs when V27 ships.

**Decisions taken and why.**

- **Rule 2 relocation, mid-session.** V26.md put Rule 2 inside *After every build*. Mid-session realisation: *After every build* can't span the testing window — the user tests between sessions, after `/clear`. Relocated to first sub-step of *During planning* where test outcomes actually arrive. *After every build* keeps the open step; close happens next planning. Reshapes V27: after-build owns open, planning owns close, hook fires between.

- **Hybrid enforcement of Rule 3.** Pure subagent hits the ~30% drift rate (Crash course → Caveats). Pure hook is hostile without a walk-through. Hybrid: hook is the load-bearing gate (PreToolUse on Task → batch-executor); planning's first sub-step is the UX. Hook fallback when no BUILD-LOG: "any unconfirmed row blocks" — strict but safe.

- **Q2 punted to Claude's judgement + reasoning trail.** Rule 5's "substantially changed" could be mechanical (line threshold) or judgemental. Mechanical needs the MANIFEST schema extension parked in OPEN-QUESTIONS. Judgemental keeps V26 scoped — and the reasoning trail makes the call auditable. Real builds will force a schema decision later if needed.

- **Drafts in flight convention added mid-session as recovery.** V26.md cited "the Sonnet draft produced in V20 planning" as input; nothing in the repo, nothing on Alex's machine. Confirmed via prompt-to-previous-session that the draft was never committed. Root cause: scope files wrote "Alex has the file locally" without an integrity check. Fix: `planning/drafts/<topic>.md` (committed when "good enough to walk away from"; deleted in the consuming commit) + CLAUDE.md session-open scan rule (halt on out-of-repo references in `Vxx.md` *Inputs*). V26 itself is the inaugural example.

**Pivots and surprises.**

- **V20→V26 "lives locally" failure as session-opener.** Above. Convention written into BUILD-METHOD with the V20→V26 case as a worked example.
- **`/build` slash-command parser-path bug.** OPEN-QUESTIONS noted `/build` did "correctly" handle the parser; that was about BACKLOG.md path resolution, but the script path itself (`python plugin/scripts/parse_backlog.py`) was wrong (project-relative; plugin isn't in the project tree). Caught by the V25 carry-over sweep; fixed inline.
- **Pre-existing "5 templates" off-by-one.** INVENTORY and SKILL.md both said "5 templates" with 4 listed since at least V19. V26's TEST-LOG makes the count actually 5 — coincidental fix.
- **Parity audit surfaced more drift than expected** — 17 edits, 8 files. Pattern worth keeping: when a new doc class lands, sweep doc-listing prose + count-mentions across NO-CODE-METHOD, Crash course, INVENTORY, README, and subagent bodies.

**Carried forward.**

- **`SPINE_FILENAMES` in `session_start.py`** still lists three docs; should include TEST-LOG for detection consistency. Not a runtime bug. → V27.
- **`PLUGIN_METHOD_VERSION` comment** says "Bumped each session" — outdated since V20+ decoupling. → V27.
- **`pre_tool_use.py:5` docstring** says "Runs three checks" — INVENTORY lists 5 (a–e); V27 adds (f). → V27.
- **Three V25 carry-over OPEN-QUESTIONS entries** absorbed and resolved; removed from OPEN-QUESTIONS.md.
- **`planning/sessions/V26.md`** + **`planning/drafts/test-log-mechanism.md`** deleted per their lifecycles.

---

## V25 — 2026-05-17 — Build orchestration core: Stop hook + batch-executor + before-build + slash commands + spec rewrites

**What shipped.** The build orchestration core — two main motivating examples for the plugin.

- `plugin/scripts/parse_backlog.py` — new shared parser. Walks BACKLOG.md, finds top unticked build batch, emits JSON payload (heading, change_list, Files: with tick state, Serves lines). Lenient on malformed input (`{}` + exit 0). Three call sites: Stop hook redirect reason; `/build` manual invocation; PreToolUse edit-time Files: lookup.
- `plugin/hooks/stop.py` — build sequencer. After batch-executor finishes, parses BACKLOG, finds next batch, returns `{"decision": "block", "reason": "<payload>"}` redirecting into the next batch-executor. Respects `stop_hook_active` — one redirect per user turn (D1's explicit user gating).
- `plugin/hooks/pre_tool_use.py` — (c) batch file-list boundary: parses BACKLOG at edit-time, blocks Edit/Write/MultiEdit on any file not on the top batch's Files: list. Originally-scoped (d) MANIFEST/UX read-before-edit deferred — the MANIFEST.md path-mapping schema gap blocks it (logged in OPEN-QUESTIONS).
- `plugin/agents/batch-executor.md` — build-time subagent. Receives JSON via invocation prompt, reads unticked files in Files: order, makes changes, ticks BACKLOG per-file (partial-completion-safe), produces recap with `[Requested]`/`[Suggested]`/`[Prerequisite, not in plan]`/`[Re-batch, not in plan]` labels. Halt-and-confirm protocols cover the two exceptions under *Prohibited of Claude* (prerequisite carve-out, re-batching carve-out). Rules inlined — intentional divergence from planning.md's read-spec-on-entry.
- `plugin/agents/before-build.md` — pre-build subagent. Validates the top batch (parser parses; Serves UX.md names resolve), enumerates Files: into BACKLOG, estimates verification burden, halts-and-confirms if Batch-sizing requires a split. Rules read at runtime from NO-CODE-METHOD → *Before build*.
- `plugin/commands/before-build.md` and `plugin/commands/build.md` — first two slash-commands in the newer commands-directory pattern (`description:` + `allowed-tools:` frontmatter + prose body). `/before-build` spawns before-build via Task; `/build` reads path block, runs parser, embeds payload into batch-executor invocation, handles empty-backlog.

NO-CODE-METHOD.md substantive work: *Before build* rewritten from 8 chat-mediated steps to 8 subagent-aware (validate → enumerate Files: → review → verification burden → Batch-sizing → conflict flags → switch out of plan mode + `/build`); *After every build* rewritten from 5 to 5 with explicit carve-out-label + flag-taxonomy refs; *Batch-sizing principle* sub-section added (split-when-test-list-long, bundle-no-behaviour, never-fragment-arbitrarily); *Pre-build verification estimate* added to *Before build* step 4; *Mid-build re-batching carve-out* added to *Prohibited → Two exceptions*; four new Vocabulary entries (Files: sub-section, Batch-sizing principle, Pre-build verification estimate, Halt-and-confirm protocol); *At session start* gained two new handoff paragraphs (Handoff to before-build, Handoff to batch-executor) paralleling planning. DOC-STRUCTURE.md gained *Files: sub-section* spec; *Build batches* "unfinished portion" sentence tightened to reference tick state. Crash course got three paragraph rewrites in *The session shape*. Both BACKLOG-TEMPLATE.md copies got Files: sub-section examples (mirrors kept in sync).

INVENTORY.md: six restructure passes during doc-code parity audit (before-build and batch-executor entries expanded; after-build annotated "absorbed into batch-executor"; slash-commands restructured for both patterns with shipped-V annotations; /before-build + /build moved from "Pending V23" to "Shipped V25"; templates path corrected; parse_backlog.py added; Stop + PreToolUse (c) annotated "Shipped V25"). OPEN-QUESTIONS gained four entries; one resolved in-session.

Footer bumps V23 → V25 across 16 files. `plugin.json` 0.23.0 → 0.25.0; `PLUGIN_METHOD_VERSION` 23 → 25. `batch-executor.md` gained a V25 footer for consistency with sibling subagents. BUILD-METHOD's *Footer bumps* list adds `before-build.md` and `batch-executor.md`. Pre-validation smoke tests via Cowork bash (15/15 parser, 8/8 Stop, 9/9 PreToolUse boundary + V19/V22 regression); see TEST-LOG #031–033. Windows integration in `claude --plugin-dir` owed to Alex post-commit.

**Decisions taken and why.**

- **Doc-code parity audit escape-clause override: NO-CODE-METHOD's *Before build* / *After every build* rewrites landed in-session.** BUILD-METHOD's escape clause recommends deferring spec rewrites that would dominate. Default lean was defer. Override: the spec gap was load-bearing for V25's shipped subagents — before-build's read-spec-on-entry *depends on* *Before build* being operationally correct; batch-executor's recap references *After every build* labels. Leaving V22-era wording would have shipped agents reading a spec that didn't match what they do.

- **before-build subagent: validate-only first move + read-spec-on-entry.** Original design had a "reorganise pass" matching the spec's steps 1–2 verbatim. Validation review (fresh Sonnet reading the actual files) caught: planning has full BACKLOG edit authority since V22, making reorganise dead weight in ~99% of cases and silently absorbing the only realistic case (out-of-band manual edits) where flagging would matter. Changed to validate-only; reorganise survives only as response to verification-burden split. Rule-loading: original draft proposed inline (matching batch-executor on "mechanical not branching"). Validation reframed as "stable vs. fresh rules" — batch-executor inlined rules stable since V18; before-build's load-bearing rules were V25-introduced and likely to churn. Read-spec-on-entry kills doc-code parity drift on freshest rules.

- **`/build` argument-less per V25 Q3.** Out-of-order batches handled by reordering BACKLOG during planning, not by a build-time chooser. Single mental model with Stop-hook auto-continuation: both entry points always pick top unticked batch.

- **Ideation-session edits bundled into V25's commit, not separated at staging.** Previous uncommitted ideation left rule edits in `universal-behaviour.md`, NO-CODE-METHOD, Crash course, PLAN.md. V25's parity audit added edits to two of those. Plan was `git add -p` for separate tags. At commit time, procedural cost (`git add -p` is new to Alex; unpacking would be the most friction-heavy close-out step) outweighed clean-tag value — BUILD-LOG carries both narratives. Ideation work folded in this commit: wording sharpen on "push back rather than agree" → "push back rather than simply agreeing"; new "Walkthroughs one step at a time; alternatives all at once" rule in *Required of Claude*; `[SEQUENCE]` tag definition expanded with no-previewing clause + cross-ref; new fourth load-bearing example in Crash course's *What's editable, what's not* (counter changed three → four); new V28 row in PLAN.md ("Walkthrough-mode for non-UI testing"; previous V28–V31 shifted to V29–V32). No own session number.

**Pivots and surprises.**

- **Validation-via-sister-Sonnet-session was the right intervention.** When before-build hit the three open questions (halt scenarios, reorganise scope, inline vs. read-spec), spinning up a separate Claude Code session with a self-contained validation prompt produced sharper pushback than continuing in Cowork. Two recommendations flipped, one halt scenario dropped (stale Files: detection — over-engineered), one missing scenario surfaced (verification-burden-triggered split). Pattern worth keeping for design questions with real downside risk.

- **"after-build subagent" was a ghost reference in INVENTORY.** V17's architecture listed a separate after-build. V25's batch-executor design absorbed those responsibilities on the principle that the recap is most accurate in-context with the build. INVENTORY hadn't been updated; audit caught it.

- **Slash-commands convention changed mid-roadmap.** INVENTORY described slash commands as skills with `disable-model-invocation: true` etc. — the older pattern. V25's `/before-build` and `/build` landed in the newer `plugin/commands/<name>.md` pattern. Both patterns coexist now (init-project still uses old; new commands use new). INVENTORY restructured with shipped-V annotations.

- **parse_backlog.py is lenient on failure (always exit 0, `{}` on malformed) — `/build`'s first draft misread it.** Initial draft told main Claude to detect empty via "exit non-zero or empty payload." Re-read of the docstring caught it: detection has to be on output content (`{}` or empty), not exit code. Corrected before the Edit went through.

- **Cowork bash-mount staleness recurred — pre_tool_use.py + BACKLOG.md.** Same phantom-state issue as V22. Worked around by running CLI smoke tests against `outputs/` copies, then validating canonical state via file tools. Memory entry already exists (`reference_cowork_git_mount_phantoms.md`).

- **Edit tool's "must Read first" requirement bit on every Grep'd file.** Footer bumps required reading 8 templates I'd only Grep'd. Two-pass workaround: parallel Reads, then parallel Edits. A Read with offset/limit doesn't cover editing outside the read range — fresh Read needed. Tool affordance to remember.

**Carried forward.**

- **Windows integration smoke test in `claude --plugin-dir`** — run 2026-05-17 against pre-populated `v25-scratch`. TEST-LOG #034–050. End-to-end works; three bugs logged as OPEN-QUESTIONS for V26: Stop-hook template-placeholder misfire (#041), BACKLOG-TEMPLATE `[FOLD-IN PENDING]` ambiguity (#042), before-build parser-path spec (#044).
- **Subagent rule-loading pattern divergence** — OPEN-QUESTIONS. Defer convergence until V26–V31 ship and NO-CODE-METHOD change rate settles. Revisit if parity audit flags drift in batch-executor.
- **MANIFEST.md path-mapping schema gap** — OPEN-QUESTIONS. Blocks PreToolUse (d) read-before-edit; (d) deferred from V25 as a result. Five candidate shapes in the entry; promote to a planning session when MANIFEST schema work fits naturally.
- **Stop-hook 8-block cap** — OPEN-QUESTIONS. Parked — current design respects `stop_hook_active` so chain length is always 1; cap can't trigger.
- **`/plan` slash command** — still pending; auto-route remains the only planning invocation.
- **Slash-command footer convention** — not pursued. SessionStart footer-tripwire reads spine docs and subagent bodies, not slash-commands. Set when a hook or audit needs the fingerprint.

---

## V24 — 2026-05-16 — BUILD-METHOD.md and TEST-LOG.md added; session-tag and method-version decoupled

**What shipped.** Two new dev-internal docs and a slim of the project-root `CLAUDE.md`.

- `sovereign-implementer/BUILD-METHOD.md` consolidates the working manual — session structure (open, three middle shapes, close), doc-code parity audit (now with sixth item, *Ghost references*), testing semantics (corrected), BUILD-LOG / OPEN-QUESTIONS / new TEST-LOG entry shapes, footer-bump rules, planning artefact lifecycle. Lifted out of the old CLAUDE.md and expanded where the old version was thin or wrong.
- `sovereign-implementer/TEST-LOG.md` is new — 30 backfilled rows from V18 (3), V19 (11), V21 (10), V22 (6), one Fail (V22 INVENTORY ghost-command catch + separate row for its in-session retest as Pass), three Skipped with reasons. V20 and V23 had no testable code.
- Project-root `CLAUDE.md` slimmed 240 → 100 lines — orientation, environment, file ops, terminology cheat sheet, Taskflowapp lock-down, command-prompt experience level only. Everything procedural moved to BUILD-METHOD.
- PLAN.md table renumbered: V24 is this session; old V24–V30 shifted to V25–V31 (V20 precedent). Session-scope files renamed, headings bumped, internal cross-refs shifted. OPEN-QUESTIONS entries 1–3 had forward-looking refs shifted; entry 4's dated historical notes intact. INVENTORY got mechanical V## shifts on 6 forward refs.

**No method-version footer bumps anywhere** — `plugin.json` stays 0.23.0, `PLUGIN_METHOD_VERSION` stays 23, all footers stay V23. First session under the new dev-internal-doesn't-bump rule.

**Decisions taken and why.**

- **BUILD-METHOD.md as a new file, not a CLAUDE.md restructure (option a, not b).** The dev project's working manual deserves its own home, separate from CLAUDE.md's orientation / environment / personal-collab material. Lets CLAUDE.md be terse and gives the manual room to grow (TEST-LOG entry shape, ghost-references audit, footer-bumps list — none of which fit cleanly in the old CLAUDE.md). Option b would have preserved single-file convenience but lost the conceptual separation.

- **Session tag and method-version footer decoupled going forward.** Old convention bumped footers every session regardless. V20 (Crash course promotion) and V23 (Cowork mentions strip) both bumped despite arguably-doc-only scopes — recording an interpretive mismatch. New rule: footer + `plugin.json` + `PLUGIN_METHOD_VERSION` only bump when the session substantively changes method or plugin. Session tag still increments per session. V21 footer-mismatch tripwire stays silent because `PLUGIN_METHOD_VERSION` moves in tandem. V18–V23 numbers stay as-is.

- **TEST-LOG.md created this session, not deferred to V26's consumer-side ship.** Alex pushed back on a draft proposing defer. The failure mode this session diagnosed (CLAUDE.md asserting "plugin never installed" while V18/V19/V21/V22 BUILD-LOG entries all describe smoke tests) is precisely what TEST-LOG fixes — making outcomes queryable rather than buried in prose. Backfill was ~30 min.

**Pivots and surprises.**

- **Initial framing wasted a round-trip on "live install + back-test."** I opened proposing live-install + back-test as next session before doing the read-pass, citing CLAUDE.md's *Plugin install status* "never installed" paragraph. Alex's pushback: (1) V23 was a terminology sweep with nothing testable, (2) tests have happened — BUILD-LOG records them — the recording isn't visible to future sessions, (3) the proposed session has no current pathway since the plugin isn't packaged for global install. Saved as `feedback_dont_propose_live_install_session.md`. Root fix is BUILD-METHOD's corrected *Testing* section, not just the memory.

- **The old footer-bump convention had quietly drifted across V20 and V23.** When I drafted BUILD-METHOD I treated "every session bumps" as the rule. Alex called it out: the rule itself was the problem for doc-only sessions. Decoupled-numbering is partly retroactive acknowledgement; history stays as-shipped with *Historical note* in BUILD-METHOD recording the discontinuity.

- **INVENTORY.md's forward-pointers are semantically stale.** During renumber, several refs (Crash course "Updated in V25", DOC-STRUCTURE "deferred to V25", `/new-project` "Pending — V26") look misaligned even pre-renumber. Mechanical +1 shift applied only. Content audit deferred.

- **Renumber surfaced V28.md and V31.md bodies still reference a "live-install session" deferred from V27/V28.** Superseded by this session's BUILD-METHOD *Testing*. Natural fix is V28's planning session.

- **BUILD-LOG header pointer updated mid-entry.** Said "see CLAUDE.md → *Build log*" — section moved to BUILD-METHOD this session.

**Carried forward.**

- **V23 carry-forwards remain valid.** Soft-discipline risk for mid-build SoT edits; OPEN-QUESTIONS cross-version entry still has Cowork-first vocabulary; V22's smoke-test items (a) and (e) not in TEST-LOG because BUILD-LOG didn't explicitly attest them.
- **INVENTORY.md forward-pointers** — semantic audit deferred.
- **`sessions/V24.md` hand-delete** — not applicable. This session was directed live without a scope file; step 7 of session close is a no-op. Precedent: live-directed sessions skip step 7.
- **V28.md and V31.md body's "live-install session" references** — superseded; address during V28's planning.

---

## V23 — 2026-05-17 — Remove Cowork mentions from method docs; Claude Code becomes explicitly required

**What shipped.** Cowork-removal sweep across method spec docs, templates, and plugin component bodies.

- `NO-CODE-METHOD.md` — explicit "the method requires Claude Code" at the top; "Claude-Code fallback" framing removed from new-project route; *Detect template state* tripwire simplified to recommend new-project route directly; every "in Cowork" / "during their next Cowork session" → "by hand during planning sessions" (the fold-in mechanism is unchanged — user edits by hand, Claude Code agent doesn't — only the location moves).
- `DOC-STRUCTURE.md` — two-line equivalents in *Fold-ins pending* and *Planning batches*.
- `Crash course.md` — bigger rewrite: "Where each tool fits" reframed from two tools to two phases (planning, build); "Day one" walkthrough rewrote around new-project route; editing-surfaces table collapsed from two columns to one ("Claude (the agent) edit access").
- Templates: `ADDITIONAL-DOC-TEMPLATE.md` and `BACKLOG-TEMPLATE.md` in both locations got Cowork mentions replaced.
- Plugin components: `plugin/agents/planning.md`, `pre_tool_use.py` deny message, `session_start.py` template-state recommendation, `init-project/SKILL.md` all stripped.
- This project's outside-the-repo `CLAUDE.md` stripped its "work happens in Cowork by default" specification per user direction — left unspecified (not replaced with Claude Code) to preserve flexibility during Alex's personal migration.
- `OPEN-QUESTIONS.md` prose-only-rewrite entry got a V23 note recording the framing shift: target audience moves from "Cowork novices" to "people using the method outside the plugin."
- PLAN.md renumbered during V23 prep: V23 (new) is Cowork-removal; old V23–V29 → V24–V30. Footers V22 → V23 across method-side files (3 spec docs + 5 templates × 2 + INVENTORY + planning.md). `plugin.json` 0.22.0 → 0.23.0; `PLUGIN_METHOD_VERSION` 22 → 23.

**Decisions taken and why.**

- **Claude Code is required, not recommended.** The user's direction was unambiguous: the method ships as a Claude Code plugin and can't run anywhere else, so the docs make it mandatory. Stronger than V17's "Cowork-first, Claude Code for builds." The prose-only rewrite (parked in OPEN-QUESTIONS) is the carve-out for users who want the planning/build disciplines without the plugin.

- **Replacement wording: "during planning sessions" + "by hand."** The Cowork mentions weren't pure mentions — they were the *location* of fold-ins. Stripping without replacement would break sentences. The replacement keeps the mechanism (user does the editing, not Claude) and updates only the location. "By hand" makes the user-vs-agent distinction explicit: user opens file in editor and types; Claude Code agent can't write to SoT docs (PreToolUse enforced).

- **This project's own `CLAUDE.md` is unspecified, not Claude-Code-prescribed.** Alex is mid-personal-migration from Cowork to Claude Code with no fixed timeline. Pinning the dev location would force a date she doesn't have. Solution: strip the specification, leave to discretion.

- **Internal planning artefacts deliberately left alone.** PLAN.md, V27.md, OPEN-QUESTIONS' cross-version reconciliation entry retain Cowork refs. V23 scope was strict mentions-strip on user-facing content. Each resolves naturally when its session runs. `Archive/` and BUILD-LOG are historical record.

**Pivots and surprises.**

- **Crash course rewrite was bigger than a mentions-strip.** "Where each tool fits" was load-bearing structural framing — two tools used in sequence — and "Day one" described starting in Cowork and switching. Both framings wrong post-V23, so both got rewritten. Within scope per V23.md's anticipated "minor rephrasing," but Crash course's narrative voice changed measurably.

- **"Edit by hand during planning sessions" implies a soft discipline that didn't exist in the Cowork-tool era.** Under the original method, SoT docs were edited in Cowork (no file editor in builds), so the user *physically couldn't* edit `UX.md` during a build. Under V23, the user has a file editor available throughout — the discipline of "don't edit UX.md mid-build" is now *soft* (not hook-enforced; only Claude's edits blocked). Small new drift risk: a user editing UX.md mid-build would silently violate build-scope-locked. Not addressed in V23 (mentions-strip, not redesign); recorded for future.

- **Cowork session corruption from parallel sessions** during V23 prep (yesterday). Linux mount vs. Windows filesystem fight produced CRLF mangling across many files and silent truncation of `Archive/Version 10/NO-CODE-METHOD.md`. Recovered via `git restore .` after closing parallel sessions. Logged as memory (`reference_cowork_parallel_sessions_corrupt.md`). Not directly V23, but worth recording.

- **"Instructions" vocabulary miss.** Mid-session, I repeatedly failed to recognise that "the instructions" in Alex's vocabulary is Cowork's UI label for `CLAUDE.md`. Screenshot disambiguated. Logged as feedback memory.

**Carried forward.**

- **Live install + back-test of V18–V23** per existing OPEN-QUESTIONS entry. V23's changes — especially the rewritten `pre_tool_use.py` deny message and `session_start.py` recommendation — should be exercised in a real Claude Code session. Pre-install era's script-level validation isn't enough for user-facing prompt strings.

- **Soft-discipline risk for mid-build SoT edits** — above. If real use surfaces failure, consider a soft-warning hook (PostToolUse on manual SoT edit) or document the discipline in NO-CODE-METHOD → *Method contract*. Not pursued.

- **OPEN-QUESTIONS' Cowork-first cross-version reconciliation entry** still uses Cowork-first vocabulary. Substance (tripwire half folded in V21, worker half pending in V27) still valid; framing stale. Sweep when V27 ships.

- **`planning/sessions/V23.md` hand-delete** per CLAUDE.md and V21/V22 precedent — Alex deletes via Windows Explorer; Cowork bash mount can't delete due to ACLs.

- **Personal migration from Cowork to Claude Code** (Alex's workflow). Not encoded as method recommendation but informs this project's CLAUDE.md (now dev-tool-unspecified). Decoupled from any session.

---

## V22 — 2026-05-14 — Planning subagent + Serves-line PreToolUse hook

**What shipped.** Two plugin components landed and four method-side docs caught up.

- `plugin/agents/planning.md` is the plugin's first subagent. System prompt covers: inputs (the `primary_intent` line main Claude passes), always-on first action (read CLAUDE.md, path block, BACKLOG/MANIFEST/UX, plus NO-CODE-METHOD → *During planning* and DOC-STRUCTURE → *BACKLOG.md structure*), the three planning flows (test notes / feature request / scope question), mixed-input secondary sort that catches "by the way, can we add dark mode?" even when primary is test notes, always-run drift checks, BACKLOG editing protocol with Q3 Serves-line caveat, Discoveries → planning batches promotion, recap contract. Tools: `Read, Edit, Write, Glob, Grep` — no Bash (no scripts), no Task (subagents can't spawn subagents per V17).
- `plugin/hooks/pre_tool_use.py` gained the Q3 Serves-line check: parses every `Serves UX.md: <names>.` line in proposed new content, matches each name against UX.md's `## Functionalities` → `### ` entries with case-insensitive exact match after whitespace-trim, denies with redirect message listing unmatched names + sample of known entries. `Serves <ADDITIONAL>.md:` lines for additional SoT docs out of scope, pass through.
- NO-CODE-METHOD → *At session start* gained "Handoff to the planning subagent" defining four `primary_intent` values (`test notes`, `feature request`, `scope question`, `mixed (primary: ...)`) and the rule that main Claude relays the subagent's recap. *During planning*'s drift-check skip clause tightened to "always run; only skip case is 'nothing has been built yet'" (Q2 explicit). Crash course got a one-paragraph mention of the subagent split. DOC-STRUCTURE gained a Serves-line matching note.
- INVENTORY's planning-subagent and PreToolUse entries filled in with V22 state, D3 structurally corrected (SessionStart hooks inject context — they can't launch subagents; main Claude is the launcher). OPEN-QUESTIONS' direct-edit-users entry got a V22 note: shape #1 partially folded — file-level manual edits caught by drift check 2 now that it runs every session; in-file changes inside still-tracked files remain uncovered.
- Footer V21 → V22 across 15 files. `plugin.json` 0.21.0 → 0.22.0; `PLUGIN_METHOD_VERSION` 21 → 22.

**Decisions taken and why.**

- **Q1 — main Claude classifies primary intent at handoff; subagent still does mixed-input sort.** Classification is cheap and main Claude has to read the opener anyway. Doing it once in main Claude keeps the subagent prompt tight. Mixed-input openers still require the subagent to look at the opener a second time during the sort, so option (a)'s "classify once" doesn't eliminate the subagent's own scan — it just hints which flow to start in. Option (b) (subagent classifies itself) would unify location at the cost of a longer prompt. (a) wins on clarity-per-token.

- **Q2 — drift checks run every planning session; only skip is "nothing has been built yet."** A "skip when nothing built since last planning" rule would need a reliable signal for "since last planning," and there isn't one. More important: drift check 2 (MANIFEST.md ↔ codebase) is exactly the diff that surfaces manual code edits outside Claude's awareness — the direct-edit-user case in OPEN-QUESTIONS. A skip rule would defeat that. Cost when no diff is low (subagent reads, finds nothing); cost when a diff is missed is silent compounding drift. Asymmetric in favour of always-running.

- **Q3 — case-insensitive exact match after whitespace-trim; no fuzzy.** The hook's job is to catch "Claude proposed a build batch with no matching UX entry," which usually means Claude skipped the planning-batch → fold-in step. Fuzzy would let that slip whenever the made-up name *resembles* a real entry. Strict-enough-to-fail-fast. Case-insensitive-after-trim handles the only harmless variation (capitalisation in headers) without opening the door to ambiguous matches. Real typos by Claude are rare; deny message gives a one-round-trip fix.

- **Slash command `/plan` not shipped.** V22.md's success criteria require the auto-route path (paste test notes → main Claude classifies → planning fires). User-facing `/plan` listed in INVENTORY but not in V22 scope; can land later if auto-route proves insufficient, or stay deferred.

**Pivots and surprises.**

- **Web-search mid-build for the subagent file format.** Started V22 not knowing the YAML frontmatter shape, whether `subagent_type` was bare or plugin-namespaced, or whether `agents/` files auto-register. Wrote structured prompt for Alex to paste into Sonnet; she paste-backed `plugin-subagent-reference.md`. Key facts: `subagent_type` is `<plugin-name>:<agent-name>` (so `no-code-method:planning`); `description` drives auto-delegation; `hooks`, `mcpServers`, `permissionMode` silently ignored in plugin subagents; `agents/*.md` auto-register. Guessing wrong would have wasted a smoke-test cycle.

- **D3 in INVENTORY described a mechanism that doesn't exist.** V17 said "SessionStart auto-launches the planning subagent." Hooks inject context — they can't launch subagents. V21's actual implementation was correct (hook surfaces state; main Claude decides), but INVENTORY hadn't been updated.

- **Cowork bash mount stuck on pre-edit snapshot of pre_tool_use.py.** Bash saw 174 lines / May 13 timestamp; Read saw current 455. Same phantom-state issue as the existing memory note. Couldn't run `python -c "ast.parse(...)"` to verify syntax in-session. Eyeball review used; smoke test is the real validation.

- **Planning subagent's prompt deliberately delegates rule detail to NO-CODE-METHOD rather than restating.** Saved against Opus risk #5 (long subagent prompts eat their own context). Names doc sections to read first, lists only V22-specific clarifications + behavioural protocol. Tightness vs. self-containment is a real tension; preferring tightness for V22.

- **INVENTORY's slash-commands list described unshipped commands as if they existed — caught mid-smoke-test.** When the smoke test opened Claude Code in Taskflow, the planning subagent confidently recommended `/migrate`. `/migrate` doesn't ship until V26, but INVENTORY listed it (and five other future slash commands) without "pending" annotation. Fold-in fix in the same V22 commit: every entry now carries "**Shipped Vxx**" or "*Pending — Vxx*"; top-of-section preface states only `/init-project` is shipped. Audit missed this in first sweep; smoke test caught it. Same precedent as V21's plugin/templates footer catch.

- **The smoke test's auto-route check (Check 2) couldn't run in Taskflow.** Taskflow is tier 2 — its `CLAUDE.md` path block uses the pre-V18 bullet-list format and its spine docs lack the method-aware footer. SessionStart correctly classified tier 2; main Claude correctly declined to auto-route. All working, but Checks 2–4 (auto-route, Serves deny, case-insensitive accept) can't be exercised in Taskflow. Plan was to pivot to `v22-scratch` via `/init-project`; actual setup hit multiple side-quests (Alex ran `/init-project` from Taskflow's session; Claude recommended non-existent `/migrate`; loop-detection menu appeared third invocation). Resolved by closing Taskflow's session and starting fresh.

**Carried forward.**

- **Smoke test for V22** — for Alex post-commit. Suggested: (a) after `/reload-plugins`, confirm `plugin/agents/planning.md` in `/agents`; (b) in Taskflow, paste short test notes — verify main Claude classifies, spawns planning, recap returns; (c) ask Claude to add a build batch with a broken `Serves UX.md: NonExistentEntry.` — verify PreToolUse denies with redirect; (d) verify `Serves UX.md: <real entry, different case>` succeeds; (e) confirm V21's SessionStart still fires in a tier-3 project.

- **`planning/sessions/V22.md` hand-delete** per CLAUDE.md and V21 precedent.

- **`/plan` slash command** — not pursued. Future session can add it (one skill file in `plugin/skills/plan/`) if auto-route proves insufficient.

- **Cowork bash-mount staleness on pre_tool_use.py** — reproducible. No action; smoke test validates syntax-in-flight.

- **Direct-edit-users OPEN-QUESTIONS entry** — V22 partially folded shape #1. Shape #2 (developer-mode entry point), shape #3 ("Who this is for" doc section), and residual gap (in-file changes inside still-tracked files) remain.

---

## V21 — 2026-05-14 — SessionStart hook extension: three-tier detection + foundational reads + footer tripwire

**What shipped.** `plugin/hooks/session_start.py` extended from ~60 lines (V18's universal-rules emitter) to ~280 lines, now doing the full V21 scope. The hook reads project root from stdin JSON `cwd` field — not from `$CLAUDE_PROJECT_DIR`, which is broken for plugin hooks (anthropics/claude-code#9447); resolves CLAUDE.md; parses its fenced JSON path block; reads spine + any additional SoT docs; detects template state (`[Project Name]` placeholder); detects unfinished top build batch in BACKLOG (filtering template-placeholder titles); runs a version-footer mismatch tripwire — for every loaded SoT doc, compare `*No-code method — Version N.*` footer against `PLUGIN_METHOD_VERSION = 21`.

**Three-tier behaviour:**
- **Tier 1** (non-method folder — no CLAUDE.md and no method-footer spine docs): emits *nothing*, exits 0. Plugin invisible.
- **Tier 2** (partial method shape — four sub-cases between missing-CLAUDE.md-with-spine-docs and present-CLAUDE.md-with-unparseable-path-block): universal rules + single-paragraph gap flag naming the missing piece and pointing at `/init-project` or `/migrate`.
- **Tier 3** (complete method project): universal rules + full state summary, including a routing reminder that the hook does not classify the user's opener — Claude does.

Footer V20 → V21 across 8 method-side files. `plugin.json` 0.19.0 → 0.21.0 (V20 missed it). INVENTORY updated for new SessionStart shape; stale "added in V20" → V21. Project's outside-the-repo CLAUDE.md gained three rules: Cowork-first lean ("stay in Cowork; switch to Claude Code only when something needs a real session to be tested"), test-run guidance (Claude must explain plugin enabling and treat Alex's Claude Code inexperience as default), "Which CLAUDE.md is which" sub-section distinguishing the three (dev project, template, consumer).

Smoke-tested on Windows in `~\v21-scratch`: plugin loaded, both hooks registered, empty-folder verified tier 1 (silent), `/init-project` scaffolded cleanly, fresh session against the scaffold fired tier 3 — Claude reported 3 of 3 path entries resolved, template state in all four spine docs, routing reminder, version-footer mismatch tripwire (which surfaced the missed `plugin/templates/` footer bumps; see *Pivots*). Tier 2 in Taskflow not pursued — the mid-smoke tripwire catch already exercised the structural-mismatch code path; revisit only if real-world tier-2 misfires surface.

**Decisions taken and why.**

- **Tier 1 emits nothing — behaviour change from V18.** V18 injected universal-behaviour rules in *every* Claude Code session regardless of project. V21 narrows to method projects only. The argument for preserving V18 was "soft visibility never hurts"; for invisibility (won): the plugin should respect folders it has no claim on. If installed globally but working in 20 unrelated folders, those shouldn't get method-shaped noise.
- **Route signal is prose, not a structured marker.** Hook describes structural state; Claude classifies the opener. Only consumer is Claude. A structured marker (`ROUTE: planning`) was considered but later hooks would re-derive route from state anyway, and SessionStart can only *recommend* — Claude makes the final call after seeing the opener.
- **Tier-2 detection tightened via method-footer check.** V21.md flagged the false-positive risk: a non-method folder with an unrelated BACKLOG.md would trip tier 2. Fix: a spine doc counts only if it carries `*No-code method — Version N.*` footer.
- **Tripwire half of cross-version reconciliation folded into V21, worker half stays in V26.** Per OPEN-QUESTIONS' plan (which referenced V20 / V24 in pre-V20-renumbering terms; corrected to V21 / V26). Tripwire is a SessionStart-time read with no auto-fix; worker (diff-and-propose) lives in `/migrate`.
- **Method response to direct-edit users — not folded into V21.** Per OPEN-QUESTIONS' own logic. V21 adds reads + tiers + routing; none catch manual code edits. Natural home for "tighten drift detection" is V22 (drift logic inlined into planning); developer-mode and "Who this is for" shapes would warrant own sessions.
- **`plugin.json` bumped 0.19.0 → 0.21.0, skipping 0.20.0.** V20 was doc-only and didn't bump. Aligning plugin version with method version is more useful than walking every integer.

**Pivots and surprises.**

- **Workflow misframed early.** Initially described V21's implementation as happening in Claude Code, with this Cowork session as planning prep. Alex corrected: she builds the method itself in Cowork; Claude Code only enters for smoke-testing. Triggered the project-CLAUDE.md edits (Cowork-first lean, "Which CLAUDE.md is which"). The tagging question collapsed accordingly — this *is* V21.

- **"Which CLAUDE.md is which" confusion was real and worth pinning.** When discussing project-root detection, I used "the project's CLAUDE.md" without naming which — Alex's, the template, or Taskflow's. Plain confusion, fixed in the project's CLAUDE.md. Also surfaced that V19's `/init-project` skill (which she'd forgotten she'd shipped) already automates the template-copy-and-rename.

- **Sonnet's hook-environment summary was confident but unsourced.** Alex pasted it; I asked whether Sonnet had web-searched; she confirmed it hadn't. Direct fetch of source URLs confirmed: stdin `cwd` is documented hook input contract; `CLAUDE_PROJECT_DIR` is broken for plugins per #9447; sibling bug #11649 (`CLAUDE_ENV_FILE` empty in plugins) marked "Fixed in next release" — implies #9447 likely fixed similarly, but stdin is the correct path regardless.

- **`planning/sessions/V21.md` couldn't be deleted via Cowork's bash mount.** Permission denied per the existing memory. Hand-deletion via Windows Explorer baked into push instructions.

- **The version-footer tripwire caught a real oversight mid-smoke-test.** The session-close footer-bump pass covered `sovereign-implementer/templates/*.md` but missed `plugin/templates/*.md` copies — the templates `/init-project` actually scaffolds from. Tier 3 flagged the scaffolded docs as Version 20 while plugin reported Version 21. Fixed in the same commit. The two-directory template sync (V19 rule) is easy to miss because CLAUDE.md → *Session close* says "every template" without naming both directories. **The smoke test paid for itself with this catch alone.**

**Carried forward.**

- **Tier-2 detection rule may need tightening.** If real-world use surfaces false positives or negatives, revisit. For V21 ship, method-footer-in-spine-doc is the tightest signal available without parsing internal doc structure.
- **Method response to direct-edit users** — remains in OPEN-QUESTIONS, V21-vs-V20 reference corrected. Revisit during V22 planning at earliest.

**Build-log housekeeping (post-tag patch — V18 precedent).** Initial V21 entry was drafted partway through the session and listed the smoke test and V21.md hand-delete under *Carried forward* — items completed before the v21 tag. Smoke-test outcome folded into *What shipped*; V21.md hand-delete bullet removed; *Carried forward* now lists only items genuinely outstanding past V21.

---

## V20 — 2026-05-14 — Crash course promoted to source-of-truth doc; planning shifts

**What shipped.** Crash course.md became a parity-tracked source-of-truth doc — CLAUDE.md's doc-code-parity audit checklist gained a fifth item naming Crash course alongside spec docs, templates, INVENTORY. To earn that status the doc got a drift audit: `[FOLD-IN PENDING]` mechanism paragraph rewritten to describe the dedicated *Fold-ins pending* section (was still describing pre-V19 in-batch marker); three-sections-of-BACKLOG rationale block updated to four; prerequisite carve-out added to *Why batch scope is locked*; UX-principle-conflict surfacing added to *How a test note becomes a feature*; Method contract Required/Prohibited named in *What's editable*; *Where the actual files live* corrected (Taskflow repo → sovereign-implementer repo, version folders → git tags); user's locking-rationale phrasing landed at top of *Editing surfaces*.

Planning shifts: existing `V20.md`–`V27.md` renamed to `V21.md`–`V29.md` (this housekeeping became V20); new `V24.md` for TEST-LOG mechanism + protocol; `V23.md` (formerly V22, Before-build subagent) absorbed batch-sizing into scope. PLAN.md rewritten. New OPEN-QUESTIONS entry: *Cowork-friendly prose-only rewrite (post-plugin-build)*. Footer V19 → V20 across 15 files.

**Decisions taken and why.**

- **Crash course earns SoT status, but not by retrofitting unshipped work.** Initial proposal bundled two things: promote (yes) and pre-populate with V20–V27 scope file contents (no — those are explicitly provisional; writing them in would turn plans into authoritative prose). Promotion stands; fold-ins land session-by-session.
- **Cowork-first stays in the spec for now; de-Cowork-ification is a future deliverable.** Mid-session reconsideration. Current plugin-based method IS Claude-Code-specific — hooks, slash commands, `[FOLD-IN PENDING]` all need Claude Code primitives that don't exist in Cowork. Spec correctly documents reality. Cowork-friendly prose-only rewrite is a separate substantial deliverable, parked pending V29.
- **TEST-LOG.md is operational, sibling of MANIFEST.md.** Sonnet's V20 draft handed a clean shape. Re-categorised as operational (Claude updates during builds), dropped inside-doc "Version: 0.1" in favour of footer convention, distributed five protocol rules across NO-CODE-METHOD's existing phases rather than as one new section. V25's After-build will enforce the gate; V24 ships the prose.
- **Batch-sizing principle folds into V23, not its own session.** Small paragraph in *Before build* plus mid-build re-batching carve-out — bundling with V23 (Before-build subagent) keeps doc-code parity clean.

**Pivots and surprises.**

- **Stale `.git/index.lock` blocked session-file renames.** Zero-byte lock existed only on Linux mount's view (Windows reported no such file). `rm -f` failed with "Operation not permitted." `git mv` recreated its own lock. Workaround: plain `mv`, let git detect renames as 100% content matches at commit. Memory note if it reproduces.
- **Read-required-before-Edit caught the renames.** First batch of post-rename header bumps on V21.md and V23.md failed because they were Read pre-rename under old paths. Re-Read after rename, edits landed.
- **"Cross-version template reconciliation" OPEN-QUESTIONS framing weakened.** Pre-commits to "Cowork-first is now the recommended path"; the new Cowork-friendly-rewrite entry partially supersedes. Both stay; cross-version wording adjusts when the rewrite question resolves.

**Carried forward.**

- **Cowork-friendly prose-only rewrite of the method** — OPEN-QUESTIONS. Parked until V29; promote sooner if public release approaches.
- **TEST-LOG.md mechanism + protocol** — `sessions/V24.md`. Five rules, new operational doc class, new template, structural spec, fourth drift check.
- **Batch-sizing principle** — folded into `sessions/V23.md`. Three sub-rules + verification-burden recap + mid-build re-batching carve-out + Crash course parity item.
- **V27 scope reframed** — was "DOC-STRUCTURE migration + Crash course update"; now "DOC-STRUCTURE migration + Crash course coherence pass" since Crash course is parity-tracked. May need further tightening when V27 plans.

---

## V19 — 2026-05-13 — PreToolUse hook + bundled templates + /init-project + Fold-ins pending section

**What shipped.** The plugin now blocks edits to locked source-of-truth docs and gives Claude an unambiguous place to record the proposed change instead.

- `plugin/hooks/pre_tool_use.py` PreToolUse hook intercepts `Edit`, `Write`, `MultiEdit` against UX.md and any additional SoT doc declared in the project's CLAUDE.md path block. Returns deny decision telling Claude to add a `[FOLD-IN PENDING]` block to the new *Fold-ins pending* section of BACKLOG.md. Registered in `hooks.json` with `Edit|Write|MultiEdit` matcher.
- 5 templates bundled inside the plugin at `plugin/templates/` (copy of repo-root, both kept in sync via session-close footer-bump rule).
- New `/init-project` skill at `plugin/skills/init-project/` (`disable-model-invocation: true`, `user-invocable: true`) — Python scaffold script recursively scans `cwd` for the four destination filenames before writing, echoes target path for confirmation, refuses (pointing at `/migrate`) on conflicts.
- Structural rewrites for fold-ins pending: BACKLOG-TEMPLATE.md (×2), DOC-STRUCTURE.md BACKLOG.md section, NO-CODE-METHOD.md Editing surfaces + Fold-in vocabulary + per-route mentions.

Smoke-tested on Windows in a scratch dir: plugin loaded, both hooks registered, `/init-project` scaffolded cleanly and refused on non-empty, PreToolUse blocked an `Edit(UX.md)` attempt with deny visible, Claude pivoted to add the `[FOLD-IN PENDING]` block, the BACKLOG edit proceeded unblocked.

**Decisions taken and why.**

- **Templates at `plugin/templates/`, not nested inside `skills/init-project/`.** Originally drafted as `skills/init-project/templates/` (one consumer), revised after recognising templates also serve `/migrate` (V24) as reference structure to diff user-authored docs against. With multiple consumers, plugin-root is the right semantic home.
- **`/init-project` refuses on non-empty target, doesn't merge.** Recursive scan checks any of the four destination filenames anywhere under `cwd`. Cowork-first authoring is the expected path, so "user arrives with pre-drafted docs" is *normal* — and belongs to `/migrate`, not `/init-project`. Half-scaffolding would silently mix template-source and user-source. Refusal is louder and safer.
- **Hook denies with a redirect message rather than silently rewriting.** PreToolUse can technically rewrite an Edit's target via `updatedInput`, but doing so would silently transform UX.md writes into BACKLOG.md writes — magical, brittle (the hook would have to synthesize a `[FOLD-IN PENDING]` block from the raw edit), and against the method's "be told what's wrong, don't be silently rerouted" principle. Hard-block + reason keeps Claude in the loop.
- **`[FOLD-IN PENDING]` gets its own top-level section in BACKLOG**, between Red flags and Planning batches. Pre-V19 nested fold-ins inside the originating planning batch, but only the planning-batch-resolution route has a preceding batch — new-project, migration, and now the PreToolUse intercept all produce orphan blocks. Own section means one clear "things waiting for fold-in" location regardless of origin. Bigger rewrite to DOC-STRUCTURE and NO-CODE-METHOD than V19 scope said, but the alternative (hook deny referring to a section that doesn't exist in the template) was worse.

**Pivots and surprises.**

- **`${CLAUDE_PLUGIN_ROOT}` does expand inside skill bodies.** Flagged as real uncertainty in V19 plan ("may differ from hooks"); smoke test resolved on first try — `python "${CLAUDE_PLUGIN_ROOT}/skills/init-project/scripts/scaffold.py" check` expanded to full Windows path correctly.
- **Skill frontmatter shape works.** `disable-model-invocation: true` + `user-invocable: true` produced a working `/init-project` (visible as `/no-code-method:init-project`). No `agent:` key needed for skills that just run a script.
- **V18's universal-behaviour rules visibly self-policed on first hook test.** Asked to add a placeholder to UX.md, Claude refused before PreToolUse fired — citing UX.md "no placeholder entries" and offering three alternatives. The hook is a backstop, not the only line of defence. Forced the hook test with explicit "stress-testing, please attempt the edit anyway" — confirmed both layers work.
- **A Discovery surfaced mid-smoke-test.** Claude's first attempt at writing the fold-in block flagged that BACKLOG-TEMPLATE.md had no designated section for `[FOLD-IN PENDING]` — placed it at top of Planning batches with "this is my guess at the canonical location." That note made the structural rewrite (originally pushed to OPEN-QUESTIONS) part of V19's shipped work. Taking the user's "let's do it in V19 anyway" call was right.
- **Hook permission gates appeared at every Python invocation.** Claude Code's "approve commands" workflow: each `python ...` (the `check` call, then the `write` call) triggered its own dialog. Bothersome on a 4-step skill but correct — blanket approval would have been over-permissive. Note for Crash course in V25.
- **Test scratch dir lived outside the mounted workspace.** Alex created `~/v19-scratch` on Windows; smoke-test work happened in a Claude Code session pointing there, but I couldn't delete it myself (path outside mount). Handed back PowerShell `Remove-Item -Recurse -Force`. Confirmation that smoke-test directories don't need to be in mounted workspace folders.

**Carried forward.**

- **Cross-version template reconciliation** raised as OPEN-QUESTIONS entry — fold into V20 (tripwire in SessionStart) + V24 (worker in `/migrate`); entry removed when both folds confirmed.
- **Step 8 (subfolder-conflict test on Windows) not pursued:** recursive scan was verified in sandbox during V19 (`/tmp/scaffold_test2/docs/UX.md` caught as `docs/UX.md`, write refused with exit code 2). `pathlib`'s `rglob` and `name` matching are platform-agnostic; Windows path separators aren't a different code path. Skipping the live Windows test saved usage with negligible information loss.
- **V25 Crash course note:** document per-command Claude Code approval gate so first-time users know to expect dialogs at each Python invocation.

---

## V18 — 2026-05-12 — Plugin scaffold + SessionStart hook + JSON path block

**What shipped.** The plugin's bones now on disk at `plugin/`. Minimal `.claude-plugin/plugin.json`, `hooks/hooks.json` declaring a `SessionStart` hook, Python script (`session_start.py`) emitting the eight universal behavioural rules — push back, plain English, no stealth fixes, red-flag surfacing, the rest — as `additionalContext` at every session start. Rules text lives in `hooks/universal-behaviour.md` (copied from NO-CODE-METHOD → Method contract → Required of Claude; becomes canonical when NO-CODE-METHOD retires in V26). CLAUDE-TEMPLATE.md's path block changed from markdown bullets to fenced JSON so V19+ hooks can parse paths deterministically without grepping prose. Smoke-tested on Windows: `claude --plugin-dir <path>` loaded, `/hooks` showed `SessionStart` registered, Claude recited all eight rules verbatim.

**Decisions taken and why.**

- **Plugin lives inside the same repo (`sovereign-implementer/plugin/`), not a separate repo.** Method docs and plugin code co-evolve through V27 — every change touches both. One history beats threading version tags across two repos. Going one-repo to two later is cheap; the reverse is expensive.
- **Hook script language is Python, not bash or Node.** Bash has the shell-profile contamination risk Opus flagged in V17 and needs Git Bash on Windows. Node isn't bundled with Claude Code on Windows. Python is cross-platform, robust at parsing, and most readable for a non-coder debugging a hook.
- **Path block is JSON, not YAML.** Both parse from Python; JSON wins because it needs zero external deps (`json` is stdlib; `pyyaml` would be a plugin install dep), fails loudly on syntax errors, no quoting gotchas. Edited rarely — reliability beats prettiness.

**Pivots and surprises.**

- **`UserPromptSubmit` hooks in plugins don't execute** — GitHub `anthropics/claude-code#10225`. V18 was scoped to install one; pivoted to `SessionStart` (works in plugins, functionally equivalent given the method's `/clear`-after-every-build discipline). Saved to memory.
- **`${CLAUDE_PLUGIN_ROOT}` doesn't quote paths with spaces.** Smoke test failed silently first time because expanded path (`C:\Users\Alex\Desktop\Taskflow Planning\...`) got truncated at the first space — Python tried `C:\Users\Alex\Desktop\Taskflow` and gave up. Fix: wrap script path in escaped quotes in `hooks.json`. Future hook commands must follow this pattern; saved to memory.
- **Claude Code CLI wasn't installed on this machine.** Smoke testing required installing it via Anthropic's native PowerShell installer — adds ~30 min but overdue work (Claude Code CLI is Alex's stated Priority 1).
- **Two working-with-me rules added to project CLAUDE.md mid-session**, saved as feedback memories: (1) when uncertain about external facts, ask Alex to web-search rather than guessing; (2) format web-search requests as paste-able prompts for Sonnet, not questions to Alex.

**Carried forward.**

- V19+ hook commands all need the escaped-quote pattern from the start (memory + V19.md note).
- Crash course (V25) needs install instructions covering Python prerequisite, Claude Code CLI install, and the `where claude` diagnostic for the native+npm hook bug (memory in V17 work).
- `BUILD-LOG.md` itself added post-tag as a working-process improvement — separate small commit after the V18 tag.

---

## V17 — 2026-05-11 — Plugin-migration architecture decided

**What shipped.** Migration path from "method as markdown docs" to "method as a Claude Code plugin" scoped end-to-end. Produced `planning/INVENTORY.md` (final plugin component list — hooks, subagents, slash commands, bundled artefacts), `planning/PLAN.md` (session-by-session roadmap V18→V27), `planning/claude-code-plugin-feasibility-response.md` (Opus run grounding design in actual Claude Code capabilities). Created `planning/sessions/V18.md` through `V27.md` as provisional scopes. Switched versioning from numbered folders (`Version 3/` through `Version 16/` in `Archive/`) to git commits and tags (`v17`, `v18`, ...) — folders archived, going forward each session ships as one tagged commit.

**Decisions taken and why.**

- **Plugin layout = two-layer split.** Per-project SoT content (UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md, additional SoT docs) stays per-project. The mechanical method itself (process, schemas, behaviour contract) becomes the plugin. This split is the whole bet: discipline becomes structural (hooks deny) rather than prompt-based (Claude is asked to behave).
- **Stop hook proposes, user gates** (D1). Build sequencer single-steps one batch per user prompt rather than auto-chaining. `stop_hook_active` naturally prevents loops; explicit user gating matches the method's `/clear`-after-build discipline.
- **Drift checks inlined into planning subagent** (revision vs walkthrough). Subagents can't spawn subagents — Opus confirmed. Drift logic moves from a would-be `drift-checker` subagent into planning's instructions.

**Pivots and surprises.**

- **"Always-loaded core skill" idea collapsed under Opus's check.** Skill bodies are progressive-disclosure — never always-loaded. Universal behavioural rules had to move to a hook (V17 chose `UserPromptSubmit`; V18 pivoted to `SessionStart` after the plugin bug).
- **Slash commands and skills merged in Claude Code v2.1.101.** Slash commands now defined as skills with `disable-model-invocation: true` + `user-invocable: true` + `agent: <subagent>`. Roadmap depends on v2.1.101+ from V19 onwards.
- **V18 nearly became a research session.** Opus did the research live during V17, so V18 was promoted to the first real build session.

**Carried forward.**

- All plugin construction work — distributed across `V18.md` through `V27.md`.
- Risk of method instability during migration: explicitly accepted at V17 close. The plugin's per-component context isolation is the testability fix, not a freeze of an unstable method.
