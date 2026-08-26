# [HASH] — Mid-build scope asks now lead with a recommendation instead of offering a flat menu

A build in the AFK-cats project found a real daylight-saving bug in a file already
in scope, stopped, and asked whether to add the fix or file it as its own item —
two outcomes, no recommendation, in a message that had already established the fix
was small, in one file, and in scope. The user answered "as you recommend", which
is a turn spent asking for the recommendation the question owed them.

The specimen in `next-build.md` was already right; the branch around it was what
let a menu through. It presented minor and significant as a pair of routes, so a
run that had already decided which arm applied could still write both out as
equals. The always-loaded rule being missed is the one on leading with the
decision, alternatives on request.

Both sites are reworded to the same shape: decide the arm first, ask one
recommended question for that arm, and name the other route only as the escape.
The minor arm's specimen now carries the recommendation and the file-it escape
inside the question itself; the significant arm keeps propose-splitting and
demotes carrying-it-through to the escape.

The grep at the keep widened the file list from one to two, and that is worth
noting: the discovery rule's needed-and-minor arm lives in the always-loaded
`skill-nonspecific-rules.md`, not in the build doc, so a fix confined to
`next-build.md` would have left the same flat shape firing in every skill.

**Files touched:**
`plugin/throughliner/docs/next-build.md` — scope-growth branch reworded to a
recommend-one-route shape.
`plugin/throughliner/docs/skill-nonspecific-rules.md` — the discovery table's
"needed and minor" arm reworded from "ask to add it" to "recommend adding it, and
ask".

**Routed to Captures:** none.

Tick form: done, confirmed — both sites re-read for a readable-as-a-menu shape,
and the typed block still parses as a block.

Rule gate: run — amendment to the scope-growth branch's wording and to the
discovery table's needed-and-minor arm, both reworded to lead with the recommended
route, nothing new admitted, nothing evicted.
