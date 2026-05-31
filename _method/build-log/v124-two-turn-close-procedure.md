# v124 — 2026-05-28 — Two-turn close procedure (dev-side)

**What shipped.** Restructured both dev-side close paths (implementation and lighter) in `Dev/session-protocol.md` into two explicit turns: a judgment pass (parity, frame corrections, build-log narrative, idea sweep) run while build context is fresh, then a `[PROMPT]` turn boundary recommending `/compact`, then a mechanical pass (script run, proxy regen, commit/tag/push). Updated `Dev/Planning/.proxies/session-protocol.md` with new line numbers, step counts, and two-turn descriptions.

**Decisions taken and why.** Build-log entry stays in Turn 1 (judgment) rather than splitting narrative vs. Performance section across turns — the whole entry benefits from fresh context, and it's one file write either way. The turn boundary is advisory (`[PROMPT]`), not enforced — short sessions can close in one turn without ceremony.

**Pivots and surprises.** None. Straightforward doc restructure per batch scope.
