# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — sorting your queue, capturing ideas, settling design questions. **/next** is for doing — it builds the work you've marked ready, and can work through several pieces back-to-back in one go. **/done** is for closing — records what happened, updates your docs, commits. Always in order: plan, do, close.

## What are the two sections in QUEUE.md?

**Processed** is work you and Claude have discussed and agreed. **Unprocessed** is everything caught but not yet weighed — ideas, discoveries, things noticed mid-build.

There's one move between them, and it happens in /plan: you talk an item through, and if it's worth doing it goes into Processed. Nothing else moves work around, because deciding what's worth building is your call, not something a build session makes on its own.

Inside Processed there's a line reading `--- Cleared to run above this line ---`. Everything above it is ready to build, and that's all /next will touch. Anything below it is waiting on another named item in your queue.

## How are entries organized in the queue?

Each piece of work is a heading — a one-line description of what it is — with its reasoning written underneath in plain sentences. At the end of the heading is a short name in square brackets, so a session record can point back at it later.

A tag at the front of the description says how the work gets done. No tag means Claude builds it. `[audit]` means a review that reads and reports rather than editing. `[user]` means a step you run, with Claude walking you through it. `[freeform]` means work Claude must not run from the queue at all.

Order matters in both sections: in Processed it's the order things get built, and in Unprocessed it's the order they get discussed.

*(There used to be "Batches" grouped under Build/Test/Audit subheadings. That structure is gone — one item per piece of work, no grouping.)*

## Where do security and privacy risks show up in the queue?

**On the piece of work that carries them.** When Claude spots something that could expose your data or your users' data, it tells you in plain English straight away, and marks the item with a line reading `Red flag · State:` followed by either `uncleared` or `cleared`.

The marker rides the work rather than living in a list of its own. That's deliberate: a standing "Red flags" section would suggest the tool tracks every risk your project has, when all it can hold is the ones Claude happened to notice. What it does is *raise* risks, not manage them.

- **uncleared** — the risk stands. An item in this state stays in Unprocessed and never reaches your ready work.
- **cleared** — dealt with, one of two ways: designed out or fixed, or you were told plainly and chose to go ahead. Either way the session record says which, and if you accepted it, what you were told.

The moment a risk gets cleared is when you and Claude discuss the item in /plan. If it can't be cleared, the item goes back to the bottom of Unprocessed rather than quietly moving on. And if a risk is ever still uncleared when /next reaches it, the run stops and says so.

*(This replaces an older "Red flags" section pinned at the top of the queue, which no longer exists.)*

## What happens to a check that can't be done yet?

It becomes an ordinary piece of work in your queue, like anything else.

Older versions kept a separate "Deferred tests" list for checks that couldn't run yet. That list is gone. A check you need to run yourself is a `[user]` item; if it's waiting on something else in your queue, it sits below the ready line naming what it waits on. At the start of every planning session Claude checks whether the thing it was waiting for has shipped, and offers to move it up if so.

The reason for folding it back in: a waiting list nobody is obliged to read is how a check sits unrun for weeks. In the queue, it gets weighed alongside everything else.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. The build's working file tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Is it safe to clear the conversation or start a new session between steps?

After /done, yes — everything is recorded in the session log and committed, so a fresh conversation loses nothing. Before /done, the plugin can still recover: it reads that conversation's own working file rather than relying on the conversation itself, so an interrupted build or planning session picks up from the file. But closing with /done first is the clean habit — it's the moment the work becomes a permanent record instead of something the plugin has to reconstruct.

## Can I edit SPEC.md while doing a build?

Yes, but never silently. SPEC.md is your project's source of truth, so it's kept from shifting under active work: the safety check blocks a build from editing any file the work being built doesn't list, and most builds don't list SPEC.md.

There are three ways it does change. A change you settle in /plan is made right there, in that same planning session. A build that discovers it needs SPEC to say something different **stops and asks you** — "this needs SPEC to say X instead of Y, add it to scope?" — and only edits it once you agree. And a large SPEC rewrite is simply a piece of work like any other, listing SPEC.md among its files.

