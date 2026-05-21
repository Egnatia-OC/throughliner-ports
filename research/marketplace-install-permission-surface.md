# Marketplace install vs --plugin-dir: permission-prompt surface

**Researched:** 2026-05-22, V44 session.
**Question:** Does marketplace installation change the per-tool permission-prompt surface compared to `--plugin-dir`?
**Answer:** No.

## Findings

### 1. Hooks fire independently of permission modes

From the official Claude Code hooks guide (code.claude.com/docs/en/hooks-guide):

> PreToolUse hooks fire before any permission-mode check. A hook that returns `permissionDecision: "deny"` blocks the tool even in `bypassPermissions` mode or with `--dangerously-skip-permissions`.

The plugin's PreToolUse denies are a separate enforcement layer from Claude Code's own permission system. This was already confirmed in session v43 research and coded into the V43 mode-aware deny messages. The docs confirm it authoritatively.

### 2. Plugin trust confirmation does not grant blanket tool permissions

When a marketplace plugin is installed, the user sees a summary of what components it contains, including a warning indicator for hooks and MCP servers that execute automatically. Users are directed to review hook scripts before enabling.

This trust confirmation is about **loading the plugin** — it does not change Claude Code's per-tool permission mode. The agent still prompts for Bash, Edit, Write etc. according to whatever permission mode the session is in (Ask, Accept edits, Auto, Bypass).

### 3. `--plugin-dir` vs marketplace install: functionally identical at runtime

The only behavioral differences between `--plugin-dir` and marketplace install are distribution and versioning:

- Marketplace plugins persist across sessions; `--plugin-dir` is session-scoped.
- When both are present with the same name, `--plugin-dir` takes precedence for that session (exception: managed-settings force-enabled/disabled plugins override `--plugin-dir`).
- At runtime, hooks fire the same way, skills load the same way, and the agent's tool calls go through the same permission flow.

### 4. Plugin-shipped agents cannot carry permissionMode

From the plugins reference (code.claude.com/docs/en/plugins-reference):

> For security reasons, `hooks`, `mcpServers`, and `permissionMode` are not supported for plugin-shipped agents.

This means a plugin cannot escalate its own agents' permissions. The plugin's subagents (planning, before-build, batch-executor, after-build, adopt) run under whatever permission mode the user's session is in — they cannot override it.

### 5. Hook deny overrides all permission modes

From the hooks guide:

> A blocking hook also takes precedence over allow rules. A hook that exits with code 2 stops the tool call before permission rules are evaluated, so the block applies even when an allow rule would otherwise let the call proceed.

And:

> Returning `"allow"` skips the interactive prompt but does not override permission rules. If a deny rule matches the tool call, the call is blocked even when your hook returns `"allow"`.

The permission precedence is: **deny rules > ask rules > hook allow > permission-mode allow**. The plugin's hook denies are structurally unbypassable.

## Implications for V44

- The `/setup` narration improvements are still needed. A new user in Ask mode (the default) will get prompted for every Bash call and file write the `/setup` subagent makes.
- The "permission-prompt surface comparison" output in V44's scope file is resolved — no difference exists between marketplace and `--plugin-dir` at the permission-prompt level.
- The two-layer permission model preamble added in V43 (SessionStart) and the mode-aware deny suffixes are correctly designed — the docs confirm the architecture they describe.

## Sources

- code.claude.com/docs/en/hooks-guide — hooks lifecycle, PreToolUse firing order, permission interaction
- code.claude.com/docs/en/permissions — permission modes, rule precedence, hook interaction
- code.claude.com/docs/en/plugins-reference — plugin component specs, agent restrictions, hook configuration
- code.claude.com/docs/en/plugins — plugin creation, --plugin-dir vs marketplace, trust model
