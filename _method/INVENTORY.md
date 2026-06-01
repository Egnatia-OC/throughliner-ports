# Inventory — current architecture

Two-layer split and plugin component list. Living document — current state, not history.

## The two-layer split

**Source-of-truth content (per-project):** UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md, additional SoT docs.

**Mechanical process (plugin):** hooks, procedure docs, skills, slash commands, and bundled artefacts.

Three plugin sub-categories: **Process** (phase orchestration via procedure docs), **Schemas** (doc structure specs), **Behaviour contract** (how Claude must act).

## Method-side doc fates

| Doc | Home | Plugin component |
|---|---|---|
| `Reference manual.md` | `Guides/` | Humans-only reference, linked from README |
| `crash-course/` | `Guides/` | HTML guide for testers/early adopters; derived from Reference manual |
| `CLAUDE-TEMPLATE.md` | Plugin | Template, scaffolded by `/sovsetup` |
| `BACKLOG-TEMPLATE.md` | Plugin | Template, scaffolded by `/sovsetup` |
| `MANIFEST-TEMPLATE.md` | Plugin | Template, scaffolded by `/sovsetup` |
| `UX-TEMPLATE.md` | Plugin | Template, scaffolded by `/sovsetup` |
| `ADDITIONAL-DOC-TEMPLATE.md` | Plugin | Template, scaffolded by `/add-sot-doc` |
| `DOC-STRUCTURE.md` | Plugin | Bundled at `plugin/docs/DOC-STRUCTURE.md` |
| `VOCABULARY.md` | Plugin | Bundled at `plugin/docs/VOCABULARY.md` |

## Project-side doc fates

| Doc | Access |
|---|---|
| `UX.md` | Phase-aware (V67): editable during planning; locked during build (PreToolUse enforced, with footer + proposed-edits carve-outs) |
| `BACKLOG/` | Read/write |
| `MANIFEST.md` | Read/write |
| `test-log/` | Read/write (test-confirmation gate V27). Legacy: flat `TEST-LOG.md` |
| `build-log/` | Read/write |
| `CLAUDE.md` | Read/write; path block in fenced JSON |
| Additional SoT docs | Phase-aware (V67): editable during planning; locked during build |
| `_method/proxies/` | Read/write; regenerated during planning and `/sovsetup`. Legacy: `.proxies/` at root |
| Source-code files | Phase-aware (V67): locked during planning; editable during build via batch Files: list |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Injects `additionalContext`: (a) universal behavioural rules from `universal-behaviour.md`; (b) foundational reads + state summary. Three tiers: tier 1 (non-method folder) → silent; tier 2 (partial) → rules + gap flag pointing at `/sovsetup`; tier 3 (complete) → rules + full state summary. State summary includes: template-state detection, resume detection, version-footer mismatch tripwire, TEST-LOG tripwire (V27), Red flags tripwire (V54), build-snapshot detection (V90 — checks `_method/active-build.md` for both unclosed and mid-build states; legacy fallback to `Status: active` in BACKLOG), OQ staleness detection (V89), OQ accumulation nudge (V90 — when 3+ OQs exist or any are stale, nudges toward `/sovdeliberate`), user-facing session-open status (V74; V90 adds OQ nudge line), parent-directory CLAUDE.md detection (V71). V43 adds two-layer-permission preamble.

