# v95 — 2026-05-26 — /sovrecap + /sovbuild rename + lock-timing fix

**What shipped.** `/before-build` renamed to `/sovrecap`; `/build` renamed to `/sovbuild`. Lock-timing fix: `Status: active` moved from the before-build procedure (step 6) to the build procedure (first action). During `/sovrecap`, BACKLOG stays editable so the user can discuss file lists, test plans, and split proposals before committing to the build. Old skill directories (`plugin/skills/before-build/`, `plugin/skills/build/`) deleted; new skills created at `plugin/skills/sovrecap/`, `plugin/skills/sovbuild/`.

**Decisions taken and why.** Procedure doc filenames kept as `before-build.md` and `build.md` — renaming them would break the `${CLAUDE_PLUGIN_ROOT}/docs/procedures/` path convention and add churn with no user-facing benefit. Consumer-facing references use skill names (`/sovrecap`, `/sovbuild`); internal procedure-doc references stay as filenames. Frame-correction applied to BACKLOG batch 0088 (success criteria said `/sovrecap` sets `Status: active` — corrected to `/sovbuild`).

**Pivots and surprises.** Doc-parity sweep caught more stale references than expected — pre_tool_use.py deny message, Reference manual's status tracking and build operations sections, crash-course phase detection, setup.md placeholder warning, planning.md build-operations handoff, and the backlog proxy template (still at V75 from a missed v94 bump) all needed updating. The reference.html slash command list was also stale from before 0097 shipped — missing `/sovclose` and `/sovgit`.

**Carried forward.** Nothing.
