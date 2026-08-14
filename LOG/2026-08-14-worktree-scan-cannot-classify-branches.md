# 78fa417 — The worktree scan now classifies by path instead of reporting a judgment it cannot make

Filed by Claude while smoke-testing the unmerged-worktree scan against this repository. Run here it returned exactly one branch: the shelved Codex port, 31 commits ahead — a deliberate archive that must never be merged. Nothing distinguished it from a stranded session branch, because both are a linked worktree holding unmerged commits.

What shipped originally was honest and not free. The hook reported only what it measured and said outright that this does not establish the branches are session work, requiring a judgment before any merge is offered. On this repository that meant firing every session about a branch that will never be merged — the cry-wolf shape the method fights hardest.

**The external fact the leading candidate waited on is now confirmed.** Claude Code's docs state that a desktop session's worktree is stored at `<project-root>/.claude/worktrees/` by default, and the desktop setting offers exactly two values: that default, or a custom folder. There is no option that disables worktrees. So: a worktree inside the project's `.claude/worktrees/` is session-allocated; one anywhere else is deliberate.

**Which way it fails is why this beats the naming test that was rejected at capture.** Where a user has set a custom worktree location, the path test calls their session worktrees deliberate and stays silent — a missed merge offer. It never does the opposite, because an archive is never inside `.claude/worktrees/`. Identifying a session branch by its *name* fails in both directions: it would miss branches the harness names differently and flag the user's own feature branches. A check that can only under-fire is admissible where one that can over-fire is not.

**The leftover-working-file signal is kept as a second check, not the primary**, and written into the hook's own comments so it is not re-proposed as the main mechanism. A worktree carrying the method's leftover working files is strong evidence a session ran there, but it only reaches worktrees where a session both ran *and* left a file behind, so it cannot carry the classification alone.

**This build recorded the deliberate specimen before it is deleted.** `[delete-codex-port-from-history]` was held behind this item for exactly that reason: the Codex port is the only live example of a deliberate long-lived worktree on this machine. What the deliberate case looks like — the branch name, the sibling-folder path outside the project, the dormancy since 2026-07-28, and what marks it as an archive rather than session work — is now written into the worktree research file, so the example survives the specimen.

Verified live against this repository: the port classifies as deliberate, and the line now says so rather than demanding a judgment. All five suites under `resources/testing/` pass.

Rule gate: not needed — a hook fix and a research-file addition. No rule was authored or amended.

**Files touched:** `plugin/throughliner/hooks/session_start.py` (`_unmerged_session_branches` returns a classification; the report splits into a session-work branch that offers the merge and a deliberate branch that never does), `SPEC.md` (the `session_start` bullet, which said the hook reports only what it measured), `resources/research/worktree-isolation-and-desktop-sessions.md` (the storage-location fact and the specimen description).
**Routed to Captures:** none. Note for planning: `[delete-codex-port-from-history]` sits below the readiness line blocked by this item, and its blocker has now shipped.
