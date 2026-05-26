# V28 — 2026-05-18 — V27 fix sweep: test-confirmation gate becomes functional

**What shipped.** Three V27 bugs fixed and live-tested end-to-end. PreToolUse `WRITABLE_LOGICAL_NAMES` extended with TEST-LOG.md (one-line fix unblocking the gate). New `project_state.py` shared module (helpers extracted from pre_tool_use.py + stop.py). Stop hook gains `is_test_session_open` check — defers batch redirect when previous-session rows unconfirmed. V28-prequel restructure renamed scope files V28→V32. Two OQ entries resolved. TEST-LOG #064–070, all Pass. Smoke-tested live against rebuilt `v27-smoke-fixtures/g4`. Alex's mid-session language-compaction pass across 9 docs folded into commit. **Footers NOT bumped** — V28 restores V27's intended behaviour.

**Decisions.** V28-prequel restructure over expanding V28's `/adopt` scope — fix foundation before building on it. Shared module named `project_state.py` in existing `plugin/scripts/`. Stop hook defers via silent exit, not redirect-to-planning — avoids re-invoking planning mid-read-back. Walkthrough-mode dropped — V27's after-build recap covers the use case.

**Pivots.** Cowork parallel-session corruption at open (phantom `.git/index.lock`; recovered via Explorer delete + `git reset --hard`). V27 fixture was unexpectedly empty; rebuilt 7 files with mtime ordering. Stop-hook V28 fix not uniquely distinguishable from natural fallthrough in test (#069 caveat). Compacted docs landed with `(1)` suffixes (Windows save-as artifact; renamed).

**Carried forward.** V27 Skipped rows #061/#062/#063 need narrower fixtures. Stop-hook unique-verification owed. PLAN.md ↔ scope-file numbering convention to enforce.

