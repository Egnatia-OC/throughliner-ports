# 7bc2c58 — The shell-write guard reads `r'...'` as the literal path it is

Reproducing the report showed the disagreement is not in the path check at all. `open(r'C:\...', 'w')` — the ordinary way to write a Windows path in Python — was unreadable to the literal extractor and read as *computed* by `has_computed_write_target`. So a scratchpad path spelled out in full was denied by a message that promises a literal scratchpad path passes. On this machine that fires constantly.

Both patterns now accept a raw/bytes string prefix, and the quoting test strips one before checking. `f` is deliberately excluded: an f-string interpolates, so it is genuinely computed and still denied.

Weakening the computed-target denial stayed refused — it exists for a recorded QUEUE.md corruption where the only difference from the correctly blocked version was one variable assignment.

Five cases pinned: a raw-string scratchpad path passes, a plain one passes, a raw-string path inside the project is still denied, a bare variable is still denied, an f-string is still denied.

The reproduction turned up a second and worse hole, filed rather than folded in.

**Files touched:** plugin/throughliner/hooks/pre_tool_use.py, resources/testing/test_pre_tool_use_shell_writes.py
**Routed to Captures:** [shell-guard-blind-to-call-built-paths]
Rule gate: not needed — a hook fix plus its tests; no method rule changes.
