# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top work item and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## How do the four commands fit together day-to-day?

You run **/setup** once, right at the start of a project. After that, every working session is either **/plan** (thinking and organising — managing the queue, adding ideas, resolving questions) or **/next** (building — it picks the top item and does it). You'll run /plan as often as planning needs, and /next once per item as you work down the queue: planning repeats for long stretches, building repeats across many items. However a session goes, it ends the same way — **/done** to record what happened, then **/clear** to start fresh. The one habit that matters: always /done before /clear, so each session is saved before the context resets.

## What does /setup do, and do I run it more than once?

/setup adopts your project folder into the method: it scaffolds the working docs (SPEC.md, QUEUE.md, the LOG folder, and this FAQ) and interviews you to fill in SPEC.md — what the project is, who it's for, how it works. The interview adapts to your answers rather than running a fixed list of questions: Claude reads each answer, asks the next thing that actually matters, suggests an answer you can just react to, and keeps going one question at a time only until there's a clear enough picture to build from. It's not an interrogation — you can stop it any time by saying "build from what we have," and Claude writes the docs from whatever you've covered. If your folder already has something in it — an old doc, a sketch, a running app — Claude reads that first and asks about what's still unclear, instead of asking things the material already answers. You run it once per project. If you run it again later — for instance after a plugin update — it only backfills scaffolding that's missing; it does not overwrite or reconcile content you've already written. So re-running it is safe, but it won't refresh or rewrite your existing docs.

## Can I keep several projects in one folder, and what if I open the wrong one?

Each Sovereign Implementer project is its own folder — self-contained, with its own SPEC, QUEUE, and log. You can keep several of them side by side (for instance nested under one parent folder), but they stay separate projects; the method doesn't run one project across many folders. Claude always works on the exact folder you opened the session in, and never goes hunting through nearby folders or asks you to pick one — the folder you point it at is the project. So to work on a particular project, open that project's folder directly. If you accidentally open a parent folder that just contains your projects, Claude notices and tells you: it says the folder looks like it holds separate projects and suggests you open the one you meant, because running /setup there would set up the parent folder itself rather than the project inside it. Nothing gets adopted or changed until you choose — the heads-up is only so you don't set up the wrong folder by mistake.

## Claude links me to a doc instead of pasting the text. Can I get the text in chat instead?

Yes — say so and Claude pastes text inline for the rest of that session. It also offers this in one line when a session opens, so you don't have to remember it exists.

The default is the link, because that text already lives in one of your project files and pasting it into chat writes it twice, which eats a session's budget for no benefit when the file is one click away. But if you're reading on your phone, or away from your computer, opening a file is a nuisance and a link is worse than useless — that's what the offer is for. It lasts the session and doesn't persist.

One thing to know about the links: they open the file, but they don't jump to a particular line — the app that opens `.md` files ignores that part. So when the exact spot matters, Claude names the line in the text around the link ("around line 40") rather than relying on the click.

There used to be two setup questions about this — which editor you use, and whether you work from your computer or your phone. Both are gone. The app opens `.md` files in its own viewer regardless of which editor you named, and the computer-or-phone question turned out to be measuring how much text people wanted pasted rather than where they actually were. One default plus one offer does the same job with nothing to maintain. If your project's CLAUDE.md still has an `Editor:` or `Working mode:` line from an older setup, it does nothing now and you can leave it alone.

## Will Claude ever ask whether I've already done one of my `[user]` steps?

No. Not in a build session, not in a planning session, not at a close — and not as a passing aside at the end of a walk-through. A `[user]` step is something Claude walks you through, and that's the whole of it. Being asked "have you done these yet?" reads as being chased about work you're perfectly reasonably saving for later, so the question is gone from the method entirely.

Instead, Claude works out what's done from what it can actually see: a step it walked you through to the end this session is done; a step whose prerequisite plainly hasn't happened isn't; and you mentioning that you did one is the third way. Where a step leaves something checkable behind — a page that now loads, a file that's now gone — Claude checks that itself rather than asking you.

There's one gap in that, and it's deliberate: if you quietly do a step on your own and it leaves nothing Claude can see, it'll stay in your queue until you mention it. Just say so and Claude records it and clears it. That's a better trade than being asked every session.

(If your project was set up before this changed, you may still have a **Completion mode** line in your CLAUDE.md. It doesn't do anything any more. Leave it or delete it — Claude ignores it either way.)

## There's a `.throughliner` folder in my project. What is it, and can I delete it?

It's a signal for other apps, and yes — deleting it is completely safe.

While Claude is writing to one of your files, it drops a small file in there saying "a write is happening right now, to this file". That exists so another application you have open on the same document — a Markdown reader or editor you're reading and typing in — can hold off for a moment instead of the two of you landing on top of each other mid-sentence. Without it, an app watching your files can see *that* something changed but not *who* changed it, and guessing wrong means being locked out of your own document while you're writing in it.

Two things make it safe rather than fiddly. Every entry carries a timestamp, and an app reading it treats anything more than about half a minute old as "nothing is happening" — so if a session crashes mid-write, nothing stays stuck. And an app that finds no folder at all simply carries on as normal, which is what happens in every project that doesn't use this plugin.

The folder is not committed to your project's history — setup adds it to your `.gitignore` — because it's about what's happening right now on this machine, not part of what you're building. If you delete it, the next write recreates it.

## What are the Processed and Unprocessed sections in QUEUE.md?

Your queue has two sections. **Processed** is vetted, ready-to-build work — one item per piece of work, worked top to bottom, discussed and agreed with you during /plan. **Unprocessed** is an inbox — ideas, questions, and tasks captured during builds or between sessions, not looked over yet. During /plan, each unprocessed item gets discussed and either moved up into Processed (kept as real work) or dropped. There's no in-between: a piece of work is unprocessed, processed, or gone.

Every work item carries a short name in square brackets (its slug), so Claude can refer to it precisely. Items you personally raised are tagged "captured by you," and that credit stays on the item even after it's processed; anything else is left unmarked (Claude is assumed to be the author by default, so it isn't labelled as such).

