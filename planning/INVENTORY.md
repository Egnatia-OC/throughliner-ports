# Inventory — current architecture

Two-layer split and plugin component list. Living document — current state, not history.

## The two-layer split

**Source-of-truth content (per-project):** UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md, additional SoT docs.

**Mechanical process (plugin):** hooks, procedure docs, skills, slash commands, and bundled artefacts.

Three plugin sub-categories: **Process** (phase orchestration via procedure docs), **Schemas** (doc structure specs), **Behaviour contract** (how Claude must act).

## Method-side doc fates

| Doc | Home | Plugin component |
|---|---|---|
| `Reference manual.md` | Repo root | Humans-only reference, linked from README |
| `crash-course/` | Repo root | HTML guide for testers/early adopters; derived from Reference manual |
| `CLAUDE-TEMPLATE.md` | Plugin | Template, scaffolded by `/setup` |
| `BACKLOG-TEMPLATE.md` | Plugin | Template, scaffolded by `/setup` |
| `MANIFEST-TEMPLATE.md` | Plugin | Template, scaffolded by `/setup` |
| `UX-TEMPLATE.md` | Plugin | Template, scaffolded by `/setup` |
| `ADDITIONAL-DOC-TEMPLATE.md` | Plugin | Template, scaffolded by `/add-sot-doc` |
| `DOC-STRUCTURE.md` | Plugin (live); repo root frozen V39 | Bundled at `plugin/docs/DOC-STRUCTURE.md` |
| `VOCABULARY.md` | Plugin (live); repo root frozen V39 | Bundled at `plugin/docs/VOCABULARY.md` |
| `NO-CODE-METHOD.md` | Repo root — frozen V39 | Retired from plugin V32; prose-only snapshot |

## Project-side doc fates

| Doc | Access |
|---|---|
| `UX.md` | Phase-aware (V67): editable during planning; locked during build (PreToolUse enforced, with footer + proposed-edits carve-outs) |
| `BACKLOG/` | Read/write |
| `MANIFEST.md` | Read/write |
| `TEST-LOG.md` | Read/write (test-confirmation gate V27) |
| `build-log/` | Read/write |
| `CLAUDE.md` | Read/write; path block in fenced JSON |
| Additional SoT docs | Phase-aware (V67): editable during planning; locked during build |
| Source-code files | Phase-aware (V67): locked during planning; editable during build via batch Files: list |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Injects `additionalContext`: (a) universal behavioural rules from `universal-behaviour.md`; (b) foundational reads + state summary. Three tiers: tier 1 (non-method folder) → silent; tier 2 (partial) → rules + gap flag pointing at `/setup`; tier 3 (complete) → rules + full state summary. State summary includes: template-state detection, resume detection, version-footer mismatch tripwire, TEST-LOG tripwire (V27 — routes to planning when unconfirmed rows exist), Red flags tripwire (V54 — surfaces deferred red flags), user-facing session-open status (V74 — batch counts, next batch name/goal/file count, pending tests; directive mandates Claude present it before routing). V43 adds two-layer-permission preamble.

- **PreToolUse hook (consolidated).** Seven checks, V67 phase-aware (`detect_phase()` from BACKLOG batch status):
  - (a) Locked source-of-truth doc enforcement. V19, V67 phase-aware. Build phase: UX.md + additional docs locked (footer + proposed-edits carve-outs). Planning phase: directly editable.
  - (b) Planning-phase source-code lock. V67. Blocks edits to non-doc files during planning (`is_path_block_doc()`, `is_research_file()` exemptions).
  - (c) Batch file-list boundary enforcement. V25, V67 phase-aware. Build phase only. Parses BACKLOG via `parse_backlog.py`.
  - (d) MANIFEST read-before-edit gate. V39, V67 build-phase only. Three path shapes (single, multi, directory-prefix). Block-once via transcript scan.
  - (e) Serves-line validation. V22. V54 extended to additional SoT docs.
  - (f) Test-confirmation gate on build-phase file edits. V27, reframed V66. Denies when an active batch exists and previous-batch TEST-LOG rows are unconfirmed. Build-log session identification with fallback.
  - (g) Project-boundary enforcement. V56. Blocks writes outside project root.
  - V43 mode-aware messaging across all checks: `[No-code method]` prefix, `What to do:` line, mode-aware suffix in permissive modes for (a), (c), (f), (g).

- **PreToolUse git safety guard.** V34. Separate hook (Bash matcher). Denies `git reset --hard` and `git push --force`/`-f`. Allows `--force-with-lease`. Mode-aware deny messages.

