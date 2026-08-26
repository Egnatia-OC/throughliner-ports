# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### [user] Verify the cycles due-ness check live: one capture filed when due, no duplicate on the next opening [cycles-due-check-verification]
Filed 2026-08-22 at the keep-step, on Claude's recommendation and your agreement. The cycles build ("Cycles shipped", record `2026-08-22-cycles-definitions-and-due-checks-build.md`) ticked done with one behaviour UNCONFIRMED: only the no-doc silent path was exercised, because this project has no cycles doc. Confirming it needs a live session in a project whose `CYCLES.md` carries a past-due observable — user work, since it happens in another project's session during your testing days. The release-cycle definition item ("Define this project's weekly release cycle") is held on this verification and lifts when it closes — timed so the definition can build before Wednesday 10am.
**Walkthrough.**
1. In any project you're testing the rezip in (not Taskflowapp's product files — its INBOX is the only sanctioned write there, so pick another test project), ask Claude to create a test `CYCLES.md` at the project root with one definition whose observable is already past due — say a weekly cycle whose last completed turn reads as two weeks ago.
2. Run /plan (or /next) there. Look for: one capture appearing in that project's queue under the cycle's slug, naming the due step.
3. Run another opening in that project without touching the capture. Look for: no second capture — the check is satisfied while one is open.
4. Ask Claude there to delete the test `CYCLES.md` and the test capture.
5. Tell this project what you saw; this line closes and the definition item lifts.
**Held 2026-08-26 at the planning close.** The feature this verifies is confirmed not to fire on the installed build ([cycles-check-fires-nowhere], whose fix is cleared to run) — walking this before that fix ships and a rezip lands can only reproduce the known failure. The dependency is host-side: it lifts once the fix is built and the host reinstalled.
**Lifted 2026-08-26 at the next planning opening.** The fix was built in the 2026-08-26 build run (`2026-08-26-cycles-check-fires-nowhere-build.md`) and the host has since been reinstalled at 1.20.0-test20, so both halves of the lift condition are met.

#### [user] Pick the release build at the end of the next build run, then say the word and the release runs [expedite-first-beta-release]
**The remaining job of the release-day item, rewritten 2026-08-26 at this planning opening; kept as `[user]` on your direction — the pick happens at the end of the next build run, in that same session, not in a run of its own.** Your decision stands: the first beta releases today, from main, marked pre-release, on your word — nothing about the release rules changes. The morning announcement's text and claims are in `LOG/2026-08-26-beta-announcement-recovered.md` with its register line in `INBOX/sent.md`. Releasing the current build resolves [onboarding-post-claims-unreleased-popout] down its nothing-to-change branch. Today is beta-only — no prior beta exists to promote to stable.

**The pick, your decision:** test20 is the hoped-for candidate, judged only after this /plan and the next /next have run on it; **the previously installed rezip (test19) is the named stable fallback** — it held up in use, so if test20 shows problems the release goes from it rather than waiting. Checked at this opening: no release has run yet — the newest GitHub release is v1.20.0 from 2026-08-09.

**What was settled at this opening and relocated:** the Wednesday stable-label selector and its argument are on [weekly-release-cycle]; the no-collision note is on [beta-tester-pathway]; the nerds-list packaging question closed as no-packaging-for-now (entries carry label, version and date — no downloads until a nerd asks for one); the chain question closed by lifting [cycles-due-check-verification]. Fuller history is in `LOG/2026-08-26-expedite-first-beta-release.md`.

**Walkthrough.**
1. At the end of the next build run, Claude reports how the run went on test20 — anything that failed, anything patched. You'll see that before deciding.
2. You pick: release from test20 (patched and re-zipped if the run found problems worth fixing), or fall back to test19. Look for: your own judgment of whether this session and that run went well — that's the whole test.
3. Say the word; Claude runs the release ritual from main (`resources/release-ritual.md`), marked pre-release.
4. Look for: the new release visible on the GitHub releases page. This line closes when you confirm it's up.

#### [user] Post the live-dangerously beta announcement and pin the nerds-channel first message [beta-day-one-posts]
Drafted 2026-08-26 in the post-close tail, both approved by you in conversation; your theme, in your words: "live dangerously" — honest about faking it, because there's never a good time, you don't believe in perfection, and ready-for-testers is good enough. Your decisions carried in the drafts: every server member (14 on the day) gets the **nerd** role as a day-one prize; the rezips' dangers stated straight up in both texts; the install link points at the how-to forum post as the most reliable route; "will be the safest pick" tense on your correction, since the real beta cycle is not running yet. **Post only after today's release is published**, and verify both texts against the shipped build first — the announcement claims the release exists and describes today's timeline. One-a-day pacing applies to the announcement; the channel pin is channel furniture, not a feed post. Both go in `INBOX/sent.md` with their claims when posted, and FAQ potential is weighed at posting per the announcement-time rule.
**Walkthrough.**
1. After the release is up, Claude re-verifies both drafts against the shipped build and shows any needed corrections.
2. You post the announcement in the main channel, grant the nerd role to all members, and pin the channel message in the test-rezips channel — Claude has no route to Discord.
3. You confirm; both register lines are written and this line closes.
**Announcement draft (under 2,000 characters):**
> **The first beta is out — and we're living dangerously. 🎲**
>
> I'll be honest about how this is happening: I'm shipping before it's perfect, because there's never a good time and I don't believe in perfection. The tool is ready for testers, and that's good enough. Today's release is brand new — today's build, patched and re-run this afternoon on top of the version I've been living in since it landed late last night. Very fresh, but not untested.
>
> **Install it the reliable way:** follow the pinned "How to install" post in the how-to forum — that's the tested route, and Claude walks you through it in plain English.
>
> **Day-one prize: everyone here gets to be a nerd. 🏅** All 14 of you are getting the **nerd** role, which opens the test-rezips channel — a running list of my raw development builds, posted as I make them, each labelled honestly: stable (with caveats), not stable (with the problems named), or under testing — use at your own risk.
>
> **What's dangerous about them, straight up:** test rezips are snapshots of work in progress. They haven't soaked, some have known failures written right on the label, and a bad one can misbehave in your project's files. The beta release will be the safest pick; the rezips are for people who enjoy the bleeding edge and will tell me what broke. Either way — keep your projects in git (Throughliner sets this up by default), and report anything odd in the support channel.
>
> Thanks for being here on day one. This is exactly the group I wanted to break things with. 💖
**Channel first-message draft (to pin):**
> **Welcome, nerds. 🤓 Read this before installing anything from here.**
>
> This channel is a running list of my raw development builds ("test rezips"), posted as I make them. Each entry carries one of three labels:
>
> **stable - [caveats]** — I've run it and it held up, with any caveats named.
> **not stable - [problems]** — it has known failures, listed on the entry. For the curious only.
> **under testing - use at your own risk** — too new for me to vouch for either way.
>
> **What's dangerous, straight up:** these are snapshots of work in progress. They haven't soaked, a label describes only what I'd seen when I posted it, and a bad build can misbehave inside your project's files — writing where it shouldn't, or mangling the documents Throughliner manages. Keep your projects in git (Throughliner sets this up by default), so anything a bad build does can be rolled back.
>
> **The safe route is the beta release** — pinned in the how-to forum. Use this channel only if you enjoy the bleeding edge and will tell me what broke.
>
> **When something breaks:** tell Claude about it right there in your Claude Code chat. It knows the reporting route — it'll draft a GitHub issue on the Throughliner repository and post it with your yes (or, without the GitHub CLI, draft a report for the form for you to paste). Mention the build label you were on. Every report makes the next beta better.
>
> The list keeps the newest builds; I prune old entries by hand. When the proper beta cycle starts, this channel stays for the brave.

#### [user] Post the first test-rezips channel entry: the build today's release ships [nerds-list-first-entry]
Raised by you 2026-08-26 at the next planning opening, processed now on your direction. The first entry in the locked test-rezips channel, posted by hand. Its subject is the rezip today's release is cut from — the rezip and the release are the same code that day, so the entry describes the released build, whichever of the two candidates you pick (test20, or the test19 fallback recorded on [expedite-first-beta-release]). The label is yours to write at posting, in your own three-label wording; this first entry can honestly carry "stable" since the build you pick is the one that just survived a planning session and a build run. Entries carry label, version and date only — no downloads, per the no-packaging-for-now decision on [weekly-release-cycle]'s record.
**Walkthrough.**
1. After the release is published, Claude updates the draft below to name the released version and the build it was cut from, and shows it to you.
2. You post it in the test-rezips channel, with your label and any caveats in your own words — Claude has no route to Discord.
3. You confirm; a register line goes in `INBOX/sent.md` with what the entry claimed, and this line closes.
**Draft (to update at step 1):**
> **[released version] — cut from [rezip name], released [date]**
> Label: stable - [your caveats]. This exact build is today's beta release: it ran a full planning session and a build run before shipping, and it's the same code beta testers get from the install route.

#### [user] Onboarding post describes pop-out as working, and it has never been released [onboarding-post-claims-unreleased-popout]
Found 2026-08-26 while recovering the onboarding posts into the record. The "Running your first session" post, published 2026-08-25, tells readers that running `/setup` in a subfolder of an existing project detects the parent, reads its spec, asks which part the subfolder covers, and pops it out into its own project.

**That behaviour was built on 2026-08-26 — the day after the post went out — and has not been released.** Checked rather than assumed: the installed plugin is 1.20.0-test18 and its `setup.md` contains no pop-out case at all. A beta tester following that paragraph today gets an ordinary adoption of the subfolder: no parent detection, no spec read, no confirmation, and none of the irreversibility warning the paragraph promises is built in. The rest of that post holds against the installed build.

