# d5378c7 — CLAUDE.md's worktree claim corrected (this folder is main), the merged queue-redesign worktree deregistered, and the worktree list recorded in the file map

CLAUDE.md's folder-move recovery instructions claimed "this is the queue-redesign worktree"; `git worktree list` reports this folder as main, so anyone repairing a folder move by those steps would have repointed the wrong links. Rewrote the recovery step from the correct vantage (main tree plus one linked worktree, the Codex port) and recorded the worktree list after the "Where things live" map. AGENTS.md's copy of the wrong sentence went with that file's gutting in the sibling item, as its blocker note predicted.

The merged queue-redesign worktree was deregistered from git. The mechanics are worth recording: `git worktree remove` failed validation because the orphaned folder's `.git` file points at the repo's pre-move path (old user profile), and `git worktree prune` kept the entry because the folder's `.git` file still exists. The safe equivalent was deleting the admin entry `.git/worktrees/No-code-method-x` directly — after re-verifying `git log main..queue-redesign` is empty, so nothing on that branch is unreachable from main. The `queue-redesign` branch ref itself remains.

Two things deliberately not done, left for the user: deleting the leftover folder on disk under the old profile (a prior attempt was defeated by an OS lock, per the LOG of 2026-07-30), and deleting `origin/queue-redesign` on the remote — a remote-state change that is in scope for the history-rewrite's branch-coverage decision, so it should be made there, not overnight.

Built in the overnight blitz of 2026-08-05 (autonomous run, approvals deferred — recorded departure).

**Files touched:** CLAUDE.md (recovery section, worktree list), .git/worktrees/No-code-method-x (deleted, untracked git metadata)
**Routed to Captures:** none
FAQ: not needed because the change is host-only — consumers never see this repo's worktrees.
