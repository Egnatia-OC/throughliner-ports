# 0e62afe — /setup declares itself with a scratchpad marker, so the scope-lock stops denying every write a migration makes

A consumer project reported that /setup could not finish a migration, and reading `pre_tool_use.py` here confirmed it: the planning gate keys on the *absence* of a build working file, and /setup never creates one, so a setup run is classified as planning and every write outside the standing list is denied — no prompt, no override. That covers the version marker, the format-epoch marker, the `.gitignore` lines, the managed CLAUDE.md block and any scaffold file the run finds missing. QUEUE.md is on the standing list, which is why fresh adoption still worked and the failure stayed invisible on the paths most likely to be tested. It was a same-day regression from `8e20122`, where the deny replaced an ask.

/setup now writes `.throughliner-setup-active` into its session scratchpad at the start of a run and removes it at the end, including on the paths that end early. The hook checks for it ahead of the planning branch and allows the write. The scratchpad was chosen because it is writable in every session type — so the declaration itself cannot be blocked by the lock it works around — and because it clears itself, so a run that dies mid-setup leaves nothing to tidy.

Widening the standing list instead was refused at processing and the refusal held here: /setup's targets are the files the lock most exists to protect, and listing them would open them for every planning session in every consumer project to fix a condition that is only true during setup. The marker keeps the exemption scoped to the moment it is true, and reuses the mechanism the hook already has — deciding what a session may write by asking which declaring file exists.

`setup.md` Step 0 also told users that in a planning session, writes outside the usual files "simply ask first". That was false and is replaced: they are denied, and the marker is what lets a setup run through.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `plugin/throughliner/docs-b/setup.md`, `plugin/throughliner/skills/setup/SKILL.md`, `resources/testing/test_plan_quiet_list.py`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the scope-lock's existing session classification, adding one recognised session kind to a mechanism that already recognises two. Failure evidence is one reported instance with a repro, verified here by reading the hook, in a consumer project where the stale managed block it would repair is read by every session. **Nothing is evicted**; the docstring's overreaching sentence is corrected rather than removed, so the net rule text barely moves.

FAQ: not needed because the fix restores behaviour /setup was already documented as having — nothing a user does changes.