## What does it mean when a work item is marked `[user]`?

It's work only you can do — a check that needs your eyes on the screen, a decision only you can make, or a physical action like tapping *send* or plugging in a device. Everything else is Claude's to build. One thing that is *not* a `[user]` step: work Claude could run itself — a command, an install — that just can't run yet because it's waiting on something (a restart, a push). That stays Claude's to do; it's simply ordered to run once its wait clears, not handed to you. When Claude works down the queue, it builds all its own items first, then walks you through any `[user]` steps at the end. Most items aren't marked — they're Claude's by default.

## When Claude reaches a `[user]` step, do I have to do it alone?

No — a `[user]` step isn't Claude dropping the task on you and stepping back. When Claude reaches one, it *leads* by walking you through it, live: it runs whatever parts it *can* (any commands or setup it can drive), then gives you the **first** step and waits while you do it, then the next, and so on — walking beside you one step at a time, not handing you a list to work alone. Helping you through it in real time is the whole point — it's a walk-through, not a hand-off. The `[user]` tag just marks who has to actually do or witness the step — usually because it needs your eyes on a screen, or a tool Claude can't reach. You're always welcome to say "just tell me what to do and I'll handle it," but the default is that Claude walks you through it, not that you're on your own. If there are several `[user]` steps, Claude takes them one at a time — it won't dump them all on you in one message.

One related detail about *when* these show up: Claude only brings up a `[user]` step once the work it depends on is finished. A step waiting on something not built yet sits below the "cleared to run" line, naming the item it's waiting for, until that item ships — so when Claude does walk you through one, it's genuinely ready for you to do.

## I did a `[user]` step Claude walked me through. How does it get recorded and cleared?

Once you've finished the step, Claude tells you how to close it out: **run /done to record it**, or **mention it at your next /plan**. Either way, Claude writes it into your session log and removes it from your queue — so a finished step doesn't sit there. This matters because a `[user]` step doesn't clear itself: if nothing records it, the next time Claude works down the queue it would bring you the same step again, as if you'd never done it. Claude never talks about recording or /done *during* the walk-through — that comes only after the last step is done (or you choose to leave it), so the walk-through itself always finishes first.

Claude won't ask whether you've already done a step, at any point — see the question above on that. If you finished one in an earlier session and it never got recorded, just say so and Claude records and clears it instead of walking you through it. And where the step leaves something Claude can check — a page that now loads, a branch that's now gone — Claude runs that check before recording it, rather than taking your word for it. That's not doubting you: a step has been logged as done once before when an unnoticed problem had actually stopped it, and the residue sat there for months. If a check comes back empty, Claude just tells you what it found and leaves the step in place.

## What are the build and audit flavors — and is there a separate "test"?

Every piece of Claude's work in the queue carries a flavor that says how Claude carries it out, shown as a small tag at the front of the line:

- **Build** (no tag) — the normal kind: Claude makes changes to your files. Most work is this.
- **`[audit]`** — a review pass: Claude reads something over and reports what it finds, without changing anything. The findings go into your queue for you to look over.

There's no separate "test" flavor. Checking is just part of building: any check Claude can run itself, it runs while building. A check only *you* can do — looking at a screen, tapping through your app — is its own `[user]` line, which Claude walks you through rather than running. When Claude works down the cleared part of the queue, it builds all its own items first, routing each by its flavor, and then walks you through any `[user]` steps — so a `[user]` step no longer ends the run partway through, and cleared work waiting after it still gets built. (Your planning session usually places `[user]` steps at the end of a run, so in practice the build runs straight through and the walk-through comes last.)

## Why did my audit file its findings as captures instead of writing them into a doc?

Because an audit's job is to find things and route them for review — not to write them anywhere durable yet. Everything an audit turns up goes into Captures, where the next /plan session and you look it over before any of it lands in a real document. That review step is the whole point: it keeps an unchecked finding from going straight into a doc you'll rely on. So if you want a lasting findings document — a report, or a summary for someone outside the project — that document is its own piece of work, built *after* the findings are vetted. The order is: the audit files findings as captures → /plan reviews them with you → a build session writes the document from the ones you kept. And if you happen to set up an audit item that points at a document to write into, Claude won't silently follow it — it'll notice the mismatch and ask which you meant: file the findings for review first, or run it as a build that writes the doc now.

## Where does Claude put research findings and test results?

