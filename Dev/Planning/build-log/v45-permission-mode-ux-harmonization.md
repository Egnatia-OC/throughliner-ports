# v45 — 2026-05-22 — Permission-mode UX harmonization

**What shipped.** Mode-aware deny messages across all 7 PreToolUse deny paths. Every deny: `[No-code method]` prefix + `What to do:` closing. 4/7 paths add mode-aware suffix in permissive modes (changing permission mode won't help). 3/7 get format standardisation only (sequencing issues, not mode-sensitive). `permission_mode` read defensively; absent values produce no suffix. SessionStart prepends two-layer-permission preamble. Reference manual gains *Two layers of permission*. Footer V40→V41; plugin 0.40.0→0.41.0.

**Decisions.** Format standardisation bundled (identity signal in every deny). Zero behaviour changes (plan-mode defer and MANIFEST allow-with-context both deferred — platform gaps). Substring mode detection (exact enum values unverified).

**Pivots.** Context compaction mid-session (no work lost).

**Carried forward.** Smoke test deferred (each deny path × two modes). Plan-mode hook firing unverified. V45 forward dependency: fold-in carve-out needs its own `[No-code method]` message.

