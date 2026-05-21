# Platform capabilities audit — 2026-05-21

## Purpose

Audit of Claude Code platform features that sovereign-implementer could use but currently doesn't. The method's plugin currently uses 3 of 18 hook events (SessionStart, PreToolUse, Stop) and 1 of 5 hook types (command). This doc catalogues what's available and what's worth pursuing.

## Source

Cross-reference of Claude Code docs, changelog (Jan–May 2026), and the active session's own toolset against sovereign-implementer's current plugin surface.

---

## Part 1: Prose directives that could become plugin automation

These are rules currently living in method docs (universal-behaviour.md, DOC-STRUCTURE.md, subagent bodies) that the user follows because Claude reads and applies them — with no structural enforcement.

### 1. BACKLOG.md parse validation after edits

**Current state:** If a subagent makes a malformed edit to BACKLOG.md, nothing catches it until the Stop hook or `/build` runs `parse_backlog.py` and silently gets an empty result (`{}` + exit 0).
**Pluginification:** PostToolUse hook watching edits to BACKLOG.md. Runs `parse_backlog.py` immediately after each edit. Surfaces parse failures at the point of introduction.
**Rule source:** Implicit structural assumption across all subagent bodies and the Stop hook.

### 2. `Serves <DOC>:` validation for additional source-of-truth docs

**Current state:** PreToolUse validates `Serves UX.md:` lines (checks named entries exist in UX.md). Consumer projects can declare additional source-of-truth docs in their CLAUDE.md path block. `Serves DESIGN-PRINCIPLES.md: <entry>` lines are not validated.
**Pluginification:** Extend existing PreToolUse serves-line check to read all docs declared in the path block, not just UX.md.
**Rule source:** DOC-STRUCTURE.md ("planning batches resolving to these docs fold into the doc, not UX.md").

### 3. Red flags non-empty warning at SessionStart

**Current state:** BACKLOG.md has a Red flags section for security/privacy/safety items. Nothing checks whether it has content at session start.
**Pluginification:** SessionStart hook addition. Already reads BACKLOG.md for test-session tripwire and batch detection — add a check for non-empty Red flags section and surface prominently in the advisory.
**Rule source:** DOC-STRUCTURE.md (red flags section definition) + universal-behaviour.md (red flag surfacing behaviour).

### 4. Fold-in aging reminder

**Current state:** `[FOLD-IN PENDING]` blocks in BACKLOG.md include a `Surfaced [date]` field. Nothing tracks how long they've been sitting or nudges if they accumulate across sessions.
**Pluginification:** Planning subagent scans fold-ins at session start; flags any older than 1–2 planning sessions. The date field is already in the canonical format.
**Rule source:** DOC-STRUCTURE.md (fold-in format and lifecycle).

### 5. Context preservation before compaction

**Current state:** When a session runs long, Claude Code compacts the conversation. If a build is mid-flight, critical state (which batch, which files ticked, which subagent active) can be lost. No doc names this risk; no protection exists.
**Pluginification:** PreCompact hook. Fires before compaction. Injects a structured summary of current build state so it survives the compaction.
**Rule source:** None — this is an unaddressed risk, not a prose directive.

### 6. Opener routing classification

**Current state:** "Routing main-Claude's openers" in universal-behaviour.md is a prose table Claude reads and applies. Classification happens inside Claude's reasoning with no enforcement.
**Pluginification:** UserPromptSubmit hook. Fires when user submits a prompt. Parses the message, classifies it (test notes / feature request / resume / question), injects routing decision as `additionalContext`. Makes routing structural rather than advisory.
**Rule source:** universal-behaviour.md ("Routing main-Claude's openers" section).

---

## Part 2: New hook events the method doesn't use

The method uses SessionStart, PreToolUse, and Stop. These are available but unused:

| Event | When it fires | Potential method use |
|---|---|---|
| **PostToolUse** | After a tool completes successfully | BACKLOG.md parse validation (item 1 above); other structural checks after edits |
| **PostToolUseFailure** | After a tool execution fails | Could log or surface build failures more clearly |
| **UserPromptSubmit** | When user submits a prompt | Opener routing classification (item 6 above) |
| **SessionEnd** | When session closes | Consumer-project close-time checks: "TEST-LOG has blank-Status rows," "fold-ins older than 2 sessions" |
| **SubagentStart** | When a subagent spawns via Task | Logging, context injection for specific subagents |
| **SubagentStop** | When a subagent finishes | More precise batch-executor → after-build handoff (currently Stop hook uses mtime heuristics). Known reliability bugs as of May 2026 |
| **PreCompact** | Before context compaction | Build state preservation (item 5 above) |
| **TaskCompleted** | When a task completes | Alternative handoff signal to SubagentStop |
| **Notification** | When Claude sends a notification | Not obviously useful for the method |
| **PermissionRequest** | When Claude requests tool permission | Could approve/reject tool access; overlaps with PreToolUse |
| **PostToolBatch** | After parallel tool calls complete | Not obviously useful for the method |
| **Setup** | During initial setup | Not obviously useful for the method |
| **TeammateIdle** | In Agent Teams scenarios | Not applicable (method is single-user) |
| **ConfigChange** | When settings change | Not obviously useful for the method |
| **WorktreeCreate** | When entering/creating worktrees | Not obviously useful for the method |

