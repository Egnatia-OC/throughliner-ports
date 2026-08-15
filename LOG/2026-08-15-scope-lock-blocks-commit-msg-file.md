# [HASH] — The close writes its commit message to the scratchpad, and the doc's backwards reason for the old path is deleted

`done.md`'s commit core told the close to write its message to a file in the project root and justified it: the file is writable *because* the sub-doc deletes the build working file before committing. That is exactly backwards. Deleting the working file is precisely what makes `pre_tool_use` classify the session as planning, which denies the project root — so the doc named the deletion as what makes the write safe when it is what makes it fail. The reporting project's repro was simple: run /next so a working file exists, then /done; the sub-doc deletes it, the commit core runs, and the very next write is refused.

Their workaround is the fix. The message now goes to the session scratchpad and `git commit -F` runs from there. The scratchpad is on the scope-lock's standing list, so the write passes in every session type — a build, a planning close, a freeform close — rather than depending on which kind the hook currently thinks it is looking at. It is also where this project's own temp-file routing already says a file the project never keeps belongs.

The false justification was deleted rather than reworded. A sentence that is exactly backwards would mislead the next reader in the same direction; the replacement states plainly that the scratchpad is on the standing list and therefore always writable.

This session's own close would have hit it, which is how the item was verified without needing anyone else's project.

**Files touched:** `plugin/throughliner/docs-b/done.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the commit core's existing instruction, correcting a path and deleting a false reason. **A genuine eviction rather than an addition:** the wrong justification comes out and a shorter true one goes in. Failure evidence is one reported instance with a repro, confirmed by reading the hook.

FAQ: not needed because the commit-message file is internal machinery — nothing a user does or sees changes.
