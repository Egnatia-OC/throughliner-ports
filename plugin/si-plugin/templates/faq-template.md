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

## How does Claude show me text it writes into my docs?

Whenever Claude writes something that belongs in one of your project files — a new idea for the list, a session record, a changed piece of wording — it writes it into the file first, then tells you in chat what it wrote: a short summary you can act on, a link to the file with the exact heading to look for, and the question you're being asked. If you want to read the whole thing right there in chat, just say so — the full text is always one word away. The short summary matters because the link isn't perfect: it opens the file at the top rather than at the right spot, so the summary is what lets you decide without going hunting.

## Setup used to ask which editor I use, and whether I work from my computer or my phone. Where did those questions go?

Both were removed, deliberately. The editor question recorded which app you'd open a doc in to edit it by hand — but nothing actually used the answer, since Claude's links open in its own viewer either way. The computer-or-phone question set a "working mode" that decided whether Claude showed you doc text as a link (at your desk) or pasted it into chat (on your phone). In practice that split just made people pick whichever meant less text, so it's gone: Claude now always gives a short summary plus a link, with the full text on request — a shape that works the same at a desk and on a phone. If your CLAUDE.md still has an `Editor:` or `Working mode:` line from an earlier version, it's simply ignored; you don't need to remove it.

## Setup used to ask about my `[user]` steps. Where did that question go?

It was removed, deliberately. Setup used to ask whether you finish the steps only you can do (`[user]` steps) together with Claude, or on your own between sessions — a setting called completion mode. Its only job was to control whether planning sessions asked you, up front, "have you already done any of these?"

That question is gone entirely. Claude no longer asks — in any session, at any point — whether one of your `[user]` steps is already done. It works it out instead: a step Claude just walked you through is done, and a step you mention having finished is done. That's it.

The reason for removing rather than softening it: being asked to account for work you haven't been walked through yet reads as being chased, and the earlier design had already tried twice to make it less annoying (moving it later in the message, adding this setting to switch it off in most projects) without questioning whether it should exist. It shouldn't.

There's one gap, and it's intentional: if you do a `[user]` step entirely on your own and there's nothing for Claude to see, that item stays in your queue until you mention it. Mentioning it is enough — Claude records it and clears it out.

If your CLAUDE.md still has a `Completion mode:` line from before, leave it. It doesn't do anything now and Claude ignores it.

## Why does setup ask which Claude model I use?

Because Claude follows instructions better when they're written for the model that's actually running. The plugin keeps two versions of its own working instructions — a fuller one and a lighter one — and uses your answer to pick. Newer models do better with less spelled out; the older one needs the fuller wording to follow a rule reliably.

You're only ever asked which model you use, never which version of the instructions you want — that's background machinery you shouldn't have to think about. The question is optional; skip it and the safer, fuller version is used, which costs you nothing but some extra words behind the scenes. Change it later by telling Claude.

You might reasonably ask why Claude can't just tell which model it's running. Sometimes it can, and where that information is available it's used and this setting isn't needed. But it isn't always available — in the desktop app it isn't — so relying on it alone meant the whole feature quietly did nothing. Your answer is the reliable source.

## Why does setup check whether my code is public, and what are the licence and publishing questions?

Four related things, and the first two are safety checks rather than preferences.

**Is your repository public?** Claude checks this rather than asking, because an answer typed once goes out of date without anyone noticing. It matters because everything in your project docs gets committed — and a commit is permanent, even if the text is deleted later. If the repository is public, everything written in these docs is readable by anyone, straight away and for good. Knowing that, Claude holds a firmer line about never writing other people's names or private circumstances into your notes, queue, or logs. (It holds that line either way — a private repository can be shared or made public later, and nothing re-checks what's already in it.)

**What email address will your saves carry?** Every save (commit) is stamped with an author email address, and if your project is ever published, those stamps are visible to anyone — they're the one thing that can't be fixed later by editing a file, only by rewriting the project's entire history. So before the very first save, Claude tells you which address yours will carry, and mentions that GitHub offers a free "noreply" address if you'd rather not publish a real one. Changing it at this moment is one line; changing it later is a major operation.

**What licence do you want?** In plain terms: are you happy for other people to use and build on this, or would you rather keep it to yourself? Claude recommends one and writes it as a LICENSE file.

