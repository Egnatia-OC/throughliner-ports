# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes so nothing gets mixed up. **/plan** is for thinking — managing the queue, processing captured ideas, resolving design questions. **/next** is for doing — it picks the top batch from the queue and builds it. **/done** is for closing — it records what happened, runs tests, updates docs, and commits. You always move through them in that order: plan what to do, do it, close it out.

## What's the difference between Batches and Captures in QUEUE.md?

**Batches** are ready-to-build work — organized groups of type-marked entries, worked top to bottom. Each batch is one /next session. **Captures** is an inbox — ideas, questions, and observations jotted down during builds or between sessions. Captures aren't actionable yet. During the next /plan session, each captured item gets discussed and either promoted into a batch, parked for later, or dropped.

## What are the type markers — [build], [test], [idea], [question]?

They tell Claude what kind of work an entry represents. **[build]** means create or change something — edit files, add features, fix things. **[test]** means verify something works — read code, run commands, or ask the user to check. **[idea]** is a suggestion or observation that hasn't been evaluated yet. **[question]** is a design decision that needs resolving before it can become work. Ideas and questions live in Captures until /plan processes them.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. When a build starts, Claude creates a file called `_build.md` that tracks what's been done and what's left. When you reopen the app, the session-start message will tell you there's an unfinished build. Run /next and Claude will read _build.md and offer to resume where it left off.

## Can I edit SPEC.md while doing a build?

No. SPEC.md is read-only during builds (/next). This prevents the spec from shifting under a build that was planned against the old version. If Claude spots a spec issue mid-build, it notes it for the next /plan session. You can edit SPEC.md freely during /plan.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. If you're mid-build, Claude will add it to the Captures section of QUEUE.md as an [idea] entry. It won't act on it or derail the current work — it just records it. The next time you run /plan, the idea gets picked up, discussed, and routed.

## The queue is empty. Does that mean the project is done?

Not necessarily. An empty queue just means there's no planned work right now. It's a normal resting state. Run /plan when you have new ideas, or when you want to review the project and see what's next. The project is done when you say it is — an empty queue is a pause, not an ending.

## What is _build.md? Should I edit it?

`_build.md` is a temporary file that exists only while a build is in progress. It tracks which batch is being built, what's been completed, and what changed. Claude manages it — you don't need to edit it. It gets deleted automatically when you run /done. If it exists when you start a new session, that means a previous build was interrupted.

## What is REGISTRY.md for?

REGISTRY.md is a list of every component in your project — what files exist and what each one does. Claude updates it after every build (during /done). It helps Claude find things quickly without searching through code. You don't need to maintain it yourself.

## What happens if Claude needs to touch something outside the current batch?

Claude will stop and ask. The batch entries describe the work — Claude stays within that scope. If it discovers something else needs changing, it will say "I need to also edit [file] because [reason]. Add to scope?" and wait for your answer.

## What does "Parked" mean in the queue?

Parked items are ideas or questions you've decided not to work on right now, but don't want to lose. During /plan, when you're processing a captured item, one option is to park it — it moves to the Parked subsection where it stays until you revisit it. Parking is different from dropping: dropped items are removed entirely, parked items are preserved.

## How do I know what was done in a previous session?

Check the LOG/ folder. `LOG/index.md` has one-line summaries of every session with commit hashes. `LOG/log.md` has the full entries — what was built or planned, which files were touched, test results, the reasoning behind the work, and anything routed to Captures. If you want to know why a design choice was made, search the log entries — every entry records why the work was done and the approach taken.
