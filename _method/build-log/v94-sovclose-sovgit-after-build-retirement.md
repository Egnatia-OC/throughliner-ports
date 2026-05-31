# v94 — 2026-05-26 — /sovclose + /sovgit skills, after-build.md retired

**What shipped.** Two new skills (`/sovclose`, `/sovgit`) and their procedure docs (`close.md`, `git.md`). `/sovclose` dual-path: post-build path absorbs after-build.md's full 14-step workflow; planning/general path is lighter (idea sweep, proxy regen, `/sovgit` nudge). `/sovgit` walks non-coders through commit/tag/push with first-use solo/team detection. `after-build.md` deleted. `build.md` completion changed from auto-proceed to `[PROMPT]` nudge. All skill-to-skill transitions now use `[PROMPT]` nudges.

**Decisions taken and why.** Planning/general path skips build-log entry — planning sessions leave no persistent build record beyond the git commit. Keeps the close lightweight for non-build sessions. `## After-build steps` section name in CLAUDE-TEMPLATE.md kept for backwards compatibility with existing consumer projects.

**Pivots and surprises.** crash-course/index.html had a stale Stop hook reference from 0079 — replaced during the sweep. Surface area was large (23+ files touched) but mechanical — no design surprises.

**Carried forward.** Dev-side backlog proxy (`planning/.proxies/backlog.md`) is stale — line numbers and queued batch list need regeneration. Not blocking.
