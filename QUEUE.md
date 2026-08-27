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

#### [user] Smoke-test the `#beta` install on your second machine, then edit the how-to post's install command [beta-install-smoke-and-post-edit]
Filed 2026-08-26 with [beta-branch-install-pin]. Two sequential user steps: the ref-pinned route is unverified against the open feature requests the research names, so it is proven on a real second machine before any tester is pointed at it; and the published "How to install" forum post claims the plain two-command route, which the pin falsifies — the correction is yours to make, per the repeal-falsifies-an-announcement rule.
**Walkthrough.**
1. On your second machine, open a fresh Claude Code chat and ask it to add the plugin marketplace `FlintcraftTech/throughliner#beta` and install `throughliner@flintcraft`. Look for: both commands succeed without a ref error.
2. Fully quit and reopen the app, open any empty folder, and type `/setup` in the chat box. Look for: the setup command appears in the menu — the smoke test from INSTALL.md.
3. If either step fails, tell this project the exact error and stop — the install post stays as it is and the pin gets re-examined.
4. On success, edit the "How to install" forum post so its install ask names `FlintcraftTech/throughliner#beta`. Look for: no live claim pointing new users at the unpinned route.
5. Tell this project; the register line for the install post is updated with the corrected claim and this line closes.

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
**Lifted 2026-08-26 at the next planning opening.** The redesign was built in the beta-eve run (`2026-08-26-plan-log-index-read-underdesigned-build.md`), the host has since been reinstalled at 1.21.0, and this very opening exercised the derived-window read live — built, live, and observed working. One-a-day pacing still applies at posting time.

#### [user] Create the Throughliner Discord bot and hand its token to the project [discord-bot-server-setup]
Split 2026-08-26 at the keep of [discord-posting-bot] — the Discord-side setup only you can do. The bot account is what gives the posting script a route; the script build is held behind this line.
Red flag · State: cleared — the bot token is a credential on your disk: anyone or any session that reads it can post as the bot in your server. Designed out as far as it goes: stored inside `INBOX/` (gitignored on every path, so it can never be published) and never quoted into any document or chat, the address-book rule. It stays readable on this machine, and you were told so plainly and chose to proceed ("ok I'm willing to try it"), recorded 2026-08-26.
**Walkthrough.**
1. Open discord.com/developers/applications in your browser, sign in, and click "New Application". Name it (e.g. "Throughliner"). Look for: the application's settings page opening.
2. In the left menu click "Bot", then "Reset Token", and copy the token it shows. Look for: a long string you can copy — it is shown only once.
3. Paste the token into a new file `INBOX/discord-bot-token.txt` in this project (ask Claude in this chat to create the file and confirm the gitignore covers it before you paste — the file must never be committed).
4. Back in the left menu click "OAuth2" → "URL Generator": tick the `bot` scope, then the permissions "Send Messages", "Manage Messages" and "Read Message History". Open the generated URL and invite the bot to the Throughliner server. Look for: the bot appearing in the server's member list.
5. Tell this project which channels the bot may post in (main channel, test-rezips). This line closes when the token file exists and the bot is in the server; the script build lifts.

#### [user] Test-rezips entries name how to obtain the build — pin edited, commit line in every entry [test-rezips-entries-name-obtain-route]
Surfaced by /rescan 2026-08-27, from the port prompt handed over this session: that prompt tells a porter to use "the newest test-rezips entry's build, obtained however the entry provides it" — and the entries so far provide nothing, the first one linking the release page instead. A porter or raw-build tester following the newest entry has no way to get the build it describes.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Both surfaces are Discord posts only you can edit until the posting bot ships. The eventual script formats entries the same way — noted here and to be read by [discord-posting-bot]'s build, referenced by slug.
**Walkthrough.**
1. Open the test-rezips channel pin and add one line: every build entry names the repository commit it was cut from (and attaches a zip where one is offered). Look for: the pin's edited text showing the promise.
2. From the next rezip entry on, include a line "Commit: <hash>" — Claude supplies the hash in the entry draft whenever it drafts one.
3. Tell this project the pin is edited; the register line for the pin is updated with the added claim and this item closes.