**Do you want this on GitHub?** Offered off the back of the licence choice, and only as an offer — "we can do it now, or note it down for later" is a real answer, not a polite formality. One thing Claude states plainly when offering: most of what a visitor to your repository will find is the planning record itself — your spec, your queue, and your session logs, with every decision and the reasons behind it. Plenty of projects publish exactly that on purpose; it's just a choice worth making with your eyes open rather than by default. If you'd rather the opposite, Claude can also set things up so none of your project docs are ever committed at all.

## Can Claude find things in my notes that shouldn't be public?

Yes — ask for a scrub sweep and Claude will run one. It reads every committed file and reports two things: every occurrence of any name you tell it to look for, which is complete and exhaustive, and a list of other capitalised words that look like they could be people's names, which is a rough list for you to glance over rather than a definitive answer.

Worth knowing up front: **deleting something from a file does not remove it from your project's history.** If a name has already been committed to a public repository, it has been readable, and it stays readable in the history. That's a decision only you can make — rewriting the history, removing it going forward only, or making the repository private — and Claude will lay out the options rather than implying an edit fixes it.

The better protection is the one that runs all the time: Claude doesn't write other people's names or private details into your docs in the first place. A note about what happened never needs them.

## What does `Blocked by:` mean on a piece of work?

It means that piece of work can't start until another piece is finished, and it names which one. You'll see it as a line under the work's description, pointing at another item by its short name.

It exists because the order things sit in isn't enough on its own. Order tells you what comes next; it doesn't remember *why*. So if the queue gets reordered — which happens routinely — a dependency held only by position quietly disappears, and something gets built before the thing it needed. Saying it outright survives any reorder.

Claude checks these for you as an advisory: if a `Blocked by:` line names something that isn't in your queue, or names something sitting *below* it (which reads backwards), you'll see a note about it. It's a nudge, never a block.

There's one near-neighbour, so you don't have to guess. `Blocked by:` is only for waiting on *another item in your queue*. Waiting on anything else — a restart, an event, a decision that's yours, or something needing to be released and running first — is written in plain words in the item's description, and the item sits below the readiness line until that clears.

(If you've used this before and remember a "push marker" between items for the released-and-running case: that's gone. It was a third route that never actually worked — one part of the method placed it and the part that builds ignored it — so work that needed a released version could get built against the old one without anything noticing. The readiness line covers that case now, along with every other kind of waiting.)

## What are the Processed and Unprocessed sections in QUEUE.md?

Your queue has two sections. **Processed** is vetted, ready-to-build work — one item per piece of work, worked top to bottom, discussed and agreed with you during /plan. **Unprocessed** is an inbox — ideas, questions, and tasks captured during builds or between sessions, not looked over yet. During /plan, each unprocessed item gets discussed and either moved up into Processed (kept as real work) or dropped. There's no in-between: a piece of work is unprocessed, processed, or gone.

Every work item carries a short name in square brackets (its slug), so Claude can refer to it precisely. Items you personally raised are tagged "captured by you," and that credit stays on the item even after it's processed; anything else is left unmarked (Claude is assumed to be the author by default, so it isn't labelled as such).

## What does it mean when a work item is marked `[user]`?

It's work only you can do — a check that needs your eyes on the screen, a decision only you can make, or a physical action like tapping *send* or plugging in a device. Everything else is Claude's to build. One thing that is *not* a `[user]` step: work Claude could run itself — a command, an install — that just can't run yet because it's waiting on something (a restart, a push). That stays Claude's to do; it's simply ordered to run once its wait clears, not handed to you. When Claude works down the queue, it builds all its own items first, then walks you through any `[user]` steps at the end. Most items aren't marked — they're Claude's by default.

## When Claude reaches a `[user]` step, do I have to do it alone?

No — a `[user]` step isn't Claude dropping the task on you and stepping back. When Claude reaches one, it *leads* by walking you through it, live: it runs whatever parts it *can* (any commands or setup it can drive), then gives you the **first** step and waits while you do it, then the next, and so on — walking beside you one step at a time, not handing you a list to work alone. Helping you through it in real time is the whole point — it's a walk-through, not a hand-off. The `[user]` tag just marks who has to actually do or witness the step — usually because it needs your eyes on a screen, or a tool Claude can't reach. You're always welcome to say "just tell me what to do and I'll handle it," but the default is that Claude walks you through it, not that you're on your own. If there are several `[user]` steps, Claude takes them one at a time — it won't dump them all on you in one message.

