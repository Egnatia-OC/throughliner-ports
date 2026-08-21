# cc33c1e — Feedback about a behaviour the method produced stops going to memory, where it was silently buying one user a fix and leaving every consumer the bug

**Why this was worth doing.** The user raised it at a close: if Claude's replies are
affected by memory, then the method cannot truly be tested. The shipped rule did not see
the conflict. The memory-boundaries rule listed what memory is free for — user
preferences, working style, **communication feedback**, cross-project facts — while this
project's `CLAUDE.md` holds that all use of the plugin to develop the plugin is testing
it, and that any moment session memory covers for something the docs should carry is a
mandatory capture. Nobody had applied that second rule to *persistent* memory, and the
two disagreed.

**Why it is sharper than a self-hosting quirk.** Communication feedback is very often
evidence about the method's own narration rules. The session that raised it demonstrated
exactly that: the user twice said there was too much text, which is evidence that a
/plan checkpoint is too long. Had that gone to memory instead, Claude would simply have
behaved better, the queue item would have stopped mattering, and the defect would have
survived in the shipped docs. Memory would quietly buy a fix for one user while every
consumer kept the bug.

**So the routing test is not "is this a preference?" but "is this evidence about the
method?"** The overlap is the problem: such feedback is genuinely both, and the old rule
named only the branch that silences it.

**The scope went the opposite way to the one the item proposed, on the user's
decision.** The entry asked whether the exception should be scoped to projects testing
the method. She said general. A consumer's complaint that Claude narrated badly is
evidence about the method too, and it is the *only* such signal originating outside this
project — routed to memory it makes their Claude quieter and tells the method's author
nothing. Scoping to self-hosting would have protected the one project that already has
other ways of noticing, and left every other project silently absorbing the evidence.

**What was built, and it needed no new machinery.** The three-way discriminator already
routes "the method is misbehaving" to the feedback channel and "my app" to the queue;
the memory-boundaries rule simply never cross-referenced it. The bare term `communication
feedback` comes off memory's list and is replaced by two subordinate qualifications:
feedback about a behaviour the METHOD produced routes by the discriminator, and a
preference no method rule governs — a name, a timezone, a tool the user likes — stays
memory's. `grep "communication feedback"` in the file returns nothing.

**One stale pointer corrected rather than left for the build to discover:** the file
named when this was captured, `plugin-behaviour.md`, was retired 2026-08-10 and the rule
moved.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`,
`plugin/throughliner/templates/faq-template.md`,
`plugin/throughliner/templates/faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none from this item.

**FAQ: updated** — new entry, "I complained about how Claude was talking to me, and now
it wants to send a report. Why?" It fires because what the user *does* changes: feedback
that used to be absorbed silently now becomes a report they are asked to approve and
send. Written for an external non-coder; a first draft named this project's own user as
an example and was corrected before the copy into `FAQ/`.

Rule gate: run — admitted as a qualification on the existing memory-boundaries rule, subordinate rather than freestanding, so no always-loaded slot is spent. **The eviction is the bare `communication feedback` entry on memory's list**, which is what made the two rules disagree. Failure evidence is one recorded instance here plus the structural argument that the affected signal is the only external evidence the method receives.

Depth: short. Built and confirmed.
