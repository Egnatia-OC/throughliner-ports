# [HASH] - post_tool_use.py: quiet the queue lint's two false positives in the Captures/Parked region

The QUEUE.md lint over-flagged in two ways that re-fired on every edit. The Blocked-by check resolved slugs only against Batches, so a parked item blocked by a slug living in Deferred tests was re-flagged as stale - now the dangling-ref check resolves against Batches plus Deferred-tests slugs (a staged test is a valid pending trigger), while a slug in neither stays flagged (a fully-shipped blocker is a real unpark signal). The loose-entry detector read a sub-bullet nested under a Parked item as its own standalone entry - _annotate now carries indentation and only a top-level (indent 0) bullet/title starts a new item. An in-session fixture test confirmed all four cases.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py

**Routed to Captures:** none