**This is the shipped-only rule failing in the direction it was written to prevent** — every claim in a post is meant to be true of the installed plugin at the moment it is posted. It reached the public forum because these posts were drafted outside this project's own route, where that rule and the register line that makes claims checkable both live. The same gap is [onboarding-posts-outside-the-record]; this is the first concrete harm from it.

**Resolved at processing 2026-08-26 down the nothing-to-change branch:** [expedite-first-beta-release] settled today's release as going from the current build, which carries pop-out — so the claim becomes true when the release publishes. Filed as `[user]` because only Alex can read and edit the forum post; kept for the confirming half.

**Walkthrough.**
1. After today's release is published, Claude confirms it went out from a commit carrying the pop-out case (the released commit's `setup.md` contains it). You'll see that confirmation before your step.
2. Open the "Running your first session" post and re-read its pop-out paragraph knowing the claim is now true of the released build. Look for: nothing to change.
3. Tell this project; the register line's untrue-when-posted warning in `INBOX/sent.md` is updated and this line closes.

#### [user] Smoke-test the `#beta` install on your second machine, then edit the how-to post's install command [beta-install-smoke-and-post-edit]
Filed 2026-08-26 with [beta-branch-install-pin]. Two sequential user steps: the ref-pinned route is unverified against the open feature requests the research names, so it is proven on a real second machine before any tester is pointed at it; and the published "How to install" forum post claims the plain two-command route, which the pin falsifies — the correction is yours to make, per the repeal-falsifies-an-announcement rule.
**Walkthrough.**
1. On your second machine, open a fresh Claude Code chat and ask it to add the plugin marketplace `FlintcraftTech/throughliner#beta` and install `throughliner@flintcraft`. Look for: both commands succeed without a ref error.
2. Fully quit and reopen the app, open any empty folder, and type `/setup` in the chat box. Look for: the setup command appears in the menu — the smoke test from INSTALL.md.
3. If either step fails, tell this project the exact error and stop — the install post stays as it is and the pin gets re-examined.
4. On success, edit the "How to install" forum post so its install ask names `FlintcraftTech/throughliner#beta`. Look for: no live claim pointing new users at the unpinned route.
5. Tell this project; the register line for the install post is updated with the corrected claim and this line closes.

--- Cleared to run above this line ---

#### [user] Write the article comparing Throughliner to memory-system approaches, finishing with what shipped [competition-comparison-article]
**Captured by you 2026-08-15**, from a discussion prompted by Discord talk about "Obsidian memory systems" and "dreaming". **Your framing and your decision: the analysis reads as an article starter for the Throughliner site, and rather than sending it now it should be captured and finished with our shipped solutions, with the announcement doubling as a Discord post.**

**This is your own shipped-only rule applied correctly, and you reached it independently.** `CLAUDE.md` says a post announces only what has shipped, and that where a post describes work designed but not built, it waits for the build and is filed as a queue item naming what it waits on. That is exactly this.

**Your stance on the article's framing, recorded 2026-08-17 and NOT generalised into a rule.** Claude proposed turning it into a standing rule about all writing describing Throughliner, and you refused: it *truly depends what we are writing, and the tone required*. Claude had also flattened the position itself — writing "no stake in persuading anyone that one approach beats another" where **your actual position is that you have a stake, just not in being seen as the best thing since sliced bread.**

**Your assessment of the draft, which is the live problem with this item.** It swung from hard marketing to substantially explaining why the competition is better. You sent it to the other project for polishing rather than continuing here, because you wanted to move on — so the draft is out of this project's hands and the item covers what comes back.

**The queue-read weakness is NOT answered, corrected 2026-08-19, and this must be right before the article goes out.** It once read that the article's weak points — manual curation and a 56,000-token queue read — were answered by [digest-reports-computed-fields-not-summaries]. That became false on 2026-08-17, when the digest was expressly stopped from replacing the read: a planning session now runs the digest **and** reads the whole file, because the digest computes facts and the file carries the reasoning. So the full read is still paid, deliberately.

**What actually addresses it is unbuilt.** [split-the-cleared-region-for-concurrent-sessions] gives a build a derived view and stops it reading the queue at all. **Under the shipped-only rule the article cannot claim that until it ships**, and the honest line if it goes out sooner is that planning still reads everything and the reason is that reasoning across items is what planning is for.

**Read this paragraph before drafting.** A `[user]` item sitting cleared to run, producing public text, is exactly how [discord-post-context-adjacency] was nearly posted about a mechanism that no longer existed.

**The substance, drafted in discussion and to be rewritten rather than pasted.** *Stronger:* typed documents with defined roles versus an undifferentiated note graph, so product truth, pending work and history each have a home; memory coupled to execution, since /next builds from the queue rather than merely reading it; the throughline carrying *why* rather than only what; deletion as a user-approved fate decision rather than an automatic prune; and everything as plain markdown in git, reversible and auditable. *Weaker:* curation is manual, which is dreaming's entire job — sixty unprocessed items with duplicates accumulated over weeks, seven merges by hand, six items found behind already-shipped blockers; scale, where graph retrieval never needs to read everything; and one-way links, where backlinks are derived for free.

**The verification step runs BEFORE drafting, and is not optional.** `resources/research/auto-memory-staleness.md` is dated 2026-06-09 and names AutoDream as Anthropic's own consolidation sub-agent — two months old, and what the Discord means by "Obsidian memory systems" may be a specific community project rather than the general vault-as-memory pattern. **Publishing a wrong description of someone else's system under your name is worse than publishing nothing**, and unlike everything else this project writes, it is a claim about a third party. Search first, update the research file, then draft.

**Two artifacts, not one text, settled at capture.** The article is the full piece and may be long, may discuss competitors, and may say where Throughliner is weaker. The Discord post is capped at 2,000 characters, takes the shipped fix as its subject with the comparison only as framing, and points at the article. One text serving both would either saddle the announcement with a comparison it doesn't need or truncate the article into a changelog.

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes**, and Claude has no route to Discord or to the site — the user posts both.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**Only the final step yields to the one-a-day chain.** Three posts are queued ahead of it, and the pacing rule applies to the post rather than to the writing — so the item is cleared and the article can be drafted whenever. Carried as prose today because there is no way to write a date; once [not-before-date-field] ships, this becomes a `Not before:` line.

**Walkthrough.** Authored 2026-08-22 at processing, closing [article-walkthrough-missing].
1. Claude re-checks the two 2026-08-15 findings still hold before drafting — AutoDream's status, and whether "Obsidian memory systems" now names a specific project — offering a fresh web search; anything changed is corrected in `resources/research/auto-memory-staleness.md` first. You'll see what the check found before the draft starts.
2. Claude drafts the full article: names the specific system it compares against or says plainly it describes the general vault-as-memory pattern, and is honest that automatic curation now ships in the base tool — the case made is why typed documents and user-approved deletion are worth the manual cost.
3. You read it and say what to change; repeat until you're satisfied.
4. You decide delivery: an INBOX message to the site project (you see the exact text first) or you carry the file across yourself. Claude does whichever you pick that it can.
5. Claude drafts the Discord post — under 2,000 characters, the shipped fix as its subject, pointing at the article.
6. You publish both — Claude has no route to either. The post yields to the one-a-day chain: it goes out on a day no other Throughliner post does.
7. You confirm both are up; the send is recorded in `INBOX/sent.md` and this line closes.

**Held 2026-08-24 on your decision, made during this item's walk-through.** Drafting stalled because Claude didn't have enough how-Throughliner-works material to draw on, and the thinking fell to you. The announcement-driven FAQ shipped 2026-08-24 and fills as announcements are posted, so the material accumulates over time; `ANNOUNCEMENT-IDEAS.md` also now carries the retired FAQ's entries — exactly the material the drafting lacked. The recovered draft did not satisfy you, so this is a redraft when it resumes, not a patch. No single queue item completes as the blocker, so the hold is a date: when it passes, the lift judgment is whether the FAQ actually has enough on the relevant features — not automatic.
Not before: 2026-09-21

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected). [comparison-article-post-needs-rewrite] follows this item — the post's rewrite runs against the final article, so it is held on this slug.

#### [user] Article: Throughliner as a memory prosthetic — built by someone with bad recall, for a brain that avoids looking back [adhd-memory-prosthetic-article]
**Your idea, 2026-08-22, seeded from a grab bag of paragraphs from a conversation you had with Gemini** — processed the same session. Your own caveats set the editing brief: the parallels it draws between AI and human memory, and between the method's docs and memory types, are not all trusted; the 15-year-project storytelling is under-developed; there is a lot of lecturing and probable doubling-up.

**The core story, which is the article's force.** Throughliner is your coping mechanism for ADHD — advertised as a memory system for Claude, built by a person with bad recall. Friends encouraged you back into a project based on an interest you feel you have failed to build anything from in 15 years; on opening it, Claude immediately picked up audits and research planned six weeks earlier that you had completely forgotten — "a pleasant slap in the face. My memory system has got my back." The difference is invisible in projects you are continuously in; the long gap is what made it visible.

**Venue chain, your decision:** flintcraft.tech first, then a YouTube version, then potentially LinkedIn. This item covers the site article; YouTube and LinkedIn adaptations are follow-on work to file once the article exists.

**Disclosure settled, 2026-08-22: you are comfortable with the personal content everywhere it goes.** The photos-and-childhood-trauma element is on the chopping block for FOCUS, not privacy — your reason: its only connection is that you couldn't look back at your project much as you reflexively avoid your photo roll, and the rest may detract from the Throughliner selling points. The aversion analogy can survive as a sentence; decide the final cut at drafting.

