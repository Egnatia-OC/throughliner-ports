# b4de5bf — The script-write guard widened to reach `py -c` and `sed -i`, measured against the suite before keeping the pattern

Two live escapes, both harmless by luck. A rezip bumped `plugin.json` with `py -c "... open(p,'w') ..."` and nothing fired. A `sed -i '' -e '' QUEUE.md` rewrote the queue in place and was harmless only because the empty scripts made no change.

The cause was the invocation half of the test, not the write detection. `PY_INVOCATION` read `\bpython[0-9.]*\b|\bpy\s+-[0-9]`, which reaches `py -3.13` and misses `py -c` entirely — so the write-call detection downstream never ran. That is the worse half of the gap, because this project's own scripting rules steer sessions towards `py` and away from `python` on this machine. The guard covered the invocation the rules discourage and missed the one they require.

The item made one thing a requirement rather than a suggestion: try the candidate pattern against the existing suite first and narrow it if it over-fires. That mattered. A bare `\bpy\b` reaches `py -c` and also fires on the `py` inside `file.py`, because a word boundary sits before it — which would deny `py .../reorder_queue.py`, the one scripted route this check exists to keep open. Narrowed to `\bpy\s+-`, which every real invocation has and no filename does, and pinned with a passing case so a later widening cannot quietly undo it.

`sed -i` needed its own shape, since the existing machinery reads Python write calls. `SED_INPLACE` matches a `sed` segment carrying the in-place flag, and `_sed_inplace_targets()` takes every bare token that is not an option, a quoted argument or an unquoted sed script. Both GNU's attached suffix and BSD's separate one are handled. The same narrowness applies: a form that does not parse cleanly passes, and that limit stays stated rather than hidden.

**A defect in this build was caught by running the suite, which is the argument for running it.** The first draft called the segment splitter `split_segments`, a name that does not exist. The hook raised, emitted nothing, and every deny-case in the suite silently read as "pass" — eleven assertions failing in a way that looks exactly like a permissive guard. Renamed to `_split_segments` and all eighteen cases pass.

The scope limit is kept honest: this reaches these two named invocations. It does not make the guard complete, and nothing here should be read as though it does — an unbounded claim is what let the first gap sit invisible while the suite passed throughout.

Rule gate: not needed — this widens a hook's detection pattern and adds test cases. The rule it enforces already exists in `CLAUDE.md`'s file-safety block.

FAQ: not needed because a consumer's actions are unchanged; a command that was silently allowed is now blocked with an explanation, and the existing FAQ entry on the guard already covers what to do when it fires.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `resources/testing/test_pre_tool_use_shell_writes.py`.

**Routed to Captures:** none.
