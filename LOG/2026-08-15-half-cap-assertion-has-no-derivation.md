# 0e62afe — An undefended threshold in the hook suite becomes a printed size, and a defended one gains its derivation

`hook_schema_check.py` asserted the session-start payload stayed under half the 10,000-character hook output cap. The cap is properly grounded — the hooks reference plus `anthropics/claude-code#44086` and `#70460`, which document that past it the harness saves the text to a file and injects a preview plus a path. The half was grounded in nothing: no comment, no measurement, no reference. That was established by looking rather than assumed — the assertion entered at `455082b`, and a search of every LOG entry for headroom reasoning returns two files, one a false match on "half the capture" and the other the session that filed this item.

A bare threshold with no derivation is what this project's own rule bans, and two others have been deleted for it: the rule-corpus ceiling and the 150–200 instruction count. A third inside a test suite is the same defect where nobody looks, and it had already fired once — its parent item existed because the assertion failed.

The hard cap stays. The half becomes a printed size line that asserts nothing: 3,412 of 10,000 characters, 34%, on this project today. That is what was done when the rule-corpus ceiling was removed, and the item's own argument applies — a test suite is exactly where a threshold sits unexamined for months, so a number nobody has to defend beats a defensible-sounding invention.

**Deriving one honestly was attempted and abandoned, recorded so it is not retried blind.** A justified early-warning threshold would need evidence of how the payload grows with project state — held items, waiting mail, worktrees, and now the delivered INBOX bodies this same run added. That evidence does not exist, and manufacturing a figure without it is the bare-number failure with extra steps.

**The separate 2KB check was examined rather than assumed to share its fate**, which the item explicitly required. It asserts the project-state line sits within the first 2KB, and 2KB is the size of the preview a capped payload is replaced by — sourced to the same hooks reference and the same two issues as the cap itself. It is grounded, so it stays, and the derivation is now written beside it.

**Files touched:** `resources/testing/hook_schema_check.py`

**Routed to Captures:** none

Rule gate: run — admitted as an application of the derivation-required rule rather than a new rule; nothing is authored, one undefended threshold is removed and one is documented. **A genuine eviction:** the corpus loses a bare number and gains no rule text. Host-only.

FAQ: not needed — a host-only test suite consumers never run.
