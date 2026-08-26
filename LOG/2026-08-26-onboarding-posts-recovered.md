# [HASH] — The six onboarding forum posts, recovered verbatim into the record

These six Discord how-to forum posts were written and published from a browser chat on 2026-08-25, outside this project's own drafting route — so no outbound-register line and no FAQ entry was written for any of them at the time. See [onboarding-posts-outside-the-record].

Alex supplied the text afterwards, one post at a time, on 2026-08-26. **This file is the verbatim record the outbound register points at.** It exists because a register line must point at the text a post actually carried: a line written from memory would be a claim about what was posted rather than a record of it, and the register's job is to be what a later repeal is checked against.

They are described as fixed posts. Her reasoning for not expecting many more: the basic instruction set should stay simple and concise.

**Destination for all six:** the Throughliner Discord, the how-to forum — named `how-to-throughliner` with a question-mark emoji leading the name. Recorded as she described it rather than reproducing the exact glyph.

---

## 1. How to install

Published 2026-08-25 to the Throughliner Discord, how-to forum.

> **If you already have Claude Code:** Open a chat in Claude Code and say:
>
> > Please add the plugin marketplace `FlintcraftTech/throughliner` and then install the `throughliner@flintcraft` plugin from it.
>
> Then fully quit using the task manager, and then reopen Claude Code so it loads.
>
> **If you're new to Claude Code (or not sure):** Open a fresh chat at [claude.ai](https://claude.ai) in your browser and paste this:
>
> > I want to install the Throughliner plugin for Claude Code. Please read this install guide and walk me through it one step at a time: https://github.com/FlintcraftTech/throughliner/raw/main/INSTALL.md
>
> Claude will read the guide and take you through everything — Claude Code install, paid plan, plugin install, and a smoke test. No terminal experience needed.
>
> **You'll need a paid Claude plan** (Pro is enough). Claude Code doesn't work on the free tier.

**What it claims, for the repeal check:** that the two-command install is a marketplace add followed by a plugin install, both runnable by asking Claude Code in plain English; that a full quit and reopen is required for the plugin to load; that the browser route is a single pasted prompt pointing at the raw INSTALL.md URL, and that the guide covers Claude Code install, paid plan, plugin install and a smoke test; and that a paid plan is required, Pro being enough.

**Checked against the repository at recovery time:** the marketplace and plugin identifiers match README.md's install section, and the raw INSTALL.md URL is the one README.md line 17 already gives. INSTALL.md exists and carries the Claude-facing instructions the browser route depends on.

---

## 2. Running your first session

Published 2026-08-25 to the same forum.

> Open your project folder in Claude Code (**"+ new" at top left**), type `/setup`, and press Enter twice. Claude interviews you about what you're building and creates your project documents — SPEC, QUEUE, LOG, FAQ.
>
> Don't overthink your answers. Plain language is fine, and nothing is locked in — your next step is a `/plan` session where you organise your first work, so anything you missed gets sorted there.
>
> ### What to expect
>
> - **What are you building, and for whom** — describe it however makes sense to you
> - **Brevity style** — whether Claude keeps replies short and decision-led (HIGHLY recommended especially for Opus 5)
> - **Public or private repo** — if public, it asks about a licence
> - **Keep planning docs out of the repo** — your SPEC/QUEUE/LOG hold your reasoning; worth keeping out of version control if your repo is public
>
> ### Big ideas with multiple parts
>
> If your project has several distinct pieces (app, website, business plan, timeline), you can start with one big Throughliner project in the parent folder. When a part outgrows the parent queue, open its subfolder and run `/setup` there — Throughliner detects it's inside an existing project, reads the parent spec, and asks which part this covers. The subfolder becomes its own full project. This is called a **pop-out** and it's irreversible by design. You don't need to plan for it upfront.
>
> ### After a plugin update
>
> If you update Throughliner on a project that was set up under an older version, `/setup` will run again — it migrates your existing documents to the current format rather than replacing them.
>
> ### After /setup
>
> Run `/plan` to scope your first piece of work, then `/next` to build it. The cycle: `/plan` → `/next` → `/done` → fresh chat → repeat.

