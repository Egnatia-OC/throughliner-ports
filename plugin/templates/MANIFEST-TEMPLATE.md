# MANIFEST.md — [Project Name]

A flat, alphabetical glossary of named elements in the codebase that the user might want context on. One line per entry. Maintained by Claude during builds. Not intended to be read cover-to-cover — use it as a reference when you encounter a name you want context on, and as the basis for drift checks against `UX.md`.

If this list ever grows long enough that scanning it becomes hard, switch to alphabetical sections by area.

<!--
Entry format (one per line, alphabetical by Name):
- **[Name]** (`path/to/file.ext`) — [one-line plain-English description of what this is and what it does]

The `(path)` field is optional but strongly recommended — the PreToolUse hook
reads it to drive the read-before-edit gate. Without a path, the entry is
silently skipped by that gate. Multi-file entries: comma-separate paths
inside the parens, e.g. `(`a.kt`, `b.kt`)`, OR use a directory-level path
with a trailing slash, e.g. `(`app/src/settings/`)`. One MANIFEST entry per
discrete element — don't bundle unrelated elements into one row to share a
path. Entries that don't correspond to a file (a cross-component flow, a
named UX state) can omit the path.

Full spec: `DOC-STRUCTURE.md` → MANIFEST.md structure.
-->

## Fold-ins pending

Proposed entries or updates that Claude has queued for this doc. Each block describes the proposed change, its origin, and whether it replaces an existing section or adds a new one. Fold these into the main body during your next planning session, then delete the block. Section starts empty for new projects.

For the canonical block format, see `DOC-STRUCTURE.md` → *Fold-ins pending sections*.

---
*No-code method — Version 50.*
