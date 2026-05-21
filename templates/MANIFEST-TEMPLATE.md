# MANIFEST.md — [Project Name]

> **FROZEN at method version V39, 2026-05-21 (shelved in session v40).** The live template is at `plugin/templates/MANIFEST-TEMPLATE.md` — that's what `/adopt` scaffolds. The two-write rule that kept this copy aligned has been shelved (see `BUILD-METHOD.md` → *Two-write rule for canonical docs*). Restoring two-write maintenance is one `planning/OPEN-QUESTIONS.md` promotion away if a real audience for the no-plugin template set emerges.

A flat, alphabetical glossary of named elements in the codebase that the user might want context on. One line per entry. Maintained by Claude during builds. Not intended to be read cover-to-cover — use it as a reference when you encounter a name you want context on, and as the basis for drift checks against `UX.md`.

If this list ever grows long enough that scanning it becomes hard, switch to alphabetical sections by area.

<!--
Entry format (one per line, alphabetical by Name):
- **[Name]** (`path/to/file.ext`) — [one-line plain-English description of what this is and what it does]

The `(path)` field is optional but strongly recommended — without it, the
read-before-edit discipline has nothing to anchor on. Multi-file entries:
comma-separate paths inside the parens, e.g. `(`a.kt`, `b.kt`)`, OR use a
directory-level path with a trailing slash, e.g. `(`app/src/settings/`)`.
One MANIFEST entry per discrete element — don't bundle unrelated elements
into one row to share a path. Entries that don't correspond to a file (a
cross-component flow, a named UX state) can omit the path.

Full spec: `DOC-STRUCTURE.md` → MANIFEST.md structure.
-->

---
*No-code method — Version 39.*
