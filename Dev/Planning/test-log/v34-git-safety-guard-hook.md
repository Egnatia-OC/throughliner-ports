# V34 — Git safety-guard hook (2026-05-21)

Direct Python invocation — deterministic, zero API cost.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 100 | 2026-05-21 | V34 | Hook denies `git reset --hard` — standalone and chained (`cd foo && git reset --hard`) | `plugin/hooks/pre_tool_use_git_guard.py` (RESET_HARD regex) | Pass | Both variants emit deny JSON with `permissionDecision: "deny"` and clear reason text naming the blocked command + safer alternatives. Regex bug caught pre-ship: `\b` before `--hard` silently passed because both preceding space and leading `-` are non-word characters; fixed by removing the leading `\b`. |
| 101 | 2026-05-21 | V34 | Hook denies `git push --force` and `git push -f` — standalone and chained | `plugin/hooks/pre_tool_use_git_guard.py` (PUSH_FORCE regex) | Pass | Three variants tested: `git push --force origin main`, `git push -f origin main`, chained `git commit -m msg && git push --force origin main`. All denied with correct reason text pointing at `--force-with-lease` as safer alternative. |
| 102 | 2026-05-21 | V34 | Hook allows safe git operations — `git commit`, `git tag`, `git push` (no force), `git push --force-with-lease`, `git reset --soft`, `git push origin v34` | `plugin/hooks/pre_tool_use_git_guard.py` | Pass | Six variants tested. All exit 0 with no stdout (implicit allow). Critical check: `--force-with-lease` is NOT blocked by the `--force` regex — negative lookahead `(?!-with-lease)` works correctly. |
| 103 | 2026-05-21 | V34 | Hook allows non-Bash tool calls and handles edge cases (Edit tool, empty command, malformed JSON) | `plugin/hooks/pre_tool_use_git_guard.py` (early-exit paths) | Pass | Three edge cases tested. All exit 0 with no stdout. Confirms lenient-by-default behaviour: hook only inspects Bash tool calls with non-empty command strings; everything else passes through. |

