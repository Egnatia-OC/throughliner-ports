# 2c76e53 — Self-invocation of the method's own skills now refused by the hook, with the early-typing trigger named

A planning session in the AFK-cats project opened by saying "Rules loaded. Starting
the planning run", tried to run the skill itself, and failed. Its next message told
the user the skill couldn't be started from Claude's side and asked them to type it
again. The user's first experience of that session was a red error followed by
being asked to repeat what they had just done.

The always-loaded rules named this failure precisely, and the session had read
them in the same breath. That is what moved it to a hook: the gate's fourth
admission question asks whether a hook could do the job instead, and it escalates
where the failure is mechanical, recurs, and its cost lands on the user rather than
on the run. All three hold. Twice on record, and your account at planning is that
it will keep happening — the desktop app takes around fifteen seconds before /plan
is runnable, and typed before then the command lands in chat as plain text, which
you usually can't resist doing.

So the refusal message does two things. It says the command is yours to type, and
it names the likely trigger: if what you typed arrived as chat text, the command
probably hadn't registered yet, so wait a few seconds and type it again. A refusal
that only says no would send you looking for a fault that isn't there.

**The guards matter as much as the gate.** It fires on the method's five skills and
nothing else: another plugin's `plan` passes even when the name collides, a bare
`plan` outside an adopted project passes, and malformed input can't crash the hook.
The prefixed form fires even in an unadopted folder, because that is where
/setup's own instance of this failure happens.

The doc half hoists the prohibition out of an aside inside a bullet about running
commands generally, into its own rule stating the action.

**Files touched:**
`plugin/throughliner/hooks/pre_tool_use.py` — `METHOD_SKILLS` constant and a
Skill-invocation deny gate.
`plugin/throughliner/docs/skill-nonspecific-rules.md` — hand-over prohibition
hoisted into its own action-stating rule.
`resources/testing/test_pre_tool_use_skill_invocation.py` — new suite, 19 cases.

**Routed to Captures:** none.

Tick form: done, confirmed — 19 cases passing, every one driving the hook code
directly. That last point is not incidental: invoking a live skill to watch the
guard refuse it would have exercised the installed host, which is the old code, so
the guard would not have fired and the invocation would have gone through for real.
This project has already destroyed a committed session record that way.

Rule gate: run — escalation to a hook under the gate's fourth admission question,
and the hand-over prohibition amended into its own rule statement rather than a new
rule added. Leaving it wording-only was refused at planning: twice on record
already.

The upstream cause is Claude Code's and was routed out as a GitHub issue in an
earlier session (anthropics/claude-code #89739). This item is the method's half:
however the bare text arrives, the response is a calm hand-back.
