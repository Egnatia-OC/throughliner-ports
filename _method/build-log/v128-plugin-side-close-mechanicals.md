# v128 — 2026-05-28 — Plugin-side close mechanicals + two-turn procedure

**What shipped.** Consumer-side `plugin/scripts/bump_version.py` for footer bumps and proxy line-number regeneration. Restructured `close.md` into two turns: judgment pass (MANIFEST through idea sweep, while build context is fresh) then mechanical pass (footer bumps, proxy regen, after-build steps, checkpoint, commit prompt) with a `/compact` boundary between them. Reference manual updated with two-turn description and Scripts bullet. Crash-course guide parity maintained across three HTML files. INVENTORY updated.

**Decisions taken and why.** Script takes simple positional args (`<old> <new>` or no args) rather than the dev-side `--session-tag` flag — consumer proxies don't carry session tags in their headers, so simpler is better. Footer bumps triggered by session-start mismatch detection rather than a dedicated pre-close check — reuses existing infrastructure. Script handles `_method/proxies/` and legacy `.proxies/` locations; skips operational indexes (build-plan, build-log, test-log) that lack source-pointing headers.

**Pivots and surprises.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 7 (1 new, 6 modified)
- **Carve-outs:** None
- **Claude-verified tests:** 1 Pass (syntax check + usage output)
- **User-verified tests:** 0 pending