## Part 3: New hook types the method doesn't use

The method uses only command hooks (Python scripts reading JSON from stdin). Four other hook types exist:

### Prompt hooks

Send a prompt to a Claude model for evaluation. The LLM returns a judgment. Use case: checks that are awkward as regex but trivial as natural language — "is this edit semantically within the scope of this batch?" or "does this change introduce a user-observable behaviour not covered by the current UX.md?"

**Trade-off:** Adds latency and cost per evaluation. Current regex-based checks are fast and deterministic. Best for checks that are genuinely hard to express mechanically.

### Agent hooks

Spawn a subagent that can use tools (read files, grep, etc.) to verify conditions before deciding to block or allow. More powerful than command hooks, which can only work with the JSON payload on stdin.

**Trade-off:** Heaviest hook type. Experimental — may change. Best for complex validations that need to read multiple files.

### HTTP hooks

Send JSON input as an HTTP POST request. For integrating with external services.

**Trade-off:** Requires a running server. Not useful for the method currently.

### MCP tool hooks

Call a tool on an MCP server. For integrating with external tool ecosystems.

**Trade-off:** Requires MCP server configuration. Not useful for the method currently.

---

## Part 4: Platform capabilities from the active toolset

These are capabilities available in Claude Code sessions that the method could reference or instruct subagents to use, but currently doesn't.

### spawn_task

Creates a clickable chip the user can spin off into a separate session and worktree. The method's "flag out-of-scope improvements" directive (universal-behaviour.md) is currently prose — Claude mentions improvements in chat text. `spawn_task` is the structural version: a discrete, actionable flag the user can dismiss or act on later. Same applies to red flag surfacing.

**Implication:** The flag taxonomy in universal-behaviour.md (out-of-scope improvement, red flag, user-facing behaviour change) could instruct Claude to use `spawn_task` for the first two, making flags persistent and actionable rather than ephemeral chat text.

### Claude Preview tools

`preview_start`, `preview_screenshot`, `preview_click`, `preview_fill`, `preview_inspect`, `preview_console_logs`, `preview_network`. Claude can start a browser preview of a dev server, take screenshots, click through UI flows, read console output, and monitor network requests.

**Implication for V48:** V48 (test split) was scoped assuming "Look and Click" tests require manual user verification. Claude Preview could automate visual testing — Claude starts a preview, takes screenshots, clicks through flows, reads console logs. This potentially changes the boundary between Claude-automatable and user-only test types.

### mark_chapter

Marks the start of a new phase in a session, creating a navigable table of contents. Build sessions have natural phases (planning, before-build, build, after-build, test). Subagents or the Stop hook could mark chapters at phase transitions, making long sessions easier to navigate.

### Scheduled tasks (CronCreate, ScheduleWakeup)

Periodic or one-shot scheduled automation. Could enable health checks (weekly scan of method doc integrity) or reminders (fold-in aging, stale TEST-LOG rows). Consumer-project value is low — the method's cadence is session-based, not time-based.

---

## Part 5: Interaction with upcoming build sessions

### V48 scope flag

V48 (test split + non-UI test types) defines four test types and assumes "Look and Click" is user-only. Claude Preview tools may change this assumption. V48's scope should be revisited to account for Claude Preview before the session runs.

### Agent frontmatter hooks (track for future)

Subagents can now define their own PreToolUse/PostToolUse/Stop hooks scoped to their lifecycle. This could simplify the global PreToolUse hook's complex branching ("am I in a build vs. planning context?") by letting each subagent carry its own rules. Known bugs as of May 2026 (issue #18392) — not ready to build on, but worth tracking. If it stabilises, it could inform a future architectural refactor of the hook system.

### SubagentStop for handoffs (track for future)

The Stop hook uses mtime heuristics to detect "batch-executor just finished." SubagentStop would give a precise signal. Known reliability issues as of May 2026 (issue #27755). Worth tracking; if it stabilises, it replaces the fragile heuristic.

---

## Status

This is a research document. No decisions have been made. Items from Part 1 will be checked against existing build batches and filed as OPEN-QUESTIONS entries if they don't overlap. Items from Parts 2–5 are reference material for future scoping.

Filed: 2026-05-21.
