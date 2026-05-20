# Inventory — current architecture

Two-layer split and final plugin component list. Living document — current state, not history. Originated as V17's design after the Opus feasibility check (`claude-code-plugin-feasibility-response.md`); revised as decisions land.

## The two-layer split

**Source-of-truth content (per-project):** filled-in `UX.md`, `BACKLOG.md`, `MANIFEST.md`, `CLAUDE.md`, and any project-specific additional SoT docs.

**Mechanical process (becomes plugin):** all hooks, subagents, skills, slash commands, and bundled artefacts orchestrating Claude Code in a project using the method.

Three sub-categories on the plugin side (V17 walkthrough):

- **Process** — phase orchestration (build sequence, routes, drift checks, fold-in).
- **Schemas** — what per-project docs must look like (was `DOC-STRUCTURE.md`).
- **Behaviour contract** — how Claude must act (push back, no-stealth-fix, red-flag surfacing, etc.).

## Method-side doc fates

| Doc | Home | Plugin component | Notes |
|---|---|---|---|
| `Crash course.md` | Method-dev repo root | Linked from plugin README (humans-only reference) | Updated as plugin architecture lands (V22 + V25 + V26); fully rewritten as standalone primer in V30. |
| `CLAUDE-TEMPLATE.md` | Plugin | Template, scaffolded by `/adopt` skill-command (V29 — formerly `/init-project`) | **Path block format must change to fenced YAML/JSON in V18** for hook parsing. |
| `BACKLOG-TEMPLATE.md` | Plugin | Template, scaffolded by `/adopt` | |
| `MANIFEST-TEMPLATE.md` | Plugin | Template, scaffolded by `/adopt` | |
| `UX-TEMPLATE.md` | Plugin | Template, scaffolded by `/adopt` | |
| `ADDITIONAL-DOC-TEMPLATE.md` | Plugin | Template, scaffolded by `/add-sot-doc <name>` | |
| `DOC-STRUCTURE.md` | Plugin | Bundled reference doc at `plugin/docs/DOC-STRUCTURE.md` (V30); read by planning, before-build, and adopt subagents when their *Mode* tag applies (planning, migration). | |
| `NO-CODE-METHOD.md` | Plugin | Source-of-truth prose at `plugin/docs/NO-CODE-METHOD.md` (V30); subagents (planning, before-build, after-build) read it at session start via read-spec-on-entry. Retirement of the prose file not scheduled. | |

## Project-side doc fates

| Doc | Home |
|---|---|
| `UX.md` | Per-project; **read-only to Claude** (PreToolUse hook enforces) |
| `BACKLOG.md` | Per-project; read/write to Claude (discussion-contract in subagent prompts) |
| `MANIFEST.md` | Per-project; read/write to Claude |
| `TEST-LOG.md` | Per-project; read/write to Claude (test-confirmation gate per V26 — V27 hook enforcement) |
| `CLAUDE.md` | Per-project; **path block in fenced YAML/JSON** for hook parsing |
| Additional SoT docs | Per-project; read-only to Claude |

## Plugin components — final list

### Hooks (deterministic enforcement)

