# v132 — 2026-05-29 — Close-procedure hook enforcement (batch 0133)

**What shipped.** PreToolUse check (9) — unclosed-build commit guard. Blocks `git commit` via Bash/PowerShell when `_method/active-build.md` exists with all Files: entries ticked but `/sovclose` hasn't run. Mechanical backstop for the doc-side prohibition shipped in v131. Prevents orphaned snapshots that block all future builds.

**Decisions taken and why.** Regex pattern `\bgit\s+(?:-\S+\s+)*commit\b` chosen over simpler `\bgit\b.*\bcommit\b` to reduce false positives on non-commit git commands (e.g. `git log --format="commit"`). Mid-build commits (some files unticked) explicitly allowed — the guard only fires when all files are done and close was skipped.

**Pivots and surprises.** Test failures on first run: `write_text()` on Windows defaults to cp1252 encoding, but `safe_read_text()` reads UTF-8. Em dashes in test fixture content caused silent read failures. Fixed by adding `encoding="utf-8"` to all `write_text()` calls in the new tests.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 1 (plugin/hooks/pre_tool_use.py)
- **Carve-outs:** None
- **Claude-verified tests:** 8 Pass, 0 Fail (of 8 total)
- **User-verified tests:** 0 pending
- **Session notes:**
