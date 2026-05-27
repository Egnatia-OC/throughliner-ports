# CLAUDE.md — [Project Name]

Claude Code auto-loads this file on session start. The plugin's canonical docs live inside the no-code-method plugin (`plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/universal-behaviour.md`). This file owns the product overview, the path block, and any project-specific behavioural notes after them.

## Product overview

<!-- Populated during /setup. Update milestones during planning as the project evolves. -->

**What it is.** 
**Who it's for.** 
**What friction it solves.** 
**Milestones.** 

## Where the docs live

Paths for each project doc, relative to the project root. Bare filenames elsewhere resolve against this list. Edit to match your project layout.

```json
{
  "UX.md": "_method/UX.md",
  "BACKLOG.md": "_method/proxies/backlog.md",
  "BUILD-LOG.md": "_method/proxies/build-log.md",
  "MANIFEST.md": "_method/MANIFEST.md",
  "TEST-LOG.md": "_method/proxies/test-log.md"
}
```

Fenced JSON so plugin hooks can parse it deterministically. Keys are logical names; values are relative paths. Additional source-of-truth docs: add `"<DOC>.md": "<path>"` entries. If a doc moves, update its entry.

## Plugin management

When the user asks how to install, disable, enable, or uninstall the plugin, read the Reference manual's *Managing the plugin* section first — don't guess. Key fact: `/plugin` is CLI-only and doesn't work in the desktop app.

## Project-specific notes

[Behavioural notes, terminology, or rules specific to this project. Most projects can leave this empty.]

## After-build steps

<!-- Optional. Steps here run during /sovclose, after standard steps and before closing prompts. Use for project-specific close actions — e.g. regenerating an API doc, updating a changelog, syncing a config file. Each step should be one sentence the agent can act on. Delete this section if unused. -->


---
*No-code method — Version 79.*
