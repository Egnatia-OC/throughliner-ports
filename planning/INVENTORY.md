# Inventory — current architecture

The two-layer split and the final plugin component list. Living document — describes current state, not a historical snapshot. Originated as V17's design after the Opus feasibility check (response in `claude-code-plugin-feasibility-response.md` in this folder); revised in subsequent sessions as decisions land.

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

- **SessionStart hook.** Two responsibilities, both injected as `additionalContext`: (a) the universal behavioural rules — push back on assumptions, surface red flags, plain English — installed in V18; (b) foundational reads (CLAUDE.md, path block, SoT docs), template-state detection, resume detection (top build batch in `BACKLOG.md`), a version-footer mismatch tripwire (each SoT doc's footer compared against the plugin's current method version; mismatches surfaced as a state-summary line), and a prose state summary that hints at the route — all added in V21. **Three-tier behaviour:** tier 1 (non-method folder — no `CLAUDE.md` and no method-footer spine docs) emits nothing; the plugin is invisible. Tier 2 (partial method shape — e.g. `CLAUDE.md` present but path block unparseable, or spine docs present without `CLAUDE.md`) emits universal rules + a single-paragraph gap flag pointing at `/init-project` or `/migrate`. Tier 3 (complete method project) emits universal rules + the full state summary. Route classification of the user's opener stays with Claude — the hook flags only deterministic structural state. *Replaces the original "always-loaded core skill" idea (skill bodies aren't always-loaded). Originally planned as a `UserPromptSubmit` hook for per-turn re-injection, but `UserPromptSubmit` hooks declared in plugin `hooks.json` don't execute due to anthropics/claude-code#10225. SessionStart works in plugins today and is functionally equivalent given the method's `/clear`-after-every-build discipline — every new session re-fires the hook. Project root is located via the stdin `cwd` JSON field rather than `$CLAUDE_PROJECT_DIR`, which is broken for plugin hooks per anthropics/claude-code#9447.*
- **PreToolUse hook (consolidated, multiple checks).**
  - (a) Read-only enforcement on locked files (`UX.md`, additional SoT docs). **Shipped V19.**
  - (b) Fold-in redirect: `UX.md` write attempts redirected to a `[FOLD-IN PENDING]` block in `BACKLOG.md`. **Shipped V19** (the redirect is the deny-reason text; Claude writes the block itself).
  - (c) Batch file-list enforcement during `batch-executor` (the file list comes in via the subagent's prompt). *Pending — V23.*
  - (d) MANIFEST/UX read-before-edit enforcement. *Pending — V22+ as the planning subagent's protocol stabilises; precise hook scope TBD.*
  - (e) Serves-line check on `BACKLOG.md` build batch additions. **Shipped V22.** Parses every `Serves UX.md: <entry>.` line in the proposed new content (Edit's `new_string`, Write's `content`, MultiEdit's per-edit `new_string`s), matches each named entry against UX.md's Functionalities section with **case-insensitive exact match after whitespace-trim** (Q3 decision). Misses deny with a redirect message listing the unmatched names and a sample of known entries so Claude can spot a typo or recognise it needs to fold in first. `Serves <ADDITIONAL>.md:` lines for additional source-of-truth docs are out of V22 scope and pass through.
- **Stop hook (build sequencer).** After `batch-executor` finishes a turn, reads `BACKLOG.md`, finds the top unticked build batch, returns `{"decision": "block", "reason": "<batch instructions>"}`. **Respects `stop_hook_active`** — one redirect per user turn (matches D1: explicit user gating between batches).

### Subagents (probabilistic, behavioural)

- **planning** — test-note sort (Suggestions/Discoveries), drift checks (**inlined — drift-checker is NOT a separate subagent**, since subagents can't spawn subagents), mixed-input secondary sort, `BACKLOG.md` edits, Discoveries → planning batch promotion, recap. **Shipped V22** at `plugin/agents/planning.md`. Invoked by main Claude via the Task tool with `subagent_type: "no-code-method:planning"` after main Claude classifies the user's opener as `test notes` / `feature request` / `scope question` / `mixed` (per `NO-CODE-METHOD.md` → *Handoff to the planning subagent*). Drift checks always run on every planning session; only skip case is "nothing has been built yet" (Q2 decision). The `/plan` slash command is *not* yet shipped — for V22, the auto-route via main-Claude classification is the only invocation path; `/plan` lands in a later session.
- **before-build** — batch grouping, file-list lock, handoff. Invoked via `/before-build`.
- **batch-executor** — runs one batch per fresh context. Receives batch instructions + declared file list via prompt; PreToolUse hook enforces the file-list boundary.
- **after-build** — `MANIFEST.md` update, plain-English build recap with `[Requested]`/`[Suggested]` labels, test/clear prompts.
- **new-project** — 4-prompt walk-through; queues `[FOLD-IN PENDING]` block in `BACKLOG.md`.
- **migration** — diagnostic + walk-through to bring existing docs up to spec.

### Slash commands (skills with `disable-model-invocation: true`, `user-invocable: true`, `agent: <subagent>`)

**As of V22, only `/init-project` is shipped.** The remaining commands are listed below for forward-looking architectural reference, with their planned-V annotation. A reader (human or Claude) should not assume the *Pending* commands exist in the installed plugin — they are roadmap items, not current capabilities.

- `/init-project` → scaffolds the 5 templates into a user project. **Shipped V19.**
- `/new-project` → new-project subagent. *Pending — V26.*
- `/migrate` → migration subagent. *Pending — V26.*
- `/add-sot-doc <name>` → scaffolds the additional-doc template. *Pending — not yet scheduled in `PLAN.md`.*
- `/plan` → planning subagent. *Pending — auto-route via main-Claude classification is the only invocation path as of V22 (per the planning subagent entry above). Explicit `/plan` skill-command not yet shipped; future session.*
- `/before-build` → before-build subagent. *Pending — V23.*
- `/build` → triggers batch-executor (alternative entry; default is auto-continuation via Stop hook). *Pending — V23.*

### Bundled artefacts

- 5 templates (CLAUDE, BACKLOG, MANIFEST, UX, ADDITIONAL-DOC) under `skills/init-project/templates/`.
- `Crash course.md` as bundled docs (not loaded into Claude's context).
- `DOC-STRUCTURE.md` content — destination decided in V25.

## Design decisions taken in V17

- **D1 — build orchestration mode.** Stop hook proposes the next batch; user gates. Naturally enforced by `stop_hook_active` loop prevention.
- **D2 — planning vs before-build subagent.** Kept as two separate subagents for clean isolation of the file-list-lock step.
- **D3 — auto-route on test-note paste.** SessionStart hook surfaces structural state; main Claude classifies the user's opener (test notes / feature request / scope question / mixed) and spawns the planning subagent via the Task tool with the classification as `primary_intent`. (V17 wording said the SessionStart hook itself auto-launches the subagent; in implementation, hooks inject context and Claude decides what subagent to spawn — the route remains automatic but main Claude is the launcher.) Explicit `/plan` is the override (not yet shipped — lands in a later session).
- **A — V18 = research session.** Not needed; research done by Opus during V17. V18 becomes the first build session.
- **B — Vxx folders ARE method versions.** Their contents expand to include plugin components alongside (and eventually replacing) the method docs. Footer convention extends.

## Architecture revisions made in V17 (vs walkthrough first-pass)

| Original (Chunks A/B/C) | Revised | Reason |
|---|---|---|
| `drift-checker` subagent invoked BY `planning` subagent | Inline drift logic into planning subagent prompt | Subagents can't spawn other subagents |
| Always-loaded core skill (universal behaviours) | `SessionStart` hook injecting `additionalContext` | Skill bodies aren't always-loaded. (V17 first chose `UserPromptSubmit`; V18 pivoted to `SessionStart` because `UserPromptSubmit`-in-plugin is blocked by anthropics/claude-code#10225.) |
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
- **`UserPromptSubmit`-in-plugin bug (anthropics/claude-code#10225).** UserPromptSubmit hooks declared in plugin `hooks.json` register and match but never execute. Other hook types (SessionStart, PreToolUse, Stop, PostToolUse) work fine. Discovered during V18 web-search; pivoted V18's universal-behaviour rules from UserPromptSubmit to SessionStart. If the bug closes upstream and per-turn re-injection becomes valuable (e.g. very long sessions), revisit moving the rules back.

---
*No-code method — Version 23.*
