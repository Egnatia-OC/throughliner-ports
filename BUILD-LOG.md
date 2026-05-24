# Build log

Running record of decisions, changes, and reasoning. Newest first. Written for a friend skimming — half a page per session, less when possible.

For format details, see `BUILD-METHOD.md` → *BUILD-LOG entry shape*.

---

## v68 — 2026-05-24 — Rename "Crash course" to "Reference manual"

**What shipped.** Scope 0061. `Crash course.md` renamed to `Reference manual.md` via `git mv`. All live references updated across 11 files: BUILD-LOG.md, BUILD-METHOD.md, PLAN.md, INVENTORY.md, README.md, plugin/README.md, CLAUDE-TEMPLATE.md, project-level CLAUDE.md, 0069 scope file, permission-prompt-surface-audit.md research file. URL-encoded links (`Crash%20course.md`) updated in both READMEs. H1 heading updated. Archive/ untouched (read-only). Doc-only; no footer bump.

**Decisions.** Renamed historical BUILD-LOG and PLAN.md references too — the log is a working reference, not a legal record, and mixed terminology makes grep harder. PLAN.md row for 0061 retains both old and new names (describes the rename action).

**Pivots.** None.

**Carried forward.** 0062 (HTML guide) depends on this rename being complete — now unblocked.

---

## v67 — 2026-05-24 — Desktop app install/update documentation

