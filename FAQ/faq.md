# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top batch and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## What's the difference between Batches and Captures in QUEUE.md?

**Batches** are ready-to-build work — entries under Build/Test subheadings, worked top to bottom. One batch per /next session. **Captures** is an inbox — ideas, questions, and observations from builds or between sessions. Not actionable yet — during /plan, each gets discussed and either promoted, parked, or dropped.

## How are entries organized in the queue?

Batches group entries under **Build**, **Test**, and **Audit** subheadings. Build entries create or change things. Test entries verify things work. Audit entries review what exists and route findings back into the queue. Not every batch needs a Test section — only when verification isn't self-evident. Captures are plain bullets — each carries its own reasoning inline.

## What is `/next freeform`?

A fourth kind of /next session, for work that isn't a build, a test, or an audit — an ad-hoc change, talking through edits you've already made, or surfacing something without the pressure of sorting it out right away. Reach for it when none of the other three fit. It keeps the safety rails — Claude still asks before touching a file, and still flags risks — but drops the fixed step list, so it suits work that doesn't know its shape up front. One thing it won't do: process your captures. A freeform session can jot ideas into Captures, but promoting, parking, or dropping them is /plan's job — Claude will say so and offer to move to /plan when captures pile up.

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

## What does "Parked" mean in the queue?

Items you've decided not to work on now but don't want to lose. During /plan, parking moves an item to the Parked subsection until revisited. Dropping removes it entirely.

Parked items carry one of two reason lines that signal whether they come back automatically:

- `Blocked by: [slug] + condition` — a trigger exists. When the named item ships or the condition fires, Claude offers to unpark it during the next /plan or /next.
- `Parked: short reason` — no trigger. The item stays parked until you bring it up; Claude won't auto-surface it.

Nothing leaves active flow without one of these — prose alone isn't enough for Claude to track it mechanically.

## What does a "Plan session here" line in the queue mean?

It's a planning checkpoint Claude placed between batches. When /next reaches it, /next stops and tells you a planning session is needed first, naming the reason — usually because the next work depends on a decision, or on findings that only get sorted out in /plan. Run /plan: it handles the named reason and removes the line, and then /next can carry on. You don't add these yourself — Claude places them when it sees a planning moment coming.

## I told Claude "not now" about something. Why did it stop coming up — and will it come back?

When you set something aside — you stop partway through a step, tell Claude to shelve a suggestion, or answer "no change" about something the work was waiting on — Claude records that on the item itself, quoting your words and noting how far things got. From then on it stops re-offering that item in its recommendations and check-ins, so you're not asked the same thing every session. Two guarantees keep this safe. Nothing is lost: the work stays exactly where it is in your queue, and it comes back up on its own when the queue has nothing else left to offer — or the moment you mention it yourself. And warnings never go quiet: a security concern or an unaddressed risk keeps surfacing until it's dealt with, no matter how often it's waved off. One more thing worth knowing: Claude never sets anything aside on its own judgment — only your say-so does it. If you stopped a step partway, the recorded progress means a later session picks up from where you left off rather than starting over.

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first), and each line ends with the name of that session's full entry file. The entry file holds the detail — files touched, reasoning, captures routed. For design rationale, search the index, then open the named file.

## Does it matter which Claude model I'm using?

Not for anything you have to do. The plugin ships two versions of its own instructions — a fuller one and a lighter one — and works out which to use at the start of every session, from the model you're running. There's no setting for it and no message about it.

Both versions describe the same method: the same four commands, the same queue, the same rules about what Claude will and won't do without asking you. The only difference is how much explaining sits around each rule, because different Claude models follow instructions best at different lengths. So your project behaves the same way whichever model you build it on, and switching models between sessions is fine.

If the plugin can't tell which model is running, it uses the fuller version — the one it's been tested on longest.

## /setup used to ask which editor I use, and whether I work from my computer or my phone. Where did those questions go?

Both were removed, deliberately. The editor question recorded which app you'd open a doc in to edit it by hand — but nothing actually used the answer, since Claude's links open in its own viewer either way. The computer-or-phone question set a "working mode" that decided whether Claude showed you doc text as a link (at your desk) or pasted it into chat (on your phone). In practice that split just made people pick whichever meant less text, so it's gone: Claude now always gives a short summary plus a link, with the full text on request — a shape that works the same at a desk and on a phone. If your CLAUDE.md still has an `Editor:` or `Working mode:` line from an earlier version, it's simply ignored; you don't need to remove it.

## Claude wrote a draft straight into my queue before I approved it. Is that meant to happen?

Yes. Text headed for one of your project docs — a new queue item, a log entry, an edit to SPEC — gets written into the file first, and then Claude tells you in chat what it wrote: a short summary you can act on, a link to the file with the exact heading to look for, and the question you're being asked. If you'd rather read the whole thing in chat, just say so — the full text is always one word away.

You still approve it. Nothing is committed to your project's history until you do, and if you say no, Claude takes the text back out and confirms it's gone.

Two reasons it works this way. You read the item as it will actually appear, next to the items around it, which catches things a chat paste hides. And Claude doesn't have to write every draft twice — once in chat and once in the file — which costs tokens on longer sessions.

## Claude merged two pieces of work together without asking me. Is that allowed?

Yes, within a strict boundary. When two agreed pieces of work belong together, merging them changes *where* the work is recorded, not *what* gets built — so if the merge doesn't add any files to what the next build is allowed to touch, Claude just does it and tells you, naming the scope effect in the same breath ("this adds no files"). If a merge *would* add files — meaning the build would reach further than what you agreed — Claude still asks first. You can always object to a narrated merge; saying so un-merges it. Relatedly, planning sessions prefer to group work that touches the same files so one build session can clear more at once — but that's only a tie-breaker: work never jumps the queue or skips vetting just because it touches the same file as something else.

## Claude suggested adding a note to CLAUDE.md about where I post updates. Why?

Because it noticed you doing that kind of work more than once — posting to a Discord, sending a newsletter, reporting to a client — and there was nowhere in the project recording what happens to it.

The log records the things your sessions *produce*, not just changes to your app. An announcement you wrote with Claude is one of those things: a later session may well need to draw on it, and if it was never recorded it's gone. That's a real thing that has happened.

The CLAUDE.md note just saves re-deciding the same details every time — where that work goes, whether its full text gets logged or only a pointer to it, and what later draws on it. It's a suggestion, and declining it is fine. Claude will keep logging the work either way.
