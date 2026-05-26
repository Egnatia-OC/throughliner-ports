# v76 — 2026-05-25 — Dev-side log folder migration

**What shipped.** Scope 0075. `BUILD-LOG.md` (59 entries) and `TEST-LOG.md` (15 session sections) split from single files into folder structures: `build-log/INDEX.md` + 59 per-entry files, `test-log/INDEX.md` + 15 per-session files. Matches the folder convention the plugin ships to consumer projects (V50). Original files deleted. Reference updates across BUILD-METHOD.md (9 path references + entry-shape instructions rewritten for per-file creation), CLAUDE.md (3 references), OPEN-QUESTIONS.md (1 reference). Dev-internal only — no footer bumps, no plugin changes.

**Decisions.** Scope file estimated 31 entries; actual count was 59 (scope was written before the file grew further). Script-based splitting for reliability — 74 files total would be error-prone by hand. Headings converted from `## ` to `# ` in per-entry files (standalone files get H1). Frozen docs (NO-CODE-METHOD.md, DOC-STRUCTURE.md, VOCABULARY.md, repo-root templates/) left untouched — they describe consumer-side conventions and are frozen at V39. Historical references to old filenames inside split files preserved as-is (accurate for when they were written).

**Pivots.** None.

**Carried forward.** Nothing.