**What shipped.** Scope 0067. Reference manual rewritten for desktop-app plugin management: *Install* expanded into four subsections (first install, version check, updating, troubleshooting stale `--plugin-dir` versions). *Managing the plugin* reframed with desktop app toggle as primary path. Uninstall stays CLI-only (#52456). Doc-only; no footer bump.

**Decisions.** No footer bump — documentation accuracy improvement, not method/plugin behaviour change.

**Pivots.** None.

**Carried forward.** Nothing.

---

## v66 — 2026-05-24 — Permission prompt surface audit

**What shipped.** Scope 0066. Root cause: subagents don't inherit parent permission mode (platform bug #28584, #40241, #18950). Mitigations: (a) replaced `allocate_number.py` Bash calls with Glob-based allocation in all five subagents; replaced `git status/diff` MANIFEST detection in after-build with batch Files-list detection; (b) Reference manual updated — Auto recommended for Build/After-build, platform bug documented with issue links. DOC-STRUCTURE, INVENTORY updated. New `research/permission-prompt-surface-audit.md`. Footer V58→V59; plugin 0.58.0→0.59.0.

**Decisions.** Glob-based allocation because every subagent Bash call generates a prompt due to the inheritance bug. Script remains for dev-side use. Auto recommended for Build/After-build (highest Bash volume).

**Pivots.** Planning subagent lacks Bash in `tools:`, so drift check 1 can't actually run — noted, not in scope. `allocate_number.py` removal touched 7 files (more than expected).

**Carried forward.** Planning drift-check-1 feasibility. All deferred smoke tests → 0068.

---

## v65 — 2026-05-24 — Memory-routing and research-filing rules

**What shipped.** No scope file. Two rules added to `universal-behaviour.md`: (1) "Route information to artifacts, not memory" — if you can name the destination, write it there. (2) Research-filing made mandatory (was advisory). New `research/memory-write-hook-feasibility.md` — auto-memory writes bypass PreToolUse entirely (#44820 closed as not planned); prose rules are the only viable enforcement.

**Decisions.** Mechanical enforcement investigated first — dead end (memory writes don't use Write tool). Prose rules are the fallback.

**Pivots.** V56 project-boundary check would block memory writes only if they used Write — they don't.

**Carried forward.** Nothing.

---

## v64 — 2026-05-24 — Project-boundary PreToolUse hook

**What shipped.** Scope 0065. New PreToolUse check (g) — blocks Edit/Write/MultiEdit outside project root. Fires before all other writing-tool checks. Mode-aware deny with `[No-code method]` prefix. 5 new tests (152 total, zero regressions). INVENTORY, Reference manual, BUILD-METHOD updated. Footer V57→V58; plugin 0.57.0→0.58.0.

**Decisions.** Bash not blocked — parsing shell syntax for file targets is unreliable; Edit/Write/MultiEdit have explicit paths. Check placed before locked_map build to short-circuit early.

**Pivots.** None.

**Carried forward.** Bash boundary enforcement as open idea. Deferred smoke tests → 0068.

---

## v63 — 2026-05-24 — /setup case 4 completion

**What shipped.** Scope 0064. Two `/setup` case 4 gaps from 0060 E2E: (1) BUILD-LOG folder migration — detects flat file, creates `build-log/` with INDEX.md + per-build files, updates path block. (2) Batch stub quality — broadened pre-V47 detection, extracts original prose as Goal content instead of placeholder. Non-blocking wording (no square brackets). 147 tests pass. Footer V56→V57; plugin 0.56.0→0.57.0.

**Decisions.** Non-blocking placeholder wording over omitting scope sections — before-build benefits from knowing what's missing vs present. Square brackets were the specific problem (pattern-match as template content).

**Pivots.** None.

**Carried forward.** Reference manual case 4 description predates V38 footer-stamp carve-out — flagged for future doc sweep. Deferred smoke tests → 0068.

---

## v62 — 2026-05-23 — Subagent efficiency pass

**What shipped.** Scope 0063. Efficiency instructions added to all five subagents (E2E findings: setup ~163k tokens, planning ~75k+). Three patterns: (1) Classify before loading — setup defers doc reads until after case detection. (2) Doc-first ordering — planning reads UX/BACKLOG before exploring code; before-build/after-build initial reads trimmed; batch-executor scoped to Files list. (3) No inner agent spawning — explicit prohibition in all five bodies. All 147 tests pass. Footer V55→V56; plugin 0.55.0→0.56.0.

**Decisions.** Doc-only (instructional guardrails, not mechanical enforcement). Mechanical enforcement can't distinguish main-Claude from subagent actions. Planning doc reads not deferred (drift checks need them) — fix targeted doc-first ordering instead.

**Pivots.** The E2E inner-agent spawn may have been main Claude misattributed to the subagent (planning lacks Agent tool). Added prohibition regardless.

**Carried forward.** V56 efficiency verification added to 0068 deferred tests.

---

## v61 — 2026-05-23 — Taskflow E2E prep and testing

*Entry written in v62 — v61 shipped 0060 but context ran out before BUILD-LOG was written.*

**What shipped.** Scope 0060. First real-project E2E test of the plugin against Taskflow. Nine findings surfaced across setup, planning, and session management. Six new scopes created (0063–0068) to address gaps found. Graduation (scope 0059) shelved indefinitely — context in OPEN-QUESTIONS.md. Reference manual gains "sessions are stateless" paragraph. Pre_tool_use.py Windows em-dash fix committed.

**Decisions taken and why.** Graduation shelved because the E2E findings showed the plugin needs more iteration before it's ready for public distribution. The six new scopes address concrete gaps found during testing. The E2E approach (run plugin against Taskflow in a desktop-app burner session, bring observations back to this project) validated as a testing method.

**Pivots and surprises.** Token costs far higher than expected — setup at 163k tokens, planning at 75k+ for a scope-existence check. Prompted scope 0063 (this session's work). Windows em-dash encoding in pre_tool_use.py was a platform-specific bug not caught by tests.

**Carried forward.** All nine E2E findings tracked via scopes 0063–0068. 0060 scope file kept (not deleted at v61 close) because downstream scopes reference its findings.

---

## v60 — 2026-05-23 — Session performance tracking

**What shipped.** Scope 0058. Performance section added to per-build files. Five mechanical measures (completion status, files count, carve-outs, Claude-verified tests, user-verified pending) plus optional user Session notes. After-build, DOC-STRUCTURE, VOCABULARY, INDEX template, Reference manual, BUILD-METHOD, INVENTORY updated. OPEN-QUESTIONS entry removed. 147 tests pass. Footer V54→V55; plugin 0.54.0→0.55.0.

**Decisions.** Collocated in per-build files (already exist, after-build already writes them) over separate folder or conversation-only capture. Mechanical measures only — "without a mechanical success criterion, 'well' becomes vibes-encoded-as-data."

**Pivots.** CLAUDE.md was two sessions stale — fixed at close.

**Carried forward.** V55 Performance section added to deferred smoke tests.

---

## v59 — 2026-05-23 — Subagent rule-loading convergence

**What shipped.** Scope 0057. Converged batch-executor on read-spec-on-entry pattern (was the sole outlier with inlined rules). Now reads DOC-STRUCTURE.md at runtime like the other three subagents. Removed trailing "Spec references" section. OPEN-QUESTIONS entry removed. INVENTORY updated. 147 tests pass. Footer V53→V54; plugin 0.53.0→0.54.0.

**Decisions.** Read-on-entry over inline: specs changed every version V50–V53, inlined copies would silently drift. Runtime overhead marginal (already reads 5+ docs per invocation). Setup excluded (doesn't use DOC-STRUCTURE/VOCABULARY).

**Pivots.** None.

**Carried forward.** V54 batch-executor verification added to deferred tests.

---

## v58 — 2026-05-23 — TEST-LOG row pruning

**What shipped.** Scope 0056. Planning subagent now prunes TEST-LOG rows whose Component no longer exists in MANIFEST + legacy Superseded rows, before drift checks. Cross-component rows exempted. DOC-STRUCTURE, VOCABULARY, Reference manual, INVENTORY, BUILD-METHOD updated. 147 tests pass. Footer V52→V53; plugin 0.52.0→0.53.0.

**Decisions.** Component-based pruning (cleanest signal). Deleted outright — git history preserves them; archive file would grow without bound. Placed at planning step 2c (not after-build) since planning already reads MANIFEST.

**Pivots.** Scope file leaned toward archive; pushed back, user accepted deletion. BUILD-METHOD stale reference caught at close.

**Carried forward.** Deferred tests unchanged. OPEN-QUESTIONS entry removed.

---

## v57 — 2026-05-22 — New hook events (compaction guard + opener routing)

**What shipped.** Scope 0055. Two new hook events: (1) PreCompact hook (`pre_compact.py`) — blocks compaction during active builds, surfaces paste-ready handoff prompt. Silent when no active build. (2) UserPromptSubmit hook (`user_prompt_submit.py`) — keyword-based first-prompt classification (setup/test notes/resume) as routing hint. Conservative thresholds; transcript-marker first-prompt detection. Session handoff protocol added to `universal-behaviour.md` (4-step process). Hook-assisted classification added to routing table. Doc-code parity across DOC-STRUCTURE, VOCABULARY, Reference manual, INVENTORY. "Six prose directives" OQ fully resolved. Footer V51→V52; plugin 0.51.0→0.52.0. Tests: 17 new (6+11); suite 147 passed.

**Decisions.** PreCompact can't inject `additionalContext` (platform limitation) — reframed to block+handoff instead of context preservation. Handoff notes in batch itself (already carries tick state). UserPromptSubmit uses transcript-marker for first-prompt detection (same V39 pattern).

**Pivots.** Scope assumed PreCompact could inject context — research disproved. Complete design reframe.

**Carried forward.** Deferred smoke tests unchanged from v56.

---

## v56 — 2026-05-22 — Validation + warnings bundle

**What shipped.** Scope 0054. Four "six prose directives" items plus `[FOLD-IN PENDING]` → `[PROPOSED EDIT PENDING]` rename. (1) `Serves <DOC>:` validation extended to all path-block docs (matches against `##` headings, excludes structural sections). (2) Red flags non-empty warning at SessionStart. (3) Deferred build-material aging in planning subagent (folder-mode batch-number comparison). (4) Rename across all live plugin files. Footer V50→V51; plugin 0.50.0→0.51.0. 8 new tests. Scope 0060 created.

**Decisions.** Additional-doc entries match `##` headings (additional docs use `##`, unlike UX.md's `###`). Structural sections excluded via frozen set. Rename bundled because all four items touched the same files.

**Carried forward.** Deferred smoke tests unchanged. "Six prose directives" items 2–4 resolved; 5–6 remain (→0055).

---

## v55 — 2026-05-22 — Automated test suite for dev project

**What shipped.** Scope 0053 (dev-internal, no method bump). Pytest suite at `tests/`: 124 tests, 2.7s, zero failures. 8 test files covering all hooks + shared helpers. 6 fixture directories (empty, tier2 variants, adopted folder/single-file, unadopted-with-work). BUILD-METHOD updated with test-suite section. OQ "Automated testing / CI" resolved.

**Decisions.** Subprocess-based tests (same stdin/stdout protocol as Claude Code). Committed fixtures (deterministic, inspectable). Manual CI only.

**Pivots.** V38/V45 carve-out tests: locked-doc carve-outs pass but batch-boundary denies downstream (UX.md not on Files: list). Correct behaviour — confirmed by asserting deny reason is "not on batch" not "locked doc."

**Carried forward.** Deferred smoke tests unchanged from v54.

---

## v54 — 2026-05-22 — BUILD-LOG restructured to build-log/ folder

**What shipped.** Scope 0052. Replaced monolithic `BUILD-LOG.md` with `build-log/` folder (one file per build + `INDEX.md`). Same folder pattern as BACKLOG/ (V48). `/setup` scaffolds it. Path block key stays `"BUILD-LOG.md"` (changing would break parsing), value points to `build-log/INDEX.md`. Session identification updated across all hooks/subagents for folder mode with single-file fallback. Footer V49→V50; plugin 0.49.0→0.50.0.

**Decisions.** 3-digit numbers (fewer builds than BACKLOG batches). No case 4 migration (no consumer project has used the method yet). Bullet list for INDEX.md (matches BACKLOG/INDEX.md). Research cross-references by path, not embedded content.

**Carried forward.** Deferred smoke tests accumulating (V43–V50) — all testable in one desktop-app burner session.

---

## v53 — 2026-05-22 — Research folder convention + Sonnet-search reword

**What shipped.** Scope 0051. (1) `/setup` scaffolds `research/` folder; all "prompt user for Sonnet search" language replaced with "research directly, save to `research/<topic>.md`." (2) New `research/` folder spec in DOC-STRUCTURE.md + VOCABULARY entry. Updated universal-behaviour.md (verify-external-facts rule), Reference manual, scaffold script, setup subagent. Footer V48→V49; plugin 0.48.0→0.49.0.

**Decisions.** Free-form kebab-case naming (research is reference, not sequence). Brief one-sentence chat mention when writing research. `[UNVERIFIED: <what>]` fallback when tools unavailable.

**Pivots.** Only two files had Sonnet-search language (universal-behaviour, Reference manual). Session spanned two context windows.

**Carried forward.** Deferred smoke tests (V43–V51). OQ V51 entry removed.

---

## v52 — 2026-05-22 — ADR-style numbering + per-batch BACKLOG file-split

**What shipped.** Scope 0050. Two structural overhauls: (1) dev-side scope files renamed `V*.md` → `NNNN-kebab-title.md` (0051–0059 created); (2) consumer-side BACKLOG split into `BACKLOG/` folder with `INDEX.md` + per-batch `NNNN-batch-name.md` files. Shared `allocate_number.py`. All hooks updated for folder-aware BACKLOG (`is_backlog_file()`, `resolve_backlog_dir()` in `project_state.py`). Parser auto-detects folder vs single-file. `/setup` case 4 migrates. All subagents updated. BUILD-METHOD updated with triple-distinction (session tag / scope-file number / method version). Footer V47→V48; plugin 0.47.0→0.48.0.

**Decisions.** Combined dev+consumer in one session (shared `allocate_number.py` concept). 4-digit zero-padded (ADR convention). INDEX.md not README.md (no GitHub collision). Numbers frozen at allocation. Legacy single-file kept working via parser fallback.

**Pivots.** Spanned two context windows. `stop.py` docstring edit failed string match — skipped.

**Carried forward.** Deferred smoke tests (all previous + V48 folder-split). OQ "Red-flag / threat-class marker" UX.md half unscheduled.

---

## v51 — 2026-05-22 — Consumer-batch structure overhaul

**What shipped.** V49 scope. Five scope-context sections added to BACKLOG build batches (Goal, Outputs, Success criteria, Decisions, Dependencies) plus conditional Red flags sub-section and `Changes:` delimiter separating scope-context from build-operations. Template placeholder cleanup (item 6): example batches → HTML-comment format specs. `/setup` case 4 detects old-format batches and inserts stubs. Parser updated with backwards-compatible `Changes:` support. DOC-STRUCTURE fully rewritten for batch structure. VOCABULARY gains 5 entries. All subagents and Reference manual updated. Footer V46→V47; plugin 0.46.0→0.47.0.

**Decisions.** `Changes:` delimiter (not scope-context fence) — cheaper, robust, backwards-compatible. Red flags auto-detected conditional (planning detects security-shaped scope). HTML-comment format specs in template (no diff noise). Case 4 stubs: Goal/Outputs/Success only (Decisions/Dependencies/Red flags are conditional).

**Pivots.** PowerShell mangled Unicode in inline parser tests — wrote proper `test_parser.py`. Session spanned two context windows.

**Carried forward.** UX friction 6/7 resolved. "Red-flag / threat-class marker" partially resolved (batch-level shipped; UX.md marker remains). Deferred smoke tests (V43–V49).

---

## v50 — 2026-05-22 — Automated vs. manual test split + non-UI test types

**What shipped.** V48 scope — biggest method change since V27. Four test types (Look and click, Run and read, Trigger and observe, Generate and inspect). Per-row Claude/User verifier split. 10-column TEST-LOG (adding Type + Verifier, renaming User Notes→Notes). Tests: sub-section in BACKLOG batches. Claude-automated test execution in after-build. Two-section recap ("Claude verified" / "Please check"). Commit/tag prompt (UX friction item 5). Backwards-compatible: shared regex handles 10- and 8-column; case 4 backfills. Extracted shared `parse_test_log_rows` from session_start.py into project_state.py (caught real bug — 8-column regex misparsed 10-column rows). Footer V45→V46; plugin 0.45.0→0.46.0.

**Decisions.** Tests in after-build (not batch-executor) — keeps build/test boundary clean. Verifier per-row (not per-type) — same test type can be structural or judgement. Optional regex group for backwards compat.

**Pivots.** Frame-correction sweep caught session_start.py misparse: 8-column regex on 10-column rows assigned Verifier to `confirmed_explicitly`, falsely flagging all rows.

**Carried forward.** OQ "test split" removed. UX friction 5/7 done. "Graduate" prerequisite 2 shipped (3/4 done).

---

## v49 — 2026-05-22 — Non-GUI vocabulary generalisation + planning/plan-mode disambiguation

**What shipped.** V47 scope (bundled). (1) "user-observable behaviours" → "observable behaviours" across all plugin-side docs (12 instances). Non-GUI guidance paragraph added to DOC-STRUCTURE.md (CLI tools, backends, plugins adapt "user" and "experience" concepts). (2) "Planning session (not plan mode)" vocabulary entry. Per-phase permission-mode table in Reference manual. Researched programmatic mode switching — confirmed impossible from hooks. Footer V44→V45; plugin 0.44.0→0.45.0.

**Decisions.** "Observable behaviours" (not "outcomes" or "testable") — keeps existing term, drops GUI assumption. Vocabulary note (not full rename of planning phase) — lower cost, direct fix. Guidance paragraph (not new non-GUI template) — preserves UX.md as universal spine.

**Pivots.** Alex proposed programmatic plan-mode during planning — research disproved. Per-phase table was the outcome. Frozen repo-root docs retain old phrasing (correct per V39 freeze).

**Carried forward.** Two OQ entries resolved.

---

## v48 — 2026-05-22 — BACKLOG.md PostToolUse parse validation hook

**What shipped.** V46 scope. New PostToolUse hook (`post_tool_use.py`) — first use of PostToolUse. Fires after Edit/Write/MultiEdit on BACKLOG.md (resolved via path block). Direct-imports `find_top_unticked_batch` from parser (no subprocess). Heuristic: unticked file bullets exist but parser returns `{}` → format broken → `additionalContext` warning. Template placeholders excluded. Full-file search (catches corrupted headings). Footer V43→V44; plugin 0.43.0→0.44.0.

**Decisions.** Direct import (not subprocess) — fires on every write, must be fast. Full-file search (not section-bounded) — catches corrupted `## Build batches` headings. Non-blocking warning via `additionalContext` (PostToolUse can't deny).

**Carried forward.** OQ "Six prose directives" item 1 resolved; items 2–6 remain. Smoke test deferred.

---

## v47 — 2026-05-22 — Distributed fold-ins + BACKLOG open-questions + batch Inputs line

**What shipped.** V45 scope. Three structural changes: (1) Fold-in blocks moved from centralized BACKLOG section to `## Fold-ins pending` at bottom of each destination doc (UX.md, MANIFEST.md, etc.). PreToolUse gained `is_fold_in_section_edit()` carve-out (same pattern as V38 footer carve-out). Templates updated. (2) Open questions section in BACKLOG — fourth section, non-blocking parking. Planning scans every session. (3) Batch `Inputs:` line — optional list of non-standard resources. Before-build populates; batch-executor reads. Footer V42→V43; plugin 0.42.0→0.43.0.

**Decisions.** Fold-in sections at end-of-doc (simple position detection). Open questions coexist with planning batches (different lifecycles — non-blocking vs blocking). No BACKLOG fold-ins section (BACKLOG is writable). Planning handles migration from old centralized location. Inputs between change list and Files (natural reading order).

**Pivots.** Context compaction mid-session (no work lost). Two extra subagents needed fold-in updates beyond scope.

**Carried forward.** Fold-in carve-out smoke test deferred. Reference manual stale `NO-CODE-METHOD.md` reference noted (pre-existing).

---

## v46 — 2026-05-22 — /setup UX + per-project opt-out

**What shipped.** V44 scope. (1) `.no-code-method-skip` marker removed from public plugin — opt-out now via Claude Code's `/plugin` toggle. Dev-project marker stays as `_LEGACY_SKIP_MARKER`. (2) `/adopt` renamed to `/setup` across entire plugin surface (skill dir, subagent, all references). (3) Three UX friction items: jargon→plain English, next-action prompts in recaps, Pass/Fail/Skipped explanations in read-back. V46 scope (cd marker walk-up) closed — marker removal made it moot. Permission-prompt surface researched (no marketplace vs `--plugin-dir` difference). Footer V41→V42; plugin 0.41.0→0.42.0.

**Decisions.** Marker removal before rename (simpler diffs). V46 closed (walk-up pointless for one legacy marker). Internal function names kept (`detect_adopt_case` etc. — never user-facing). CLI/desktop parity deferred (needs hands-on testing).

**Pivots.** Context ran out mid-session (after marker removal, before rename). Continuation clean. UX friction 4/7 resolved; 3 remain.

**Carried forward.** CLI/desktop parity testing. Remaining UX friction items 3, 5, 6. Smoke tests deferred.

---

## v45 — 2026-05-22 — Permission-mode UX harmonization

**What shipped.** Mode-aware deny messages across all 7 PreToolUse deny paths. Every deny: `[No-code method]` prefix + `What to do:` closing. 4/7 paths add mode-aware suffix in permissive modes (changing permission mode won't help). 3/7 get format standardisation only (sequencing issues, not mode-sensitive). `permission_mode` read defensively; absent values produce no suffix. SessionStart prepends two-layer-permission preamble. Reference manual gains *Two layers of permission*. Footer V40→V41; plugin 0.40.0→0.41.0.

**Decisions.** Format standardisation bundled (identity signal in every deny). Zero behaviour changes (plan-mode defer and MANIFEST allow-with-context both deferred — platform gaps). Substring mode detection (exact enum values unverified).

**Pivots.** Context compaction mid-session (no work lost).

**Carried forward.** Smoke test deferred (each deny path × two modes). Plan-mode hook firing unverified. V45 forward dependency: fold-in carve-out needs its own `[No-code method]` message.

---

## v44 — 2026-05-22 — Consumer-batch structure ideation + V49/V50 scoping

**What shipped.** Dev-internal ideation. (1) Interrogated which V-file scope sections propagate to consumer batches. Five landed (Goal, Outputs, Success criteria, Decisions to make this batch, Dependencies). Risks scoped out (degrades to hand-waving for non-coders). Re-framing: consumer batches skew V-file-sized because non-coders absorb ideas mid-stream. (2) ADR-style numbering (`NNNN-kebab-title.md`) confirmed as fix for V-numbering churn. Scoped as V49 (batch structure) then V50 (file-split + numbering). New OQ: red-flag/threat-class marker.

**Decisions.** V49 before V50 (structure first, file-split after). Retroactive rename in V50 (cleaner than partial cutover). No slash command for session creation. Risks section scoped out. Red-flag concern parked separately.

**Pivots.** Alex pushed back on "smaller consumer batches" — recalibrated to five sections. Reference manual "absorbs mid-stream ideation" section surfaced as V49 deliverable.

**Carried forward.** V49 and V50 await build. Red-flag/threat-class OQ awaits trigger.

---

## v43 — 2026-05-22 — Permission-mode research + roadmap rescope V43–V48

**What shipped.** Dev-internal. Research confirmed PreToolUse hooks fire in every permission mode — `permission_mode` in hook JSON, deny blocks regardless. Resolves OQ item 4 (method lock complementary to Claude Code's permissions, not redundant). Motivated new V43 (permission-mode UX harmonization). Roadmap renumbered V43–V48: old V43→V47, V46→V48, V47→V46. Cross-references updated.

**Decisions.** Permission-mode session at V43 (UX gap affects every user from day one). Vocab sweep displaced to V47 (V48 depends on it).

**Pivots.** Opened expecting vocab sweep. Alex redirected to permission-mode research. Answer clear enough for full session scope.

**Carried forward.** UX friction items 1, 2, 5, 6, 7 as candidates for V44. Item 3 tied to V45.

---

## v42 — 2026-05-21 — Git-diff drift detection + direct-edit confirmation protocol

**What shipped.** New drift check 1 (direct-edit detection) in planning subagent. Runs `git diff <last-tag>...HEAD` + working-tree diff at planning start. Files in previous batch's Files: list and writable surface pass silently. Everything else triggers per-file confirmation walk (path + summary + MANIFEST entry → "Was this you? Yes / No / not sure"). Yes → check conflicts, accept or queue fold-in. No → pause. Existing checks renumbered 2–5. Parity sweep across VOCABULARY, DOC-STRUCTURE, after-build, Reference manual, INVENTORY. OQ "direct-edit users" removed. Footer V39→V40; plugin 0.39.0→0.40.0. Repo-root docs frozen at V39.

**Decisions.** Numbered as check 1 (execution order = listing order). Per-file walk always (no threshold — bulk-confirm is the failure mode). No-tag fallback: diff working tree vs HEAD. Standard fold-in blocks (no thinner shape needed). No new Required behaviour (concrete procedure, not abstract principle).

**Carried forward.** Smoke test pending (scratch fixture with manual edits). `pre_tool_use.py` NO-CODE-METHOD.md citations unfixed.

**Smoke-test instructions.** git init → scaffold → build → tag → manual edit outside Claude → reopen → verify drift check 1 fires with per-file walk.

---

## v41 — 2026-05-21 — Rescope OPEN-QUESTIONS into V45–V47

**What shipped.** Dev-internal rescoping (pattern: V31). Three OQ entries scoped into V45 (distributed fold-ins + open questions + Inputs line), V46 (test split + non-UI types), V47 (cd-cwd marker fix). Existing V41–V43 renumbered to V42–V44. PLAN.md, OQ, CLAUDE.md updated. Meta-goal prerequisites all scheduled; graduation promotable after V46 + verification.

**Decisions.** V45 before V46 (V46 needs V45's Inputs: line). V47 separate from V44 (different concerns; V44 already heavy). Renumbering applied post-fix (collision caught: session tag v41 consumed V41 slot).

**Pivots.** Shipped without renumbering initially; Alex caught the collision. Fix followed V31 precedent.

**Carried forward.** No scope file (ad-hoc). `pre_tool_use.py` NO-CODE-METHOD.md citations unfixed.

---

## V40 — 2026-05-21 — Shelve the two-write rule for canonical docs

**What shipped.** Dev-internal. V32 two-write rule shelved. Repo-root prose docs (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`) and `templates/` frozen at V39 with FROZEN notices. Plugin-side becomes sole operational source. Method version stays V39. BUILD-METHOD's two-write section annotated as shelved. Project CLAUDE.md, README, plugin-side references, INVENTORY, OQ, PLAN.md all updated. Scope files renumbered (V40→V41, etc.).

**Decisions.** Freeze (not archive or delete) — lowest blast radius, resume path is one OQ promotion away. Annotate BUILD-METHOD section in place (resume-ability). Own session (not folded into drift-detection — one tag at a time). Method version stays V39 (dev-internal, no method substance).

**Pivots.** CLAUDE-TEMPLATE references `NO-CODE-METHOD.md` — adjusted to "frozen prose snapshot." `pre_tool_use.py` still cites `NO-CODE-METHOD.md` at 4 sites — flagged, not fixed. V42 bundling rationale dissolves (only plugin side now) — note added.

**Carried forward.** `pre_tool_use.py` citations unfixed. Three pre-v40 OQ entries committed alongside (part of same thinking arc).

---

## V39 — 2026-05-21 — MANIFEST paths field + read-before-edit hook gate

**What shipped.** Optional `(path)` field on MANIFEST entries (three shapes: single, list, directory). PreToolUse check (6): denies first edit on MANIFEST-covered file with inline context; retries allowed via transcript-scan marker. Spine docs exempt. After-build populates paths on touch (incremental migration). Rule rewritten from "check first" to "have context by edit time." OQ resolved. Smoke-tested: 7 cases Pass (#116–122). Footer 38→39; plugin 0.38.0→0.39.0.

**Decisions.** Shape B (transcript-as-state) over shape A (state file + cross-hook). Half the implementation, same guarantee. Paths optional (no flag-day for mid-flight projects). Three shapes cover single/list/directory without forcing artificial granularity.

**Pivots.** Bash `cd` shifted plugin cwd mid-session — adoption gate fired against dev project. Recovered with second `.no-code-method-skip` at `sovereign-implementer/` root. New OQ logged for cwd-shift issue.

**Carried forward.** New OQ (cd-shifts-cwd). `.no-code-method-skip` at repo root committed.

---

## V38 — 2026-05-21 — Locked-doc edit rules + Sonnet-search discipline

**What shipped.** Three discipline changes resolving three OQ entries. (1) Footer-stamp carve-out: `is_footer_only_edit()` + regex lets footer-only `Edit` calls pass locked-doc check (`Write`/`MultiEdit` still blocked). (2) Preview-then-fold-in convention: subagents preview SOT edits in chat, get approval, write fold-in block, prompt immediate fold-in. (3) Verify-external-facts rule: web-search or paste-ready Sonnet prompt; fallback `[UNVERIFIED: <what>]`. Three OQ entries removed. Footer 37→38; plugin 0.37.0→0.38.0.

**Decisions.** Preview convention (not planning-context carve-out) — hook can't identify caller, so lock stays intact. `[UNVERIFIED]` as fallback (not hard block) — user can't always run searches. Footer carve-out Edit-only (Write/MultiEdit too broad to verify).

**Pivots.** adopt.md case 4 recap template stale — caught in parity audit. Context ran out mid-session (resume accurate).

**Carried forward.** No smoke test (needs consumer build cycle).

---

## V37 — 2026-05-21 — Marketplace.json + local install + first globally-installed smoke test

**What shipped.** `.claude-plugin/marketplace.json` — single-plugin marketplace (`sovereign-implementer`, owner `FlintCraftTech`, relative source `./plugin`). Works for both local install and public distribution. Local install via `claude plugin marketplace add ./` + `claude plugin install`. Smoke test against empty folder (no `--plugin-dir`): tier 1 silent, hooks registered, `/adopt` case 1 fires, `/reload-plugins` loads full surface (1 plugin · 2 skills · 11 agents · 4 hooks). TEST-LOG #109–115. README updated (install instructions, license corrected to PolyForm Noncommercial). Footer 36→37; plugin 0.36.0→0.37.0.

**Decisions.** Marketplace name matches repo. No version in marketplace.json (`plugin.json` authoritative). Description added after validation warning.

**Pivots.** `/hooks` shows only PreToolUse for globally-installed (vs 3 event types for `--plugin-dir`) — cosmetic gap, hooks fire correctly. `claude -p` misfire (sends prompt, not project dir) — corrected to `cd` + `claude`.

**Carried forward.** OQ entries unchanged.

---

## V36 — 2026-05-21 — OPEN-QUESTIONS doc-only bundle: TEST-LOG newest-first, BACKLOG authority, plan-panel resolved

**What shipped.** Three doc-only items + method-version catch-up (34→36, skipping 35). (1) TEST-LOG flipped to newest-first across DOC-STRUCTURE, templates, after-build, planning. Transition stance for existing rows. (2) BACKLOG-authority sentence in planning.md (not universal-behaviour.md — scope file was wrong, caught at edit time). (3) Plan-panel resolved: research confirmed not programmatically writable. Collapsed to Reference manual caveat pointing at BACKLOG for build sequence. OQ entry removed. No smoke test (doc-only). Parser ordering-agnostic — no code change needed.

**Decisions.** BACKLOG-authority in planning.md (phase-specific, not cross-phase). Plan-panel as caveat (not standalone section). Footer 34→36 (V35 dev-internal, didn't bump).

**Pivots.** Scope file named wrong target file — caught at edit time. Footer-bump parallelism hit Read-before-Edit requirement on 16 files.

**Carried forward.** V37 queued. 11 OQ entries parked. Plan-panel research file retained.

---

## V35 — 2026-05-21 — E2E Taskflow test — `/adopt` validated; planning-subagent first contact

**What shipped.** Dev-internal. First plugin run against real Taskflow (not synthetic). `/adopt` case 1 + case 4 refresh validated — footers bumped on writable docs, locked docs routed through fold-in. TEST-LOG #104–108. Two new OQ entries (footer-stamp fold-in friction, /adopt permission-prompt UX). Marketplace path researched (`research/plugin-marketplace-scoping.md`): relative-path source works for both local and public. V37 scope created.

**Decisions.** Closes as planning/observational (not full E2E — plugin clashed with already-settled Taskflow decisions). No method bump (dev-internal). V37 as own session (marketplace packaging warrants clean smoke test). Local marketplace install over cache copying.

**Pivots.** Previous session blew up mid-planning-subagent (questions clashed with settled decisions). `/adopt` first run from home dir — subagent caught it (refused to scaffold in user profile). "Two configurations" framing was wrong — relative source works for both.

**Carried forward.** Full E2E cycle remains owed. V37 queued.

---

## V34 — 2026-05-21 — Consumer-method git workflow + OPEN-QUESTIONS promotion

**What shipped.** (1) Recommended habits line: "tag and push after every build." Windows `.git/index.lock` contention documented (manual `del` as recovery). (2) Git safety-guard hook (`pre_tool_use_git_guard.py`, Bash matcher) — denies `git reset --hard` and `git push --force`; allows `--force-with-lease` and all other git ops. 14 test cases (5 deny, 9 allow). Regex `\b` bug caught pre-ship. (3) V36 scope created (3 OQ items promoted). (4) Cowork drift cleanup (4 edits, 3 files).

**Decisions.** New file (not `pre_tool_use.py` extension) — different matcher, different concern domain. `--no-optional-locks` not viable (git flag, not Claude Code flag). `/git-discipline` skill deferred. Lock reproduction deferred.

**Pivots.** `\b` before `--flags` fails (space and `-` are both non-word chars) — caught by automated testing. Context compaction mid-session (clean).

**Carried forward.** Stop-hook auto-commit deferred. Lock contention deferred. `git-integration-research.md` consumed.

---

## V33 — 2026-05-20 — Consumer-side BUILD-LOG, planning/drafts/, and frame-correction sweep

**What shipped.** Three additions to consumer *After every build* (in after-build.md, mirrored in NO-CODE-METHOD.md): (1) BUILD-LOG.md as 6th spine doc — template, scaffold, after-build writes entry per build, path block updated. (2) `planning/drafts/` folder — destination-agnostic carryover, scaffolded by `/adopt`. 3 new VOCABULARY terms. (3) Frame-correction sweep (after-build step 6) — scan BACKLOG for old-behaviour references after substantive changes; BACKLOG only (UX.md caught by drift check 1). Parity sweep caught ~8 extra files beyond the 11-file plan.

**Decisions.** Both chat recap and BUILD-LOG entry (different audiences/lifecycles). Frame-sweep BACKLOG-only (UX.md caught elsewhere). Frame-sweep in after-build (build context freshest). Drafts as own DOC-STRUCTURE section (not sub-section).

**Pivots.** Context compaction (clean). Plan underestimated blast radius (11→~19 files — every new spine doc propagates widely).

**Carried forward.** Smoke test owed. NO-CODE-METHOD.md still uses plugin-specific phrasing (correct substance, wrong framing).

---

## V32 — 2026-05-20 — NO-CODE-METHOD.md retired from plugin; two-write architecture established

**What shipped.** Split canonical method into two parallel sets: plugin-side (operational) and docs-only (project-agnostic prose). `NO-CODE-METHOD.md` retired from plugin runtime — subagents stopped reading it; operating procedures inlined into subagent bodies (planning gained *Procedure order*, before-build gained *Batch-sizing* sub-rules, after-build already complete). `universal-behaviour.md` absorbed cross-cutting orphans (routing logic, Rule 1, Prohibited block, flag taxonomy, tags glossary, Editing surfaces). New `VOCABULARY.md` (plugin + docs-only mirror). All cross-references redirected. BUILD-METHOD gained two-write architecture section. Coverage map consumed. Footer V30→V32; plugin 0.32.0.

**Decisions.** Shape A (full retirement + inline) over trim or pointer — rules live in plugin, not docs read. Plugin leads, docs-only follows. VOCABULARY as own file (not lumped into universal-behaviour — different concerns).

**Pivots.** Previous chat glitched — memory carried framing decision into continuation. Scope file stale (pre-docs-only framing). Cowork mount truncations (twice). Bash `rm` blocked by ACLs. Subagent inline gaps larger than coverage map suggested — real procedural gaps surfaced in planning and before-build.

**Carried forward.** `NO-CODE-METHOD.md` deletion owed. Docs-only still uses plugin phrasing. Smoke test owed.

---

## V31 — 2026-05-20 — Planning: rescope OPEN-QUESTIONS into V33/V34; V32–V35 numbering shifted

**What shipped.** Rescoping session (pattern: V20). Four OQ entries promoted into V33 (consumer audit trail + frame-sweep — three OQs combined, all touch *After every build*) and V34 (git workflow). Renames: V31→V32, V32→V35. PLAN.md and OQ updated. Four promoted entries removed; five remaining retargeted to V36+. 13 OQ entries remaining (from 17). Dev-internal — no footer bumps.

**Decisions.** Re-order (not append) — discipline before E2E testing. Three OQs combined into V33 (one doc sweep, one smoke test). Stop-hook auto-commit deferred (one user rolled it back). MANIFEST schema gap held honestly (heavy decision, consistently lower priority).

**Pivots.** Tag-numbering shift forced mid-session (BUILD-METHOD requires own tag). OQ entries' Working notes did most scope-design work — assembly, not invention.

**Carried forward.** Five OQ entries for V36+. Eight parked entries retargeted. Reference manual review parked.

---

## V30 — 2026-05-20 — Method docs relocated into plugin; Reference manual rewritten as standalone primer

**What shipped.** Doc relocation (`NO-CODE-METHOD.md` + `DOC-STRUCTURE.md` → `plugin/docs/` via `git mv`; subagent bodies updated to `${CLAUDE_PLUGIN_ROOT}/docs/...`). Reference manual fully rewritten as standalone primer (install + first session up front; planning-input paragraph tightened; Risk-accepted example corrected). Plugin README gains Reference manual link. NO-CODE-METHOD *Before build* closing prompt reframed defensively re plan mode. BUILD-METHOD gains *Graduation paths* sub-section for OQ entries. CLAUDE-TEMPLATE (×2) rewritten for plugin-bundled location. INVENTORY updated for new doc locations. V31/V32 scope files frame-corrected. OQ git-workflow entry refreshed with Sonnet web-search; `planning/drafts/git-integration-research.md` committed. Ten new OQ entries surfaced (five from retrospective, five from Reference manual review). 21 footers bumped V29 → V30; `plugin.json` → `0.30.0`.

**Decisions.** Bundled doc + sister-doc symmetry — DOC-STRUCTURE as reference doc, not skill body; scope expanded to relocate NO-CODE-METHOD alongside. Full Reference manual rewrite, not surgical — standalone-primer criterion required it. Reference manual stays at repo root — audience is humans, not plugin runtime.

**Pivots.** Subagent read-spec-on-entry was silently failing pre-V30 — `CLAUDE_PLUGIN_ROOT` substitution wasn't applied; relocation surfaced and fixed it. Git index corruption from bash mount + Drive sync; recovered via PowerShell `git read-tree HEAD`. Session split across two Cowork conversations (length limits). Ten OQ entries surfaced — largest blind-spots: no consumer-side BUILD-LOG, no git workflow, GUI-centric phrasing.

**Carried forward.** Ten OQ entries parked for V31+. Git-workflow research at `planning/drafts/`. Reference manual review pass parked pending OQ planning session. Next session is OQ planning, not V31 directly.

---

## V29 — 2026-05-19 — Safety net (SessionStart advisory + PreToolUse enforcement) + unified `/adopt`

**What shipped.** Two-hook safety net + unified `/adopt` skill-command (replaces `/new-project` + `/init-project` + `/migrate`; five folder-state branches). Smoke-tested across 5 fixtures; see TEST-LOG #071–089.

SessionStart gains unadopted-folder detection + `systemMessage` advisory. PreToolUse gains unadopted-folder gate (Edit/Write/MultiEdit + Task denied; `/adopt` calls pass through; self-clears on adoption). New `adopt.md` subagent (five-case dialogue; case-4 writable/locked classification fixed mid-session per #083). New `adopt/SKILL.md` + `scaffold.py`. Plugin README created. Reference manual gains safety-net section. NO-CODE-METHOD gains adoption-state vocabulary + detection rule. BUILD-METHOD gains frame-correction sweep step. 20 footers bumped V27 → V29; `plugin.json` → 0.29.0. Two OQ entries resolved. TEST-LOG #071–089 (one Fail, one Skipped; fixes applied, retests owed).

**Decisions.** Frame-correction sweep: option A (audit step) over B (shorten horizon) — cheap to run, preserves roadmap visibility. Template-reconciliation worker lives in `/adopt` case 4, not separate `/refresh`. Plugin README for "is plugin loaded" UX — `${CLAUDE_PLUGIN_ROOT}` doesn't expand in `settings.json`.

**Pivots.** PreToolUse gate is Edit/Write/MultiEdit only — Bash bypasses by design (threat model is accidental edits). Case-4 over-locked spine docs; fixed same commit. Case-4 walkthrough text possibly scrolled past (#089). V21 tripwire emits to `additionalContext`, not `systemMessage` — not user-visible.

**Carried forward.** TEST-LOG #083/#089 retests owed. Two `uploads/` files referenced in V29.md never committed — same failure mode as V20→V26 *Drafts in flight* incident. V21 tripwire user-visibility: code read pending.

---

## V28 — 2026-05-18 — V27 fix sweep: test-confirmation gate becomes functional

**What shipped.** Three V27 bugs fixed and live-tested end-to-end. PreToolUse `WRITABLE_LOGICAL_NAMES` extended with TEST-LOG.md (one-line fix unblocking the gate). New `project_state.py` shared module (helpers extracted from pre_tool_use.py + stop.py). Stop hook gains `is_test_session_open` check — defers batch redirect when previous-session rows unconfirmed. V28-prequel restructure renamed scope files V28→V32. Two OQ entries resolved. TEST-LOG #064–070, all Pass. Smoke-tested live against rebuilt `v27-smoke-fixtures/g4`. Alex's mid-session language-compaction pass across 9 docs folded into commit. **Footers NOT bumped** — V28 restores V27's intended behaviour.

**Decisions.** V28-prequel restructure over expanding V28's `/adopt` scope — fix foundation before building on it. Shared module named `project_state.py` in existing `plugin/scripts/`. Stop hook defers via silent exit, not redirect-to-planning — avoids re-invoking planning mid-read-back. Walkthrough-mode dropped — V27's after-build recap covers the use case.

**Pivots.** Cowork parallel-session corruption at open (phantom `.git/index.lock`; recovered via Explorer delete + `git reset --hard`). V27 fixture was unexpectedly empty; rebuilt 7 files with mtime ordering. Stop-hook V28 fix not uniquely distinguishable from natural fallthrough in test (#069 caveat). Compacted docs landed with `(1)` suffixes (Windows save-as artifact; renamed).

**Carried forward.** V27 Skipped rows #061/#062/#063 need narrower fixtures. Stop-hook unique-verification owed. PLAN.md ↔ scope-file numbering convention to enforce.

---

## V27 — 2026-05-17 — After-build subagent + test-confirmation gate hook + SessionStart TEST-LOG tripwire + [Requested]/[Suggested] labels in BACKLOG.md

**What shipped.** Test-confirmation gate wired end-to-end. New `after-build.md` subagent (MANIFEST update, labelled recap, test-session-open, idempotent). Batch-executor shed *After every build* responsibilities. Planning gains TEST-LOG read-back + inline label-writing. Before-build gains label-preservation rule. PreToolUse gains check (f): test-confirmation gate on Task → batch-executor. SessionStart gains TEST-LOG tripwire (routing override with row IDs). Stop hook gains after-build routing (BACKLOG.mtime vs TEST-LOG.mtime heuristic). `/build` command updated. DOC-STRUCTURE gains `[Requested]`/`[Suggested]` labels sub-section. NO-CODE-METHOD gains after-build handoff. Reference manual, INVENTORY, BACKLOG-TEMPLATE (×2), BUILD-METHOD updated. 19 footers bumped V26 → V27. Three V26 carry-forwards absorbed. **No smoke tests** — 13-check sweep owed post-commit.

**Decisions.** Labels live on change-list items, not Files: sub-section — a change touches many files; files-level labels would force arbitrary calls. Label work folded into V27 rather than split — files already in scope. Batch-executor must shed after-build responsibilities to avoid duplication. Stop-hook heuristic uses mtime comparison — robust to same-day second batches. TEST-LOG tripwire overrides routing, not just flags — necessary to pre-empt feature-request openers.

**Pivots.** Stale "NO-CODE-METHOD.md retired in V27" in INVENTORY — aspirational, not actual scope. Batch-executor's flags section needed restructuring post-recap-handoff. Reference manual's "hook is the gate" was aspirational at V26, now true.

**Carried forward.** Smoke testing owed. Helper-code duplication across hooks → extract to shared module in future session. Design-lock-first rhythm validated by Q3 category-error catch.

---

## V26 — 2026-05-17 — TEST-LOG.md mechanism + Drafts in flight convention + V25 carry-over bugfixes

**What shipped.** New consumer-side TEST-LOG.md doc class (8 columns, phase-based pruning) with templates (×2) and DOC-STRUCTURE spec. Five protocol rules placed across NO-CODE-METHOD phases. CLAUDE-TEMPLATE (×2) gains TEST-LOG in path block; scaffold.py extended. Reference manual: *Three disciplines* → *Four*. Three V25 carry-over bugfixes absorbed (#041/#042/#044; plus `/build` parser-path bug). Session-open recovery: CLAUDE.md gains inputs-must-be-in-repo scan rule; BUILD-METHOD gains *Drafts in flight* convention; `planning/drafts/` folder created. Parity audit: 17 edits across 8 files. 21 footers bumped V25 → V26. No smoke tests — doc-only on the gate.

**Decisions.** Rule 2 relocated mid-session from *After every build* to *During planning* — testing window spans sessions. Hybrid enforcement of Rule 3: hook is load-bearing gate, planning's read-back is the UX. Rule 5 "substantially changed" punted to Claude's judgement + reasoning trail. *Drafts in flight* convention added as recovery — V26.md cited an input that was never committed (V20→V26 failure).

**Pivots.** `/build` parser-path bug caught by carry-over sweep (project-relative path; plugin isn't in project tree). Pre-existing "5 templates" off-by-one coincidentally fixed by TEST-LOG addition. Parity audit surfaced more drift than expected.

**Carried forward.** Three code carry-forwards (SPINE_FILENAMES, PLUGIN_METHOD_VERSION comment, docstring count) → V27.

---

## V25 — 2026-05-17 — Build orchestration core: Stop hook + batch-executor + before-build + slash commands + spec rewrites

**What shipped.** Build orchestration core. New `parse_backlog.py` shared parser (top unticked batch → JSON; lenient on malformed; three call sites). New `stop.py` build sequencer (respects `stop_hook_active`). PreToolUse gains (c) batch file-list boundary. New `batch-executor.md` subagent (JSON payload in, tick-per-file, labelled recap, halt-and-confirm protocols; rules inlined). New `before-build.md` subagent (validate-only, read-spec-on-entry). `/before-build` and `/build` slash commands (newer commands-directory pattern). NO-CODE-METHOD *Before build* and *After every build* rewritten for subagent-aware flow; *Batch-sizing principle* added; four new Vocabulary entries. DOC-STRUCTURE, Reference manual, BACKLOG-TEMPLATE (×2), INVENTORY updated. Previous ideation edits bundled in. Four OQ entries added. 16 footers bumped V23 → V25. Pre-validation smoke tests (15/15 parser, 8/8 Stop, 9/9 PreToolUse); see TEST-LOG #031–033.

**Decisions.** Parity-audit escape clause overridden for *Before build*/*After every build* rewrites — spec gap was load-bearing for shipped subagents. Before-build: validate-only (reorganise dropped — planning owns BACKLOG since V22) + read-spec-on-entry (fresh rules likely to churn). `/build` argument-less — out-of-order handled by reordering BACKLOG in planning. Ideation edits bundled — `git add -p` cost outweighed clean-tag value.

**Pivots.** Validation via sister Sonnet session flipped two recommendations and dropped one halt scenario. "After-build subagent" was a ghost reference in INVENTORY — batch-executor had absorbed it. Slash-commands convention changed mid-roadmap (old skills pattern → newer commands pattern). Parser leniency (exit 0, `{}` on malformed) almost misread by `/build` draft.

**Carried forward.** Windows smoke test run 2026-05-17 → TEST-LOG #034–050; three bugs logged as OQ for V26. Subagent rule-loading divergence, MANIFEST schema gap, Stop-hook cap, `/plan` command all in OQ.

---

## V24 — 2026-05-16 — BUILD-METHOD.md and TEST-LOG.md added; session-tag and method-version decoupled

**What shipped.** New `BUILD-METHOD.md` (working manual lifted from CLAUDE.md + expanded). New `TEST-LOG.md` (30 backfilled rows from V18–V22). Project-root CLAUDE.md slimmed 240 → 100 lines. PLAN.md renumbered (V24 inserted; old V24–V30 → V25–V31). **No method-version footer bumps** — first session under dev-internal-doesn't-bump rule.

**Decisions.** BUILD-METHOD as new file, not CLAUDE.md restructure — working manual and orientation deserve separate homes. Session tag and method-version decoupled — old convention bumped even for doc-only sessions. TEST-LOG created now, not deferred to V26 — Alex pushed back; making test outcomes queryable fixes the "plugin never installed" assertion bug.

**Pivots.** Initial framing wasted a round-trip proposing live-install session — Alex corrected: tests exist, recording isn't visible. Footer-bump convention had quietly drifted across V20/V23. INVENTORY forward-pointers semantically stale after renumber.

**Carried forward.** V23 carry-forwards remain valid. INVENTORY forward-pointer audit deferred. V28.md/V31.md "live-install session" references superseded.

---

## V23 — 2026-05-17 — Remove Cowork mentions from method docs; Claude Code becomes explicitly required

**What shipped.** Cowork-removal sweep: NO-CODE-METHOD makes Claude Code explicitly required; Reference manual rewritten (two-phase framing, new-project-route walkthrough, single-column editing table); DOC-STRUCTURE, templates (×4), planning.md, pre_tool_use.py, session_start.py, init-project/SKILL.md all stripped. Dev-project CLAUDE.md left unspecified (Alex mid-migration). OQ prose-only-rewrite entry noted framing shift. PLAN.md renumbered. Footers V22 → V23; `plugin.json` → 0.23.0.

**Decisions.** Claude Code is required, not recommended — method ships as plugin, can't run elsewhere. Replacement wording "by hand during planning sessions" preserves fold-in mechanism while updating location. Dev-project CLAUDE.md unspecified — Alex has no fixed migration timeline. Internal planning artefacts left alone (historical record).

**Pivots.** Reference manual rewrite bigger than anticipated — "Where each tool fits" was load-bearing framing. "Edit by hand" introduces a soft discipline that didn't exist in Cowork era — user *can* now edit UX.md mid-build (only Claude's edits blocked). Cowork parallel-session corruption during prep (CRLF mangling; recovered via `git restore .`).

**Carried forward.** Live install + back-test of V18–V23 owed. Soft-discipline risk for mid-build SoT edits recorded. OQ cross-version entry still has Cowork vocabulary.

---

## V22 — 2026-05-14 — Planning subagent + Serves-line PreToolUse hook

**What shipped.** First subagent: `planning.md` (three planning flows, mixed-input sort, always-run drift checks, recap contract; tools: Read/Edit/Write/Glob/Grep only). PreToolUse gains Serves-line check (case-insensitive exact match against UX.md `### ` entries). NO-CODE-METHOD gains planning handoff + four `primary_intent` values; drift-check skip clause tightened. Reference manual, DOC-STRUCTURE, INVENTORY updated. INVENTORY D3 corrected (hooks inject context, can't launch subagents). OQ direct-edit-users shape #1 partially folded. 15 footers bumped V21 → V22.

**Decisions.** Main Claude classifies intent at handoff; subagent does mixed-input sort — keeps subagent prompt tight. Drift checks run every session; only skip is "nothing built yet" — skipping would defeat manual-edit detection. Serves-line matching: case-insensitive exact, no fuzzy — strict enough to catch skipped fold-ins. `/plan` not shipped — auto-route path required first.

**Pivots.** Web-search mid-build for subagent format surfaced key facts (`subagent_type` is `<plugin-name>:<agent-name>`; `agents/*.md` auto-register). INVENTORY ghost-commands caught mid-smoke-test — subagent recommended unshipped `/migrate`. Smoke-test auto-route couldn't run in Taskflow (tier 2; pre-V18 path block format).

**Carried forward.** Smoke test owed. `/plan` deferred. Direct-edit-users OQ shapes #2/#3 remain.

---

## V21 — 2026-05-14 — SessionStart hook extension: three-tier detection + foundational reads + footer tripwire

**What shipped.** SessionStart extended to ~280 lines: reads project root from stdin `cwd` (not broken `$CLAUDE_PROJECT_DIR`), parses CLAUDE.md JSON path block, reads spine + additional SoT docs, detects template state, detects unfinished batch, runs version-footer tripwire. Three-tier behaviour: Tier 1 (non-method folder) emits nothing; Tier 2 (partial method shape) emits universal rules + gap flag; Tier 3 (complete project) emits full state summary + routing reminder. 8 footers bumped V20 → V21; `plugin.json` 0.19.0 → 0.21.0. Dev-project CLAUDE.md gains Cowork-first lean, test-run guidance, "Which CLAUDE.md is which." Smoke-tested on Windows: all tiers verified; tripwire caught missed `plugin/templates/` footer bumps mid-test.

**Decisions.** Tier 1 emits nothing (behaviour change from V18 — plugin should be invisible in non-method folders). Route signal is prose, not structured marker. Tier-2 detection tightened via method-footer check (prevents false positives from unrelated BACKLOG.md). Tripwire half of cross-version reconciliation folded in; worker half stays in V26. `plugin.json` skipped 0.20.0 — aligning with method version.

**Pivots.** Workflow misframed early — Alex builds in Cowork, Claude Code only for smoke-testing. "Which CLAUDE.md is which" confusion pinned in project CLAUDE.md. Footer tripwire caught real oversight mid-smoke: `plugin/templates/` copies missed by footer-bump pass. Smoke test paid for itself with this catch.

**Carried forward.** Tier-2 detection may need tightening. Direct-edit-users OQ remains.

---

## V20 — 2026-05-14 — Reference manual promoted to source-of-truth doc; planning shifts

**What shipped.** Reference manual promoted to parity-tracked SoT doc (drift audit: fold-in mechanism, BACKLOG rationale, prerequisite carve-out, UX-conflict surfacing, file-location, editing-surfaces all corrected). Planning shifts: scope files V20–V27 renamed to V21–V29; new V24 for TEST-LOG; V23 absorbs batch-sizing. PLAN.md rewritten. New OQ: *Cowork-friendly prose-only rewrite*. 15 footers bumped V19 → V20.

**Decisions.** Reference manual earns SoT status but not by retrofitting unshipped scope-file content — plans are provisional. Cowork-first stays in spec for now — method IS Claude-Code-specific. TEST-LOG is operational (sibling of MANIFEST), not a new section — five rules distributed across existing NO-CODE-METHOD phases. Batch-sizing folds into V23 (before-build subagent session).

**Pivots.** Stale `.git/index.lock` on Linux mount blocked renames — workaround: plain `mv`, let git detect 100% content matches. Cross-version template reconciliation OQ framing weakened by new Cowork-rewrite entry.

**Carried forward.** Cowork-friendly prose-only rewrite in OQ. TEST-LOG mechanism → V24. Batch-sizing → V23.

---

## V19 — 2026-05-13 — PreToolUse hook + bundled templates + /init-project + Fold-ins pending section

**What shipped.** PreToolUse hook blocks Edit/Write/MultiEdit on locked SoT docs; redirects to `[FOLD-IN PENDING]` section in BACKLOG.md. Five templates bundled at `plugin/templates/`. New `/init-project` skill (scaffold script; refuses on non-empty, points at `/migrate`). Structural rewrites: BACKLOG-TEMPLATE (×2), DOC-STRUCTURE, NO-CODE-METHOD for fold-ins pending section. Smoke-tested on Windows: all paths verified.

**Decisions.** Templates at `plugin/templates/`, not inside skill — multiple consumers (init-project + future migrate). `/init-project` refuses on conflict, doesn't merge — half-scaffolding would silently mix sources. Hook denies with redirect message, not silent rewrite — "be told what's wrong" principle. `[FOLD-IN PENDING]` gets own top-level BACKLOG section — orphan blocks from multiple routes need one location.

**Pivots.** `${CLAUDE_PLUGIN_ROOT}` expands inside skill bodies — resolved uncertainty on first smoke try. V18's universal-behaviour rules self-policed before hook fired (Claude refused UX.md edit on its own; hook is backstop). Mid-smoke discovery surfaced missing `[FOLD-IN PENDING]` section in template → structural rewrite pulled into V19.

**Carried forward.** Cross-version template reconciliation raised as OQ. Windows subfolder-conflict test skipped (platform-agnostic `pathlib`).

---

## V18 — 2026-05-12 — Plugin scaffold + SessionStart hook + JSON path block

**What shipped.** Plugin scaffold: `plugin.json`, `hooks.json` with SessionStart hook, `session_start.py` emitting eight universal behavioural rules as `additionalContext`, rules text in `universal-behaviour.md`. CLAUDE-TEMPLATE path block changed from markdown bullets to fenced JSON for deterministic parsing. Smoke-tested on Windows: plugin loaded, hook registered, rules recited verbatim.

**Decisions.** Plugin in same repo (`sovereign-implementer/plugin/`) — method and code co-evolve. Python for hooks, not bash/Node — cross-platform, no profile contamination, readable for non-coders. JSON for path block, not YAML — stdlib, loud failures, no quoting gotchas.

**Pivots.** `UserPromptSubmit` hooks in plugins don't execute (#10225) — pivoted to SessionStart. `${CLAUDE_PLUGIN_ROOT}` doesn't quote paths with spaces — smoke test failed silently; fix: escaped quotes in `hooks.json`. Claude Code CLI wasn't installed — required PowerShell installer.

**Carried forward.** Escaped-quote pattern for all hook commands. Reference manual needs install instructions. BUILD-LOG.md added post-tag.

---

## V17 — 2026-05-11 — Plugin-migration architecture decided

**What shipped.** Plugin-migration architecture scoped end-to-end. Produced INVENTORY.md, PLAN.md (V18→V27 roadmap), Opus feasibility response. Scope files V18–V27 created. Versioning switched from numbered folders to git tags.

**Decisions.** Two-layer split: per-project SoT stays per-project; mechanical method becomes plugin — discipline becomes structural, not prompt-based. Stop hook proposes, user gates — single-step per prompt. Drift checks inlined into planning subagent — subagents can't spawn subagents.

**Pivots.** "Always-loaded core skill" collapsed — skill bodies are progressive-disclosure; universal rules moved to hook. Slash commands and skills merged in Claude Code v2.1.101. V18 promoted from research to first build session.

**Carried forward.** All plugin construction across V18–V27. Method instability during migration explicitly accepted.
