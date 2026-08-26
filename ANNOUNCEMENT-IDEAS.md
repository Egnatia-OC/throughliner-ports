# Announcement ideas — post source material

The retired FAQ's entries, retooled as raw material for Discord announcements
([faq-reseed-from-announcements], 2026-08-24). Each section below explains one
piece of Throughliner behaviour a user meets; a post drafted from one turns it
into an announcement or a teaching post, subject to the standing Discord rules
in CLAUDE.md (announce only what has shipped, the 2,000-character limit, Alex
posts everything). When an announcement is posted and its line lands in
`INBOX/sent.md`, its FAQ entry is authored in the same turn — that is how the
fresh FAQ refills — and the section it drew on can be trimmed or deleted here.

The headings keep their question form because a question is already a post
angle; nothing below is required to survive as written.

## Why doesn't my session log's index grow forever?

(Added by the [log-retrieve-search-leg] build, after the FAQ moved to
announcement-driven entries.) The log index is split by month — the current
month's lines stay in `LOG/index.md`, and each completed month's move into
their own `LOG/index-YYYY-MM.md` file at the close that first touches the index
in a new month. When Claude needs an old decision it searches the index files
for the subject's words rather than reading them whole, so the archive can grow
without any single read growing with it. The trade is stated: a search finds
lines carrying the words tried, so an entry indexed under different phrasing
can be missed where reading everything could not miss it — which is why the
lines newer than the last planning session's own record are still read
unprompted at each planning opening.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top work item and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## How do the four commands fit together day-to-day?

You run **/setup** once, right at the start of a project. After that, every working session is either **/plan** (thinking and organising — managing the queue, adding ideas, resolving questions) or **/next** (building — it picks the top item and does it). You'll run /plan as often as planning needs, and /next once per item as you work down the queue: planning repeats for long stretches, building repeats across many items. However a session goes, it ends the same way — **/done** to record what happened, then **/clear** to start fresh. The one habit that matters: always /done before /clear, so each session is saved before the context resets.

## What does /setup do, and do I run it more than once?

/setup adopts your project folder into the method: it scaffolds the working docs (SPEC.md, QUEUE.md, the LOG folder, and this FAQ) and interviews you to fill in SPEC.md — what the project is, who it's for, how it works. The interview adapts to your answers rather than running a fixed list of questions: Claude reads each answer, asks the next thing that actually matters, suggests an answer you can just react to, and keeps going one question at a time only until there's a clear enough picture to build from. It's not an interrogation — you can stop it any time by saying "build from what we have," and Claude writes the docs from whatever you've covered. If your folder already has something in it — an old doc, a sketch, a running app — Claude reads that first and asks about what's still unclear, instead of asking things the material already answers. You run it once per project. If you run it again later — for instance after a plugin update — it only backfills scaffolding that's missing; it does not overwrite or reconcile content you've already written. So re-running it is safe, but it won't refresh or rewrite your existing docs.

## Can I keep several projects in one folder, and what if I open the wrong one?

Each Throughliner project is its own folder — self-contained, with its own SPEC, QUEUE, and log. You can keep several of them side by side (for instance nested under one parent folder), but they stay separate projects; the method doesn't run one project across many folders. Claude always works on the exact folder you opened the session in, and never goes hunting through nearby folders or asks you to pick one — the folder you point it at is the project. So to work on a particular project, open that project's folder directly. If you accidentally open a parent folder that just contains your projects, Claude notices and tells you: it says the folder looks like it holds separate projects and suggests you open the one you meant, because running /setup there would set up the parent folder itself rather than the project inside it. Nothing gets adopted or changed until you choose — the heads-up is only so you don't set up the wrong folder by mistake.

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

Every entry in your queue carries a short name in square brackets (its slug), so Claude can refer to it precisely — captures included, from the moment they're filed. Items you personally raised are tagged "captured by you," and that credit stays on the item even after it's processed; anything else is left unmarked (Claude is assumed to be the author by default, so it isn't labelled as such).

## Can more than one person work in a session — say, a teammate sitting in?

Yes. Anyone present can add ideas: captures go into the Unprocessed section, which is un-vetted by design, so a participant's idea lands there safely and gets weighed at the next planning session like any other. What stays with one named person — whoever holds the authority to run the project — are the decisions that change state: keeping or deleting work, expanding a build's scope, clearing a privacy or security risk, and approving anything that leaves the machine. In a shared session, that one person's yes is what counts for those; everyone else's ideas still get in, they just get in as captures.

## What does it mean when a work item is marked `[user]`?

It's work only you can do — a check that needs your eyes on the screen, a decision only you can make, or a physical action like tapping *send* or plugging in a device. Everything else is Claude's to build. One thing that is *not* a `[user]` step: work Claude could run itself — a command, an install — that just can't run yet because it's waiting on something (a restart, a push). That stays Claude's to do; it's simply ordered to run once its wait clears, not handed to you. When Claude works down the queue, it builds all its own items first, then walks you through any `[user]` steps at the end. Most items aren't marked — they're Claude's by default.

## When Claude reaches a `[user]` step, do I have to do it alone?

No — a `[user]` step isn't Claude dropping the task on you and stepping back. When Claude reaches one, it *leads* by walking you through it, live: it runs whatever parts it *can* (any commands or setup it can drive), then gives you the **first** step and waits while you do it, then the next, and so on — walking beside you one step at a time, not handing you a list to work alone. Helping you through it in real time is the whole point — it's a walk-through, not a hand-off. The `[user]` tag just marks who has to actually do or witness the step — usually because it needs your eyes on a screen, or a tool Claude can't reach. You're always welcome to say "just tell me what to do and I'll handle it," but the default is that Claude walks you through it, not that you're on your own. If there are several `[user]` steps, Claude takes them one at a time — it won't dump them all on you in one message.

One related detail about *when* these show up: Claude only brings up a `[user]` step once the work it depends on is finished. A step waiting on something not built yet sits below the "cleared to run" line, naming the item it's waiting for, until that item ships — so when Claude does walk you through one, it's genuinely ready for you to do.

## I got partway through a `[user]` step last time. Will Claude make me start over?

No. Before walking you through a step, Claude checks your session logs for any record of it — a walk-through that got interrupted, or one you finished part of in an earlier session. If a record exists, Claude says which parts it shows were already done and picks up at the first one that isn't, rather than marching you through the whole list again.

## Why did Claude walk me through a step in the middle of a planning session?

Usually a step you're walked through comes up when Claude works down the queue. But sometimes, during planning, a step gets written into your queue and doing it *right now* would clear a privacy risk or unblock the very work the session is doing. In that case Claude may walk you through it on the spot, while you're there. The step is always written into the queue first, before anything starts — so if the walk-through gets interrupted, the step is safely on the list and picks up later instead of vanishing with the conversation.

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

## Do I need to use the terminal to install or update Throughliner?

No. The plugin installs and updates through Claude Code's own plugin system, and **Claude runs those commands for you** — you just ask it in plain English inside a Claude Code chat. You never open or type into a terminal. "Marketplace" and "CLI install" sound technical, but in practice they mean: Claude Code knows where to find this plugin (a marketplace is just the published location on GitHub), and it fetches and installs it with a couple of commands it runs itself. To install, you ask Claude Code to add the `FlintcraftTech/throughliner` marketplace and install `throughliner@flintcraft`; to update later, you ask it to run the update. Either way it's Claude doing the typing, then you fully restart the app so the new version loads.

## How do I find out when there's a new version of the plugin?

GitHub can email you whenever a new version of Throughliner is published. Go to the plugin's page at `https://github.com/FlintcraftTech/throughliner`, click **Watch** near the top right, choose **Custom**, tick **Releases**, and click **Apply**. After that you get an email each time a new release goes out. It needs a free GitHub account, which costs nothing to set up.

## I just updated the plugin — how do I check it still works?

You don't have to do anything special. Just carry on using it — run your normal /plan, /next, and /done sessions — and if something behaves oddly, you'll notice it in the moment and can have Claude capture it as work to fix. There's no set-aside list of post-update checks to work through, and no separate testing session to run.

The one exception is a check that genuinely can't be done except by you — looking at a screen, tapping through your app, running something in a place Claude can't reach. When a piece of work needs a check like that, it's written into your queue as its own `[user]` item, so it's already waiting for you there rather than resting on you to remember it. Everything Claude can check itself, it checks while building — so most updates need nothing from you at all.

## What is the "build stamp" the plugin records at the start of a session?

A short fingerprint of the installed plugin's own files — a content check that reflects exactly what's installed right now, not just a version number. Its job is to tell whether a plugin update is genuinely in place after you reinstall. Some behaviour can only be confirmed once an update is actually live, and a version number alone can miss a change that didn't bump the version — so the stamp gives Claude a reliable yes/no on whether the installed files are current. It runs behind the scenes: you don't see it or manage it, and nothing about your own project goes into it — it only fingerprints the plugin's files.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. The build's working file tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Is it safe to clear the conversation or start a new session between steps?

After /done, yes — everything is recorded in the session log and committed, so a fresh conversation loses nothing. Before /done, the plugin can still recover: it reads that conversation's own working file rather than relying on the conversation itself, so an interrupted build or planning session picks up from the file. But closing with /done first is the clean habit — it's the moment the work becomes a permanent record instead of something the plugin has to reconstruct.

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

## What is the `_build-...md` file? Should I edit it?

The active build's working file. It does four jobs: carries the work item being built (so QUEUE.md stays free while the build runs), lists which files the build may change (the plugin's safety check blocks edits to anything else), ticks off finished steps (so an interrupted session can resume without redoing work), and keeps the item's reasoning (so /done can write the session record). Claude manages it — don't edit it. Deleted when /done closes the session; if it exists at session start, a previous build was interrupted and /next will offer to resume.

