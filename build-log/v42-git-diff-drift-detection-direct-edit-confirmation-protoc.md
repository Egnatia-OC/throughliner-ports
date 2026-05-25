# v42 — 2026-05-21 — Git-diff drift detection + direct-edit confirmation protocol

**What shipped.** New drift check 1 (direct-edit detection) in planning subagent. Runs `git diff <last-tag>...HEAD` + working-tree diff at planning start. Files in previous batch's Files: list and writable surface pass silently. Everything else triggers per-file confirmation walk (path + summary + MANIFEST entry → "Was this you? Yes / No / not sure"). Yes → check conflicts, accept or queue fold-in. No → pause. Existing checks renumbered 2–5. Parity sweep across VOCABULARY, DOC-STRUCTURE, after-build, Reference manual, INVENTORY. OQ "direct-edit users" removed. Footer V39→V40; plugin 0.39.0→0.40.0. Repo-root docs frozen at V39.

**Decisions.** Numbered as check 1 (execution order = listing order). Per-file walk always (no threshold — bulk-confirm is the failure mode). No-tag fallback: diff working tree vs HEAD. Standard fold-in blocks (no thinner shape needed). No new Required behaviour (concrete procedure, not abstract principle).

**Carried forward.** Smoke test pending (scratch fixture with manual edits). `pre_tool_use.py` NO-CODE-METHOD.md citations unfixed.

**Smoke-test instructions.** git init → scaffold → build → tag → manual edit outside Claude → reopen → verify drift check 1 fires with per-file walk.