**Science route, your decision: verify, keep only what fits.** The seed asserts amygdala-heavy encoding, dopamine deficits, episodic/autobiographical memory impairment in ADHD, trauma generalising recall into a threat, and a docs-to-memory-types mapping (LOG as episodic, FAQ as semantic, QUEUE unmapped). Before drafting, web-search each claim; file what holds in `resources/research/` with its index line; anything unsupported is cut or reframed as your first-person experience. The docs mapping is an analogy at best and is presented as one if kept.

**Known defects in the seed, to fix at drafting:** it names doc files Throughliner doesn't have (BACKLOG.md, UX.md, claude.md as the method's docs) — use the real four; the lecturing register and the repetition go; "brilliant" self-praise inherited from Gemini's voice goes.

**Walkthrough.**
1. Claude interviews you for the story — the project and interest (as much as you want public), what your friends said, the /plan moment and what it surfaced — and folds your answers into the draft material. Your choice, made at processing: interview at drafting rather than telling it now.
2. Claude verifies the science claims by web search, files the findings under `resources/research/` (index line in the same move), and lists which claims survived and which are cut. You see the list before drafting starts.
3. Claude drafts the article for flintcraft.tech, first-person throughout, with the photos/trauma element trimmed or kept per your call on reading the draft.
4. You read it and say what to change; repeat until you're satisfied.
5. You decide delivery to the site project: an INBOX message (you see the exact text first) or you carry the file across yourself.
6. You publish — Claude has no route to the site.
7. You confirm it's live; the send is recorded in `INBOX/sent.md`, follow-on captures for the YouTube and LinkedIn versions are filed, and this line closes.

**Held 2026-08-24 with the comparison article, same reason recorded there:** articles wait until the announcement-driven FAQ has material for Claude to draw on. Re-offered when the date passes; the lift judgment is whether the material is there.
Not before: 2026-09-21

**Files:** none in this project except the research file step 2 creates under `resources/research/`. The artifact is an article for flintcraft.tech. Relates to [competition-comparison-article] — a separate piece, no dependency either way.

#### [user] Discord post: how much stronger a session is from its start once /plan opens by reading recent LOG index lines [discord-post-session-start-strength]
Captured by you 2026-08-11. Your point, rendered in Claude's words rather than quoted: before, it felt shaky for the first few items; starting with log-awareness plus some maybe-relevant context massively boosts the start of sessions. The angle is yours; the correction below is Claude's.
**It cannot be written yet, which is why this is a queue item rather than a draft.** You asked believing the feature was live. It wasn't: `plan.md`'s Step 1 reads QUEUE.md and SPEC.md only, and its three `LOG/index.md` mentions are targeted lookups — has this been decided — not an orientation read. The feature is [plan-reads-recent-log-index], held below the line behind [index-line-length-proportional-cap].
**Your experience was real; the mechanism you credited was wrong.** What steadied that session was the below-line revisit reading LOG to check two blockers, plus the previous session's forward advisory naming where to start. Both live; neither is the five-recent-lines read. Worth carrying into the post — "the thing that helped wasn't the thing I thought" is the better story.
**The post's content, to draft when it ships.** The shaky-first-items problem and its cause; what the orientation read changes; and the honest scope — it doesn't carry all necessary context, it sets upcoming work against past work. Include the cost bound, since it's why the feature waited: five index lines is an unbounded read until index lines are capped, which [index-line-length-proportional-cap] fixes.
**Constraints:** 2000 characters, the Discord limit. Not posted until *everything* the post describes has shipped — standing rule in `CLAUDE.md`, adopted 2026-08-11.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside the limit. 3. You say what to change. 4. You post — Claude has no route to Discord. 5. You confirm, and the line closes.
**Unblocked 2026-08-13.** [plan-reads-recent-log-index] shipped — `LOG/2026-08-12-plan-reads-recent-log-index.md`; /plan's read-state step now opens with the five newest index lines. Ordinary ready work. Fourth item found sitting behind a shipped blocker; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: third in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone holds it.
**Blocker repointed 2026-08-21.** [discord-post-cycle-awareness] was posted and closed on 2026-08-21 (`INBOX/sent.md`), so the old blocker had resolved and this item read as liftable while the pacing chain still held it. Repointed at [discord-post-context-adjacency], the post now ahead of it in the chain — it lifts by itself when that one goes out and closes. Same repair, same reasoning, as the repointing recorded on that item.
**Lifted 2026-08-24.** [discord-post-context-adjacency] was posted and confirmed on 2026-08-23 (`LOG/2026-08-23-discord-post-context-adjacency.md`), so the chain ahead of this post is clear. The one-a-day pacing still applies at posting time: it goes out on a day no other Throughliner post does.
**Held again 2026-08-26.** The feature the post announces was found underdesigned ([plan-log-index-read-underdesigned], now cleared as its redesign: a derived window, a checkable relevance test, a required report line) — announcing the current version would describe behaviour about to change. Lifts by itself when the redesign ships.
Blocked by: [plan-log-index-read-underdesigned]

#### [user] Correct and post the announcement about rationale moving out of operative rules — the draft tells readers the why lives in session logs they can't reach [announcement-rationale-split-correction]
Captured by you 2026-08-09 — split out of [rationale-relocation-invisible-to-consumers] when that capture was deleted as otherwise satisfied. The 2026-08-09 Discord draft says the reasoning "lives in the session logs where you can go and read it." False for every reader not developing the method: the plugin package ships neither `LOG/` nor `resources/`. Posting it as written points users at something they cannot access.
**Why this is the user's line:** Claude can draft the correction; only the user can post. Under the capability test, drafting is Claude-work and posting is not.
**Walkthrough:**
1. Claude drafts the corrected announcement, replacing the session-logs claim with the actual split: why the method behaves a certain way is in the shipped FAQ; why a rule is worded as it is stays in the development log.
2. The user says what to change.
3. The user posts it.
4. The user confirms; it's recorded and the line removed.
Rough draft, to sharpen at step 1 — the announcement's other content wasn't reviewed, so check the whole thing, not only the false sentence. Also decide at step 1 whether it's still worth announcing, given the week that has passed.
**Paced 2026-08-14 on the user's decision: last in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Last because it corrects an already-posted announcement rather than being news, so it yields to the three new posts. It lifts when [discord-post-session-start-strength] is posted and closed.
Blocked by: [discord-post-session-start-strength]

**Files:** none — the artifact is a Discord post. Relates to [self-authoring-rules].

#### Define this project's weekly release cycle, and amend the release model to run on it [weekly-release-cycle]
**Your decision, 2026-08-22: releases move from purely on-request to a weekly Wednesday cycle.** The pick costs no judgment — release the newest rezip at least a week old, so every change in it has had seven days of continuous dogfooding inside its successors; your correction that no single rezip runs a week is what led there. Due when the latest GitHub release is over seven days old and a week-old rezip exists — both observables. **Extended the same session by the three-channel model on [beta-tester-pathway]:** a Wednesday turn produces two events — this week's pick becomes the new beta, and last week's beta promotes to the stable release — so the cycle definition's steps carry both once those items are kept; the definition here stays buildable on the release half alone.

**The rule change this carries, gate-run at the build from this disposition.** CLAUDE.md's release section currently says a release runs when Alex asks and at no other time (your decision of 2026-08-09, made after stopping an automatic release twice). This narrows it: on request, or when the weekly release cycle falls due — and the reason the old failure does not recur is that the cycle asks no readiness question: the calendar and the git log settle which rezip goes, retrospectively, where the rejected middle option asked "is this good enough?" prospectively. On-request stays; the pre-rejected pause-before-publishing middle option stays rejected.

Rule gate: run — amendment to the Release section of CLAUDE.md, naming and superseding its at-no-other-time clause; the 2026-08-09 reasoning is outweighed on the stated ground rather than called wrong.

--- Build block ---
Changes: create this project's cycles doc with the release-cycle definition (artifact: the GitHub release; steps: pick newest week-old rezip, run the release ritual; cadence: weekly, Wednesday, declared; observable: the latest GitHub release's published date, plus the rezip log for a week-old candidate). `CLAUDE.md` — amend the Release section: a release runs when Alex asks, or when the weekly release cycle falls due; the at-no-other-time sentence is reworded to carry the cycle.
Acceptance: the cycles doc parses under the shipped check; CLAUDE.md's release section names both routes and still bars the pause-before-publishing middle option; release-ritual.md needs no change (the ritual itself is untouched).
Refused: choosing among candidate rezips each Wednesday — newest week-old wins, no judgment.
--- End build block ---
**Blocker repointed 2026-08-22:** the cycles machinery is built (`2026-08-22-cycles-definitions-and-due-checks-build.md`) with one behaviour unconfirmed, so the fact holding this item is the verification, not the build — the field now names the `[user]` verification line, and this lifts by itself when that closes.
**Read [expedite-first-beta-release] before building this, 2026-08-26.** Alex proposed a published list of labelled test rezips and then that each Wednesday's pick be the most recent one labelled stable. That is a different selector from this item's newest-rezip-at-least-a-week-old, and it meets this item's recorded refusal of choosing among candidates — the argument for and against is written out there. It may also bear on this item's blocker, since a hand-driven Wednesday turn would not depend on the cycles due-ness check that [cycles-check-fires-nowhere] has stalled.
**Selector settled 2026-08-26, your decision at the next planning opening — a supersession of this item's pick rule.** The Wednesday **beta** pick is the most recent rezip labelled stable on the nerds list; the **stable release** is last week's beta promoted after its seven-day soak. The newest-rezip-at-least-a-week-old selector is superseded: its week-old property now lives in the promotion step, not the pick. Why the old reasoning loses without reopening the readiness question: the label is applied when the rezip is posted, describing a build that already exists, so the Wednesday turn still reads a recorded state rather than asking "is this good enough?" — the prospective readiness question stays banned. The refusal of choosing among candidates stands: the selector is still mechanical (most recent stable label wins, no judgment on the day). The build block's pick wording is updated to match at build time.
Blocked by: [cycles-due-check-verification]
**Files:** `CLAUDE.md`, the new cycles doc. The dependency is host-side: the checks that read the definition must ship first.

