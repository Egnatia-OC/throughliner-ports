# 29ba751 - next.md + plugin-behaviour.md + FAQ: make /next's pre-flight scope flag loop-aware so it does not recommend a non-terminating fix

The pre-flight blocker gate recommended popping to /plan to incorporate a capture first, even when that capture was transitively blocked by the very batch being completed - a loop that can never terminate, which a user had to catch by hand. The gate now checks whether the flagged item is transitively blocked by the current batch; if so it surfaces the circularity and recommends building the minimal first version to break the loop, leaving the item's parked/blocked mechanism to hold the gap. The check redirects the fix without suppressing the completeness flag.

**Files touched:**
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
