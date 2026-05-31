# v100 — 2026-05-27 — /test skill and testing procedure

**What shipped.** New `/test` skill and `plugin/docs/procedures/testing.md` procedure doc. Guides non-coders through pending User-verified TEST-LOG rows one at a time with type-specific walkthrough steps, records outcomes directly to TEST-LOG, and routes failures through structured debugging to BACKLOG.

**Decisions taken and why.**
1. User-verified rows only — Claude-verified tests already handled by `/sovclose`. Avoids duplicate work.
2. Generic type-specific guidance, not per-project templates — Test Description carries project specifics; generic walkthrough shapes (open/interact/observe for Look-and-click, etc.) are sufficient and maintainable.
3. Record outcomes directly to TEST-LOG — planning read-back then skips confirmed rows. Deferring would lose context between testing and next session.
4. Moderate debugging depth — gather symptoms, investigate code, propose diagnosis, route to BACKLOG. No fixing inside `/test`.
5. Consent-gated manual walkthrough for unrunnable Claude-verified rows — Claude explains why it can't auto-run and asks permission before handing off to the user.

**Pivots and surprises.** Skipped batch 0088 (Build E2E test) — user on remote control, E2E requires separate desktop-app session. Crash-course reference.html had stale procedure doc count (said "Five" — was already eight before this session added the ninth). Fixed as part of guide parity.

**Carried forward.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 5 new/modified (testing.md, SKILL.md, close.md, README.md, plugin.json) + 20 footer bumps + 3 crash-course updates + INVENTORY + Reference manual + universal-behaviour.md
- **Carve-outs:** None
- **Session notes:** 0088 deferred, not parked — still top of queue for next E2E opportunity.
