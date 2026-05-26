# Platform capabilities audit — 2026-05-21

## Purpose

Catalogue Claude Code features sovereign-implementer could use but doesn't. Plugin currently uses 3 of 18 hook events and 1 of 5 hook types.

---

## Part 1: Prose directives that could become plugin automation

### 1. BACKLOG.md parse validation after edits
**Current:** Malformed edits silently return `{}` later. **Fix:** PostToolUse hook running `parse_backlog.py` after each edit. **Shipped V46.**

### 2. `Serves <DOC>:` validation for additional SoT docs
**Current:** Only validates `Serves UX.md:`. **Fix:** Extend PreToolUse to all path-block docs. **Shipped V54.**

### 3. Red flags non-empty warning at SessionStart
**Current:** Nothing checks Red flags at session start. **Fix:** SessionStart addition. **Shipped V54.**

### 4. Deferred build-material aging
**Current:** No tracking of stale `[PROPOSED EDIT PENDING]` blocks. **Fix:** Planning subagent scan. **Shipped V54.**

### 5. Context preservation before compaction
**Current:** No protection when build mid-flight. **Fix:** PreCompact hook. Can only block, not inject context. **Shipped V52.**

### 6. Opener routing classification
**Current:** Prose table in universal-behaviour.md. **Fix:** UserPromptSubmit hook. **Shipped V52.**

---

## Part 2: Unused hook events

| Event | Potential use |
|---|---|
| **PostToolUse** | BACKLOG parse validation (shipped V46) |
| **PostToolUseFailure** | Log build failures |
| **UserPromptSubmit** | Opener routing (shipped V52) |
| **SessionEnd** | Close-time checks |
| **SubagentStart** | Logging, context injection |
| **SubagentStop** | Precise handoff signal (known bugs May 2026) |
| **PreCompact** | Build state preservation (shipped V52) |
| **TaskCompleted** | Alternative handoff signal |
| **Notification / PermissionRequest / PostToolBatch / Setup / TeammateIdle / ConfigChange / WorktreeCreate** | Not obviously useful |

## Part 3: Unused hook types

- **Prompt hooks** — LLM-based evaluation. Adds latency/cost; best for semantically hard checks.
- **Agent hooks** — Subagent with tool access for complex validations. Experimental.
- **HTTP hooks** — External service integration. Not currently needed.
- **MCP tool hooks** — MCP server integration. Not currently needed.

---

## Part 4: Platform capabilities from toolset

- **spawn_task** — Structural version of "flag out-of-scope improvements." Could replace ephemeral chat flags.
- **Claude Preview** — Browser automation (screenshot, click, console, network). Could automate visual testing.
- **mark_chapter** — Phase-transition markers for session navigation.
- **Scheduled tasks** — Periodic health checks. Low value for session-based method.

---

## Part 5: Interaction with build sessions

- **V48 scope:** Claude Preview may change the "Look and Click = user-only" assumption. (V48 shipped without this change.)
- **Agent frontmatter hooks:** Subagent-scoped hooks could simplify global PreToolUse branching. Known bugs (issue #18392) — track for future.
- **SubagentStop:** Would replace Stop hook's mtime heuristic. Known reliability issues (#27755) — track for future.

Filed: 2026-05-21.