- **PreToolUse hook (consolidated).** Eight checks, V67 phase-aware (`detect_phase()` — V90: checks `_method/active-build.md` first, falls back to BACKLOG batch status; V92: handles all-ticked batches by checking `Status: active` directly when parser returns empty):
  - (a) Locked source-of-truth doc enforcement. V19, V67 phase-aware. Build phase: UX.md + additional docs locked (footer + proposed-edits carve-outs). Planning phase: directly editable.
  - (b) Planning-phase source-code lock. V67. Blocks edits to non-doc files during planning (`is_path_block_doc()`, `is_research_file()`, `is_method_infra_file()` exemptions). V71: unadopted folders get a `/sovsetup`-pointing deny message instead of referencing BACKLOG/before-build. V91: method infrastructure dirs (BACKLOG/, proxies/, planning/) whitelisted. V92: root-level `_method/` files (`active-build.md`) also whitelisted.
  - (c) Batch file-list boundary enforcement. V25, V67 phase-aware. Build phase only. V90: reads `_method/active-build.md` snapshot first, falls back to BACKLOG via `parse_backlog.py`. V92: test-log/ and build-log/ writes exempted (close procedure needs these during build phase).
  - (d) MANIFEST read-before-edit gate. V39, V67 build-phase only. Three path shapes (single, multi, directory-prefix). Block-once via transcript scan.
  - (e) Serves-line validation. V22. V54 extended to additional SoT docs.
  - (f) Test-confirmation gate on build-phase file edits. V27, reframed V66. Denies when an active batch exists and previous-batch TEST-LOG rows are unconfirmed. Build-log session identification with fallback.
  - ~~(g) Project-boundary enforcement. V56.~~ Removed V91. Downstream checks (planning source lock, build batch boundary) already prevent cross-project writes. The Bash write-guard retains its own boundary check.
  - (h) Bash/PowerShell write-guard. V83. Scans Bash/PowerShell commands for file-write patterns (`sed -i`, `>`, `>>`, `tee`, `Set-Content`, `Out-File`, `Add-Content`, `cp`, `mv`). V91: strips heredoc/here-string content before scanning to avoid false positives. Extracts target paths best-effort; applies existing rules (project boundary, locked docs, batch file list, planning source lock). BACKLOG/MANIFEST exempted as always-writable. Null targets (`/dev/null`, `$null`) skipped.
  - (i) Unclosed-build commit guard. V132. Blocks `git commit` via Bash/PowerShell when `_method/active-build.md` exists with all Files: ticked. Prevents orphaned snapshots from skipping `/sovclose`. Mid-build commits (some files unticked) allowed.
  - V43 mode-aware messaging across all checks: `[Sovereign Implementer]` prefix, `What to do:` line, mode-aware suffix in permissive modes for (a), (c), (f), (g), (i).
  - V83 skill escape guidance on all phase-lock denies: (a), (b), (c), (h), (i) deny messages name the skill that unlocks the target (`/sovclose`, `/sovplan`, `/sovrecap`, `/sovbuild`).

- **PreToolUse git safety guard.** V34. Separate hook (Bash matcher). Denies `git reset --hard` and `git push --force`/`-f`. Allows `--force-with-lease`. Mode-aware deny messages.

- **PostToolUse hook.** V46, extended V82. Fires after Edit/Write/MultiEdit on structured method docs. Five validation paths: (1) BACKLOG parse validation (V46 — imports `find_top_unticked_batch`), (2) scope-context checks on BACKLOG batch files (Goal/Outputs/Success criteria), (3) TEST-LOG 10-column check, (4) build-log entry required sections, (5) proxy HTML comment header format. All lenient — warnings via `additionalContext`, not denies. Calls `validate_docs.py` for non-BACKLOG validators.

- **PreCompact hook.** V52. Blocks compaction during active builds (unticked files in top batch). Surfaces handoff prompt. Silent when no build active.

- **UserPromptSubmit hook.** V52, extended V90. Classifies first prompt (setup / test notes / resume / deliberate / plan structural) via keyword detection. Injects routing hint as `additionalContext`. Conservative: test notes need 2+ keyword hits. V109: idea-capture patterns merged into deliberate route (formerly separate ideate classification). First-prompt detection via transcript marker.

### Procedure docs (phase orchestration)

Ten procedure docs at `plugin/docs/procedures/`, read into main context on demand. Replaced the subagent layer (V66).

- **planning.md** — V22 origin, procedure doc V66. V90: narrowed to structural-only (reorder/split/merge/rescope batches). Test-note sort, drift checks (5, inlined), BACKLOG edits, Discoveries promotion, TEST-LOG row pruning, per-row read-back, recap. OQ work-through and feature requests redirected to `/sovdeliberate`. Inline git commit step with `plan:` prefix. V78: ordering principles and batch-ordering audit.

- **deliberate.md** — V90 origin; V109: absorbed ideate.md. OQ deliberation and idea capture: per-OQ work-through (promote/drop/re-park), new-topic exploration (discuss/assess/route), legacy Ideas-section triage, build-log entry for dispositions, inline git commit step with `deliberate:` prefix.

- **before-build.md** — V25 origin, procedure doc V66. Validates top batch, enumerates Files:, estimates verification burden, proposes splits. V27: label-preservation on splits. Halt-and-confirm for (a) no batch, (b) malformed BACKLOG, (c) vague changes, (d) split needed. V93: pre-build sizing check (8+ files AND open decisions → advisory warning). Invocation-prompt compact nudge on recap closing. V94: pre-build blocker gate — scans batch body and BACKLOG OQs for unresolved items before proceeding; halts with `/sovdeliberate` or `/sovplan` nudge if blockers found.

- **build.md** — V25 origin, procedure doc V76. V90: build-snapshot architecture — extracts batch to `_method/active-build.md`, removes from BACKLOG, ticks in snapshot. Receives JSON from `parse_backlog.py` for initial extraction. PreToolUse (c) enforces boundary (reads snapshot or BACKLOG). Prerequisite and re-batching carve-outs. V93: invocation-prompt compact nudge on completion prompt.

