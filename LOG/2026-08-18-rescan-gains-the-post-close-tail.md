# 02ec308 — /rescan widens to the post-close tail, and the delta close it replaces is deleted as already decided against

The user asked for a lightweight way to bank post-close work without typing the whole request each time. Her first framing was a "done delta" already sitting in the queue from 2026-08-01.

**That one was checked and deleted, because `done.md` refuses both its options by name.** A second lightweight close over the tail "is another commit wearing a different name, and it needs the user to decide when the tail has ended, which nothing can tell them" — landed 2026-08-15 with the one-commit-per-session decision, two weeks after the item was captured. Her alternative, a post-close nag, is the same refusal. The catching she wanted already happens on the record side; what it does not do is commit. This session's own opening was evidence for the mechanism rather than against it: the 31 uncommitted files were exactly the documented signature.

**Her second framing survives both refusals, and it is a different thing.** No commit, and nothing has to judge when the tail ended, because it can be run as many times as the tail has parts. `/rescan` is already user-invoked, repeatable, and commits nothing — and `rescan.md` names `LOG/` exactly once, only to place a capture. So a conversation's *decisions* have a one-word route and post-close *work* has none.

The widening routes what `/rescan` finds by the triage the always-loaded rules already carry: work to do becomes a capture, what happened becomes a marked tail on this session's record. Its stated boundary is untouched — it files, and never decides a fate.

**Queue changes:** [rescan-appends-post-close-work] filed and cleared; [done-delta-close] deleted, oldest item in the section.
**Work processed:** kept — [rescan-appends-post-close-work]. Deleted — [done-delta-close].