**What it claims, for the repeal check:** that /setup interviews the user and scaffolds SPEC, QUEUE, LOG and FAQ; that the interview covers what is being built and for whom, the brevity style, repository visibility with a licence question where public, and keeping the planning documents out of the repository; that running /setup in a subfolder of an adopted project detects the parent, reads its spec, asks which part the subfolder covers, and pops it out irreversibly into its own project; that /setup re-runs after a plugin update and migrates existing documents rather than replacing them; and that the working cycle is /plan, /next, /done, fresh chat.

**One claim was not true of the installed plugin when this was posted, and still is not.** The pop-out paragraph describes [subprojects-pop-out], which was built on 2026-08-26 — the day *after* this post went out — and has not been released. Checked rather than assumed: the installed plugin is 1.20.0-test18 and its `setup.md` contains no pop-out case at all, so a beta tester following this paragraph today gets an ordinary adoption of the subfolder with no parent detection, no spec read and no confirmation. Filed as [onboarding-post-claims-unreleased-popout]. Everything else in the post holds against the installed build.

---

## 3. Running /plan for the first time

Published 2026-08-25 to the same forum.

> After finishing your first`/setup` session, type `/plan` and press Enter. This is where you and Claude figure out what to build and in what order.
>
> ### What you actually do
>
> Talk. Describe what you want, share ideas, answer Claude's questions. Claude does the heavy lifting — it checks your queue for consistency, asks design questions, and files everything. You can interrupt at any time to bring up a new idea or change direction. There's no wrong order.
>
> ### How the queue works
>
> Everything you want to build lives in your QUEUE. It has two main zones:
>
> **Unprocessed.** New ideas land here as **captures**. They're rough — just enough to remember what you meant. Captures can come from you at any time while using Throughliner (no matter what skill as been run), or from Claude noticing something mid-build, or from `/rescan` picking up things you said or Claude thought but were never filed.
>
> **Above the line — processed.** When you and Claude agree a capture is ready — it's scoped, the files it touches are known, design questions are answered — it moves above the line and becomes **ready work**. This is `/next`'s work list.
>
> ### What /plan does at the start
>
> Before you get into new ideas, `/plan` opens by checking the queue for problems — work marked ready that contradicts its own notes, items with no files listed, circular dependencies. It reports what it finds and you decide what to do. Just answer "go" when it finishes the first turn, and it will walk you through all the above as per procedure.
>
> ### Tips
> - Rough ideas are fine. "I want some kind of settings page" is a perfectly good capture.
> - You don't have to process everything in one session. `/plan` → `/done` → fresh chat → `/plan` again is normal, you do not have to progess to /next until ready.
> - it's good practise to clear enough items just justify a /next run before /done.
>
> ### What's next
>
> Once you have work above the build line, you're ready to build. That's what `/next` is for — covered in the next post.

**What it claims, for the repeal check:** that captures may be filed from any chat whatever skill is running, by the user, by Claude mid-build, or by /rescan; that a capture becomes ready work once it is scoped with its files known and its design questions answered; that the ready work is /next's work list; and that /plan opens by checking the queue for problems, naming three by example — work marked ready that contradicts its own notes, items with no files listed, and circular dependencies.

**Every claim above is true of the installed build.** The three named problems are exactly the placement contradictions the queue digest computes and the opening reports.

**Two imprecisions, recorded because a later reader should not mistake them for the model.** The post describes two zones, Unprocessed and above-the-line-processed, which collapses the real shape: there are two *sections*, Processed and Unprocessed, and a readiness line *inside* Processed with a held region beneath it. A user whose work gets held below that line will not find it described here. And the opening's actual question is whether anything should be prioritised or whether Claude should pick the order, so "answer go" is a paraphrase of a question that is not put that way.

**One divergence created after posting, worth knowing when the post is next touched:** this project settled **"the ready list"** as the standing plain-English name for that region on 2026-08-26 ([keep-approval-reading-burden]), so a session on the next release will say "the ready list" where this post says "above the line".

