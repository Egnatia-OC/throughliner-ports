# V52 — BUILD-LOG restructuring (per-build files)

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22).**

## Goal

Replace monolithic `BUILD-LOG.md` with a `build-log/` folder containing one file per build plus a lightweight index. The current single-file BUILD-LOG grows with every build; Claude reads the entire file to write one entry or check history during planning. Per-build files mean the agent reads only the entries it needs. The index preserves scan-the-full-history capability in one place.

## Inputs

- OPEN-QUESTIONS entry: "BUILD-LOG restructuring — per-build files in a folder with index"
- `plugin/agents/after-build.md` — currently writes entries to BUILD-LOG.md; updated to write per-build files and append index lines
- `plugin/templates/BUILD-LOG-TEMPLATE.md` — replaced by folder template
- `plugin/docs/DOC-STRUCTURE.md` — BUILD-LOG.md structural spec
- `plugin/agents/setup.md` — `/setup` scaffolding gains `build-log/` folder
- `plugin/scripts/scaffold.py` — if scaffolding is scripted
- V50's file-split pattern — reference for per-file + index architecture

## Outputs

- `build-log/` folder replaces `BUILD-LOG.md` in consumer projects. `/setup` scaffolds the folder.
- One file per build — naming TBD (e.g. `BUILD-001.md`, `BUILD-002.md`, or batch-name-based)
- `build-log/INDEX.md` — one line per build with short summary and link. After-build subagent writes the build entry and appends the index line in the same pass.
- `plugin/templates/BUILD-LOG-TEMPLATE.md` replaced by `plugin/templates/build-log/INDEX-TEMPLATE.md` + `plugin/templates/build-log/ENTRY-TEMPLATE.md`
- `plugin/docs/DOC-STRUCTURE.md` updated for new structure
- `/setup` case-4 refresh migrates existing consumer-project BUILD-LOG.md to `build-log/` folder
- OPEN-QUESTIONS entry removed
- All plugin-side method-version footers bumped

## Success criteria

- After-build writes a per-build file and appends an index line — no monolithic BUILD-LOG.md
- `/setup` on a fresh project scaffolds `build-log/` folder with INDEX.md
- `/setup` case-4 refresh migrates existing BUILD-LOG.md to `build-log/` folder preserving all entries
- Planning subagent reads the index for history overview, individual files only when needed
- Smoke-testable in a desktop-app burner session with the plugin installed via local marketplace: run a build; verify per-build file created and index updated

## Open questions for this session

- **Entry file naming.** Sequential numbers (`BUILD-001.md`), batch-name-based (`add-login-page.md`), or date-based (`2026-05-22-add-login.md`)? Sequential is simplest; batch-name is most readable; date adds chronological scanning. Leaning: sequential — matches V50's ADR-style allocation if it ships first.
- **Migration of existing BUILD-LOG.md.** Split by entry boundaries (each `## Build N` heading becomes a file) or simpler heuristic? Entry boundaries are cleanest but require reliable heading detection.
- **Index format.** One-line-per-build table, or bullet list with links? Leaning: bullet list — lighter, easier to append.
- **Research file cross-references.** V51 ships `research/` folder. Build entries should link to relevant research files rather than embedding findings. Add this as a convention in DOC-STRUCTURE, or leave to emerge? Leaning: add one line of guidance.
- **Session-token rename cascade.** When a user edits a build's session token (in the per-build file heading or INDEX.md), the plugin must cascade the rename to all TEST-LOG rows referencing the old token — and announce the change plainly (not silently). Design the detection and cascade as part of this restructure, not as a bolt-on. Decided 2026-05-22 during idea discussion.

## Risks / dependencies

- **No hard dependencies** on V44–V50, but benefits from V50's file-split pattern being established. Placed after V50 for that reason.
- **Migration is the risk.** Splitting an existing BUILD-LOG.md into per-build files requires reliable entry-boundary detection. Test against Taskflow's BUILD-LOG before shipping.
- **After-build subagent change.** After-build already has significant changes in V48 (test split). By V52, the subagent's shape should be stable enough for this structural change.