- **close.md** — V76 origin (absorbed after-build.md). V90: snapshot-aware phase detection (`_method/active-build.md` existence). V96: two-turn structure — Turn 1 (judgment, while build context is fresh): MANIFEST update, capabilities summary generation (step 1b, V106), doc-parity check, test session + Claude tests, recap, build-log entry, write-back + snapshot deletion, frame-correction sweep, staleness sweep, lost-feature check, idea sweep, then `[PROMPT]` turn boundary recommending `/compact`. Turn 2 (mechanical): footer bumps via `bump_version.py` (if version mismatch), proxy regeneration (script for headers/line numbers, then Claude reviews summaries), after-build steps, pre-commit checkpoint, `/sovgit` nudge. Planning/general path also two-turn (idea sweep → boundary → proxy regen → closing). Idempotent.

- **git.md** — V76 origin. Commit, tag, push walkthrough. First-use detection writes `## Git workflow` to CLAUDE.md (solo/team). Solo: commit-tag-push to main. Team: branch, commit, push, PR guidance. V93: end-of-session prompt standardised (`/compact` for continuing, `/clear` for fresh start).

- **testing.md** — V81 origin. Guided testing walkthrough: load pending User-verified rows, walk one at a time (type-specific guidance), record outcomes directly to TEST-LOG, structured debugging on failures (diagnose + route to BACKLOG). Consent-gated for unrunnable Claude-verified rows.

- **tersify.md** — V80 origin. Guided doc compression: phase gate, triage pass (rank by size, flag wrong-home/structural/verbose), compact gate, per-doc audit with approval gates. Planning phase only.

- **setup.md** — V29 origin, procedure doc V66. Four cases: (1) empty → 5 questions (product overview + 3 UX + language) + scaffold + `git config --local core.quotepath false`, (2) existing code → scaffold alongside, (3) foreign CLAUDE.md → migrate/overwrite/leave, (4) already adopted → refresh with V47/V48/V46/V57/V69/V70/V75/V94 migrations (V94: Language section + quotepath). PreToolUse exempts setup's tool calls.

- **revert.md** — V87 origin. Guided rollback: confirms commit exists, identifies changes since last commit, confirms revert, restores tracked files (`git checkout -- .`), optionally removes untracked files (`git clean -fd`), verifies clean state, advises committing before future builds. Edge case: no prior commit → explain and stop.

### Slash commands

All commands use the **skill-with-flags** pattern (`skills/<name>/SKILL.md` with `user-invocable: true`). Legacy **commands-directory** pattern retired v71.

