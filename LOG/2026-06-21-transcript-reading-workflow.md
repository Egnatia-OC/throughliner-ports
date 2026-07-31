# 29ba751 - CLAUDE.md: record the session-transcript reading workflow

Self-hosting and E2E testing increasingly evaluate behaviour from the raw session transcript, but no doc said how to get or read one, so each session re-derived it. A new subsection records sourcing the raw .jsonl from .claude/projects (the authoritative, unedited record - not a regenerated reconstruction, which hits handoff-provenance) and, when it would swamp context, preprocessing it with a short Python pass to just the conversation text. The why weighs the alternatives (chunked read, subagent, grep). Host-only dev/E2E workflow.

**Files touched:**
- CLAUDE.md

**Routed to Captures:** none