One related detail about *when* these show up: Claude only brings up a `[user]` step once the work it depends on is finished. A step that's waiting on something not built yet stays parked in your queue until it's ready — so when Claude does walk you through one, it's genuinely ready for you to do.

## I did a `[user]` step Claude walked me through. How does it get recorded and cleared?

Once you've finished the step, Claude tells you how to close it out: **run /done to record it**, or **mention it at your next /plan**. Either way, Claude writes it into your session log and removes it from your queue — so a finished step doesn't sit there. This matters because a `[user]` step doesn't clear itself: if nothing records it, the next time Claude works down the queue it would bring you the same step again, as if you'd never done it. Claude never talks about recording or /done *during* the walk-through — that comes only after the last step is done (or you choose to leave it), so the walk-through itself always finishes first. And Claude never asks whether you've already done a step — not at the start, not as a closing aside, not in a planning session. If you *have* already done one, just say so and Claude records and clears it instead of walking you through it. Otherwise it walks you through it. The reason there's no such question anywhere: asking treats work that's ready for you as though it's probably already behind, and makes you push back before Claude will help. The walk-through is the point, so that's what you get.

## What are the build and audit flavors — and is there a separate "test"?

Every piece of Claude's work in the queue carries a flavor that says how Claude carries it out, shown as a small tag at the front of the line:

- **Build** (no tag) — the normal kind: Claude makes changes to your files. Most work is this.
- **`[audit]`** — a review pass: Claude reads something over and reports what it finds, without changing anything. The findings go into your queue for you to look over.

There's no separate "test" flavor. Checking is just part of building: any check Claude can run itself, it runs while building. A check only *you* can do — looking at a screen, tapping through your app — is its own `[user]` work item, which Claude walks you through rather than running. When Claude works down the cleared part of the queue, it builds all its own items first, routing each by its flavor, and then walks you through any `[user]` steps — so a `[user]` step no longer ends the run partway through, and cleared work waiting after it still gets built. (Your planning session usually places `[user]` steps at the end of a run, so in practice the build runs straight through and the walk-through comes last.)

## Why did my audit file its findings as captures instead of writing them into a doc?

Because an audit's job is to find things and route them for review — not to write them anywhere durable yet. Everything an audit turns up goes into Captures, where the next /plan session and you look it over before any of it lands in a real document. That review step is the whole point: it keeps an unchecked finding from going straight into a doc you'll rely on. So if you want a lasting findings document — a report, or a summary for someone outside the project — that document is its own piece of work, built *after* the findings are vetted. The order is: the audit files findings as captures → /plan reviews them with you → a build session writes the document from the ones you kept. And if you happen to set up an audit item that points at a document to write into, Claude won't silently follow it — it'll notice the mismatch and ask which you meant: file the findings for review first, or run it as a build that writes the doc now.

## Where does Claude put research findings and test results?