- **SessionStart hook.** Two responsibilities, both injected as `additionalContext`: (a) universal behavioural rules — push back on assumptions, surface red flags, plain English (V18); (b) foundational reads (CLAUDE.md, path block, SoT docs), template-state detection, resume detection (top build batch in `BACKLOG.md`), a version-footer mismatch tripwire (each SoT doc's footer vs. the plugin's current method version; mismatches surfaced in the state summary), a **TEST-LOG tripwire** (V27 — when `TEST-LOG.md` has previous-batch rows with `Confirmed Explicitly: No`, inject a routing override directing main Claude to the planning subagent regardless of opener classification, so the per-row read-back per `NO-CODE-METHOD.md` → *During planning* Rule 2 runs before any new work), and a prose state summary hinting at the route — added V21 (state summary + footer tripwire), V27 (TEST-LOG tripwire + `TEST-LOG.md` in `SPINE_FILENAMES`). **Three-tier behaviour:** tier 1 (non-method folder — no `CLAUDE.md`, no method-footer spine docs) emits nothing; plugin invisible. Tier 2 (partial — `CLAUDE.md` with unparseable path block, or spine docs without `CLAUDE.md`) emits universal rules + a single-paragraph gap flag pointing at `/adopt` (V29 — formerly `/init-project` and `/migrate`, now unified). Tier 3 (complete) emits universal rules + full state summary, including the TEST-LOG tripwire block when fired. Route classification of the opener stays with Claude — the hook flags only deterministic structural state, with the V27 TEST-LOG tripwire as the one routing-override exception. *Replaces the original "always-loaded core skill" idea (skill bodies aren't always-loaded). Originally planned as `UserPromptSubmit` for per-turn re-injection, but plugin `UserPromptSubmit` hooks don't execute (anthropics/claude-code#10225). SessionStart works in plugins and is functionally equivalent given the method's `/clear`-per-build discipline — every new session re-fires the hook. Project root via stdin `cwd` JSON, not `$CLAUDE_PROJECT_DIR` (broken for plugin hooks per anthropics/claude-code#9447).*
- **PreToolUse hook (consolidated, multiple checks).**
  - (a) Read-only enforcement on locked files (`UX.md`, additional SoT docs). **Shipped V19.**
  - (b) Fold-in redirect: `UX.md` write attempts redirected to a `[FOLD-IN PENDING]` block in `BACKLOG.md`. **Shipped V19** (redirect is the deny-reason text; Claude writes the block).
  - (c) Batch file-list enforcement during `batch-executor`. **Shipped V25.** Parses `BACKLOG.md` via `plugin/scripts/parse_backlog.py` at edit-time to look up the current top batch's `Files:` list; blocks Edit/Write/MultiEdit on any file not on it. Prerequisite carve-outs appear on the list with `[Prerequisite, not in plan]` so the boundary updates as the batch evolves.
  - (d) MANIFEST/UX read-before-edit enforcement. *Deferred from V25 — blocked by the MANIFEST.md path-mapping schema gap (`planning/OPEN-QUESTIONS.md`). Rule lives in the SessionStart-injected universal-behaviour and is followed when Claude remembers; no hook enforcement until the schema resolves.*
  - (e) Serves-line check on `BACKLOG.md` build batch additions. **Shipped V22.** Parses every `Serves UX.md: <entry>.` line in proposed new content (Edit `new_string`, Write `content`, MultiEdit per-edit `new_string`s), matches each named entry against UX.md's Functionalities section with **case-insensitive exact match after whitespace-trim** (Q3 decision). Misses deny with a redirect listing unmatched names plus a sample of known entries so Claude can spot a typo or recognise it needs to fold in first. `Serves <ADDITIONAL>.md:` lines pass through (out of V22 scope).
  - (f) Test-confirmation gate on `Task` → `batch-executor` invocation. **Shipped V27.** `PreToolUse` matcher extended from `Edit|Write|MultiEdit` to `Edit|Write|MultiEdit|Task`; hook script dispatches on `tool_name` (writing tools → (1)–(3); `Task` → (f)). (f) fires only when `subagent_type == no-code-method:batch-executor`; other Task invocations pass through. Reads `TEST-LOG.md` via the path block, parses the 8-column data rows, identifies the previous build batch's session from `BUILD-LOG.md`'s first `## <token>` heading (path-block lookup first, then project-root fallback). Denies if rows from that session have `Confirmed Explicitly: No`. **Hook fallback** when `BUILD-LOG.md` is missing OR unparseable: "any row with `Confirmed Explicitly: No` blocks" — strict but safe per V26 Q3 + V27 Q4. The unparseable-vs-missing distinction is surfaced in the deny message. Defined by Rule 3 (`NO-CODE-METHOD.md` → *Method contract → Prohibited → Test-confirmation gate*); made trustworthy by Rule 1 (*Required → Never infer completion*); closed each session by Rule 2 (per-row read-back as first sub-step of *During planning*, owned by planning per V27 extension).
- **Stop hook (build sequencer).** **Shipped V25** at `plugin/hooks/stop.py`, **extended V27**. After `batch-executor` finishes a turn, parses `BACKLOG.md` via `parse_backlog.py` to find the top unticked build batch. If one exists, returns `{"decision": "block", "reason": "<batch payload>"}` to redirect into the next batch-executor. If none exists (all batches ticked, or no batches), the V27 extension checks whether after-build has run for the just-completed batch — signal is BACKLOG.mtime vs. TEST-LOG.mtime: when BACKLOG is more recently modified (a file just ticked) AND the Build batches section has at least one `- [x]` bullet, after-build is presumed pending. Hook emits a `decision: block` redirect to `no-code-method:after-build` with a short prose reason — the after-build subagent reads BACKLOG.md and TEST-LOG.md itself to figure out which batch it's recapping. **Respects `stop_hook_active`** — one redirect per user turn (D1: explicit user gating between batches and between batch-and-after-build).

### Subagents (probabilistic, behavioural)

- **planning** — test-note sort (Suggestions/Discoveries), drift checks (**inlined — drift-checker is NOT a separate subagent**, since subagents can't spawn subagents), mixed-input secondary sort, `BACKLOG.md` edits, Discoveries → planning batch promotion, recap. **Shipped V22** at `plugin/agents/planning.md`, **extended V27**: (1) **per-row read-back of pending TEST-LOG.md rows** as the first sub-step of *During planning* (Rule 2 — closes the test session opened by after-build's recap); read-back protocol pushes back on bulk confirmations and requires a reason for any Skipped row. (2) **Inline `[Requested]` / `[Suggested]` label-writing** on every change-list bullet added to a build batch in BACKLOG.md (V27 Q3 — labels live on change-list items, not in `Files:`). after-build reads these labels at recap. Invoked by main Claude via Task with `subagent_type: "no-code-method:planning"` after opener classification (`test notes` / `feature request` / `scope question` / `mixed`, per `NO-CODE-METHOD.md` → *Handoff to the planning subagent*), or when the SessionStart V27 TEST-LOG tripwire fires (routing override — see SessionStart). Drift checks always run; only skip is "nothing built yet" (Q2; V26 fourth drift check on TEST-LOG ↔ what's-been-touched runs alongside the original three). The `/plan` slash command is *not* yet shipped — auto-route remains the only invocation path; `/plan` lands later.
- **before-build** — validate top build batch, enumerate `Files:`, estimate verification burden, propose splits when Batch-sizing requires. **Shipped V25** at `plugin/agents/before-build.md`, **extended V27** with a label-preservation rule (when halt-C splits a batch, every change-list bullet's `[Requested]` / `[Suggested]` label travels with it — no re-classifying to `[Suggested]` because items are "now in a different batch"). Invoked via `/before-build`. Rules read at runtime from `NO-CODE-METHOD.md` → *Before build* (read-spec-on-entry — see `OPEN-QUESTIONS.md` on subagent rule-loading divergence). Halt-and-confirm protocols cover (a) no top batch, (b) malformed `BACKLOG.md` or unresolvable `Serves UX.md:` name, (c) change list too vague to enumerate Files:, (d) verification burden triggers a split.
- **batch-executor** — runs one build batch per fresh context. **Shipped V25** at `plugin/agents/batch-executor.md`, **scope-reduced V27** (the *After every build* responsibilities V25 absorbed — MANIFEST.md update, build recap, user prompts — move out to after-build; batch-executor's turn now ends with a short completion note when the last file ticks, and Stop routes to after-build). Invoked via `/build` or by Stop-hook redirect after the previous batch finishes. Receives a JSON payload from `parse_backlog.py` (batch heading, change list, Files: with tick state, Serves lines) via prompt. Edits each unticked file in Files: order, ticks `BACKLOG.md` per-file (partial-completion-safe). PreToolUse (c) enforces the Files: boundary at edit-time. Halt-and-confirm covers the two exceptions in `NO-CODE-METHOD.md` → *Prohibited* (prerequisite carve-out, re-batching carve-out); the `[Prerequisite, not in plan]` and `[Re-batch, not in plan]` recap labels these imply are now surfaced by after-build (which sees carve-out evidence in BACKLOG.md). Rules inlined in the agent body rather than read-spec-on-entry (V25 Decision 4; see `OPEN-QUESTIONS.md`).
- **after-build** — **Shipped V27** at `plugin/agents/after-build.md`. Owns the *After every build* phase: updates `MANIFEST.md` silently (fully automatic per V27 Q2), generates the plain-English build recap with `[Requested]`/`[Suggested]` labels from BACKLOG.md (V27 Q3) plus any `[Prerequisite, not in plan]` / `[Re-batch, not in plan]` labels visible in BACKLOG.md from batch-executor's carve-outs, opens the test session by appending blank-`Status` rows to TEST-LOG.md (one per user-observable behaviour the recap names), and prompts the user to refresh, test, and bring per-row outcomes to next planning. Identifies the just-completed batch as the topmost fully-ticked batch in BACKLOG.md. **Idempotent** — if rows for the current session already exist in TEST-LOG.md, exits with a brief "test session already open" note rather than duplicating (covers Stop-hook re-fires when the user continues after after-build's first run). Invoked by Stop-hook redirect (V27 Q1); no slash-command alternative. Rules read at runtime from `NO-CODE-METHOD.md` → *After every build* (read-spec-on-entry, matching planning and before-build). Does NOT do the per-row test-confirmation read-back — relocated to planning per V26 Q4 (read-back is the test-session-*close*, owned by planning; test-session-*open* is owned by after-build).
- **adopt** — **Shipped V29** at `plugin/agents/adopt.md`. Owns the five-case adoption dispatch: case 1 (empty folder → 4-question walk + scaffold), case 2 (existing code, no docs → scaffold alongside, or cancel writing `.no-code-method-skip`), case 3 (existing code, foreign `CLAUDE.md` → migrate / overwrite / leave-alone), case 4 (already method-managed → refresh-templates or cancel), case 5 (opted out → clear marker or cancel). Replaces the V17-planned **new-project** and **migration** subagents (folded into cases 1+2 and case 3 respectively). Invoked by the `/adopt` skill-command. Cases 1 and 2 use `plugin/skills/adopt/scripts/scaffold.py` for the scaffold step; case 3 migrate walks foreign `CLAUDE.md` section-by-section via Edit; case 5 clears `.no-code-method-skip` via Bash `rm`. PreToolUse V29 gate exempts `/adopt` subagent's tool calls so scaffolding works against an unadopted folder (whose paths would otherwise be locked or boundary-blocked).

### Slash commands

Two patterns exist in the current plugin:

- **Commands-directory pattern** (newer, V25). Files at `plugin/commands/<name>.md` with frontmatter `description:` + optional `allowed-tools:`, and a body that is the prose prompt main Claude executes (spawning subagents via Task when needed). Used by `/before-build` and `/build`.
- **Skill-with-flags pattern** (older, V19). Skills with `disable-model-invocation: true`, `user-invocable: true`. Claude Code v2.1.101 merged commands into skills; this pattern is the result. Used by `/adopt` (V29 — formerly `/init-project`).

**As of V29, four commands shipped:** `/adopt` (V29, skill-with-flags — replaces V19's `/init-project`), `/before-build` (V25, commands-directory), `/build` (V25, commands-directory). Remaining commands below are forward-looking architectural reference with planned-V annotations — a reader (human or Claude) should not assume *Pending* commands exist in the installed plugin.

- `/adopt` → five-case adoption dispatch (empty / existing-code-no-docs / existing-code-foreign-docs / already-adopted / opted-out). Scaffolds the 5 spine templates in cases 1 and 2 (CLAUDE, BACKLOG, MANIFEST, UX, TEST-LOG; ADDITIONAL-DOC handled by `/add-sot-doc`); migrates / overwrites / leaves-alone in case 3; refreshes templates in case 4; clears or keeps the `.no-code-method-skip` opt-out marker in case 5. **Shipped V29** — replaces V19's `/init-project` and the V17-planned `/new-project` + `/migrate`. Skill body at `plugin/skills/adopt/SKILL.md` invokes the `no-code-method:adopt` subagent. Scaffold script at `plugin/skills/adopt/scripts/scaffold.py`.
- `/add-sot-doc <name>` → scaffolds additional-doc template. *Pending — not yet scheduled in `PLAN.md`.*
- `/plan` → planning subagent. *Pending — auto-route via main-Claude classification is the only invocation path as of V22; explicit `/plan` skill-command lands in a future session.*
- `/before-build` → before-build subagent. **Shipped V25** at `plugin/commands/before-build.md`. Commands-directory; `allowed-tools: Task`.
- `/build` → triggers batch-executor (explicit entry; default is auto-continuation via Stop hook). **Shipped V25** at `plugin/commands/build.md`. Commands-directory; `allowed-tools: Read, Bash, Task`. Argument-less per V25 Q3 (out-of-order batches handled by reordering BACKLOG.md during planning).

### Bundled artefacts

- 6 templates (CLAUDE, BACKLOG, MANIFEST, UX, TEST-LOG, ADDITIONAL-DOC) under `plugin/templates/`. The 5 spine templates are scaffolded by `/adopt` (V29 — formerly `/init-project`); ADDITIONAL-DOC lands via `/add-sot-doc`.
- `plugin/scripts/parse_backlog.py` — shared BACKLOG.md parser used by the Stop hook, PreToolUse (c), and `/build`. Single source of truth for BACKLOG.md structure interpretation.
- `plugin/scripts/project_state.py` — shared module imported by `pre_tool_use.py` and `stop.py` (V28 extraction). Holds project-state readers: path-block extraction from CLAUDE.md, BACKLOG parser invocation, TEST-LOG row parsing, BUILD-LOG session-narrowing, plus the `is_test_session_open` predicate that backs both V27's PreToolUse gate (check (f)) and V28's Stop-hook silent-exit. Single definition of "what does the project state currently say."
- `plugin/docs/NO-CODE-METHOD.md` — method-spec prose at canonical bundled path (V30 relocation from repo root). Read by planning, before-build, and after-build subagents at session start via `${CLAUDE_PLUGIN_ROOT}/docs/NO-CODE-METHOD.md`.
- `plugin/docs/DOC-STRUCTURE.md` — structural-spec reference at canonical bundled path (V30 relocation from repo root). Read by planning, before-build, and adopt subagents when their *Mode* tag applies (planning, migration).

## Design decisions taken in V17

- **D1 — build orchestration mode.** Stop hook proposes next batch; user gates. Naturally enforced by `stop_hook_active` loop prevention.
- **D2 — planning vs before-build subagent.** Two separate subagents for clean isolation of the file-list-lock step.
- **D3 — auto-route on test-note paste.** SessionStart hook surfaces structural state; main Claude classifies the opener (test notes / feature request / scope question / mixed) and spawns planning via Task with the classification as `primary_intent`. (V17 wording said the hook itself auto-launches the subagent; in implementation, hooks inject context and Claude decides — the route remains automatic but main Claude is the launcher.) Explicit `/plan` is the override (not yet shipped — lands later).
- **A — V18 = research session.** Not needed; research done by Opus during V17. V18 becomes the first build session.
- **B — Vxx folders ARE method versions.** Contents expand to include plugin components alongside (and eventually replacing) method docs. Footer convention extends.

## Architecture revisions made in V17 (vs walkthrough first-pass)

| Original (Chunks A/B/C) | Revised | Reason |
|---|---|---|
| `drift-checker` subagent invoked BY `planning` subagent | Inline drift logic into planning subagent prompt | Subagents can't spawn other subagents |
| Always-loaded core skill (universal behaviours) | `SessionStart` hook injecting `additionalContext` | Skill bodies aren't always-loaded. (V17 first chose `UserPromptSubmit`; V18 pivoted to `SessionStart` because `UserPromptSubmit`-in-plugin is blocked by anthropics/claude-code#10225.) |
| `batch-executor` enforces file-list isolation directly | PreToolUse hook enforces; `batch-executor` receives the list via prompt | Subagent config restricts tools, not paths |
| `CLAUDE.md` path block as free-form markdown bullets | Fenced YAML/JSON code block | Robust hook parsing |
| Slash commands as standalone components | Slash commands as skills with `disable-model-invocation: true` + `user-invocable: true` + `agent: <subagent>` | Claude Code v2.1.101 merged commands into skills |
| Stop hook auto-chains batches | One redirect per user turn (`stop_hook_active`) | Platform-level loop prevention |

## Risks taken on (from Opus feasibility response)

- Hook fragility around shell environments — defensive shell scripts required; test on a clean shell.
- Stop-hook infinite loops if `stop_hook_active` not respected — test the loop-exit path before shipping.
- Plugin skills can't define hooks (security) — all hook logic at plugin level (`hooks/hooks.json`), not inside individual skills.
- Subagent context isolation: only channel in is the prompt — long prompts eat the subagent's own context budget.
- Cache invalidation on plugin update is manual — `/reload-plugins` required.
- The "vibe coder distributing a plugin" UX gap — local-install requires CLI muscle; consider a one-click install script.
- **Method-still-being-refined risk acknowledged and accepted at V17 close.** Current method docs are large enough that context bloat is itself preventing realistic adherence testing; the plugin's per-component context isolation is the testability fix, not a freeze of an unstable method.
- **`UserPromptSubmit`-in-plugin bug (anthropics/claude-code#10225).** UserPromptSubmit hooks declared in plugin `hooks.json` register and match but never execute. Other hook types (SessionStart, PreToolUse, Stop, PostToolUse) work fine. Discovered V18 web-search; pivoted V18's universal-behaviour rules from UserPromptSubmit to SessionStart. If the bug closes upstream and per-turn re-injection becomes valuable (e.g. very long sessions), revisit moving the rules back.

---
*No-code method — Version 30.*
