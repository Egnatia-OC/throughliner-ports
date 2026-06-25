# [HASH] — [subagent-ask-gate] subagent cost guard: hardened tool-use rule + PreToolUse "ask" gate on the Task tool + FAQ

Built in a goal run (first of four back-to-back batches). Claude had silently escalated a plain "research this" request into the built-in deep-research skill — a five-subagent fan-out — exhausting the user's Max usage for the first time in weeks. The existing plugin-behaviour.md "Tool use" rule said "don't spawn agents" but carried no why, no stakes, no scope — the one un-hardened rule in an otherwise compliance-hardened doc — and it had slipped before. So one behavioural rule wasn't enough; this lays down two layers.

Layer one, steering: rewrote the "Tool use" section in the doc's compliance-hardened style — "ask before spawning a subagent" as a positive action, the stakes named as the why (a single subagent run can exhaust the user's session usage), an explicit scope (every session type, every skill, any subagent or deep-research spawn), and the named offender with its positive replacement (a plain "look into X" gets inline Read/Grep first, never a silent fan-out). The rationale travels with the rule because on 4.8 a self-enforced rule holds only when its reason does.

Layer two, guarantee: added a PreToolUse gate in pre_tool_use.py matching the Task tool that returns permissionDecision "ask" (never "deny") with a reason naming the token cost — so the user is always prompted before a subagent runs but keeps full choice. Design call worth recording: the gate fires *before* the cwd / SPEC.md adoption checks, so it guards subagent spawns wherever the plugin is installed, not only in adopted projects — a subagent is as expensive in an unadopted folder as an adopted one, and the cost protection is the whole point. Wiring the gate also required a `Task` matcher in hooks.json (the original batch file list named only pre_tool_use.py; the matcher is what actually invokes the hook for Task calls, so it was a needed addition). The escalation choice — hook on top of hardened wording rather than wording alone — is the high-cost case of the escalation heuristic [generalize-authoring-heuristic] records.

Run-now test passed: a simulated Task call returns permissionDecision "ask" with a non-empty reason; Read and a safe Bash call are unaffected. The live-host prompt is a deferred test ([subagent-ask-gate], host-side, observed after reinstall).

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — "Tool use" section rewritten (hardened, three bullets)
- plugin/si-plugin/hooks/pre_tool_use.py — `_ask()` helper + Task ask-gate (fires before cwd/SPEC gates) + docstring updated to three rules
- plugin/si-plugin/hooks/hooks.json — added the `Task` PreToolUse matcher; updated the description
- plugin/si-plugin/templates/faq-template.md — new entry "Why did Claude ask before starting a 'subagent'?"
- plugin/si-plugin/templates/faq-index-template.md — index line for the new entry

**Routed to Captures:** none