#### The beta channel: each Wednesday's pick offered via Discord and a GitHub pre-release [beta-tester-pathway]
**Your idea, 2026-08-22, designed in the same session into a three-channel model — the standard release-channel shape (Chrome/Firefox), adopted on your terminology question.** Your day-to-day rezips are dev builds, yours alone and unchanged by this. Each Wednesday's pick becomes the **beta**: announced on the Throughliner Discord, hosted as a GitHub pre-release (Discord cannot host an install; the release ritual already builds and attaches zips), and offered to willing testers while it soaks for a week — you as the only tester at first, which is better than nothing and still a beta channel. After its week it promotes to **stable** and goes to the community listing ([marketplace-submission]). This superseded the earlier two-route question (repo-at-HEAD versus per-rezip artifacts): the weekly-pick artifact route won because it gives testers your chosen moments rather than every commit, and it reuses release machinery rather than adding a publish step to every rezip.
**Your sequencing, 2026-08-22, revised the same day: the channels launch together rather than beta-then-listing** — the community listing is itself part of how testers arrive, so the chain is beta channel + community listing (honestly framed as early), then YouTube videos pointing at them. Written on both items per the known-ordering rule.

**Kept 2026-08-22, held behind [weekly-release-cycle].** The three things the capture left open are settled. **Install route: a ref-pinned marketplace add** — research done at processing (`resources/research/claude-marketplace-listing-paths.md`, beta-channel section): a marketplace-add pins to a branch via `#ref`, so a `beta` branch fast-forwarded to each Wednesday's pick serves testers through the README's existing ask-Claude install shape, and no tester touches a zip; the pre-release zip stays as the release artifact. The research caveat travels: some ref-handling behaviour is covered by open feature requests, so the walkthrough is smoke-tested on a real second machine before any tester gets it. **Naming, your decision at processing: one cycle, called the release cycle** — beta is a step inside the Wednesday turn, not a sibling cycle; this build amends the one definition rather than adding another. **Offer wording:** drafted in the build, honestly-early testing framing; the launch announcement is the `[user]` line [beta-launch-announcement], filed with this keep.

