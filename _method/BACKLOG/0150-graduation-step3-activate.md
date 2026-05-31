# Graduation step 3: activate self-management

**Goal.** Remove the skip marker, let the plugin manage sovereign-implementer, and verify everything works. This is the session where graduation actually happens.

**Scope.**

1. Remove `.no-code-method-skip`.
2. Scaffold any missing files the plugin expects but 0148 didn't create (e.g. `_method/UX.md`, `_method/MANIFEST.md` if not yet present).
3. Open a fresh session (or `/clear`) and verify SessionStart fires correctly — state summary, orientation, no errors.
4. Verify phase detection works (planning phase when no active build).
5. Verify hook enforcement: PreToolUse allows `_method/` edits during planning, blocks source-code edits.
6. Verify `/sovrecap` can parse the BACKLOG and present a batch.
7. Fix any immediate issues found during verification.
8. Add host/target disambiguation to CLAUDE.md project-specific notes: "You are building target SI from within host SI" with path references.
9. Document the graduation procedure: target SI passes E2E → repackage → install as new host → bump version reference. Lightweight checklist in CLAUDE.md or a dev-side reference.

**Outputs.** Sovereign-implementer is a self-managed project. Issues filed as new BACKLOG entries if not fixable in-session.

**Success criteria.** Plugin recognises sovereign-implementer as a fully adopted project (tier 3). SessionStart produces a coherent state summary. Hooks enforce correctly. At least one skill (`/sovrecap`) works end-to-end.

**Standing constraint (all graduation batches).** Copy, don't move. Dev/ originals stay in place as a safety net. `_method/` is canonical; Dev/ is the fallback. Do not delete, rename, or git-rm any Dev/ file as part of graduation work.

**Risks / dependencies.** Depends on 0148 and 0149. Risk: hooks designed for consumer projects may behave unexpectedly with plugin source code in `plugin/` alongside `_method/` — e.g. batch file-list boundary enforcement might not expect `plugin/hooks/*.py` as valid build targets. Mitigant: this batch is explicitly about finding and fixing such issues.
