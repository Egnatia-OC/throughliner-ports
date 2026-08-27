# 32675a3 — The release ritual now opens its queue item and closes with its record

A release runs after the close, structurally — it is asked for, and by then the
session that would have recorded it has finished. So a release left no trail at
all, and any constraint written onto the item that scheduled it went unread.

Two steps bracket the ritual now. The first searches the queue for an entry about
this release — a cycle, a version it has to carry, a post waiting on it — and
reads it whole before anything else, because that item is where the constraints
were written down. The last writes the session record under that item's slug, with
its index line, and closes or updates the item.

Both name what happens when no scheduling item exists: proceed, and record under a
plain release entry of its own. A step that only works in the expected case is a
step that silently does nothing in the other one.

**Two alternatives were refused on the item and stay refused.** Barring a release
after the close — post-close is structurally the only slot there is. And a hook to
detect an unrecorded release — the ritual is fetched-on-demand host tooling, and no
hook can see "a release is happening".

**Files touched:** `resources/release-ritual.md` — the two new steps, the eleven
existing steps renumbered, and three within-doc step references converted from
numbers to names so the next insertion does not silently retarget them.

**Routed to Captures:** none.

Rule gate: run — amendment to the release ritual's steps in a host-only fetched doc; no method rule authored, nothing shipped.
