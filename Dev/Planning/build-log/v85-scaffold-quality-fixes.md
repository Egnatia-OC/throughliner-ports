# V72 — 2026-05-26 — Scaffold quality fixes

**What shipped.** Four fixes to `/setup`'s scaffold output found during E2E testing (0084). Scaffold script now replaces `[Project Name]` placeholders with the folder name in all templated files. Setup procedure's "apply answers" step now explicitly maps Q1–Q4 to their destinations — Q2 says "write every principle" and Q3 says "write every functionality," preventing the single-principle capture bug. Seeded batch files now include `Status: queued` line. `marketplace.json` description updated from "subagents" to "procedure docs."

**Decisions taken and why.** Used `target_dir.name` (folder name) for `[Project Name]` replacement rather than accepting a CLI argument — the folder name is available at write time without changing the procedure's question-then-scaffold sequence, and is the natural project name by convention.

**Pivots and surprises.** None — all four fixes were straightforward.

**Carried forward.** Nothing.
