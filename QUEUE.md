# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

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

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected).

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

**Files:** none in this project except the research file step 2 creates under `resources/research/`. The artifact is an article for flintcraft.tech. Relates to [competition-comparison-article] — a separate piece, no dependency either way.

#### [user] Verify the cycles due-ness check live: one capture filed when due, no duplicate on the next opening [cycles-due-check-verification]
Filed 2026-08-22 at the keep-step, on Claude's recommendation and your agreement. The cycles build ("Cycles shipped", record `2026-08-22-cycles-build.md`) ticked done with one behaviour UNCONFIRMED: only the no-doc silent path was exercised, because this project has no cycles doc. Confirming it needs a live session in a project whose `CYCLES.md` carries a past-due observable — user work, since it happens in another project's session during your testing days. The release-cycle definition item ("Define this project's weekly release cycle") is held on this verification and lifts when it closes — timed so the definition can build before Wednesday 10am.
**Walkthrough.**
1. In any project you're testing the rezip in (not Taskflowapp's product files — its INBOX is the only sanctioned write there, so pick another test project), ask Claude to create a test `CYCLES.md` at the project root with one definition whose observable is already past due — say a weekly cycle whose last completed turn reads as two weeks ago.
2. Run /plan (or /next) there. Look for: one capture appearing in that project's queue under the cycle's slug, naming the due step.
3. Run another opening in that project without touching the capture. Look for: no second capture — the check is satisfied while one is open.
4. Ask Claude there to delete the test `CYCLES.md` and the test capture.
5. Tell this project what you saw; this line closes and the definition item lifts.

--- Cleared to run above this line ---

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
Blocked by: [discord-post-context-adjacency]

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
**Blocker repointed 2026-08-22:** the cycles machinery is built (`2026-08-22-cycles-build.md`) with one behaviour unconfirmed, so the fact holding this item is the verification, not the build — the field now names the `[user]` verification line, and this lifts by itself when that closes.
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

**Not designable here yet, and that is why this is a capture.** The file contract, which Taskflow Project a pushed item lands in, and when a push happens all depend on what Taskflow agrees to build — so the second limb cannot be stated. It waits on [taskflow-bridge-request].

**Dated 2026-08-21 with your approval.** It waits on Taskflow's reply to the three questions mailed 2026-08-20, which nothing in this queue can produce; a week is when there is plausibly news, since Taskflow is your own project. Not offered again before then.
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

#### Refer to people by their GitHub-published identity, not first-name habit — the first brick of multi-user Throughliner [github-identity-naming]
**Your idea, 2026-08-22**, raised while processing the consumer report about the lint misreading possessives ("Queue lint reads any possessive-plus-'words'…"). Your reasoning: Claude tends to refer to users by first name or by pronoun, and that habit was designed for the private desktop environment — but the method's documents are committed and can be public, so the register should follow what each person has chosen to publish on GitHub: username, pronouns where supplied, first name only where they put it there. More consistent with people's wishes where privacy is concerned.
**Why it is a capture rather than work:** multi-user Throughliner has never been developed — verified in the record this session: SPEC assumes one user throughout, the provenance conventions ("captured by you") and the lint's possessive list hard-code a single addressee, and no queue or log entry designs for more. This idea is the first designed piece of that territory, and it needs the multi-user frame to exist before its build can be described: where the identity is read from (git config? the GitHub remote? asked at /setup?), what happens with no GitHub profile, and how it meets the scrub rule that keeps personal names out of committed docs — which currently pushes the same direction by omission rather than by design.
Relates to the lint item and to the close-amending question ("May a close amend an existing work item?"), both from the same multi-person consumer project.

#### Search leg over LOG/, added beneath the recent-lines read and the ladder's lookups [log-retrieve-search-leg]
Raised by you 2026-08-23, mid-run, out of a question about what the memory-system tools do that this one does not. Filed for a later /plan; the design is half-formed and the first step is a measurement rather than a build.

