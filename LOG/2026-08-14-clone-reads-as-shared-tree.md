# 78fa417 — The isolation check gains a third case: a cloud session runs on a clone, and was being told collisions are handled

Filed by Claude from the user's screenshot of a cloud session's initialization steps. A Claude Code cloud session — started from the mobile or web app against the GitHub repository — reports its startup as: set up a cloud container, **cloned repository**, run setup script, started Claude Code. No worktree. It works on a clone inside a container, and its work reaches this machine only as a pushed branch.

The defect followed from a two-way test on a three-way world. `session_start` decided the isolation model by comparing `git rev-parse --git-dir` against `--git-common-dir`: they differ in a linked worktree and match in a main checkout. **In a clone they also match, because a clone is a main checkout.** So a cloud session was classified as a shared tree and given the shared-tree advice — that two appends to different parts of QUEUE.md do not collide and the file-modified warning catches it if they do. Both halves are false there.

**This is worse than the worktree case rather than equivalent, which is what made it worth fixing rather than noting.** The worktree branch of the advice at least describes isolation, so a session reading it is warned that a capture will not reach the other side. A clone got the one branch that actively misleads.

**The detection method was measured, not reasoned about.** A live cloud session was asked to report its git layout and environment. Both git paths resolved to the same `.git`, confirming an ordinary clone. The environment carries the discriminator: `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE` (observed as `cloud_def…`), alongside `CLAUDE_CODE_ENTRYPOINT=remote_mobile` and `IS_SANDBOX=yes`. The container was `sandbox-ccr-default`, running Claude Code 2.1.42, entered from mobile.

**`IS_SANDBOX` was weighed and rejected as the signal.** It describes sandboxing generally rather than this environment, and a false positive would hand an ordinary session the wrong branch of the advice — which is the exact failure being fixed, in the other direction.

**Absence means "not cloud", deliberately.** These variable names are undocumented, so a rename is a live risk. Written this way, a rename loses the improvement and the check falls back to today's behaviour; written the other way, it would produce a confident wrong answer. The asymmetry is the whole reason for the ordering.

The advice table gained a third branch rather than a reworded second one, because the clone case says something the other two do not: work reaches the main machine only as a pushed branch, and a capture filed there is invisible everywhere else until that branch merges.

Verified live: with the variable set, the clone branch fires; without it, the session correctly reports a shared tree. All five suites under `resources/testing/` pass.

Rule gate: not needed — a hook fix plus one branch added to an existing advice table. No rule was authored or amended.

**Files touched:** `plugin/throughliner/hooks/session_start.py` (`_isolation_model` and its report), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the parallel-sessions advice table), `SPEC.md` (the `session_start` bullet), `resources/research/worktree-isolation-and-desktop-sessions.md` (a new section on the clone case, since it read as though worktrees were the only isolation mechanism).
**Routed to Captures:** none