*(There used to be a separate "spec-edit batch" type for this. It's gone — SPEC is an ordinary document that any piece of work can list.)*

**And builds now read SPEC rather than only writing to it.** At the start of a build run Claude reads your SPEC once, so every piece of work is built against it and gets checked against it. If something built contradicts what SPEC says, Claude stops and tells you which sentence — and **leaves the decision to you**, because either the build is wrong or the spec is, and only you know which.

That's a change from how it used to work, and worth knowing why. The old behaviour was to update SPEC at the end of a build to match whatever got built. That can only ever record what happened — it can't catch a build that went against your spec, because there was nothing to compare against. In practice it became a place to justify the work rather than check it.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. It gets added to Captures without derailing current work. Next /plan session picks it up for discussion and routing.

## The queue is empty. Does that mean the project is done?

No — an empty queue is a normal resting state. Run /plan when you have ideas or want to review. The project is done when you say it is.

## What is the `_build-...md` file? Should I edit it?

The active build's working file. It does four jobs: carries the work being built (so QUEUE.md stays free while the build runs), lists which files the build may change (the plugin's safety check blocks edits to anything else), ticks off finished steps (so an interrupted session can resume without redoing work), and keeps the reasoning (so /done can write the session record). Claude manages it — don't edit it. Deleted when /done closes the session; if it exists at session start, a previous build was interrupted and /next will offer to resume.

**The jumble of characters in the name is the session's own id**, so the file is `_build-<something>.md` rather than plain `_build.md`. Each conversation gets its own. That matters if you ever run two conversations at once — a planning chat alongside a build, say. With one shared file, the planning chat would see the build's file, decide it was inside that build, and apply the build's list of allowed files to edits you never agreed to. With one file per conversation, that can't happen.

## What is the `_plan-...md` file? Should I edit it?

A planning session's working file — the planning counterpart to the build one above, and named the same way, with the conversation's own id. When /plan starts working through your captures, it creates the file to track where it is: which items it's processing, the current one, and what it has routed so far (kept or dropped). It does three jobs: it survives a cleared or compacted conversation, it lets an interrupted /plan pick up where it stopped, and it gives /done a record of what was decided. Claude manages it — don't edit it. /done deletes it when the planning session closes; if it exists at session start, a previous /plan was interrupted and you can resume with /plan.

**If a working file is left behind by a conversation that never closed, Claude tells you at the start of the next session** and never deletes it. A working file can hold the only record of what a crashed session actually did, so throwing it away could lose real work. Run /done if you want what it records written up and committed.

## What if my project already has planning docs from another tool or an older version?

/setup handles it as a migration. When it sees your folder has content but none of the method's own docs yet, it treats your existing planning or spec documents as a starting point rather than assuming a blank slate. With your help, it maps that content into the method's docs (SPEC.md, QUEUE.md, and the LOG folder), keeping them at the top level of your project. Before renaming anything, it checks that each old doc actually fits the method doc it's mapped to — and if something doesn't fit, it asks you rather than guessing. It won't blindly rename or overwrite your existing files.

## What happens if Claude needs to touch a file the current work doesn't cover?

Claude stops and asks. A build stays inside the work it was given: "I need to edit [file] because [reason]. Add to scope?" Nothing outside that list gets edited without your yes.

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

## Can I see text before Claude writes it, instead of after?

**Yes — just ask, any time.** Say you'd like to see things before they're written, and Claude will show you the wording and wait for you for the rest of that session.

By default it works the other way round: Claude writes to your docs first and then tells you in one line what landed and where. That's deliberate — the text is in the file where you'd read it anyway, and if you don't like it, saying so undoes it. But if you'd rather approve wording before it exists, that's your call to make and it costs you nothing to ask.

It isn't remembered between sessions, and that's on purpose. It's about where you are and how you're working today, not a fact about you worth storing. Ask again next time if you want it again.

A few things are always shown first, whether you ask or not: a commit message, anything being sent outside your computer, and a wholesale conversion of a document you already own where there's no saved copy to fall back on. Asking only ever adds to that list.

**A related but different thing:** at the start of a session Claude offers to paste text into the chat rather than linking to the file — useful on a phone, or anywhere opening a file is awkward. If you take that offer, then during a /next run Claude also shows you each edit's new wording in the chat as it goes, and will point out any pieces of work large enough that showing them inline would bury everything else. That's just *seeing* the work — it doesn't pause the run or ask you to approve anything.

