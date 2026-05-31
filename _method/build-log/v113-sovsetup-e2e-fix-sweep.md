# v113 — 2026-05-28 — /sovsetup E2E fix sweep

**What shipped.** Batch 0115. Five fixes that prevent `/sovsetup` from completing a clean case-1 run. (1) Handoff step at setup close — tells the user to run `/sovplan` or `/sovbuild` next. (2) UX principles question flipped to yes/no gate with no minimum count. (3) Method infrastructure directories (BUILD-PLAN/, proxies/, planning/) whitelisted during planning phase via `is_method_infra_file()`. (4) Heredoc/here-string stripping in the Bash write-guard — `_strip_heredoc_content()` prevents false-positive filename extraction from content bodies. (5) V56 project-boundary block removed for Edit/Write/MultiEdit — downstream checks (planning source lock, build batch boundary) already cover the threat; Bash write-guard retains its own boundary check. 271 tests (11 new). Doc-code parity: 6 files updated (INVENTORY, universal-behaviour, DOC-STRUCTURE, Reference manual, both crash-course HTML files).

**Decisions taken and why.** Removed the standalone project-boundary check rather than phase-gating it — analysis showed planning source lock and build batch boundary already deny external writes through different paths, making the boundary check redundant for Edit/Write/MultiEdit. Kept the Bash write-guard's own boundary check because shell commands bypass the Edit-tool path. Method infra whitelist checks both `_method/` and root-level layouts for backwards compatibility with pre-0087 projects.

**Pivots and surprises.** None.

**Carried forward.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 3 (pre_tool_use.py, setup.md, test_pre_tool_use.py)
- **Carve-outs:** None
- **Claude-verified tests:** 271 Pass, 0 Fail (of 271 total)
- **User-verified tests:** 0 pending
