# 3ed3db1 — Built: the overwrite guard offers kind-suffixed record names, numeric only when both are taken

The guard was handing back `-2.md` hours after the kind-suffix naming rule shipped — a helpful message teaching the retired convention. `_log_collision_suggestion` now offers whichever of `-plan` / `-build` is free (both where both are — the hook cannot see the session's kind and does not need to), numeric only when both kind names are taken, and the refusal cites the record-naming rule. New suite `test_pre_tool_use_overwrite_guard.py`: nine cases covering all three states plus the new-name pass, all green via `py`.

Rule gate: not needed — a hook message change; no method rule text is touched.

Files touched: plugin/throughliner/hooks/pre_tool_use.py; resources/testing/test_pre_tool_use_overwrite_guard.py (new)
Routed to Captures: none
Done, confirmed: suite passes; no bare -N offered while a kind name is free.
