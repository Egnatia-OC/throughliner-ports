# v87 — 2026-05-26 — Dev-side terminology and BACKLOG alignment

**What shipped.** Renamed `planning/PLAN.md` → `planning/BACKLOG.md`, `planning/sessions/` → `planning/scopes/`, and merged `planning/OPEN-QUESTIONS.md` content into BACKLOG.md as a new *Open questions* section. Updated all references across BUILD-METHOD.md, CLAUDE.md, and active scope files. Table format kept with column renamed ("Session" → "Batch"). "Scope file" retained as the term for `planning/scopes/NNNN-kebab-title.md` files — folder became `scopes/` not `batches/` after design discussion concluded "scope" carries stronger technical signal for Claude compliance.

**Decisions taken and why.**
- Flat BACKLOG.md (not folder) — dev-side volume is low enough for one file; simpler than plugin-side folder convention.
- Kept table format — compact and scannable; dev-side batches aren't consumer build batches with full scope-context sections.
- "Scope file" kept as term — Alex observed Claude naturally gravitates to "scope" language and is more compliant with it. Basis in established software engineering terminology (scope definition, scope management).
- Folder named `planning/scopes/` not `planning/batches/` — aligns with the retained term.

**Pivots and surprises.** Design discussion surfaced a deeper question: should scope files split planning-content from build-content, and should "build cycle" retire as a term? Parked as open question — the current terminology doesn't foreclose either direction.

**Carried forward.** New open question added to BACKLOG.md: "Scope file split: separate planning content from build content." Parks until 0091 ships and terminology settles.