--- Build block ---
Changes: none in this project — the artifacts are Discord posts. The entry-format note travels to [discord-posting-bot] by this slug.
Acceptance: the pin's text promises the commit line, reported by you.
--- End build block ---

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

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, was still true when this was filed and is falsified as of 2026-08-27: [builds-read-the-queue-again] retires the view, so both paragraphs now need rewriting at step 2 — the first against the shipped read-the-queue model, the second against the final article. The claim was approved but never posted (`INBOX/sent.md`), so no public correction is owed. The rewrite runs after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. You post it, with the live article URL pasted in — Claude has no route to Discord. 5. You confirm, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Kept 2026-08-24, held below the line on Claude's recommendation and your agreement.** As a capture this carried its ordering in prose because captures have no `Blocked by:`; as a held work item it carries the field, so it lifts by itself when the article item closes instead of being re-offered every session while the external review is out. The same ordering sentence is written on the article item per the known-ordering rule.
Blocked by: [competition-comparison-article]

#### Discord posting bot: an all-rounder so posts and rezip-list updates can be made straight from a session [discord-posting-bot]
Raised by you 2026-08-26, in the post-close tail, as a side-thought filed for a later /plan. The want: the test-rezips channel's posts and their updates — adding notes to previous entries when issues are reported, changing an entry's stable status — done by a bot rather than by hand, and more generally an all-rounder bot this project can post through directly during /plan or a build. That would be the first route Claude has to Discord, so the never-send-unseen guarantee has to be designed in from the start: nothing posts without you seeing the exact text and saying yes, and an automated update is still a send. Bears on the nerds-list mechanics left open on [expedite-first-beta-release] and on the eventual [weekly-release-cycle] turn.

**Kept 2026-08-26 at the next planning session, on Claude's recommendation and your agreement — "ok I'm willing to try it."** It designs out smaller than "bot" sounds: no hosted service — a bot account (the Discord-side setup split out as the `[user]` line [discord-bot-server-setup], which holds this build) plus a script making one API call per send or edit. The token risk and its informed consent are recorded on that item's red flag. Every send stays behind the exact-text-yes rule; a register line is still written per post; the route is all that changes, which falsifies CLAUDE.md's "Claude has no route to Discord" sentences — amended in this build, with the never-send-unseen rule restated where they stood.

Rule gate: run — amendment to CLAUDE.md's Discord section (the no-route sentences replaced by the route-plus-approval statement); no new freestanding rule, the send-approval rule unchanged and cited.

--- Build block ---
Changes: `resources/discord_post.py` — standard library only, UTF-8 reconfigure per the scripting constraints: send a message to a named channel, edit a previous message by id, token read from `INBOX/discord-bot-token.txt`, exact text passed in from a file; verified against Discord's current API docs before writing. `CLAUDE.md` — Discord posts section: the "Claude has no route to Discord" sentences amended to name the bot route, with the exact-text-yes approval and the sent-register line restated as unchanged; walkthrough steps in queue items keep "you post" wording only where a post genuinely stays manual.
Inputs: `INBOX/discord-bot-token.txt` (created by [discord-bot-server-setup]), the channel ids the user names there. Entry format: every test-rezips entry the script posts carries a "Commit: <hash>" line, per [test-rezips-entries-name-obtain-route].
Acceptance: a test post to the test-rezips channel, its exact text approved by you first, appears in the channel and is then edited by the script; the token is never printed, quoted or committed; CLAUDE.md nowhere still claims Claude has no route to Discord.
Refused: a hosted always-on bot — nothing here needs to listen, only to send; per-post manual copying stays available whenever you prefer it.
--- End build block ---
Blocked by: [discord-bot-server-setup]

