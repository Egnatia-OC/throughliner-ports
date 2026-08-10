# 10d6474 — /next stopped copying every run item's rationale into the build working file

Split from [invented-rationale-compounds-past-the-shipped-rule] at the keep-step.
The measurement is the user's finding: on a fifteen-item run the copy came to
roughly eight thousand tokens, all of it text read from QUEUE.md minutes earlier —
and re-paid on every run that touches those items.

`next.md`'s scope-lock now records each run item by flavor, slug and description,
with its rationale read from QUEUE.md where it already lives.

**The safety it had to not break, and how the minimum was established.** `f8b03ea`
deliberately made the scope-lock *copy* items in, so no item's only copy sits in a
file scheduled for deletion and a partial close has nothing to restore. That
decision is not reverted. What makes the pointer safe is the copy-per-item removal
ordering already in the same step: an item stays in QUEUE.md until the moment it is
ticked, so there is never a window where the working file holds the only copy. The
doc says so explicitly beside the pointer, and adds that **if that ordering is ever
changed, this pointer must be revisited with it** — the two together are what
replaced copying the prose in.

The run that built this used the new form on its own twenty-two-item working file.

**Files touched:** `plugin/si-plugin/docs-b/next.md`. `done.md`'s completion
consistency check was read and needed no change — it reconciles ticks against
QUEUE.md, not against copied prose.

**FAQ: not needed because** the working file is Claude's scratch space; the
existing entry describing it still describes it correctly.

**Routed to Captures:** none from this item.
