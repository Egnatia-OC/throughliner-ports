# a216873 — The Codex port deleted, and its queue item's "cheap and reversible" premise found false mid-build

The shelved Codex port was not merely a sibling folder — it was a git worktree of this repository, checked out on branch `codex/si-port`, which is how it kept appearing in `git worktree list` as live work. It had been dormant since 2026-07-28 with `CLAUDE.md` already describing it as read-only history.

**The build halted on something processing had settled wrongly.** The item chose the cheap operation — remove the worktree, drop the branch ref — over rewriting history, and it recorded that the cheap one is also the reversible one, because dropped commits stay in the reflog until garbage collection. That is true of commits. `git status` inside the worktree showed 722 added lines across 24 modified files, plus two untracked files including a research note: work that had never been committed, that no reflog holds, and that removal would destroy with nothing to recover from.

**The first attempt to explain this failed, and the failure is filed as its own item.** The halt was written in the project's own vocabulary — worktree, reflog, commits, branch ref — and Alex said she did not understand it. Restated as "a second working copy of this same project, sitting next to it", with the pending edits described as existing only as loose files on disk, she decided in one turn. That is `[halt-narration-used-unexplained-jargon]`.

**Her decision, in her own words: delete the folder and let those edits go.** She was told plainly first that they could not be recovered.

**The removal needed two attempts for an unrelated reason.** `git worktree remove --force` deregistered the worktree and then failed with a permission error on the folder itself and on the `.git/worktrees` metadata — this project lives inside a synced Drive folder. The branch was deleted separately (tip `59da478`), and the folder and stale metadata were removed with PowerShell.

**What survives and what does not.** The port's commits are unreachable rather than erased, recoverable from the reflog until git collects them. The uncommitted edits are gone. `CLAUDE.md`'s ports section used to point at the folder as the place to look up what an old Codex-side slug meant; that pointer resolved to nothing after this, so the section now says so rather than leaving a dead reference.

**The specimen was preserved before it was destroyed**, which is why this item waited. `[worktree-scan-cannot-classify-branches]` shipped first and wrote the deliberate-worktree example — the branch name, the sibling path, the dormancy — into `resources/research/worktree-isolation-and-desktop-sessions.md`. With the port gone, any worktree appearing here is now unambiguously session-allocated.

**Files touched:** `CLAUDE.md`; git operations (`git worktree remove --force`, `git worktree prune`, `git branch -D codex/si-port`, folder removal)
**Routed to Captures:** `[processing-asserts-reversibility-without-checking]`, `[halt-narration-used-unexplained-jargon]`

Rule gate: not needed — no rule authored or amended; a git operation plus a factual correction to CLAUDE.md's ports section.