## Claude sometimes stops and corrects itself about something it said it filed. What's happening?

A check is catching a report that doesn't match your queue.

Here's the background. Claude writes to your queue **first** and tells you **after** — that way, if you don't like what it wrote, it's already there to look at and can be undone. The trade-off is that the telling is now a separate act from the writing. A reply can say "filed as [something]" when the write never actually ran, and from where you're sitting that reads exactly like a real one. This happened, and it happened repeatedly: the report was acted on before the work existed.

So when a reply says a named piece of work was filed, a check looks in your queue for it. If it's genuinely there, nothing happens and you see nothing. If it isn't, Claude is handed that fact and has to sort it out — make the write, or tell you plainly that it didn't land — before you go and rely on it.

**What you'll see** is Claude carrying on for a moment and correcting the record. It isn't an error and nothing is lost.

**What it doesn't catch:** a report that stays vague. "I've written that up" names nothing, so there's nothing to look for. That gap is deliberate rather than hidden — Claude is required to name what it filed, so the check enforces that rule and no more.

It also gives up after one go on the same claim, so a genuine disagreement can never trap the conversation in a loop.

## What is the "queue dependency facts" line at the start of a session?

Three numbers, worked out by reading your queue before Claude says anything: **how many items are ready to build, how many are held back waiting on other work, and how many of the things they're waiting on haven't been sorted out yet.**

It's there for one reason. Some of your work is stuck behind other work, and the useful question at the start of a planning session is *what should I sort out to get the most unstuck?* Claude used to work that out by reading the whole queue and counting by hand, which is slow and occasionally wrong. Now the numbers are counted before the session starts and simply handed over.

In a planning session you'll see them turn into a recommendation — something like "three items are holding other work up, so I'd suggest getting through at least those three." That number is now derived from the count rather than picked, and Claude will tell you where it came from.

**You'll see the line even when all three numbers are zero**, which is deliberate. "Nothing is waiting on anything" is genuinely useful to know, and staying silent would be ambiguous — you couldn't tell the difference between nothing to report and a check that didn't run.

You don't need to do anything with it. It's information, not a request.

## Another project sent me a message. When does Claude actually read it?

**At the start of your next planning session.** When you run /plan, Claude opens whatever is waiting in your INBOX before anything else happens — before it suggests dropping anything, and before it asks what you'd like to work on first.

Each message gets sorted into one of three places: work to do becomes an item in your queue, a finding gets written into your session record, and anything you'd need to re-read word-for-word gets saved as a file. Then the message file is moved into `INBOX/archive/` so it doesn't come up again.

You'll also see a line at the start of *any* session telling you mail is waiting — that's a heads-up, not the reading. And you can ask Claude to open your mail at any point in any session; /plan is simply the moment it's guaranteed to happen. Before this, mail could be announced session after session and never actually opened by anyone.

**Once a message has been read, its contents are just ordinary items in your queue.** They don't jump the line for having arrived by mail — they get weighed and ordered like everything else.

One limit worth knowing: **a message that arrives while you're mid-session won't be noticed until your next session starts.** That's when your mailbox is checked. Nothing is lost; it just waits.

## Why is my INBOX folder ignored by git, and can I change that?

If you run more than one project on this method, each gets an `INBOX/` folder — a mailbox where your other projects can leave you a message. Setup adds `INBOX/` to your `.gitignore`, so those messages stay on your computer and never get committed. You aren't asked about it, and the same thing now happens when an older project is brought up to date.

The reason is what a message *is*. It's another project's raw text, carried into this one. Anything you commit is published if your repository is public — and once it's in the history, deleting the file later doesn't take it back. Meanwhile, when Claude reads a message it moves the file into `INBOX/archive/` rather than deleting it, so an un-ignored mailbox would pile up other projects' text in your repository indefinitely, long after the useful part was already written into your queue in your project's own words.

**You can change it.** Delete the `INBOX/` line from `.gitignore` and messages will be committed like any other file. Nothing stops you — the ignore line is just the safe starting point.