One of three places, decided by a simple rule so nothing piles up where it doesn't belong. If a finding means there's **work to do**, it becomes a captured item in your queue's Unprocessed list — because it's work. If it's just **a finding or a clean pass** — something worth remembering but not a to-do — it goes into that session's log entry, which is durable and searchable and keeps your queue uncluttered (a test that passed is a finding, not work, so it's logged rather than left sitting in the queue). Only the third kind earns its own lasting file in the project's `resources/` folder: **evidence a future session will need to re-read word-for-word** — for instance a saved transcript that a specific queued item will later be judged against, where the exact wording *is* the evidence. `resources/` is kept for exactly two things — research write-ups and this re-read-later evidence — so it stays useful instead of becoming a junk drawer. So if you notice a finding went into the log rather than a new file, that's why: a file is only created when its exact words will be needed again later.

## Why does Claude sometimes ask me to run a test instead of running it itself?

Because some tests need something only you can provide — and when that's the case, Claude tells you plainly what the test checks, what it needs, and why it can't run it. A test might need you to look at a screen and judge how something appears, tap through your app on a phone, or run a command in a terminal Claude can't reach. Claude usually can't see your setup, so it doesn't guess what you can or can't do — instead it names exactly what the test requires ("needs the terminal," "needs a phone connected," "needs you to look at the screen") and leaves it to you to judge whether that's yours to do. If a test needs nothing of yours, Claude just runs it — handing one to you is only ever for the checks that genuinely need you.

## Claude offered to find a command-line tool to do a task for me. Why?

Because it can often do a job itself with a small command-line tool instead of walking you through doing it by hand in an app — and doing it for you is usually faster and less error-prone. So before handing you a step-by-step for a desktop app, Claude pauses to consider whether a tool exists that would let it just do the task (things like reading text out of a scanned image, converting a PDF, or reshaping a data file often have one). When it thinks one might but isn't sure which, it offers to look one up on the web. You're never obliged to say yes: decline and Claude falls back to guiding you by hand. And the usual safeguards still apply — Claude names the tool and what it's for rather than installing things blindly, asks before downloading or running anything, and won't assume you have a terminal or the right setup; it names what a tool would need and lets you say whether that fits. The reason it offers this on its own is that a lot of these tools aren't things a non-coder would know to ask for — so the option shouldn't depend on you knowing it exists.

## Do I need to use the terminal to install or update SI?

No. The plugin installs and updates through Claude Code's own plugin system, and **Claude runs those commands for you** — you just ask it in plain English inside a Claude Code chat. You never open or type into a terminal. "Marketplace" and "CLI install" sound technical, but in practice they mean: Claude Code knows where to find this plugin (a marketplace is just the published location on GitHub), and it fetches and installs it with a couple of commands it runs itself. To install, you ask Claude Code to add the `FlintcraftTech/throughliner` marketplace and install `sovereign-implementer@flintcraft`; to update later, you ask it to run the update. (Those two names not matching is expected, not a typo — the repository and the plugin inside it are named differently.) Either way it's Claude doing the typing, then you fully restart the app so the new version loads.

## How do I find out when there's a new version of the plugin?

GitHub can email you whenever a new version of Sovereign Implementer is published. Go to the plugin's page at `https://github.com/FlintcraftTech/throughliner`, click **Watch** near the top right, choose **Custom**, tick **Releases**, and click **Apply**. After that you get an email each time a new release goes out. It needs a free GitHub account, which costs nothing to set up.

## I just updated the plugin — how do I check it still works?

You don't have to do anything special. Just carry on using it — run your normal /plan, /next, and /done sessions — and if something behaves oddly, you'll notice it in the moment and can have Claude capture it as work to fix. There's no set-aside list of post-update checks to work through, and no separate testing session to run.

The one exception is a check that genuinely can't be done except by you — looking at a screen, tapping through your app, running something in a place Claude can't reach. When a piece of work needs a check like that, it's written into your queue as its own `[user]` item, so it's already waiting for you there rather than resting on you to remember it. Everything Claude can check itself, it checks while building — so most updates need nothing from you at all.

## What is the "build stamp" the plugin records at the start of a session?

A short fingerprint of the installed plugin's own files — a content check that reflects exactly what's installed right now, not just a version number. Its job is to tell whether a plugin update is genuinely in place after you reinstall. Some behaviour can only be confirmed once an update is actually live, and a version number alone can miss a change that didn't bump the version — so the stamp gives Claude a reliable yes/no on whether the installed files are current. It runs behind the scenes: you don't see it or manage it, and nothing about your own project goes into it — it only fingerprints the plugin's files.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. `_build.md` tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Is it safe to clear the conversation or start a new session between steps?

After /done, yes — everything is recorded in the session log and committed, so a fresh conversation loses nothing. Before /done, the plugin can still recover: it reads its working file (`_build.md` or `_plan.md`) rather than relying on the conversation, so an interrupted build or planning session picks up from the file. But closing with /done first is the clean habit — it's the moment the work becomes a permanent record instead of something the plugin has to reconstruct.

## Claude offered to write a "handoff prompt" for a fresh session. What is that?

It means Claude thinks a clean restart would help — and it only ever offers this after *you* signal the session is wearing thin: it's dragging, the answers are slipping, or the usage bar you can see (and Claude can't) is filling up. Claude has no sense of that on its own, so it waits for your cue rather than guessing. When you give it, Claude offers two things: to continue the work in a brand-new session, and to write you a paste-ready handoff prompt — a short summary of what you're working on, what's been decided, and what's left to do — that you drop into the fresh session so it picks up right where you left off, without you having to re-explain. A long conversation gradually gets slower and more error-prone as it fills up; starting fresh is the fix, and the handoff prompt is what stops you losing your place in the switch. It's only ever an offer — say yes and Claude writes the prompt, or wave it off and keep going.

## What's the difference between committing and pushing, and why does Claude only ask about pushing?

Two different saves. **Committing** saves a snapshot of your work to your project's history on your own computer. It always happens when you close a build session, and you don't have to approve it — the snapshot's description is the session summary you already approved. **Pushing** additionally sends that snapshot to a remote backup, like GitHub, if your project has one set up. So at the end of a build, Claude commits first (the safe, local save), then asks whether to also push (the part that sends your work somewhere external). If your project has no remote set up, there's nothing to push to, so Claude just commits and doesn't ask. Planning sessions commit too, but never offer a push — they record bookkeeping, not a change to release.

## I changed some files by hand — how do I save them?

Just run /done. Claude reads changes you made yourself as your own expected work — not as something broken — confirms they're yours, writes them up in the session log, and commits them. You don't have to run /plan or /next first: a /done on its own, after a set of hand edits, records and saves them cleanly. It's never required — if you leave hand edits uncommitted, the next /done you run (after any session) sweeps them up anyway — it's just there for when you want your handmade work saved as its own tidy record. If you made several unrelated changes, Claude may split them into separate log entries so each is easy to find later. One habit, entirely optional: if you've made ad-hoc changes by hand, mention it to Claude before running /done. It's not a requirement and skipping it breaks nothing — Claude handles the changes either way — it just helps Claude describe them accurately.

## Why did Claude say my new change has to wait for a fresh session?

