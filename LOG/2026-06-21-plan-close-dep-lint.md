# 29ba751 - post_tool_use.py: add a Depends-on ordering check to the QUEUE.md lint

The mechanical net for dependency-integrity: the lint now flags (advisory, never blocks) a batch whose Depends on: names another active batch positioned later in Batches than itself - the out-of-order dependency /next trips on. It reuses the cleaned-up slug resolution so a dependency that resolves to a Deferred-tests slug (staged) or to nothing (shipped) is not treated as an ordering error, and a parked target is skipped (depending on a parked item is a block, not a mis-order). An in-session fixture test confirmed below/above/staged cases.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py

**Routed to Captures:** none
