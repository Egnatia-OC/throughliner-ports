# Graduation step 2: CLAUDE.md reconciliation

**Goal.** Rewrite the dev CLAUDE.md into the plugin's template format so SessionStart can parse it and hooks can find the path block. The current CLAUDE.md has 100+ sessions of accumulated instructions; the template expects a product overview + path block + project-specific notes.

**Approach.** Archive current CLAUDE.md as `Dev/CLAUDE-pre-graduation.md`. Write new CLAUDE.md using CLAUDE-TEMPLATE.md as the skeleton. Carry forward all still-relevant dev instructions under `## Project-specific notes`.

**Inputs.** `_method/research/dev-side-architecture-map.md` — section-by-section mapping of current CLAUDE.md to template destinations.

**Scope.**

1. Archive current CLAUDE.md.
2. Write new CLAUDE.md with template structure: Product overview (what SI is, who it's for, what friction it solves, milestones), Language, path block (pointing at `_method/` from 0148), Project-specific notes, After-build steps.
3. Product overview: distill from current "What this project is" and "Main goal."
4. Project-specific notes: carry forward design constraints, dev/plugin disambiguation, E2E test workflow, host/target vocabulary, adherence-drop diagnostic, experience level, command execution, proactive research, Taskflowapp reference.
5. Drop sections made obsolete by graduation: convergence strategy, dev-project marker file, "Read this first" load-order instructions (plugin procedures handle this), "Make BACKLOG edits directly" (plugin already does this).
6. Keep Current state section — updated each session close.

**Outputs.** New CLAUDE.md in template format. Archived old CLAUDE.md.

**Success criteria.** SessionStart hook can parse the new CLAUDE.md (path block resolves, product overview populated). All still-relevant dev instructions preserved in project-specific notes. Nothing silently dropped — obsolete sections listed in the build-log entry with reason.

**Standing constraint (all graduation batches).** Copy, don't move. Dev/ originals stay in place as a safety net. `_method/` is canonical; Dev/ is the fallback. Do not delete, rename, or git-rm any Dev/ file as part of graduation work.

**Risks / dependencies.** Depends on 0148 (needs `_method/` paths for the path block). Risk: judgment calls on what's "still relevant" vs. "obsolete." Mitigant: archive the original — nothing is permanently lost.
