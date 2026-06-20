# [HASH] - plugin.json: fix the hook count in the description - three hooks, not two

The install/marketplace-screen description undercounted the plugin's hooks (two for scope enforcement) when it ships three - session_start and pre_tool_use enforce, post_tool_use advises. This blurb is shown to every installing user, so the wrong count was consumer-visible. The description now names three hooks (two enforce scope and git safety, one advises on queue structure), matching the wording used in marketplace.json.

**Files touched:**
- plugin/si-plugin/.claude-plugin/plugin.json

**Routed to Captures:** none
