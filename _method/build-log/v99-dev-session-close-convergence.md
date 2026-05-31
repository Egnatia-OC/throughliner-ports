# V99 — 2026-05-27 — Dev-side session-close convergence

**What shipped.** Two dev-side protocol changes. (1) Response-shape tags added to all 11 close steps in `session-protocol.md`, matching the plugin-side convention from `universal-behaviour.md`. (2) New step 6 — proxy regeneration — inserted between idea sweep and pre-commit checkpoint, making the regen explicit rather than silently skippable. Tag definitions added to `session-reference.md` (cross-referencing plugin-side for authority). Step count 10→11; pre-commit checkpoint reference updated from "steps 1–5" to "steps 1–6".

**Decisions taken and why.** (1) Tags reproduced in session-reference.md rather than just cross-referencing — dev-side sessions don't routinely load plugin docs, so the definitions need to be reachable from the dev doc set. (2) Proxy regen step placed at 6 (after idea sweep, before checkpoint) so the checkpoint can verify it happened — same reasoning as plugin-side close.md's ordering.

**Pivots and surprises.** None. Straightforward doc edit.

**Carried forward.** Nothing.
