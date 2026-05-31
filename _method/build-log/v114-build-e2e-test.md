# v114 — 2026-05-28 — Build E2E test

**What shipped.** Batch 0088. Full build-lifecycle E2E of the procedure-doc architecture against the Polite Fart Announcer burner app. `/sovsetup` → `/sovplan` → `/sovrecap` → `/sovbuild` → `/sovclose` → `/sovgit` — all six skills exercised in sequence. Three `pre_tool_use.py` bugs found and filed as new batch 0116: (1) `active-build.md` creation blocked by `_METHOD_INFRA_DIRS` not covering root-level `_method/` files, (2) `test-log/` and `build-log/` writes blocked during close for the same reason, (3) phase detection falling through to "planning" after batch completion despite `Status: active`. Compact-nudge-at-invocation-prompts idea folded into 0113 scope. Four observations documented in research file. Session transcript filed at `Dev/Planning/test-log/session-transcript.md`.

**Decisions taken and why.** Filed all three bugs as a single batch (0116) rather than individual entries — they share a root cause (`_METHOD_INFRA_DIRS` coverage gaps) and will be fixed in the same files. Updated 0095's parked note — dependency on 0088 is now met, but parked for a different reason (cowboy-testing is sufficient for now). Updated 0113 and 0114 risk notes to reflect that base build flow is now validated.

**Pivots and surprises.** The build phase worked end-to-end despite the three bugs — all had workarounds (pre-V90 status fallback for Bug 1, `planning/drafts/` location for Bug 2). The most significant UX finding was that `/compact` between skill invocations is critical — a fresh session starts cold even with full project docs, while a compacted session carries context seamlessly.

**Carried forward.** 0116 (three pre_tool_use.py bug fixes). 0113 scope expanded with invocation-prompt compact nudge.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 0 plugin files (E2E test — observations only)
- **Carve-outs:** None
- **Claude-verified tests:** 0
- **User-verified tests:** 0
