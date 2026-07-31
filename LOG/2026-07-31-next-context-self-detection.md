# 98a9223 — next.md — removed the "if context runs long mid-build" self-detection stop so /next no longer implies it senses context filling

next.md — removed the "if context runs long mid-build" stop from the Rules section. It presupposed /next can detect context filling, contradicting plugin-behaviour.md's fresh-session-handoff rule (Claude learns a session is wearing thin only when the *user* reports it). The user-report path is unaffected — it already lives globally in that rule, so nothing needed adding to next.md. Target-side; live after reinstall.

**Files touched:**
- plugin/si-plugin/docs/next.md

**Routed to Captures:** next-build-context-self-detection (next-build.md's "Context management" section carries the same self-detection premise)