#### [user] Discord post draft: plain-English consent [discord-post-plain-english-consent]
Drafted 2026-08-25 at the planning close under the close-sweep design ([plan-close-post-drafting]); approved as a candidate by you, with your addition of the terse-docs mention. [keep-approval-reading-burden] shipped 2026-08-26 and its claims held — then held again 2026-08-27 behind [shared-vocabulary-not-standing-names], whose build retires "the ready list", which this draft's example quotes. At the lift: reword the example to the method's own words, re-verify the whole draft against the shipped build, then post on a day no other Throughliner post goes out.
Blocked by: [shared-vocabulary-not-standing-names]
**Draft (under 2,000 characters):**
> **Plain-English approvals.** When you and Claude go through your captured ideas in a planning session, each one now opens with a plain-English summary of what the idea says — right there in the chat, before any analysis. And when Claude recommends what to do with it, it says in plain words what would actually change ("this would go on the ready list — the queue's cleared-to-build region") and asks whether you agree, in those words. No procedure jargon, no needing to open the queue file to know what you're saying yes to: you approve what's in front of you.
>
> The files themselves stay tidy through a companion rule: everything written into your project's documents is bounded by the project's own measured norms, so records stay terse enough to actually read when you do open them. The summary serves the moment; the documents serve the return visit.

## Unprocessed

#### Last session advises: plan next, and start with the three failures this run recorded about itself [last-session-advises]
Advice from the 2026-08-27 build close, not work. The next planning run reads this and deletes it in the same breath.

**Plan rather than build.** Only 5 items are cleared to run and all five are `[user]` work, four of which this run already addressed. Unprocessed holds twelve fresh captures. A /next now would reach almost nothing.

**Start with the three self-observations, and weigh them together rather than one at a time** — [capability-just-granted-not-considered], [walkthrough-jargon-broken-by-its-own-author] and [file-link-not-offered-at-hand-over]. All three are the same shape: a shipped, clearly written rule that did not fire at the moment it applied, and two of the three were caught by the user rather than by anything in the method. One of them broke a rule this very run had authored an hour earlier. The third capture names a candidate worth testing against the transcript: all three happened while composing a message handing something over, and none while editing a file. A rule per instance is what the admission gate exists to refuse.

**Then [no-route-to-discord-is-false]**, which is the highest-value single fix: this project's own always-loaded instructions still tell every session that Claude has no route to Discord, and that route now exists. It is the standing instruction that would have produced the capability failure above again tomorrow, memory or not.

**Two lifts are waiting**, both blocked on work this run shipped: [discord-post-plain-english-consent] (its own prose already says to reword its "ready list" example at the lift) and [comparison-article-post-needs-rewrite].

**One red flag is uncleared**: [bot-prunes-test-rezips]. An unattended prune holding Manage Messages deletes published messages irreversibly, and a wrong bound could take the channel pin or another member's post. It wants deciding before it is built, not during.

**And [compliance-audit-lag] is filed as an `[audit]`.** This run authored or amended roughly twenty rules and moved the always-loaded corpus by +47 statements for consumers — the largest single movement on record. That audit is the check on this session's own work.

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

