# [HASH] — plan.md Step 2 skip-to-defer routed through reorder_queue.py's new single-item-move mode instead of a hand-retype

Observed 2026-07-31: /plan's in-session skip-to-defer move retyped an item's whole prose block via Edit — the corruption risk done-plan.md's close reorder warns about and routes through reorder_queue.py, but that mover was wired only into the /done close, not plan.md Step 2's in-session move. Scope was narrowed at processing to skip-to-defer only: the keep-move half was already decided against ([queue-move-viewer-lag]) because keeping re-authors the item, so no identical block exists to relocate. Skip-to-defer relocates the item's prose unchanged — a pure byte-move where hand-retyping is the real exposure.

The build added a `--move <slug> <TOP|BOTTOM>` mode to reorder_queue.py: the caller names only the one slug, the script derives the full section order from the file (keeping every other item in place) and lifts the named slug to top or bottom, running the same byte-for-byte block preservation and self-checks as the full-order path. Tested on a scratch queue — the moved item's multi-line body was preserved and the other section plus the cleared-to-run marker were untouched. plan.md Step 2's Skip-to-defer paragraph now instructs the move via `reorder_queue.py --move <slug> BOTTOM`, with the corruption-risk why inline.

**Files touched:**
- plugin/si-plugin/scripts/reorder_queue.py (new --move mode)
- plugin/si-plugin/docs/plan.md (Step 2 Skip-to-defer)

**Routed to Captures:** none
