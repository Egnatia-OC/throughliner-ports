# 0075 — Dev-side log folder migration

## Goal

Migrate this project's `BUILD-LOG.md` (31 entries, 663 lines) and `TEST-LOG.md` (15 sections, 272 lines) from single files to folder structures. Pure dev-side housekeeping — no plugin code changes. Matches the folder convention the plugin already ships to consumer projects for build-log (V50).

## Inputs

- `sovereign-implementer/BUILD-LOG.md` — the file being split.
- `sovereign-implementer/TEST-LOG.md` — the file being split.
- `sovereign-implementer/plugin/templates/build-log/INDEX-TEMPLATE.md` — reference for build-log INDEX shape (already shipped to consumers).
- `sovereign-implementer/BUILD-METHOD.md` — references both files; needs path updates.
- `No code method/CLAUDE.md` — references both files; needs path updates.

## Outputs

**BUILD-LOG split:**
- `sovereign-implementer/build-log/INDEX.md` — header + newest-first file list. One line per entry: `- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — One-line summary`.
- `sovereign-implementer/build-log/vNN-slug.md` — 31 per-entry files. Each contains the content of one `## vNN — date — title` section from the original. Slug derived from the title (e.g. `v71-e2e-round-2.md`, `v17-plugin-migration-architecture.md`).
- Delete `sovereign-implementer/BUILD-LOG.md`.

**TEST-LOG split:**
- `sovereign-implementer/test-log/INDEX.md` — header + newest-first file list. One line per session: `- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — Session title`.
- `sovereign-implementer/test-log/vNN-slug.md` — 15 per-session files. Each contains the session heading + its table (header row + data rows). Slug from session title (e.g. `v18-v22-backfilled.md`, `v25-build-orchestration.md`).
- Delete `sovereign-implementer/TEST-LOG.md`.

**Reference updates:**
- `sovereign-implementer/BUILD-METHOD.md` — update 9 references (paths and entry-shape instructions to say "create a new file in `build-log/`" / "create a new file in `test-log/`").
- `No code method/CLAUDE.md` — update 3 references.

## Success criteria

1. `build-log/INDEX.md` lists all 31 entries; each per-entry file contains exactly its original section content.
2. `test-log/INDEX.md` lists all 15 sessions; each per-session file contains its heading + complete table.
3. Original `BUILD-LOG.md` and `TEST-LOG.md` deleted.
4. `BUILD-METHOD.md` and `CLAUDE.md` reference the new paths — no stale `BUILD-LOG.md` or `TEST-LOG.md` references remain in either file.
5. `git grep 'BUILD-LOG\.md'` and `git grep 'TEST-LOG\.md'` within `sovereign-implementer/` return zero hits outside `plugin/` (plugin-side references are 0073's scope).

## Open questions for this session

None — the pattern is established and the work is mechanical.

## Risks / dependencies

- **Low risk.** File reorganization only. No code, no plugin changes, no consumer-facing impact.
- **No dependencies.** Can execute independently of any other scope.
- **Remote-safe.** Mechanical splitting + reference updates. No judgement calls needed.
