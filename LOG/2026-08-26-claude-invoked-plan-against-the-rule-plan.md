# 0d02b6a — Skill self-invocation gets a hook guard, and the real trigger routed out as Claude Code issue #89739

Kept on Claude's recommendation and your agreement, reframed by your account at processing. The transcript was re-read and confirms the incident (typed /plan, Claude tried to start it, red error, retype). Your account changed the diagnosis: the desktop app takes ~15 seconds before /plan is runnable at session start — typed early it lands as plain chat text, possibly colliding with Claude Code's native plan mode; the other four skills are unaffected, only /plan. And you usually can't resist typing it early, so it recurs. Two halves: the method's — a pre_tool_use guard refusing a Skill invocation of the method's own skills with calm guidance, plus the hand-over prohibition hoisted into its own rule; and Claude Code's — a GitHub issue drafted, approved, and posted under your account (anthropics/claude-code#89739, register line written from the approved text). Two search passes found no adjacent issue.

**Queue changes:** kept and cleared, in the build set.
**Work processed:** kept — [claude-invoked-plan-against-the-rule].
**Also:** issue #89739 posted; the planning opening's issue scan watches it.
Rule gate: run — escalation to a hook under the fourth admission question; the prohibition amended, not added; wording-only refused (twice on record, recurring trigger).