**The jumble of characters in the name is the session's own id**, so the file is `_build-<something>.md` rather than plain `_build.md`. Each conversation gets its own. That matters if you ever run two conversations at once — a planning chat alongside a build, say. With one shared file, the planning chat would see the build's file, decide it was inside that build, and apply the build's list of allowed files to edits you never agreed to. With one file per conversation, that can't happen.

**If a working file is left behind by a conversation that never closed, Claude tells you at the start of the next session** and never deletes it. A working file can hold the only record of what a crashed session actually did, so throwing it away could lose real work. Run /done if you want what it records written up and committed.

## Why did /setup rewrite part of my CLAUDE.md, and is my own text safe?

The top part of your project's CLAUDE.md sits between two marker lines that say "PLUGIN-MANAGED". Everything between those markers is the method's own description of how your project docs work — and that text goes stale as the plugin improves, which matters because every session reads it as current.

So when you run /setup to bring a project up to date, it compares that region against the plugin's current wording. Where they differ, it tells you what it's replacing and swaps in the current text.

**Your own text is safe.** Anything found between the markers that isn't the plugin's — lines you added yourself — is moved below the end marker rather than deleted, and /setup says so when it does it. Everything below the end marker is yours and is never touched. If you want to add your own rules, put them below the end marker to begin with, and they'll never be involved in a refresh at all.

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

Here's what actually happens. Two things run. A mechanical scan looks at QUEUE.md, SPEC.md and your log entries for things *shaped* like credentials — a private key, an API token, an email address. That scan is exact: it either matches a known shape or it doesn't, so it never guesses and never gives you false comfort. Separately, before writing a new item or a log entry, Claude reads what it's about to write against a short list — personal names, details that identify a real situation, other people's information, paths with someone's name in them — and rewrites what it spots. One case is written the other way: a collaborator or other third person appears by the identity they have published on GitHub — their username, pronouns where they've supplied them, first name only where they put it there — never by a private name; anything they haven't published is rewritten away like everything else.

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

## In a planning session Claude wouldn't edit a file and put it in the queue instead. Why?

Because a planning session is for deciding what to do, and changing a file is doing it. Claude is only allowed to write a small fixed set of files while planning: your queue, your SPEC, your session records, any research notes, and its own scratch files. Anything else is refused outright, and the change becomes a piece of work in your queue.

**This used to be a question and now it's a refusal, which is the whole change.** Claude used to ask — "I'd like to edit this file, go ahead?" — and you'd say yes, and the edit happened. The problem with that is quiet: an approval request you skim and wave through isn't really consent, and after a few of them nobody is reading the question at all. A refusal can't be skimmed.

**What it costs you.** A change that genuinely does need making right now takes longer: instead of one word, it becomes an item in your queue, and it gets built in a build session. That's a real cost and it's the intended one — the stop is what makes the change visible to you as a decision rather than passing by as a detail.

**What to do when it happens.** Claude will tell you in plain words what it was about to change and why. If it's something you want, it goes into the queue and a build session does it — usually the very next one. If it's urgent, say so: you can close the planning session and start a build.

**Nothing is lost.** The refusal never discards work. The change is written down as an item with the reasoning attached, exactly like anything else you decide during planning.

## Will Claude use my phone or another device to test my app?

Only if you say yes. Some checks need a real device or emulator — installing the app on a phone, tapping through a screen. Before Claude connects to or tests on any device attached to your computer, it asks your permission first and waits for your answer. It won't reach into your hardware silently. And if no device is connected, Claude asks whether one is available rather than guessing — so a check that needs a device doesn't quietly get skipped or run behind your back.

## What's a "red flag," and what do cleared and uncleared mean?

A red flag is how Claude surfaces a risk to your data or your users' data — anything that could expose private information or amount to a security breach. Claude watches for these in every session, and when it spots a genuine one, it tells you plainly rather than quietly working around it or building past it. The risk then goes into your queue as an ordinary piece of work, marked with a red-flag tag and one of two states:

- **Uncleared** — the risk still stands, and nothing's been decided about it yet. An uncleared flag sits in the "not yet fully processed" part of your queue; it's surfaced first each session until it's dealt with.
- **Cleared** — the risk has been dealt with, one of two ways: either it was **designed out or fixed** (the work no longer carries it), or you **heard it spelled out and chose to go ahead anyway**. Which of the two it was is written into the session log — for an acceptance, that's the record of what you were told and that you agreed, the trail that protects you if the risk ever surfaces later.

Clearing a flag happens when you and Claude work through the item in planning — a piece of work only becomes "ready to build" once its flag is cleared. If a risk can't be cleared yet, its item stays in the "not yet fully processed" part of the queue rather than moving to "ready" — so a risk is never quietly shelved.

It's tagged onto the queue entry carrying the work rather than kept in a separate "risks" list, and that's deliberate: a standing risk list would look like a promise that Claude tracks every possible risk to your project, which no tool can honestly make. The tag only ever marks the risks Claude actually noticed — real ones, surfaced so you can decide what happens next.

## What happens to a red flag when the work carrying it is built?

By the time a red-flagged piece of work is ready to build, its flag has already been cleared — that happened back in planning, when you and Claude decided how the risk was handled and recorded it in the log. So when the work is built and committed, Claude just carries that cleared flag through into the session log; the risk was never left hanging. A red flag never quietly disappears, and it never lingers as a leftover reminder with no work left to do.

One detail worth knowing: a risk counts as cleared the moment it's designed out or you accept it — even if a fix still needs a real-world check to confirm it works. That leftover check becomes its own `[user]` item in your queue — a normal thing for you to verify later — rather than keeping the flag hanging. So "fixed, with a check still to do" shows up as a cleared flag plus a waiting check, not as an unhandled risk.

## Why did Claude ask before starting a "subagent"?

A subagent is a separate helper Claude can spin up to go off and work on something on its own — handy for wide, open-ended research. The catch is cost: a subagent burns through usage fast, and a single run that fans several out at once can use up your session's usage in one go. So before Claude starts one, the method stops and asks you first — a prompt saying Claude wants to start a subagent, which you approve or decline. Declining is completely fine: Claude just does the work directly instead, which is usually all that's needed. The prompt exists so a subagent can never quietly run up a big cost without you knowing — you always get the choice.

## I remember lines in the queue saying "Plan session here" or "Push required". Where did they go?

**They're gone, and nothing replaced them in the same shape.** They were markers Claude put between pieces of work to make /next stop — one to force a planning session, one to force a release. If you have an old queue that still carries either, they no longer do anything and can be deleted.

Two things do their jobs now, both better:

**Whether work is ready is settled before it ever reaches /next.** Ready work sits above the `--- Cleared to run above this line ---` line, and that line is set during planning. If something isn't ready, it doesn't go above the line, so there's no need for a marker telling a build session to stop at it.

**Work waiting on other work names what it's waiting for.** A held item carries a line reading `Blocked by:` and the other item's name — or several names, where it waits on more than one thing, in which case it stays held until they are all done. That survives things a marker doesn't: reorder your queue and a positional marker ends up pointing at the wrong place, while a named reference still says exactly what it meant.

## I have work sitting below the "cleared to run" line, waiting on something. Will Claude come back to it?

Yes, and there's only one reason work can be sitting down there: **other work in your queue has to happen first.** Claude writes that other work's name right into the held one — a line reading `Blocked by:` followed by the name in square brackets — so what it's waiting for is never a vague note, it's a specific piece of work you can look at. Where a piece of work waits on **several** things, the line names all of them, separated by commas, and the work stays held until every one of them is done. That matters because naming just one of them would set the work loose the moment that one finished, with the rest still outstanding.

That matters more than it sounds. Work often waits on something in the world rather than on other work — a restart, a website going live, somebody getting back to you. Those don't get written as a waiting-note inside the held item; they get written as **their own item in your queue**, which means they turn up in planning like everything else and actually get done. The old way buried them as a sentence inside another item, where nobody ever saw them — one piece of work sat waiting for weeks on a step that was never going to happen, because nothing had put that step anywhere you'd find it.

Then at the start of every planning session, Claude goes down the held work and checks one thing per item: has the thing it's waiting for been finished? If yes, Claude offers to move it up above the line so it's ready to build. If not, it stays put and Claude says nothing about it — no repeated questions, because there's nothing to ask you: the answer is in the record, not in your memory.

## What does the "Cleared to run above this line" marker in the queue mean?

It's a line Claude keeps in your queue showing which work is ready to build. Everything above it has been vetted in planning — discussed and agreed with you, and ready to build next. Everything below it still needs a planning pass before it's ready. Claude positions the line at the end of every planning session and tells you where it sits, so you never have to work out for yourself how much of the queue is safe to run. When /next runs several ready items in a row, it stops at this line — a clean finish, rather than running on into work that hasn't been vetted. You don't manage the line; Claude does.

## Why did /next stop before finishing everything?

Because it hit a wall on one item and stopped rather than spinning on it. When /next works down your cleared queue, it watches the item it's building for signs of no progress — the **same error** coming back, an edit that **changes nothing**, or the **same check failing** the same way, roughly three times on one item. When it sees that, it stops and tells you plainly what repeated (the exact error, or what wouldn't change), and hands you the decision, instead of burning the rest of the run thrashing on something stuck. Since /next often runs faster than you're watching, this stop is what keeps a stuck item from quietly wasting the whole session. It's not a failure of your project — it just means that one item needs a human look before it can go further; the items already finished before it are safe, and you decide how to handle the stuck one from there.

## Why does a planning session open by asking what I want to prioritise?

Because the order you work through your ideas in changes how much you get out of the session, and you're the only one who knows if something is urgent today.

