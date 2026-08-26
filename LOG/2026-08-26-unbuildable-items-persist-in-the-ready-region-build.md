# [HASH] — Queue digest now flags a cleared item carrying no build block, where planning actually looks

Six items sat cleared to run in Taskflowapp and a build run was the first thing to
catch them — it stopped before locking scope and named all six as unscopeable. The
planning run hours earlier had worked fourteen captures and reported "24 items
cleared to build" with nothing flagged.

**The cause was established at planning by running the digest rather than
assuming.** It reported zero placement contradictions against that live queue while
26 items sat cleared, and the file held 40 items against 24 build blocks. So the
rot was cleared items with no build block at all — and the only two mechanisms that
detect that state fire at moments a planning opening never reaches: the advisory
lint fires on a queue edit, and the view generator halts when a run starts. This
build puts the same mechanical check where planning looks.

**The duplication with the lint is deliberate and recorded in the code**, because
the two triggers differ. The lint speaks when the queue is *written*, which is the
cheapest possible moment; the digest is read at every planning opening. An item
that becomes blockless by any other route — a change to what a block must carry, an
edit made outside the editing tools — is never re-examined by the lint, and the
live failure got past a lint-only arrangement.

The guards are what keep it off the normal state of a queue: `[user]` and
`[freeform]` items are exempt because neither is built from a block, held work is
exempt because it isn't built until it lifts, and a capture is exempt because it
isn't work yet. Firing on any of those would be the cry-wolf shape this project has
repealed measures for twice.

**Files touched:**
`plugin/throughliner/scripts/queue_digest.py` — `BUILD_BLOCK_OPEN` constant and a
blockless-cleared-item contradiction class.
`resources/testing/test_queue_digest.py` — a `BLOCK` fixture constant, two existing
fixtures given blocks so an unrelated contradiction count doesn't move, and six new
cases.

**Routed to Captures:** none.

Tick form: done, confirmed — the suite passes at exit 0, and the edited digest run
against this project's own queue prints zero placement contradictions, so nothing
carrying a block is caught.

Rule gate: not needed — a mechanical check added to a shipped script, no method
rule authored or amended.

SPEC already carries the sentence naming the new contradiction class, written at
the keep.
