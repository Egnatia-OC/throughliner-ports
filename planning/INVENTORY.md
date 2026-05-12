# Inventory — V17

The two-layer split and the final plugin component list. Permanent reference for V18–V27. Design as **revised after V17's Opus feasibility check** (response in `claude-code-plugin-feasibility-response.md` in this folder).

## The two-layer split

**Source-of-truth content (per-project):** filled-in `UX.md`, `BACKLOG.md`, `MANIFEST.md`, `CLAUDE.md`, and any project-specific additional source-of-truth docs.

**Mechanical process (becomes plugin):** all hooks, subagents, skills, slash commands, and bundled artefacts that orchestrate Claude Code's behaviour in a project that uses the method.

Three sub-categories on the plugin side, surfaced in V17's walkthrough:

- **Process** — phase orchestration (build sequence, routes, drift checks, fold-in mechanics).
- **Schemas** — what the per-project docs must look like (was `DOC-STRUCTURE.md`).
- **Behaviour contract** — how Claude must act in the seat (push back, no-stealth-fix, red-flag surfacing, etc.).

## Method-side doc fates

| Doc | Home | Plugin component | Notes |
|---|---|---|---|
| `Crash course.md` | Plugin | Bundled docs (humans-only reference) | Updated in V25 to reflect plugin architecture. |
| `CLAUDE-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` skill-command | **Path block format must change to fenced YAML/JSON in V18** for hook parsing. |
| `BACKLOG-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `MANIFEST-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `UX-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `ADDITIONAL-DOC-TEMPLATE.md` | Plugin | Template, scaffolded by `/add-sot-doc <name>` | |
| `DOC-STRUCTURE.md` | Plugin | Skill body OR bundled reference doc (decision deferred to V25) | |
| `NO-CODE-METHOD.md` | Plugin | Distributed across components (skills + hooks + subagents); original retired in V26 | |

## Project-side doc fates

| Doc | Home |
|---|---|
| `UX.md` | Per-project; **read-only to Claude** (PreToolUse hook enforces) |
| `BACKLOG.md` | Per-project; read/write to Claude (with discussion-contract in subagent prompts) |
| `MANIFEST.md` | Per-project; read/write to Claude |
| `CLAUDE.md` | Per-project; **path block in fenced YAML/JSON** for hook parsing |
| Additional SoT docs | Per-project; read-only to Claude |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Foundational reads (CLAUDE.md, path block, SoT docs); template-state detection; resume detection; routing decision injected as `additionalContext`.
- **UserPromptSubmit hook.** Universal behavioural rules injected as `additionalContext` on every turn (push back on assumptions, surface red flags, plain English). *Replaces the original "always-loaded core skill" idea — skills bodies aren't always-loaded.*
- **PreToolUse hook (consolidated, multiple checks).**
  - (a) Read-only enforcement on locked files (`UX.md`, additional SoT docs).
  - (b) Fold-in redirect: `UX.md` write attempts redirected to a `[FOLD-IN PENDING]` block in `BACKLOG.md`.
  - (c) Batch file-list enforcement during `batch-executor` (the file list comes in via the subagent's prompt).
  - (d) MANIFEST/UX read-before-edit enforcement.
  - (e) Serves-line check on `BACKLOG.md` build batch additions.
- **Stop hook (build sequencer).** After `batch-executor` finishes a turn, reads `BACKLOG.md`, finds the top unticked build batch, returns `{"decision": "block", "reason": "<batch instructions>"}`. **Respects `stop_hook_active`** — one redirect per user turn (matches D1: explicit user gating between batches).

### Subagents (probabilistic, behavioural)

- **planning** — test-note sort (Suggestions/Discoveries), drift checks (**inlined — drift-checker is NOT a separate subagent**, since subagents can't spawn subagents), `BACKLOG.md` edits, recap. Invoked via `/plan` or auto-routed by SessionStart hook on test-note paste.
- **before-build** — batch grouping, file-list lock, handoff. Invoked via `/before-build`.
- **batch-executor** — runs one batch per fresh context. Receives batch instructions + declared file list via prompt; PreToolUse hook enforces the file-list boundary.
- **after-build** — `MANIFEST.md` update, plain-English build recap with `[Requested]`/`[Suggested]` labels, test/clear prompts.
- **new-project** — 4-prompt walk-through; queues `[FOLD-IN PENDING]` block in `BACKLOG.md`.
- **migration** — diagnostic + walk-through to bring existing docs up to spec.

### Slash commands (skills with `disable-model-invocation: true`, `user-invocable: true`, `agent: <subagent>`)

- `/new-project` → new-project subagent
- `/migrate` → migration subagent
- `/init-project` → scaffolds the 5 templates into a user project
- `/add-sot-doc <name>` → scaffolds the additional-doc template
- `/plan` → planning subagent (also auto-routed via SessionStart)
- `/before-build` → before-build subagent
- `/build` → triggers batch-executor (alternative entry; default is auto-continuation via Stop hook)

### Bundled artefacts

- 5 templates (CLAUDE, BACKLOG, MANIFEST, UX, ADDITIONAL-DOC) under `skills/init-project/templates/`.
- `Crash course.md` as bundled docs (not loaded into Claude's context).
- `DOC-STRUCTURE.md` content — destination decided in V25.

## Design decisions taken in V17

- **D1 — build orchestration mode.** Stop hook proposes the next batch; user gates. Naturally enforced by `stop_hook_active` loop prevention.
- **D2 — planning vs before-build subagent.** Kept as two separate subagents for clean isolation of the file-list-lock step.
- **D3 — auto-route on test-note paste.** SessionStart hook auto-launches the planning subagent; explicit `/plan` is the override.
- **A — V18 = research session.** Not needed; research done by Opus during V17. V18 becomes the first build session.
- **B — Vxx folders ARE method versions.** Their contents expand to include plugin components alongside (and eventually replacing) the method docs. Footer convention extends.

## Architecture revisions made in V17 (vs walkthrough first-pass)

| Original (Chunks A/B/C) | Revised | Reason |
|---|---|---|
| `drift-checker` subagent invoked BY `planning` subagent | Inline drift logic into planning subagent prompt | Subagents can't spawn other subagents |
| Always-loaded core skill (universal behaviours) | `UserPromptSubmit` hook injecting `additionalContext` | Skill bodies aren't always-loaded |
| `batch-executor` subagent enforces file-list isolation directly | PreToolUse hook enforces; `batch-executor` receives the list via its prompt | Subagent config restricts tools, not paths |
| `CLAUDE.md` path block as free-form markdown bullets | Fenced YAML/JSON code block | Robust hook parsing |
| Slash commands as standalone components | Slash commands as skills with `disable-model-invocation: true` + `user-invocable: true` + `agent: <subagent>` | Claude Code v2.1.101 merged commands into skills |
| Stop hook auto-chains batches | One redirect per user turn (`stop_hook_active`) | Platform-level loop prevention |

## Risks taken on (from Opus feasibility response)

- Hook fragility around shell environments — defensive shell scripts required, test on a clean shell.
- Stop-hook infinite loops if `stop_hook_active` not respected — must test the loop-exit path before shipping.
- Plugin skills can't define hooks (security) — all hook logic at plugin level (`hooks/hooks.json`), not inside individual skills.
- Subagent context isolation: only channel in is the prompt — long prompts eat the subagent's own context budget.
- Cache invalidation on plugin update is manual — `/reload-plugins` required.
- The "vibe coder distributing a plugin" UX gap — local-install requires CLI muscle; consider a one-click install script.
- **Method-still-being-refined risk acknowledged and accepted at V17 close.** Reasoning: current method docs are large enough that context bloat is itself preventing realistic adherence testing; the plugin's per-component context isolation is the testability fix, not a freeze of an unstable method.

---
*No-code method — Version 17.*
