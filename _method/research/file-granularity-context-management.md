# File granularity for context window management

## Problem

Large monolithic files (e.g. everything in one `index.html`) cost context window during build sessions. Claude reads whole files — unlike Cursor/Windsurf, there's no chunking or AST-based retrieval layer. Every edit means loading the entire file, burning context on unchanged code.

## Research findings (2026-05-30)

- No AI coding tool currently pushes users to restructure projects for better AI collaboration. Cursor, Windsurf, and Copilot solve this on their end with indexing infrastructure (Merkle trees, dependency graphs, vector search).
- The "context engineering" field agrees that smallest effective context wins, but advice targets instruction files, not project source files.
- The proxy pattern (condensed summary of a large file for Claude to read instead of the full file) and file-granularity guidance are novel to this method — no established prior art found.
- Claude Code lacks the retrieval layer that IDE-based tools have, so file structure matters *more* for this method's users than for Cursor/Windsurf users.

## Design direction

**Posture:** Advisory with built-in assist, not a rule. The plugin explains the tradeoff ("large files cost you context window during building") and offers to do the splitting if the user wants it.

**No-code user reframe:** Splitting files has zero cognitive cost to the user. They don't navigate the file tree manually — Claude does. Whether the project is one file or five, the user's experience ("change the button colour") is identical. Clean win, no tradeoff.

**Timing:**
- **Setup:** Establish the principle in scaffolded docs (CLAUDE.md or UX.md) — "prefer smaller, purpose-specific files over monoliths." Gives Claude permission to suggest splits later.
- **End-of-build:** Natural checkpoint. Work is done, Claude knows current file sizes. Quick size scan; if anything exceeds threshold (~200 lines), surface as an open question at user consent. Not mid-build — that's disruptive and risky.
- **Post-deployment:** Matters less unless maintenance sessions are frequent. The guidance is primarily a build-phase optimisation.

**Threshold:** ~200 lines as a soft flag point (matches dev-side proxy convention).

## Importance rating

- High during build phase (every session pays the cost).
- Low post-deployment (occasional maintenance only).
- Applies equally whether or not the consumer project itself contains AI — the build process always involves AI (Claude).

## Sources

- [Context Engineering Best Practices — Packmind](https://packmind.com/context-engineering-ai-coding/context-engineering-best-practices/)
- [Context Engineering for Large Codebases — Packmind](https://packmind.com/context-engineering-ai-coding/context-engineering-large-codebases/)
- [Context Engineering for Coding Agents — Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
- [AI Context Windows Explained — Local AI Master](https://localaimaster.com/models/context-windows-coding-explained)
- [Context Windows Explained — Inventive HQ](https://inventivehq.com/blog/context-windows-explained-ai-coding)
