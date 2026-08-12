# [HASH] — Unmerged worktree work detected and offered a merge; the isolated close warns that "remove" deletes it

The failure this addresses is not two sessions colliding — that was cut when the item was reshaped to merge-at-close only. It is a session's work sitting unmerged on a branch nobody is tracking, one prompt away from being deleted by a user who reads "remove" as tidying up. The harness creates a session's worktree and branch and **never merges either back**; its exit prompt's remove option deletes the worktree directory and the branch with everything in them.

**The constraint that inverts the obvious design.** Git refuses to update a branch checked out in another working tree, so an isolated session cannot merge itself into the main line. The merge therefore cannot happen at the isolated close — it is offered at a **main-checkout** session's start.

## What shipped

- **`session_start.py`** — new `_unmerged_session_branches()`, walking `git worktree list --porcelain` and counting `HEAD..<ref>` per linked worktree. Reported in the shared-tree branch only, since only a main checkout can act on it.
- **`done.md` step 6a** — an isolated close names the branch, states plainly that it is not merged, warns that **remove** deletes it (using that word, because it is the word the exit prompt uses), and says where the merge is offered instead.
- **`skill-nonspecific-rules.md`** — the parallel-sessions block's isolated case extended with what happens to the work at close.
- **SPEC.md**, **README.md**, and a **FAQ entry** aimed squarely at a user meeting the keep-or-remove prompt.

## A defect found by smoke-testing, and how it was handled

The scan was run against this repository and returned one hit: **`si-port`, 31 commits ahead** — the shelved Codex port, a deliberate archive that must never be merged. Nothing distinguishes it from a session branch: both are a linked worktree holding unmerged commits.

A name-based test was considered and rejected. It would need Claude Code's worktree naming convention, an external fact nobody has confirmed, and it would fail in both directions — missing branches the harness names differently and catching the user's own feature branches.

**So the hook was reworded to report only what it measured** and to require a judgment before any merge is offered, rather than shipping something that would offer to merge the Codex port every session. That is honest and it is not free: on this repository the line will fire every session about a branch that will never be merged, which is the cry-wolf shape the method fights. Filed as [worktree-scan-cannot-classify-branches] with three candidate fixes and none chosen.

**The isolated case still has never been observed on this machine**, and the item was built knowing that. `git worktree list` shows only the main checkout and the shelved port. This must not be described as solving the remote-start problem until the isolated case is actually seen.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `SPEC.md`, `README.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** [worktree-scan-cannot-classify-branches].

Rule gate: run — one always-loaded amendment, admitted. The parallel-sessions block in `skill-nonspecific-rules.md` gained a paragraph on what happens to an isolated session's work at close. It passes the four-skills test only weakly — the close half fires at /done — but it extends an existing always-loaded block on the same subject rather than opening a new one, and splitting the isolated case across two files is how the two would drift. Recorded as the weaker admission of this run, and a candidate for the eviction pass to revisit alongside [device-access-rule-could-be-fetched]. The `done.md` step and the hook change are procedure, not rules.
FAQ: updated — a new entry on the keep-or-remove prompt, written because a user meeting that prompt with work on the branch is exactly who this protects and exactly who would otherwise pick "remove".
