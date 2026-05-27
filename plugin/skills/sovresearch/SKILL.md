---
name: sovresearch
description: Nudge Claude to identify and execute a research search for the current work context. No arguments — Claude assesses what to search based on the active task.
user-invocable: true
---

# /sovresearch

The user wants you to think about what external information would help the current work. Assess the active task, identify a gap where research would improve a decision, and follow the search flow below.

This same flow runs when you proactively suggest a search (per `universal-behaviour.md` → *Proactive research*). `/sovresearch` is the user's way of triggering it explicitly.

## Search flow

**1. Identify the gap.** What decision or action is blocked or uncertain without external information? If nothing benefits from research right now, say so — don't force a search.

**2. Draft the query.** Write four fields:
- **Trigger:** what you were doing when the need arose
- **Decision it informs:** what choice is blocked or uncertain
- **Query:** the exact search query
- **Good-answer criteria:** what a useful response would contain

**3. Propose to the user.** Present the draft in chat. `[PROMPT]` — wait for approval before executing. The user may edit the query or decline.

**4. Execute.** Three mechanisms, in priority order:
- **MCP search tool** (e.g. `google_search` from a Gemini search server): call it with the query. Preferred when available.
- **WebSearch tool**: use Claude's built-in WebSearch. Use when MCP search is unavailable.
- **Copyable prompt**: produce a formatted search prompt the user can paste into their preferred research environment (Gemini, ChatGPT, Perplexity, etc.). Use when neither tool is available.

**5. File the results.** Save to `_method/research/search-queries/YYYY-MM-DD-topic-slug.md` using the template at `${CLAUDE_PLUGIN_ROOT}/templates/research/search-queries/QUERY-TEMPLATE.md`. Fill in the Response and Outcome fields. Mention in chat what you saved and where.

If the response doesn't meet the good-answer criteria, say so. The user decides whether to refine and re-search or accept what's there.
