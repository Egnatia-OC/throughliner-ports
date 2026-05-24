# Desktop app plugin upload — what format does it expect?

*2026-05-24*

## Question

The desktop app's upload flow (Customise → plugin icon → + → Create plugin → Upload plugin) doesn't accept a raw folder. What does it actually need?

## Answer

It needs a **`.zip` file** — the plugin directory zipped up, under 50 MB. The `.claude-plugin/plugin.json` manifest must be at the root of the archive.

## Details

### Required structure inside the zip

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        ← required manifest
├── skills/                 ← optional
├── agents/                 ← optional
├── hooks/                  ← optional
├── .mcp.json               ← optional
└── ...
```

The manifest must contain at minimum:

```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Author Name"
  }
}
```

(`version` and `author` are optional but recommended.)

### `.plugin` vs `.zip` extension

Anthropic's docs describe a `.plugin` extension (which is just a renamed `.zip`), but the desktop app upload handler **only accepts `.zip`** — it rejects `.plugin` files with "Only .zip files are accepted." This is a known bug: [#40414](https://github.com/anthropics/claude-code/issues/40414).

Use `.zip`, not `.plugin`.

### How to package Sovereign Implementer

The plugin content lives in the `plugin/` subfolder of the repo. To create a zip the desktop app accepts:

```powershell
cd "C:\Users\Alex\Desktop\Taskflow Planning\No code method\sovereign-implementer"
Compress-Archive -Path plugin\* -DestinationPath sovereign-implementer-plugin.zip
```

This puts the contents of `plugin/` (which contains `.claude-plugin/plugin.json`, `skills/`, `hooks/`, etc.) at the zip root.

**Untested.** The zip approach has not been verified with SI's specific structure — the plugin was built for CLI install via marketplace, not zip upload. Potential issues:

- Hook scripts reference `${CLAUDE_PLUGIN_ROOT}` for paths — unclear whether the desktop app sets this the same way as CLI install.
- The plugin's `hooks.json` uses Python scripts that need Python on PATH — the zip doesn't bundle a runtime.
- Subagent definitions reference plugin-relative paths for docs — may or may not resolve correctly from a zip-uploaded install.

### CLI alternatives that still work

- `claude --plugin-dir ./plugin` — loads for one session, no install needed.
- `/plugin marketplace add <path>` then `/plugin install no-code-method@sovereign-implementer` — persistent install, but CLI-only command.

### Other known desktop app issues

- **Upload button hidden on Windows** unless at least one plugin is already installed: [#37169](https://github.com/anthropics/claude-code/issues/37169).
- **Third-party plugin updates** via the desktop app's Personal tab can fail: [#38185](https://github.com/anthropics/claude-code/issues/38185).

## Sources

- [Create plugins — Claude Code Docs](https://code.claude.com/docs/en/plugins)
- [#40414 — Desktop plugin upload rejects .plugin files](https://github.com/anthropics/claude-code/issues/40414)
- [#37169 — Upload plugin hidden on Windows](https://github.com/anthropics/claude-code/issues/37169)
- [#38185 — Cannot update third-party plugins](https://github.com/anthropics/claude-code/issues/38185)
- [#37093 — Documentation: Publishing plugins as npm packages](https://github.com/anthropics/claude-code/issues/37093)
