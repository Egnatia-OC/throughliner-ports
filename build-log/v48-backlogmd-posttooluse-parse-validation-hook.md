# v48 — 2026-05-22 — BACKLOG.md PostToolUse parse validation hook

**What shipped.** V46 scope. New PostToolUse hook (`post_tool_use.py`) — first use of PostToolUse. Fires after Edit/Write/MultiEdit on BACKLOG.md (resolved via path block). Direct-imports `find_top_unticked_batch` from parser (no subprocess). Heuristic: unticked file bullets exist but parser returns `{}` → format broken → `additionalContext` warning. Template placeholders excluded. Full-file search (catches corrupted headings). Footer V43→V44; plugin 0.43.0→0.44.0.

**Decisions.** Direct import (not subprocess) — fires on every write, must be fast. Full-file search (not section-bounded) — catches corrupted `## Build batches` headings. Non-blocking warning via `additionalContext` (PostToolUse can't deny).

**Carried forward.** OQ "Six prose directives" item 1 resolved; items 2–6 remain. Smoke test deferred.

