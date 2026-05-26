# V42 — Drift check 1 (direct-edit detection) smoke test (2026-05-21)

`claude --plugin-dir` against `~\v42-scratch`. Full adopt → plan → before-build → build → tag → manual-edit → reopen-planning loop. Plugin v0.40.0.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 123 | 2026-05-21 | V42 | Drift check 1 detects uncommitted manual edit to `index.html` (hello → goodbye) after `git tag v1`, surfaces per-file confirmation walk | `plugin/agents/planning.md` (drift check 1 — direct-edit detection) | Pass | Full loop: adopt → plan → build → tag → manual Notepad edit outside Claude → new session → planning. Subagent diffed against tag, found change, asked per-file confirmation. Shape matches spec. |