The queue is bounded and complete, and that is the property the retrieve ladder rests on. `LOG/` is neither: it grows without limit, and `LOG/index.md` is read in full on every retrieve, which the always-loaded rules already describe as a fixed toll rather than something a reader skims past. Two legs of retrieval exist today and both are live — the five newest index lines read unprompted at a /plan opening ([plan-reads-recent-log-index]), which gives orientation, and the ladder's targeted lookups, which answer "has this been decided". Neither reaches a finding that is relevant but old, because a targeted lookup needs the word to look for and the recency read only reaches the top of the file.

**Additive, and the item is written this way because the alternative was raised and rejected in the same conversation.** A search must not displace the recent-lines read. Search returns only what someone knew to ask about, so replacing an unprompted orientation read with a query-driven one reintroduces exactly the gap the orientation read was built to close — your objection, and it is the reason this is a third leg rather than a redesign of the ladder.

**Emphatically not over QUEUE.md.** The queue's value is that a session reads all of it, so a sampled read of the queue would trade a complete input for a partial one, which is the property the comparison article spends two paragraphs defending.

**First step is measurement, not a build.** Nobody has measured what `LOG/index.md` actually costs to read at its current length, and this project bans limits it cannot derive — so "the index is too long now" is not yet a claim anyone here can make. Measure the current toll and the growth rate first; the result decides whether a search leg is worth building at all, and a null result closes the item.

**Relates to** [index-line-length-proportional-cap], which bounds what each index line costs, where this asks what the whole file costs. Different questions, and the cap landing does not answer this one.

#### Purpose statement for the method, absent from every consumer project [method-purpose-orientation]
Captured by you 2026-08-23, from writing the comparison article and the ladder announcement in the same session. Your observation: authoring those pieces revealed how badly Claude understands what the method is for, and you were at a loss how to remedy it. Your proposal was skill intros plus a plugin intro in the always-loaded rules; the finding below is Claude's, and it sharpens the diagnosis rather than replacing the proposal.

**Nothing in the shipped package states what the method is for.** Verified at capture time. `CLAUDE-TEMPLATE.md` opens "This project uses the Throughliner method" and goes straight to mechanics. Each skill doc opens with what it does — plan.md "is where unprocessed work becomes processed work", next.md "You are building the cleared work from the queue", done.md "Close the current session", setup.md "You are setting up a project folder". All four are operating instructions. No sentence anywhere says why any of it exists.

**The reason this went unnoticed here is that this project is the exception.** In a consumer project `SPEC.md` describes the consumer's app. The purpose material — intent surviving whatever Claude remembers, the throughline as a reasoning spine, approving as the product rather than overhead — lives in this project's SPEC only because this project's product happens to be Throughliner. Every consumer session runs on procedure with no purpose statement at all.

**Evidence, all from the session that raised it.** A Discord draft that narrated how the ordering ladder was built rather than what a user gets, rejected in your words as "not a useful post about what users can now get out of Throughliner". A concession written into the comparison article that semantic search "will beat anything a structured queue can do", which gave away the queue's defining property — you caught it. A rung described as a bare mechanism until you supplied the reason long entries are served. Each is a session that knew the rules and not the point.

**Why prose is the right mechanism here, against this project's own record.** The recorded class of correctly-worded rules that do not fire are rules asking a session to remember a step; prose is weak at that. This is comprehension rather than compliance, and framing what a thing is for is the one job prose does well. Stated because the gate will otherwise read this as the weak-mechanism pattern it resembles.

**It need not consume a rule slot.** `skill-nonspecific-rules.md` already carries one piece of non-rule orientation — the work-cycle block, marked read-here-not-recited. A purpose statement is the same kind of object and the precedent is set. Whether the admission test for rules applies to orientation at all is a question for the keep-step.