Because the close (/done) is for recording and saving the work that was just finished — not for starting new work. If you ask for something brand-new while Claude is closing a session — a redesign, a new feature, a change to something that already worked — Claude finishes the close first, then that new change becomes its own build session (or gets noted for later if it isn't urgent). The one thing Claude will fix on the spot is a genuine bug in what was just built — that's finishing the job, not starting a new one. Keeping new work to its own session means it gets planned and built properly instead of squeezed into the close.

## Can I change SPEC.md, and how?

Yes. SPEC.md is your project's source of truth, and the method keeps it changing only in deliberate, approved ways — but it's a normal document now, not something locked behind a special mode. A SPEC change happens one of two ways. If a planning session decides something that changes what SPEC says — a new capability, a different rule, who it's for — Claude updates SPEC right there in that /plan session, with your approval. If a build turns out to need a SPEC change, Claude asks you, adds SPEC.md to that build's file list, and edits it as part of the build. Either way you approve the change before it lands, and the safety check still blocks a build from touching SPEC unless that build lists it in its files — so a spec change never slips in quietly as a side effect of something else. (There used to be a separate "spec-edit step" for this; it's gone — it added a whole extra step to change one line and protected nothing that the approval and the safety check don't already.)

## What's the difference between SPEC.md, CLAUDE.md, and Claude's memory?

Three different homes for three different kinds of thing, and they're easy to mix up:

- **SPEC.md** is *what your project is* — what it does, who it's for, how it works. Product truth. A feature, a rule your app enforces, who the users are: all SPEC.
- **CLAUDE.md** is *how Claude should work on this project* — your conventions, workflow rules, house style. Instructions for Claude, specific to this one project.
- **Claude's memory** is for things that apply *across all your projects* — how you like Claude to communicate, your general preferences — not tied to any single project.

Two quick tests sort almost everything. "What it is" vs "how to work on it" splits SPEC from CLAUDE.md: if it describes the product, it's SPEC; if it's an instruction for working on the product, it's CLAUDE.md. "This project" vs "every project" splits CLAUDE.md from memory: only-here goes in CLAUDE.md, everywhere goes in memory. One thing Claude watches for on your behalf: if you say "make Claude always do X" but it's really describing what the app should *do*, that's product truth — Claude will point out it belongs in SPEC, rather than filing it as a working instruction.

## When Claude edits a doc or other writing during a build, do I see the new wording?

Yes. For readable changes — a doc, a piece of copy, a section of your spec, anything you read rather than run — Claude surfaces the actual new wording right after making the edit, so you see what changed. Normally that's a link to the edited file, with the line named in the text beside it; if you've asked for text in chat this session, Claude pastes the new wording inline instead. Either way you meet the real words, not just the plan for them. (Code changes aren't shown this way; reading raw code back wouldn't tell a non-coder much.) The exact wording is written while building, so this is your first look at the real words, not just the plan for them. If something's slightly off, you can ask for a small tweak on the spot — "change this one bit" — and Claude adjusts it there and then, as part of the same build, no separate step. Only a genuinely new or bigger change — a different feature, or reworking something that already worked — waits for its own session.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. It gets added to your Unprocessed work without derailing what's going on. The next /plan session picks it up for discussion — kept as real work or dropped.

## Why does Claude sometimes re-read our conversation at the end of a planning session?

Before wrapping up a planning session, Claude takes a pass back over the conversation and points out things you mentioned in passing but never asked to save. It's a safety net: when you think out loud, good ideas and concerns slip by without being formally captured, and this catches them before the session closes. It's best-effort — Claude can only re-read what's still in view, so in a long session some earlier discussion may already be out of reach. That means "I didn't find anything" means nothing jumped out in what Claude could still see, not a guarantee nothing was missed. Whatever it surfaces, you approve (or wave off), and approved items get sorted into the queue like any other captured idea.

## Does Claude do that end-of-conversation pass when I close with /done too?

Yes — a lighter version. When you close any session with /done, Claude takes the same quick pass back over the conversation and points out things you mentioned but never asked to save. The difference from a planning session is what happens next: at /done it only *files* what it finds into your captures list, so nothing is lost, and leaves the sorting — whether each one becomes real work or gets dropped — for your next /plan. You still approve what gets filed; Claude shows you the wording first. Two limits worth knowing: if you opened a brand-new conversation just to run /done, there's no earlier discussion to re-read, so it won't find anything; and if you already did a planning session in the same conversation, it may turn up the same things you already captured, which is harmless.

## Claude offered to "seed the queue from SPEC." What does that mean?

When your SPEC describes a lot of your app but your queue is empty or nearly so, all those described features have no path into your build queue — they can just sit in SPEC with nothing to build them. So in that situation Claude offers to *seed* the queue from SPEC: it reads your SPEC and drafts a set of work items from the features it describes, so the backlog actually reflects what you've said you want built. You choose how chunky those items are — a few big milestones, or one item per feature — and you approve the drafts before anything is written. The items land in your **Unprocessed** list (the inbox), not straight into ready-to-build work, so they still get discussed and vetted in planning like any other idea. Claude only offers this on its own when your queue is thin and your SPEC is rich; the rest of the time it stays quiet, but you can ask for it any time by saying "seed the queue from SPEC." Note this is a /plan thing — /setup never does it; setup only scaffolds and interviews, it never invents work for you.

## The queue is empty. Does that mean the project is done?

No — an empty queue is a normal resting state. Run /plan when you have ideas or want to review. The project is done when you say it is.

## What is _build.md? Should I edit it?

The active build's working file. It does four jobs: carries the work item being built (so QUEUE.md stays free while the build runs), lists which files the build may change (the plugin's safety check blocks edits to anything else), ticks off finished steps (so an interrupted session can resume without redoing work), and keeps the item's reasoning (so /done can write the session record). Claude manages it — don't edit it. Deleted when /done closes the session; if it exists at session start, a previous build was interrupted and /next will offer to resume.

## What is _plan.md? Should I edit it?

A planning session's working file — the planning counterpart to _build.md. When /plan starts working through your captures, it creates `_plan.md` to track where it is: which items it's processing, the current one, and what it has routed so far (kept or dropped). It does three jobs: it survives a cleared or compacted conversation, it lets an interrupted /plan pick up where it stopped, and it gives /done a record of what was decided. Claude manages it — don't edit it. /done deletes it when the planning session closes; if it exists at session start, a previous /plan was interrupted and you can resume with /plan.

## What if my project already has planning docs from another tool or an older version?

