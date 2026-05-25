# 0091 — Dev-side terminology and BACKLOG alignment

## Goal

Align dev-side terminology and structures with plugin-side conventions. Three changes in one batch: (1) rename "session" → "batch" where it means "unit of work" across dev-side docs, renaming `planning/sessions/` to `planning/batches/`; (2) rename PLAN.md to BACKLOG.md, aligning with plugin-side naming; (3) merge OPEN-QUESTIONS.md entries into the new BACKLOG structure, matching how plugin-side BACKLOG carries open questions inline.

## Inputs

- `BUILD-METHOD.md` — primary target for terminology updates.
- `CLAUDE.md` (this project's) — references to sessions/, scope files, PLAN.md.
- `planning/PLAN.md` — becomes the new BACKLOG.
- `planning/OPEN-QUESTIONS.md` — content to merge.
- `plugin/docs/VOCABULARY.md` — plugin-side terms to align with.
- All existing files in `planning/sessions/` — relocate to `planning/batches/`.

## Outputs

- `planning/batches/` — renamed from `planning/sessions/`, all existing files moved.
- `planning/BACKLOG.md` — renamed from PLAN.md, with OPEN-QUESTIONS content merged in.
- `planning/OPEN-QUESTIONS.md` — deleted (content merged into BACKLOG).
- `BUILD-METHOD.md` — terminology updated throughout ("batch" for unit of work, "session" only for Claude Code conversation).
- `CLAUDE.md` — all path and terminology references updated.
- Existing batch files — internal cross-references updated if they name `planning/sessions/`.

## Success criteria

- No remaining references to `planning/sessions/` in dev-side docs.
- "Session" only used to mean "Claude Code conversation," never "unit of work."
- OPEN-QUESTIONS content findable in the new BACKLOG.
- Existing batch files accessible at new paths; git history intact via rename tracking.

## Open questions for this session

- Should BACKLOG be flat (BACKLOG.md) or folder (BACKLOG/INDEX.md + per-file)? Plugin-side went folder in 0050. Dev-side volume is lower — flat file may suffice.
- The PLAN.md table format (| # | Session | Output |) works well as an index. Keep the table, or adopt plugin-side BACKLOG entry format?
- "Scope file" → what? "Batch file" collides with Windows `.bat` in casual speech. "Batch spec"? Just "batch"?

## Risks / dependencies

- Blast radius across dev docs is wide but shallow — find-and-replace, not logic changes.
- Existing files (0085–0090 plus cancelled ones) all move; git tracks renames cleanly.
- No plugin-side changes. No footer bump. Dev-internal only.
