# 0086 — Scaffold quality fixes

## Goal

Fix the minor issues in `/setup`'s scaffold output found during E2E testing: unreplaced placeholders, dropped UX principles, missing batch Status line, and stale marketplace description.

## Inputs

- E2E research: `research/e2e-greenfield-post-redesign.md` — Finding 2, scaffold issues.
- `plugin/skills/setup/` — setup skill body and scaffold script.
- `plugin/templates/` — template files with `[Project Name]` placeholders.
- `marketplace.json` — plugin description.

## Outputs

- Setup skill/scaffold script replaces `[Project Name]` placeholders with the actual project name in CLAUDE.md, MANIFEST.md, build-log/INDEX.md headers.
- Setup skill captures all agreed-upon UX principles, not just the first one.
- Seeded batch files include `Status: queued` line (0069 feature).
- `marketplace.json` description updated to remove "subagents" reference (removed in 0079).

## Success criteria

1. After `/setup` in a fresh folder, no `[Project Name]` placeholders remain in any scaffolded file.
2. All UX principles the user agrees to appear in UX.md.
3. Seeded batch file has a `Status: queued` line.
4. `marketplace.json` description accurately reflects current architecture.

## Open questions for this session

None — these are straightforward fixes.

## Risks / dependencies

- The UX-principles issue may be in the setup skill's prompt rather than the scaffold script — need to check which component handles that conversation.
