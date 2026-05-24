---
description: Build the top unticked batch from BACKLOG.md. Argument-less — out-of-order batches are handled by reordering BACKLOG.md during planning.
allowed-tools: Read, Bash, Task
---

The user has invoked /build. Parse BACKLOG, then spawn batch-executor.

**Step 1 — parse BACKLOG.md.** Resolve path from `CLAUDE.md` path block. Run:

    python "${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py" "<BACKLOG.md absolute path>"

Both paths quoted (Windows spaces). Parser emits JSON for the top unticked batch, or `{}` if none (structural failures also return `{}`).

**Step 2 — handle empty case.** If `{}`, tell the user there's nothing to build — prompt `/before-build` or planning.

**Step 3 — spawn batch-executor.** Pass JSON verbatim via Task tool in a short prose prompt. Don't reshape the JSON.

Relay batch-executor's completion note as-is. The build recap comes from after-build — the Stop hook routes there when batch-executor ends. Don't invoke after-build manually.
