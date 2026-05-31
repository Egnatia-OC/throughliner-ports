# v151 — 2026-05-31 — Graduation step 3: activate self-management

**What shipped.** Sovereign-implementer is now a self-managed project. Removed `.no-code-method-skip` marker. Created `_method/UX.md` (4 principles, 10 functionalities) and `_method/MANIFEST.md` (empty, ready for builds). Fixed `BUILD_LOG_INDEX_REF_PATTERN` in `project_state.py` to accept session-tagged filenames (`v150-name.md`) — the old 3-digit-only regex matched an HTML comment example instead of real entries. Added host/target "building from within" framing and plugin update procedure to CLAUDE.md. Updated milestones to reflect graduation complete.

**Decisions taken and why.** UX.md content written from Reference manual at intent level rather than left as template placeholders — template detection in SessionStart would flag placeholders, and the plugin's features are stable enough to document. MANIFEST.md left empty — entries accumulate through `/sovclose` after real builds. The build-log pattern fix broadened from `\d{3}` to `(?:\d+|v\d+)` rather than `\S+` to avoid matching placeholder text inside HTML comments.

**Pivots and surprises.** The broadened `\S+` regex initially matched the HTML comment example (`NNN-batch-name.md`) before real entries, causing the hook to try reading a nonexistent file. Required a more targeted pattern.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 5 (UX.md, MANIFEST.md, project_state.py, CLAUDE.md, proxies)
- **Carve-outs:** None
- **Claude-verified tests:** 4 Pass, 0 Fail (SessionStart tier 3, phase detection, PreToolUse planning lock, BACKLOG parser)
- **User-verified tests:** 0 pending
