# V34 — 2026-05-21 — Consumer-method git workflow + OPEN-QUESTIONS promotion

**What shipped.** (1) Recommended habits line: "tag and push after every build." Windows `.git/index.lock` contention documented (manual `del` as recovery). (2) Git safety-guard hook (`pre_tool_use_git_guard.py`, Bash matcher) — denies `git reset --hard` and `git push --force`; allows `--force-with-lease` and all other git ops. 14 test cases (5 deny, 9 allow). Regex `\b` bug caught pre-ship. (3) V36 scope created (3 OQ items promoted). (4) Cowork drift cleanup (4 edits, 3 files).

**Decisions.** New file (not `pre_tool_use.py` extension) — different matcher, different concern domain. `--no-optional-locks` not viable (git flag, not Claude Code flag). `/git-discipline` skill deferred. Lock reproduction deferred.

**Pivots.** `\b` before `--flags` fails (space and `-` are both non-word chars) — caught by automated testing. Context compaction mid-session (clean).

**Carried forward.** Stop-hook auto-commit deferred. Lock contention deferred. `git-integration-research.md` consumed.

