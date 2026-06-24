# [HASH] — SPEC.md "How it works" hooks list — extended the pre_tool_use bullet to also name the subagent ask-gate (a cost guard that asks before Claude spawns a subagent, never blocks), alongside scope-lock and git safety.

The subagent ask-gate will add a new behaviour to the pre_tool_use hook: it prompts before a subagent spawns. SPEC's hooks summary described pre_tool_use as only enforcing the scope-lock and git safety, so it would have been incomplete once the gate ships. This edit extends the pre_tool_use bullet to also name the ask-gate — a cost guard that asks, never blocks. It was ordered before the feature build [subagent-ask-gate], per the spec-edit-first pipeline, so SPEC stays accurate ahead of the build. Kept to a single clause so SPEC stays lean rather than drifting toward boilerplate.

**Files touched:**
- SPEC.md

**Routed to Captures:** none
