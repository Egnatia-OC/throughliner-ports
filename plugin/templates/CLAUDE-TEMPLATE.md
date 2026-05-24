# CLAUDE.md — [Project Name]

Claude Code auto-loads this file on session start. The plugin's canonical docs live inside the no-code-method plugin (`plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/universal-behaviour.md`). This file owns the path block below and any project-specific behavioural notes after it.

## Where the docs live

Paths for each project doc, relative to the project root. Bare filenames elsewhere resolve against this list. Edit to match your project layout.

```json
{
  "UX.md": "UX.md",
  "BACKLOG.md": "BACKLOG/INDEX.md",
  "BUILD-LOG.md": "build-log/INDEX.md",
  "MANIFEST.md": "MANIFEST.md",
  "TEST-LOG.md": "TEST-LOG.md"
}
```

Fenced JSON so plugin hooks can parse it deterministically. Keys are logical names; values are relative paths. Additional source-of-truth docs: add `"<DOC>.md": "<path>"` entries. If a doc moves, update its entry.

## Plugin management

When the user asks how to install, disable, enable, or uninstall the plugin, read the Reference manual's *Managing the plugin* section first — don't guess. Key fact: `/plugin` is CLI-only and doesn't work in the desktop app.

## Project-specific notes

[Behavioural notes, terminology, or rules specific to this project. Most projects can leave this empty.]


---
*No-code method — Version 59.*