**Recommended shape:** one purpose statement in the always-loaded file, modelled on the work-cycle block, plus a single what-this-is-for line at the top of each of the four skill docs. Start with the always-loaded one — it is the only text every session reads, including chats with no skill running, which is where the problem was noticed.

**The honest limit, and it should be weighed before this is kept.** There is no way to tell whether it worked. Nothing fires when Claude misunderstands the point, which is why every instance above reached you rather than a check. This buys better odds and no guarantee, and it must not be described as fixing comprehension.

#### Walk-through re-did a step already done, because nothing sends a session to the record first [walkthrough-repeats-completed-steps]
Found by Claude 2026-08-23, in the run that hit it. The [competition-comparison-article] walk-through ran step 2 — "Claude drafts the full article" — and drafted a full article from scratch. That step had already been performed the previous day: a draft was written, approved by the user in her own words ("works ok"), and delivered into the site project's mailbox, all recorded in `LOG/2026-08-22-competition-comparison-article.md` and on the `INBOX/sent.md` register. Roughly an hour of drafting and three rounds of the user's editing were spent before the collision surfaced, and it surfaced by accident — only because `INBOX/sent.md` was opened for an unrelated reason.

**The item was legitimately still open, which is what makes this a real hole rather than a stale queue entry.** Its last two steps are the user publishing and confirming, so it correctly survived the previous close. A multi-step `[user]` item can therefore be partly done, and nothing in the walk-through records which steps those were.

**Three mechanisms each looked away, and none of them is at fault alone.** The build view carries no decision history by design, so it could not mention an earlier draft. The item's walkthrough pointed at one artifact to re-read, the research file, and at no record. And the always-loaded retrieve ladder does require checking the record, but it is framed around answering a design question — "why does this exist" — rather than around "has this step already been performed", so a session driving a walkthrough does not recognise itself as being in its scope.

**Candidate directions, none designed.** A walk-through step could check `LOG/` for the item's slug before acting, which is one directory listing and reaches exactly the case that failed here. Or the view could carry, for a `[user]` item, whether any record already exists under its slug — the digest already resolves slugs against LOG filenames, so the machinery exists. Or the walkthrough itself could record progress against its own steps, which is the largest change and the one that actually answers "which steps are done".

**Relates to** [log-record-kind-suffix] (shipped this session), which made a second record for a slug visible to the digest at all — the same attribution machinery any fix here would read.

#### Address book the method describes does not exist in this project's INBOX [inbox-address-book-absent]
Found by Claude 2026-08-23 while sending a message to the site project. SPEC states that a correspondent's folder path is recorded on first use inside `INBOX/`, so continuing a conversation does not make the user retrieve the path again. `INBOX/` here holds `sent.md` and `archive/` and nothing else — there is no address book, and `sent.md` names correspondents in prose ("flintcraft.tech (the site project), its `INBOX/`") without recording any path.

**What happened instead, which is the tell.** The site project's folder was resolved from the Desktop-level `CLAUDE.md`, which happens to name the projects under it. That worked here and is not a general route: it works only because this project sits inside a parent folder whose own doc lists its siblings. A consumer whose correspondent lives anywhere else has nothing to resolve from, so the session would have to ask the user for the path again — the exact thing the record exists to prevent.

**Two readings, and the item should settle which before anything is built.** Either the address book was never implemented and SPEC describes an intention, or it was implemented and this project predates it — a check of the shipped `setup.md` and `feedback-and-inbox.md` for what creates the file answers it. The second reading makes this a migration gap for existing projects rather than a missing feature, and the fix differs accordingly.

**Worth weighing at the keep-step:** whether the sent register should carry the path itself rather than a separate file existing alongside it. `sent.md` already records who was written to, is already inside the gitignored folder for the same privacy reason, and is written at every send — so it is the artifact that already has the habit. Against that, SPEC currently describes two things and merging them is a SPEC change, not just a build.

