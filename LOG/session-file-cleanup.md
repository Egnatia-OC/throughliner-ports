# [HASH] — plugin-behaviour.md + done.md: prevention-first temp-file hygiene with a narrow close-time cleanup

Two levers against accumulating throwaway files. Prevention (the main lever): the scratchpad-routing rule added to plugin-behaviour.md keeps temp files out of the project folder in the first place, so they never become clutter. Cleanup (narrow): a new "Session-file cleanup" section in done.md, wired into the commit core so it runs at every close, offers to delete throwaway files Claude created this session with no future use — one at a time, the user approving each, never auto-delete. A file Claude didn't create this session is never presumed rubbish (the don't-panic reading — it's the user's own work); deletions are warned by recoverability (git-tracked is recoverable, untracked or outside-repo is permanent). Generalises the _build.md / _plan.md working-file lifecycle to other session-created artifacts. The wider sweep of unspecified/orphaned/historical files, and "don't ask again once kept," were dropped in /plan as unsound.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md (scratchpad-routing rule, shared subsection with temp-file-delete-time)
- plugin/si-plugin/docs/done.md (Session-file cleanup section + commit-core pointer)
- plugin/si-plugin/templates/faq-template.md (new entry)
- plugin/si-plugin/templates/faq-index-template.md (index link)

**Routed to Captures:** none
