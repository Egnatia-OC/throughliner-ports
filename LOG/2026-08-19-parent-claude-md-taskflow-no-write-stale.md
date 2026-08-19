# [HASH] — the parent-folder rule about Taskflow found duplicated, stale in both copies, and needing the INBOX exception

Filed out of the Taskflow bridge conversation recorded in `2026-08-19-taskflow-bridge-request.md`, which is where the reasoning behind the exception itself sits. This entry covers the rule text.

The instruction — Taskflow may be read freely and never written to, no edits and no new files — lives in `My Drive/CLAUDE.md` and in `Taskflow Planning/CLAUDE.md`, and both load into every session opened in this project. Asked which rule it was, the two files were read rather than the version pasted into the session, and three faults came out of one paragraph. It needs Alex's INBOX exception written in, or every future session reads a flat prohibition and stops exactly where this one did. Both copies name a path that is not this machine's — one under `C:\Users\Alex\...`, the other under a `G:` drive — where the project actually sits elsewhere. And the duplication is total rather than confined to that paragraph: both files are 17 lines and byte-identical apart from the path string, so one is a whole copy of the other at a different level, and the Drive-root copy describes folders three levels beneath it.

Two things settled the design. Neither file is under version control — My Drive is not a git repository and the Taskflow Planning folder sits above this project's repo — so write-first's own test returns no and every edit here, including the deletion, is shown before it happens. And the Drive-root copy is deleted rather than reduced to a pointer, because it describes a folder three levels down and `Desktop/CLAUDE.md` already orients anything opened above this project.

A rule is genuinely amended here and no gate is summoned, because the trigger reads staged paths inside the repository and these files are outside it. That silence is recorded as a second instance on [gate-trigger-misses-the-audit-checklist] rather than treated as new: the trigger misses rules held outside the repository as well as rules in unlisted files inside it, and a path list cannot be extended to cover a file the repository does not contain.

**Queue changes:** [parent-claude-md-taskflow-no-write-stale] filed to Unprocessed and kept into Processed, placed second in the cleared region beside the bridge request; a second instance appended to [gate-trigger-misses-the-audit-checklist].

**Work processed:** kept — [parent-claude-md-taskflow-no-write-stale]. Deleted — none.
