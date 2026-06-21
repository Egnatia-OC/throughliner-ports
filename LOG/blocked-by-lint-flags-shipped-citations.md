# [HASH] — post_tool_use.py: the QUEUE.md lint's dangling-ref check resolves slugs against LOG/index.md, so a shipped or context-cited slug in a Blocked-by tail no longer false-flags

The structure lint's dangling-reference check (check 4) flagged any slug named in a `Blocked by:`/`Depends on:`/`Blocks:` header that wasn't defined in the file or staged in Deferred tests — including shipped prerequisites cited for context in a prose tail. Because a shipped slug is gone from the queue, such a citation read as unresolved forever and re-fired on every QUEUE.md edit; it fired seven times during the 2026-06-21 /plan, a live demonstration.

Settled on candidate (b) of the two the batch named — resolve a named slug against LOG/index.md before flagging, the more general "check the authoritative record" shape — because it's the fail-safe: a satisfied citation must never read as dangling, and over-resolving only quiets an advisory flag. New `_shipped_slugs(cwd)` reads LOG/index.md and collects every `[slug]` token; `_check_dangling_refs` now resolves against defined | deferred | shipped, and only a slug resolved by none of those flags. `lint()` gained a `shipped_slugs` parameter (default empty, so existing callers/tests are unaffected) and `main()` passes `_shipped_slugs(cwd)`. The prose-ref check (check 6) deliberately stays on defined slugs only — adding shipped slugs there would start flagging citations the absent-slug skip currently quiets. Module docstring, function docstrings, and the denial message updated to match.

A known precision nuance was filed as a capture: reading every `[slug]` token in the index also resolves slugs merely *named* in a /plan summary (promoted-but-not-built), so a later-dropped-without-shipping slug wouldn't flag — accepted as within the chosen fail-safe.

Run-now test (in-session) passed: with no shipped knowledge a shipped-slug citation flags (reproducing the bug); with the shipped set it no longer flags while a genuinely-unresolved ghost slug still does; `_shipped_slugs` read the real LOG/index.md (171 slugs). All three hooks byte-compile clean.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py — `_shipped_slugs(cwd)`; `_check_dangling_refs` resolves against defined | deferred | shipped; `lint()` gains `shipped_slugs`; `main()` passes it; docstrings + denial message updated.

**Routed to Captures:** [shipped-slugs-breadth] (the index-mention ≠ shipped precision nuance).
