# CLAUDE.md — [Project Name]

This is the project's per-project glue file. Claude Code auto-loads it on session start. The plugin's internal canonical docs live inside the no-code-method plugin (`plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/universal-behaviour.md`) — one copy per plugin install. A frozen prose snapshot of the project-agnostic method spec (`NO-CODE-METHOD.md`) sits at the no-code-method repo root, snapshotted at method version V39 (two-write rule shelved in session v40); humans can browse it at https://github.com/FlintCraftTech/sovereign-implementer/blob/main/NO-CODE-METHOD.md. The two project-specific things this file owns are the path block below and any project-specific behavioural notes after it.

## Where the docs live

This section declares the path for each of the project's docs, relative to the project root. Bare filenames elsewhere (`UX.md`, `BACKLOG.md`, `MANIFEST.md`, etc.) resolve against this list. Edit the paths in the JSON block below to match where the docs actually live in this project.

```json
{
  "UX.md": "UX.md",
  "BACKLOG.md": "BACKLOG/INDEX.md",
  "BUILD-LOG.md": "build-log/INDEX.md",
  "MANIFEST.md": "MANIFEST.md",
  "TEST-LOG.md": "TEST-LOG.md"
}
```

The block is fenced JSON (not freeform markdown) so plugin hooks can parse it deterministically. Keys are the logical names referenced elsewhere in the method docs; values are paths relative to the project root.

If the project has additional source-of-truth docs (see `DOC-STRUCTURE.md` → *Additional source-of-truth docs*), add a `"<DOC>.md": "<path>"` entry to the block above for each one. If a doc is moved later, update its entry — Claude Code will catch unresolved paths at session start and propose the correction, but the declaration here is the source of truth.

## Plugin management

When the user asks how to install, disable, enable, or uninstall the no-code method plugin, do not guess — read the Crash course's *Managing the plugin* section first. The Crash course is a humans-only reference doc browsable at https://github.com/FlintCraftTech/sovereign-implementer/blob/main/Crash%20course.md. Key fact: the `/plugin` command is CLI-only and does not work in the Claude Code desktop app.

## Project-specific notes

[Any behavioural notes, terminology, or rules specific to this project that don't belong in the method's general spec or the source-of-truth docs. Most projects can leave this section empty. Delete this instruction when filled in, or leave the section empty.]


---
*No-code method — Version 58.*
