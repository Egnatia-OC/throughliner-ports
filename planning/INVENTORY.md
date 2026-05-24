# Inventory — current architecture

Two-layer split and plugin component list. Living document — current state, not history.

## The two-layer split

**Source-of-truth content (per-project):** UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md, additional SoT docs.

**Mechanical process (plugin):** hooks, subagents, skills, slash commands, and bundled artefacts.

Three plugin sub-categories: **Process** (phase orchestration), **Schemas** (doc structure specs), **Behaviour contract** (how Claude must act).

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
| `UX.md` | Read-only to Claude (PreToolUse enforced) |
| `BACKLOG/` | Read/write |
| `MANIFEST.md` | Read/write |
| `TEST-LOG.md` | Read/write (test-confirmation gate V27) |
| `build-log/` | Read/write |
| `CLAUDE.md` | Read/write; path block in fenced JSON |
| Additional SoT docs | Read-only to Claude |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Injects `additionalContext`: (a) universal behavioural rules from `universal-behaviour.md`; (b) foundational reads + state summary. Three tiers: tier 1 (non-method folder) → silent; tier 2 (partial) → rules + gap flag pointing at `/setup`; tier 3 (complete) → rules + full state summary. State summary includes: template-state detection, resume detection, version-footer mismatch tripwire, TEST-LOG tripwire (V27 — routes to planning when unconfirmed rows exist), Red flags tripwire (V54 — surfaces deferred red flags). V43 adds two-layer-permission preamble.

- **PreToolUse hook (consolidated).** Seven checks:
  - (a) Read-only enforcement on locked docs. V19.
  - (b) Proposed-edit redirect on locked-doc writes. V19.
  - (c) Batch file-list boundary enforcement. V25. Parses BACKLOG via `parse_backlog.py`.
  - (d) MANIFEST read-before-edit gate. V39. Three path shapes (single, multi, directory-prefix). Block-once via transcript scan.
  - (e) Serves-line validation. V22. V54 extended to additional SoT docs.
  - (f) Test-confirmation gate on Task → batch-executor. V27. Denies when previous-batch TEST-LOG rows are unconfirmed. Build-log session identification with fallback.
  - (g) Project-boundary enforcement. V56. Blocks writes outside project root.
  - V43 mode-aware messaging across all checks: `[No-code method]` prefix, `What to do:` line, mode-aware suffix in permissive modes for (a), (c), (f), (g).

- **PreToolUse git safety guard.** V34. Separate hook (Bash matcher). Denies `git reset --hard` and `git push --force`/`-f`. Allows `--force-with-lease`. Mode-aware deny messages.

