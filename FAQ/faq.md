# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top batch and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## What's the difference between Batches and Captures in QUEUE.md?

**Batches** are ready-to-build work — entries under Build/Test subheadings, worked top to bottom. One batch per /next session. **Captures** is an inbox — ideas, questions, and observations from builds or between sessions. Not actionable yet — during /plan, each gets discussed and either promoted, parked, or dropped.

## How are entries organized in the queue?

Batches group entries under **Build**, **Test**, and **Audit** subheadings. Build entries create or change things. Test entries verify things work. Audit entries review what exists and route findings back into the queue. Not every batch needs a Test section — only when verification isn't self-evident. Captures are plain bullets — each carries its own reasoning inline.

## What is the Red flags section at the top of QUEUE.md?

It's where Claude lists security and privacy risks it has spotted — anything that could expose your data or your users' data, or amount to a breach. It sits at the very top of the queue so it's the first thing you see each session; a risk you should know about shouldn't be buried. The section stays empty until something comes up.

Each red flag carries one of three states:

- **Open** — the risk has been raised but not yet dealt with.
- **Resolved** — the risk has been fixed or designed out; the work no longer carries it.
- **Accepted** — you were told the risk plainly and chose to go ahead anyway. That choice is written into the session log: what you were warned about, and that you agreed to proceed. It's a clear record if the risk ever matters later.

Claude raises and updates these — you don't maintain the section. Accepting a risk is a decision only you can make.

## What is the "Deferred tests" section in QUEUE.md?

A waiting list for tests that couldn't run in the session that planned them — some only become checkable later, some need you to try something, some wait on an outside event. When /done closes a session and a planned test couldn't run, it adds a one-line entry here: which batch the test came from, what to verify, and what confirms it. /plan reads this list each session and folds the ones that can now run into a test batch; and when a later session happens to confirm one along the way, /done removes its line and records the result in the session log. Claude writes and clears this section — you don't maintain it.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. `_build.md` tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Is it safe to clear the conversation or start a new session between steps?

After /done, yes — everything is recorded in the session log and committed, so a fresh conversation loses nothing. Before /done, the plugin can still recover: it reads its working file (`_build.md` or `_plan.md`) rather than relying on the conversation, so an interrupted build or planning session picks up from the file. But closing with /done first is the clean habit — it's the moment the work becomes a permanent record instead of something the plugin has to reconstruct.

## Can I edit SPEC.md while doing a build?

Not during an ordinary build. SPEC.md is your project's source of truth, so it's kept from shifting under active work — the safety check blocks a build from editing any file its batch doesn't list, and ordinary builds don't list SPEC.md. Changing SPEC takes a planned spec-edit batch: /plan queues it, and /next runs it like any other build. So if you spot a spec issue mid-build, note it for /plan, which turns it into a spec-edit batch.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. It gets added to Captures without derailing current work. Next /plan session picks it up for discussion and routing.

## The queue is empty. Does that mean the project is done?

No — an empty queue is a normal resting state. Run /plan when you have ideas or want to review. The project is done when you say it is.

## What is _build.md? Should I edit it?

The active build's working file. It does four jobs: carries the batch being built (so QUEUE.md stays free while the build runs), lists which files the build may change (the plugin's safety check blocks edits to anything else), ticks off finished steps (so an interrupted session can resume without redoing work), and keeps the batch's reasoning (so /done can write the session record). Claude manages it — don't edit it. Deleted when /done closes the session; if it exists at session start, a previous build was interrupted and /next will offer to resume.

## What is _plan.md? Should I edit it?

A planning session's working file — the planning counterpart to _build.md. When /plan starts working through your captures, it creates `_plan.md` to track where it is: which items it's processing, the current one, and what it has routed so far (promoted, parked, or dropped). It does three jobs: it survives a cleared or compacted conversation, it lets an interrupted /plan pick up where it stopped, and it gives /done a record of what was decided. Claude manages it — don't edit it. /done deletes it when the planning session closes; if it exists at session start, a previous /plan was interrupted and you can resume with /plan.

## What if my project already has planning docs from another tool or an older version?

/setup handles it as a migration. When it sees your folder has content but none of the method's own docs yet, it treats your existing planning or spec documents as a starting point rather than assuming a blank slate. With your help, it maps that content into the method's docs (SPEC.md, QUEUE.md, and the LOG folder), keeping them at the top level of your project. Before renaming anything, it checks that each old doc actually fits the method doc it's mapped to — and if something doesn't fit, it asks you rather than guessing. It won't blindly rename or overwrite your existing files.

## What happens if Claude needs to touch something outside the current batch?

Claude stops and asks. It stays within batch scope. If something else needs changing: "I need to edit [file] because [reason]. Add to scope?"

## What does it mean when work sits below the "cleared to run" line?

It means one thing only: **another named item in your queue has to happen first.** There is no general "parked" or "set aside" state — the Parked subsection this question used to describe no longer exists.

A held item carries a line reading `Blocked by:` followed by the blocking item's name in square brackets. Claude checks that the name refers to a real item in your queue, so it can't quietly point at nothing.

If work is waiting on something in the *world* rather than on other work — a restart, a website going live, someone getting back to you — that thing doesn't get written as a note inside the held item. It gets filed as **its own item in your queue**, so it comes up in planning and actually gets done, and the held item names it. That change came from a real failure: a step buried as a sentence inside another item sat unnoticed for weeks, because a sentence inside someone else's item is invisible as work.

At the start of every planning session Claude asks one question per held item — has its blocker shipped? — and offers to move up the ones whose blockers have. It doesn't ask you anything, because the answer is in the record.

If nothing in the queue blocks a piece of work, it doesn't belong below the line at all — it goes above it, ready to build.

## What is the "freeform" tag on a piece of work?

It marks work that Claude must **not** run with /next — work you and Claude do by hand together, in a session of its own.

Most of the time that distinction wouldn't matter. It matters when the work being fixed is part of the machinery /next itself relies on — the thing that moves items around your queue, the safety check on which files can be edited, the check that keeps your queue's formatting valid. Using a broken mechanism to repair itself is exactly how a repair goes wrong, so the tag stops /next from trying.

You'll see it as `[freeform]` at the front of a work item's line. Claude places these at one end of your ready work, never in the middle: first if the fix has to land before anything else, last if it's unrelated, so a run finishes everything it can before stopping. When /next reaches one it says plainly what the item is and stops rather than skipping past it, and when a session closes with one waiting, it tells you so you don't run /next into a stop.

Either of you can ask for the tag. It's usually the right call for a stopgap, or for something too tangled to fix in small steps.

*(This replaces the old `/next freeform` command, which no longer exists. Freeform is now a label on a piece of work rather than a way of starting /next.)*

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first), and each line ends with the name of that session's full entry file. The entry file holds the detail — files touched, reasoning, captures routed. For design rationale, search the index, then open the named file.
