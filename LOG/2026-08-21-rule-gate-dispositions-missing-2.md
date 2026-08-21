# [HASH] — The gate-line check skips the freshest commit while a hash backfill is outstanding

`BORN` matches a commit to its disposition by the hash in a LOG entry's heading. An entry is written before its commit exists, so the heading carries a `[HASH]` placeholder until the next session start backfills it. Run immediately after a close — which is exactly when the close's own step runs it — the check therefore reported the commit just made as carrying no disposition, every single time. The dispositions were there and simply could not be matched yet.

`_rule_bearing_commits` now drops the newest commit while any LOG entry heading still holds the placeholder. Both `BORN` and `CONTRADICTED` read that helper, so one change covers both. A repository with every heading backfilled is checked exactly as before.

Two alternatives stayed refused. Filename-fallback matching reintroduces the misattribution the heading-only rule was written to fix. Running the check before the commit changes what the close's step means, for the same result this gets more cheaply.

Output after the fix is unchanged from the confirmed baseline: 0 of 4 found something, 10 rule-bearing commits since the baseline.

**Files touched:** resources/rule_signals.py, resources/testing/test_rule_signals.py (new)
**Routed to Captures:** none
Rule gate: not needed — a false-positive fix in a dev script; the rule corpus is untouched.
