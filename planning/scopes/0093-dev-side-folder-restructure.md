# 0093 — Dev-side folder restructure

## Goal

Reshape the dev-side folder layout to reflect the naming and structural changes from 0091 and 0092. Cleanup pass — the earlier batches created the new structures; this one retires leftover organizational debt and documents the final layout.

## Inputs

- State of repo after 0091 and 0092 ship.
- `CLAUDE.md` — current folder/path references to update.
- Plugin-side folder conventions for comparison.

## Outputs

- Folder layout finalized and documented in CLAUDE.md's orientation sections.
- Stale path references across dev docs cleaned up.
- Any remaining `planning/` organizational debt resolved.

## Success criteria

- Every dev-side doc has a logical home that parallels plugin-side conventions where applicable.
- No stale path references in CLAUDE.md, session-protocol.md, session-reference.md, or BACKLOG.
- A new Claude session can orient from CLAUDE.md without encountering dead paths.

## Open questions for this session

- Does `planning/` as a parent folder still earn its keep, or do its remaining contents (BACKLOG, scopes/, drafts/) promote to repo root? Plugin-side puts BACKLOG inside `_method/` (not at project root — only CLAUDE.md sits at root).
- Where do `drafts/` live after the restructure? Plugin-side has no direct equivalent (closest: `research/`).
- Do `build-log/` and `test-log/` stay at repo root? Plugin-side keeps them at project root — already aligned.

## Risks / dependencies

- Hard dependency on 0091 and 0092 both shipping first.
- Scope may shrink naturally if 0091 and 0092 resolve most layout questions during their own sessions.
- Dev-internal only. No footer bump.
