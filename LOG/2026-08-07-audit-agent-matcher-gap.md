# 5993a10 — The subagent cost ask-gate was silently absent on this harness; hooks.json now matches both tool names

`pre_tool_use.py` matches `("Task", "Agent")` and its comment says both names occur across harness builds — but `hooks.json` registered only a `Task` matcher. On a harness that presents the subagent tool as "Agent", the hook never runs and the cost ask-gate silently does not exist.

**The item required confirming how the current harness names the tool before building, rather than assuming the fix.** That check was run and it decides the question: **this harness names it `Agent`.** So the gate was not merely theoretically absent — it was absent here, in the project that dogfoods the plugin, on every session.

That matters because of what the gate protects. A subagent can exhaust the user's session usage in one run; the rule exists because a plain "research this" was once silently escalated into a five-subagent fan-out and blew the user's usage. A gate that doesn't fire is indistinguishable from no gate, and nothing surfaces its absence — the code was written for both names, so reading `pre_tool_use.py` alone tells you the gate exists.

The matcher is now `Task|Agent`. Alternation needed no assumption either: the same file already uses `Edit|Write|MultiEdit` and `Bash|PowerShell`, so the form is proven in place. Verified after the change — the file parses and the three PreToolUse matchers read as expected.

**A limitation worth naming:** this is a target-side change, so the gate is still absent in the installed host until this ships and the plugin is reinstalled. The check that revealed the gap is exactly the class of thing the run's premise-verification work is about — a documented behaviour assumed to be wired, and wired only halfway.

**Files touched:** `plugin/si-plugin/hooks/hooks.json`
**Routed to Captures:** none
