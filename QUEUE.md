# QUEUE

Entries are worked top-to-bottom. Each entry has a type marker and a clear scope.

## Next up

- [build] Add mid-build course-correction procedure to next.md — when Claude realises mid-build that scope grew beyond estimate, stop at a clean boundary (finish current file), /done what's shipped, split remainder back to queue. Compact mid-build is last resort, not primary offer. Files: `si-plugin/docs/next.md`. [Requested]
- [build] Add missing rules and compact nudge to behaviour.md — (1) SPEC.md is read-only during builds, (2) one build at a time, (3) between-skill compact nudge. First two mirror CLAUDE-TEMPLATE.md rules that behaviour.md currently lacks — if compaction drops the CLAUDE.md rules, behaviour.md is what remains. Files: `si-plugin/docs/behaviour.md`. [Requested + Discovered]
- [build] Add findings-routing step to done.md — when a [test] validation surfaces findings, /done should route each finding to QUEUE.md as a queue entry, not just log them under "Deferred." Currently findings only land in the LOG, where nobody looks to pick up work. Files: `si-plugin/docs/done.md`. [Discovered]

## Parked