/setup handles it as a migration. When it sees your folder has content but none of the method's own docs yet, it treats your existing planning or spec documents as a starting point rather than assuming a blank slate. With your help, it maps that content into the method's docs (SPEC.md, QUEUE.md, and the LOG folder), keeping them at the top level of your project. Before renaming anything, it checks that each old doc actually fits the method doc it's mapped to — and if something doesn't fit, it asks you rather than guessing. It won't blindly rename or overwrite your existing files.

## Claude says my project is "out of date" and offers to run /setup. What does that do?

It means the plugin has been updated and now creates a file or folder your project doesn't have yet. Running /setup catches the project up: it adds what's missing without touching your existing work — it backfills the missing scaffolding and does not overwrite or reconcile content you've already written. So it's safe to run, but it isn't a cure-all: it won't refresh or rewrite your existing docs, only add what's absent. The one exception is your **queue**: if an older version stored it in a different layout, /setup offers to convert it to the current format — and even then it drafts the converted queue and shows it to you before writing, so nothing changes without your okay. If something already in your docs is out of step with the new version, that's a separate change you'd make deliberately, not something /setup does for you.

## I want to undo a lot of work and go back to how the project was a while ago. What should I know?

Ask Claude — it has a guide for exactly this and will read it before starting. The rolling-back part is straightforward. The part that catches people is what happens *afterwards*, so here is the headline.

**Your queue will start asking for work that's already done.** Going back restores your files, but it can't restore the match between your queue and reality. Work that was finished before the point you're going back to is still finished in your project — but the queue entries describing it come back, because they were cleared away when that work was built. So the next few sessions get handed finished work, presented as ready to build, with nothing marking it. In one real case that happened seven times in a single session, and every one was caught by luck.

So for the first few sessions after a big rollback, expect Claude to check the record before building anything, and don't be surprised when it says a piece of work is already done and removes it.

A few other things the guide covers: bring back straight away anything that obviously wasn't the problem, rather than restoring it piecemeal later; if another project of yours was built against this one, it may quietly break; and going back undoes *deletions* too, so things you deliberately got rid of will reappear.

## Does Claude check my queue and logs for private information before they get committed?

Partly — and the honest answer to the second half of that question matters more than the first, so here it is up front: **you should never treat these files as checked and safe to publish.**

Here's what actually happens. Two things run. A mechanical scan looks at QUEUE.md, SPEC.md and your log entries for things *shaped* like credentials — a private key, an API token, an email address. That scan is exact: it either matches a known shape or it doesn't, so it never guesses and never gives you false comfort. Separately, before writing a new item or a log entry, Claude reads what it's about to write against a short list — personal names, details that identify a real situation, other people's information, paths with someone's name in them — and rewrites what it spots.

Now the limit. The second half is Claude checking its own writing, and the first half only knows credential shapes. Neither can tell whether an ordinary sentence quietly identifies a real person — and that, not a leaked password, is what actually gets exposed from files like these. So Claude will never tell you your files are scrubbed or clean, and you shouldn't infer it.

This matters because these files get committed, and a commit keeps the text even after you delete it. If your repository is public, or might become public, the only real protection is not publishing these documents at all — keeping them out of the repository entirely, rather than trusting a check to have caught everything.

## A session stopped and said my project's files are on an "older format". What is that, and is my work at risk?

Your work is safe, and stopping is the point. The method occasionally changes the *shape* of your project's own documents — how the queue is laid out, what a piece of work looks like, which lines Claude reads for what. A project set up before such a change has files in the older shape.

That is worse than a missing file, which is why it gets a full stop rather than a note. A missing file announces itself. A file that's *present* but on an old shape doesn't error at all — Claude reads it, gets a wrong picture, and carries on confidently. You'd get a session's worth of planning or building based on a misreading, with nothing anywhere saying so. Stopping first is the only way that doesn't happen quietly.

The fix is to run `/setup`. It migrates what's there rather than replacing it: your work items, your notes, your reasoning all carry across into the new shape, and Claude shows you the converted version before writing anything. Once it's done, the project records the new format and sessions open normally again.

Two details worth knowing. This is **not** the same as "the plugin has a new version" — the plugin updates often and almost none of those updates change the format, so you won't see this message routinely; it's reserved for the changes that genuinely affect your files. And if you'd rather press on, you can tell Claude to carry on anyway — it's your call. Claude will do it and mention once that what it tells you may not be reliable until the migration runs.

## A session opened by saying my project was missing something — what happened?

The plugin keeps improving after your project is set up, so a project can end up missing a setting the method has since added. At the start of a session, before /plan or /next, Claude checks for this and catches the project up — adding only what's missing, and never rewriting or clobbering anything you've written. Most of the time it just adds what's needed and tells you in one line what changed; if something genuinely needs an answer from you, Claude asks it in one line and you can always say skip. This only ever adds; if something already in your docs is out of step with a new version, that's a separate change you'd make deliberately.

## What happens if Claude needs to touch something outside the current work item?

Claude stops and asks. It stays within the work item's scope. If something else needs changing: "I need to edit [file] because [reason]. Add to scope?"

## Will Claude use my phone or another device to test my app?

Only if you say yes. Some checks need a real device or emulator — installing the app on a phone, tapping through a screen. Before Claude connects to or tests on any device attached to your computer, it asks your permission first and waits for your answer. It won't reach into your hardware silently. And if no device is connected, Claude asks whether one is available rather than guessing — so a check that needs a device doesn't quietly get skipped or run behind your back.

## What's a "red flag," and what do cleared and uncleared mean?

A red flag is how Claude surfaces a risk to your data or your users' data — anything that could expose private information or amount to a security breach. Claude watches for these in every session, and when it spots a genuine one, it tells you plainly rather than quietly working around it or building past it. The risk then goes into your queue as an ordinary piece of work, marked with a red-flag tag and one of two states:

- **Uncleared** — the risk still stands, and nothing's been decided about it yet. An uncleared flag sits in the "not yet fully processed" part of your queue; it's surfaced first each session until it's dealt with.
- **Cleared** — the risk has been dealt with, one of two ways: either it was **designed out or fixed** (the work no longer carries it), or you **heard it spelled out and chose to go ahead anyway**. Which of the two it was is written into the session log — for an acceptance, that's the record of what you were told and that you agreed, the trail that protects you if the risk ever surfaces later.

