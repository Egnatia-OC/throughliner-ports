# Host/target safeguards for self-developing project

**Goal.** Prevent Claude from confusing the installed plugin (host SI) with the source code being edited (target SI). Three failure modes identified in v152: (1) expecting target edits to take effect immediately, (2) editing the wrong copy of a doc, (3) hooks validating template files as real project files.

**Outputs.** CLAUDE.md behavioral rules in the Host SI vs Target SI section. Possibly session_start.py detection of self-developing project with orientation banner.

**Success criteria.** Claude states "editing target SI" when touching `plugin/` files. Claude never claims target changes are live without reinstall. Claude uses full paths when referencing docs that exist in both `_method/` and `plugin/templates/`.

**Decisions to make this batch.**

- **Layer scope.** Layer A (CLAUDE.md rules) is confirmed. Layer B (session_start.py banner) was proposed — adds runtime orientation but increases per-session read cost. Layer C (pre-tool-use contextual note) skipped. Resolve A-only vs A+B before build.

Changes:
- [Requested] Add behavioral rules to CLAUDE.md Host SI vs Target SI section: state when editing target SI, never expect target changes to take effect, use full paths for ambiguous docs.
- [Suggested] session_start.py: detect self-developing project (e.g. `plugin/.claude-plugin/plugin.json` alongside `_method/`) and emit host/target reminder at session open.

Serves UX.md: Session-open orientation.
