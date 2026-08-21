# [HASH] — The build view now carries each item's rule-gate disposition, so a build transcribes instead of halting

Build entry; the planning record is `2026-08-21-build-view-strips-the-gate-disposition.md`. Raised by the user: if CLAUDE.md is editable in a build, the build can justify what it built. The decide-versus-type split answers that only if the build can *see* the disposition it transcribes — and the view stripped it as decision history, making every rule-authoring build halt by the letter of the instruction.

Built first in the run, by Claude's ordering call: after it, the regenerated view carried every later rule-amending item's disposition, so the rest of the run transcribed rather than halted — the fix proving itself in the same run. `generate_build_view.py` now pulls labelled `Rule gate:` and `FAQ:` lines from each cleared item's prose into its view block, tolerating the bolded label and skipping lines already inside the block. CLAUDE.md's halt instruction narrowed to its intended case: transcribe where a disposition exists anywhere, halt only where none was ever written. BUILD-VIEW.md gitignored, closing the untracked-file observation the item carried.

**Files touched:** `plugin/throughliner/scripts/generate_build_view.py`, `CLAUDE.md`, `.gitignore`, `resources/testing/test_build_view_gate_disposition.py` (new, 5 assertions).
**Routed to Captures:** none from this item.
Tick: done, confirmed — the new test passes and the regenerated view shows the lines.
FAQ: not needed because nothing a consumer does changes — the view is machinery.
Rule gate: run — the generator change authors no rule; the one rule text touched is CLAUDE.md's halt instruction, amended in place so it fires only where no disposition exists anywhere — which was its intended case. Nothing freestanding, nothing evicted.
