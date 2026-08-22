# d7ea8a0 — Freeform sessions get a sanctioned scope declaration: a marker file the scope-lock reads, kept and cleared

Processed first on the previous close's advisory. The workaround from the freeform sitting — hand-writing a build working file — was promoted to design: a freeform session opens by writing its own scope file (`_freeform-<session_id>.md`) listing the files from its queue item's build block, and the hook enforces that list plus the standing list. Deny-becomes-ask was refused (hook parsing queue prose per write; per-file asking on agreed work). The declare-scope clause goes in the always-loaded `[freeform]` flavour block because a freeform session runs no skill. SPEC's scope-lock paragraph gained the carve-out sentence at the keep. Full rationale, gate disposition and build block on the item in QUEUE.md.

**Queue changes:** kept into Processed, cleared to run, placed with the builds ahead of the post items.
**Work processed:** kept — [freeform-blocked-by-standing-list].