One thing worth knowing, because it's easy to assume otherwise: **if messages were already committed before the line was added, the line does not undo that.** It stops future commits only; the old ones stay in your project's history. If that applies to you, Claude will say so when it adds the line rather than letting you think the mail is now private.

## Can I run two conversations on the same project at once?

**Yes** — a planning conversation alongside a build is a supported way to work, and Claude won't refuse one. What you can't do is run two *builds* at the same time, or mix planning and building inside one conversation.

**What Claude guarantees depends on how your app isolates sessions, and Claude now checks rather than guessing.** At the start of every session it looks at your project folder and works out which of two situations you're in. You'll see a one-line note saying which.

- **Sharing one folder.** Both conversations edit the same files. In practice this works fine — two additions to different parts of your queue don't clash, and if they somehow do, Claude gets a warning that the file changed underneath it. The one moment worth avoiding is the very end of a build, when Claude is rewriting the queue to remove finished work.
- **Each in its own copy.** The two conversations genuinely can't interfere. The catch is the mirror image: something you add to your queue in one conversation *doesn't reach the other one at all*, and when the two copies are merged back together, the last one to merge wins. So keep queue edits in one conversation until a merge has happened.

**One rule holds either way: don't interrupt a running build to add something to your queue.** If you're sharing a folder, there's no need — nothing collides. If you're in separate copies, it doesn't work — what you add lands in the other copy and the running build never sees it. Wait until the build finishes; nothing is lost by waiting.

## Why does a planning session now open knowing what happened last time?

Because it reads the last five one-line session summaries before saying anything.

Sessions don't remember each other. That used to show most at the very start of a planning session: Claude would be working from your queue alone, with no sense of what had just been done, and you'd often end up asking it to go and look. Now it reads the top five lines of your session index as part of getting its bearings, and folds anything relevant into what it says to you at the opening.

**It's orientation, not a report.** You won't get a summary of your recent history for its own sake — only the parts that bear on what you're about to work on. And it's five short lines, not five full session records, so it costs very little.

## Claude said "last session recommends starting with…". What is that?

A note the previous session left for this one.

When a session closes, if it has a clear view of what should happen next — because it just cleared a batch of related work, or because one item obviously unlocks the rest — it writes a single line into your queue saying so. The next planning session reads that line and mentions it in one sentence.

**It's orientation, not an instruction.** It suggests where to *start*; it never narrows the session to only that item, and you can ignore it entirely. It also isn't a piece of work — it never gets discussed, kept or dropped like your real queue items. It's cleared automatically at the end of the next session, so it can't go stale and sit there advising you about work that's already done.

## Why doesn't Claude ask whether I've already done a step it gave me?

Because asking makes you re-assert your own work before Claude will help you, and that turned out to be worse than the alternative.

A `[user]` item — a step only you can run — is walked through, and that's all that ever happens to it. Claude won't open with "have you already done this one?", won't close with "…or tell me if you've done it", and won't slip it in as an aside. If you *have* already done it, just say so and Claude takes you at your word and moves on to recording it.

**Where your step leaves a visible trace, Claude checks the trace instead of asking you** — a file that should now exist, a page that should now load, a branch that should now be gone. That's not asking; that's looking.

**The gap this leaves is deliberate.** If you quietly do something with nothing to show for it, the item sits in your queue until you mention it. That's a known cost, accepted on purpose, because the alternative is being interrogated about every step you were given.

## Something's wrong with the workflow itself, not my app. Where does that go?

Somewhere different, and Claude will ask if it isn't sure which. Three destinations:

- **Your app misbehaving** — an ordinary item in your queue, like any other work.
- **This workflow misbehaving** — a plugin bug, a confusing instruction, a step that doesn't fit how you work. That goes to the method's own report page at flintcraft.tech/report.
- **Claude Code itself misbehaving** — the app around the workflow. That's a GitHub issue on Anthropic's own repository.

**Nothing is ever sent without you seeing the exact text and saying yes.** Claude drafts the report, shows it to you in full, and waits. If you'd rather not send it at all, that's the end of it.

## Is my queue and session log safe to make public?

**Claude cannot tell you that, and won't.** The honest answer is that not publishing these files is the only real protection.

