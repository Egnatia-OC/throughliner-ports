# v58 — 2026-05-23 — TEST-LOG row pruning

**What shipped.** Scope 0056. Planning subagent now prunes TEST-LOG rows whose Component no longer exists in MANIFEST + legacy Superseded rows, before drift checks. Cross-component rows exempted. DOC-STRUCTURE, VOCABULARY, Reference manual, INVENTORY, BUILD-METHOD updated. 147 tests pass. Footer V52→V53; plugin 0.52.0→0.53.0.

**Decisions.** Component-based pruning (cleanest signal). Deleted outright — git history preserves them; archive file would grow without bound. Placed at planning step 2c (not after-build) since planning already reads MANIFEST.

**Pivots.** Scope file leaned toward archive; pushed back, user accepted deletion. BUILD-METHOD stale reference caught at close.

**Carried forward.** Deferred tests unchanged. OPEN-QUESTIONS entry removed.