Clearing a flag happens when you and Claude work through the item in planning — a piece of work only becomes "ready to build" once its flag is cleared. If a risk can't be cleared yet, its item stays in the "not yet fully processed" part of the queue rather than moving to "ready" — so a risk is never quietly shelved.

It's tagged onto a work item rather than kept in a separate "risks" list, and that's deliberate: a standing risk list would look like a promise that Claude tracks every possible risk to your project, which no tool can honestly make. The tag only ever marks the risks Claude actually noticed — real ones, surfaced so you can decide what happens next.

## What happens to a red flag when the work carrying it is built?

By the time a red-flagged piece of work is ready to build, its flag has already been cleared — that happened back in planning, when you and Claude decided how the risk was handled and recorded it in the log. So when the work is built and committed, Claude just carries that cleared flag through into the session log; the risk was never left hanging. A red flag never quietly disappears, and it never lingers as a leftover reminder with no work left to do.

One detail worth knowing: a risk counts as cleared the moment it's designed out or you accept it — even if a fix still needs a real-world check to confirm it works. That leftover check becomes its own `[user]` item in your queue — a normal thing for you to verify later — rather than keeping the flag hanging. So "fixed, with a check still to do" shows up as a cleared flag plus a waiting check, not as an unhandled risk.

## Why did Claude ask before starting a "subagent"?

A subagent is a separate helper Claude can spin up to go off and work on something on its own — handy for wide, open-ended research. The catch is cost: a subagent burns through usage fast, and a single run that fans several out at once can use up your session's usage in one go. So before Claude starts one, the method stops and asks you first — a prompt saying Claude wants to start a subagent, which you approve or decline. Declining is completely fine: Claude just does the work directly instead, which is usually all that's needed. The prompt exists so a subagent can never quietly run up a big cost without you knowing — you always get the choice.

## What does a "Plan session here" line in the queue mean?

It's a planning checkpoint Claude placed between work items. When /next reaches it, /next stops and tells you a planning session is needed first, naming the reason — usually because the next work depends on a decision, or on findings that only get sorted out in /plan. Run /plan: it handles the named reason and removes the line, and then /next can carry on. You don't add these yourself — Claude places them when it sees a planning moment coming.

## I have work sitting below the "cleared to run" line, waiting on something. Will Claude come back to it?

Yes, and there's only one reason work can be sitting down there: **another item in your queue has to happen first.** Claude writes that other item's name right into the held one — a line reading `Blocked by:` followed by the name in square brackets — so what it's waiting for is never a vague note, it's a specific piece of work you can look at.

That matters more than it sounds. Work often waits on something in the world rather than on other work — a restart, a website going live, somebody getting back to you. Those don't get written as a waiting-note inside the held item; they get written as **their own item in your queue**, which means they turn up in planning like everything else and actually get done. The old way buried them as a sentence inside another item, where nobody ever saw them — one piece of work sat waiting for weeks on a step that was never going to happen, because nothing had put that step anywhere you'd find it.

Then at the start of every planning session, Claude goes down the held work and checks one thing per item: has the thing it's waiting for been finished? If yes, Claude offers to move it up above the line so it's ready to build. If not, it stays put and Claude says nothing about it — no repeated questions, because there's nothing to ask you: the answer is in the record, not in your memory.

## What does the "Cleared to run above this line" marker in the queue mean?

It's a line Claude keeps in your queue showing which work is ready to build. Everything above it has been vetted in planning — discussed and agreed with you, and ready to build next. Everything below it still needs a planning pass before it's ready. Claude positions the line at the end of every planning session and tells you where it sits, so you never have to work out for yourself how much of the queue is safe to run. When /next runs several ready items in a row, it stops at this line — a clean finish, rather than running on into work that hasn't been vetted. You don't manage the line; Claude does.

## Why did /next stop before finishing everything?

Because it hit a wall on one item and stopped rather than spinning on it. When /next works down your cleared queue, it watches the item it's building for signs of no progress — the **same error** coming back, an edit that **changes nothing**, or the **same check failing** the same way, roughly three times on one item. When it sees that, it stops and tells you plainly what repeated (the exact error, or what wouldn't change), and hands you the decision, instead of burning the rest of the run thrashing on something stuck. Since /next often runs faster than you're watching, this stop is what keeps a stuck item from quietly wasting the whole session. It's not a failure of your project — it just means that one item needs a human look before it can go further; the items already finished before it are safe, and you decide how to handle the stuck one from there.

## Why does a planning session open by asking what I want to prioritise?

Because the order you work through your ideas in changes how much you get out of the session, and you're the only one who knows if something is urgent today.

