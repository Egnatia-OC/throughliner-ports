# Dev-side architecture map

Written v149. Reference for graduation batches (0148–0151).

## The situation

The dev side and the plugin side are parallel systems that do the same job. The dev side uses prose rules Claude reads each session. The plugin uses hooks, procedure docs, and skills that enforce mechanically. Graduation means: stop using the prose system, start using the mechanical system on this project.

## What each dev-side file does and where it goes

### session-protocol.md (~270 lines)

Defines session lifecycle: how to open (read docs, classify opener, run checks), what happens mid-session (rules like "no stealth fixes"), how to close (two-turn structure, sweeps, build-log entry, commit/tag/push).

**Plugin equivalents that already cover this:**
- Session open → SessionStart hook (state summary, orientation, tier detection)
- Opener routing → UserPromptSubmit hook (keyword classification)
- Before build → before-build.md procedure
- Build → build.md procedure
- Close → close.md procedure (two-turn, sweeps, build-log, commit)
- Git → git.md procedure
- Planning → planning.md procedure
- Mid-session rules → universal-behaviour.md

**Gaps — things the plugin doesn't enforce:**
- Three-number versioning convention (session tag / method version / batch number) — plugin only tracks method version
- Session handoff protocol (tick completed work, annotate in-progress, record decisions) — not in any procedure doc
- Batch-input check at session open (scan for out-of-repo references) — not in SessionStart
- OQ blocker check at session open — partially in before-build.md (blocker gate) but not at session open

**Graduation action:** Most content is already covered. Gaps go into CLAUDE.md project-specific notes or become new batch items.

### session-reference.md (~340 lines)

Entry shapes (build-log, OQ, ideas, test-log, queued batch), footer bump lists, testing setup (pytest), response-shape tags, planning artifact lifecycle, proxy spec, drafts-in-flight convention.

**Plugin equivalents:**
- Entry shapes → DOC-STRUCTURE.md
- Response-shape tags → universal-behaviour.md
- Testing → testing.md procedure
- Proxy spec → DOC-STRUCTURE.md

**Gaps:**
- Dev-side queued batch shape (Goal/Approach/Inputs/Outputs/Success criteria/Risks — different from plugin's scope-context + build-operations format)
- Footer bump list (mechanical — bump_version.py handles it, but the "which files" list lives here)
- Pytest suite location and conventions
- Dev-side proxy spec (slightly different from plugin-side)

**Graduation action:** Dev-specific content (pytest, dev batch shape) goes into CLAUDE.md project-specific notes. Plugin-equivalent content is dropped.

### INVENTORY.md (~160 lines)

Lists every plugin component with descriptions and version history. Architecture reference.

**Plugin equivalent:** No consumer-project equivalent. Closest is MANIFEST.md, but MANIFEST tracks the consumer project's components, not the plugin's own architecture.

**Graduation action:** Keep as a regular project file (it describes what the plugin IS, not method-managed planning). Not an _method/ artifact. Already carries the method footer and is updated during doc-code parity.

### CLAUDE.md (~200+ lines)

Project instructions. Mix of design philosophy, project identity, disambiguation rules, workflow rules, environment context, current state tracker.

**Plugin equivalent:** CLAUDE-TEMPLATE.md provides the skeleton: product overview, language, path block, project-specific notes, after-build steps.

**Graduation action — section-by-section mapping:**

| Current section | Destination |
|---|---|
| Read this first | Drop — plugin procedures handle load order |
| Design constraints | Project-specific notes |
| What this project is | Product overview fields |
| Main goal | Project-specific notes |
| This project vs consumer projects | Project-specific notes (shortened) |
| Plugin management questions | Project-specific notes |
| Dev-side vs plugin-side disambiguation | Project-specific notes |
| Dev-side convergence strategy | Drop — goal achieved by graduation |
| Don't default to memory | Project-specific notes |
| Make BACKLOG edits directly | Drop — plugin already does this |
| Proactive research | Project-specific notes |
| File research before moving on | Project-specific notes |
| Use absolute paths | Project-specific notes (check if still needed) |
| Dev-project marker file | Drop — marker deleted |
| E2E test sessions | Project-specific notes |
| Taskflowapp as E2E test reference | Project-specific notes |
| Adherence-drop diagnostic | Project-specific notes |
| Command execution | Project-specific notes |
| My experience level | Project-specific notes |
| Current state | Keep — updated each session close |

### Dev/Planning/BACKLOG.md

Monolithic roadmap file with queued batches (full scope inline), open questions, shipped history summary.

**Plugin equivalent:** `_method/BACKLOG/` folder with per-batch files + `_method/proxies/backlog.md` index.

**Graduation action:** Split into per-batch files. The "Shipped history" line becomes a note in the BACKLOG proxy. OQs section moves into the BACKLOG proxy (per plugin DOC-STRUCTURE convention).

### Dev/Planning/build-log/

Per-session build history. INDEX.md newest-first. Same structure as plugin's `_method/build-log/`.

**Graduation action:** Move to `_method/build-log/`. No content changes needed.

### Dev/Planning/test-log/

Per-session test records. Same structure as plugin's `_method/test-log/`.

**Graduation action:** Move to `_method/test-log/`. Test session index currently in separate INDEX.md — plugin convention puts it in the BACKLOG proxy under `## Test sessions`.

### Dev/Planning/.proxies/

Three proxy files (session-protocol, session-reference, backlog). Same concept as plugin's `_method/proxies/`.

**Graduation action:** Move to `_method/proxies/`. Session-protocol and session-reference proxies become obsolete once those files are retired — replace with plugin-standard proxies (ux, manifest, research, backlog, build-log).

### Dev/drafts/

One file currently (`claude-cli-headless-feasibility.md`). Scratch space for substantive content.

**Graduation action:** Move to `_method/planning/drafts/`.

### Dev/Resources/research/

~15 research files. External findings, platform audits, feasibility studies.

**Graduation action:** Move to `_method/research/`.

### Files that DON'T move

- `Dev/Resources/scripts/` — project code (bump_version.py, parse_backlog.py, etc.), not method artifacts
- `Dev/Resources/tests/` — pytest suite, project code
- `Dev/Resources/Marketing/` — project content
- `Dev/Resources/Iteration playbook/` — historical archive, read-only
- `Guides/` — product-facing docs (Reference manual, crash course)
- `plugin/` — the plugin source code itself
