# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top batch and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## What's the difference between Batches and Captures in QUEUE.md?

**Batches** are ready-to-build work — entries under Build/Test subheadings, worked top to bottom. One batch per /next session. **Captures** is an inbox — ideas, questions, and observations from builds or between sessions. Not actionable yet — during /plan, each gets discussed and either promoted, parked, or dropped.

## How are entries organized in the queue?

Batches group entries under **Build** and **Test** subheadings. Build entries create or change things. Test entries verify things work. Not every batch needs a Test section — only when verification isn't self-evident. Captures use inline tags: **[idea]** for unevaluated suggestions, **[question]** for design decisions needing resolution.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. `_build.md` tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Can I edit SPEC.md while doing a build?

No. SPEC.md is read-only during builds to prevent the spec from shifting under active work. Spec issues get noted for /plan. Edit freely during /plan.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. It gets added to Captures as an [idea] entry without derailing current work. Next /plan session picks it up for discussion and routing.

## The queue is empty. Does that mean the project is done?

No — an empty queue is a normal resting state. Run /plan when you have ideas or want to review. The project is done when you say it is.

## What is _build.md? Should I edit it?

A temporary file tracking the active build — what's done, what's left, what changed. Claude manages it; deleted on /done. If it exists at session start, a previous build was interrupted.

## What is REGISTRY.md for?

A list of every component — what files exist and what each does. Claude updates it after every build. You don't need to maintain it.

## What happens if Claude needs to touch something outside the current batch?

Claude stops and asks. It stays within batch scope. If something else needs changing: "I need to edit [file] because [reason]. Add to scope?"

## What does "Parked" mean in the queue?

Items you've decided not to work on now but don't want to lose. During /plan, parking moves an item to the Parked subsection until revisited. Dropping removes it entirely.

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first). `log.md` has full entries for the current release — files touched, reasoning, captures routed. Older entries in `log-v*.md` files. For design rationale, search the log entries.
