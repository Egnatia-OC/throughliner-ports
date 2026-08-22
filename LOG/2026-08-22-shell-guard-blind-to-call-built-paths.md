# 2625fa0 — Kept and cleared: the write guard learns to see call-built paths, one nesting level, computed by construction

Design settled at processing: one additional regex for the computed-target check only, tolerating exactly one level of nested parentheses in the `open(` argument — enough for `os.path.join(...)` forms — with anything it matches computed by construction, since a call argument is never a quoted literal. A doubly-nested call still escapes and the docstring states that limit. The `.+?` widening stays refused as matching across unrelated arguments.

Rule gate: not needed — hook code fix, no method rule text.

**Work processed:** kept — [shell-guard-blind-to-call-built-paths].
