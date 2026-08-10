# [HASH] — Rezip and Release moved to a fetched doc; Push stayed always-loaded

Audit finding 4, approved by the user on 2026-08-09, and the largest single saving
the compliance audit found. `CLAUDE.md`'s ritual section was roughly 25
always-loaded instructions — about a third of that file's whole instruction budget
— and every one fires on an explicit word from the user.

**The split was decided at build, as the item asked, rather than moving the
section wholesale.** The item flagged the risk itself: push runs after every /next
and at any /done, which is a standing condition rather than an explicit trigger,
and the distribution test in `resources/self-authoring-rules.md` is exactly that a
rule which must fire unprompted cannot be fetched — a session cannot fetch a rule
it has never read.

So: **Rezip and Release went out** to `resources/release-ritual.md`, along with the
project-folder-move recovery, which has the same shape. **Push stayed in
`CLAUDE.md`** in full, as did the three-way framing of rezip-versus-push-versus-
release and the on-request rule — because knowing *which* of the three is being
asked for has to happen before the fetched file is ever opened. The fetched doc
says so in its own opening, so a session that lands there is not tempted to think
push was forgotten.

One correction made in passing: the folder-move note asserted flatly that this
checkout is the `queue-redesign` worktree. That merged long ago, so the moved copy
now says to check whether the checkout is a worktree rather than assuming it.

**Files touched:** `CLAUDE.md`, new `resources/release-ritual.md`.

**FAQ: not needed because** rezip and release are self-hosting rituals. Consumers
install from the marketplace and never rezip or publish the plugin.

**Routed to Captures:** none from this item.