One of three places, decided by a simple rule so nothing piles up where it doesn't belong. If a finding means there's **work to do**, it becomes a captured item in your queue's Unprocessed list — because it's work. If it's just **a finding or a clean pass** — something worth remembering but not a to-do — it goes into that session's log entry, which is durable and searchable and keeps your queue uncluttered (a test that passed is a finding, not work, so it's logged rather than left sitting in the queue). Only the third kind earns its own lasting file in the project's `resources/` folder: **evidence a future session will need to re-read word-for-word** — for instance a saved transcript that a specific queued item will later be judged against, where the exact wording *is* the evidence. `resources/` is kept for exactly two things — research write-ups and this re-read-later evidence — so it stays useful instead of becoming a junk drawer. So if you notice a finding went into the log rather than a new file, that's why: a file is only created when its exact words will be needed again later.

## Why does Claude sometimes ask me to run a test instead of running it itself?

Because some tests need something only you can provide — and when that's the case, Claude tells you plainly what the test checks, what it needs, and why it can't run it. A test might need you to look at a screen and judge how something appears, tap through your app on a phone, or run a command in a terminal Claude can't reach. Claude usually can't see your setup, so it doesn't guess what you can or can't do — instead it names exactly what the test requires ("needs the terminal," "needs a phone connected," "needs you to look at the screen") and leaves it to you to judge whether that's yours to do. If a test needs nothing of yours, Claude just runs it — handing one to you is only ever for the checks that genuinely need you.

## Claude offered to find a command-line tool to do a task for me. Why?

Because it can often do a job itself with a small command-line tool instead of walking you through doing it by hand in an app — and doing it for you is usually faster and less error-prone. So before handing you a step-by-step for a desktop app, Claude pauses to consider whether a tool exists that would let it just do the task (things like reading text out of a scanned image, converting a PDF, or reshaping a data file often have one). When it thinks one might but isn't sure which, it offers to look one up on the web. You're never obliged to say yes: decline and Claude falls back to guiding you by hand. And the usual safeguards still apply — Claude names the tool and what it's for rather than installing things blindly, asks before downloading or running anything, and won't assume you have a terminal or the right setup; it names what a tool would need and lets you say whether that fits. The reason it offers this on its own is that a lot of these tools aren't things a non-coder would know to ask for — so the option shouldn't depend on you knowing it exists.

## Do I need to use the terminal to install or update SI?

No. The plugin installs and updates through Claude Code's own plugin system, and **Claude runs those commands for you** — you just ask it in plain English inside a Claude Code chat. You never open or type into a terminal. "Marketplace" and "CLI install" sound technical, but in practice they mean: Claude Code knows where to find this plugin (a marketplace is just the published location on GitHub), and it fetches and installs it with a couple of commands it runs itself. To install, you ask Claude Code to add the `FlintCraftTech/sovereign-implementer` marketplace and install `sovereign-implementer@flintcraft`; to update later, you ask it to run the update. Either way it's Claude doing the typing, then you fully restart the app so the new version loads.

## How do I find out when there's a new version of the plugin?

GitHub can email you whenever a new version of Sovereign Implementer is published. Go to the plugin's page at `https://github.com/FlintCraftTech/sovereign-implementer`, click **Watch** near the top right, choose **Custom**, tick **Releases**, and click **Apply**. After that you get an email each time a new release goes out. It needs a free GitHub account, which costs nothing to set up.

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

Yes. For readable changes — a doc, a piece of copy, a section of your spec, anything you read rather than run — Claude surfaces the change right after making the edit: a short summary of what the new wording does, plus a link to the file naming the section that changed, with the full new text shown in chat whenever you ask. So you meet the real words, not just the plan for them. (Code changes aren't shown this way; reading raw code back wouldn't tell a non-coder much.) The exact wording is written while building, so this is your first look at the real words, not just the plan for them. If something's slightly off, you can ask for a small tweak on the spot — "change this one bit" — and Claude adjusts it there and then, as part of the same build, no separate step. Only a genuinely new or bigger change — a different feature, or reworking something that already worked — waits for its own session.

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

## A session opened by saying my project was missing something — what happened?

The plugin keeps improving after your project is set up, so a project can end up missing a setting the method has since added. At the start of a session, before /plan or /next, Claude checks for this and catches the project up — adding only what's missing, and never rewriting or clobbering anything you've written. A setting that needs an answer from you gets asked in one line, and you can say to skip it; settings that need no answer are just added, with a note telling you what changed. This only ever adds; if something already in your docs is out of step with a new version, that's a separate change you'd make deliberately.

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

## In a planning session, Claude asked permission to change a file. Why?

Planning sessions are for talking things through and shaping your queue, so they normally only touch a few files: your queue, your spec, your session log, and Claude's own working notes. Those go through without interrupting you.

Anything else, Claude asks about first — naming the file — and you say yes or no.

The reason it asks rather than refusing: a planning session sometimes has a genuinely good reason to change something. You spot a problem that needs fixing now rather than in three sessions' time. You ask Claude to tidy a file while you're both looking at it. Something is exposed and shouldn't stay exposed for another day. Blocking those would just get in your way.

But equally, a planning session quietly rewriting parts of your project isn't something that should be able to happen without you noticing. So the prompt splits the difference: nothing is forbidden, and nothing happens unremarked. **Declining is a completely normal answer** — it usually just means "capture that as a work item and build it properly later."

If you approve something out of the ordinary, Claude also notes it in the session log, so there's a record of what was changed outside the usual shape and why.

## What does a "Plan session here" line in the queue mean?

It's a planning checkpoint Claude placed between work items. When /next reaches it, /next stops and tells you a planning session is needed first, naming the reason — usually because the next work depends on a decision, or on findings that only get sorted out in /plan. Run /plan: it handles the named reason and removes the line, and then /next can carry on. You don't add these yourself — Claude places them when it sees a planning moment coming.

## I have work sitting below the "cleared to run" line, waiting on something. Will Claude come back to it?

Yes. When a piece of work is parked below the line because it's waiting on something — a step you have to do, another piece of work being finished and checked, a restart — Claude records right there in the item what it's waiting for ("once X is done", "after a restart"). Then at the start of every planning session, Claude goes back over everything parked below the line and re-checks those conditions. Anything it can confirm by itself — a piece of work that's now finished and verified, a file that's now there — it offers to move up above the line so it's ready to build. Anything only *you* can confirm — did the restart happen, did you set the thing up — it rolls into a single question asked once, rather than pestering you item by item. The point is that parked work gets picked back up when its wait actually clears, instead of relying on you to remember it was there.

## I told Claude "not now" about something. Why did it stop coming up — and will it come back?

When you set something aside — you stop partway through a step, tell Claude to shelve a suggestion, or answer "no change" about something the work was waiting on — Claude records that on the item itself, quoting your words and noting how far things got. From then on it stops re-offering that item in its recommendations and check-ins, so you're not asked the same thing every session. Two guarantees keep this safe. Nothing is lost: the work stays exactly where it is in your queue, and it comes back up on its own when the queue has nothing else left to offer — or the moment you mention it yourself. And warnings never go quiet: a security concern or an unaddressed risk keeps surfacing until it's dealt with, no matter how often it's waved off. One more thing worth knowing: Claude never sets anything aside on its own judgment — only your say-so does it. If you stopped a step partway, the recorded progress means a later session picks up from where you left off rather than starting over.

## What does the "Cleared to run above this line" marker in the queue mean?

It's a line Claude keeps in your queue showing which work is ready to build. Everything above it has been vetted in planning — discussed and agreed with you, and ready to build next. Everything below it still needs a planning pass before it's ready. Claude positions the line at the end of every planning session and tells you where it sits, so you never have to work out for yourself how much of the queue is safe to run. When /next runs several ready items in a row, it stops at this line — a clean finish, rather than running on into work that hasn't been vetted. You don't manage the line; Claude does.

## Why did /next stop before finishing everything?

Because it hit a wall on one item and stopped rather than spinning on it. When /next works down your cleared queue, it watches the item it's building for signs of no progress — the **same error** coming back, an edit that **changes nothing**, or the **same check failing** the same way, roughly three times on one item. When it sees that, it stops and tells you plainly what repeated (the exact error, or what wouldn't change), and hands you the decision, instead of burning the rest of the run thrashing on something stuck. Since /next often runs faster than you're watching, this stop is what keeps a stuck item from quietly wasting the whole session. It's not a failure of your project — it just means that one item needs a human look before it can go further; the items already finished before it are safe, and you decide how to handle the stuck one from there.