- **PostToolUse hook.** V46. Fires after BACKLOG.md edits. Imports `find_top_unticked_batch` directly; surfaces parse failures via `additionalContext`. Non-blocking (PostToolUse can't deny).

- **PreCompact hook.** V52. Blocks compaction during active builds (unticked files in top batch). Surfaces handoff prompt. Silent when no build active.

- **UserPromptSubmit hook.** V52. Classifies first prompt (setup / test notes / resume) via keyword detection. Injects routing hint as `additionalContext`. Conservative: test notes need 2+ keyword hits. First-prompt detection via transcript marker.

- **Stop hook.** V25, extended V27. After batch-executor: parses BACKLOG for next unticked batch → redirect. If none and after-build pending → redirect to after-build. `stop_hook_active` prevents loops.

### Subagents (probabilistic, behavioural)

- **planning** — V22 at `plugin/agents/planning.md`. Test-note sort, drift checks (5, inlined — V42 added direct-edit detection as check 1), BACKLOG edits, Discoveries promotion, TEST-LOG row pruning (V53), per-row read-back (V27), recap. V32: inlined. V56: doc-first ordering, deferred-material aging.

- **before-build** — V25 at `plugin/agents/before-build.md`. Validates top batch, enumerates Files:, estimates verification burden, proposes splits. V27: label-preservation on splits. V32: inlined. Halt-and-confirm for (a) no batch, (b) malformed BACKLOG, (c) vague changes, (d) split needed.

- **batch-executor** — V25 at `plugin/agents/batch-executor.md`. Runs one build batch. Receives JSON from `parse_backlog.py`. Edits per-file, ticks BACKLOG. PreToolUse (c) enforces boundary. Prerequisite and re-batching carve-outs. V54: reads DOC-STRUCTURE at runtime. V56: scope-of-exploration limits.

- **after-build** — V27 at `plugin/agents/after-build.md`. MANIFEST update, recap (two-section: Claude-verified / user-verified, V48), TEST-LOG rows (10-column, V48), build-log entry with Performance section (V55), frame-correction sweep (V33), commit/tag prompt (V48). Idempotent. Invoked by Stop-hook redirect.

- **setup** — V29 at `plugin/agents/setup.md` (renamed from adopt.md V44). Four cases: (1) empty → 4 questions + scaffold, (2) existing code → scaffold alongside, (3) foreign CLAUDE.md → migrate/overwrite/leave, (4) already adopted → refresh with V47/V48/V46/V57 migrations. PreToolUse exempts setup's tool calls.

### Slash commands

All shipped commands use the **skill-with-flags** pattern (`skills/<name>/SKILL.md` with `user-invocable: true`). The legacy **commands-directory** pattern (`plugin/commands/<name>.md`) was retired in v71 — all commands migrated to skills/*/SKILL.md.

- `/setup` — four-case adoption. Scaffolds 6 spine templates + `planning/drafts/` + `research/`. **Shipped V29** (as `/adopt`; renamed V44).
- `/add-sot-doc <name>` — scaffolds additional-doc template. *Pending.*
- `/plan` — planning subagent. *Pending; auto-route is current path.*
- `/before-build` — before-build subagent. **Shipped V25.** Migrated to skills/ v71.
- `/build` — triggers batch-executor. **Shipped V25.** Migrated to skills/ v71.

### Bundled artefacts

- 8 templates under `plugin/templates/`: build-log/INDEX, CLAUDE, BACKLOG (legacy), BACKLOG/INDEX, MANIFEST, UX, TEST-LOG, ADDITIONAL-DOC.
- `plugin/scripts/parse_backlog.py` — shared BACKLOG parser. Auto-detects folder vs single-file mode. Exposes `status` field per batch (queued/active/parked/shipped); skips shipped/parked when finding top batch.
- `plugin/scripts/project_state.py` — shared module for path-block extraction, TEST-LOG parsing, build-log session identification, BACKLOG helpers.
- `plugin/scripts/allocate_number.py` — 4-digit number allocator. V59 removed subagent calls (Glob-based instead); now dev-side only.
- `plugin/docs/DOC-STRUCTURE.md` — structural specs. Read by planning, before-build, setup subagents.
- `plugin/docs/VOCABULARY.md` — method-term definitions.
- `plugin/hooks/universal-behaviour.md` — behavioural rules injected via SessionStart.
- `.claude-plugin/marketplace.json` — marketplace registration. V37.

## Design decisions (V17)

- **D1** — Stop hook proposes next batch; user gates via `stop_hook_active`.
- **D2** — Separate planning and before-build subagents for file-list-lock isolation.
- **D3** — SessionStart injects state; main Claude classifies opener and spawns planning.

## Architecture revisions (V17)

| Original | Revised | Reason |
|---|---|---|
| `drift-checker` subagent | Inline into planning | Subagents can't spawn subagents |
| Always-loaded core skill | SessionStart `additionalContext` | Skills aren't always-loaded |
| `batch-executor` enforces paths | PreToolUse hook enforces | Subagent config restricts tools, not paths |
| Free-form path block | Fenced JSON | Robust hook parsing |
| Standalone slash commands | Skills with flags (`skills/*/SKILL.md`) | Claude Code merged commands into skills; commands-directory retired v71 |
| Stop hook auto-chains | One redirect per turn | Loop prevention |

## Risks (from Opus feasibility response)

- Hook fragility around shell environments — defensive scripts required.
- Stop-hook loops if `stop_hook_active` not respected.
- Plugin skills can't define hooks — all hook logic at plugin level.
- Subagent context isolation: only channel in is the prompt.
- Cache invalidation on plugin update is manual (`/reload-plugins`).
- "Vibe coder distributing a plugin" UX gap.
- Method-still-being-refined risk accepted at V17.
- `UserPromptSubmit`-in-plugin bug (anthropics/claude-code#10225) — pivoted to SessionStart.

---
*No-code method — Version 61.*
