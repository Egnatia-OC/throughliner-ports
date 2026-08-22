# 576506c — Freeform sessions declare a scope file the scope-lock reads, extending the standing list to their item's files

Found live 2026-08-21: a queued `[freeform]` item's own files were denied by Rule 4's standing list, because a freeform session has no build working file and the deny message's advice — queue the work — described work already queued. The keep shaped the fix as a sanctioned declaration mirroring the build's mechanism: the session writes `_freeform-<session-id>.md` from its item's build block, and the hook permits the listed paths for that session. The list still originates at planning, so nothing widens without an agreed item behind it.

Built: `_freeform_scope_files()` in pre_tool_use.py reuses the existing Files-section parser (one parser, one set of parsing bugs), the Rule 4 branch consults it, and the quiet-path shape widened to `_(build|freeform)-` so the scope file itself is writable — a freeform session's first write. The top docstring's stale "asks, never deny" was corrected to the deny decision. The always-loaded `[freeform]` block gained the one clause telling a session to write the file and report it in one line. Refused at the keep and honoured: no deny-becomes-ask parsing of queue prose, and no reuse of the build working file, which the close reads as a build's.

Tick: done, confirmed — new suite passes: listed path allowed, unlisted denied, no-scope-file behaviour unchanged, standing list intact, the scope file itself writable.

**Files touched:** plugin/throughliner/hooks/pre_tool_use.py, plugin/throughliner/docs/skill-nonspecific-rules.md, resources/testing/test_pre_tool_use_freeform_scope.py (new)
**Routed to Captures:** none
Rule gate: run — admitted as a subordinate clause on the [freeform] flavour block in skill-nonspecific-rules.md, its named parent; no freestanding rule, no slot beyond the clause, nothing evicted; enforcement is the hook's. Failure evidence is one live instance, the 2026-08-21 freeform sitting, worked around by hand on approval.
FAQ: not needed because the declaration is Claude's move, reported in one line; nothing a user does changes.
