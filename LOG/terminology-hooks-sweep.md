# [HASH] — post_tool_use.py + session_start.py: renamed user-facing "work line"→"work item", "top batch"→"top work item", completing [work-item-terminology]

The [work-item-terminology] sweep made "work item" canonical across docs/templates/SPEC/QUEUE-header but excluded the hooks, so the lint output a consumer reads still said "work line," and session_start still told the user to "start the top batch" — the canonical name wasn't canonical where the user sees it.

This build renamed "work line"/"work-line" → "work item"/"work-item" across post_tool_use.py (13 occurrences, user-facing lint strings plus docstrings/comments) and "work line" → "work item" in session_start.py's docstrings, and the user-facing "start the top batch" → "start the top work item". Literal file-line references were kept intact — "line {idx}:", "description line", "heading line" all stay, since there "line" means a file line, not the work unit. Both hooks were syntax-checked and a grep confirmed zero "work line" / "top batch" remaining. Completes [work-item-terminology].

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py
- plugin/si-plugin/hooks/session_start.py

No SPEC/FAQ — internal hook strings.

**Routed to Captures:** none
