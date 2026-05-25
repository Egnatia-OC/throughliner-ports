# V71 — 2026-05-26 — First-time user experience

**What shipped.** Three fixes from greenfield E2E findings: (1) `/setup` enforcement — unadopted empty folders now get a deny message saying "run `/setup` first" instead of referencing BACKLOG/before-build which don't exist yet; (2) build-transition UX — before-build recap prompt changed from "Switch out of plan mode, then run `/build`" to "Run `/build` to start building"; (3) parent-directory advisory — SessionStart detects CLAUDE.md files in parent directories and warns that instructions from those files will affect the session. All three tiers + the unadopted-with-work path emit the parent warning. Reference manual, crash-course, and INVENTORY updated.

**Decisions taken and why.** Three scope-file open questions resolved: (1) unadopted deny targets empty/unadopted folders specifically — V29's existing `is_unadopted_with_work()` path already handles pre-existing work; (2) plan-mode reference dropped entirely rather than explained — if the user is in plan mode, Claude handles it at build time; (3) parent-directory warning fires unconditionally — detecting "different project" is unreliable and the warning is cheap.

**Pivots and surprises.** Test `test_empty_folder_silent` broke after adding parent-directory detection because the fixture directory sits inside the sovereign-implementer tree (which has CLAUDE.md in parents). Fixed by switching the "silent" test to `tmp_path` and adding a separate test for the parent warning using the original fixture.

**Performance.** 5 new tests added (4 in test_pre_tool_use, 1 in test_session_start). 172 total, all passing.

**Carried forward.** None.
