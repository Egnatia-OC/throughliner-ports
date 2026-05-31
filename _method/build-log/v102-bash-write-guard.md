# V83 — 2026-05-27 — Bash write-guard + skill escape guidance

**What shipped.** Check (h) on PreToolUse: Bash/PowerShell write-guard. Scans shell commands for file-write patterns (`sed -i`, `>`, `>>`, `tee`, `Set-Content`, `Out-File`, `Add-Content`, `cp`, `mv`) and applies existing rules (project boundary, locked docs, batch file list, planning source lock). Skill escape guidance added to all phase-lock deny messages — not just Bash — so Claude names the skill that would unlock the target (`/sovclose`, `/sovplan`, `/sovrecap`, `/sovbuild`). hooks.json updated with Bash|PowerShell matcher routing to pre_tool_use.py. 24 new tests (21 in TestBashWriteGuard, 3 in TestSkillEscapeGuidance). Also fixed pre-existing drift: PLUGIN_METHOD_VERSION was 80, should have been 82; corrected to 83.

**Decisions taken and why.**
- Added Bash write-guard to existing pre_tool_use.py (not a separate file) because the existing check functions (build_locked_map, detect_phase, etc.) are all there and share state.
- Two-stage approach: quick keyword regex first (fast path for 99% of Bash calls), then expensive path extraction only when write patterns detected.
- Null targets (`/dev/null`, `$null`, `NUL`) treated as non-writes to avoid false positives.
- BACKLOG/MANIFEST exempted from Bash guard (same as Edit/Write/MultiEdit flow — always writable).
- Adoption gate (V29) not enforced for Bash — out of scope per batch description; planning source lock already handles unadopted folders.

**Pivots and surprises.** `sed -i` regex initially failed: `\bsed\s[^\n]*\s-[^\s]*i` consumed the space between `sed` and `-i` in the first `\s`, then `[^\n]*` greedily consumed everything. Fixed by using `\b` word boundary instead of `\s` after `sed`.

**Carried forward.** Nothing.
