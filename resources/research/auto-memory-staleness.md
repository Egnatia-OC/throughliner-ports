# Auto-memory staleness — is Claude Code's memory system harming us?

**Date:** 2026-06-09
**Question:** Are the entries in `~/.claude/projects/.../memory/` injecting stale or wrong context into sessions in a way that's degrading planning quality?

## Finding

Yes, this is a recognised failure mode of Claude Code auto-memory as of 2026 — not a one-off. Auto-memory accumulates well but doesn't curate itself: snapshots of project state ("V47 promoted X," "ideas scoped to V51/V52") rot fast because the underlying state moves while the memory doesn't. Behavioural/preference memories don't have this problem and stay durable.

Anthropic's own remedy is **AutoDream**, a background sub-agent that consolidates memory between sessions — replacing vague time refs with exact dates and resolving contradictions. We don't have it running, so cleanup is manual.

## Pattern (what goes stale vs. what doesn't)

| Memory shape | Goes stale? | Why |
|---|---|---|
| Project-state snapshot (queue contents at a moment, version-specific scope claims) | Yes, fast | Queue and version state move; the memory is frozen |
| Time-relative references ("yesterday," "last week," "now scoped V51/V52") | Yes | Lose meaning past their window |
| Behavioural feedback ("don't fire a modal over prose," "use tags not prose") | No | Preferences don't decay with project state |
| Reference pointers (where bugs live, what dashboard to check) | Slow | Decay only if the external system moves |

## Implication for this project

Of the eight memory files indexed in `MEMORY.md` at the time of this research:
- Six behavioural feedback files — durable, keep.
- `project_v47-oq-promotion.md` and `ideation-research-and-build-log.md` — both are version/queue snapshots from V47 and V51/V52. Target is at v1.9.0 with no current OPEN-QUESTIONS structure. These are the textbook failure mode and should be deleted, not relied on.

Going forward: avoid writing project-state snapshots into memory at all. The queue itself is the source of truth for "what's planned." Memory is for behaviour, preferences, and external pointers — not for caching queue contents.

## Sources

- [Claude Code Memory Guide (2026): CLAUDE.md vs Auto Memory vs Plugins](https://blog.laozhang.ai/en/posts/claude-code-memory)
- [Automatic Memory Is Not Learning — Brent W. Peterson](https://medium.com/@brentwpeterson/automatic-memory-is-not-learning-4191f548df4c)
- [Claude Code Memory System Explained — Milvus Blog](https://milvus.io/blog/claude-code-memory-memsearch.md)
- [Persistent Memory Across Context Compactions — anthropics/claude-code#34556](https://github.com/anthropics/claude-code/issues/34556)
- [Claude Code AutoDream: Memory Consolidation for AI Agents](https://zenvanriel.com/ai-engineer-blog/claude-code-autodream-memory-consolidation-guide/)
