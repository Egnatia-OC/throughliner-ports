# V70 — 2026-05-26 — Research search flow

**What shipped.** `/research` skill (proactive and explicit research search flow), query file template (`research/search-queries/YYYY-MM-DD-topic-slug.md`), proactive-search rule in universal-behaviour.md, scaffold.py update for `research/search-queries/`, Reference manual section on the search flow, DOC-STRUCTURE spec for search query files, VOCABULARY terms (search query file, proactive research), INVENTORY update. Crash-course fix: stale Stop hook reference removed, `/research` added to slash commands.

**Decisions taken and why.** Five design questions resolved at session open: (1) environment variable for API key — standard, no accidental commits; (2) pass full response — Claude summarises with context; (3) date+slug naming — temporal visibility, no allocator; (4) proactive-search guidance in universal-behaviour — mechanism-agnostic, works with or without MCP server; (5) reuse existing `yukukotani/mcp-gemini-google-search` — plugin's value is the discipline wrapper, not the API call.

**Pivots and surprises.** Scope file assumed building a custom MCP server (`plugin/mcp/gemini_search.py`). Q5 resolution eliminated that — the plugin ships only the discipline wrapper (skill + template + rule). Crash-course audit caught a stale Stop hook reference from V66's subagent removal.

**Carried forward.** None.
