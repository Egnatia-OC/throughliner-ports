# [HASH] — pre_tool_use.py — call-built open() paths now read as computed and denied

The hole ([shell-guard-blind-to-call-built-paths]): `open(os.path.join(d, 'x.md'), 'w')` passed the guard entirely — the literal extractor found no path, and the computed detector's pattern excludes parens and commas, so a call-built argument matched neither and the command ran. This is the exact failure the guard was written for; the bare-variable form of the same path was already denied. Found and verified by direct drive while reproducing a sibling defect, deliberately not fixed there because widening the general pattern with `.+?` risks matching across unrelated arguments — the fragile general-parsing the module rejects, refused again here.

The fix as settled at processing: one additional regex (`PY_OPEN_WRITE_CALL`) used only by the computed-target check, matching an `open(` whose first argument is a call with at most one level of nested parentheses, followed by a write mode. Anything it matches is computed by construction, since a call argument is never a quoted literal. The one-level limit is stated in the pattern's comment; a doubly-nested call still escapes.

Tick: done, confirmed (28 suite cases pass via `py`; direct drive shows computed=True for the join form, the read-mode form does not trigger, literal and scratchpad paths still pass).

Rule gate: not needed — hook code fix, no method rule text touched.
FAQ: not needed because the guard's user-visible behaviour (deny with an explanation) is unchanged in kind.

**Files touched:** plugin/throughliner/hooks/pre_tool_use.py, resources/testing/test_pre_tool_use_shell_writes.py
**Routed to Captures:** none
