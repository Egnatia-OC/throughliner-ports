# 0083 — Gemini search MCP server

## Goal

Add a research-search flow where Claude drafts a search query, proposes it to the user for approval, sends it to Gemini via an MCP server, and files both the query and response in the project's research folder. Claude watches for opportunities to use it proactively but always defers to user approval.

## Design decisions (settled)

- **Mechanism**: Python MCP server exposing a `search_gemini` tool. Installed separately from the plugin.
- **Trigger**: Claude proposes (proactively or after user nudge); user approves before send.
- **Query authorship**: Claude always drafts the query — user never writes it themselves.
- **Slash command**: `/research` as a no-argument nudge (tells Claude "think about what to search here").
- **File location**: `research/search-queries/` inside the consumer project.
- **Fallback when MCP unavailable**: Claude detects the MCP server isn't installed and offers two alternatives:
  1. Produce a formatted search query for the user to paste into their preferred web search agent (Gemini, ChatGPT, etc.)
  2. Perform a web search on the spot using Claude's built-in WebSearch tool.
  Either path still saves results to the research folder using the same query file template.

## Query file template

```markdown
---
status: pending | complete | discarded
date: YYYY-MM-DD
session-context: [active scope file or task]
---

## Trigger
[One sentence: what Claude or the user was doing when the need arose]

## Decision it informs
[What choice or action is blocked or uncertain without this answer]

## Query
[The exact query sent to Gemini]

## Good-answer criteria
[What a useful response would contain — so the result can be evaluated, not just filed]

## Response
[Gemini's response, filled after return]

## Outcome
[One sentence: what was done with the result — used, discarded, superseded, spawned further questions]
```

## Inputs

- Gemini API documentation (for MCP server implementation)
- Existing research folder convention (`sovereign-implementer/research/`)
- MCP server patterns (Python FastMCP or similar)
- `/mcp-builder` skill — invoke at build time for implementation guidance

## Outputs

- `plugin/mcp/gemini_search.py` — the MCP server
- Plugin config to register the MCP server
- `/research` skill definition
- `plugin/templates/` update: `research/search-queries/` scaffolded by `/setup`
- Reference manual section on the search flow

## Success criteria

- Claude can propose a Gemini search, get user approval, and file results — all within a normal session.
- Query files follow the template and contain meaningful "Decision it informs" and "Good-answer criteria" fields.
- `/research` nudge triggers Claude to draft a query without the user writing one.

## Open questions for this session

1. **API key management** — where does the Gemini API key live? Environment variable? `.env` in project root? Global Claude Code config?
2. **Response length** — should the MCP server truncate or summarise long Gemini responses before returning them, or pass the full response and let Claude summarise?
3. **Naming convention** — how should query files be named? Date-based (`2026-05-25-auth-middleware.md`)? Numbered (`001-auth-middleware.md`)? Slug-only?
4. **Scope of proactive suggestions** — should the plugin's universal-behaviour rules include guidance on *when* Claude should suggest a search vs. just proceeding with its own knowledge?

## Risks / dependencies

- No hard dependency on the subagent removal chain (0079–0082). Can be built independently.
- Requires a Gemini API key — the user needs a Google AI Studio account.
- MCP server registration in Claude Code desktop app may have friction (marketplace vs. manual config).
