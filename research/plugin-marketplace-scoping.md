# Claude Code Plugin Marketplace: Scoping Reference

## 1. Marketplace manifest: filename and location

The marketplace catalog file is `.claude-plugin/marketplace.json`, and it goes at the **repository root** — not inside the plugin directory. The correct path is:

```
<repo-root>/.claude-plugin/marketplace.json
```

Your assumption about the filename is correct. There is no indication in the current docs that this format has changed.

---

## 2. Required fields and minimal valid example

Required fields in `marketplace.json`:

| Field | Type | Required |
|---|---|---|
| `name` | string (kebab-case, no spaces) | Yes |
| `owner` | object with `name` string | Yes |
| `plugins` | array | Yes |

Each plugin entry requires `name` and `source`.

Minimal valid example for a single-plugin marketplace:

```json
{
  "name": "my-plugins",
  "owner": {
    "name": "Your Name"
  },
  "plugins": [
    {
      "name": "quality-review-plugin",
      "source": "./plugins/quality-review-plugin",
      "description": "Adds a /quality-review skill for quick code reviews"
    }
  ]
}
```

---

## 3. How the marketplace manifest references the plugin

By `source` — which supports four types:

| Source type | Format | Notes |
|---|---|---|
| Relative path | `"./my-plugin"` (string) | Same repo; must start with `./` |
| GitHub repo | `{"source": "github", "repo": "owner/repo"}` | Supports `ref`, `sha` |
| Git URL | `{"source": "url", "url": "https://..."}` | Any git host |
| Git subdirectory | `{"source": "git-subdir", "url": "...", "path": "..."}` | Monorepo; sparse clone |
| npm package | `{"source": "npm", "package": "@org/pkg"}` | Supports `version`, `registry` |

For a plugin in the same repo, use a relative path:

```json
"source": "./plugins/sovereign-implementer"
```

**Important caveat:** relative paths only work when users add your marketplace via Git. If users add it via a direct URL to the `marketplace.json` file, relative paths will not resolve correctly. For URL-based distribution, use GitHub, npm, or git URL sources instead.

---

## 4. Relationship between `plugin.json` and `marketplace.json`

They are distinct with overlapping optional fields — not duplicates.

- `plugin.json` lives at `.claude-plugin/plugin.json` **inside the plugin directory** and defines the plugin's identity and components from the plugin's own perspective.
- `marketplace.json` lives at `.claude-plugin/marketplace.json` in the **marketplace repo root** and is a catalog pointing to one or more plugins.

Plugin entries in `marketplace.json` can include any field from the plugin manifest schema (`description`, `version`, `author`, `commands`, `hooks`, etc.), plus marketplace-specific fields: `source`, `category`, `tags`, and `strict`.

The `strict` field (default: `true`) controls authority:

| Value | Behaviour |
|---|---|
| `true` (default) | `plugin.json` is authoritative; marketplace entry can supplement — both are merged |
| `false` | Marketplace entry is the entire definition; if `plugin.json` also declares components, the plugin fails to load |

**Version conflict:** if both files declare `version`, `plugin.json` silently wins. For relative-path plugins, set the version in the marketplace entry only. For all other plugin sources, set it in the plugin manifest.

---

## 5. Constraints to know about

**Claude Code version:** The `/plugin` command requires a recent release. If you don't see it, update Claude Code. The `--plugin-dir` flag accepts `.zip` archives from v2.1.128+; no minimum version is stated for marketplace publishing itself.

**License:** Not required. `license` is an optional SPDX identifier field — omit it freely.

**README:** Not required by schema. Recommended as a best practice; not enforced.

**Public vs private repo:** Private repos work. Manual install and updates use your existing git credential helpers. Background auto-updates require an auth token in your environment:

| Provider | Environment variable |
|---|---|
| GitHub | `GITHUB_TOKEN` or `GH_TOKEN` |
| GitLab | `GITLAB_TOKEN` or `GL_TOKEN` |
| Bitbucket | `BITBUCKET_TOKEN` |

**Reserved marketplace names:** The following are blocked for third-party use: `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `knowledge-work-plugins`, `life-sciences`. Names that impersonate official marketplaces are also blocked.

**Validation:** Run `claude plugin validate .` locally before distributing.

---

## 6. Simpler interim path: skip the marketplace entirely

Yes — and it's cleaner for personal use.

**Option A — `--plugin-dir` flag**

Load your plugin directly without installation:

```bash
claude --plugin-dir ./sovereign-implementer
```

All component types (hooks, agents, commands/skills) work from this flag. Alias it in your shell for convenience. Does not persist across sessions without the flag.

**Option B — local marketplace add (recommended)**

Add your marketplace once and install once:

```bash
/plugin marketplace add ./my-marketplace
/plugin install no-code-method@my-marketplace
```

No hosting required. The plugin persists across sessions. Run `/reload-plugins` to pick up changes after edits.

The `~/.claude/plugins/cache` directory exists but is a managed cache — not a documented drop-in folder. Don't write to it manually.

---

*Source: [code.claude.com/docs](https://code.claude.com/docs/llms.txt) — plugins, plugin-marketplaces, discover-plugins pages. Retrieved May 2026.*