---

## 4. Running /next — start building

Published 2026-08-25 to the same forum. Its title carries a leading number and a construction emoji. The paste this was recovered from also carried the forum's own chrome — the poster's handle and a relative timestamp — which is not post content and is left out.

> Once `/plan` has moved enough work above the build line, you can type `/next` and press Enter twice. Claude picks the top piece of ready work and builds it. The scope of the build is locked to the files slated for edit, and Claude won't add a file to this list without asking first.
>
> **What happens**
>
> Claude reads the item's scope — what it does, which files it touches — and builds it. It stays locked to that scope. If it notices something outside the current job, it files a capture in your queue and tells you why, rather than silently deferring or wandering off.
>
> If you have several pieces of ready work above the line, `/next` can build them back-to-back without you confirming each one. It works through everything marked ready, stopping only when it really needs you.
>
> **Work tags**
>
> Not all work runs the same way. Items can be tagged:
>
> `[audit]` — Claude reads and reports without editing anything. Findings route to captures in queue for later processing in `/plan`.
> `[user]` — Claude walks you through doing it yourself, live. These run at end of a `/next` session, after all the Claude work.
>
> **If you want something mid-build**
>
> If you ask for something that isn't part of the current job, Claude files it as a capture and explains why. Ask a second time and a small change gets done on the spot.
>
> **When the build is done**
>
> Type `/done` to record what happened and commit. Claude tells you what's next and stops — it won't invite you straight into another build. Start a fresh chat for your next session.
>
> The full cycle: `/plan` → `/next` → `/done` → fresh chat → repeat.

**What it claims, for the repeal check:** that a build is scope-locked to the files the item names and no file joins that list without asking; that work outside the current job is captured with a reason given rather than done or silently dropped; that several ready items build back-to-back with no per-item confirmation; that `[audit]` reads and reports without editing and its findings become captures; that `[user]` work is walked through live and runs after all the Claude work; that a second ask for a small change carries it through on the spot; and that the close records, commits, and does not invite another build.

**Every claim above is true of the installed build**, including the two-pass ordering that puts `[user]` items after the Claude work and the second-ask yield.

**One omission, not an error.** The post lists two tags; there is a third, `[freeform]`, which /next halts on rather than building. A beta user is unlikely to meet one, since flavors are settled during planning, but a reader taking this list as complete would be surprised by the halt.

**One thing this session changed underneath it, which does not falsify the post:** the yield rule gained an arm for a queue move the user explicitly directs mid-run ([build-refuses-user-queue-move]). The post's account of the second ask stays accurate; there is now simply more that a direction can carry through.

---

## 5. Ending your session with /done

Published 2026-08-25 to the same forum. Its title carries a leading number and a notebook emoji; the forum chrome in the paste is again left out.

> When a build or planning session is finished, type `/done` and press Enter. Claude records what happened in your LOG — decisions made, work completed, anything still open — and commits.
>
> **Why this matters**
>
> Without `/done`, while a session's work is may still be in your code, but the reasoning behind it isn't yet on the record. So once you've finished your session, always run `/done`.
>
> **After /done: clear the context**
>
> Start a fresh chat. Either type `/clear` or open a new conversation entirely.
>
> This isn't optional housekeeping — it's how Claude Code works well. Every message in a conversation takes up space in the context window, and a long session fills it. Once it's full, Claude starts losing track of earlier details — instructions get fuzzy, scope drifts, mistakes creep in. A fresh chat gives your next session the full window to work with. Future sessions know what already happened from your reading your LOG (written to in `/done`), and what is planned from reading your QUEUE.
>
> **The habit**
>
> Every session ends the same way:
>
> `/done` — record to LOG and commit
> `/clear` or new chat — reset the context
> Start your next `/plan` or `/next` with a clean slate
>
> `/done` before `/clear`, always. If you `/clear` first, the session's history is gone before it was saved.

