# Claude Code Plugin Marketplace: Scoping Reference

## 1. Marketplace manifest location

`.claude-plugin/marketplace.json` at the **repository root** (not inside the plugin directory).

---

## 2. Required fields and minimal example

| Field | Type | Required |
|---|---|---|
| `name` | string (kebab-case) | Yes |
| `owner` | object with `name` | Yes |
| `plugins` | array | Yes |

Each plugin entry needs `name` and `source`.

```json
{
  "name": "my-plugins",
  "owner": { "name": "Your Name" },
  "plugins": [
    {
      "name": "quality-review-plugin",
      "source": "./plugins/quality-review-plugin",
      "description": "Adds a /quality-review skill"
    }
  ]
}
```

---

## 3. Source types

| Type | Format | Notes |
|---|---|---|
| Relative path | `"./my-plugin"` | Same repo; must start with `./` |
| GitHub repo | `{"source": "github", "repo": "owner/repo"}` | Supports `ref`, `sha` |
| Git URL | `{"source": "url", "url": "https://..."}` | Any git host |
| Git subdirectory | `{"source": "git-subdir", "url": "...", "path": "..."}` | Monorepo |
| npm package | `{"source": "npm", "package": "@org/pkg"}` | Supports `version`, `registry` |

**Caveat:** relative paths only work when users add via Git clone, not via direct URL.

---

## 4. plugin.json vs marketplace.json

Distinct files with overlapping optional fields. `plugin.json` is inside the plugin directory (plugin identity). `marketplace.json` is at the repo root (catalog pointing to plugins).

`strict` field (default `true`): when true, `plugin.json` is authoritative and marketplace supplements. When false, marketplace is the entire definition. Version conflicts: `plugin.json` silently wins.

---

## 5. Constraints

- `/plugin` command requires a recent Claude Code release.
- License and README are optional.
- Private repos work; auto-updates need auth tokens (`GITHUB_TOKEN`, `GITLAB_TOKEN`, `BITBUCKET_TOKEN`).
- Reserved marketplace names: `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `knowledge-work-plugins`, `life-sciences`.
- Validate with `claude plugin validate .` before distributing.

---

## 6. Simpler paths

**Option A — `--plugin-dir`:** Load directly, session-scoped. `claude --plugin-dir ./sovereign-implementer`

**Option B — local marketplace (recommended):** `/plugin marketplace add ./my-marketplace` then `/plugin install no-code-method@my-marketplace`. Persists across sessions. `/reload-plugins` after edits.

Don't write to `~/.claude/plugins/cache` manually.

---

*Source: code.claude.com/docs — plugins, plugin-marketplaces, discover-plugins. Retrieved May 2026.*
