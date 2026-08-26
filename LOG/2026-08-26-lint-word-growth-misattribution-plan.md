# 0d02b6a — Lint's phantom word deltas explained: the readiness marker counts as its neighbour's words; counter to exclude it

Noticed by Claude, filed at /rescan, kept on Claude's recommendation and your agreement — the cause checked, not assumed. The flagged item's text between HEAD and the working tree is byte-identical; the lint's per-item counter runs each span to the next heading, so the readiness marker's 8 words counted as the adjacent item's and moving the marker at the lift made the item appear to shrink. Fix: post_tool_use.py's word-growth counter excludes the marker line from item spans, with a suite case (item beside the marker, marker moved, delta zero).

**Queue changes:** kept and cleared, in the build set.
**Work processed:** kept — [lint-word-growth-misattribution].
Rule gate: not needed — a counting fix in a hook script.