- `/sovsetup` — four-case adoption. Scaffolds CLAUDE.md at root + spine docs inside `_method/` (UX.md, BACKLOG/, build-log/, test-log/, MANIFEST.md) + `_method/planning/drafts/` + `_method/research/` + `_method/proxies/`. **Shipped V29** (as `/adopt`; renamed V44; sov-prefixed V84).
- `/sovresearch` — proactive research search flow. Drafts query, proposes to user, executes via MCP/WebSearch/copyable prompt, files results. **Shipped V70** (sov-prefixed V84).
- `/add-sot-doc <name>` — scaffolds additional-doc template. *Pending.*
- `/sovplan` — structural planning (test read-back, drift checks, BACKLOG editing, ordering audit). Narrowed V90 to structural-only. **Shipped V78.**
- `/sovdeliberate` — OQ deliberation and idea capture (per-OQ work-through, new-topic exploration, dispositions, build-log entry). **Shipped V90; V109: absorbed `/sovideate`.**
- `/sovrecap` — pre-build planning recap (before-build procedure). **Shipped V25** (as `/before-build`); renamed V77.
- `/sovbuild` — lock and build procedure. **Shipped V25** (as `/build`); renamed V77.
- `/sovclose` — close procedure (dual-path: post-build or planning/general). **Shipped V76.** Absorbed after-build.md.
- `/sovgit` — git walkthrough (commit/tag/push, solo or team). **Shipped V76.**
- `/sovtest` — guided testing walkthrough (pending User-verified rows, debugging on failure). **Shipped V81** (sov-prefixed V84).
- `/sovtersify` — guided doc compression (triage + audit). Planning phase only. **Shipped V80** (sov-prefixed V84).
- `/sovrevert` — guided rollback (restore last committed state after a failed build). **Shipped V87.**
- `/sovexplain` — three-way router for method questions. Classifies as "what" (capability overview → MANIFEST proxy's capabilities summary), "how" (usage → matching skill or procedure doc), or "why" (design rationale → explain-proxy.md → explain-reference.md). Self-contained (no procedure doc). Handles both topic mode (user asks a question) and reactive mode (infers from last hook denial or skill interaction). **Shipped V102; routing V106.**

### Bundled artefacts

- 13 templates under `plugin/templates/`: CLAUDE, BACKLOG (legacy single-file), BACKLOG/BATCH, MANIFEST, UX, ADDITIONAL-DOC, test-log/ENTRY-TEMPLATE, research/search-queries/QUERY-TEMPLATE, .proxies/ux, .proxies/manifest, .proxies/research, .proxies/backlog, .proxies/build-log. .proxies/ templates scaffolded into `_method/proxies/` in consumer projects; .proxies/backlog and .proxies/build-log serve as operational indexes. Test session index lives inside .proxies/backlog as `## Test sessions` (V120 merge).
- `plugin/scripts/parse_backlog.py` — shared BACKLOG parser. Auto-detects folder vs single-file mode. Exposes `status` field per batch (queued/active/parked/shipped); skips shipped/parked when finding top batch.
- `plugin/scripts/validate_docs.py` — V82 structured-markdown validator. Four validators: TEST-LOG column count, build-log entry sections, scope-context completeness, proxy header format. Called by PostToolUse; usable standalone as CLI pre-flight.
- `plugin/scripts/project_state.py` — shared module for path-block extraction, TEST-LOG parsing, build-log session identification, BACKLOG helpers, file-type detection (V82: `is_test_log_content_file`, `is_build_log_entry_file`, `is_proxy_file`, `is_backlog_batch_file`). V94: `safe_read_text()` uses `utf-8-sig` encoding to strip Windows BOM bytes.
- `plugin/scripts/allocate_number.py` — 4-digit number allocator. V59 removed subagent calls (Glob-based instead); now dev-side only.
- `plugin/scripts/bump_version.py` — consumer-side close mechanical. Bumps `*Sovereign Implementer — Version N.*` footers and regenerates proxy line-number pointers. Invoked by `/sovclose` Turn 2. Two modes: `<old> <new>` for bump + regen, no args for regen only.
- `plugin/docs/DOC-STRUCTURE.md` — structural specs. Read by planning, before-build, setup procedures.
- `plugin/docs/VOCABULARY.md` — method-term definitions.
- `plugin/docs/explain-reference.md` — curated design rationale for all 42 method features. Read by `/sovexplain` via targeted offset/limit reads.
- `plugin/docs/explain-proxy.md` — topic index into explain-reference.md. Maps user questions to line ranges for targeted reads.
- `plugin/hooks/universal-behaviour.md` — behavioural rules injected via SessionStart. V93: session-length awareness (mid-session compact nudge + invocation-prompt compact nudge).
- `.claude-plugin/marketplace.json` — marketplace registration. V37.

## Design decisions (V17)

- **D1** — ~~Stop hook proposes next batch; user gates via `stop_hook_active`.~~ Removed V66 (subagent removal). V76: build procedure nudges `/sovclose`; `/sovclose` nudges `/sovgit`. All transitions via `[PROMPT]`.
- **D2** — Separate planning and before-build phases for file-list-lock isolation. V66: converted from subagents to procedure docs.
- **D3** — SessionStart injects state; Claude classifies opener and reads the matching procedure doc.

## Architecture revisions (V17)

| Original | Revised | Reason |
|---|---|---|
| `drift-checker` subagent | Inline into planning | Subagents can't spawn subagents |
| Always-loaded core skill | SessionStart `additionalContext` | Skills aren't always-loaded |
| `batch-executor` enforces paths | PreToolUse hook enforces | Tool-level enforcement, not instruction-level |
| Free-form path block | Fenced JSON | Robust hook parsing |
| Standalone slash commands | Skills with flags (`skills/*/SKILL.md`) | Claude Code merged commands into skills; commands-directory retired v71 |
| Stop hook auto-chains | ~~Removed V66~~ — V76: build → `/sovclose` → `/sovgit` via `[PROMPT]` nudges | Subagent layer removed; skill-to-skill via user invocation |

## Risks (from Opus feasibility response)

- Hook fragility around shell environments — defensive scripts required.
- ~~Stop-hook loops if `stop_hook_active` not respected.~~ Removed V66 (Stop hook deleted).
- Plugin skills can't define hooks — all hook logic at plugin level.
- ~~Subagent context isolation: only channel in is the prompt.~~ Removed V66 (subagents replaced by procedure docs in main context).
- Cache invalidation on plugin update is manual (`/reload-plugins`).
- "Vibe coder distributing a plugin" UX gap.
- Method-still-being-refined risk accepted at V17.
- `UserPromptSubmit`-in-plugin bug (anthropics/claude-code#10225) — pivoted to SessionStart.

---
*Sovereign Implementer — Version 110.*