#### Should cycles get mermaid diagrams? [cycles-mermaid-diagrams]
Captured by you, 2026-08-24, mid-planning — your framing: seems reasonable. Filed at your direction without discussion, so the idea is unshaped: what a diagram would show (a cycle's steps? the turn's two events? due-ness over time?), where it would live (in CYCLES.md beside the definition, or generated), and who reads it are all open for the keep-step. Context worth having there: the desktop app renders mermaid in its markdown viewer, and the cycles doc is user-facing by design.
Skipped 2026-08-26 on Claude's recommendation and your agreement: what settles it is a build that must ship first — [weekly-release-cycle] creating this project's first real cycles doc, with the due-ness check working ([cycles-check-fires-nowhere]'s fix). A diagram designed before any real cycles doc exists would be guessing at a document nobody has seen; take it up once there is one to draw.

#### setup.md's Step 3 heading still promises two settings questions the step says do not exist [setup-step3-heading-stale]
Noticed while tagging setup.md for [setup-case-d-untagged]. The heading reads "Step 3: Interview (adaptive discovery + two settings)", and the step's own body states plainly that there is no settings question at all, here or anywhere — the last one was dropped in favour of ignoring `INBOX/` on both paths. So the heading contradicts its own step. Left alone rather than fixed in that build, because the item was scoped to response-shape tags and a heading rewrite is not tagging. The fix is one parenthetical; the reason to file it rather than drop it is that a heading is what a session reads first when it jumps into a step, so a stale one steers the read before the correcting sentence is reached.

#### [user] Delete the test cycle fixture and its filed capture from the demo project [cycles-fixture-cleanup]
Split out of [cycles-due-check-verification], whose verification passed on 2026-08-26 (`LOG/2026-08-26-cycles-due-check-verification-2.md`). What remains is housekeeping in another project, not verification: `DEMOS/Polit Fart Announcer 1` still carries the made-up `CYCLES.md` with its `[weekly-listen]` definition and fixture observable of 2026-08-10, plus the `[weekly-listen]` entry the check filed into that project's Unprocessed.

Both are downstream of a fixture rather than work that project chose — the user's correction on 2026-08-26: the whole cycle was made up as a test, not just its date. The three items the filed entry overlaps ([reload-persistence-check], [other-chimes-unheard], [honorifics-never-fired]) were queued on their own merits and are untouched by this.

Filed as its own item because a walkthrough ends at the item's observable and cleanup after a test gets its own line — and because no session here writes another project's files, so this can only be done in that project's own chat. It blocks nothing: the verification it follows has already passed.

**Walkthrough.**
1. Open a chat on `DEMOS/Polit Fart Announcer 1`. Ask Claude there to delete `CYCLES.md` from the project root. Look for: the file gone from the folder listing.
2. In the same chat, ask Claude to delete the `#### [user] Weekly listen-through of the page is due [weekly-listen]` entry from that project's Unprocessed. Look for: the entry gone from QUEUE.md, and the three items it named still present.
3. Tell this project it is done; this item closes.

#### Discord posts split into tips and news, and the posting rule describes only one kind [discord-channel-purposes-split]
Raised by you on 2026-08-27, while naming the channels the bot may post in. Your decision, in your own terms: what currently sits in *announcements* is posts that will from now on be known as **tips**, and *announcements* is being narrowed to **news only**. The bot may post in tips, announcements, and test rezips for nerds.

This project's own posting rule (CLAUDE.md, "Discord posts") does not carry that split. It describes a single kind of post — announcing new features, changes and improvements to Throughliner — and explicitly rules out tips on using Claude Code and general development lessons, with the test being "did Throughliner change" rather than "did we learn it". Under the new split that test still fits announcements-as-news, but it is the wrong test for a tips channel, and the rule now has nothing to say about the channel that will carry most of the volume.

Worth settling before a bot can post anywhere, because a bot aimed at the wrong channel is a published mistake rather than a draft one, and because the existing rule would currently refuse to draft the tips the tips channel is for.

What a planning session would decide: whether the posting rule gains a second kind with its own test, or whether tips are out of scope for this project entirely and only news is drafted here; and what the draft brief is for a tip, given the existing brief is written for a feature announcement. Also whether `INBOX/sent.md` should record which channel a post went to — it currently records the destination as "the Throughliner channel", which no longer distinguishes anything.

Filed rather than built: this changes a standing rule about what leaves the machine, and rule admission is planning work.

#### Posting bot prunes old test-rezips entries after each new post [bot-prunes-test-rezips]
Your decision, 2026-08-27, given while the channel pin was being edited: pruning old entries is no longer a by-hand job — now the bot exists it can be done from this project, straight after each new build entry is posted. The pin no longer claims hand-pruning; it was reworded to name no mechanism at all, precisely so this can ship without the pin becoming wrong.

Scoped as an addition to [discord-posting-bot] rather than separate work: the same script that posts an entry does the prune in the same run. Referenced by slug from both sides.

What the build has to settle: how many entries the list keeps (a number nobody can derive is a bare number, so it wants your figure or a rule like "keeps the newest N of each label"); that the **pin itself is never pruned** — it is a pinned message rather than a build entry, and the prune must exclude it by construction rather than by ordering luck; and what happens when a prune fails partway, since deleting published messages is not recoverable.

Two facts established live this session and worth carrying into that build:
- the bot's `Manage Messages` permission is what allows deleting other people's messages, and it is already granted;
- a bot can only EDIT messages it authored itself, so anything the bot may later need to rewrite has to have been posted by the bot in the first place. Pruning is deletion, not editing, so this does not block the prune — but it does mean an entry posted by hand can never be corrected by the bot afterwards.

Red flag · State: uncleared
Deleting published messages is irreversible and reaches other people's posts. The prune targets a public channel, runs unattended after a post, and has `Manage Messages` — so a wrong bound, an off-by-one, or a mis-parsed entry deletes content nobody can recover, including potentially the pin or another member's message. The risk is stated rather than designed around here: what to do about it is the build's decision and yours, not this capture's.

#### Sent-register pointer resolved to nothing — the pin's text was not where the register said [sent-register-pointer-resolves-to-nothing]
Found live on 2026-08-27 while trying to rewrite the test-rezips channel pin. The register line in `INBOX/sent.md` for that pin ends "posted text verbatim in `LOG/2026-08-26-beta-day-one-posts-2.md`". That record contains no quoted text at all — no blockquotes, no fenced block, nothing. The pin's words were in no other record either. What the project actually held was the register's own one-clause paraphrase of the claims.

This defeats the register's stated purpose. The rule says a post's claim is recorded so a later repeal can be checked against it, and a pointer that resolves to nothing means the check cannot run — while the line still reads as though it can, which is worse than an obviously missing record. The failure was only found because a session needed the text for something else; nothing detects it.

The text was recovered from the live channel through the newly-built Discord bot, so the pin's words are now genuinely on file in `LOG/2026-08-27-test-rezips-pin-edited.md`. That repairs this one instance and nothing else.

What a planning session would settle: whether the same fault sits on other register lines (several say "posted text verbatim in <file>" and none has been checked); whether a pointer should be verified at the moment it is written, which is the only moment the text is definitely to hand; and whether the bot now makes recovery cheap enough that unverified pointers matter less — noting that recovery only works for channels the bot can read, and only while the message still exists.

Related: [bot-prunes-test-rezips] would delete old entries, which removes the recovery route for exactly the posts whose text was never stored.

#### Capability granted minutes earlier was not considered when the work needed it [capability-just-granted-not-considered]
Raised by you on 2026-08-27, in your own words: *"you're supposed to have read message history access through the bot"*.

The sequence, which is the whole point of the capture. Claude walked you through creating the Discord bot, and in that walkthrough specified Read Message History among its permissions and confirmed the token was on disk. Roughly twenty minutes later, in the very next item, Claude needed the text of a Discord message, could not find it on file, and offered you two ways to supply it yourself — never considering the bot it had just provisioned for reading Discord.

The method already carries the rule this breaks: before handing work to the user, name the tool that would do it and confirm it is absent or unauthenticated. Here the tool was present, authenticated, and had been set up in the same session by the same session. The check either did not run or ran against stale knowledge of what this project can do.

Why it is worth a rule rather than a shrug: the existing check is written for tools that might exist somewhere in the environment, and it is weakest exactly where it should be strongest — on a capability so new that nothing in the project's documents mentions it yet. A session's sense of "what I can do here" is formed early and is not re-derived when it changes mid-session.

What a planning session would settle: whether anything durable should record a project's live capabilities as they are gained — a `TOOLS.md` line written at the moment a credential or integration lands would have answered this in one look — or whether the fix belongs in the capability check's wording, requiring it to re-read what this session itself has set up. Note that `TOOLS.md` already exists for exactly this class of fact, which suggests the gap is a missing write rather than a missing mechanism.

#### Walk-through jargon rule broken within the hour by the run that built it [walkthrough-jargon-broken-by-its-own-author]
Found live on 2026-08-27. Your words when the step arrived: *"I don't understand what you want me to do"*.

Earlier in the same run, two rules shipped: general developer and testing vocabulary joins the translate-away list ([general-jargon-translate-and-walkthrough-readback]), and a step being handed over is read back for such terms before it goes out. Within the hour the same session handed you a step reading "Developer Portal → Bot → Privileged Gateway Intents → Message Content Intent → Save Changes" — four terms naming nothing in your own files, no indication where any of them sit on screen, and no read-back.

Re-explaining it as five located steps worked immediately, which is the evidence the rule is right and the trigger is what failed.

The uncomfortable part, and the reason this is worth filing rather than noting: the rule was not forgotten. It was authored, tested against a specimen and written into the shipped docs by the session that then broke it. So "state the rule more clearly" is not the fix — the rule was as clear as it will ever be to its own author. What failed is that nothing fires at the moment a step is composed; the read-back is an instruction to remember to re-read, which is the shape this project has repeatedly found does not hold.

Compounding it: those steps were also not verified before being handed over. The permission fix and the intent toggle were each described from Claude's model of Discord's interface rather than checked, and the first description of the intent toggle was the one that failed.

What a planning session would settle: whether a hand-over step can be checked mechanically at all (a word list is the obvious idea and the rule itself already refuses one, on the ground that the class is open-ended); or whether the answer is structural — for instance requiring every handed-over step to name a thing on screen and a thing to look for, which is a shape a reader can check even where the vocabulary cannot be enumerated. Note that requirement already exists for authored walkthroughs and was not applied to a step composed live.

#### CLAUDE.md still says Claude has no route to Discord, and that stopped being true today [no-route-to-discord-is-false]
Surfaced by /rescan at the end of the 2026-08-27 build run. The Discord posts section of this project's CLAUDE.md ends "Claude drafts and Alex posts, because Claude has no route to Discord." The bot built and authorised in that same run read the test-rezips channel's pinned message live, so the stated reason is already false, and the posting half becomes false when [discord-posting-bot] ships.

This is not a tidying job. The sentence is a standing instruction read at the start of every session in this project, and it tells a session not to look for a route. That is the precise shape of the failure recorded the same day in [capability-just-granted-not-considered]: work was handed to the user that the project could have done, minutes after the capability landed. The instruction would have produced that outcome again tomorrow even without the memory lapse.

What a planning session would settle: what the sentence becomes. Reading and posting are not the same permission and should probably not be described together — the bot can read the channels it has been added to, and posting stays gated by the standing rule that nothing leaves the machine without the user seeing the exact text. That approval rule is untouched by any of this and should be restated rather than quietly dropped, since "Claude has no route" was doing double duty as both a fact and a safeguard. Only the fact has changed.

Also worth settling in the same pass: whether the draft-and-hand-over flow survives at all for channels the bot can post in, or whether the user approves text that Claude then posts directly.

Related: [capability-just-granted-not-considered], [discord-channel-purposes-split], [bot-prunes-test-rezips], [record-discord-environment-in-tools-md].

#### Record the Discord environment in TOOLS.md so the next session doesn't rediscover it [record-discord-environment-in-tools-md]
Surfaced by /rescan at the end of the 2026-08-27 build run. Everything below was learned live that day, by making API calls and by two rounds of you changing settings in Discord. None of it is written anywhere a future session reads, so the next one that needs it repeats the calls and, where a permission is missing, repeats the walkthrough.

`TOOLS.md` at the project root is the home the method already defines for exactly this — facts about a project's environment that are expensive to re-derive — and this project has no such file yet. Any session may write one the moment it has a fact to record, so this is an overdue write rather than new machinery.

The facts:
- the bot's token lives at `INBOX/discord-bot-token.txt`, outside git (proved with `git check-ignore`), and is used as an `Authorization: Bot <token>` header against `https://discord.com/api/v10`;
- the server is "Throughliner fan club";
- **announcements** and **tips** were readable with no per-channel setup;
- **test-rezips-for-nerds** returned HTTP 403 "Missing Access" until the bot was added to that channel's own permissions — a channel overwrite, not a missing scope;
- **main** still returns 403, and has not been granted access, although the bot item expected it to be a posting target;
- Message Content Intent had to be enabled in the Developer Portal, or message text comes back as an empty string with no error;
- a bot can only EDIT messages it authored itself; `Manage Messages` allows deleting others' messages and pinning, never rewriting them.

One thing to decide rather than assume: `TOOLS.md` is committed, so the channel IDs would sit in the repository. They are not credentials and the server is this project's own, but it is a publication decision and yours to make — the alternative is recording the channel names only and letting a session look the IDs up through the bot.

Related: [capability-just-granted-not-considered], which is the failure this write prevents; [no-route-to-discord-is-false]; [bot-prunes-test-rezips], whose build needs the can't-edit-others fact.

#### View-in-doc link not offered until the user asked for it [file-link-not-offered-at-hand-over]
Raised by you on 2026-08-27, in your own words: *"please link to the file so it opens in sidebar"*.

The instance: during the bot walkthrough, Claude created an empty file for the token and told you to find it in File Explorer and open it with Notepad — naming the path in prose but giving no link. The view-in-doc rule already requires a plain link to a file being pointed at, and you had to ask for what the rule already mandates.

Small on its own. Filed because it is the **third instance in one run** of a shipped rule failing to fire at the moment it applies, alongside [walkthrough-jargon-broken-by-its-own-author] and [capability-just-granted-not-considered]. Two of the three were caught by you rather than by anything in the method, and the third was caught only because a later step needed the thing the rule would have provided.

What makes this one distinct from the jargon case: the jargon rule was authored in that same session, so recency was not the problem. This rule has shipped for months. So "the rule is too new to have stuck" does not explain the pattern, and neither does "the rule is unclear" — all three are clearly written and were correctly applied elsewhere in the same run.

What a planning session might weigh: whether these three are one finding rather than three, and if so what the shared cause is. A candidate worth testing against the transcript: all three failures happened while composing a message to hand something over, and none happened while editing a file. If that holds, the gap is that hand-over composition has no checkpoint, while file edits have several.

Not proposing a rule here — a rule per instance is what the admission gate exists to refuse, and the useful move is probably one look at all three together.

#### Throughliner bot needs an icon in the sibling-project house style — white linework on Chagora's background [bot-icon-house-style]
Captured by you on 2026-08-27, on your instruction, with the reference files you named.

**What you asked for:** the Throughliner bot icon redone in the same style as Chagora's, and as AFK-cats' will be — **white linework, on the same background Chagora uses**. The draft to work from is `Throughliner-icon.png` at this project's root. Note it is currently untracked, so git holds no copy of it.

**The house style, read from `Casual Projects/Chagora/icon.png`:** a circular badge with a thin dark rim; the subject drawn as flat, stroke-only **white** line art with no fill and no shading; sitting on a dark diagonal gradient that runs deep red at the left through to a desaturated teal-blue at the right, darkening toward the centre. The line art exists separately as `Casual Projects/Chagora/chagoraiconw.svg` — white paths, no background — which suggests the working method is line art as vector, composited onto the gradient disc and exported as PNG.

**The gap is larger than a recolour, and that is the thing to weigh before scoping it.** The current draft is not line art with the wrong colour on it — it is a fully rendered illustration: a pastel orange-and-blue mascot with gradient fills, soft highlights, dark outlines and an orange flame glow, on black. Turning that into flat white strokes is a redraw, not a colour change, and no filter gets from one to the other. **Corrected at the 2026-08-27 close: a vector source now exists.** `throughlinerprojectboticon.svg` was added at the project root during that session — Inkscape, currently black fill on an A4 page. The paragraph above was written before it appeared and treated the job as a redraw because no line art existed. With vector line art in hand it is much closer to a recolour and composite, which changes who can do it: recolouring the strokes white and placing them on the Chagora background is plausibly Claude's work, not a design act. Confirm the SVG is the intended line art before scoping on it — it was not discussed, only found. The figure in the rendered draft carries a wrench and a pencil, which read well and are worth keeping either way.

**AFK-cats is already staged for the same treatment**, which is why this is a family decision rather than a one-off: `AFK-cats/assets/` holds `cat-noun-project-source.svg` and, tellingly, `reference-sibling-bot-icon.png`. Whatever is settled here sets the pattern for that one.

**On who does it — not settled, and worth splitting at the decision step.** Inkscape is installed on this machine (it is why `python` resolves oddly here, per the scripting constraints), and its command line could do the compositing and export once white line art exists as an SVG. The drawing itself is a design act and is likely yours, or a redraw commissioned some other way. So this probably decomposes into a `[user]` item for the line art and a build item for compositing to the house background — rather than being wholly one or the other.

Also worth deciding: whether the finished icon belongs in the repository (Chagora keeps both the SVG and the PNG at its root), and whether the bot's Discord avatar gets set from it, which is a separate act in the Developer Portal.

#### [audit] Compliance audit over the rule changes since the last audit [compliance-audit-lag]
Filed by the rule checks at the 2026-08-27 build close, under the slug they print. `py resources/rule_signals.py .` reported 3 rule-bearing commits since `2026-08-26-compliance-audit-lag-build.md` uncovered by any compliance audit — and this session's own commit makes a fourth, much the largest, so the real scope is wider than the figure the check printed before the commit landed.

Scoped to the changed files (delta scope, as the check computes it): `CLAUDE.md`, `plugin/throughliner/docs/done-build.md`, `done.md`, `feedback-and-inbox.md`, `next-build.md`, `next.md`, `plan.md`, `rescan.md` — plus, from this session, `skill-nonspecific-rules.md`, `next-audit.md`, `done-plan.md`, `setup.md` and `migrate-checklist.md`. The audit run should recompute the list rather than trusting this one, since the check reads it from git.

The criteria are already written and are not re-derived: `resources/method-compliance-audit-checklist.md` carries the four lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history sitting in operative text (the delete-and-read test).

**This session is an unusually good reason to run it rather than a routine one.** It authored or amended roughly twenty rules in a single run, several by supersession and repeal, and it added +47 always-loaded rule statements for consumers and +144 across the fetched procedure docs — the largest single movement the growth report has recorded. Two of the four lenses are exactly what a run that size is most likely to have degraded: rationale creeping into operative text, and tags placed by habit rather than by the arm they govern.

Worth checking specifically, because they were done fast and late in the run: the response-shape tags added across `setup.md` (fifteen steps tagged in one pass, several with conditional arms), and whether the terminology renames left any sentence whose grammar no longer works around the new word.

As an `[audit]` this edits nothing — it reads and files findings as captures, which the next planning session weighs.

#### SPEC owes two sentences for behaviour built on 2026-08-27 [spec-owes-warn-and-outcomes]
Filed at the build close, by the build that found the gap. Not written into SPEC here: the session that made a choice is not the session that certifies it in product truth, so this waits for a planning run. SPEC lags these two sentences, visibly, until then.

**Most of the run needed nothing.** SPEC already carried the sentences for builds reading the queue's cleared region whole with its reasoning, the completion-ask carve-out keyed on a post-close hand-over, and session_start reporting the date from the clock — all written ahead of the build, which is the lead model working as designed. These two are what it does not carry.

**One, for [warn-dont-enforce-immediate-requests].** SPEC describes no behaviour for what happens when a user asks directly for something a rule of the method would hold back. The shipped rule: one standalone warning turn naming what the request crosses, the risk, and briefly what could be done instead; the work then proceeds on the user's next word, whatever it is; both the warning and the work are recorded. Two carve-outs where the existing gate stands instead — anything leaving the machine still needs an explicit yes to the exact text, and destruction git cannot undo still goes through the file-safety rules. The warning is a turn of its own so the request can be withdrawn, and a second ask is not what unlocks it. This belongs in SPEC because it is a promise to the user about who decides, not an internal procedure detail.

**Two, for [walkthrough-outcome-not-reached].** SPEC's `[user]`-work paragraph describes completion but has no vocabulary for an item a run did not get to. The shipped model: every `[user]` item a run touched ends on one of three outcomes — done, deferred, or not reached — with **deferred written only from the user's own word**, and not-reached telling a later session to present the item fresh. It matters in SPEC because it is what stops a record claiming a decision the user never made.

Suggested placement is beside the existing "No completion asks on `[user]` work" paragraph for the second, and near the multi-item /next paragraph for the first — but where a sentence sits is the planning session's call, as is whether SPEC's own wording differs from the summary above.

