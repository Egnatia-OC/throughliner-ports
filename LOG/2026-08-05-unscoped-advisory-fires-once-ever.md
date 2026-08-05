# d9162e4 — the no-containment advisory now re-fires per build instead of once per project's life

pre_tool_use.py's unscoped-build advisory was deduped by a temp-dir marker keyed to the project path alone and never cleared, so the second unscoped build a week later got nothing — restoring exactly the invisibility the advisory exists to fix. _fire_once gains a scope argument; the unscoped advisory passes _build.md's Run: line as the scope, which is stable across a build's own progress ticks and different for each new run. Two rejected scope keys are recorded in the code so they aren't re-proposed: creation time (ctime means inode-change on non-Windows, so ticks would re-arm it) and mtime (every tick re-arms). Fail-open direction preserved — any error fires the advisory. Schema check passed after the change. Processed-and-built in the overnight blitz of 2026-08-05 under the softened bar (fix named in the item, fail-open direction pre-settled); autonomous run — recorded departure.

**Files touched:** plugin/si-plugin/hooks/pre_tool_use.py (_fire_once and its unscoped-advisory caller)
**Routed to Captures:** none
FAQ: not needed because the advisory's wording and meaning are unchanged — only how often it repeats.