--- Build block ---
Changes: amend the release-cycle definition in the cycles doc so one Wednesday turn carries both events — fast-forward the `beta` branch to the newest week-old rezip's commit, and promote last week's beta to the stable release; create the `beta` branch. `README.md` — add a beta-channel section: what beta means (honestly early), the tester install walkthrough (ask Claude to add the marketplace `FlintcraftTech/throughliner#beta` and install), and how updates arrive. Draft the Discord beta-offer announcement text into [beta-launch-announcement]'s walkthrough.
Acceptance: the cycles doc still parses under the shipped check with the two-event turn; the `beta` branch exists; README's beta section reads for a non-coder and matches the walkthrough smoke-test caveat (not offered to testers until smoke-tested); the announcement draft is under 2,000 characters.
Refused: a separate beta cycle with its own cadence — one cycle, beta as a step (the user's call); zip-download installs for testers — the ref-pinned marketplace add replaces it; a separate beta repo — a branch suffices.
--- End build block ---
**Understudy ordering, your decision 2026-08-22: the beta launch does not wait for it** — Understudy debuts as the standard companion app with the YouTube videos, after this channel and the listing; until then the beta materials carry the one-line caution against editing project docs while a run writes. Written on both this item and the marketplace item per the known-ordering rule.
**Read [expedite-first-beta-release] before building this, 2026-08-26.** Alex's labelled test-rezip list would give the Wednesday pick a defined candidate set, which this item never had. It does not collide with the ref-pinned install decided here — the list is zips for people who want raw dev builds, testers still install from the `beta` branch — but it changes what the pick selects from, so the two are designed together or not at all.
**Selector settled 2026-08-26, your decision, recorded in full on [weekly-release-cycle]:** the Wednesday beta pick is the most recent stable-labelled rezip from the nerds list; the stable release is last week's beta promoted after its soak. This item's two-event turn is unchanged in shape — only what the pick selects from changed.
**Install half advanced 2026-08-26:** [beta-branch-install-pin] creates the `beta` branch at today's expedited release and points README/INSTALL at `#beta`, with the second-machine smoke test as [beta-install-smoke-and-post-edit]. What remains here is the cycle wiring — the two-event Wednesday turn — and the announcement draft; this item's build reconciles its block against what those two already shipped.
Blocked by: [weekly-release-cycle]
**Files:** the cycles doc, `README.md`, QUEUE.md (the announcement item's walkthrough). The dependency is real, not just conceptual: the definition this amends is created by [weekly-release-cycle]'s build.

#### [user] Post the beta-channel launch announcement on the Throughliner Discord [beta-launch-announcement]
Filed 2026-08-22 with the keep of [beta-tester-pathway], which drafts the announcement text into this walkthrough as part of its build. The offer is framed honestly early — a testing invitation, not a product launch — and yields to the one-a-day posting chain like every other post. Launches alongside the community listing per your sequencing recorded on [beta-tester-pathway] and [marketplace-submission].
**Walkthrough.**
1. The draft is in this item once [beta-tester-pathway] builds; Claude walks you through any final edits.
2. Before posting, the tester install walkthrough must have been smoke-tested on a second machine — confirm that happened; do not post an install route nobody has run.
3. You post it on Discord, on a day no other Throughliner post goes out — Claude has no route to Discord.
4. You confirm; the send is recorded in `INBOX/sent.md` with what it claimed, and this line closes.
Blocked by: [beta-tester-pathway]
**Files:** none — the artifact is a Discord post.

#### [user] Approved Discord post about the comparison article now describes a superseded draft [comparison-article-post-needs-rewrite]
Found by Claude 2026-08-23 while walking the comparison-article item. A Discord post was drafted and approved on 2026-08-22 and has not gone out — it is recorded on `INBOX/sent.md` as approved and not yet posted, with its text verbatim in `LOG/2026-08-22-competition-comparison-article.md`. Its second paragraph announces the article and describes it as closing "on the coherence-over-scale trade", which was true of the 2026-08-22 draft.

That draft is superseded. The 2026-08-23 rewrite names a specific project rather than a category, adds a section on Papi as the nearest comparable tool, and ends on a shipped mechanism instead of a general trade-off — roughly 1,400 words against 900. A hold-note has already gone to the site project asking that the old one not be published.

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, is unaffected and still true. Only the second needs rewriting, and it needs rewriting after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. You post it, with the live article URL pasted in — Claude has no route to Discord. 5. You confirm, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Kept 2026-08-24, held below the line on Claude's recommendation and your agreement.** As a capture this carried its ordering in prose because captures have no `Blocked by:`; as a held work item it carries the field, so it lifts by itself when the article item closes instead of being re-offered every session while the external review is out. The same ordering sentence is written on the article item per the known-ordering rule.
Blocked by: [competition-comparison-article]

## Unprocessed

#### Show-first approval moments produce their text twice [approval-flow-token-doubling-simplification]
Captured by you (2026-08-01) while reviewing your Claude Code feature request anthropics/claude-code#77134. Rescoped at your direction 2026-08-13 from a larger item about approval-time doubling generally.
**The cost, narrowed to where it still exists.** Showing text in chat and writing it to a file are both the model producing those tokens, so text doing both is produced twice. That used to hit every approval moment; it no longer does — write-first shipped, and the post-write report is one line naming what landed, never a re-paste.
**What remains is the show-first set only** — the moments write-first deliberately keeps showing first, because the previous version isn't recoverable without the user: a commit message, anything leaving the machine, a wholesale conversion of a document the user already owns. There the text is composed in chat, approved, then produced again to be used.
**Why it is not buildable yet.** The saving needs the harness to surface an already-produced Write's content verbatim with no second model pass — issue #77134, which hasn't landed. Until it does there's no build to describe. Re-examine when the issue ships.
**Two things settled, not to be re-opened here.** The write-first ordering flip is decided and shipped. The convergence note about view-in-doc machinery is spent — working-mode field, Editor field and line-anchored-link promise all retired 2026-08-09.
External dependency: anthropics/claude-code#77134.

**Checked 2026-08-19 and still open** — filed 2026-07-13, labelled `enhancement`, `area:cost`, `area:tools`, `area:core`, no maintainer response and no close date. The disposition is unchanged: nothing to build, re-examine when it ships. **What the check buys is that the next session reads a date rather than re-running the lookup**, which is the whole reason it is written here.

**Two things in the discussion are worth having when this does become buildable.** A comment dated 2026-08-01 sets out the mirror direction — author-in-chat, approve, then write — and argues it needs no second primitive, because a workflow that can show a Write's content verbatim can adopt write-first ordering and get the same saving so long as rejection reverts. That is this project's shipped model described from the outside. **It looks like yours, on the date and the reasoning, but nothing in the record here says so — worth confirming rather than assuming.** A later comment proposes generalising the primitive to `show_file(path, range?)`, which would also let Claude surface parts of *existing* files without re-emitting them — that reaches the view-in-doc pointer and the inline-text offer, not just the three show-first cases, so it would widen this item rather than merely unblocking it.

**Surfaced 2026-08-19 by the decay rung, on its first firing since the interleave was adopted.** It had been the oldest entry in the queue at 17 days and nothing in the ladder had ever reached it.

**Dated 2026-08-21 with your approval — the field's first use, as this item predicted.** It waits on `anthropics/claude-code#77134`, which nothing in this queue can resolve; five weeks open with no maintainer movement, so a month out is when there is plausibly news. Not offered again before then.
Not before: 2026-09-21

**Skipped again 2026-08-19, and it is the item that produced the fix for its own condition.** Presented, found unchanged, and in being presented it made the pattern visible: three entries in one session waiting on something outside this project, none able to name a blocker, all re-offered every session. That is [not-before-reaches-unprocessed], kept and cleared in the same session. **This is its first candidate** — once `anthropics/claude-code#77134` ships, or a date is worth guessing at, the field goes here and the re-offering stops. Until the field is built there is nothing to write, so the skip stands.

#### A personal bridge pushing `[user]` items into Taskflow as tasks, and reading completions back [taskflow-personal-bridge]
**Raised by you 2026-08-19**, from executing in another of your projects where the work is mostly `[user]` items. Your framing: Throughliner becomes an executive layer over projects Claude only half-implements, and sometimes you do not want to complete things in conversation — you want the to-do list. **The mapping is yours: a `[user]` item is a task, and its steps are subtasks.** The assessment below and the decomposition are Claude's.

**Your mapping is Taskflow's own model rather than an approximation, which is what makes the completion half work.** Taskflow's subtasks inherit their parent's Project, date and placement, and a parent has no checkmark of its own — it is complete only when every subtask is, and un-checking any child pulls the parent back out of the completed tray. So completion arrives as one derived signal per item, and a half-done item cannot read as done.

**Two decisions of yours, in your own words.** Route: *"design this against the file-based route now, with MCP as the later transport."* Scope: *"agreed, personal bridge to start."* So this is host-only tooling in this project, assuming your own Drive setup, and it ships nothing to consumers; promoting it to a shipped feature is a later decision this does not pre-empt.

**Why file-first rather than MCP.** Taskflow's paid tier already designs the channel — Claude reaching Taskflow through a remote MCP server — so Throughliner would be a client of a route Taskflow intends rather than an integration Taskflow's local-first principle forbids. But `[0020-remote-mcp-server]` and `[0019-ai-choice-flow-and-mcp-setup]` are unbuilt over there and cloud sync is their precondition. The same reasoning is already on their queue in `[strategy-doc-preview]`, in your words there: *"We're just here, so we don't need the MCP."*

**Two hazards found by reading their SPEC rather than assumed.** Taskflow runs on the phone against a local Room database, so a file route means producing a file that is carried onto the device, not writing where Taskflow reads. And their existing `[0014-json-export-and-import]` is a whole-database export and restore — pushing tasks through it would replace every other task in the app. What this needs is an **additive** import, which Taskflow has neither built nor designed.

**Taskflow's answers arrived 2026-08-26** (their mail read and archived here; the standalone capture [taskflow-bridge-asks-answered] was merged into this item and deleted). All three asks are settled on their side. The bridge is not a breach of their no-external-task-app rule — that rule is about data living in two places with neither being the truth, not about who may put work in, and they have added a SPEC sentence drawing the line. They have designed a separately named **additive** import that inserts rather than restores, creating a named Project where one is missing and leaving everything present untouched — deliberately a separate action rather than a mode on the replacing import, because one destroys data and the other does not. And every exported task will carry its completion state and date, with a parent's state as the derived roll-up — the two-way half. Two of their choices travel into our design rather than being rediscovered: additive stays separately named, and incoming tasks are deliberately not de-duplicated, on their view that a visible duplicate is a smaller harm than a task that silently never arrives.

**The status qualifier is load-bearing: all of this is settled and unbuilt on their side** — product decisions, not shipped capabilities. So the design here can now be written at the keep-step, but anything depending on the file format depends on a design rather than a thing that exists, and the item stays unbuildable until their export and additive import ship.

**A second question rides this item's keep, merged 2026-08-26 from the deleted capture [multipart-user-handoff-queue-side]: the queue-side bookkeeping Taskflow declined to design.** What this queue does with a `[user]` item whose parts have moved onto a to-do list. Their side is settled and small — an arriving task is an ordinary task with no origin marker (their trust-at-a-glance reasoning, now in their SPEC), so a handoff sends only a title, an optional Project and an optional date. The candidate design here is existing machinery rather than new state: a handoff is an outbound send, so the sent register's intent field carries the bookkeeping — *for completion* can clear the item, with completion read back through the bridge's export or your mention; *for continuation* leaves the line in place carrying a note of what moved. Their one flag is the constraint the design must survive: the handoff most likely fires **mid-walkthrough**, when the item's true size becomes visible and the user is least able to reorganise — so the run records which steps moved and stops walking them.

**Dated 2026-08-21 with your approval; the date stands.** The reply it waited on has arrived, so when the date passes this is taken up on its merits rather than re-dated.
Not before: 2026-08-28

**One thing to settle at processing regardless of their answer:** a `[user]` item's text can name real people or client details, so what crosses the boundary needs the scrub the queue already gets, and a pushed task is leaving this project's records.

#### Submit Throughliner to Anthropic's community marketplace, as step one toward in-app browsability [marketplace-submission]
**Your goal, 2026-08-22: actual release to the Claude marketplace so people can browse for it inside the desktop app.** The research (`resources/research/claude-marketplace-listing-paths.md`) found two routes: the official marketplace is the only one browsable in-app by default, is curated at Anthropic's discretion, and has no self-serve path — the submission form feeds the community marketplace instead. So the realistic sequence is community first: submission via the clau.de/plugin-directory-submission form, automated security scanning plus human review, a public listing at claude.com/plugins pinned to a commit SHA; then official at Anthropic's discretion.
What a keep must settle: ending the pre-release posture CLAUDE.md declares ("in active testing, not ready for the Claude marketplace") — the user's decision; version-consistency discipline (plugin.json, changelog, git tags — the commonest reported rejection cause; the weekly release cycle [weekly-release-cycle] supplies the cadence for it, and a changelog does not yet exist); and confirming the name is final, since a marketplace slug is immutable once published and a rename breaks every install. The submission itself is a `[user]` step — a web form Claude cannot submit.
Runs behind [weekly-release-cycle] in spirit — a regular release rhythm is what makes the version discipline real — carried as this sentence rather than a blocker, since the submission decision is independently the user's.
**Reframed 2026-08-22, same session: the listing is the stable channel of the three-channel model settled on [beta-tester-pathway].** The research question this paragraph used to flag is answered — see below.
**Your sequencing, 2026-08-22, revised the same day: the listing launches alongside the beta channel rather than after it** — your first thought was beta testers before any listing, revised when it emerged the listing may be the only realistic way testers arrive; the listing is framed honestly as early instead. YouTube videos come after both, on your reasoning that videos without a listing would look bad to viewers while YouTube may bring the very first users. Written on both items per the known-ordering rule.
**Update-cadence research answered, 2026-08-22** (`resources/research/claude-marketplace-listing-paths.md`, listing-updates section): the listing's commit pin updates **only after re-review**, and no turnaround is documented anywhere — so the Wednesday stable promotion cannot push to the listing. The realistic shape: the weekly stable channel lives on this repo, and the listing is updated on a slower submit-and-wait rhythm — monthly, or when something worth announcing lands — worded as "submit the update".
**Your decision, 2026-08-22: the not-ready-for-the-marketplace posture ends.** You are ready to remove it; the one thing genuinely holding the submission is company registration, which is [abr-identity-and-address] on the flintcraft.tech project's queue — designed there with its research done. A dependency note was sent to that project's INBOX the same day (recorded in `INBOX/sent.md`); it asks no new work, only flags that a second project now waits. Whether the submission form itself actually requires registered-business details is unverified — check at keeping.
**Dated 2026-08-22 with your approval.** It waits on the ABR work in another project, which nothing in this queue can build; a month out is when there is plausibly news. Not offered again before then. Still to settle at the eventual keep: the changelog, and confirming the Throughliner name is final (the slug is immutable).
**Understudy ordering, your decision 2026-08-22: the launch does not wait for it.** Understudy debuts as the standard companion app with the YouTube videos (already last in the chain); the listing stays silent on it until it is real. Until a companion app honouring the editing-state contract is out, launch materials carry one honest line: don't edit the project docs while a run is writing them. A dependency note went to Understudy's own project INBOX the same day (recorded in `INBOX/sent.md`). Written on both this item and the beta-channel item per the known-ordering rule.
Not before: 2026-09-22

#### [user] Discord post draft: plain-English consent [discord-post-plain-english-consent]
Drafted 2026-08-25 at the planning close under the close-sweep design ([plan-close-post-drafting]); approved as a candidate by you, with your addition of the terse-docs mention. Waits on [keep-approval-reading-burden] shipping; verify against the shipped build before posting, and post on a day no other Throughliner post goes out.
Not before: 2026-08-27
**Draft (under 2,000 characters):**
> **Plain-English approvals.** When you and Claude go through your captured ideas in a planning session, each one now opens with a plain-English summary of what the idea says — right there in the chat, before any analysis. And when Claude recommends what to do with it, it says in plain words what would actually change ("this would go on the ready list — the queue's cleared-to-build region") and asks whether you agree, in those words. No procedure jargon, no needing to open the queue file to know what you're saying yes to: you approve what's in front of you.
>
> The files themselves stay tidy through a companion rule: everything written into your project's documents is bounded by the project's own measured norms, so records stay terse enough to actually read when you do open them. The summary serves the moment; the documents serve the return visit.

#### [user] Discord post draft: issue-first problem reporting [discord-post-issue-first-reporting]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the GitHub-CLI-recommended mention. Waits on [method-feedback-issue-first] and [plan-open-github-issue-check] shipping; verify against the shipped builds before posting; one-a-day chain applies.
Not before: 2026-08-28
**Draft (under 2,000 characters):**
> **Report a problem, get the answer back automatically.** When something in Throughliner misbehaves, Claude now offers to file it as a GitHub issue on the Throughliner repository for you — drafted, shown to you word for word, and posted only on your yes. (An issue is public under your GitHub account; if you'd rather stay private, the report form is still there.)
>
> The reason issues are worth it: they're two-way. Your planning sessions now scan your correspondence at their opening — waiting mail, answers on issues your project filed, and new issues arriving on your own repository — so a reply reaches you without you checking anywhere or remembering to. And if you want a follow-up on a report, say so when it's sent: a dated reminder lands in your queue and surfaces on its day, with the checking method already agreed.
>
> For all of this, the GitHub command line tool (`gh`) is a highly recommended companion to Throughliner — everything degrades gracefully without it, but the two-way channel is what you'd be missing.

#### [user] Discord post draft: subprojects [discord-post-subprojects]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the start-big benefit. Waits on [subprojects-pop-out] shipping; verify against the shipped build before posting; one-a-day chain applies. FAQ potential noted for posting time, per the announcement-time FAQ rule.
Not before: 2026-08-29
**Draft (under 2,000 characters):**
> **Subprojects: start big, split later.** When one part of your project outgrows the rest — the software inside a business plan, the contracts inside a venture — you can now pop that subfolder out into its own full Throughliner project. Run setup inside the subfolder: it reads the parent project's spec, works out which part this is, checks with you, and tells the parent it's moved out. From then on it's an ordinary project with its own clear queue.
>
> The quiet benefit: you don't have to understand your project's final shape at the start. If the idea is nebulous and multi-parted, start it as one big project, rest assured that any part which grows a life of its own can be popped out later.
>
> The link back is deliberately simple: work in a subproject can hold up work in the parent — never the other way round — so the popped-out piece marches forward on its own terms, and anything crossing between them travels as mail you approve, never as one project silently editing another. One thing to know going in: there's no scripted way to pop a subproject back in, so it's for parts that have genuinely outgrown the nest.

#### [user] Discord post draft: multi-person sessions [discord-post-multi-person]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your additions: name Chagora — your new app by its-coughfee, designed to work with Throughliner but not dependent on it — and credit zebbern. Both names are published GitHub identities, which is what the scrub rule permits. Explanatory register. Waits on [multi-user-identity-layer] shipping; verify against the shipped build before posting; one-a-day chain applies.
Not before: 2026-08-30
**Draft (under 2,000 characters):**
> **Several people, one session — and everyone's ideas stay theirs.** Throughliner now understands a session with more than one person in it. Anyone present can drop ideas into the queue; the decisions — what gets kept, built, or published — stay with the one person holding the reins. Credit follows whoever's message raised an idea, under the same fairness rules as ever: agreeing to a suggestion doesn't make it yours, and Claude's own proposals stay Claude's.
>
> Identity can be as solid as you want it. Where people join through a Discord server, Discord's own account-linking can stamp members with a verified GitHub login — no custom bot — so contributions arrive under an identity someone actually proved. And contributors get real credit where it counts: commits carry co-author lines, so their work shows on GitHub itself, using only details they've chosen to share.
>
> This grew out of real use: **Chagora**, a new app by its-coughfee, is built to work with Throughliner (though it doesn't depend on it) and runs exactly this shape — a team prompting one session from a shared channel. Credit also to zebbern for the upstream groundwork.

#### [user] Discord post draft: session-flow smoothings [discord-post-session-smoothings]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved by you as an announcement for now, with the note that it carries the makings of several FAQ entries — authored at posting time per the announcement-time FAQ rule, as may the other four drafts each in their own right. Waits on [build-refuses-user-queue-move], [end-of-queue-gate-refill-and-standing-intent] and [build-view-delete-ask-at-close] shipping; verify against the shipped builds before posting; one-a-day chain applies.
Not before: 2026-08-31
**Draft (under 2,000 characters):**
> **A round of session-flow smoothings.** Small changes, each removing a moment of friction:
>
> **Your word carries mid-build.** Tell a build run to move a queue item — skip this, shelve that — and it does it, says so in one line, and carries on. The run still never rearranges your queue on its own initiative; what changed is that your explicit instruction goes through instead of being deferred to a later session.
>
> **The wrap-up question behaves.** The end-of-session ask returns when new ideas refill the queue and it empties again — and if you tell a session you're keeping it open as a drop-box for ideas while you work elsewhere, it stops offering to wrap up for the rest of that chat.
>
> **Housekeeping goes quiet.** The temporary file a build run reads from is cleaned up silently at the close and kept out of your repository — no more being asked about a file you never created.

#### Process-now "yes" was spent as disposition approval: two items written and cleared with no recommend-and-wait turn [process-now-yes-spent-as-disposition]
Raised by you 2026-08-26, in a live /plan on this project: after the process-now offer for the beta install pin, your "yes, process it now" — an answer to *when* — was treated as approval of a design first shown in the offer message, and two items were written and cleared with no recommendation turn. Your words: "you skipped processing and landed stuff straight to queue like was always happening with 'keep' in the last version." Repaired in-session: you reviewed and kept both items as written.

The rule already forbids this — plan.md's fold conditions say a design first shown in the offer message cannot fold, and the process-now section says either branch is subject to them — so this is an instance of a shipped rule not being followed, not a missing rule. Evidence for the keep-step: the one site where bundling was actually fixed was the checkpoint, fixed by a specimen message rather than a rule statement ([style-negatives-to-rewrite-positive] carries the citation) — so the candidate fix is a specimen at the process-now section showing the offer turn and the separate recommend turn, weighed against accepting it as a slip. Runs on the version installed today, so check the current text before scoping.

#### Should cycles get mermaid diagrams? [cycles-mermaid-diagrams]
Captured by you, 2026-08-24, mid-planning — your framing: seems reasonable. Filed at your direction without discussion, so the idea is unshaped: what a diagram would show (a cycle's steps? the turn's two events? due-ness over time?), where it would live (in CYCLES.md beside the definition, or generated), and who reads it are all open for the keep-step. Context worth having there: the desktop app renders mermaid in its markdown viewer, and the cycles doc is user-facing by design.
Skipped 2026-08-26 on Claude's recommendation and your agreement: what settles it is a build that must ship first — [weekly-release-cycle] creating this project's first real cycles doc, with the due-ness check working ([cycles-check-fires-nowhere]'s fix). A diagram designed before any real cycles doc exists would be guessing at a document nobody has seen; take it up once there is one to draw.

#### Session openings could report how long the installed build has been running [session-start-reports-install-age]
Raised by you 2026-08-26, in the post-close tail, from a live instance: an announcement draft claimed you had been "running this build all week" when you had been running it since late the night before — Claude has no way to know how long an installed build has been tested, and this misjudgment recurs. The opening already reports the installed version and content stamp; the candidate is reporting the installed snapshot's age alongside them (the plugin cache directory's install time is a readable fact), so a session weighing "how tested is this build" reads a date instead of guessing. A derived fact in the session_start payload, same register as the stamp. For the keep-step: whether the age alone is enough, or whether what is really wanted is time-under-use rather than time-since-install.

#### Discord posting bot: an all-rounder so posts and rezip-list updates can be made straight from a session [discord-posting-bot]
Raised by you 2026-08-26, in the post-close tail, as a side-thought filed for a later /plan. The want: the test-rezips channel's posts and their updates — adding notes to previous entries when issues are reported, changing an entry's stable status — done by a bot rather than by hand, and more generally an all-rounder bot this project can post through directly during /plan or a build. That would be the first route Claude has to Discord, so the never-send-unseen guarantee has to be designed in from the start: nothing posts without you seeing the exact text and saying yes, and an automated update is still a send. Bears on the nerds-list mechanics left open on [expedite-first-beta-release] and on the eventual [weekly-release-cycle] turn; unshaped beyond that — platform, hosting, and what "all-rounder" covers are all for the keep-step.

#### "Ready list" naming rule is defined in plan.md but binds every skill's asks [ready-list-name-defined-where-only-plan-reads-it]
From the compliance audit of the rule changes since 3ed3db1, lens 1 (distribution).

`plan.md` around line 796 declares "the ready list" the standing plain-English name for the cleared region, and says it is "used identically in every session's asks". It fires wherever a session names that region to the user: at /plan's recommend step, at /next's off-ramp where the run is presented, and at /done where the close reports what is ready. Only the first of those reads `plan.md` — the other two load their own docs and the always-loaded rules, neither of which carries the name. A grep of the shipped docs finds "ready list" in `plan.md` alone.

So the rule as written cannot do what it claims: two of its three sites can never read it. The fix is distribution — the name belongs in `skill-nonspecific-rules.md`, where every skill and every no-skill conversation reads it, with `plan.md` keeping only the recommend-step wording that uses it.

#### Issue-channel check stays silent unless it files, while its sibling cycles check no longer may [issue-check-silent-while-cycles-check-speaks]
From the compliance audit of the rule changes since 3ed3db1, lens 1 (consistency).

Both checks sit in `plan.md`'s opening and fire at the same moment — the read-state step, before the queue is ranked. The issue-channel check (around line 349) is tagged `[SILENT]` when nothing is found or the tools are absent, `[BRIEF]` only when a capture is filed. The cycles check (around line 490) was rewritten this session to speak whenever the project has a cycles doc, on the stated ground that a check which speaks only when it files cannot be told from a check that never ran — which is what the cycles check turned out to be for its whole life.

The reasoning that moved one applies unchanged to the other: an issue scan that ran and found nothing produces the same silence as an issue scan that never ran, and nobody would know to ask. Either the issue check gains a one-line either-way report, or the cycles change needs an argument for why the two differ. Worth settling as one decision rather than drifting further apart.

#### Case D pop-out section carries no response-shape tags, and two of its steps wait on the user [setup-case-d-untagged]
From the compliance audit of the rule changes since 3ed3db1, lens 2 (tag placement).

`setup.md`'s Case D section (around lines 107 to 140) was added since the last audit and carries no tag on any step. Two of them stop for the user: reading the parent's SPEC and putting the inferred subpart to them in clarifier form, which fires at the very start of adopting a subfolder and cannot proceed without their answer; and drafting the pop-out message to the parent's INBOX, which fires at the close and is shown in full before an explicit yes. Both are `[PROMPT]` moments by the definition in the always-loaded rules.

Case B's peek — the sibling this section says it copies — is tagged. Untagged, the output behaviour of a step that must wait is left to chance, which is the missing-tag failure the lens names.

#### Write-first rule gained a rationale clause that fails the delete-and-read test [write-first-rule-carries-its-why-inline]
From the compliance audit of the rule changes since 3ed3db1, lens 4.

`skill-nonspecific-rules.md` around line 150 now reads: "Write first, then report — decided by one test: is the previous version recoverable without the user's help? Consent happens in conversation, in plain words, before the write — the file is the record of what was agreed, not where agreement happens — and showing recoverable text before writing it costs a wait that buys nothing."

Delete the second sentence and what remains is a complete instruction with its test intact, so by the lens's own detector the deleted sentence is rationale rather than operative text. It fires in every skill and in plain conversation, since this is the always-loaded file, so the weight is paid at every session start.

Where it should go: the LOG entry that decided the write-first inversion, which is where an authoring decision belongs. Worth checking first whether any part of it is doing work the bare rule cannot — the "consent happens in conversation" half may be operative for a session that would otherwise read write-first as consent-free.

#### Log-index read carries two rationale sentences inside its operative text [plan-log-index-read-carries-rationale]
From the compliance audit of the rule changes since 3ed3db1, lens 4. Both sentences were written by the build run that filed this finding, so it is flagged against this session's own work.

`plan.md`'s orientation read, around line 238, carries "That window is the work done since the last time anyone stood where you are standing now" and "A read that speaks only when it finds something is indistinguishable from a read that never ran." Delete either and the surrounding instruction — read the window, fold in a line when it names a slug or file the queue also names, carry one line either way — is complete.

The step fires once, at every /plan opening, so this is weight paid by every planning session. Its home is the LOG entry for [plan-log-index-read-underdesigned], which already records why the window replaced a bare five.

#### Cycles step narrates this session's own diagnosis inside the rule [plan-cycles-step-carries-dated-history]
From the compliance audit of the rule changes since 3ed3db1, lens 4. Written by the build run that filed this finding, so it is flagged against this session's own work.

`plan.md`'s cycles due-ness check, around line 490, ends its opening paragraph with: "a check that spoke only when it filed was indistinguishable from a check that never ran, which is what it turned out to be." The final clause is dated history — the failure this session diagnosed — written in rule syntax with no "because" to mark it, which is the disguised-rationale shape the lens exists to catch. Delete the whole clause and the instruction to speak whenever a cycles doc exists still reads complete.

The same wording was carried into `next.md` and `done.md` in shorter form; check all three when this is fixed, so the copies do not disagree. Its home is the LOG entry for [cycles-check-fires-nowhere].

#### Delete branch's "judgment, not a test" line is commentary plus a restatement [plan-delete-branch-commentary]
From the compliance audit of the rule changes since 3ed3db1, lens 4. Minor.

`plan.md`'s delete branch, around line 1252, follows its decision block with "Judging 'fully relocated' is a judgment, not a test — and naming each part's destination is what makes a wrong one visible." The first half is commentary on the block above; the second half restates a requirement the block already carries, since its narrate arm says to name where each part went.

The step fires at the delete disposition, once per deleted item. Small on its own, filed because the eviction pass that handles findings 4 to 6 will already have this file open.

#### Doubled-rules table claimed the method carried narration cadence when it did not [audit-checklist-table-overclaimed-cadence]
From the compliance audit of the rule changes since 3ed3db1. Outside the audited delta — `resources/method-compliance-audit-checklist.md` has not changed since the last audit — but found while reading the checklist to run this one, and filed rather than dropped.

The table at line 128 lists "How often to speak while working (narration cadence)" as carried by M, the method's own always-loaded file, and not by G. That row is what tells a reader this project's cadence behaviour tests something the method ships. It was not true: until the build filed as [narration-cadence-promotion-candidate] ran this session, the cadence rule lived only in the brevity output style, so a project declining the style got none — which is why that item was filed in the first place. The row appears to have been written when the deleted output style's rules were counted as migrated into M, and one of them was not.

Two things to do, and the second is the reason this is worth more than a one-word edit. The row is now true, so it needs no change for today. What needs checking is the rest of that migration: the same paragraph claims three style-only rules moved into M, and at least one demonstrably did not, so the other two should be verified against the shipped file before the table is trusted again. A table that reports coverage the corpus lacks is the over-claiming this project guards hardest against, and this one sits inside the checklist that audits for exactly that.

#### Mid-build scope question landed as a flat menu, and the user had to ask for the recommendation [build-scope-ask-lands-as-a-menu]
From the AFK-cats transcript pair, build session `028fb28e` (1.20.0-test18). Checked against the current build before filing: live.

The run's test suite found a real daylight-saving bug in a file already in scope. The build stopped and asked: "Shall I add that fix to this item's scope, or leave the bug and file it as its own queue item?" — two outcomes, no recommendation, though the message right before it had already established the fix was small, in one file, and in scope. The user answered "as you recommend", which is them spending a turn asking for the recommendation the question owed them.

`next-build.md`'s scope-growth branch models the minor arm as one recommended ask — "This needs [work], which means editing [file] — add it to scope?" — so the specimen is right and the branch around it is what let a two-option menu through: it presents minor and significant as a pair of routes, and a run that has just decided which one applies can still write both out. The always-loaded narration rule (dependency ownership: lead with the recommendation, alternatives as fallback) is the rule being missed.

Worth checking the same shape at the run's other blocking asks — the discovery rule's needed-and-minor arm has the same two-outcome structure. The same session shows the contrast working: the planning run recommended explicitly five times ("I'd take the first", "I'd do it now") and the user's "as you recommend" there was agreement rather than a request.

#### Claude invoked /plan itself and handed the user a red error, against the rule naming that exact failure [claude-invoked-plan-against-the-rule]
From the AFK-cats transcript pair, planning session `da1599f2` (1.20.0-test18). Checked against the current build before filing: live, since nothing about the rule has changed.

The session's first exchange: Claude said "Rules loaded (`docset: current`). Starting the planning run", attempted to run the skill, and the attempt failed. Its next message told the user the skill "can't be started from my side" and asked them to type it again. So the user's first experience of the session was an error, followed by being asked to repeat what they had already done.

The always-loaded rules name this precisely — the method's own skills ship with model-invocation disabled, an attempt fails and shows a red error, and the rule exists because it had already happened once at a close. The rule was loaded (the session says so in the same breath) and not followed.

What to work out at processing: this is a rule that is stated, read and still missed, which is the shape the gate's admission questions are for. Candidates are wording (it sits inside a bullet about running commands generally, so the prohibition reads as an aside to a rule about doing more yourself) and placement (nothing fires at the moment of temptation — the opening, where a session has just been handed a skill's instructions and reads them as something to start). Whether a hook could refuse the call is worth asking, since the failure has a mechanical signature.

#### Context-coverage caveat was written three times across one pair of sessions [coverage-caveat-repeats-within-a-session]
From the AFK-cats transcript pair (1.20.0-test18). Checked against the current build before filing: live.

The line "I can't tell whether any of our earlier conversation has dropped out of view, so this is what I could still see rather than a guarantee I've caught everything" appears at the build session's close, at `/rescan` in the planning session, and again at the planning close. Twice of those three are inside a single session, minutes apart.

Each instance is honest and none is wrong — the rule requiring it is doing its job, and the fix is not to say it less truthfully. What is worth deciding is whether a session that has already given the caveat needs to give it again in full at the next scan, or whether a shorter back-reference carries the same information. The reader is a non-coder meeting an unfamiliar limitation; the first statement teaches it, the third reads as boilerplate, and boilerplate is what people learn to skip past — which is how a genuinely important caveat stops being read at all.

Small, and filed because the cry-wolf failure it edges toward is one this project has repealed measures for twice.

#### Build view drops file paths an item's work depends on, because they live in rationale prose [build-view-drops-paths-in-rationale]
Noticed by Claude while running the two transcript audits in this session's build run.

Both transcript-analysis items name the exact `.jsonl` paths to read. Those paths sit in the item's rationale prose, not in its `Changes:` line — so the generated build view, which carries the build block and no decision history, showed the instruction "preprocess both transcripts" with nothing saying which two. The run had to open QUEUE.md to find them, against the standing rule that a build leaves the queue closed.

This is the view's stated cost landing on a case it did not anticipate. The view drops history deliberately and that design is not in question; what this shows is that a path can be *instruction* while sitting in a sentence that reads like *context*, and nothing at the keep-step catches it. An item whose work is "read these two files" has its file list in the wrong place, and the item still passed the two-limb buildability test because its `Changes:` line does say what happens.

Two directions for processing, and the first looks cheaper. Either the keep-step's build block gains a place for inputs an item reads (distinct from files it changes), so a path an audit needs travels in the block; or the buildability test gains a limb asking whether everything the work needs to start is inside the block rather than around it. Worth checking how many existing items would fail whichever is chosen before committing to it.

#### Six unbuildable items sat cleared to run, and a build run was the first thing to catch them [unbuildable-items-persist-in-the-ready-region]
From the Taskflowapp transcript pair, build session `8731b6b2` and the planning session `536b761a` that preceded it by hours (1.20.0-test18). Checked against the current build before filing: live.

The build stopped before locking scope and named six items it could not scope — a tier model naming no billing library, cloud sync whose backend was never chosen, an MCP setup screen pointing at a server with no host, that server itself, a reconciliation item depending on it, and a content item waiting on words that sit unwritten in Unprocessed. It checked their archived specs too and found "[To be filled in during the next planning session.]" where the goal should be.

All six were already in the ready region from earlier sessions. The planning run that day worked the fourteen unprocessed captures and reported "24 items cleared to build", with nothing flagged. The digest is supposed to report an item whose file list names nothing to change — that is one of its placement contradictions — so either it did not reach these items or it reported and nothing surfaced them. This was not verified by running the digest against that queue, so the cause needs establishing before anything is designed.

The shape of the gap is the part worth keeping either way: the buildability test runs at the keep-step, once, and an item that passes it (or was cleared before the test existed) is never asked again. Everything downstream trusts the ready region, so six items rotted there in plain sight and the first mechanism to notice was a run refusing to start. Twenty items built after they were dropped, so the run recovered — but the recovery cost the user a turn and the diagnosis cost the run its first act.

#### Compile check reported a pass that came from the pipeline's last command, not the compiler [piped-check-reports-the-wrong-exit-code]
From the Taskflowapp transcript pair, build session `8731b6b2` (1.20.0-test18). Checked against the current build before filing: live.

The run put a Gradle build through a pipe ending in `tail`, read the exit status, and reported the compile as succeeding. Gradle had already failed; the status belonged to `tail`. Claude caught it later and said so plainly — "my first compile check reported success, but that exit code came from the `tail` at the end of the pipe, not from Gradle".

`next-build.md` tells a run to verify whatever it can and treats a check Claude can run as part of building. Nothing anywhere says a piped command reports only its last stage, so a run that trims noisy output — which is the natural thing to do with a build log — can turn a failure into a pass without noticing. The tick that follows then reads "done, confirmed", which is the one tick form that asserts something ran and passed.

A false pass is worse than no check at all: an unconfirmed tick names what still needs running, and this one names nothing. Worth writing into the build doc's verification guidance rather than left as something each session rediscovers — and worth checking whether the same shape can reach the hook suites, which this project runs as plain scripts and reads the same way.

#### Run assumed a build environment was absent instead of asking, and the user quoted the method back [environment-check-skipped-user-had-to-cite-it]
From the Taskflowapp transcript pair, build session `8731b6b2` (1.20.0-test18). Checked against the current build before filing: live — the rule is unchanged.

Gradle failed from the run's own shell. The run concluded it could not compile, recorded an outstanding check, and asked whether to carry on with the Kotlin work uncompiled or retreat to the four document items. It never asked whether the user could build.

The user's reply, in their own words: *"you're supposed to ask me if I have android studio then add it to a list of tools the project has on hand, as I understand Throughliner method"*. They were right about the first half — `next-build.md` says before assuming a device or environment is absent, check, and ask whether one is available rather than assuming none is, on the recorded ground that a check wrongly skipped sits unrun for weeks.

Claude's own correction names the defect exactly: what it had established was "can't compile *from my shell*", not "can't compile". That distinction is the whole rule, and the rule as written does not make it — it says to check whether an environment is *available*, which a session that just watched a tool fail will read as already answered. Whether the fix is wording, or a narrower trigger keyed on a tool failing rather than on an environment being absent, is the question for processing.

The cost here was the whole run: the session ended with the build question open and twenty items part-built.

#### Tools a project has on hand have no home, so each session re-derives them or assumes wrong [no-home-for-a-projects-tool-facts]
From the Taskflowapp transcript pair, build session `8731b6b2` (1.20.0-test18). Raised by the user in that session; checked against the current build before filing: live.

Asked to record what the project has available, Claude answered correctly that Throughliner has no tools-inventory document and that per-project working facts belong in the project's own CLAUDE.md. That answer is right about today and does not settle whether it should be.

What that session established and then had nowhere durable to put: Android Studio is installed, its bundled JDK 21 runs fine at a known path, the Android SDK is at a known path, and Gradle's client-to-daemon connection fails from Claude's shell specifically while a plain loopback test succeeds. Every one of those is a fact a later session needs and cannot cheaply re-derive — the last one especially, since rediscovering it costs a run its first act, which is what happened.

The user expected a list. The method's nearest existing answer is the project's own CLAUDE.md, which is method-adjacent rather than method-owned, so nothing prompts a session to write there and nothing tells a later session to read it for this. Related to [environment-check-skipped-user-had-to-cite-it]: the check that rule requires is much cheaper when the answer from last time is written down, and a recorded "Gradle fails from Claude's shell here" turns an assumption into a known.

For processing: whether this is a scaffolded section in the project's CLAUDE.md that the build doc points at, or something smaller — a convention that a build recording an outstanding environment check writes what it learned beside it.

#### Sent-register line claimed answers the message it points at never contained [sent-line-written-from-decisions-not-from-the-message]
From the Taskflowapp transcript pair, planning session `536b761a` (1.20.0-test18). Checked against the current build before filing: live.

Mid-session Claude recorded three settled answers as having been sent to another project, then caught it: *"I wrote that into the sent record, but the reply I actually sent didn't contain these answers. Removing that line."* A second message carrying the answers was drafted and sent later, so the record ended correct — but only because the same session noticed within the hour.

The register exists so that a later repeal can be checked against what was actually claimed. A line written from what the session decided, rather than from the text of the message that went out, records the session's intent and not the correspondence — which is precisely the thing the register was built to stop, one layer up. The rule requires the line in the same turn as the approval and says it carries what the message claimed; nothing says to write it *from the approved text*, and the two come apart exactly when a session settles more than it sends.

The fix is likely one clause on the existing rule rather than new machinery — the approved wording is on screen at the moment the line is written, so reading the claim off it costs nothing. Worth checking the existing lines in this project's own `INBOX/sent.md` for the same shape while the fix is being scoped, since nothing has ever checked them.

#### Rule-gate lines in a build working file attach by position, so a later tick can land between an item's own lines [gate-line-in-working-file-is-positional]
Noticed by Claude at the close of the 2026-08-26 build run, and filed on Alex's direction.

Each ticked item writes up to three lines into the working file's Progress block: the tick itself, a `Depth: <slug> — …` line, and, where the item carries one, a transcribed `Rule gate:` line. The depth line is slug-bound, and next.md says plainly why — a bare positional line attaches to whichever tick it happens to sit under, so two written together silently attach to the wrong items. The gate line carries no slug and has exactly that problem.

It happened three times in one run. Each new tick was written by matching on the previous item's last line, and where that item's last line was its depth line rather than its gate line, the new tick landed between the two — leaving a gate disposition sitting under the wrong item's tick. All three were caught and repaired in the same session, by a run that happened to be watching for it. Nothing would have caught them otherwise: the close reads depth by slug, so it never has to notice the gate line's position, and the working file is deleted at the close.

**The consequence if one survives is small but exactly the kind this project cares about.** The close transcribes each item's gate disposition into that item's LOG entry, and the board's checks read those entries. A disposition attributed to the wrong slug is a wrong record of which rule was gated, in the one artifact the gate produces as evidence.

Two candidate fixes, and the first mirrors a decision already made here: give the gate line a slug, as the depth line has, so it is self-identifying and the close reads it by slug rather than by what sits above it. Or state the per-item write order in next.md's completion step so the three lines are written as one block — cheaper, but it depends on care rather than removing the need for it, which is the argument the depth line's slug already won.

#### CLAUDE.md's Architecture section undercounts the skills and hooks that actually ship [claude-md-architecture-undercounts]
Found by the v1.21.0 release sweep's CLAUDE.md pass. The Architecture section says "**4 skills:**" and lists four, omitting `/rescan`; and "**3 hooks** — two enforcing, one advisory", omitting `stop.py`. The plugin ships five skills (`plugin/throughliner/skills/` holds setup, plan, next, rescan, done) and four hooks (`plugin/throughliner/hooks/` holds session_start, pre_tool_use, stop, post_tool_use). `plugin.json`'s own description already names five skills, and SPEC.md already describes both `/rescan` and the `stop` hook correctly — so this file is the one that fell behind.

Why it matters beyond tidiness: this is the always-loaded project file every session here reads to orient itself. A session reading it learns the method has no `/rescan` and no `stop` hook, which is the same class of failure the migration's retired-term detection exists to catch in consumer projects.

The fix is a straight correction of both counts plus one bullet each, worded from SPEC's existing descriptions. The edit was attempted during the release sweep and refused by the scope-lock, which was right: the build working file had already been deleted at the close, so the session was on the standing planning list and CLAUDE.md is not on it.

Rule gate: not needed — a stale description corrected to match what ships; no rule authored or amended.