The opening has two parts. First, if anything in your queue is obviously not worth doing any more — a duplicate, or something whose reason has passed — Claude shows those as one short numbered list to drop together, and you name any you'd rather keep. That comes first because there's no point deciding the order of things that are about to be deleted. (If nothing is obviously droppable, this part doesn't happen at all.)

Then one question: anything you want to prioritise, or shall Claude pick the order? The default is that Claude picks — working through a few sensible orders on its own, like starting with the item whose answer frees up the most other work, or with decisions that clear the pile down — and then says in one line which order it used. So you can just say go. But if something has become urgent, or you woke up thinking about one particular idea, saying so here is what puts it first.

There's one exception: if your queue holds an unaddressed privacy or data-exposure risk, the question changes shape. Claude leads with that risk as what comes first, and asks only whether anything else is definitely more important — a risk shouldn't quietly lose its place to an ordinary idea.

## How does a planning session work through my unprocessed ideas — can I skip or drop things?

Yes, both, and it's built to keep you moving rather than grinding through every item in order. The session opens with the drop list and the ordering question (see [the previous answer](#why-does-a-planning-session-open-by-asking-what-i-want-to-prioritise)), then it orders the items (naming the order it picked), and suggests roughly how many to get through this session.

After that it goes through the rest one at a time. At each step you can carry on to the next item, **skip** the next one to the bottom of the queue for a later session (it's not dropped — just set aside), close out, or raise something new. And if you toss in a fresh idea mid-session, Claude asks first whether you want to dig into it now or keep going through the queue, and only writes it down if you say keep going — so a new thought never feels like it got parked and forgotten, and nothing gets written twice when you'd rather just get on with it.

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

It's advice, not a command. When you run /plan, Claude reads it, mentions what it says, and lets it inform where you focus — but you're free to go a different direction. Mentioning it is what uses it up: the note is deleted automatically at that point, whether or not you follow it. It never moves into Processed and is never treated as real work — it's a one-time orientation handoff that disappears once it's done its job. If no note is there when you start /plan, nothing was recommended — the last session's close didn't have a specific suggestion to make.

There's one other way a note disappears: a session's close that has its own advice to leave, and finds a spent note still sitting in the slot, replaces it — deleting the old note and saying it did. The read-uses-it-up rule covers only notes a close isn't replacing.

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

The honest trade: under the old flow, text you hadn't agreed to never reached disk at all. Now it briefly does. That's cheap and recoverable — but it does mean the risk isn't you saying no, it's you not noticing. So the one line reporting what landed names the document precisely enough that you know which one to open, and it points you there rather than standing in for it. Reading the record is how you stay in control of the project; the line is a pointer to it, not a replacement for it.

Why it changed: pasting every draft into the chat and then writing it wrote everything twice, which burns through a session's budget fast, and you ended up reading the same text in two places. This way you read it once, where it lives.

## Why does the method record the reasoning behind every decision, not just the decision?

Because the record has to be yours, not Claude's. Claude Code now keeps some memory of its own between sessions — private notes and summaries you never see or approve, kept lossily and on no schedule you control. The recorded *why* is different in kind: a structured record you vouched for, carried alongside the work — so any session, including a fresh one that carries nothing forward, still builds the project the way you meant, instead of guessing from your files or from Claude's own unvouched notes and guessing wrong.

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

## Claude said a queue item "rests on a superseded finding". What does that mean?

It means work you planned was based on something that has since turned out to be wrong.

When Claude researches something that shapes a decision — how a tool behaves, what a limit is, whether a feature exists — it saves that research in your project under `resources/research/`. Queue items then get written referring to it. The research is the foundation; the work sits on top.

**The problem this catches.** Sometimes the research turns out to be wrong, or gets overtaken. Someone re-checks it and finds a better answer. But the connection only runs one way: your queue item mentions the research file, and the research file has no idea who's relying on it. So the correction gets written down, and every piece of work built on the old answer carries on looking perfectly fine.

**How it's caught now.** When a finding is superseded, a line goes at the top of that research file saying what replaced it and whether the whole thing falls or only part. Then, whenever you run /plan, Claude checks each queue item for research files it mentions, and flags any that carry that line.

**What to do with a flag.** Re-read the item before building it. Sometimes the item is fine — only part of the research changed. Sometimes its whole premise is gone and it needs rewriting or dropping. Claude flags it and stops there; deciding is yours.

**One honest limit.** This only catches items that actually *name* the research file. Work that was shaped by a finding without ever citing it won't be flagged, and nothing here reaches it — so treat a clean result as "nothing obvious", not "all clear".

## At the end of a session Claude used to ask me to approve a list of new queue items. Now it just tells me. Why?

Because the items are already written by the time you read the list, and that's deliberate.

When you run /done, Claude re-reads the session for anything worth capturing that hasn't been written down yet. It used to draft those as a numbered list, show them to you, and wait for your yes before writing any of them. Now it writes them into your queue first and then shows you the same numbered list, saying what landed.

**Nothing is lost by this, and one thing is gained.** You still see every item, still as one list, and you can still reject any of them by number — Claude reverts it. What changes is that a session ending abruptly no longer loses the captures: they're on disk from the moment they're named.

**Why it's safe to write first.** Your queue is tracked in git, so an item you don't want costs a one-line undo and nothing else. The things Claude still shows you *before* acting are the ones where that isn't true: a commit message, and anything that leaves your computer.

**What to do if one is wrong.** Say which number, and Claude removes or rewrites it. The one thing to know is that rejecting is now an undo rather than a non-event — so it's worth reading the list rather than skimming it.

## A build run stopped early and said the next job "runs alone". Why?

Because that job is one it would be dangerous to half-finish, so it gets a run to itself.

Normally /next works straight down your ready pile and builds everything above the "cleared to run" line in one go. Some jobs shouldn't be part of a batch like that. The clearest example is renaming a folder: the moment the folder's name changes, everything that pointed at the old name is broken until the rest of the job is done. If a run like that gets interrupted halfway — because you stepped away, or the conversation ran long — you're left with a project pointing at somewhere that no longer exists.

So during planning, a job like that gets marked **runs alone**. When a build run reaches it, one of two things happens:

- **If the run has already built other things**, it stops there and tells you why. The marked job stays in the queue, ready, and you start a fresh run for it.
- **If the marked job is the very first thing in the run**, it gets built — and then the run ends after it, rather than carrying on into the next job.

Either way it ends up with a run of its own. One exception: if the run reaches a marked job and finds it's *already done* — the check that job names is already satisfied before any step runs — the job just gets closed and the run carries on. The guard exists to protect a run from a job being performed underneath it, and a job that's already finished performs nothing.

**One honest limit.** This only controls automatic build runs. It doesn't stop you and Claude working on that job alongside other things by hand if you decide to — it's a guard against a long unattended run sweeping the job up, not a lock on the work itself.

## The plugin is now called Throughliner. What do I have to do?

Install it once under the new name, and that's it. Everything you've built stays exactly where it is.

The plugin used to be called Sovereign Implementer. The name changed because it was describing the wrong thing: the real value here is the **throughline** — the reasoning behind every decision, carried from the moment you capture an idea, through the work item, into the session record. Whatever Claude happens to remember between sessions, the throughline is the record you vouched for — it is why any session, including a fresh one, still builds your project the way you meant, instead of re-reading your code and guessing at what you wanted.

**What happens on your side.** Claude Code notices the old name and follows it to the new one automatically, rewriting its own settings and showing you a one-line notice. But because the plugin comes from GitHub, it also needs fetching under the new name, so you'll be asked to install it once. Ask Claude to install `throughliner@flintcraft` and then fully restart the app. That's the whole job.

**Two things worth knowing.** The automatic follow-along needs Claude Code version 2.1.193 or newer — on an older version you'd see a "plugin not found" message, and the fix is to update Claude Code first. And if your Claude Code settings are managed by an administrator (a work laptop, for instance), those can't be rewritten automatically, so the notice keeps appearing until an admin updates them.

**Inside your own project**, two small hidden marker files are renamed too — they record which version and which document format your project is on. If your project was set up before the rename, Claude will say your project is on an older format and point you at /setup, which renames them for you along with anything else that needs bringing up to date. Nothing you wrote is touched.

## Claude wouldn't send a message to my other project and asked me first. Why?

Because sending a message writes a file into that other project's folder, and Claude found that the other project's setup would commit it to that project's history rather than keep it private.

Every project on the method has an `INBOX/` folder, and one project can drop a message into another's. Your projects are normally set up so the mailbox stays out of git — the message sits on your disk and never becomes part of the project's saved history. But that only holds if the receiving project is set up that way. A project adopted a while ago, or one whose ignore settings were edited by hand, may not be.

**So before sending, Claude checks the receiving end and stops if the mailbox isn't protected there.** It tells you plainly what it found and waits for you to say go. The reason it stops rather than sending with a warning: once the message is committed in the other project's history, it's there, and that history may be somewhere neither of you is looking.

**What to do about it.** You have two straightforward options. Say go anyway — reasonable if the message is unremarkable and the other project is private. Or open the other project first and ask Claude to add its `INBOX/` to that project's ignore list, then come back and send. The second takes a minute and fixes it for every message afterwards.

**One related thing worth knowing.** When you tell Claude where another project lives, it remembers the folder path so you don't have to look it up again. It keeps that note inside the mailbox folder, out of git, and it won't quote the path back to you in conversation or write it into your queue or your session records — because those *are* saved, and a folder path can say more about you than you'd want a saved file to carry.

## Claude said a sentence I wanted in SPEC belongs somewhere else. Why?

Because SPEC is meant to say what your project **is and does**, and the sentence was describing **how something is built**. Those are different jobs, and mixing them is what makes a spec slowly stop being readable.

SPEC.md is the one document Claude reads before proposing work and again before building it. It's the answer to "what is this thing, who is it for, how does it behave." That makes it valuable in proportion to how much of it is true and load-bearing. The problem is that it only ever grows: every change that affects what your app does adds a sentence, and nothing ever takes one out. Left alone for a year, it becomes long, expensive to read every session, and full of detail nobody needs at that level.

**So three rules apply whenever Claude edits it.**

- **What goes in.** Product truth — the behaviour, not the machinery. "Users can export their list as a spreadsheet" belongs in SPEC. "The export runs through a queue and writes a temporary file first" is implementation, and belongs wherever that part of the project is documented.
- **Reasoning goes to the session record.** Why you chose one approach over another is genuinely worth keeping — it just isn't a description of your product. It goes into the log entry for the session that decided it, where the decision lives with its reasons. SPEC keeps the plain statement of what's true now.
- **Out-of-date sentences get fixed, not tolerated.** If SPEC describes something your app doesn't do any more, that's a mistake in the document, not just untidiness — because Claude will build against it. Whoever notices it corrects it.

**There's no length limit, and that's deliberate.** Claude won't ever tell you SPEC has got too big, or ask you to trim it to fit a number. Your spec has to describe your product as it actually is — so a true sentence about a real feature can never be cut just to save room. The rules above are about what goes in and whether it's still true, never about size.

**If you disagree, say so.** These are Claude's judgement calls about where a sentence lives, not rules about what you're allowed to want. If you'd rather the detail sat in SPEC, tell Claude and it goes in SPEC.

## A build asked to change SPEC halfway through. Is it allowed to do that?

Yes — that's the normal route, and asking you first is the rule it's following, not one it's breaking.

Here's the situation it's in. A build works from a job you already agreed during planning, and SPEC describes what your project does. Sometimes, partway through building, it turns out the work establishes something true about your project that SPEC doesn't say yet. Leaving SPEC behind isn't an option: it's the document Claude reads at the start of every future build, so a gap there quietly misleads every session afterwards.

**So the method's answer is that the build may update SPEC, but never quietly.** It stops, tells you exactly what sentence it wants to add or change, and waits for you. That pause is the safeguard — SPEC is your project's truth, so a change to it is always yours to approve.

**Why it can look alarming.** You agreed to a piece of work, and mid-way through Claude asks to edit the document that defines your project. Read cold that can look like it's asking permission to go out of bounds. It isn't. It's the one moment the method insists on asking, precisely because the document matters.

**How to answer.** Read the proposed sentence. If it matches what you now want your project to do, say yes and the change lands in the same commit as the work — which is the point, so the two never drift apart. If it doesn't match, say no: that's a useful signal that the build has gone somewhere you didn't intend, and it's much better caught here.

**One thing this is not.** If Claude says the work **contradicts** something SPEC already says, that's a different and more serious moment — it means the job and your project's stated truth disagree, and one of them is wrong. That one stops the run and needs a real decision from you, rather than a quick yes.

## Claude calls some things "captures" and others "work items". What's the difference?

Where they sit in your queue, and whether anyone has agreed to them yet.

- A **capture** is anything written into the **Unprocessed** part of your queue. An idea, a problem spotted mid-build, something you said in passing. Anyone can file one at any time — that's the point of it. Nobody has decided it's worth doing.
- A **work item** is an entry in the **Processed** part. It got there because a planning session weighed it with you, agreed it was worth doing, and worked out what building it would actually change.

**Why the two words are kept apart.** Everything in your queue looks the same on the page — a heading, a short name in brackets, some reasoning underneath. Using one word for both makes an idea nobody has looked at read exactly like work you approved. That blur is how a half-thought-through capture can end up looking queued and ready.

So: **captures become work items.** That transition is what a planning session is for, and it's the only line the queue really has.

## What is a "return path" on a message from another project, and what if one hasn't got one?

It's the sending project's own folder, written into the message — so whoever receives it can reply without you having to go and find where the sender lives.

Messages between your projects carry two things identifying the sender: its **name**, in the filename and the opening line, and its **return path**, in the body. The name tells you who wrote. Only the path says where to write back, which is why both are there.

**Mail without a return path may be undeliverable in the reply direction.** Older messages, sent before this existed, often name the project and nothing else — and a few name nobody at all. Claude can't go looking: it works only in the folder you opened it in, and never scans your machine for your other projects. So if a reply is owed to a message with no path, Claude will ask you for the folder, once, and remember it for next time.

**Is the path safe to have in there?** It only ever goes into a mailbox folder that git has been told to ignore — and before writing anything, Claude checks the receiving project's ignore rules and refuses to send if that folder isn't covered. So the path stays on your machine and never reaches a published repository.

## Do I have to type out the other project's folder path?

No. Telling Claude where to look counts the same as typing the path yourself.

When a message needs to reach one of your other projects, Claude needs that project's folder location. You can paste the path — or you can just name the folder ("it's called Recipe Menu, somewhere under Documents") and ask Claude to find it. Claude then runs a narrow search for that name, shows you what it found, and only records or uses the path once you've confirmed it's the right folder.

What never happens is Claude going looking on its own. The search runs only when you ask for it, it searches for the name you gave, and nothing is saved or sent until you've confirmed the match. Once confirmed, the location is remembered in the project's mailbox folder — which git never publishes — so you won't be asked again for that correspondent.

## Claude mentioned word counts and a missing quote after editing my queue. Is something wrong?

No. Those are notes, not errors — the queue check has always reported things it noticed without stopping anything, and these are two more.

**"[some-item] +420 words"** is a bare fact: that item got longer since your last save. There's no threshold and no opinion attached, and there deliberately never will be — nobody can say what the right length for a piece of work is, so the note tells you what changed and leaves the judgement to you. Sometimes growth is exactly right, because a decision genuinely needed recording. Sometimes it's padding. You can tell; a number can't.

**"says 'captured by you' but quotes nothing"** means an item claims the words or reasoning were yours without showing any of them. The rule behind it is that a credit to you should rest on something you actually said — not on Claude's summary of what you probably meant. The fix is either to quote you properly or to drop the credit, in which case the item reads as Claude's, which is the default.

**What neither of these can do**, said plainly because it would be easy to assume otherwise: they cannot tell whether reasoning attributed to you is genuinely yours. The first makes growth visible. The second makes an unsupported credit visible. Both turn something silent into something you can point at, and neither is a guarantee.

## What is /rescan, and when would I use it?

It reads back over your conversation and writes down anything you decided or noticed but never actually put in the queue. Run it whenever you like.

A lot gets said in a working conversation that never lands in a file — an idea in passing, a problem you spotted, a decision made out loud and moved on from. Until now the only thing catching those was the closing step, at the very end. `/rescan` is that same check, available whenever you want it.

**It only looks back as far as the last time you ran it.** So running it three times in one conversation doesn't show you the same things three times — each run picks up from where the last one stopped. That's what makes it cheap enough to use mid-conversation.

**It writes things down. It doesn't decide what happens to them.** Everything it finds goes into the unprocessed part of your queue, and planning is what decides what's worth keeping — including the planning session you are already in, if one is running. You don't have to wait for a future session to sort out what was just written down. It never builds anything — partly because that's `/next`'s job, and partly because it couldn't help if it tried: the plugin your conversation is running is a fixed copy, so a fix made now wouldn't reach you until the plugin is reinstalled anyway.

**And it hands back when it's finished.** Whatever you were in the middle of carries on from where it was — running it doesn't end anything or make you start again.

**Why it exists as its own command.** Two reasons, both from real annoyance. Every check added to the closing step made the end of a conversation heavier and pulled the whole thing toward wrapping up. And an earlier version of this check that fired "at a natural pause" had no way to tell what a pause was — it ran three times in one conversation, unasked. Yours is the honest trigger: it runs when you say so.

**The closing step still does it**, just shortened — it picks up whatever came after your last `/rescan`. Never run it and nothing changes for you.

## The planning session told me some work is "being held". Do I need to do something?

Usually not — but read the line, because sometimes the answer is yes, and that's exactly why it's now said out loud.

Work sits in a held state when something has to happen before it can be built: another piece of work has to ship first, or a date has to arrive. Held work is still yours and still queued; it just isn't offered to a build run yet.

**What changed.** Every planning session now names each held item, what it's waiting for, and how long it's been waiting. Before, you were told a number — "three items held" — which is true and tells you nothing you can act on. A number reads as normal. "Held since the 14th, waiting on you" doesn't.

**Why it mattered enough to change.** Work has sat held, correctly held, while its owner couldn't see it during ordinary use — running builds and closes without ever sitting through the part of a planning session where held work is examined. In one case a post someone had decided to make simply never went out, and nobody noticed for a day. In another, someone asked why a feature "wasn't queued" when it was queued, fully designed, and held for a perfectly good reason.

**So: read it, and act only if it names you.** If a held item is waiting on other work, it lifts itself when that work ships. If it's waiting on a date, it lifts itself when the date arrives. If it's waiting on **you**, that's the one worth stopping for.

**One honest gap.** For older items, Claude can't always work out the date a hold started. When it can't, it says the item is held without claiming to know since when, rather than guessing.

## A queue item says "Not before" and a date. What is that?

It's work that is finished being planned and is waiting for a day to arrive — nothing more.

Most work that sits below the "cleared to run" line is waiting on **other work**: something else in your queue has to happen first, and the item says which. A date is the other kind of wait. If you want a post to go out tomorrow rather than today, or a check to run a week after a change ships, the item carries a line reading `Not before:` and the date.

**Nothing is asked of you, and nothing has to be remembered.** When the day arrives, the planning session sees it has arrived and offers the work. You don't confirm it, and Claude doesn't have to notice it — the date is read off the calendar automatically at the start of every session.

**Why this is worth having.** Before, the only way to hold work until a date was to file a second, made-up piece of work saying "a day has passed" — which someone then had to sit through a planning session to answer. It cost a session to answer a question a calendar answers, and it failed anyway: the work being paced simply never came back up.

**If the date looks wrong**, say so and Claude will change it. It's an ordinary line in your queue, not a setting.

## Can I plan and build in the same conversation?

**Yes.** Planning, building and recording in one conversation is the normal shape of a session — it's the cycle the method describes: /plan to decide what to work on, /next to build it, /done to record and commit.

If Claude has ever pushed back on that, it was reading a rule that has now been removed. The old wording said planning and building must not be "crossed" inside one session, which sounded like a ban on typing both commands in one conversation. It was never meant that way, and it contradicted the workflow's own description of a session.

**What the real boundary is, and it hasn't changed.** Anyone — any session, any command — can *write something down* in your queue. Only a planning session *decides what happens to it*: whether it's kept, what shape the work takes, where it sits. So a build that spots something new writes it into your queue and carries on; it doesn't quietly promote it to agreed work. That's the line the method actually holds.

**The one practical caution is about length, not permission.** Claude works better in shorter conversations, so a long session that has already planned and built a lot is a good moment to start fresh — a suggestion about how well the work will go, never a rule about what you're allowed to do.

## What is "freeform" work, and when would I use it?

**Freeform work is work you and Claude do by hand, in a session of its own, instead of building it from the queue.** Something too big to break into queue items, or something that by its nature can't run inside a build run.

**You don't have to set it up.** The common case never touches the queue at all: you open a session, you and Claude work on something directly, and when you're done you run /done. It reads the edits as your expected work — not as a broken project — records what happened, and commits. That's a freeform close, and it's what the word names.

**Occasionally one is filed as a piece of work.** Then it carries a `[freeform]` tag, sits with your ready work, and a build run **stops** when it reaches it rather than building it — saying plainly that this one needs a session of its own. Claude places it at one end of your ready work so a run either stops immediately or gets everything else finished first.

**One case where it genuinely matters.** If the thing being repaired is part of the machinery a build run itself uses — the tool that moves items around your queue, the safety check on which files can be edited — then using that machinery to fix itself is the risk. That's an example of freeform work, not the definition of it.

**If you're unsure which you've got**, just work on it and run /done. That's the freeform path, and it needs no decision from you in advance.

## How do I start the freeform work the close told me about?

Paste the starter line Claude gave you into a fresh chat. That's the whole move.

When a session closes and your queue holds a piece of freeform work — work you and Claude do by hand rather than run from the queue — Claude announces it and hands you a short ready-made prompt in a copy-able block. It names the work, says where its entry lives, and says the chat will end with /done. You don't have to remember or explain anything: open a new chat, paste it, and the new session picks the work up from the queue entry.

If you've lost the prompt, that's fine too — the work is still sitting in your queue, so you can tell a fresh chat "let's do the freeform item in the queue by hand" and it will find it.

## An update told me my CLAUDE.md describes things that no longer exist. What do I do?

**Nothing, unless you want to.** It's a heads-up, not a problem with your project, and nothing is broken.

**Where it comes from.** Your `CLAUDE.md` was written when the project was first set up, and Claude reads it at the start of every session. The method itself keeps changing — pieces get replaced by better ones — so a file written a while ago can end up describing parts that were retired since. The words are still sitting there being read as though they were current.

**What Claude checks, and only during an update.** When a newer version of the plugin brings your project up to date, it reads your `CLAUDE.md` for names of things the method no longer has, and tells you each one alongside what took its place. Common ones: a queue made of "batches" with Build/Test/Audit sub-headings, a "Deferred tests" section, and items carrying a `Parked:` line. Each is now something simpler — a single work item with a tag saying how it runs, a step written as work for you to do, and work held below the "cleared to run" line.

**It reads and never rewrites.** Claude will not edit that file for you here, deliberately. It's your file, you may have written a good deal of it yourself, and replacing your paragraph with the current wording would throw away what you wrote to fix something cosmetic. So you get told what's out of date, and the change is yours to make or ignore.

**Why it's worth telling you at all.** A session that reads a description of something retired goes looking for it. That happened on a real project: a session hunted for a section that had been removed months earlier, then had to work out from scratch that it was gone. Ten seconds of your attention now saves that.

## A build run stopped and said a job doesn't say enough to build. What does it want from me?

**It wants the missing decision, and there are two kinds it can be missing.**

A build run works through jobs you already agreed, without checking back. It stops for one reason: the job doesn't contain enough to build from, and going ahead would mean inventing something you never agreed to.

Two things can be missing:

- **Which files it changes.** The job describes an outcome but nothing that says where the change goes.
- **What changes inside them.** The job names the files perfectly clearly and still doesn't say what the new behaviour should *be* — "improve how this works" names a place, not a change.

**The second one is new, and it used to come out differently.** A run meeting that kind of gap had no defined route, so it improvised: it stopped mid-build and started a design conversation. That's the wrong shape — design happens when you're planning, with time to think, not halfway through a run you weren't watching.

**What to do.** Say what the job should actually do, and Claude carries on — or say you'd rather work it out properly, and it goes back for planning. Either answer is fine; the stop exists so the choice is yours rather than Claude's.

**It isn't a failure.** Nothing is broken and nothing is lost. A job that reaches a run under-specified got through a check earlier on, and the stop is the backstop working.

## Setup offered to keep my planning documents out of the repository. What does that cover, and can I change my mind?

**It covers three things, and you pick them individually: `SPEC.md`, `QUEUE.md`, and the whole `LOG/` folder.** Those are your plans, your reasoning and your session history — the most personal material the method produces. Saying yes to any of them adds that one to `.gitignore`, so it stays on your computer and never enters the repository.

**You can have any combination.** All three, none, or just the ones you mind about. The common case is wanting the queue private — it's where the half-formed ideas and the reasoning live — while leaving the history and the description of the project public. It's asked as one question, so answering it costs you one reply either way.

**What you give up, for whichever ones you keep out.** They stop being version-controlled. That means an unwanted change can't be undone by going back to a previous version, and they don't come with the project if you clone it somewhere else. Everything else about how they work is unchanged — Claude still reads and writes them exactly as before.

**Yes, you can change your mind, in either direction.** It's a few lines in a file called `.gitignore` at the top of your project. Ask Claude to add them or remove them and it will. Nothing about the decision is locked in.

**One thing that isn't reversible.** If those documents were already committed before you changed your mind, adding them to `.gitignore` stops *future* changes being recorded — it doesn't remove what's already in the repository's history. If that matters to you, say so and Claude will tell you plainly what's already in there.

**Why you're asked at all.** If your repository is ever made public, these documents go public with it, and they're the ones most likely to contain something you didn't mean to publish. Claude checks its own writing and scans for things shaped like passwords, but no check can tell whether a sentence quietly identifies a real person. Not publishing them is the only complete protection — which is what this option is.

## My session record has an "Also in this chat" section. What goes in there?

**Everything real that happened in the conversation but wasn't one of the jobs.**

Your session records are organised around work: one record per piece of work that got built or planned. That's most of what happens, but not all of it. You correct Claude about something and the correction changes how the tool behaves. A decision gets reached in conversation. Something goes wrong and gets fixed. You edit a file by hand between two runs.

None of that belongs to any job on your list — so before this existed, it went into the record only if someone happened to think of it, and usually vanished when the conversation ended.

**What it looks like.** A short section at the end of the record, listing those things plainly. If nothing like that happened, the section isn't there at all.

**Why it matters more than it sounds.** /done closes a **conversation**, not a single command. A correction you gave that changed how something works is often the most valuable thing in the whole session — and it was the one thing with nowhere to live.

**It's separate from the "work came after the close" section.** That one covers things done *after* the record was written and committed. This one covers things that happened during the conversation and simply weren't jobs.

## At the end of a build Claude told me some work was "unconfirmed". What should I do?

**It means the code was written but nothing has run it yet, and Claude is telling you rather than letting you assume otherwise.**

When a build finishes a piece of work, it marks it one of two ways: **built and confirmed** — something actually ran and passed, a test, a command, a check of the output — or **built but unconfirmed**, along with what still needs running. At the close, anything in the second group gets named out loud.

**Why this is worth a moment of your attention.** "It's written" and "it works" are different claims, and they used to look identical in the record. A build could finish, everything could look complete, and nobody would know that a piece of it had never been executed. Worse, other work in your queue waits on things being *verified*, not merely built — so a missing distinction quietly weakened a safety check somewhere else.

**What to do about it.** Usually nothing immediately. It's a note of what's outstanding, and the check gets run when it can be. If it's something only you can do — looking at a screen, trying it on a device — Claude will have put that in your queue as a step for you.

**What it isn't.** It isn't a failure, and it isn't a warning that something is broken. Unconfirmed means unknown, not wrong.

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

In a planning session you'll see them turn into a recommendation — something like "three items are holding other work up, so I'd suggest getting through at least those three." That number is derived from the count rather than picked, and Claude will tell you where it came from.

**You'll see the line even when all three numbers are zero**, which is deliberate. "Nothing is waiting on anything" is genuinely useful to know, and staying silent would be ambiguous — you couldn't tell the difference between nothing to report and a check that didn't run.

You don't need to do anything with it. It's information, not a request.

## Why does a planning session open knowing what happened last time?

Because it reads the last few one-line session summaries before saying anything.

Sessions don't remember each other. That used to show most at the very start of a planning session: Claude would be working from your queue alone, with no sense of what had just been done, and you'd often end up asking it to go and look. Now it reads the top lines of your session index as part of getting its bearings, and folds anything relevant into what it says to you at the opening.

**It's orientation, not a report.** You won't get a summary of your recent history for its own sake — only the parts that bear on what you're about to work on. And it's a few short lines, not a few full session records, so it costs very little.

## My app asked whether to keep or remove this session's copy of the project. Which do I pick?

**If the session did any work, do not pick remove until it's been merged.**

Some setups give each conversation its own private copy of your project, so two conversations can't tread on each other. The catch is what happens at the end: **that copy is never merged back on its own.** When you close it, the app asks whether to keep it or remove it — and *remove deletes the copy, the branch, and every commit on it.* It reads like tidying up. It isn't.

So the workflow does two things about it:

- **At the close of an isolated conversation**, Claude tells you which branch your work is on, that it hasn't been merged, and that "remove" would delete it. It can't do the merge itself from there — git won't let a copy update the main line while the main line is open elsewhere.
- **At the start of a conversation in your main copy**, Claude points out any copies holding commits the main one doesn't have, and offers to merge them. It offers; it never merges on its own. If the merge can't be done cleanly, it leaves the branch exactly where it is and tells you the work is safe there — you'll never be shown a tangle of conflict markers to sort out.

One honest limit: what Claude can see is *a copy holding commits yours doesn't*. It can't tell that apart from a deliberate long-lived copy — an archived version of the project, say — so it will describe what it found and judge before offering, rather than assuming everything it sees is stranded work.

## Claude flagged some queue items as contradicting themselves. What does that mean?

When you run /plan, Claude checks your queue for work whose *position* disagrees with what the work itself says. It reports what it finds and stops there — it never moves anything.

Three things get flagged:

- **Work marked ready that says it isn't.** An item sitting above the "cleared to run" line whose own notes say it must not be built as written, or that a previous build session handed it back untouched. Left alone, the next build run would build exactly the thing the item warns against.
- **Work with nothing to change.** An item marked ready whose list of files to edit is empty, or says the list will come out of designing it. That means it's still a design question, not a build.
- **A chain of waiting.** Work waiting on something that is itself waiting on something else. Neither moves until the far end of the chain does, which is easy to miss when you only look at one item at a time.

**Why this check exists.** Work gets examined carefully when it's *put* into the ready pile, and then never looked at again. But things change around it afterwards — a decision gets reversed, a build session hands something back, the thing it was waiting for turns out to be waiting too. A gate on the door isn't the same as looking around the room.

**Nothing happens automatically.** Whether a flagged item gets moved, rewritten or left exactly where it is, is your call — that's a decision about what the work *is*, and those are always yours. Claude tells you and waits.

## My session records used to be long. Why are some of them short now?

Because short is now the normal one, and long is the exception it's meant to be.

Every piece of work gets a record written into your `LOG/` folder when you run /done. Those records used to run long by default — several hundred words each, walking through the reasoning, the options considered and why one won. That's genuinely valuable for a decision you might revisit or disagree with later. It's wasted on a change that's fully explained by saying what changed.

The problem was that writing less *felt* like leaving something out, so nearly everything got the long treatment. On a session that finished a dozen pieces of work, writing the records cost more than doing several of the jobs did.

**What changed.** As Claude builds each piece of work, it decides on the spot whether that one deserves the long version — while the reasoning is fresh, not hours later at the end. Two things earn it: the reasoning was genuinely contested, or a real alternative was weighed and rejected. Everything else gets a short record naming what changed.

**Nothing is capped, and nothing is lost.** There's no word limit — a hard decision still gets as much room as it needs. The only change is which way the default points. And the reasoning behind your *work* isn't affected at all: that lives on the queue items themselves and travels with them, which is separate from how the finished record is written up.

## I sent a message to another one of my projects. How do I know it arrived?

**You know it was delivered. You don't know it was read, and nothing here will tell you.**

Sending writes a file into the other project's mailbox. That's the whole mechanism — there's no receipt, no read confirmation, and no notification back to you. The other project sees it the next time you open a session there, and only then.

**Two things happen to make that less fragile.** Before writing, Claude checks the other project actually has a mailbox, and says so plainly if it has to create one — because a project set up before mailboxes existed has nothing that tells you mail is waiting, so a message can sit there forever with neither side knowing. And the first time you give Claude the folder path for a project, it's saved, so continuing a conversation doesn't mean digging out the path again every time.

**That saved list lives inside the `INBOX/` folder, which git ignores** — so the folder paths on your computer are never committed and never end up in a published repository. If you ever move that file somewhere else, you lose that protection without any warning.

**Why there's no read receipt.** It would mean one project automatically writing into another, and nothing here sends anything without you seeing the exact wording first. A receipt you have to approve for a message you didn't write is worse than no receipt at all.

## I asked for something during a build and Claude wrote it down instead of doing it. Can I insist?

**Yes — ask again and a small change gets done.**

When you raise something mid-build that isn't part of what's being built, Claude writes it into your queue and carries on, and tells you in one line *why*: the run stays on the work you agreed, and the new thing gets weighed properly against everything else still to come rather than being decided on the spot. It also gets a proper check and a file list before anything is written, which is what stops a half-thought-through change landing in the middle of a build.

**If you ask a second time, Claude takes that as your decision and does it** — as long as it's small, meaning it touches a file or two. That's not a special rule for builds; it's the same principle everywhere here, that if Claude raises a concern and you repeat yourself, the call is yours.

**Big changes still get pushed back.** If what you're asking for touches a lot of files, or isn't fully worked out yet, Claude will suggest finishing the current run and picking it up properly afterwards. Asking twice doesn't make a large change small, and that's exactly the kind of change that goes wrong when it's squeezed into a run already underway.

## We kept working after the session was "closed", and Claude offered to add it to the record. Why?

**Because the record was already written and committed, so that work wasn't in it.**

Closing a session writes up what happened and commits it. That's the end of the session as far as the workflow is concerned — but conversations don't stop that neatly. You ask one more thing, something gets fixed, a small job gets run. All of it is real work, and none of it appears anywhere, because the write-up was finished before it happened.

So when something after the close actually changes a file, Claude offers once to **add a short section to the end of that session's record**, marked as work that came afterwards. It's added rather than blended in, so you can still see what was true at the close and what came later.

Three things about the offer:

- **It comes once**, not after every message.
- **It only comes if a file changed.** Talking something through afterwards has nothing to record.
- **It's an offer.** Say no and nothing happens.

Before this, the only thing that closed the gap was you remembering to ask.

## Claude queued an audit right after a piece of work. Why two items instead of one?

Because building a tool and reading what it says are two different jobs, and the second one used to get forgotten.

When a piece of work produces something that **measures or reports** — a script that counts things, a check that lists problems — the tool being finished is not the same as anyone having looked at its output. So Claude now files the reading as its own item, placed straight after the building one.

It has happened twice here that a measuring tool was built, the work was recorded as finished, the queue showed nothing outstanding — and nobody read the output for days. Nothing catches that, because there is no missing step to notice: the reading was never written down as a step in the first place.

**What this means for you:**

- **They run in the same session.** The second item needs nothing waiting — the tool works the moment it is written, so one run can build it and then use it.
- **They stay next to each other.** The close normally shuffles audits toward the end of the ready work, and it now makes an exception for this pair so they don't get separated.
- **The second one edits nothing.** It reads the output and files what it finds as new items for you to sort at your next planning session.

## Claude used to repeat the same queue warnings after every single action. What changed?

It now only tells you in full about problems **your current work introduced**, and mentions the rest as a count.

The queue check looks at your QUEUE.md and flags anything shaped wrongly. It used to re-list every flag it found, every time it ran — so a few long-standing ones would be repeated after every edit and every command, unchanged, sometimes dozens of times in a session.

That is worse than noise. Warnings that appear constantly get skipped past, and the one time a genuinely new problem appears, it is buried in the same wall of text as the ones you have already read and decided to leave.

So the check now compares against your last commit. Anything new gets the full explanation. Anything already there before you started gets one line: how many, and that none of them came from this change.

**Two other things worth knowing:**

- **Nothing is hidden.** A long-standing flag is still counted, and still appears in full the moment its item is edited.
- **The word-count report is quieter too.** It now appears only after something actually writes to your queue, rather than after any command at all.

## Why wasn't I credited with that decision? I agreed to it.

Because agreeing to something Claude worked out is not the same as having thought of it — and the records only credit you with what was actually yours.

Your project's queue and session records note where an idea came from. Anything unmarked is Claude's. Something you raised says so. This is not bookkeeping for its own sake: the whole point of these records is that you can read them back later and trust them, and a record that credits you with reasoning you never did is one you cannot trust.

**So the line is drawn at authorship, not approval.** If Claude proposed something, laid out why, and you said yes — the reasoning is Claude's. You made the call, and that gets recorded as your decision, but the thinking behind it is not attributed to you.

**There is a specific case this covers.** If you reply by tapping one of the suggested replies, or answering in a word or two, that reply is often Claude's own wording handed back. Claude cannot treat that as evidence you originated the idea, because there is nothing in it that Claude did not just write. The test is simple: if your reply is entirely contained in what Claude just said, it does not establish that the idea was yours.

**Quoting you is stricter still.** Quotation marks, or a phrase like "in your words", mean you actually said those words. Where Claude has put your point in its own words, it says so rather than dressing a paraphrase as a quote.

**When it is genuinely mixed, the record says so** — naming which part was yours and which was Claude's, rather than picking one.

**If you think a credit is wrong, say so and it gets checked.** What Claude will not do is go through every past credit and mark them all as doubtful — that would be an unverifiable claim about your own records, and it would damage the honest credits along with the questionable ones.

## Claude suggested dropping one item from a build because `/setup` is waiting. What does that mean?

It means that one piece of work is probably already done, and building it would be wasted effort.

When the plugin is updated, your project's own documents can fall behind what the new version scaffolds. `/setup` brings them up to date, and it wants a session to itself. Claude tells you that at the start of every session until you run it.

Here's the trap. Some of your project's documents have a section that `/setup` **rewrites from a template**. If a piece of ready work is a fix to something inside one of those sections, then running `/setup` would replace that text anyway — very likely with the corrected version already. Building it first does the work twice, and the second time wins.

So when both things are true — `/setup` is outstanding, **and** a piece of work in this run touches a file `/setup` rewrites — Claude names that item and suggests leaving it out of this run.

**Three things worth knowing:**

- **Only that item is dropped, and only from this run.** It stays in your queue exactly as it was. Nothing is deleted and nothing is decided about it.
- **You can say no.** It is a recommendation. If you want it built, it gets built.
- **It only appears when it actually applies.** Claude does not warn you on every run just because `/setup` is pending — a warning that shows up whether or not it is relevant is one you learn to ignore.

**This came from a real session** in another project: a whole build ran and closed with its top item already void before it started, and the session had to end with nothing built so that `/setup` could run.

**What to do about it:** finish or close the current session, then run `/setup` on its own.

## We kept working after the close. Is there a quicker way than explaining it every time?

Yes — say **`/rescan`**. It looks back over what has happened since it last ran, works out what each thing is, and files it in the right place.

This used to be a longer conversation. Work carries on after the session was closed, and getting it recorded meant explaining what had happened and asking for it to be added — every time. `/rescan` is that request in one word.

**It sorts what it finds three ways:**

- **Something still to do** goes to your queue as a new idea, exactly as before.
- **Something that already happened** — including work done after the close — gets added to this session's record, marked as a tail so it is clear it came afterwards.
- **Evidence someone will need to re-read word for word** goes into a file of its own.

**It saves nothing to your project's history.** The tail sits there waiting and rides along with your next close. That is deliberate: it stops this being a second close wearing another name, and it is why you can run it as many times as you like. You never have to decide "is this the last bit?" — just run it again when there is more.

**It never decides anything.** It writes things down and stops there. Whether a new idea is worth doing, and when it gets built, is still settled at planning.

**One honest limit**, which Claude will say out loud when you run it: if the earlier part of your conversation has dropped out of view, Claude cannot tell. What you get is what it could still see, not a guarantee it caught everything.

## What is `INBOX/sent.md`?

A one-line record of everything this project has sent out — so you can answer "what did we send them?" without digging.

Your `INBOX/` folder holds messages other projects sent *you*. `sent.md` is the other half: one line for each thing that left, whether that was a message to another project, a problem report, a bug filed against Claude Code, something posted publicly, or a draft handed over for someone else to finish.

**Each line carries five things:** the date, where it went, whether you handed the work over **for completion** or only **for continuation**, what it claimed in a single clause, and a pointer to the text itself. No second copy of the content — just enough to find it.

**"For completion" versus "for continuation" is the one that does real work.** If you hand a piece of work to another project to *finish*, that item can come off your queue. If you handed it over for them to *carry on with*, it stays — it's still yours. Recording which one it was is what lets Claude close the item out correctly later instead of guessing.

**Why this was needed.** Two questions had no answer. *What did we send that project?* — and *did we ever announce the thing we've just changed?* That second one matters: if you posted publicly that your tool behaves a certain way, and then changed it, nothing would have caught that. Now there's something to check against.

**The line is written the moment you approve the send**, not later, because the exact wording exists right then and nobody can reconstruct it afterwards.

**One limitation worth knowing:** `sent.md` lives inside `INBOX/`, which is deliberately kept out of your repository — those lines name other projects and where they live. So it isn't version-controlled and it can be lost. That is the same trade the method makes for your address book, for the same reason.

## A build told me my SPEC is missing a sentence, but wrote a queue item instead of just adding it. Why?

Because the session that made a decision is not allowed to be the session that writes it up as product truth.

`SPEC.md` is what your project *is* — what it does, who it's for, how it works. A build session has just spent its time making things. If that same session then wrote a sentence into SPEC describing what it made, that sentence would be the build justifying itself, not a description you agreed to. So the build writes the sentence down as a new item in your queue and carries on.

**What happens next.** At your next planning session, that item comes up, and Claude writes the sentence into SPEC with you there to agree or change it.

**Meanwhile SPEC is behind by one sentence**, which is worth being plain about. That is the real cost. What makes it acceptable is that it is behind *visibly* — there is an item sitting in your queue saying exactly what is missing — rather than behind silently, which is what used to happen.

**Normally this doesn't come up at all.** When work is planned, Claude asks of each piece: does this change what SPEC says? If yes, the sentence gets written then, before anything is built. You only see this fallback when that question was missed.

**A build stopping to ask you mid-run was tried and dropped.** It interrupted runs for a single sentence, and read — even to the person who wrote the method — like the run asking permission to break a rule. Deferring it to the end of the same run was also considered and rejected, because the end of a build session is still that build session.

**One thing this is not:** if the work you just built *contradicts* something SPEC already says, that is different and more serious. Claude stops, shows you the sentence, and asks which one is wrong. It never quietly rewrites SPEC to match what it did.

## Claude said some of my project documents "are not tracked by git". Have I broken something?

No. That is a setting you were offered, and it is doing exactly what it says. Claude mentions it at the start of every session because three things behave differently as a result, and none of them announces itself.

When your project was set up, you were offered the option of keeping `SPEC.md`, `QUEUE.md` and `LOG/` out of your repository — they hold your plans, your reasoning and your session history, which is the most personal material this method produces, so keeping them out is the only complete protection if the repository is ever published. If you took that option, or added those lines yourself later, this is what you are seeing.

**The three things that change:**

- **Claude shows you text before writing it, instead of writing and then telling you.** Normally it writes straight into these documents and tells you what landed, because if you disliked it, undoing it would cost nothing. Without git there is no previous version to go back to — so the safer order applies and you see things first.
- **A deleted queue item is really gone.** Normally your project's history keeps a copy of anything removed from the queue. Not here.
- **The close records from memory.** Normally the session close can look at exactly what changed in your queue and describe it. It cannot, so it writes the record from what happened in the conversation.

**Why you're told at every session opening, not once.** This state does not only come from the setup question — you might have written the ignore lines yourself, or chosen it weeks ago in a project you haven't opened since. In one real project it went unnoticed until a full planning session's record turned out never to have been saved at all.

**If you want to change it**, the fix is editing your `.gitignore` file to remove those lines. That is a one-line change and the start of a session is the right moment for it — ask Claude and it will walk you through.

**And if you keep it as it is, nothing is wrong.** This is a supported choice, and Claude will not call it a mistake or keep pushing you.

## Can I start a build and walk away?

No — and if you have been told otherwise, that was wrong and has been corrected.

A build run does go through your ready work without stopping to confirm each piece, and it moves faster than you can read. That part is real, and it is why Claude does not interrupt it to ask you things. But it does not finish by itself. **It stops three times, and one of those stops is at the very end.**

- **A step that is yours to do.** Claude walks you through it live, one instruction at a time, and waits for you between each. Nothing moves until you answer.
- **Work marked as needing its own session.** The run halts on it and says so, rather than skipping past.
- **The close.** Recording what happened and committing it is a command you run. Claude cannot run it for you.

That last one is the one that catches people. **If you walk away, you come back to finished work that has not been recorded or saved anywhere permanent.** Nothing is lost — the files are changed and sitting there — but until you run the close, there is no session record and nothing is committed.

**Why Claude can't just close it for you.** Committing is one of the very few things Claude shows you before doing, because a commit is genuinely awkward to undo and the message never ends up in a file you could edit afterwards. A run that closed itself would either skip that or invent a version of it with nobody there to read it. Neither is worth saving you one command.

**There is one other thing worth knowing.** While a run is going, it is using your session — so you cannot capture a passing thought at the same time. Mention it and Claude will write it down as it goes, but you cannot be planning in parallel.

**So: stay nearby.** You will not be asked much, and possibly nothing at all until the end. But the end needs you.

## How long should my queue items and session records be?

There is no answer, and that is deliberate — the method used to give one and it was withdrawn.

For a while each kind of writing had a target length and a limit: so many words for an idea, so many for a piece of work, so many for a session record. Those are gone. What replaced them is not a vaguer version of the same thing — Claude is not asked to "be concise" instead — because that was tried first, measured, and did nothing at all.

**Why the numbers went:**

- **They were read off your own writing.** The limits were the middle of what this method's own project had already written. A limit derived from what you already do can only ever tell you that you do what you do.
- **They fired on almost everything.** At one point the limit was exceeded by nearly nine out of ten ideas and three-quarters of work items. Something that flags nearly everything cannot tell you which ones are actually a problem — and people learn to click past it.
- **Acting on a breach barely helped.** Three separate passes at tightening the writing removed 8%, 3% and 9%. The conclusion of those passes was that the text was not padded: its length was accumulated decision-making.

**What you get instead.** A tool that reports your project's own distributions — how long your ideas, work items, session records and index lines actually run, longest first — and prints no threshold of any kind. It tells you the facts and leaves the verdict to you. That is the same posture as everything else the method measures.

**What has not changed.** Both failures are still real, and Claude still watches for them: something too short to reconstruct why you did it is as broken as something too long to read. The method's actual lever now is *where text lives* rather than how it is worded — the reasoning behind a decision gets moved into your session records and pointed at from the work item, instead of piling up inside it.

**If an item is getting unwieldy**, Claude has two moves, and neither is a word count: split it, if it is really two pieces of work; or move the long narrative into the record and cite it, if it is one piece of work with a history.

## There's a BUILD-VIEW.md in my project now, and my queue items have a "build block". What are they?

The build block is the short set of instructions attached to a piece of ready work. BUILD-VIEW.md is the file Claude builds from — assembled from those blocks, and refreshed every time a build starts.

Each piece of work in your queue has two halves. There's **why** you want it — the discussion, what you rejected, what changed your mind — and there's **what to actually do**: which files change, and how you'd tell it worked. The second half is now written into a marked-off block at the bottom of the item, agreed with you when the work is planned.

When a build starts, Claude generates BUILD-VIEW.md from those blocks and works from that instead of reading your queue.

**Why it's split that way**, because it isn't about speed:

- **Claude copies what it reads.** The reasoning written into queue items was found turning up, almost word for word, inside the method's own rulebook — reasoning quietly becoming rules. Claude can't copy what it was never shown.
- **Your reasoning is not deleted, or moved.** Your queue keeps every item's discussion exactly where it was. The view is a copy of one part, thrown away and rebuilt each time.
- **It still reaches your records.** When the session closes, Claude reads each finished item's reasoning back out of your queue and writes it into that session's record — so the why survives, it just arrives later.
- **Rejected options travel with the work.** If you already ruled something out, that goes in the block. Otherwise Claude would suggest it again and stop to ask you a question you'd already answered.

**What it costs you, which is worth knowing.** During a build, Claude can see a list of everything in your queue by name, so it can tell whether something it noticed is already written down. What it can't see is what depends on what. So if you mention something mid-build, Claude may not spot that it matters to a different item you have queued.

**You never write a block yourself.** They're written during planning, with you there, because deciding which half of an item is an instruction and which half is history is a judgement — no script can do it.

**If a ready item has no block**, the build stops on it and says so rather than guessing. That means it was never fully worked out, and it goes back for planning.

**Don't edit BUILD-VIEW.md** — it's overwritten every time. Change the queue item instead.

## Claude asked to put a date on one of my unprocessed ideas, so it stops coming up. What is that?

It is a way of saying "come back to this in March" about an idea that cannot go anywhere until something outside your project happens.

Planning normally works through your unprocessed ideas one at a time, and anything you don't settle comes back to the top next session. That is usually right — it is how an idea stays visible instead of quietly rotting. But some ideas are waiting on something nobody here controls: a reply from someone, a feature shipping in a tool you use, an answer from another one of your projects. Those cannot be settled however many times they are offered, so they get set aside again every single session.

A date fixes that. Claude names what the idea is waiting on, suggests a date by which there is plausibly news, and asks. If you say yes, a line saying `Not before:` and that date goes on the idea, and planning skips past it until the date passes. After that it comes up normally again.

**Three things worth knowing:**

- **You always get asked.** Claude never puts a date on an idea by itself, because a date takes something out of your sight without anything actually being resolved — how long you are content not to see it is your call, not Claude's.
- **Nothing else changes about the idea.** It stays an ordinary unprocessed idea. It has not been approved, rejected, or moved anywhere.
- **This is not for "I'll get to it later".** Something you simply haven't decided yet just gets set aside the ordinary way and comes back next session. The date is only for waiting on the outside world.

You can also just say no. Then it comes back next session as usual, which costs you one word to skip.

## If I run /rescan in the middle of something, do I lose what I was doing?

No. It hands back when it's done, and whatever was running carries on from where it was.

This is worth saying plainly because the wording used to suggest otherwise. `/rescan` looks back over the conversation for anything you decided, noticed or asked for that never got written into a file, and writes it down. It used to finish by saying a planning session would decide what happens to those things — which read like "this conversation is over, come back later", even when you were in the middle of a planning session that could have sorted them right there.

**Two things follow from that:**

- **Nothing is exited and nothing is restarted.** The instructions for whatever you were running are still in the conversation, so picking back up costs nothing.
- **If you're already planning, this session can settle what was just written down.** Sorting out captured ideas is exactly what planning does. You don't have to wait for a future session to look at something you noticed five minutes ago.

So you can run it whenever something occurs to you, mid-build or mid-plan, without weighing up whether it's worth the interruption.

## I complained about how Claude was talking to me, and now it wants to send a report. Why?

Because if the thing you disliked came from the method's own rules, then it is doing that to everyone using it — not just to you.

Claude keeps a private memory of your preferences: your name, the tools you like, how you prefer to work. For a long time, feedback about how Claude *talks* went in there too. That quietly did the wrong thing. Your session got better, and the rule that produced the annoyance carried on shipping to every other project, unchanged and unreported.

**So there is now a split:**

- **A preference nothing in the method governs** — you prefer metric, you go by a different name, you like a particular tool — is still just remembered. Nothing leaves your machine.
- **Something the method itself made Claude do** — a step that asked you the same thing twice, narration that buried the point, a warning that fired when it shouldn't have — becomes a report, because it is a fault in the tool rather than a fact about you.

**You are always asked, and you always see the exact words first.** Nothing is sent otherwise. You can say no, and then it is simply remembered the old way.

**Why this matters more than it sounds.** Very few people ever tell a tool's author that something about it is irritating to use. If your complaint gets quietly absorbed as "this user prefers shorter messages", nobody ever finds out the messages were too long for everyone.

## What is the short name in square brackets at the end of each queue item?

It's a handle — a short nickname for that piece of work, so you and Claude can point at it without retyping the whole description.

Every item in your queue has one, sitting at the end of its heading line, like `[login-screen-copy]`. It never changes, even when the item gets reworded or moved, which is the whole point: it is the one stable way to refer to a piece of work.

**You never have to write one, or use one.** Claude makes it up when the item is filed. "Let's do the login one" works perfectly well.

**Where you'll see it show up:**

- **In your session records.** When work gets built, its record is filed under that name, so you can trace a finished piece of work back to the item that asked for it.
- **Between items.** If one piece of work has to wait for another, the waiting one names the other by its handle — that's how Claude knows what is holding what.
- **In chat.** When Claude mentions one, it should also say what that item is about, so you never have to go and look it up.

If Claude ever throws one of these at you without saying what it means, that's Claude getting it wrong, and you can just ask.

## The plugin updated to a new version. Do I need to do anything?

No. A new version on its own asks nothing of you, and Claude will not suggest anything because of it.

Versions go up at every release, and most releases change nothing about your own files — a reworded instruction, a fixed bug, a tightened rule. Your project keeps working exactly as it did.

**There are three things that do ask you to run `/setup` again, and each one says so plainly when it happens:**

- **Your documents are on an older shape than the method now reads.** This one stops the session at the start and tells you so, because otherwise Claude would spend the whole session reasoning over a structure it is misreading.
- **A document or folder is missing** that the method now creates — a FAQ folder, a queue, a session-record folder.
- **A setting is missing** that the method has added since your project was set up.

If none of those is mentioned, there is nothing to do. Claude still tells you which version is installed at the start of every session, so you can see what you are on; that line is information, not a prompt.

**This used to work differently, and the change is worth knowing about if you saw the old behaviour.** Any version difference at all produced a line telling you `/setup` wanted a session of its own — and because only `/setup` records the version, that line came back at *every* session until you ran it. So a message that sounded urgent appeared over and over for a reason that was never real. Now the only things that ask are the three above, and each of them is a genuine gap in your project rather than a number that changed.

## Is anything I approve ever gone for good?

Almost never. Deleting something from your queue is your decision, not Claude's — an item is only dropped when you have said so, either by agreeing to a recommendation or by naming it yourself.

**And a deleted item is not really gone.** Your project's history keeps every version of every document, including the one from just before the deletion. If you change your mind an hour later or a month later, ask Claude to bring back the item you deleted, describing it however you remember it. Claude reads it out of the history and puts it back.

That is true of anything written into your project's documents — a queue item, a session record, a sentence in your spec that was reworded. The version before the change is still there.

**There is one exception, and it is one you chose.** When your project was set up you were offered the option of keeping your spec, your queue and your session records *out* of the project's history, so they are never published anywhere. If you took that option for a document, then nothing is recording its earlier versions — so an item deleted from a queue kept that way is genuinely gone, and Claude will tell you plainly at the time rather than promising a recovery it cannot make.

Claude also says which of your documents are in that state at the start of every session, so you are never guessing which case you are in.

## What is the brevity style Claude offered me at setup?

It's a setting that keeps Claude's replies in this project short and decision-led — the first thing in every message is the thing you need to see or act on, with the explanation available when you ask for it. On projects like these, which carry a lot of documentation, Claude tends to run long, and long replies bury the one thing you needed to catch.

**Saying yes changes this project only.** The setting is written into this project's own settings file. Nothing outside the project changes, and if you already had a style of your own set, your style file is never edited — though while the brevity style is the project's setting, your own choice isn't the one applying here, which is why Claude names your style and any differences before you decide.

It takes effect at the next session (or after /clear) — styles never change a conversation already under way.

**If you said no**, nothing is set, and each session opens with one short line noting the style is not enabled — a statement, not a nag. You can take the offer later by running /setup again, or set it yourself in the project's settings.

## What is a cycle?

A cycle is a named piece of recurring work — a weekly release, a posting rhythm, a maintenance pass — defined once and then driven by the queue like everything else. Ask for one during a planning session and Claude writes the definition with you into a `CYCLES.md` file your project gains the first time: the thing the cycle produces, the steps of one turn, how often it runs, and the visible sign that a turn was completed (a release's date, a line in a sent-record).

Nothing keeps a schedule or stores a position. At the openings and closes of planning and build sessions, Claude reads the definitions, checks each cycle's visible sign, and — where a turn is overdue — files one item into your queue for it. That item is then weighed and built like any other work, and no duplicate is filed while one is still open. A project with no cycles has no `CYCLES.md` and pays nothing.

Claude may also offer a cycle once when it notices you working the same artifact repeatedly — creating one is always your call.

## At the end of a session Claude said a piece of ready work has a problem. What are my options?

Two, and it's worth knowing which one you're being offered.

**If you tell Claude to fix the item, it can.** When you direct a change to a piece of work during a close — its reasoning, or what it says should be built — Claude makes that change and records it in the session record under that item's name. You're there and deciding, which is the same authority a planning session runs on.

**If Claude is the one who spotted the problem, it won't quietly fix it.** Instead it writes the problem into your queue as something to look at, and tells you plainly that the item in question is ready to build — so it will run in your next build session, as written, unless you direct the change now.

That second message isn't Claude asking permission to do its job. It's there because a piece of ready work is about to be built, and this is the last moment anyone can say otherwise. Either answer is fine: direct the change and it happens, or leave it and the work runs as it stands, with the concern sitting in your queue for the next planning session.

What Claude won't do is change a piece of ready work on its own judgement at a close. Work is agreed with you during planning, and a close is the point in a session where your attention is lowest.
