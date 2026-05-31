# Graduation step 4: retire dev-side protocol files

Status: parked

**Parked.** v149. Ship after 2–3 sessions of real work under self-management (post-0150). Build confidence that the plugin's procedures cover everything these files provide before deleting them.

**Goal.** Retire session-protocol.md, session-reference.md, and INVENTORY.md once the plugin has proven it covers the same ground through actual use.

**Approach.** Section-by-section comparison: for each section in the dev files, verify the plugin has a matching mechanism (procedure doc step, hook check, template field, VOCABULARY entry). File gap-batches for anything missing. Archive the retired files.

**Outputs.** Retired files archived. Gap-batches filed if any coverage holes found.

**Success criteria.** No dev-side rule exists that isn't enforced or documented plugin-side. CLAUDE.md project-specific notes carry any project-specific rules that don't belong in the plugin generally.

**Standing constraint (all graduation batches).** Copy, don't move. Dev/ originals stay in place as a safety net. `_method/` is canonical; Dev/ is the fallback. Do not delete, rename, or git-rm any Dev/ file as part of graduation work. This batch is the *only* one that may eventually retire Dev/ files — and only after real sessions prove coverage.

**Risks / dependencies.** Depends on 0150 (must have working self-management first). Risk: retiring too early and discovering a gap mid-session. Mitigant: parking condition requires real sessions first.
