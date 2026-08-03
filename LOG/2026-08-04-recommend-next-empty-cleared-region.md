# [HASH] — Split the close's queue-state ladder so below-the-line-only work routes to /plan instead of a dead-end /next

At a close where three fixes shipped and left the readiness marker at the top of Processed with nothing above it, Claude still pointed at /next as a live next step. That's a dead end: with nothing above the marker, /next's pre-flight hits its nothing-cleared exit and soft-stops, recommending /plan.

The capture blamed the build close's own phase, and the correction widened the fix. That phase only delegates — the logic is a shared ladder all three close flavors run, so building it as captured would have fixed the build close and left audit and planning closes broken.

What the ladder actually got wrong: its second rung read "Processed work exists → name the next item and offer /next," with nothing distinguishing work above the readiness line from work below it. The third rung's "Processed empty" didn't catch the case either, because in this state Processed is not empty — it is full of work that simply isn't runnable yet. The state fell between two rungs and landed on the wrong one.

One rung became two. Work above the line names the next item and offers /next as before; Processed holding only below-line work recommends /plan to green-light something, and says plainly that work is waiting but none of it is ready to build. All three flavors inherit it from the one shared file.

Built together with [close-advise-new-session], which rewrites the same rungs — two items editing the same lines would have collided, and doing them together produced one coherent recommendation rather than two passes disagreeing about wording.

**Files touched:** `plugin/si-plugin/docs-b/done.md` (the queue-state ladder under **Recommend next**).
**Routed to Captures:** none.
