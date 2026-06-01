# QUEUE

Entries are worked top-to-bottom. Each entry has a type marker and a clear scope.

## Next up

- [build] Fix _build.md whitelist bug in pre_tool_use.py — add `_build.md` to the `_is_method_doc` whitelist so the hook allows Claude to update build progress. Also remove unused `cwd_norm` variable. Files: `si-plugin/hooks/pre_tool_use.py`. [Discovered]
- [build] Add batch-sizing guidance to plan.md — entry specificity criteria (name concrete outputs, not categories) and verification-burden estimate (how many things will the user test? if unclear or >5, split or sharpen before it reaches /next). Files: `si-plugin/docs/plan.md`. [Requested]
- [build] Add mid-build course-correction procedure to next.md — when Claude realises mid-build that scope grew beyond estimate, stop at a clean boundary (finish current file), /done what's shipped, split remainder back to queue. Compact mid-build is last resort, not primary offer. Files: `si-plugin/docs/next.md`. [Requested]
- [build] Add between-skill compact nudge to behaviour.md — when conversation is long, suggest compacting between skill invocations (a natural seam where nothing is in flight). Files: `si-plugin/docs/behaviour.md`. [Requested]

## Parked