Here's what actually happens. Before writing anything into your queue, your spec or your session log, Claude reads back over the wording for things that shouldn't be committed — people's names, details that identify a real situation or client, anyone else's data, passwords and keys, file paths that identify a person or an organisation. Where it finds one, it rewrites it at the same level of usefulness: "a family member", "the client's deadline", rather than dropping the fact.

There's also an automatic check that looks for things *shaped* like passwords and keys.

**Neither of those can tell whether a sentence quietly identifies a real person**, and once something is committed, deleting the file later doesn't take it back — the history keeps it, and if your repository is public, so does the internet. So Claude will say it has checked; it will never say your files are clean or safe to publish.

## How do I steer a planning session — skip something, or stop?

Just say so. At the start of working through your queue Claude tells you the four things you can say at any point, once, and then doesn't repeat them:

- **continue** — go on to the next item. It only chooses *which item comes next*; it isn't you approving that item, and Claude won't treat it as one.
- **skip** — leave this one for another day. Nothing moves in your file; it's simply not brought up again this session.
- **stop** — stop working through the queue.
- **run /done** — close the session, record it, commit.

They aren't recited after every item, deliberately. Naming "close" at the end of every finished piece of work reads as an announcement that closing is what happens next — someone once closed a session they meant to continue for exactly that reason. All four stay available; only the repetition went.

## The plugin updated and Claude says my project's files are in an old shape. What now?

Claude walks you through it before doing anything else.

The workflow occasionally changes the *shape* of your own documents — a new section, a heading it reads, a field that becomes required. When that happens, the plugin records that the shape has moved on, and the next session that opens your project notices your files are still in the previous one and stops to convert them with you rather than carrying on and quietly misreading them.

**It only fires when something would actually be wrong.** An update that your existing files survive unchanged says nothing at all — which is the point of having a separate signal for it rather than reacting to every version bump.

## My app asked whether to keep or remove this session's copy of the project. Which do I pick?

**If the session did any work, do not pick remove until it's been merged.**

Some setups give each conversation its own private copy of your project, so two conversations can't tread on each other. The catch is what happens at the end: **that copy is never merged back on its own.** When you close it, the app asks whether to keep it or remove it — and *remove deletes the copy, the branch, and every commit on it.* It reads like tidying up. It isn't.

So the workflow does two things about it:

- **At the close of an isolated conversation**, Claude tells you which branch your work is on, that it hasn't been merged, and that "remove" would delete it. It can't do the merge itself from there — git won't let a copy update the main line while the main line is open elsewhere.
- **At the start of a conversation in your main copy**, Claude points out any copies holding commits the main one doesn't have, and offers to merge them. It offers; it never merges on its own. If the merge can't be done cleanly, it leaves the branch exactly where it is and tells you the work is safe there — you'll never be shown a tangle of conflict markers to sort out.

One honest limit: what Claude can see is *a copy holding commits yours doesn't*. It can't tell that apart from a deliberate long-lived copy — an archived version of the project, say — so it will describe what it found and judge before offering, rather than assuming everything it sees is stranded work.

## Claude flagged some queue items as contradicting themselves. What does that mean?

When you run /plan, Claude now checks your queue for work whose *position* disagrees with what the work itself says. It reports what it finds and stops there — it never moves anything.

Three things get flagged:

- **Work marked ready that says it isn't.** An item sitting above the "cleared to run" line whose own notes say it must not be built as written, or that a previous build session handed it back untouched. Left alone, the next build run would build exactly the thing the item warns against.
- **Work with nothing to change.** An item marked ready whose list of files to edit is empty, or says the list will come out of designing it. That means it's still a design question, not a build.
- **A chain of waiting.** Work waiting on something that is itself waiting on something else. Neither moves until the far end of the chain does, which is easy to miss when you only look at one item at a time.

**Why this check exists.** Work gets examined carefully when it's *put* into the ready pile, and then never looked at again. But things change around it afterwards — a decision gets reversed, a build session hands something back, the thing it was waiting for turns out to be waiting too. A gate on the door isn't the same as looking around the room.

**Nothing happens automatically.** Whether a flagged item gets moved, rewritten or left exactly where it is, is your call — that's a decision about what the work *is*, and those are always yours. Claude tells you and waits.
