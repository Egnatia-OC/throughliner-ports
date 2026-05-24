# Marketplace install vs --plugin-dir: permission-prompt surface

**Researched:** 2026-05-22, V44 session.
**Question:** Does marketplace installation change the permission-prompt surface compared to `--plugin-dir`?
**Answer:** No.

## Findings

1. **Hooks fire independently of permission modes.** PreToolUse denies block even in `bypassPermissions` mode. Confirmed in official docs and V43 session.

2. **Plugin trust confirmation does not grant blanket tool permissions.** Trust is about loading the plugin; the agent still prompts per Claude Code's permission mode.

3. **`--plugin-dir` vs marketplace: functionally identical at runtime.** Only differences are persistence (marketplace persists; `--plugin-dir` is session-scoped) and precedence (`--plugin-dir` wins when both present).

4. **Plugin-shipped agents cannot carry `permissionMode`.** Claude Code blocks it for security. Subagents run under the session's mode.

5. **Permission precedence:** deny rules > ask rules > hook allow > permission-mode allow. Plugin hook denies are structurally unbypassable.

## Sources

- code.claude.com/docs/en/hooks-guide, permissions, plugins-reference, plugins
