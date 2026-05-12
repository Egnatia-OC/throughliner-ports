# CLAUDE.md — [Project Name]

This is the project's per-project glue file. Claude Code auto-loads it on session start. The structural workflow lives in `NO-CODE-METHOD.md` (verbatim across every project using the no-code method); the structural specs for the project's docs live in `DOC-STRUCTURE.md` (also verbatim). Read those files for the workflow and the doc structure rules. The two project-specific things this file owns are the path block below and any project-specific behavioural notes after it.

## Where the docs live

This section declares the path for each of the project's docs, relative to the project root. Bare filenames elsewhere (`UX.md`, `BACKLOG.md`, `MANIFEST.md`, etc.) resolve against this list. Edit the paths in the JSON block below to match where the docs actually live in this project.

```json
{
  "UX.md": "UX.md",
  "BACKLOG.md": "BACKLOG.md",
  "MANIFEST.md": "MANIFEST.md"
}
```

The block is fenced JSON (not freeform markdown) so plugin hooks can parse it deterministically. Keys are the logical names referenced elsewhere in the method docs; values are paths relative to the project root.

If the project has additional source-of-truth docs (see `DOC-STRUCTURE.md` → *Additional source-of-truth docs*), add a `"<DOC>.md": "<path>"` entry to the block above for each one. If a doc is moved later, update its entry — Claude Code will catch unresolved paths at session start (see `NO-CODE-METHOD.md` → *At session start*) and propose the correction, but the declaration here is the source of truth.

## Project-specific notes

[Any behavioural notes, terminology, or rules specific to this project that don't belong in NO-CODE-METHOD.md or the source-of-truth docs. Most projects can leave this section empty. Delete this instruction when filled in, or leave the section empty.]


---
*No-code method — Version 18.*
