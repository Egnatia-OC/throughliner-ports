# [HASH] — CLAUDE.md drive paths: replaced stale G:\ File Stream paths with C:\ mirror-mode paths after the 2026-07-10 move

The project moved off Google Drive's `G:\` File Stream drive to a mirrored local folder at `C:\Users\Alex\My Drive` on 2026-07-10, leaving stale `G:\` paths in the CLAUDE.md docs. Fixed four references across two files: this project's CLAUDE.md (the absolute-paths convention line, the marketplace-add command, and the Taskflowapp E2E path) and the mid-level Taskflow Planning\CLAUDE.md (the Taskflowapp location). The My Drive root drive-org doc was named in the batch but needed no change — it was already reframed to mirror mode on 2026-07-10, and its sole remaining `G:\` mention is the deliberate history note ("G: no longer exists — any path referring to G:\My Drive should now read C:\...") which must stay. Two of the edited files sit outside this git repo, so those edits aren't committed here; only this project's CLAUDE.md change lands in the commit.

**Files touched:**
- CLAUDE.md (this project) — 3 stale G:\ paths → C:\ (committed)
- ..\CLAUDE.md (Taskflow Planning, outside repo) — 1 stale G:\ path → C:\ (not committed)
- My Drive root CLAUDE.md — no change; already correct

**Routed to Captures:** none
