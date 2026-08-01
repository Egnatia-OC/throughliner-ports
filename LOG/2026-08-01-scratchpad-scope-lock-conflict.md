# ea272f6 — Whitelist the session scratchpad in the scope-lock so builds can write scratch files there

The pre_tool_use scope-lock denied writes outside _build.md's `Files:` list — including the session scratchpad directory — while plugin-behaviour.md's Temporary-files rule actively routes scratch scripts and working files *to* the scratchpad. The two rules contradicted, forcing a build to pipe scratch scripts through `python` via stdin to avoid writing a file (observed during [log-file-sort-heuristic]).

Fix: pre_tool_use.py gained `_is_scratchpad_dir(filepath, cwd)`, an exemption alongside the method-docs / memory / research exemptions. It matches by path *shape*, not a hardcoded machine path, so it holds for every consumer: three conditions must all hold — a `scratchpad` path segment, a `claude` segment above it (the harness scratchpad sits at `<temp>/claude/<slug>/<session-id>/scratchpad/…`), and the path being outside the project repo. Requiring all three keeps the whitelist tight — an in-repo `scratchpad/` folder stays under the normal scope-lock. Verified against this session's real scratchpad path plus in-repo and SPEC negatives.

Host-side (a hook change; live after rezip + reinstall). No FAQ — internal scope-lock behaviour a consumer never sees. A one-line exemption note was added to plugin-behaviour.md's Scope and Temporary-files sections so the docs match the hook.

**Files touched:**
- plugin/si-plugin/hooks/pre_tool_use.py — added `_is_scratchpad_dir` helper + wired it into the Edit/Write enforcement block; updated module docstring
- plugin/si-plugin/docs/plugin-behaviour.md — one-line notes in Temporary-files and Scope

**Routed to Captures:** none
