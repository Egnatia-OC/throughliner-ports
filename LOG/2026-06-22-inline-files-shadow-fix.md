# ec7ce6f — pre_tool_use.py `_parse_build_files` hardened so a stray inline `Files:` line can't shadow the structured section; next.md template drops inline `Files:` from the Entry field

The scope-lock parser bound to the *first* line starting with `Files:`. When `/next` copied a batch's entry text into `_build.md` and that text carried a stray inline `Files: a, b, c` line, the parser latched onto it, found no bare-path bullets beneath, broke at the next prose line, and returned an empty list — which read as "method docs only" and denied the build edits to its own listed files. Traced live against the 2026-06-20 `/next` build of [plan-close-dep-check].

Fixed in two layers, matching the spec-edit guard's shape (a mechanical guard plus an authoring tidy-up at the source). The load-bearing fix rewrites `_parse_build_files`: every `Files:` line now contributes and the scan never stops at the first — a non-bullet line ends only the current bullet run, not the whole scan, so a structured `Files:` section further down is still read. A content-bearing `Files: a, b, c` line is no longer ignored either; its comma-separated paths are taken directly, so even an inline-only line yields a non-empty scoped list (lock on) rather than None (lock off). This is the fail-safe of the two candidates the batch named: a malformed file can never silently turn enforcement off, and over-collecting is safe because an extra path only widens the allow-list to a file the build named anyway. The authoring tidy-up: next.md's Step 2 template now drops any line starting with `Files:` from the Entry field and carries a one-line caution that the structured `Files:` section is the only list the lock reads.

Run-now test (in-session module import) passed five cases: inline-shadow returns the structured paths not `[]`; a normal section parses; an inline-only line yields a scoped list not None; no `Files:` returns None; an empty bare header returns `[]` (method docs only).

**Files touched:**
- plugin/si-plugin/hooks/pre_tool_use.py — rewrote `_parse_build_files` (accumulate across all `Files:` lines; parse inline comma paths; never stop at the first; expanded docstring).
- plugin/si-plugin/docs/next.md — Step 2 `_build.md` template: Entry field drops any `Files:`-leading line; caution added at the `Files:` template.

**Routed to Captures:** none
