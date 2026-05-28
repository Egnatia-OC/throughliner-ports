# TEST-LOG — [Project Name]

One row per test for every shipped build batch. Per-session files in `test-log/`, newest-first in this index. Maintained by Claude during builds (`/sovclose` writes rows) and planning (per-row read-back confirms). The test-confirmation gate gates new builds against unconfirmed rows.

Full spec: `DOC-STRUCTURE.md` → *TEST-LOG structure*.

<!--
Index format (newest first):
- `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed)

Entry file format:

# Test session — <Session> — YYYY-MM-DD

| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 001 | ... | ... | ... | ... | ... | ... | ... | ... | ... |
-->

---
*No-code method — Version 92.*
