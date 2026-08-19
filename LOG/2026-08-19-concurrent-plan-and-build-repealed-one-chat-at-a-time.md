# cb50e2b — a plan session alongside a build run: the one-chat-at-a-time rule repealed, on the ground that a run currently blocks ideation outright

Split out of the build-view design as its own item, because the single-writer file split is buildable on its own and the session mechanics are not.

The case is the user's and it inverted Claude's reading of it. Claude had warned that switching sessions to hold a thought would cost her context and lose ideas, and treated concurrency as a second-order optimisation to hold behind the real fix. Her answer defeated that: she already switches every minute or so because of wait times, today between whole *projects*, losing the context each time — so switching within one project is a straight win rather than a cost. Her second point is sharper and is now the item's spine. A semi-autonomous run occupies the only session there is, so for as long as it runs she cannot capture anything. SPEC's first principle says the user must be able to ideate at any point in the build cycle, and that is therefore false today. Concurrency is not an enhancement to the split; it is what makes a shipped principle true.

That reframe changed the design rather than only the ordering. The build view stops being the goal and becomes the enabler, which means the write-direction rule — planning writes the full queue, a build never does — has to be built into the first item from the start rather than retrofitted here.

What this repeals is on the record and the repeal is written as one. The always-loaded rule bars working on a project from more than one chat, because a capture filed in one is invisible to the other and the two disagree about the queue from the moment either writes. The build view answers exactly that: one writer, and a view regenerated rather than merged. The old objection does not reach this shape — but it was settled after the arrangement "fell over every time it was tried", so the item names what changed rather than quietly dropping the rule.

What is still to design is the whole of the item, and it is deliberately not designed here. Two sessions committing to one working tree is a git problem no file split touches. The plumbing exists — `session_start` already detects worktrees, reports commits a checkout does not have, and offers the merge back — so the choice is whether a build runs in its own worktree or both share the tree with a single committer. Then the shipped-slug cleanup at the next planning opening, and the guard against resurrecting finished work, which rests on status being re-derived from LOG.

Its gate disposition is deliberately deferred: the repeal is decided, but the rule text waits on the git question, so it is authored when this is next processed rather than at the build. That is the /plan-sited gate applied to itself — a build cannot refuse, so a build must not be the first party to write the rule.

**Queue changes:** [concurrent-plan-and-build-sessions] filed and placed below the readiness line, blocked by [split-the-cleared-region-for-concurrent-sessions].

**Work processed:** kept — [concurrent-plan-and-build-sessions], held.
