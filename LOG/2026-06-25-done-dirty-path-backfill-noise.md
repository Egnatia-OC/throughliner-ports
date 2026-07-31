# 3a12926 — [done-dirty-path-backfill-noise] /done recognises the expected hash-backfill LOG files instead of re-investigating them

Built in the goal run (fourth of four). Every /done's out-of-scope dirty-path check finds the LOG files the session-start hook auto-edited — filling the previous session's placeholder hash with the real commit hash, in the entry heading and the index line. These appear every single session after a /done and the answer is always the same ("it's the backfill, stage it"), but the check didn't recognise them, so it investigated and explained them every time for zero decision value. Per the escalation heuristic this is a sharpen-the-rule case (mild delay, not a high-cost failure), so it's a behavioural change to done.md, not a hook.

Added backfill-signature recognition to the commit core's out-of-scope dirty-path step (done.md): a dirty LOG path whose only change is a placeholder hash becoming a real commit hash, in an entry heading or the start of an index line, is the session-start hook's automatic backfill — which the hook also announces in its opening housekeeping line, so the dirty path is already accounted for. The step now folds it into the commit with at most a one-line note and skips the git-diff investigation and per-file explanation, while keeping the full investigate-and-surface treatment for any other out-of-scope dirty path. The why is carried in the doc: it's expected every session, so re-investigating it each time is pure delay. No FAQ (reduces noise, adds no new concept); the live behaviour is a deferred test ([done-dirty-path-backfill-noise], host-side, observed after reinstall).

**Files touched:**
- plugin/si-plugin/docs/done.md — commit core step 2 (out-of-scope dirty-path detection) gains backfill-signature recognition

**Routed to Captures:** none
