# 5993a10 — The queue mover no longer drags the readiness marker when its anchor moves; crossings are reported and the marker's real position is printed

**The defect, diagnosed at processing and reproduced here before the fix.** The marker is not stored as a position: `split_blocks()` records it as an **anchor slug** — the slug of the item directly above it — and `elements_with_marker()` re-inserts it after that same item, *wherever that item has moved to*. So the marker follows its anchor around the section rather than holding its place.

That accounts for the observed failure exactly. `--move merged-plugin-live-verification AFTER concurrent-session-support`, with no `--marker-after` given, moved the marker's own anchor — so the marker was dragged down and landed below a deliberately-shelved item, clearing it to run unattended. The script printed `Processed reordered (50 items), marker placed`, which reads as reassurance and does not say the marker *moved*.

This is serious rather than untidy: that marker is the method's authorisation boundary, setting how much work an unattended /next run may build without the user present. A tool that moves it as a side effect of an unrelated request is silently widening what an autonomous run may do.

**Reproduced pre-fix on a scratch queue in this session**, against the committed script: moving the anchor below a shelved item dragged the marker and cleared that item. Post-fix, the same command leaves the marker exactly where it was and the shelved item stays shelved.

**Four parts built.**

1. **The fix.** The reorder path re-anchors the marker when the moved item is its anchor, reusing the logic `delete_item()` has carried since it was written. That protection was never added to the reorder path, which both `--move` and the full-slug-list form use. An explicit `--marker-after` still wins, because that is the caller asking for the marker to move.
2. **A crossing move is reported, not refused.** Moving an item across the line is a legitimate way to clear or shelve work, so refusing would force a two-step dance for an ordinary operation. The output names the item that crossed and the direction.
3. **`marker placed` replaced** with the marker's actual position — how many items now sit above the line — on every run touching a section carrying it.
4. **Three regression cases** written from the reproduction rather than the field report, so they target the anchor case specifically: the drag case, the negative case (a non-anchor move must leave the marker alone, so the re-anchor branch can't over-fire), and explicit-`--marker-after` precedence.

The suite now runs 24 checks, all green. The bug is **not** confined to `--move` by command name — any operation through the reorder path can trigger it, and the discriminator is whether the moved item is the marker's anchor. That explains every previously-unexplained negative observation, including the nine watched `--move-section` calls folded in from [mover-move-section-marker-evidence]: none touched the anchor.

The fix was then exercised across nineteen live removals during this run's own build loop, and the marker held its position throughout.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py`, `resources/testing/test_reorder_queue.py`
**Routed to Captures:** none