The opening has two parts. First, if anything in your queue is obviously not worth doing any more — a duplicate, or something whose reason has passed — Claude shows those as one short numbered list to drop together, and you name any you'd rather keep. That comes first because there's no point deciding the order of things that are about to be deleted. (If nothing is obviously droppable, this part doesn't happen at all.)

Then one question: anything you want to prioritise, or shall Claude work through them most-unblocking-first? That default means starting with the item whose answer frees up the most other work — settle it, and several other things become possible. It's usually the right order, so you can just say go. But if something has become urgent, or you woke up thinking about one particular idea, saying so here is what puts it first.

If nothing in your queue unblocks anything else, Claude falls back through a few other sensible orders on its own — an unaddressed privacy or data-exposure risk always goes first, then things whose reasoning is going stale, then quick decisions that clear the pile down. You don't get asked about any of that; Claude just says in one line what order it used.

## How does a planning session work through my unprocessed ideas — can I skip or drop things?

Yes, both, and it's built to keep you moving rather than grinding through every item in order. The session opens with the drop list and the ordering question (see [the previous answer](#why-does-a-planning-session-open-by-asking-what-i-want-to-prioritise)), then it puts the items that would unblock the most other work first and suggests roughly how many to get through this session.

After that it goes through the rest one at a time. At each step you can carry on to the next item, **skip** the next one to the bottom of the queue for a later session (it's not dropped — just set aside), close out, or raise something new. And if you toss in a fresh idea mid-session, Claude files it and asks whether you want to dig into it now or keep going through the queue — so a new thought never feels like it got parked and forgotten.

Claude may also *suggest* skipping an item itself: if a piece of work turns out to be too big or too unsettled to pin down into something buildable this session, it'll propose noting down whatever you worked out and setting the item aside for a later planning session, rather than grinding on it. There's no special "give this its own session" mode — setting it aside to the bottom of the queue *is* how something gets deferred, and next time it comes back up as an ordinary item.

## Why did Claude reorder my queue at the end of a planning session?

At the end of a planning session, Claude checks whether either section of your queue needs reordering and, if so, puts it in the order that makes the most sense for working through it. It doesn't re-sort from scratch every time — it looks at what changed that session and only moves things when the current order is actually wrong, so a session that didn't disturb the order leaves it untouched and says nothing. For unprocessed items, it puts the one that would unblock the most other work first — so processing it moves the most things forward. For processed items, it puts the one that should be built first — the one whose output is needed by later work — at the top, so you're not building something that depends on something you haven't done yet.

Claude owns this ordering and does it on its own — it tells you what it moved and why, but doesn't ask permission. That's because ordering is low-stakes and easy to undo (just say "move X back above Y"), and asking about every reorder would add ceremony to every planning close. The narration is the catch-point: if Claude moved something you disagree with, say so and it adjusts. A reorder that changes what gets built *next* is flagged clearly; a small tidy gets a one-line note.

## Claude tidied up the queue while committing, without asking me. Is that normal?

Yes. Some queue housekeeping is Claude's to handle on its own — clearing a "waiting on" note once the thing it was waiting for is done, or fixing a pointer to a section that has moved. These change nothing you decide: they drop no work, reorder nothing, and don't alter any choice you've made — they're bookkeeping on entries that are otherwise fine. So Claude makes the fix and tells you it did, as part of the commit, rather than stopping to ask. Anything that's a real judgment call — dropping an item, rewriting it, or deciding whether to keep it — still waits for a planning session and your say. You always see what was tidied; you just aren't asked to approve the routine kind.

## Something is broken or confusing — where does it go?

There are three possible homes, and the question that picks between them is simply: **which thing is misbehaving?**

- **Your app** — the thing you're building. That's ordinary work, and it stays in your queue as a capture, like anything else.
- **The method** — a command doing something odd, a step that doesn't make sense, a rule that produced a bad outcome, or a question this FAQ doesn't answer. That's not work on your app, and a note about it would just clutter your queue, so it goes to the plugin's author at **flintcraft.tech/report**.
- **Claude Code itself** — the app all of this runs inside: its viewer, its links, its own machinery. That belongs to Anthropic, not to this plugin, so it goes to a **GitHub issue on `anthropics/claude-code`**.

If Claude genuinely can't tell which of the three it is, it asks you rather than guessing — a wrong guess either buries method feedback in your app's queue or pushes your own work out to a stranger.

Both outward reports are scrubbed by design: they describe what happened, which step, and the version — never your app's name, your files, or any secrets. And nothing is ever sent without you reading the exact text first.

The two differ only in who does the sending, and only because of what's possible. The method report goes to a web page Claude can't fill in for you, so Claude writes it out and you paste it. A Claude Code report can be filed from the command line, so if you have GitHub's `gh` tool installed and you're signed in, Claude offers to post it for you — showing you the full text and waiting for an explicit yes. If you don't have `gh`, Claude writes the report out for you to paste on GitHub yourself, so the offer never simply fails. Before drafting a Claude Code report, Claude searches the existing issues — partly to avoid repeating one, but mostly because knowing what's already been reported is what lets your report say something new.

Either of you can start one: tell Claude when you hit something, or Claude may spot it mid-session and offer once, without nagging.

(None of this is Claude Code's built-in `/bug` command. That reports Claude Code to Anthropic — fine for the third case, but it can't reach this plugin's author, so it's never the route for a method problem.)

## Why is there a "Last session advises…" line at the top of my queue?

That's a forward-recommendation note — the previous session's suggestion for where to focus next. It's there so you don't have to remember what the last session recommended; the recommendation sits right where the next /plan session sees it first.

You'll see it ends with `[forward-advisory]`, the same way your real work items end with a short name in brackets. That's deliberate: your queue's automatic checks expect every line in that shape to carry one, and the note used to be written without it — which made the checks complain about a perfectly correct note, and stopped the tool that moves and removes queue items from running at all while the note was there. Giving it a fixed name of its own fixed both. It is still not a work item, and Claude never treats it as one.

It's advice, not a command. When you run /plan, Claude reads it, mentions what it says, and lets it inform where you focus — but you're free to go a different direction. Once you and Claude have agreed on the processing or build order for the session, the note is deleted automatically. It never moves into Processed and is never treated as real work — it's a one-time orientation handoff that disappears once it's done its job. If no note is there when you start /plan, nothing was recommended — the last session's close didn't have a specific suggestion to make.

## Claude offered to delete some files when I closed a session. What's that?

When you close a session with /done, Claude offers to clean up throwaway files it made during that session — a scratch file, a one-off working file with no further use. It only ever offers files *it* created this session that have no future purpose, it asks about each one singly, and it never deletes anything without your yes. It won't touch files you made yourself — those are treated as your own work, never as rubbish. When a file is tracked in your project's history, Claude says so (you could get it back if needed); when it isn't tracked, or it's outside your project, Claude warns you the deletion is permanent before you approve. Most of the time there's nothing to clean up, because Claude writes its temporary files to a scratch area outside your project in the first place — so they never land in your folder, and they clear themselves.

## Why did Claude split my project into several files (or keep it in one)?

When Claude builds, it recommends how to divide your project across files by a simple rule: split things that are genuinely independent — a self-contained tool, a standalone screen — into their own files, but keep things that have to be understood together in one file. The reason is that Claude does the editing. When each piece lives in its own file, a change touches just that file, Claude reasons over less at once, and a mistake stays contained instead of spreading through the whole project. The flip side is that Claude works less well when closely related logic is scattered across files, so tightly connected parts stay together even if that file grows large. It's a recommendation, not a rule — you can always ask for a different structure.

## What is the filed-after note on one of my captured items?

When Claude captures an idea into your queue, it tags it with the last save-point that existed at that moment — shown as a short "filed after …" note. It's a rough marker of *when* the item was captured. It matters most for ideas captured after a session was already recorded and saved, so there's still a trace of roughly when they came up rather than the timing being lost. You don't need to do anything with it — it's bookkeeping that helps place the item in time later.

## What is the INBOX folder, and how do my projects send each other messages?

If you run more than one project on this method, they can pass notes to each other instead of you carrying them between chats. Each project has an `INBOX/` folder. When another of your projects has something to tell this one, it writes a message file in there, and at the start of your next session Claude mentions in one line that something is waiting.

When you open it, Claude sorts it the same way it sorts anything else: if it's work to do, it becomes a captured item in your queue; if it's just something worth knowing, it goes in the session record; if it's evidence you'll need to re-read word-for-word later, it's saved as a file. Then the message moves into `INBOX/archive/` so you're not told about it again every session.

Going the other way, Claude will always show you the exact message and wait for your yes before writing it into another project. That's deliberate: a message takes this project's content somewhere else, and either project's folder might be published one day. Setup also asks once whether these messages should be saved into your project's history or kept out of it — keeping them out is the safe default.

One thing this is *not*: the `.throughliner/` folder. That's a live "Claude is typing right now" signal for other apps. INBOX is for messages. They're separate.

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first), and each line ends with the name of that session's full entry file. The entry file holds the detail — files touched, reasoning, captures routed. For design rationale, search the index, then open the named file. Each entry file's name starts with its date (`2026-06-09-…`), so if you browse the LOG folder itself, sorting the filenames in descending order lines them up newest-first — the same order the index reads. That's the mechanical answer to *where* a reason is written down; for what the record of reasoning is actually for, see [Why does the method record the reasoning behind every decision, not just the decision?](#why-does-the-method-record-the-reasoning-behind-every-decision-not-just-the-decision).

## Claude writes things into my docs and then tells me. Doesn't it need my approval first?

It writes first and reports second now, and the report is your approval moment — you can reject anything it wrote and Claude reverts it.

The rule is one question: **does undoing it put things back exactly as they were?** For anything written into a file in your project — a captured idea, a work item, a session record, a change to SPEC.md, an ordinary edit during a build — the answer is yes. Your project is under version control, so an unwanted change costs one revert and nothing else. Claude writes it, then tells you in one line what landed and where, and you read it in the doc where it's going to live anyway.

Two things still get shown to you *before* they happen, because a revert can't fully undo them:

- **Commit messages.** A commit is harder to unwind than a file edit, and the message never becomes part of a file, so there's nothing to read back and nothing to revert.
- **Anything that leaves your machine** — a report sent to the method's author, or a message written into another one of your projects. Once it's delivered, undoing your copy doesn't recall theirs.

The honest trade: under the old flow, text you hadn't agreed to never reached disk at all. Now it briefly does. That's cheap and recoverable — but it does mean the one line reporting what landed is worth actually reading, because the risk isn't you saying no, it's you not noticing. Claude keeps that line specific enough to object to without opening the file.

Why it changed: pasting every draft into the chat and then writing it wrote everything twice, which burns through a session's budget fast, and you ended up reading the same text in two places. This way you read it once, where it lives.

## Why does the method record the reasoning behind every decision, not just the decision?

Because Claude forgets. Every session starts from nothing — Claude has no memory of the last one, and no idea why your project is the way it is. The record of *why* is what carries your intent across that gap. It's the reason a fresh, short, even cheaper session still builds the project the way you meant, instead of reading your files, guessing at the intent behind them, and guessing wrong.

That's worth separating from the thing it sits alongside. Your work *moves* through a pipeline: an idea is captured, discussed and kept, then built. The reasoning is what travels *with* that work and outlives it. Two different things, and the second is easy to miss because the first is the visible one.

It isn't one file, either. Your intent lives in SPEC.md; the reasoning for each piece of work rides along inside that work item in QUEUE.md; the history of what was decided and why lives in LOG/. SPEC and QUEUE are read *while* planning and building — so the reasoning is quietly shaping every plan and every build, not just sitting there waiting for you to ask a question. The LOG is the deep archive, pulled up on demand.

What it buys you, concretely:

- **Settled things stay settled.** When an option was considered and rejected, the reason it lost is on the record. Without that, it gets proposed again in three months and you re-argue a decision you already made.
- **Fewer silent regressions.** You (or Claude) can see *why* something is the way it is before changing it — so the change that would quietly break something gets caught.
- **It survives a break.** Come back after a month away, or hand the project to someone else, and the thinking is still there. That's institutional memory, and it's the thing projects normally lose first.
- **It keeps a growing project coherent.** Recorded intent makes contradictions visible, so drift can be spotted instead of accumulating.

And it steadies Claude, not just you. A rule with its reason attached gets followed more reliably than a bare rule — knowing *why* you want something a particular way is a large part of staying aligned to what you actually want.

## Approving drafts and writing session records feels like overhead. What am I actually getting?

A fair question, and the honest answer is that the cost is real but small and the payoff is large and later.

**The approving is the point, not a tax on it.** A reason you never read and never agreed to is a reason you can't trust when you read it back in six months. Your approval is what makes the record genuinely *yours* rather than Claude's summary of a conversation it half-followed. That's the difference between a record you can rely on and one you have to re-verify.

**The writing pays a small cost now against a much larger one later.** Ten minutes across a session, against the "why on earth did we do it this way?" archaeology that otherwise eats an afternoon — usually at the exact moment you're trying to change something and can't tell whether it's safe.

**And it's what makes short, cheap sessions work at all.** If your intent only exists in the conversation, then every session has to be long enough to rebuild it, and every session has to be with a model good enough to reconstruct it. Once the intent is written down outside the conversation, a short session on a cheaper model can pick up the project and get it right. The record isn't overhead on top of the work — it's what lets the work be done in small, affordable pieces.
