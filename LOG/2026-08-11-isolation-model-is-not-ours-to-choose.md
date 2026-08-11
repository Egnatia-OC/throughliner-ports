# [HASH] — session_start measures which isolation model is in force, and the parallel-sessions rule states both cases [isolation-model-is-not-ours-to-choose]

Captured by the user, who asked what the branching was for and refused to let Claude design out an intentional design without knowing — which is what produced the research at `resources/research/worktree-isolation-and-desktop-sessions.md`. The detection finding and the design are Claude's.

**The premise changed at processing, and that is the whole item.** The research concluded the method *cannot assume* an isolation model, having observed a session in the main checkout with no worktrees directory and no worktree key in any readable settings file. That conclusion was superseded by a cheaper one: the method does not have to assume, because it can **detect**. In a linked worktree `git rev-parse --git-dir` and `--git-common-dir` differ; in a main checkout they are identical. Two strings, one comparison, no asking the user and no inferring from a missing directory.

**What the detection reports, and what it does not.** It reports the state of *this session*, not the setting. It cannot explain why a session is not isolated when the app documents a new session getting its own worktree, and that discrepancy remains unexplained. It is accepted because the advice consults the current state and never the setting, so knowing the setting would change no behaviour — and because the `[user]` line that would have asked for the setting was deleted for producing an answer nothing consumes.

**The advice inverts between the two cases, and the rule now says both.** Under a shared tree the existing precaution stands: avoid two sessions writing QUEUE.md or committing at the same instant. Under isolation, sessions cannot collide at all, but a capture filed in one never reaches the other and the last branch to merge wins — so queue edits belong in one session until a merge lands.

**One sentence holds under both, for opposite reasons**, which is the absorbed [concurrent-capture-during-next-costs-interruptions] resolved to its one line: don't interrupt a run to file a capture. On a shared tree no coordination is needed and the only moment worth avoiding is /next's close, which rewrites Processed. Under isolation, pausing achieves nothing, because the capture lands in the other session's copy and cannot reach the running build. The live cost that item recorded was the user stopping a run twice to append a capture, then having to re-establish where the run was.

**The reversal is recorded so it is not mistaken for a settled line.** Claude first recommended dropping branching and promoting [worktree-override-hook] as the remote-control fix, then found the documented refusal and reversed. Neither position was reached with the evidence now on file, and the detection finding postdates both.

**An FAQ entry shipped with it rather than being dispositioned away.** What the method tells users about running two sessions at once is user-facing, and a missing FAQ entry in a file list is precisely how the FAQ went stale.

**This item's build instructed two re-processings rather than performing them**, because deciding another item's fate is /plan's with the user present. Written into their prose: [concurrent-session-support] should lose branch creation entirely and keep only merge-at-close for the isolated case, and should drop Finding 2 from its scope since that shipped this run; [worktree-override-hook] is now a probable delete, on the documented refusal of a path resolving into the main checkout.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `FAQ/faq.md`, `FAQ/index.md`, `QUEUE.md`, `SPEC.md`, `README.md`
**Routed to Captures:** none from this item