**What it claims, for the repeal check:** that /done records what happened to the LOG and commits; that the code may exist without the reasoning until it runs; that a fresh chat should follow every close; that a later session learns what happened from LOG and what is planned from QUEUE; and that clearing before closing loses the session's history.

**Every claim above is true of the installed build**, including the last one, which is the sharpest and the most load-bearing: a close run in a fresh chat has none of the session's thinking in view, so there is nothing left to re-scan.

**Two sentences carry copy errors, in a post beta testers read tomorrow.** "while a session's work is may still be in your code, but the reasoning behind it isn't yet on the record" has a stray *is* and a *while*/*but* that fight each other; and "from your reading your LOG" repeats a word. Neither changes what the post claims. Recorded here rather than filed as work, since fixing them is one edit whenever the post is next opened — for instance alongside [onboarding-post-claims-unreleased-popout], which may require an edit anyway.

**Nothing this session changed touches it.** The close gained a fresh disk read for cycles, a response-shape tag, silent cleanup of the generated view and optional co-author trailers — none of which this post describes.

---

## 6. /rescan — catching what you missed

Published 2026-08-25 to the same forum. Its title carries a leading number and a telescope emoji; the forum chrome in the paste is again left out.

> A rescan runs automatically inside `/done`, but it's also a standalone skill you can run any time. Type `/rescan` and Claude reads back over everything still in the conversation — its own thinking, your comments, stray ideas — and files captures for anything that wasn't picked up.
>
> **Why it's a standalone skill**
>
> The `/done` rescan is a safety net: it catches things before the context is cleared. But if you're in a `/plan` session and you want new ideas to land in the queue before you finish, you need them filed before `/done`. That's what running `/rescan` mid-session is for.
>
> This makes it a speedrun tool for ideation. Talk freely in `/plan`, throw out rough ideas, let Claude think out loud — then run `/rescan` to sweep everything into captures. Now those captures are in your queue and can be processed in the same session, potentially making it above the build line and into your very next `/next`.
>
> **What makes it interesting**
>
> Claude doesn't just rescan what you said. It reads back over its own reasoning — the thinking it did while working through a problem — and files ideas that came up in its own process but were never explicitly discussed. These are often good, because they come from Claude having actually worked with your code and your spec, not from general knowledge.
>
> **When to use it**
> Mid-`/plan` when you've been freewheeling and want to bank what's been said
> Midway in a long session, before compaction is run (`/rescan` can't see much past compact point)
> Any time you feel like the conversation held more than what made it to the queue
>
> Remember, `/rescan` will only look back as far as Claude can see, and up to the last time `/rescan` was run in that session; no earlier. It won't waste time scanning chat that's already been combed through with `/rescan` once.

**What it claims, for the repeal check:** that a rescan runs inside /done and also standalone at any time; that it reads back over the conversation including Claude's own thinking and files what was never picked up; that captures filed mid-/plan can be processed in that same session and reach the ready region for the next /next; and that a scan reaches only as far back as Claude can still see, and no earlier than the last /rescan in that chat.

**Every claim above is true of the installed build.** The same-session processing claim is worth stating precisely, because this project changed something adjacent to it on 2026-08-26: processing filed captures in the same planning session was always available, since a skill's instructions stay loaded for the rest of the chat. What [rescan-offers-processing-in-plan] added is that /rescan now *offers* it rather than leaving the user to know it was possible. So the post described a real capability and the change makes that capability easier to reach.

**One omission.** /rescan routes by the three-way triage — work still to do becomes a capture, but what already *happened* is appended to the session's record as a marked tail, which is what makes it the one-word route for work done after a close. The post describes only the capture half, so a reader would not know the post-close use exists.

**One tension worth naming rather than treating as an error.** The post advises running it "midway in a long session, before compaction is run", which asks the user to judge by session length. This method forbids *Claude* from naming length, duration or message count as proxies for compaction, on the grounds that each stands in for something not observable at all. Advice to a user about when to reach for a tool is not the same act as Claude discounting its own coverage by a fictional factor — but the two sit close enough together that anyone reworking this post should know the rule exists.
