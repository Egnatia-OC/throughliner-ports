# [HASH] — Surfaced the unscoped-build state, so a build with no file list stops looking identical to a contained one

`pre_tool_use.py` reads `if build_files is None: return 0` — an absent `Files:` section means no file enforcement for the whole session. **That fail-open is correct and was not changed.** A build whose scope genuinely isn't settled shouldn't be locked out of every file, and /next writes the section itself, so in normal operation it is always present. No denial behaviour moved.

The defect was invisibility. A session running with no containment looked exactly like one running with full containment, while every doc-level scope rule is written assuming the floor is there. The asymmetry is what marked this as an unclosed door rather than a considered choice: the *malformed* case was hardened deliberately, so a badly-parsed inline `Files:` yields a non-empty list precisely to stop it silently disabling the lock. Someone thought about silent disabling and shut one door; the absent case is the same door, left open.

The advisory rides a tool result rather than session start. That placement was weighed and decided in the item, and this session's own first build point vindicated it: the session-start payload is exactly the thing that was being truncated, so an advisory placed there might not have arrived at all.

Delivery uses PreToolUse's `additionalContext`, which lands next to the tool result. `permissionDecision` is deliberately omitted — emitting "allow" would have bypassed the user's normal permission prompt as a side effect of printing a note, which is a real behaviour change smuggled in behind a message.

It is worded as state, not alarm, because an unscoped build is a normal condition; the line exists so the session knows which regime it is in.

Built in the same pass as the planning-session gate, per the item's own instruction — same file, same function, and three separate passes over one hook is the consolidation this queue keeps paying for.

One residue found while building and captured rather than fixed: the de-duplication marker is keyed to the project path and never cleared, so the advisory fires once per project rather than once per session — see [unscoped-advisory-fires-once-ever].

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `SPEC.md`
**Routed to Captures:** [unscoped-advisory-fires-once-ever]
