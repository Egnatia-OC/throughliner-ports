# V35 — 2026-05-21 — E2E Taskflow test — `/adopt` validated; planning-subagent first contact

**What shipped.** Dev-internal. First plugin run against real Taskflow (not synthetic). `/adopt` case 1 + case 4 refresh validated — footers bumped on writable docs, locked docs routed through fold-in. TEST-LOG #104–108. Two new OQ entries (footer-stamp fold-in friction, /adopt permission-prompt UX). Marketplace path researched (`research/plugin-marketplace-scoping.md`): relative-path source works for both local and public. V37 scope created.

**Decisions.** Closes as planning/observational (not full E2E — plugin clashed with already-settled Taskflow decisions). No method bump (dev-internal). V37 as own session (marketplace packaging warrants clean smoke test). Local marketplace install over cache copying.

**Pivots.** Previous session blew up mid-planning-subagent (questions clashed with settled decisions). `/adopt` first run from home dir — subagent caught it (refused to scaffold in user profile). "Two configurations" framing was wrong — relative source works for both.

**Carried forward.** Full E2E cycle remains owed. V37 queued.

