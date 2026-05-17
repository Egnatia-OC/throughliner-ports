---
description: Build the top unticked batch from BACKLOG.md. Argument-less — out-of-order batches are handled by reordering BACKLOG.md during planning, not at build time.
allowed-tools: Read, Bash, Task
---

The user has invoked /build. Prepare the batch-executor payload, then spawn the batch-executor subagent via the Task tool.

**Step 1 — parse BACKLOG.md.** Read `CLAUDE.md`'s path block to resolve where `BACKLOG.md` lives in this project. Run:

    python "${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py" "<BACKLOG.md absolute path>"

Both paths quoted — Windows paths with spaces break unquoted invocations silently. The parser emits a JSON payload on stdout for the top unticked build batch — or `{}` if no top unticked batch exists. The parser is lenient: any structural failure (missing file, unparseable section, template-placeholder batch) also results in `{}` and exit 0, so detect the empty case on output content, not exit code.

**Step 2 — handle the empty case.** If the parser returns `{}` (or any falsy/empty payload), do NOT spawn batch-executor. Tell the user plainly there's nothing to build and prompt them to run `/before-build` or switch to planning.

**Step 3 — spawn batch-executor.** Pass the JSON payload verbatim to batch-executor via the Task tool, embedded in a short prose prompt naming the route — e.g. "User invoked /build. Execute this batch. Payload follows: <JSON>". Do not summarise, reshape, or modify the JSON; the subagent's input contract depends on its exact shape.

Relay batch-executor's completion note to the user without restructuring. The build recap itself is produced by the after-build subagent — the Stop hook will route to after-build when batch-executor's turn ends (V27). Do not invoke after-build manually here; the Stop-hook routing is the intended path.

This is the same parser, same payload shape, and same subagent the Stop hook uses for auto-continuation between batches — `/build` is the explicit-invocation entry point for the same flow.
