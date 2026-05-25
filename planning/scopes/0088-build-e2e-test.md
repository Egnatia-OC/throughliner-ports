# 0088 — Build E2E test

## Goal

Test the build phase of the procedure-doc architecture. Picks up where 0084 left off — `/setup` and planning are validated, now test `/before-build` through `/build` through after-build in the Polite Fart Announcer burner app.

## Inputs

- E2E research: `research/e2e-greenfield-post-redesign.md` — "What wasn't tested" section.
- Burner app at `C:\Users\Alex\Desktop\Polite Fart Announcer` (already scaffolded from 0084 testing).
- Fixes from 0085 and/or 0086 if shipped by then (if not, test against current state and note gaps).

## Outputs

- Updated research file: `research/e2e-greenfield-post-redesign.md` — build-phase findings appended.
- New scope files or BACKLOG.md open-question entries for any build-phase issues.
- Token cost baseline for procedure-doc architecture (if full cycle completes).

## Success criteria

1. `/before-build` activates the batch correctly (Status: active, Files: and Tests: populated).
2. `/build` creates `index.html` successfully — file exists and the app works in a browser.
3. After-build fires: MANIFEST updated, build-log entry written, TEST-LOG rows written.
4. Phase-aware permissions work: source-of-truth docs locked during build, batch files editable.
5. Observations documented in research file.

## Open questions for this session

1. Can the existing burner session be reused (with `/reload-plugins` if fixes landed), or does it need a fresh session? Depends on whether 0085/0086 changes require a clean session-start.
2. If a fix session (0085 or 0086) shipped between 0084 and this session, re-test the fixed behaviour before proceeding to build.

## Risks / dependencies

- ~~Soft dependency on 0085: resolved — 0085 shipped in v84, before-build recap now says "Run `/build` to start building."~~
- The burner app may have stale state from 0084 testing (Status: active on the batch from the before-build that ran). May need to reset batch status or start fresh.
