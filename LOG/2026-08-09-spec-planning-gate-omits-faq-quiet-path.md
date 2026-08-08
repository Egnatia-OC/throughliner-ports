# [HASH] — FAQ/ added to the planning gate's quiet path in both SPEC and the hook's own ask message

Noticed during the 2026-08-08 differential audit's pass 9 but outside its span, so
it was recorded rather than filed as an audit finding, then filed at that close so
it wasn't lost.

`pre_tool_use.py`'s planning-session file gate passes FAQ/ writes silently —
`_is_plan_quiet_path()` includes it, with a docstring explaining why: the close's
FAQ-sync disposition is a mandated edit, and a required step that prompts every
time trains the user to click through the ask that matters. But SPEC.md's
description of the gate named only "the queue, SPEC, the log, the session's own
notes", and the hook's own ask message named the same four. Both under-described
the quiet-list the code enforces.

**Verified at processing, and the ask message was moved from optional into scope.**
The capture had left it as "if judged worth it". Reading both: `_is_plan_quiet_path()`
at line 427 includes FAQ/ with its reasoning, while the ask message at line 858
listed only the four. **The message is the copy the user actually reads at the
moment the gate fires**, so an incomplete list there misleads at the point of
decision — which is worse than an incomplete sentence in a document nobody consults
mid-write. Both were fixed.

SPEC's sentence also gained the one-line reason, since a reader meeting a list of
five files with four explained would reasonably wonder about the fifth.

**Files touched:**
- `SPEC.md` — the `pre_tool_use` bullet's planning-gate sentence.
- `plugin/si-plugin/hooks/pre_tool_use.py` — the ask message's parenthetical list.

**Routed to Captures:** none from this item.

**FAQ:** not needed because the existing entries describing the planning gate don't enumerate the quiet-list; the message the user reads at the moment it fires is now correct, which is where this mattered.
