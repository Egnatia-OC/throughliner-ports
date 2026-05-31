# Graduation step 1: migrate planning artifacts into _method/

**Goal.** Move dev-side planning artifacts into the plugin's expected `_method/` structure so hooks and procedures can find them. Mechanical migration — no content changes, no judgment calls. The `.no-code-method-skip` marker stays in place throughout; the plugin remains inactive.

**Vocabulary.** "Host SI" = the installed plugin doing the work. "Target SI" = the source code at `plugin/` being built. They are never both active in the same session. Building happens under the host SI; E2E testing happens in a separate session with only the target SI installed. "Graduation" = the target SI passes E2E, gets repackaged and installed as the new host SI.

**Scope.**

1. Fix plugin name: `plugin/.claude-plugin/plugin.json` → rename `"name": "no-code-method"` to `"name": "sovereign-implementer"`.
2. Create `_method/` at sovereign-implementer root with subdirectories: `BACKLOG/`, `build-log/`, `test-log/`, `proxies/`, `planning/drafts/`, `research/`, `research/search-queries/`.
3. Move `Dev/Planning/build-log/` contents → `_method/build-log/`.
4. Move `Dev/Planning/test-log/` contents → `_method/test-log/`.
5. Move `Dev/drafts/` contents → `_method/planning/drafts/`.
6. Move `Dev/Resources/research/` contents → `_method/research/`.
7. Split monolithic `Dev/Planning/BACKLOG.md` queued batches into per-batch files under `_method/BACKLOG/`. Shipped-history summary becomes a note in the BACKLOG proxy.
8. Create plugin-standard proxies in `_method/proxies/` (ux, manifest, research, backlog, build-log). Old dev-side proxies (`Dev/Planning/.proxies/`) retired.
9. Update all path references in CLAUDE.md, session-protocol.md, session-reference.md, and INVENTORY.md to point at new `_method/` locations.

**What stays in place.** `Dev/Resources/scripts/`, `Dev/Resources/tests/`, `Dev/Resources/Marketing/`, `Dev/Resources/Iteration playbook/`, `Guides/` — regular project files, not method artifacts. `session-protocol.md`, `session-reference.md`, `INVENTORY.md` — still needed as prose rules until 0151 retires them.

**Outputs.** `_method/` fully populated. Old planning locations empty or removed. All path references updated. Dev-side protocol files still in place but pointing at new paths.

**Success criteria.** Every file the plugin's hooks would look for in `_method/` exists at the expected path. No broken path references in dev docs. BACKLOG per-batch files parse correctly via `parse_backlog.py`.

**Risks / dependencies.** Large number of path references to update — grep thoroughly after moves. Soft dep on 0147 (Ideas/OQ merge changes BACKLOG template) — but dev-side BACKLOG already has no Ideas section, so no conflict. The skip marker stays throughout; no risk of plugin interference.
