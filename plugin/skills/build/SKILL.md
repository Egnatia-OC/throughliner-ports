---
name: build
description: Build the top unticked batch from BACKLOG. Argument-less — out-of-order batches are handled by reordering BACKLOG during planning.
allowed-tools: Read, Edit, Write, MultiEdit, Glob, Grep, Bash
user-invocable: true
---

The user has invoked /build. Parse BACKLOG, then follow the build procedure.

**Step 1 — parse BACKLOG.** Resolve path from `CLAUDE.md` path block. Run:

    python "${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py" "<BACKLOG path>"

Both paths quoted (Windows spaces). Parser emits JSON for the top unticked batch, or `{}` if none (structural failures also return `{}`).

**Step 2 — handle empty case.** If `{}`, tell the user there's nothing to build — prompt `/before-build` or planning.

**Step 3 — follow the build procedure.** Read `${CLAUDE_PLUGIN_ROOT}/docs/procedures/build.md` and follow it, using the parsed JSON as the batch payload.