- **PostToolUse hook.** V46. Fires after BACKLOG.md edits. Imports `find_top_unticked_batch` directly; surfaces parse failures via `additionalContext`. Non-blocking (PostToolUse can't deny).

- **PreCompact hook.** V52. Blocks compaction during active builds (unticked files in top batch). Surfaces handoff prompt. Silent when no build active.

- **UserPromptSubmit hook.** V52. Classifies first prompt (setup / test notes / resume) via keyword detection. Injects routing hint as `additionalContext`. Conservative: test notes need 2+ keyword hits. First-prompt detection via transcript marker.

### Procedure docs (phase orchestration)

Five procedure docs at `plugin/docs/procedures/`, read into main context on demand. Replaced the subagent layer (V66).

- **planning.md** — V22 origin, procedure doc V66. Test-note sort, drift checks (5, inlined — V42 added direct-edit detection as check 1; cold-start skip V63), BACKLOG edits, Discoveries promotion, TEST-LOG row pruning (V53), per-row read-back (V27), recap. V56: doc-first ordering, deferred-material aging. V63: classify-then-load, cold-start gate, reasoning constraint.

- **before-build.md** — V25 origin, procedure doc V66. Validates top batch, enumerates Files:, estimates verification burden, proposes splits. V27: label-preservation on splits. Halt-and-confirm for (a) no batch, (b) malformed BACKLOG, (c) vague changes, (d) split needed.

- **build.md** — V25 origin, procedure doc V66. Runs one build batch. Receives JSON from `parse_backlog.py`. Edits per-file, ticks BACKLOG. PreToolUse (c) enforces boundary. Prerequisite and re-batching carve-outs. V54: reads DOC-STRUCTURE at runtime. V56: scope-of-exploration limits. On completion, directs Claude to read after-build.md.

- **after-build.md** — V27 origin, procedure doc V66. MANIFEST update, doc-parity check (V62), recap (two-section: Claude-verified / user-verified, V48), TEST-LOG rows (10-column, V48), build-log entry with Performance section (V55), frame-correction sweep (V33), idea sweep (V62), CLAUDE.md after-build steps (V62), pre-commit checkpoint (V62), commit/tag prompt (V48). Idempotent.

- **setup.md** — V29 origin, procedure doc V66. Four cases: (1) empty → 4 questions + scaffold, (2) existing code → scaffold alongside, (3) foreign CLAUDE.md → migrate/overwrite/leave, (4) already adopted → refresh with V47/V48/V46/V57 migrations. PreToolUse exempts setup's tool calls.

### Slash commands

All shipped commands use the **skill-with-flags** pattern (`skills/<name>/SKILL.md` with `user-invocable: true`). The legacy **commands-directory** pattern (`plugin/commands/<name>.md`) was retired in v71 — all commands migrated to skills/*/SKILL.md.

- `/setup` — four-case adoption. Scaffolds 6 spine templates + `planning/drafts/` + `research/`. **Shipped V29** (as `/adopt`; renamed V44).
- `/add-sot-doc <name>` — scaffolds additional-doc template. *Pending.*
- `/plan` — planning procedure. *Pending; auto-route is current path.*
- `/before-build` — before-build procedure. **Shipped V25.** Migrated to skills/ v71.
- `/build` — triggers build procedure. **Shipped V25.** Migrated to skills/ v71.

### Bundled artefacts

- 8 templates under `plugin/templates/`: build-log/INDEX, CLAUDE, BACKLOG (legacy), BACKLOG/INDEX, MANIFEST, UX, TEST-LOG, ADDITIONAL-DOC.
- `plugin/scripts/parse_backlog.py` — shared BACKLOG parser. Auto-detects folder vs single-file mode. Exposes `status` field per batch (queued/active/parked/shipped); skips shipped/parked when finding top batch.
- `plugin/scripts/project_state.py` — shared module for path-block extraction, TEST-LOG parsing, build-log session identification, BACKLOG helpers.
- `plugin/scripts/allocate_number.py` — 4-digit number allocator. V59 removed subagent calls (Glob-based instead); now dev-side only.
- `plugin/docs/DOC-STRUCTURE.md` — structural specs. Read by planning, before-build, setup procedures.
- `plugin/docs/VOCABULARY.md` — method-term definitions.
- `plugin/hooks/universal-behaviour.md` — behavioural rules injected via SessionStart.
- `.claude-plugin/marketplace.json` — marketplace registration. V37.

## Design decisions (V17)

- **D1** — ~~Stop hook proposes next batch; user gates via `stop_hook_active`.~~ Removed V66 (subagent removal). Build procedure chains to after-build directly.
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
| Stop hook auto-chains | ~~Removed V66~~ — build procedure chains to after-build directly | Subagent layer removed; no inter-turn redirect needed |

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
*No-code method — Version 67.*
