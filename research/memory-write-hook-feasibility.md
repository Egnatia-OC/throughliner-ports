# Memory-write hook feasibility research — 2026-05-24

## Purpose

Determine whether Claude Code's auto-memory writes can be intercepted by a PreToolUse hook, so the plugin could mechanically block or redirect memory writes to project artifacts instead.

## Context

Claude defaults to saving information as memories instead of writing it to the correct project artifact (scope files, BACKLOG.md, OPEN-QUESTIONS.md, etc.). The question was whether a PreToolUse gate on Write could catch memory writes and deny them with a redirect message — the same pattern used by the V56 project-boundary check and V39 read-before-edit gate.

## Findings

### Auto-memory does not use the standard Write tool

Memory writes use an internal mechanism, not the standard Write tool that PreToolUse hooks intercept. A PreToolUse hook matching Write calls with a path regex targeting the memory directory (`~/.claude/projects/<hash>/memory/`) is described in the community as a fragile workaround that "relies on undocumented internal tool naming that could break between releases."

Source: [GitHub issue #44820](https://github.com/anthropics/claude-code/issues/44820) — feature request for dedicated PreMemoryWrite/PostMemoryWrite hook events.

### Feature request for dedicated memory hooks was declined

Issue #44820 requested two new hook events:
- **PreMemoryWrite** — fire before a memory file is written, allowing inspection, modification, or blocking.
- **PostMemoryWrite** — fire after the write succeeds, for audit logging or external sync.

The issue was **closed as not planned** by the Anthropic team. No public reasoning was given.

### V56 project-boundary check is irrelevant

The plugin's V56 check blocks Write calls targeting paths outside the project root. Since memory files live at `~/.claude/projects/<hash>/memory/` (outside any project root), V56 would theoretically block them — but only if the writes went through the standard Write tool, which they don't.

## Conclusion

**No mechanical gate is possible.** Memory writes bypass the hook pipeline entirely, and the feature request for dedicated memory hooks was rejected. The only viable approach is prose rules in universal-behaviour.md (plugin-side) and CLAUDE.md (dev-side), which were added in this session.

## Related

- Plugin-side rule: `plugin/hooks/universal-behaviour.md` → Required behaviours → "Route information to artifacts, not memory."
- Dev-side rule: project CLAUDE.md → "Don't default to memory — route to the artifact."
