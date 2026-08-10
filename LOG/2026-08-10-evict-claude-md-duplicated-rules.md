# [HASH] — Seven duplicated rules repealed from CLAUDE.md, and four more from the shipped template

Audit findings 1, 2 and 15, approved by the user on 2026-08-09 and 2026-08-10.
The disposition is consolidate-and-repeal, which the self-authoring gate names as
its main eviction lever: delete the copies, keep the shipped ones.

Out of `CLAUDE.md`: only-touch-files-in-scope, one-build-at-a-time, state-problems-
plainly, route-discoveries-to-the-queue, the memory-boundaries paragraph (which was
almost word for word), and the two Working-conventions repeats — run-commands-
directly and route-decisions-to-QUEUE.md. Out of
`plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`: the same first four.

Each was checked against its shipped counterpart before deletion, per the item's
own instruction — a rule stated inside a why-clause is the failure the gate warns
about, and a merely-similar-looking sentence is where it hides. Nothing in the
deleted copies carried anything the shipped versions lack.

**The safety check that makes the template half sound**, stated because it is what
would have made widening wrong: a rule may only be dropped from the template if
consumers still receive it another way, and they do — the rules file ships inside
the plugin and loads at every session start in an adopted project. Nothing is
lost, only the second copy. Cleaning the dev project while the template kept
emitting the defect would have been the narrower half of the job.

Beyond the slots, a standing drift risk goes with them: two copies of a rule can
disagree and nothing mechanical notices when they do.

**Files touched:** `CLAUDE.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`.

**FAQ: not needed because** nothing changed for a consumer — the rules still reach
them, by exactly one route instead of two.

**Routed to Captures:** none from this item.
