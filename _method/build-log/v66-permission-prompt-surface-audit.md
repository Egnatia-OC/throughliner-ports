# v66 — 2026-05-24 — Permission prompt surface audit

**What shipped.** Scope 0066. Root cause: subagents don't inherit parent permission mode (platform bug #28584, #40241, #18950). Mitigations: (a) replaced `allocate_number.py` Bash calls with Glob-based allocation in all five subagents; replaced `git status/diff` MANIFEST detection in after-build with batch Files-list detection; (b) Reference manual updated — Auto recommended for Build/After-build, platform bug documented with issue links. DOC-STRUCTURE, INVENTORY updated. New `research/permission-prompt-surface-audit.md`. Footer V58→V59; plugin 0.58.0→0.59.0.

**Decisions.** Glob-based allocation because every subagent Bash call generates a prompt due to the inheritance bug. Script remains for dev-side use. Auto recommended for Build/After-build (highest Bash volume).

**Pivots.** Planning subagent lacks Bash in `tools:`, so drift check 1 can't actually run — noted, not in scope. `allocate_number.py` removal touched 7 files (more than expected).

**Carried forward.** Planning drift-check-1 feasibility. All deferred smoke tests → 0068.

