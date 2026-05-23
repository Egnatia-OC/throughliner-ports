# 0061 — Rename "Crash course" to "Reference manual"

## Goal

Rename the current `Crash course.md` to `Reference manual.md` across the codebase, freeing the "Crash Course" name for a new HTML guide aimed at testers and early adopters (see 0062). The file keeps its content unchanged — this is a name change only.

## Inputs

- `Crash course.md` (the file being renamed)
- `BUILD-METHOD.md` (doc-code parity rules reference "Crash course" — 6 occurrences)
- `CLAUDE.md` (this project's instructions — 2 occurrences)
- `README.md` (repo root — 2 occurrences)
- `plugin/README.md` (1 occurrence)
- `planning/PLAN.md` (9 occurrences across session descriptions)
- `planning/INVENTORY.md` (1 occurrence)
- `BUILD-LOG.md` (65 occurrences — historical entries; see open question below)

## Outputs

- `Reference manual.md` at repo root (renamed from `Crash course.md`)
- Updated references in all live files listed above
- No changes to `Archive/` files (frozen historical snapshots)
- No changes to `planning/OPUS-FEASIBILITY-PROMPT.md` (historical context)

## Success criteria

- The file is renamed and git tracks it as a rename (not delete + create)
- Every live reference to "Crash course" now says "Reference manual" (except where the term refers to the future HTML guide)
- `BUILD-METHOD.md` doc-code parity rules reference the new name
- No broken cross-references
- Archive files untouched

## Open questions for this session

1. **BUILD-LOG.md historical entries.** 65 occurrences. These are historical records ("updated Crash course" in past session entries). Options: (a) rename all to "Reference manual" for consistency, accepting that the historical record uses a name that didn't exist at the time; (b) leave them as-is, accepting mixed terminology in the log; (c) rename only the most recent entries (post-rename) and leave older ones. Recommend (a) — the log is a working reference, not a legal record, and mixed terminology makes grep harder.

## Risks / dependencies

- **High churn, low risk.** The change is mechanical (find-and-replace) but touches many files. Risk of a missed reference is low because grep catches them; risk of breaking something is near zero because these are all markdown docs with no code dependencies on the name.
- **No dependency on 0062.** This session frees the name; 0062 uses it. They don't need to ship in the same session.
