# V105 — 2026-05-27 — Sov-prefix rename for remaining skills

**What shipped.** Renamed four skill directories and all references: `/setup` → `/sovsetup`, `/research` → `/sovresearch`, `/test` → `/sovtest`, `/tersify` → `/sovtersify`. Completes the naming convention designed in v91 (which shipped `/sovrecap`, `/sovbuild`, `/sovclose`, `/sovgit`, `/sovplan`). ~30 files updated across plugin code (hooks, SKILL.md files, procedure docs, spec docs), templates, guides (Reference manual + crash-course HTML), INVENTORY.md, tests, and dev docs. All 244 pytest tests pass.

**Decisions taken and why.** Historical references in the shipped-batch table and build-log entries left untouched — they record what existed at the time. BACKLOG open questions describing future plugin behavior updated (internationalization OQ lines 258/260). The `_method/research/` folder path — which looks like it contains `/research` — correctly left alone since it's a directory name, not a skill command.

**Pivots and surprises.** One missed test assertion (`test_unadopted_empty_folder_deny_mentions_setup`) checked for `/setup` in the deny message — caught by the pytest run and fixed.

**Carried forward.** Nothing.