## How does a planning session work through my unprocessed ideas — can I skip or drop things?

Yes, both, and it's built to keep you moving rather than grinding through every item in order. When /plan starts on your unprocessed queue, it does two quick things first. It skims for items that are clearly not worth doing any more — a duplicate, or something whose reason has passed — and shows them to you as one short list to drop together; you just name any you'd rather keep. (This pass can only *drop* things, never quietly promote them — anything that isn't an obvious drop gets discussed properly, one at a time.) Then it puts the items that would unblock the most other work first, and suggests roughly how many to get through this session.

After that it goes through the rest one at a time. At each step you can carry on to the next item, **skip** the next one to the bottom of the queue for a later session (it's not dropped — just set aside), close out, or raise something new. And if you toss in a fresh idea mid-session, Claude files it and asks whether you want to dig into it now or keep going through the queue — so a new thought never feels like it got parked and forgotten.

Claude may also *suggest* skipping an item itself: if a piece of work turns out to be too big or too unsettled to pin down into something buildable this session, it'll propose noting down whatever you worked out and setting the item aside for a later planning session, rather than grinding on it. There's no special "give this its own session" mode — setting it aside to the bottom of the queue *is* how something gets deferred, and next time it comes back up as an ordinary item.

## Why did Claude reorder my queue at the end of a planning session?

At the end of a planning session, Claude checks whether either section of your queue needs reordering and, if so, puts it in the order that makes the most sense for working through it. It doesn't re-sort from scratch every time — it looks at what changed that session and only moves things when the current order is actually wrong, so a session that didn't disturb the order leaves it untouched and says nothing. For unprocessed items, it puts the one that would unblock the most other work first — so processing it moves the most things forward. For processed items, it puts the one that should be built first — the one whose output is needed by later work — at the top, so you're not building something that depends on something you haven't done yet.

Claude owns this ordering and does it on its own — it tells you what it moved and why, but doesn't ask permission. That's because ordering is low-stakes and easy to undo (just say "move X back above Y"), and asking about every reorder would add ceremony to every planning close. The narration is the catch-point: if Claude moved something you disagree with, say so and it adjusts. A reorder that changes what gets built *next* is flagged clearly; a small tidy gets a one-line note.

## Claude merged two pieces of work together without asking me. Is that allowed?

Yes, within a strict boundary. When two agreed pieces of work belong together, merging them changes *where* the work is recorded, not *what* gets built — so if the merge doesn't add any files to what the next build is allowed to touch, Claude just does it and tells you, naming the scope effect in the same breath ("this adds no files"). If a merge *would* add files — meaning the build would reach further than what you agreed — Claude still asks first. You can always object to a narrated merge; saying so un-merges it. Relatedly, planning sessions prefer to group work that touches the same files so one build session can clear more at once — but that's only a tie-breaker: work never jumps the queue or skips vetting just because it touches the same file as something else.

## Claude tidied up the queue while committing, without asking me. Is that normal?

Yes. Some queue housekeeping is Claude's to handle on its own — clearing a "waiting on" note once the thing it was waiting for is done, or fixing a pointer to a section that has moved. These change nothing you decide: they drop no work, reorder nothing, and don't alter any choice you've made — they're bookkeeping on entries that are otherwise fine. So Claude makes the fix and tells you it did, as part of the commit, rather than stopping to ask. Anything that's a real judgment call — dropping an item, rewriting it, or deciding whether to keep it — still waits for a planning session and your say. You always see what was tidied; you just aren't asked to approve the routine kind.

## Something about the method itself is broken or confusing — where does that go?

Not into your project's queue — that queue is for your app, and a note about how Sovereign Implementer *itself* behaves would just clutter it. Method problems go to the plugin's author instead. If you hit one — a command doing something odd, a step that doesn't make sense, or a question this FAQ doesn't answer — tell Claude, and it drafts a short report you can send. Claude can also spot a method problem itself mid-session and offer once to draft the report. The report is scrubbed by design: it describes what the plugin did, which step, and the version — never your app's name, your files, or any secrets. Claude shows you the report and you paste it at flintcraft.tech/report yourself; Claude never sends it for you, so nothing leaves your machine without your eyes on it first.

There's a third case: the problem is in **Claude Code itself** — the app the method runs inside, its viewer, its links, its sidebar — rather than in the method or your app. Those reports belong with Claude Code's makers, as an issue on their public GitHub project. Claude first searches the existing issues (if yours is already reported, adding your experience to that issue helps more than a duplicate), then drafts the issue text and shows it to you in full. If your computer has GitHub's command-line tool signed in, Claude can post it for you — only after you say yes to the exact text; otherwise it hands you the text to post yourself. Same scrubbing rule as always: the report describes the problem without exposing your project's names, files or secrets.

So the routing test has three answers: about what you're *building* → your queue; about how the *method* works → flintcraft.tech/report; about *Claude Code the app* → a GitHub issue. If it's genuinely unclear which, Claude asks rather than guessing. (Claude Code's built-in `/bug` command reports to Anthropic privately — the GitHub route is used instead because it's public and trackable, and never for method problems, which belong to this plugin's author.)

## Why is there a "Last session advises…" line at the top of my queue?

That's a forward-recommendation note — the previous session's suggestion for where to focus next. It's there so you don't have to remember what the last session recommended; the recommendation sits right where the next /plan session sees it first.

It's advice, not a command. When you run /plan, Claude reads it, mentions what it says, and lets it inform where you focus — but you're free to go a different direction. Once you and Claude have agreed on the processing or build order for the session, the note is deleted automatically. It never moves into Processed and is never treated as real work — it's a one-time orientation handoff that disappears once it's done its job. If no note is there when you start /plan, nothing was recommended — the last session's close didn't have a specific suggestion to make.

## Claude offered to delete some files when I closed a session. What's that?

When you close a session with /done, Claude offers to clean up throwaway files it made during that session — a scratch file, a one-off working file with no further use. It only ever offers files *it* created this session that have no future purpose, it asks about each one singly, and it never deletes anything without your yes. It won't touch files you made yourself — those are treated as your own work, never as rubbish. When a file is tracked in your project's history, Claude says so (you could get it back if needed); when it isn't tracked, or it's outside your project, Claude warns you the deletion is permanent before you approve. Most of the time there's nothing to clean up, because Claude writes its temporary files to a scratch area outside your project in the first place — so they never land in your folder, and they clear themselves.

## Why did Claude split my project into several files (or keep it in one)?

When Claude builds, it recommends how to divide your project across files by a simple rule: split things that are genuinely independent — a self-contained tool, a standalone screen — into their own files, but keep things that have to be understood together in one file. The reason is that Claude does the editing. When each piece lives in its own file, a change touches just that file, Claude reasons over less at once, and a mistake stays contained instead of spreading through the whole project. The flip side is that Claude works less well when closely related logic is scattered across files, so tightly connected parts stay together even if that file grows large. It's a recommendation, not a rule — you can always ask for a different structure.

## What is the filed-after note on one of my captured items?

When Claude captures an idea into your queue, it tags it with the last save-point that existed at that moment — shown as a short "filed after …" note. It's a rough marker of *when* the item was captured. It matters most for ideas captured after a session was already recorded and saved, so there's still a trace of roughly when they came up rather than the timing being lost. You don't need to do anything with it — it's bookkeeping that helps place the item in time later.

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first), and each line ends with the name of that session's full entry file. The entry file holds the detail — files touched, reasoning, captures routed. For design rationale, search the index, then open the named file. Each entry file's name starts with its date (`2026-06-09-…`), so if you browse the LOG folder itself, sorting the filenames in descending order lines them up newest-first — the same order the index reads.

## Does it matter which Claude model I'm using?

Not for anything you have to do. The plugin ships two versions of its own instructions — a fuller one and a lighter one — and works out which to use at the start of every session, from the model you're running. There's no setting for it and no message about it.

Both versions describe the same method: the same four commands, the same queue, the same rules about what Claude will and won't do without asking you. The only difference is how much explaining sits around each rule, because different Claude models follow instructions best at different lengths. So your project behaves the same way whichever model you build it on, and switching models between sessions is fine.

If the plugin can't tell which model is running, it uses the fuller version — the one it's been tested on longest.

## Why won't Claude ask me for my email address, account numbers, or other personal details?

Everything written into your project's planning docs gets saved into your project's history — and if your project is ever shared or made public, that history goes with it, even for text that was later deleted. So the method keeps sensitive details out of the docs in the first place, in three ways.

First, Claude doesn't write other people's names or private circumstances into your docs — "a client", "a third party" carries the same point without the exposure. Second, Claude doesn't *ask* you for sensitive identifiers — email addresses, account numbers, keys, payment details — when writing up a piece of work. A work item like "fix the account that's under the wrong email" is complete without the actual addresses: you'll have those to hand when you do the work, and they never need to sit in a saved doc. Third, when Claude records something about you — say, why a piece of work was set aside — it writes the decision and its reason ("set aside: needs specialist help"), not a personal assessment of you.

If a detail like that genuinely is needed for the work itself, you can always give it — this is about Claude not soliciting it into documents that keep it forever.

## Claude asked me something but I couldn't see how to answer it. What happened?

Claude Code sometimes puts suggested replies in your typing box — faint grey text you can accept with the Tab key. They're generated by the app from the conversation, not written by Claude as part of its message. That matters, because they don't always appear: they're switchable off, they're reported to stop showing up for some people, and they don't render at all when you're driving a session from your phone or another device. So an answer that lived only in a suggestion simply isn't there for you.

The method now requires every question Claude asks you to be answerable from the message itself. Where there are two ways to reply, both are named in the text — "tell me any numbers to drop, or say keep them all" rather than just the first half. You should never have to guess the other option, and you can always just say what you want in your own words; the named replies are there to save you thinking about it, not to limit what you can say.

If you do hit a question you can't see how to answer, saying so is a fine reply — Claude will restate it. And it's worth reporting, since it means a question somewhere is still leaning on the suggestions.
