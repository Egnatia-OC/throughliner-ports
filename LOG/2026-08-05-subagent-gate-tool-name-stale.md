# 3affa20 — pre_tool_use.py subagent ask-gate now matches both tool names "Task" and "Agent" (docstrings updated) — restores the gate under the harness's current Agent tool name

The gate read `if tool_name == "Task":` — one exact string match, no alias. The current desktop app presents the subagent-spawning tool as `Agent`, so if the harness sends that name in hook payloads, the gate matched nothing and every spawn went unprompted — invisible in use, because a dead ask-gate looks identical to a session that never spawned a subagent. The hook documentation was checked before building, per the diagnosis-order rule, and it names neither tool for PreToolUse, so neither name could be confirmed or refuted. Matching both is correct under either payload, costs nothing if only one ever arrives, and needs no live test to justify — the name has already changed once. The rejected alternative is recorded in the queue item's history: moving the gate to the new `SubagentStart` hook event, which reads like the obvious home and cannot block or ask (informational only), so it would warn after the decision was out of the user's hands. Verified: both names fire the ask; the module docstring and routing comment now name both.

Overnight blitz run (branch overnight-blitz-2026-08-05b): built under the blitz plan's sanctioned departures — approvals deferred to the branch review, no push.

**Files touched:** plugin/si-plugin/hooks/pre_tool_use.py
**Routed to Captures:** none
FAQ: not needed because the change restores intended behaviour — the ask the user sees is unchanged.
