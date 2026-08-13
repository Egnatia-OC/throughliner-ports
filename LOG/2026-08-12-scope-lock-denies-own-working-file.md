# 16ed591 — The scope-lock denied every build its own working file, and the run that found it could only proceed by working around itself

Not a queue item. This was found within minutes of locking scope on a seventeen-item run: the first attempt to write a rule-gate disposition into the build working file was denied outright by the scope-lock, with the file's own name absent from the list of paths it allowed.

The cause is one missing argument. `pre_tool_use.py`'s scope-lock exempts "this session's working files" by calling `_is_method_doc(filepath, cwd)` — a function whose third parameter is the session id, defaulting to the empty string. With no id, `working_file()` resolves the name through `safe_session_id("")`, which falls back to `unknown`, so the exemption looks for `_build-unknown.md` and can never match a real working file. Every scoped build has therefore been denied every write to the file that holds its progress ticks, its change notes, and the dispositions the close transcribes. It is the same failure family as the two stale-fixture items shipped in this same run, and the pre-flight glob in the third: a rename to session-scoped names that left a call site behind.

The fix is to pass the id. Confirmed as the only call site by grep before and after.

What is worth recording beyond the fix is the ordering problem it created, because it is the kind of thing a later session will hit and should not have to re-derive. The fix lives in the target; the running session reads the installed host, which still carries the defect. So the file could not be edited to add itself to scope, and the file that grants scope could not be edited either — each blocked by the other. The way through was to move the working file aside, which disengages the scope-lock entirely (with no build file present the hook asks rather than denies, and recognises working files by shape), rewrite it with both `pre_tool_use.py` and its own path listed, and carry on. Listing the working file in its own `Files:` section is what let the rest of the run tick progress normally against a host that still has the bug.

The user approved adding the file to scope before either edit was made.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`

**Routed to Captures:** [scope-lock-fix-unverified-live]

Rule gate: not needed — a one-argument correction to existing code, authoring no rule and changing no always-loaded text.
