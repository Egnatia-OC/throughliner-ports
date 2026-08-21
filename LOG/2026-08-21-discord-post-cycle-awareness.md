# cc33c1e — Discord post drafted: Claude now knows how the work cycle fits together

Walk-through of `[discord-post-cycle-awareness]`, run inside the /next of
2026-08-21 after its seventeen build items. Written as the walk-through happened
rather than reconstructed at the close.

**Step 1 — feature ships. Satisfied before the walk-through began.**
`[cycle-summary-at-every-skill-opening]` shipped 2026-08-12
(`LOG/2026-08-12-cycle-summary-at-every-skill-opening.md`). Verified live rather
than assumed: the work-cycle block is present in the installed host's
`skill-nonspecific-rules.md`, read at this session's opening. Installed host is
1.20.0-test13, well past the shipping commit, so every claim the post makes is
true of the plugin as installed.

**Step 2 — Claude drafts inside 2,000 characters.** Draft produced and shown to
the user in chat. It leaves the machine, so it was shown before anything was
sent, per the standing rule that nothing goes out without the user seeing the
exact wording and giving an explicit yes.

Claude's first draft, superseded at step 3:

> **Claude can now tell you how its own work cycle fits together.**
>
> Throughliner splits work into a loop: you capture an idea, a planning session
> decides its fate, a build session builds it, and a close records what happened.
> Every piece of that was documented. The loop itself was not.
>
> That gap had a cost I can point at. In two consecutive planning sessions,
> Claude assembled the cycle wrong — both times confidently. It reasoned that
> because a planning session sits between an audit's findings and the work that
> fixes them, those findings could never reach a build. That is exactly backwards:
> the planning session is how they get there. The second time, the person using it
> had to explain the same thing again.
>
> The fix was not a longer list of stages. A flat list would not have caught
> either failure, because both were about a loop *closing* — about the edges that
> return work to the start, not the stages themselves. So what ships now names
> those return edges explicitly: an audit edits nothing and files what it finds
> back into the queue; a build that discovers something files it and carries on;
> user-work leaves the loop only when the person has actually done it.
>
> Every session now opens holding that. Claude reads it and never recites it at
> you.
>
> The general point, if it is useful to you elsewhere: documenting every component
> of a process is not the same as documenting the process. The loop is the part a
> model gets wrong, and it is the part nobody writes down, because everyone who
> already understands it cannot see that it is missing.

Character count: 1,704 of 2,000.

**Step 3 — the user rewrote it, and the rewrite is what went out.** This is
mixed authorship and is recorded as mixed. The structure, the framing and the
voice of the posted text are hers: she folded the
documenting-components-is-not-documenting-the-process point into the setup, where
Claude's draft had tacked it on as a closing moral, and she moved the failure
account into the first person — "I had to explain the same things again and
again" — which Claude's draft had rendered in the third person. Claude made four
corrections to her text and composed none of its argument.

**The four corrections, and one flagged and left alone:**

1. **"The fix was just list of stages" → "was not just a list of stages."** The
   substantive one. As written the post said the fix *was* a list of stages, and
   the next sentence said a flat list would not have caught the failures — a
   contradiction in consecutive sentences. Flagged to her rather than silently
   assumed, since it was her sentence.
2. **The filename removed.** Her draft named `skill-nonspecific-behaviours.md`;
   the file is `skill-nonspecific-rules.md`. Rather than correct it, Claude
   replaced it with "the rules every session loads" — a reader outside this
   project has no such file and no way to look at it, so naming it is both wrong
   and useless to them. This is the shipped audience rule applied to an outbound
   artifact: internal procedure-doc filenames do not belong in text a consumer
   reads.
3. "the skill work together" → "the skills work together".
4. "This only continued until finally, a section was added…" smoothed into one
   clause.

**Flagged and left to her, and she kept it:** "Claude reads it and actually knows
where it is in the work cycle" claims more than the rest of the post supports.
What is demonstrable is that every session opens holding the instruction; whether
it *knows* is precisely what the two failures showed cannot be assumed. Recorded
because the project's standing posture is not to over-claim, and this is a live
instance of that judgment being put to the user and answered.

**Steps 4 and 5 — posted and confirmed, 2026-08-21.** The posted text, 1,290
characters of 2,000:

> **Claude can now tell you how its own work cycle fits together.**
>
> **Throughliner splits work into a loop:** you capture an idea, a planning
> session decides its fate, a build session builds it, and a close records what
> happened. Every such piece was documented. But because documenting every
> component of a process is not the same as documenting the process itself, the
> loop the skills essentially inhabit was invisible.
>
> In two consecutive planning sessions, Claude assembled the cycle wrong — both
> times confidently, and I had to explain the same things about how the skills
> work together again and again. That continued until a section describing that
> higher-level orchestration was finally added to the rules every session loads,
> filling the gap.
>
> The fix was not just a list of stages. A flat list would not have caught the
> relevant failures, as the skills have edges that return work to the start. What
> ships now names those return edges explicitly: an audit edits nothing and files
> what it finds back into the queue; a build that discovers something files it
> and carries on; user-work leaves the loop only when the person has actually
> done it... and so on.
>
> Every session now opens holding this essential instruction. Claude reads it and
> actually knows where it is in the work cycle.

Its line is in `INBOX/sent.md`, written in the same turn as the send.

**Consequence for the queue, for the close to act on.** This item is complete —
walked to its end this session and confirmed posted by the user — so the close
removes it from Processed. `[competition-comparison-article]` names this item as
its blocker and therefore lifts.
