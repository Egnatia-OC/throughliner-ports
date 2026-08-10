# [HASH] — /next now opens a [user] item's LOG entry when the walk-through starts, and appends as it goes

Found at a session close on 2026-08-09 and processed the same day. Caught only
because the session was still in view — a fresh session would have had nothing to
reconcile against.

## What was wrong

Walking through [merged-plugin-live-verification] once required a full rezip:
bumping `plugin.json`, running three test suites, pruning the plugin cache,
reinstalling the host, comparing content stamps. All Claude work, all changing real
state, and none of it appeared anywhere. A `[user]` item never enters the build
working file — deliberately, since that file is deleted at the close and extracting
the item would strand it — so the walk-through branch had no working-file home. A
crash lost everything, and the working file positively suggested none of it
happened, which is worse than an absent record because that file reads as
authoritative.

## The fix, and why not the intuitive one

`next.md`'s walk-through branch now opens the item's LOG entry under its slug when
the walk-through starts and appends each action as it happens. The item stays in
QUEUE.md untouched, so nothing is stranded, and a crash mid-walk-through leaves a
partial entry saying exactly what was done. `done-build.md` handles finding an
entry already started rather than always writing one fresh — the cost the item
predicted, authored rather than assumed.

A section in the build working file was the intuitive fix and was rejected: the
scope-lock keys on that file existing and restricts edits to its `Files:` list,
while a walk-through legitimately touches files no build scope would list — the
live case bumped `plugin.json` and reinstalled the host. A working-file record would
either block the walk-through or force the lock to be weakened. `LOG/` is writable
regardless of scope-lock, and it is where the record has to end up anyway.

**The tension respected while building:** the branch is *supposed* to run whatever
parts Claude can — that is what makes it a live drive rather than a hand-off. The
doc says so explicitly beside the new rule: this is a place to record, never a
restriction on doing.

## Used the same session it shipped

Both `[user]` items in this run had their entries opened live before the
walk-through finished — `2026-08-10-report-url-404.md` and
`2026-08-10-merged-plugin-live-verification.md`. The first records a fetch and the
address handed over; the second records a whole verification pass that would
otherwise have existed only in chat.

**Files touched:** `plugin/si-plugin/docs-b/next.md`,
`plugin/si-plugin/docs-b/done-build.md`.

**FAQ: not needed because** the user sees no difference — the record appears in
LOG/ either way; what changed is when it is written.

**Routed to Captures:** none from this item.
