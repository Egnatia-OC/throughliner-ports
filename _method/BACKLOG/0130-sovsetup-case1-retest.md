# /sovsetup case 1 retest (post-fix verification)

**Unparked.** v142. Test plan rewritten v145 — reconciliation (0136–0139), /sovexplain (0140), plugin OQ fixes (0141–0142) all accounted for. Repackage plugin at HEAD before E2E run.

**Goal.** Verify that v113, v115, v117, and v129 changes work end-to-end in a real `/sovsetup` case 1 run. v113/v115 fixed hook path resolution (7 cowboy-test issues from plugin v90). v117 added setup Q5 (language setting) and BOM hardening. v129 renamed BUILD-PLAN → BACKLOG across the plugin. None verified E2E.

**Inputs.** Fresh empty folder. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. Invoke `/sovsetup` on empty folder. Confirm `detect-case` returns case 1.
2. Walk through all five questions with test content. Verify Q5 (language setting) appears. Answer Q1–Q4 in a non-English language to test Q5 default detection.
3. After scaffold: verify full output structure — `_method/` with `UX.md`, `MANIFEST.md`, `BACKLOG/`, `build-log/`, `test-log/`, `planning/drafts/`, `research/`, `research/search-queries/`, `proxies/` (5 proxy files: ux, manifest, research, backlog, build-log). `CLAUDE.md` at root. All directory names use BACKLOG (not BUILD-PLAN). BACKLOG proxy includes `## Test sessions` section. No separate test-log proxy.
4. After Q answers applied: verify doc population. Q1 → CLAUDE.md `## Product overview` (4 fields) + UX.md `## Project context`. Q2 → UX.md `## UX principles`. Q3 → UX.md `## Functionalities` with `###` entries. Q4 → batch file in `_method/BACKLOG/` with scope content. Q5 → CLAUDE.md `## Language` field + `git config --local core.quotepath false` (if `.git/` exists).
5. Hook path validation (planning phase): Edit `_method/BACKLOG/<batch>.md` → allowed. Edit `_method/proxies/ux.md` → allowed. Edit `_method/planning/drafts/<file>.md` → allowed. Edit `_method/research/<file>.md` → allowed.
6. Bash heredoc test: write a heredoc containing markdown headings → verify no false-positive filename extraction from the write-guard.
7. BOM hardening: verify scaffolded files don't contain BOM bytes that break `safe_read_text()`.
8. Verify recap message and handoff. Handoff should direct to `/sovplan` or `/sovrecap` + `/sovbuild` depending on Q4 scope completeness.

**Success criteria.** Clean case 1 setup with no hook blocks on method-file writes. Full scaffold structure correct. All five Q answers persist in the right docs. Language default detection works. BACKLOG naming throughout. Handoff message matches Q4 scope state.

**Risks / dependencies.** Requires repackaging plugin at HEAD. If scaffold.py still outputs `BUILD-PLAN/` paths (missed in v129 rename), the test surfaces it immediately at step 3.
