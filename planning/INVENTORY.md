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
| `Crash course.md` | Plugin | Bundled docs (humans-only reference) | Updated as the plugin architecture lands (V22 + V25 + V26 so far). |
| `CLAUDE-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` skill-command | **Path block format must change to fenced YAML/JSON in V18** for hook parsing. |
| `BACKLOG-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `MANIFEST-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `UX-TEMPLATE.md` | Plugin | Template, scaffolded by `/init-project` | |
| `ADDITIONAL-DOC-TEMPLATE.md` | Plugin | Template, scaffolded by `/add-sot-doc <name>` | |
| `DOC-STRUCTURE.md` | Plugin | Skill body OR bundled reference doc (decision deferred to V26) | |
| `NO-CODE-METHOD.md` | Plugin | Distributed across components (skills + hooks + subagents); original retired in V27 | |

## Project-side doc fates

| Doc | Home |
|---|---|
| `UX.md` | Per-project; **read-only to Claude** (PreToolUse hook enforces) |
| `BACKLOG.md` | Per-project; read/write to Claude (with discussion-contract in subagent prompts) |
| `MANIFEST.md` | Per-project; read/write to Claude |
| `TEST-LOG.md` | Per-project; read/write to Claude (test-confirmation gate per V26 — V27 hook enforcement) |
| `CLAUDE.md` | Per-project; **path block in fenced YAML/JSON** for hook parsing |
| Additional SoT docs | Per-project; read-only to Claude |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Two responsibilities, both injected as `additionalContext`: (a) the universal behavioural rules — push back on assumptions, surface red flags, plain English — installed in V18; (b) foundational reads (CLAUDE.md, path block, SoT docs), template-state detection, resume detection (top build batch in `BACKLOG.md`), a version-footer mismatch tripwire (each SoT doc's footer compared against the plugin's current method version; mismatches surfaced as a state-summary line), and a prose state summary that hints at the route — all added in V21. **Three-tier behaviour:** tier 1 (non-method folder — no `CLAUDE.md` and no method-footer spine docs) emits nothing; the plugin is invisible. Tier 2 (partial method shape — e.g. `CLAUDE.md` present but path block unparseable, or spine docs present without `CLAUDE.md`) emits universal rules + a single-paragraph gap flag pointing at `/init-project` or `/migrate`. Tier 3 (complete method project) emits universal rules + the full state summary. Route classification of the user's opener stays with Claude — the hook flags only deterministic structural state. *Replaces the original "always-loaded core skill" idea (skill bodies aren't always-loaded). Originally planned as a `UserPromptSubmit` hook for per-turn re-injection, but `UserPromptSubmit` hooks declared in plugin `hooks.json` don't execute due to anthropics/claude-code#10225. SessionStart works in plugins today and is functionally equivalent given the method's `/clear`-after-every-build discipline — every new session re-fires the hook. Project root is located via the stdin `cwd` JSON field rather than `$CLAUDE_PROJECT_DIR`, which is broken for plugin hooks per anthropics/claude-code#9447.*
- **PreToolUse hook (consolidated, multiple checks).**
  - (a) Read-only enforcement on locked files (`UX.md`, additional SoT docs). **Shipped V19.**
  - (b) Fold-in redirect: `UX.md` write attempts redirected to a `[FOLD-IN PENDING]` block in `BACKLOG.md`. **Shipped V19** (the redirect is the deny-reason text; Claude writes the block itself).
  - (c) Batch file-list enforcement during `batch-executor`. **Shipped V25.** Parses `BACKLOG.md` via `plugin/scripts/parse_backlog.py` at edit-time to look up the current top batch's `Files:` list; blocks Edit/Write/MultiEdit on any file not on that list. Prerequisite carve-out additions appear on the list with a `[Prerequisite, not in plan]` label so the boundary updates as the batch evolves.
  - (d) MANIFEST/UX read-before-edit enforcement. *Deferred from V25 — blocked by the MANIFEST.md path-mapping schema gap (see `planning/OPEN-QUESTIONS.md`). Rule lives in the SessionStart-injected universal-behaviour and is followed when Claude remembers, but no hook enforcement until the schema question resolves.*
  - (e) Serves-line check on `BACKLOG.md` build batch additions. **Shipped V22.** Parses every `Serves UX.md: <entry>.` line in the proposed new content (Edit's `new_string`, Write's `content`, MultiEdit's per-edit `new_string`s), matches each named entry against UX.md's Functionalities section with **case-insensitive exact match after whitespace-trim** (Q3 decision). Misses deny with a redirect message listing the unmatched names and a sample of known entries so Claude can spot a typo or recognise it needs to fold in first. `Serves <ADDITIONAL>.md:` lines for additional source-of-truth docs are out of V22 scope and pass through.
  - (f) Test-confirmation gate on `Task` → `batch-executor` invocation. *V27 implementation per V26 spec.* Reads `TEST-LOG.md`, finds rows whose `Session` matches the previous build batch's session and whose `Confirmed Explicitly` is `No`, denies invocation if any exist. **Hook fallback** when the project doesn't keep `BUILD-LOG.md` (the session-identification source): "any unconfirmed row blocks" — strict but safe, V26 decision. Defined by Rule 3 (`NO-CODE-METHOD.md` → *Method contract → Prohibited of Claude → Test-confirmation gate*); made trustworthy by Rule 1 (*Required of Claude → Never infer completion*); closed each session by Rule 2 (per-row read-back as first sub-step of *During planning*).
- **Stop hook (build sequencer).** **Shipped V25** at `plugin/hooks/stop.py`. After `batch-executor` finishes a turn, parses `BACKLOG.md` via `plugin/scripts/parse_backlog.py` to find the top unticked build batch, then returns `{"decision": "block", "reason": "<batch payload>"}` to redirect into the next batch-executor invocation. **Respects `stop_hook_active`** — one redirect per user turn (matches D1: explicit user gating between batches).

### Subagents (probabilistic, behavioural)

- **planning** — test-note sort (Suggestions/Discoveries), drift checks (**inlined — drift-checker is NOT a separate subagent**, since subagents can't spawn subagents), mixed-input secondary sort, `BACKLOG.md` edits, Discoveries → planning batch promotion, recap. **Shipped V22** at `plugin/agents/planning.md`. Invoked by main Claude via the Task tool with `subagent_type: "no-code-method:planning"` after main Claude classifies the user's opener as `test notes` / `feature request` / `scope question` / `mixed` (per `NO-CODE-METHOD.md` → *Handoff to the planning subagent*). Drift checks always run on every planning session; only skip case is "nothing has been built yet" (Q2 decision). The `/plan` slash command is *not* yet shipped — for V22, the auto-route via main-Claude classification is the only invocation path; `/plan` lands in a later session.
- **before-build** — validate the top build batch, enumerate the `Files:` list, estimate verification burden, propose splits when the Batch-sizing principle requires. **Shipped V25** at `plugin/agents/before-build.md`. Invoked via the `/before-build` slash-command. Rules read at runtime from `NO-CODE-METHOD.md` → *Before build* (read-spec-on-entry pattern — see `OPEN-QUESTIONS.md` entry on subagent rule-loading divergence). Halt-and-confirm protocols cover (a) no top batch, (b) malformed `BACKLOG.md` or unresolvable `Serves UX.md:` name, (c) change list too vague to enumerate Files:, (d) verification burden triggers a split.
- **batch-executor** — runs one build batch per fresh context. **Shipped V25** at `plugin/agents/batch-executor.md`. Invoked via the `/build` slash-command or by Stop-hook redirect after the previous batch finishes. Receives a JSON payload from `parse_backlog.py` (batch heading, change list, Files: list with tick state, Serves lines) via prompt. Edits each unticked file in Files: order, ticks `BACKLOG.md` per-file (partial-completion-safe), and produces a build recap with `[Requested]`/`[Suggested]`/`[Prerequisite, not in plan]`/`[Re-batch, not in plan]` labels per the After every build rules. The PreToolUse hook (c) enforces the Files: boundary at edit-time. Halt-and-confirm protocols cover the two exceptions in `NO-CODE-METHOD.md` → *Prohibited of Claude* (prerequisite carve-out, re-batching carve-out). Rules inlined in the agent body rather than read-spec-on-entry (intentional divergence per V25 Decision 4; see `OPEN-QUESTIONS.md`).
- **after-build** — *Revival planned for V27 per V26 spec.* V25 originally absorbed the *After every build* responsibilities (MANIFEST.md update, build recap, user prompts) into the completion path of `batch-executor`, since the recap was most accurate when produced in the same context as the build itself. V26 added a *test-session-open* step to *After every build* (write one blank-`Status` TEST-LOG.md row per user-observable behaviour the recap names) — that work makes a dedicated subagent useful again. V27 moves the *After every build* responsibilities back out to a fresh `after-build` subagent at `plugin/agents/after-build.md`; the test-confirmation read-back relocates to the planning subagent (V26 Q4 decision) as the first sub-step of *During planning*.
- **new-project** — 4-prompt walk-through; queues `[FOLD-IN PENDING]` block in `BACKLOG.md`.
- **migration** — diagnostic + walk-through to bring existing docs up to spec.

### Slash commands

Two patterns exist in the current plugin:

- **Commands-directory pattern** (newer, V25). Files at `plugin/commands/<name>.md` with frontmatter `description:` + optional `allowed-tools:`, and a body that is the prose prompt main Claude executes (spawning subagents via the Task tool when needed). Used by `/before-build` and `/build`.
- **Skill-with-flags pattern** (older, V19). Skills with `disable-model-invocation: true`, `user-invocable: true`, and `agent: <subagent>`. Claude Code v2.1.101 merged commands into skills; this pattern is the result. Used by `/init-project`.

**As of V25, three commands are shipped:** `/init-project` (V19, skill-with-flags), `/before-build` (V25, commands-directory), `/build` (V25, commands-directory). The remaining commands listed below are forward-looking architectural reference, with their planned-V annotation. A reader (human or Claude) should not assume the *Pending* commands exist in the installed plugin — they are roadmap items, not current capabilities.

- `/init-project` → scaffolds 5 spine templates (CLAUDE, BACKLOG, MANIFEST, UX, TEST-LOG) into a user project (ADDITIONAL-DOC handled separately by `/add-sot-doc`). **Shipped V19**; extended in V26 to also scaffold TEST-LOG.md.
- `/new-project` → new-project subagent. *Pending — V27.*
- `/migrate` → migration subagent. *Pending — V27.*
- `/add-sot-doc <name>` → scaffolds the additional-doc template. *Pending — not yet scheduled in `PLAN.md`.*
- `/plan` → planning subagent. *Pending — auto-route via main-Claude classification is the only invocation path as of V22 (per the planning subagent entry above). Explicit `/plan` skill-command not yet shipped; future session.*
- `/before-build` → before-build subagent. **Shipped V25** at `plugin/commands/before-build.md`. Commands-directory pattern; `allowed-tools: Task`.
- `/build` → triggers batch-executor (explicit entry; default is auto-continuation via Stop hook). **Shipped V25** at `plugin/commands/build.md`. Commands-directory pattern; `allowed-tools: Read, Bash, Task`. Argument-less per V25 Q3 (out-of-order batches handled by reordering BACKLOG.md during planning).

### Bundled artefacts

- 6 templates (CLAUDE, BACKLOG, MANIFEST, UX, TEST-LOG, ADDITIONAL-DOC) under `plugin/templates/`. The 5 spine templates (excluding ADDITIONAL-DOC) are scaffolded into user projects via `/init-project`; ADDITIONAL-DOC lands separately via `/add-sot-doc`.
- `plugin/scripts/parse_backlog.py` — shared BACKLOG.md parser used by the Stop hook, the PreToolUse (c) batch-file-list check, and the `/build` slash-command. Single source of truth for BACKLOG.md structure interpretation.
- `Crash course.md` as bundled docs (not loaded into Claude's context).
- `DOC-STRUCTURE.md` content — destination decided in V26.

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
*No-code method — Version 26.*
