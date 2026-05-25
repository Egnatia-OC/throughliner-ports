# v65 — 2026-05-24 — Memory-routing and research-filing rules

**What shipped.** No scope file. Two rules added to `universal-behaviour.md`: (1) "Route information to artifacts, not memory" — if you can name the destination, write it there. (2) Research-filing made mandatory (was advisory). New `research/memory-write-hook-feasibility.md` — auto-memory writes bypass PreToolUse entirely (#44820 closed as not planned); prose rules are the only viable enforcement.

**Decisions.** Mechanical enforcement investigated first — dead end (memory writes don't use Write tool). Prose rules are the fallback.

**Pivots.** V56 project-boundary check would block memory writes only if they used Write — they don't.

**Carried forward.** Nothing.