#### SPEC owes two sentences from the 2026-08-23 build run [spec-owes-close-amend-and-gate-once]
Filed by Claude 2026-08-23 at the build close, per the rule that a build records the sentence SPEC owes and files it rather than writing it — the session that made a choice is not the session that certifies it as product truth. Both are user-visible behaviour changes that shipped this run; SPEC lags them until a planning session writes them.

**From [close-amending-items-boundary].** SPEC's `/done` paragraph describes what the close does in some detail, down to offering once to append post-close work to the record, and says nothing about amending a work item. The behaviour now: at a close, a user-directed amendment to an existing work item is permitted and is recorded in the session record under that item's name; where Claude rather than the user notices a problem with a cleared item, it stays a filing and the close names the collision plainly — this item runs before the next planning session unless you direct the amendment now. The second half is the part that reaches the user, since it puts a decision to them at a moment that previously had none.

**From [end-of-queue-gate-fires-once].** SPEC's processing-flow paragraph states that a planning run never offers to stop while unprocessed work remains, and that the wrap-up question is available only once nothing is left but items set aside. It does not state how often that question may fire. The behaviour now: it is asked once when the queue first comes to rest, and on later returns to rest in the same stretch the session ends plainly with no re-ask, firing again only after further work has emptied the queue again.

**Neither sentence is drafted here deliberately** — drafting it would be the self-certification the rule prevents, one step removed. What is recorded is which paragraph is short of what, and of what.

#### Last session advises processing [walkthrough-repeats-completed-steps] next [forward-advisory]
Advice, not work. It replaces a spent note that advised processing [cycles-due-check-verification], which has already been processed and is sitting cleared.

The reason it is worth going first: three `[user]` items remain cleared to run — the comparison article, the ADHD article and the cycles verification — and the next build run will walk through them. One of those, the comparison article, is the item that produced this finding: a walk-through re-performed a drafting step that had been done the previous day, and nothing in the run could see it. The other two have multi-step walkthroughs of the same shape. So the next run is the one most likely to hit it again, and this capture is what would stop it.

It touches no other unprocessed work, and it names no fix — three candidate directions are recorded on the item and none is designed.

#### Staleness sweep tells a build close to fix pointer drift, and the scope-lock forbids the only way to do it [pointer-drift-unfixable-at-a-build-close]
Found by Claude 2026-08-23 at a build close, by hitting it. `done.md`'s staleness sweep splits its findings by fix path: a fate decision defers to planning, but **pure pointer drift — a file reference whose target content is unchanged — is "mechanical. Fix it HERE, report in one line, riding this commit, with no approval ask."** That instruction cannot be carried out.

**What happened.** This run renamed fifteen session records to their full slugs. Two queue items name one of those records in their prose (`2026-08-22-cycles-build.md`, now `2026-08-22-cycles-definitions-and-due-checks-build.md`) — textbook pointer drift, same content, new name. The edit was refused by `pre_tool_use`, correctly and by design: a build does not edit QUEUE.md directly, and the sanctioned route is `reorder_queue.py`, which moves, deletes and appends **whole entries by slug** and has no way to change text inside one.

**The workaround available is worse than the drift.** Deleting the entry and re-appending it with corrected text would relocate it — one of the two items is held below the readiness line, so it would land at the bottom of the wrong region and lose its position. Nothing about a stale filename justifies that.

**So the sweep's mechanical arm is unreachable from the close it is written for.** It is reachable from a planning close, where the scope-lock permits QUEUE.md — which suggests either the arm belongs only to planning closes, or the queue tool needs a narrow in-entry replace, or the sweep should file drift as a capture from a build close and say so. All three are directions, none is designed.

**Worth checking at the keep-step: how long this has been true.** The instruction reads as though someone expected it to work, so it may predate the shell-write guard or the build's queue-write refusal. The two stale pointers this found are left in place and named here, so whatever is decided has a concrete case to fix.

