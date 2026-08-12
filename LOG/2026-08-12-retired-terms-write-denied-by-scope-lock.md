# e5d169b — resources/retired-terms.md joins the scope-lock's exempt set

The method requires a session that retires a term to append it to `resources/retired-terms.md`. The scope-lock denied that write, because no build item names the file and self-scoping therefore never puts it in `Files:`. It succeeded only by accident of ordering — after the close deletes the working file, which disengages the lock entirely.

`pre_tool_use.py` gains `_is_retired_terms_file`, a sibling of `_is_research_dir`, matched relative to the project root the same way and checked in the same exemption chain.

The reason is structural rather than convenient, and the docstring carries it: **retirement is discovered *during* a build — you find out a term is retired by retiring it — so the path can never appear in a `Files:` list computed from the work items before the build started.** No amount of better self-scoping fixes that. Without the exemption the obligation was satisfiable only in a narrow undocumented window, and a session hitting the denial mid-close was told to ask the user to widen scope, which is a bad trade for a bookkeeping append.

Two alternatives are recorded with why they lost: stating the ordering in `done.md` works but leaves a trap for anyone who reorders the close, and the ordering that currently works is an accident rather than a design; having /next widen `Files:` when a run touches rule-bearing files is more machinery than the problem deserves, and it guesses.

The docstring also records what must **not** be swept in. `SPEC.md` is outside the exempt set too, deliberately and correctly — a build may edit SPEC only by naming it in `Files:`, which is the whole point of the SPEC gate. It is not a second instance of this problem. The grep the item called for was run at /plan and found `retired-terms.md` to be the only close-time write outside the set.

The exemption ships to consumers who will never have the file. Accepted knowingly: a host-only branch inside a shipped hook costs more than an inert path check.

A test case was added to `resources/testing/hook_schema_check.py` and passes. Note the exemption is not live in the installed host yet — this close's own append to `retired-terms.md` went through because the file was listed in the run's `Files:`, not because of the new code.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `resources/testing/hook_schema_check.py`
**Routed to Captures:** none from this item
**Rule gate:** not needed — a hook exemption and its test; no rule in the method's text.