#### [audit] Compliance audit of the rule changes made since the last one [compliance-audit-lag]
Filed by the audit-lag check in `resources/rule_signals.py`, run at the 2026-08-23 build close because that close staged rule-bearing paths. The check reported one rule-bearing commit since the most recent compliance-audit record (`2026-08-22-post-restyle-compliance-audit-2.md`) that no audit has covered, and it files exactly one capture under its own slug — which nothing in the queue carried.

**Scope is the delta the check printed, not the whole corpus:** `CLAUDE.md`, and under `plugin/throughliner/docs/`, `done.md`, `done-build.md`, `feedback-and-inbox.md`, `migrate-checklist.md`, `next.md`, `plan.md`, `rescan.md`.

**The scope will have grown by the time this runs.** The close that filed it then committed a further rule-bearing change of its own — amendments to `done.md`, `plan.md`, `skill-nonspecific-rules.md` and `CLAUDE.md` from this run's eight built items. Re-run the check when the audit starts and audit what it reports then, rather than the list above, which is a snapshot taken one commit early.

**Criteria are not re-derived here.** `resources/method-compliance-audit-checklist.md` holds the four standing lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history sitting in operative text via the delete-and-read test.

An `[audit]` edits nothing: it reads and reports, and its findings return as ordinary captures.

#### Overwrite guard suggests the retired numeric suffix, not the kind suffix the naming rule now requires [guard-suggests-legacy-record-suffix]
Found by Claude 2026-08-23 at the close that shipped the naming rule, by being handed the wrong suggestion. `pre_tool_use` refuses a write onto an existing session record and names a free filename instead — it offered `2026-08-23-log-record-kind-suffix-2.md`. [log-record-kind-suffix] shipped hours earlier and says the second record for an item carries its **kind** (`-plan` / `-build`), with the numeric form kept only so existing history still reads. The record was written as `-build` against the guard's advice.

**Nothing broke, and that is the concern.** The guard's suggestion is a plain-English filename in a refusal message, so a session that follows it produces a legacy-shaped name that the digest still attributes correctly — the stripper matches `-N` too. The cost is not attribution but drift: a helpful message that quietly recommends the retired convention will reproduce it, and the guard fires at exactly the moment a session is deciding what to call a record.

**Worth deciding at the keep-step whether the guard should know the kind at all.** It can see the filename it refused and the names already taken; it cannot see whether the session writing is a plan or a build, so it could offer both kind forms and let the session pick, or offer the numeric only when both kind names are taken. Offering a suffix it cannot justify is what a smaller fix would avoid — the message could simply say the name is taken and point at the naming rule, leaving the choice where the rule already puts it.

**Relates to** [log-record-kind-suffix], shipped 2026-08-23, whose own record documents this collision as the rule's first live test.

#### [user] Approved Discord post about the comparison article now describes a superseded draft [comparison-article-post-needs-rewrite]
Found by Claude 2026-08-23 while walking the comparison-article item. A Discord post was drafted and approved on 2026-08-22 and has not gone out — it is recorded on `INBOX/sent.md` as approved and not yet posted, with its text verbatim in `LOG/2026-08-22-competition-comparison-article.md`. Its second paragraph announces the article and describes it as closing "on the coherence-over-scale trade", which was true of the 2026-08-22 draft.

That draft is superseded. The 2026-08-23 rewrite names a specific project rather than a category, adds a section on Papi as the nearest comparable tool, and ends on a shipped mechanism instead of a general trade-off — roughly 1,400 words against 900. A hold-note has already gone to the site project asking that the old one not be published.

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, is unaffected and still true. Only the second needs rewriting, and it needs rewriting after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. You post it, with the live article URL pasted in — Claude has no route to Discord. 5. You confirm, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Ordering, written here rather than as a field:** this follows [competition-comparison-article] and cannot be worked before it, because the rewrite has to be against the final article. A capture carries no `Blocked by:` — that field belongs to the held region — so the relationship lives in prose, and the same sentence belongs on the article item if it is not already there.

