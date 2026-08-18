# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Compress the log index's over-ceiling lines, cutting the retrieve's fixed toll by about 40% [split-action-defeats-the-bands-in-aggregate]
**Subject replaced at processing 2026-08-17; the slug is unchanged because slugs are immutable.** Raised by you at the close that first applied the plan-entry split: *"That was almost 17k tokens. I am concerned that the bands won't reach this new record keeping model."*

**The aggregate half was measured and refuted, and that finding is in this session's record rather than here.** Per-entry cost *fell* after the split — 518 words per entry before it, then 329 and 316, against July's own 341. The 17k came from recording 26 items, so a per-close band would measure run size, which is your decision and not a length defect.

**What survives is the index toll, larger than the item claimed.** `LOG/index.md` is 817 lines and 48,165 words, read in full on every retrieve. 351 lines sit at or above 61 words — over the ceiling — and carry 32,408 of those words. 265 of the 351 are August's.

**What changes.** Each of the 351 is rewritten to the artifact touched, the nature of the change and the entry filename, inside the 20–40 band, working from the line's own text only: an over-ceiling line is over because it restates the entry it points at, so no entry needs re-reading. Commit hashes are preserved — the digest and the hash backfill read them.

**This edits a pointer, not the record.** Every entry file stays byte-for-byte and no claim changes, which is what separates it from editing a session record to agree with a later decision.

**The intuitive fix was refused: monthly index files.** Four mechanical readers would each have to glob a directory, and the digest must resolve a slug from any month, so it would read all of them regardless — a format change, an epoch bump and a migration path for a smaller saving.

**Acceptance test:** line count, total words and median line before and after; expect roughly 28,000 words.

**Files:** `LOG/index.md` only. The ripple was traced by grep — `session_start.py`, `queue_digest.py`, `rule_signals.py` and `measure_written_shape_length.py` all read the file, none reads line length.

Rule gate: not needed — no rule authored and no always-loaded text touched. This applies the existing index-line band to a backlog that mostly predates it.

**The measurement this item asked for was run 2026-08-18, and it moves the subject: the problem is the queue's TOTAL length, of which item length is one term.** Across one full planning session the file went **21,512 words to 24,771 — up 15% — with the item count unchanged at 58**, and words per item rising 370 to 427. Twelve items were processed, four deleted and three folded away, and it still grew, because **processing an item is what lengthens it**: every keep adds a settlement, a Files line and a gate disposition. Only building an item out or deleting it shrinks the file. **This is the user's framing and it supersedes the per-artifact one this item was filed under.**

**So a wording pass is not the lever, which is measured rather than argued.** Two tersify passes over this queue yielded 8% and 3%, and their own write-up concludes the file is not verbose — its length is accumulated decision history. A tightening pass over seventeen freshly authored entries the same day cut 9%, 8,343 words to 7,585, leaving fifteen still over ceiling. Both passes removed meta-commentary and barely moved the totals.

**And the ceiling those passes were measured against is derived from a shape that no longer exists.** 45 of 54 entries breach it, the worst at 1,347, 1,102 and 805 words — corpus-wide rather than one session's authoring, so **an earlier claim on this item that the over-length was newly written text is withdrawn as false.** The band is July's median; dispositions moved onto the item on 2026-08-13, and the ripple-trace and SPEC-question limbs on 2026-08-17. A July item carried none of them. Re-derived figures without multipliers are in [word-band-script-does-not-ship]'s discussion.

**One narrower finding survives intact.** The breach action "split into two items" worked where an entry genuinely held two pieces of work and failed where it held one clause plus a long narrative — there the remedy was relocating the narrative to the record and citing it, 558 to 407 and 571 to 442, reaching the ceiling in neither case. **The action needs a second limb: for a one-clause item, relocation rather than division.**

**The accretion mechanism is now filed separately** as [folding-in-has-no-eviction-step] — folding content into an item requires naming nothing that comes out, and appends rather than merges.

Relates to [bands-fire-on-the-median-artifact], [plan-entry-split-action-underspecified] and [index-line-length-is-a-toll-on-every-retrieve].

#### Planning writes the SPEC sentence ahead of the build, and a build that finds one missing files it rather than writing it [missed-spec-write-interrupts-the-run]
Raised by you 2026-08-17 when a run stopped in its second minute to ask for one SPEC sentence. **Subject settled at processing the same day; the slug is unchanged because slugs are immutable.**

**Your principle, which is the whole of this and which Claude missed twice before you stated it.** SPEC is managed across a session boundary so that no one instance of Claude is both the party that made a choice and the party that certifies it in product truth. Claude proposed deferring the write to that same run's close; you refused it on exactly that ground — the close is the same session, so it moves the self-certification later rather than crossing anything.

**Already settled one layer over:** `CLAUDE.md` says a disposition written as an item is built "improves attribution and restores no power to refuse," and that only /plan can refuse. [build-wrote-its-own-gate-disposition] is that failure in this queue.

**What changes, in three steps.** The keep-step asks whether an item changes what SPEC says, and **planning writes the sentence then**, with the user present. The build then builds against it and never touches SPEC. Only where planning missed one does the build record the sentence, file it as work, and leave SPEC alone for the next planning session.

**So SPEC leads the build rather than trailing it**, which is what "read at build time" requires. The cost, stated: on a miss, SPEC lags that sentence by one planning session. It is a queue item rather than silence, and the keep-step question is what makes the miss rare.

**Folded in from [batch-spec-writes-at-the-end-of-a-run], deleted at processing:** deferring SPEC writes inside a run was tried live on your instruction — four sentences held in the working file, written in one pass, nothing lost and the run never stopped again. That is the evidence the file-it fallback is safe. The rest of that item dissolved, because under this model a run owes no SPEC sentences.

**Files:** `plugin/throughliner/docs-b/plan.md` (the keep-step question, and the two-other-routes paragraph loses the build-asks route), `next-build.md` (the scope-grow SPEC ask and step 4's establishes-new-product-truth branch, both replaced by the file-it path), `done-build.md`, `CLAUDE.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`, `faq-template.md` plus `FAQ/faq.md` and both index lines for the entry. `SPEC.md` is **not** listed — its sentence was rewritten in this planning session, which is the rule applied to itself. The eight sites were traced by grep before this list was written.

**The SPEC-contradiction halt is untouched and must not be softened** — built work conflicting with SPEC still stops the run and names the sentence.

Rule gate: run — admitted as a clause on plan.md's existing two-limb keep check, not a freestanding rule, so no always-loaded slot is spent. **The eviction is the build-asks route, repealed outright across seven live files.** Failure evidence is one recorded instance, which is thin for a new rule and is what the amendment-plus-eviction shape carries; the same defect is independently recorded for dispositions in [build-wrote-its-own-gate-disposition].

Relates to [stated-open-design-question-passes-the-keep-step], the same shape one step over.

#### An outgoing record: one index of everything that leaves this project, carrying destination, intent and what was claimed [send-record-lacks-destination-and-intent]
**Widened at processing 2026-08-17 to absorb [inbox-has-no-outgoing-record] and [shipped-change-falsifies-a-past-post], both deleted once their content landed here; the slug is unchanged because slugs are immutable.** Raised by you while asking whether an article had been passed to another project — checked rather than assumed, and the LOG entry said only *"she approved the exact text before it was sent"*. **The design is Claude's, deferred to in your words: "as you recommend."**

**Your rule, in your own framing.** A send may clear a work item where it hands that item to another project **for completion**. Where it defers only **continuation**, the item stays and a later capture wakes it.

**Three absences with one cause.** No destination or intent on a send; no sent copy in the mailbox, whose archive holds twenty-two inbound messages and nothing outbound; and no record of what was announced, so a shipped change falsifies a past post unnoticed — the instance being your spec-driven-development post, inverted by [missed-spec-write-interrupts-the-run] in the same conversation.

**What changes.** `INBOX/sent.md` gains one line per outbound artifact — mail, feedback report, GitHub issue, Discord post, delivered draft — carrying the date, the destination, the intent, what was claimed in one clause, and a pointer to the text that already exists. Written in the same turn as the approved send, because the text exists then and nothing later reconstructs it. No second copy of anything; the same shape as `LOG/index.md`.

**Why inside `INBOX/`.** That folder is gitignored on every path and these lines name correspondent projects, which is the reason the address book lives there too. The cost: not version-controlled, so it can be lost, exactly as the address book can.

**Not built here — the check that reads it.** An item repealing shipped behaviour greps this file for the claim. That is a limb of [repeal-has-no-ripple-trace], which needs this file first; the ordering is written into both.

**Files:** `plugin/throughliner/docs-b/feedback-and-inbox.md` (the send flow writes the line, and the clearing rule), `CLAUDE.md` (the Discord section, host-only), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is not listed — written in this planning session.

**The live inconsistency this exposed.** [competition-comparison-article] sits cleared to run while its draft is in another project being polished; its fate turns on which intent that send carried.

Rule gate: run — the record obligation is a clause on the existing approved-send flow in a fetched doc, so no always-loaded slot is spent, and your clearing rule gains operative wording for the first time. Nothing evicted. Failure evidence is three recorded instances.

#### Widen /rescan to append post-close work to the session's record, so a tail needs one word instead of a paragraph [rescan-appends-post-close-work]
**Captured by you 2026-08-17**, immediately after [done-delta-close] was deleted — and it is not that item. Your framing: a skill so you don't have to type the whole request and the reasoning behind it every time; it picks up the post-close work, logs it, and it rides the next commit.

**What exists, and what doesn't.** `/rescan` is already user-invoked, repeatable within a chat, scans back only as far as the last `/rescan`, files to Unprocessed and commits nothing. What it does not do is touch the session's LOG entry: `rescan.md` names `LOG/` once, and only to place a capture. So a conversation's *decisions* have a one-word route and post-close *work* has none.

**Why this survives the refusal that killed [done-delta-close].** That refusal was against a second commit wearing another name, and against needing someone to judge when the tail had ended. Neither applies here — this commits nothing, and it can be run as many times as the tail has parts.

**What changes.** `/rescan` routes what it finds by the three-way triage the always-loaded rules already carry, rather than filing captures only: work to do becomes a capture, what happened becomes an append to this session's LOG entry as a marked tail. Its stated boundary is untouched — it files, and never decides a fate or builds.

**Files:** `plugin/throughliner/docs-b/rescan.md` (the routing), `done.md` (its tail section names `/rescan` as the route), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is not listed — its `/rescan` bullet is rewritten in this planning session.

Rule gate: run — a widening of one skill's own routing to the triage it already sits inside, so no always-loaded slot and no freestanding rule. **Nothing is evicted, and that is stated rather than dressed up.** Evidence is your report that post-close work happens a lot, plus this session's own opening: the previous session's tail was correctly recorded, but only because it was asked for in prose.

#### A run can be presented whose top item is already void because /setup is outstanding [next-presents-items-setup-will-overtake]
Filed 2026-08-15 from INBOX mail sent by a consumer project running this method, which flagged it as the less clear-cut of their two findings and possibly working as designed.

**What happened.** Their project's recorded plugin version was behind the installed one, so session_start correctly said /setup wanted a session of its own. /next then presented a run as normal. Its top item was a fix to a stale description inside CLAUDE.md's plugin-managed block — exactly what /setup rewrites, from a template already carrying the correct text. The item was void before the run began, and the run had to be closed with nothing built to free /setup.

**Nothing malfunctioned, which is why it is a design question rather than a bug.** Each part did its job. But session_start already knows the project is behind, and /next's pre-flight has no branch that says so when presenting a run.

**Kept 2026-08-17 on your decision, and your reason is that it is live here rather than hypothetical** — [setup-outstanding-here] is sitting in the cleared region now.

**Their fix is narrowed rather than adopted, answering the cry-wolf objection they raised themselves.** The branch fires only where an item in *this* run names a file /setup rewrites — a read of that item's Files line, not a judgment about plugin-managed content.

**And it reuses an existing mechanism.** `next.md` already carries a drop-an-item-from-this-run recommendation for waiting mail, stated as **the one thing** that may drop an item from a run. This becomes its second trigger: /next recommends dropping the affected item from that run alone and never decides its fate.

**One recorded objection is dead** — that pointing a user at /setup would send them into a denial. [scope-lock-blocks-setup] shipped 2026-08-15 in `0e62afe`. No hook change either: session_start already emits the outstanding-setup fact, as it did at this session's opening.

**Files:** `plugin/throughliner/docs-b/next.md` (the present-the-run beat, and the "one thing" sentence), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is not listed — its sentence is rewritten in this planning session.

Rule gate: run — admitted as a second trigger on next.md's existing drop-from-this-run mechanism, so no new mechanism and no always-loaded slot spent. **The eviction is that sentence's "the one thing" claim**, which becomes false and is rewritten rather than left standing. Failure evidence is two instances: the reporting project's void run, and this project sitting in the same state today.

#### Work that finishes in another project has no way to tell this one, so an item can sit ready long after it is done [cross-project-work-completes-invisibly]
Filed 2026-08-10 during a /next walk-through, at your instruction. Mixed authorship: you raised the question that found it — why the site was being edited from here when it belongs to another project — and the diagnosis is Claude's. Rides this session's commit.
**What happened.** [report-url-404] was a `[user]` line waiting on a page existing at flintcraft.tech/report, work on a different project. The page had been up for some time. Nothing here learned that, and the item sat in the cleared region as ready work until a /next walk-through fetched the URL and found it live.
**No harm this time, and that is not the point.** The item recorded an observable check, so the walk-through ran the check instead of asking whether the work was done — the check-the-world rule working as designed. The cost was one wasted run slot and a moment of reasonable confusion about whether Claude was reaching into another project.
**The general shape.** Any item whose completion happens outside this repo is invisible here until someone looks. An observable check rescues cases where "done" leaves a trace a fetch or file test can find. It rescues nothing where completion is visible only to the user or inside another project's records — the larger class.
**Settled 2026-08-17: observable checks are as far as this goes, and the docs say so.** The notification branch is refused on [inbox-delivery-unconfirmed]'s own finding — mail is fire-and-forget both ways, so a notice nobody must read moves the problem rather than closing it.

**The checking side already works and the defect is upstream of it.** The walk-through rule already checks the world where an item names an observable result, which is what rescued [report-url-404]. Nothing requires an item to *carry* one when one exists.

**What changes.** At the keep-step, an item whose completion happens outside this project **names what would show it done** — a URL, a file, a branch — or states plainly that nothing observable exists. The second half carries as much as the first: it is what tells a later run to ask rather than check, instead of leaving it to guess. Where nothing is observable the item waits until the user mentions it, now stated rather than looking like an oversight.

**No FAQ entry:** this changes what a queue item carries, not anything the user does.

**Files:** `plugin/throughliner/docs-b/plan.md` (the keep-step clause) and `feedback-and-inbox.md` (that work finishing elsewhere is never learned by notification). `SPEC.md` is not listed — its sentence is rewritten in this planning session.

Rule gate: run — admitted as an amendment to the existing check-the-world clause, sited at the keep-step where the item is authored rather than restated where it is read; no always-loaded slot and no freestanding rule. **Nothing is evicted, stated plainly.** Failure evidence is one instance, [report-url-404], which is thin and carried by the amendment shape rather than by weight of cases.
Relates to [inbox-delivery-unconfirmed], [inbox-mail-has-no-place-in-the-ladder] and [report-url-404] (the instance).

#### Report in the digest how many cleared items sit ahead of a `Runs alone` item [runs-alone-at-the-end-can-be-starved]
Filed 2026-08-13 by Claude, from your question about why the rename hadn't happened. **Subject replaced at processing 2026-08-17; the slug is unchanged because slugs are immutable. The design is Claude's, deferred to in your words: "as you recommend."**

**The starvation reading is refuted, and this is recorded rather than quietly dropped.** The item was filed about [rename-to-throughliner] receding; that shipped on 2026-08-13, three days later. And a `Runs alone` item is not deferred indefinitely by work sitting ahead of it — /next stops **before** it, so the following run reaches it. Genuine starvation needs planning to outpace building forever, which is a throughput problem rather than a placement one.

**What survives is visibility.** This session placed six items ahead of the `docs-b` rename and the queue gave no sign of it. It was said out loud only because Claude happened to notice, which is the siteless-check failure this project has recorded five times.

**Which is why the item's own third option is refused.** It floats /plan narrating the placement — and that is exactly what happened today, unprompted and therefore unrepeatable. A fresh short session, which this method designs for, would not notice.

**What changes.** `queue_digest.py` prints one more computed line: for each `Runs alone` item, how many cleared items sit ahead of it. A fact, like every other digest line, never a verdict — and read at /plan's opening alongside the held-work lines. No threshold, no age, no judgment, so nothing here needs a derivation.

**The two obvious fixes stay refused, with their reasons.** Placing such work first stops every run at the top. Reporting how long an item has been *cleared* needs an invented age threshold, which this project bans.

**No FAQ entry:** this changes what a planning opening reports, not anything the user does.

**Files:** `plugin/throughliner/scripts/queue_digest.py` (the computed line), `resources/testing/test_queue_digest.py` (a case for it), `plugin/throughliner/docs-b/plan.md` (the opening read). `SPEC.md` is not listed — its digest paragraph is rewritten in this planning session.

Rule gate: run — no rule is authored. **The disposition is that a mechanical check replaces a prose rule**, which is this project's own stated test for retiring a noticing, and the eviction is the narration fix this item proposed, refused on the record above rather than shipped alongside.

Relates to [digest-reports-computed-fields-not-summaries] and [held-items-invisible-during-normal-use].

#### A user-named subset of items, once processed, has no stated shape — so the session reaches for the empty-queue gate and leans toward stopping [subset-done-has-no-stated-shape]
Filed 2026-08-13 by Claude from a live instance in this /plan session, caught by you. Filed after the last committed close, so it belongs to no committed session record.
**What happened.** You named three items at the opening. When the third was processed, Unprocessed still held 35 items, and the session offered "anything else to capture or discuss, or shall we close out?" — `plan.md`'s **neutral end-of-queue gate**, specified for the case where Unprocessed *empties*. You had to ask why continuing wasn't offered.
**The gap, a missing case rather than a misread one.** `plan.md` states the four routes once at the start of processing and specifies the end-of-queue gate for an empty queue. Between those sits an unhandled state: a user-named subset exhausted while the queue is not. Nothing says what the session does there, so the nearest gate gets reached for — and it names closing.
**Why that substitution is worse than a neutral miss.** The end-of-queue gate is carefully worded not to lean toward closing *given an empty queue*. Applied to a full one it stops being neutral: it silently reclassifies 35 unprocessed items as nothing left to do. The same failure the checkpoint recital was stripped back for.
**Settled 2026-08-17, and smaller than either option the item offered.** Neither a new branch nor a new state is needed, because **what to do next is already specified**: plan.md's checkpoint says that after every item you present the next item. Nothing was missing about the behaviour. What was missing is that the session took a subset the user *named* to be the length of the session.

**So two clauses on statements that already exist.** The neutral end-of-queue gate gains its precondition — it may fire only where Unprocessed holds nothing but items skipped this session — and the ordering ask at the opening gains one clause: **a subset the user names sets the order, not the session's length**, so when it is exhausted the checkpoint carries on with the next item. With the gate unavailable, the only thing left to reach for is the checkpoint, which is the correct behaviour.

**Third instance of one family**, with [close-invites-same-session-next] and [plan-gates-say-close-out-for-a-retired-phase], both shipped — a close offered where continuing was better.

**No FAQ entry:** the user still answers one question there; only which question changes.

**Files:** `plugin/throughliner/docs-b/plan.md` — the neutral end-of-queue gate and beat 2's ordering ask. `SPEC.md` is not listed: its processing-flow paragraph gains the matching sentence in this planning session, alongside the promise it already carries that the close never invites another build.

Rule gate: run — both clauses are admitted as conditions on existing statements rather than freestanding rules, so no always-loaded slot is spent. **Nothing is evicted**, stated plainly. Failure evidence is three recorded instances of the same family.

#### Give the provenance rule the containment test, so a one-word agreement stops reading as authorship [chip-replies-are-indistinguishable-from-user-authorship]
**Captured by you 2026-08-13; split at processing 2026-08-17.** The finding is now `resources/research/chip-replies-and-provenance-evidence.md`, cited here rather than restated: this entry stood at 656 words against a 345-word ceiling, and most of it was evidence rather than work. Your objection is what produced it, in your own words: *"those are ALL chip answers, i don't write like that."*

**What changes.** The always-loaded provenance rule already says approval is not authorship, and that agreeing to a proposal Claude reasoned out makes the reasoning Claude's. What it does not give is any way to tell agreement from authorship when the reply is one word. It gains that as a subordinate clause: **a reply wholly contained in Claude's preceding message cannot evidence an origin claim.**

**The bulk audit is refused, and so is a bulk disclaimer.** The test needs the message that preceded each credit, which is not recoverable item by item — and the research file records that the transcript cannot answer authorship in any case. Declaring existing credits unreliable in bulk would be an unverifiable claim about the record that degrades every honest credit alongside the doubtful ones. Specific credits are checked when challenged, which has already happened once.

**A wrongly-credited decision is re-labelled, not re-decided — except where the credit is what kept it from being examined.** `Runs alone` is the instance both ways: its authorship was wrong, and its stated justification was independently tested and refuted on 2026-08-14.

**The FAQ is where the "as you recommend" convention lands**, answering "why wasn't I credited with that decision?" for anyone who asks — without the once-per-session notice you refused as "a bit much", which would have fired at every user including those who never touch the chips.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the provenance rule's approval-is-not-authorship limb), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is not listed — it says nothing about credits, and how a record is authored is not product truth.

Rule gate: run — admitted as a subordinate clause on an existing always-loaded rule, so no slot is spent and nothing freestanding is added. **Nothing is evicted.** Failure evidence is a wrong credit asserted twice inside one exchange, plus the shipped rule proving unapplicable without a discriminator.

Relates to [invented-rationale-compounds-past-the-shipped-rule], which this makes structural rather than a discipline problem, and to [message-ending-drives-the-suggestion-chip].

#### Claude tried to run /done itself, and then explained the failure with a rule that was not the reason [claude-cannot-invoke-its-own-skills]
**Captured by you 2026-08-17** from a screenshot of another project running this method, at the end of a planning session.

**What happened, in order.** Claude wrote "Now closing the session", attempted `/throughliner:done`, and the app answered **"Failed to run skill"** in red. Claude then said: *"I can't run the close myself — it's reserved for you to invoke."*

**All five skills carry `disable-model-invocation: true`, whose documented meaning is that Claude cannot auto-invoke them and only the user can** — the flag for work with side effects or user-controlled timing, which a close is. **So the second defect recorded here is withdrawn: the explanation was the mechanical cause, not a true-sounding rule standing in for one.** The withdrawal stays on the item because the wrong reading is the intuitive one.

**One defect survives.** The plugin ships that flag and no procedure doc says so, so a session attempts the invocation and shows the user a red failure mid-close, where a non-coder has least context.

**What changes.** The always-loaded communication rule already says to run every command you can run yourself, handing one over only in the cases the rules name. It gains one named case: **the method's own skills — name the command and hand it over, never attempt it.**

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, that rule's hand-over cases. Not `SPEC.md`, which already says the close is the user's to run.

Rule gate: run — a named case added to an existing always-loaded rule, subordinate rather than freestanding, so no slot is spent and nothing is evicted. Failure evidence is one instance, which is thin and admitted as such; what carries it is that the failure is visible to the user and the fix is three words of an existing sentence.

#### Repealing a shipped clause has no ripple-trace rule, so an unattended run stops to ask [repeal-has-no-ripple-trace]
Filed 2026-08-16 by Claude, from a failure observed twice in one run rather than reasoned about.

**What happened.** [spec-control-model-not-what-happens] repealed one sentence from the always-loaded rules and its Files line named that one file, stating in its own prose that "the defect is in the always-loaded rules, not in SPEC." The repealed clause was in fact restated verbatim in three more live places — `SPEC.md`, the shipped FAQ template, and the FAQ copy. The run therefore stopped twice to grow scope, in a run whose whole premise is that it does not stop.

**The existing rule does not reach it.** `CLAUDE.md` requires a grep-traced ripple when an item changes a format or enum the hooks enforce; a repealed sentence is neither, though the trace is identical and just as mechanical. **And it needs no judgment: a repealed sentence is a literal string, so the item either grepped for it or did not.**

**Settled 2026-08-17: a third limb on the keep-step's two-limb check, in the shipped doc rather than in this project's own file.** Where an item repeals or rewords a specific sentence or value, **grep its distinctive words across the project before writing the Files line.** That is where the omission happens, and a consumer repealing a sentence in their own SPEC has the identical problem — so a host-only rule would miss everyone the method ships to.

**The existing host-only rule is subordinated to it rather than left beside it.** `CLAUDE.md`'s hook-enforced-format rule traces the same ripple for a narrower trigger and adds one requirement of its own, that the grep name the enforcing hook; it now declares itself a specialisation of the shipped limb. **Two rules on one subject, at the same level, with no declared relationship is the exact signature folded into [law-prose-restyle-heavy-docs] this session** — leaving them as peers would author the defect that pass is being sent to find.

**Files:** `plugin/throughliner/docs-b/plan.md` (the third limb) and `CLAUDE.md` (the existing rule declaring the relationship). `SPEC.md` is not listed: it describes no part of the keep check, and how a Files line is derived is not product truth.

Rule gate: run — a third limb on an existing check, subordinate rather than freestanding, so no always-loaded slot. **The eviction is the standalone status of `CLAUDE.md`'s ripple-trace rule**, which stops being a peer. Failure evidence is three instances: the repeal that stopped one run twice, and this session's seven-file repeal caught only because the grep was run by hand with nothing requiring it. Relates to [fix-level-has-no-site], which asks the same question about levels.

**Split at processing 2026-08-17 at 542 words against a 345 ceiling.** The announcement surface — a repeal falsifying an already-posted claim — is now [repeal-falsifies-a-posted-claim], held below the line because it cannot be built until there is a record of what was sent. This item covers live documents only, and is buildable now.

#### A build verified its own hook change against the installed host and destroyed a committed record doing it [live-testing-a-hook-change-hits-the-old-host]
Filed 2026-08-17 by Claude at its own close, from a data-destroying mistake it made minutes earlier and recovered from git.

**What happened, in one line; the full account is in `LOG/2026-08-17-chat-2.md`** and is cited rather than restated here, because this entry stood at 558 words against a 345 ceiling and all of the excess was narrative. Having just built the guard that refuses a Write onto an existing file under `LOG/`, the run deliberately performed that write to watch the guard refuse it — and overwrote a committed entry, recovered whole with `git checkout HEAD --`.

**The one distinction the fix turns on.** Every existing statement of host-versus-target asks whether a change is *live*. This is a session choosing to **exercise** the change to confirm it, which turns passive staleness into an active write against the old, unguarded behaviour.

**Settled 2026-08-17, and it has a parent already in place.** `CLAUDE.md` requires a close whose staged paths include `plugin/throughliner/hooks/` to run the suites under `resources/testing/`, as plain scripts. That rule already says how a hook change is verified, so this is a clause on it rather than anything new: **verify a hook change by driving the new code directly — the suites, or `py` against the target file, which this run did successfully three times.**

The unsafe form is named as its consequence rather than as a prohibition: performing the guarded action in the live project exercises the **installed host**, which is the old code, so the guard never fires and the action completes for real.

**Files:** `CLAUDE.md` — the hook-suite close gate. Nothing shipped: consumers never author hooks.

Rule gate: run — a clause on the existing hook-suite rule, subordinate rather than freestanding, though it does cost a slot in this project's always-loaded file. Nothing evicted. **A hook was considered and refused:** a write made to watch a guard refuse it is byte-for-byte a write meant to succeed, so nothing mechanical can separate them — which is also why the safe test and the destructive one look identical from the inside. Failure evidence is one instance, carried by its cost: a committed session record destroyed, and the destroyed entry's own text had predicted it, was read during that run, and the mistake followed anyway.

Relates to [log-entry-write-can-clobber-an-existing-entry], which is the guard, and whose own record predicted this.

#### Decouple the test-suffix clean from the push, now that a rezip happens at every run [decouple-test-suffix-from-the-push]
**Raised by you 2026-08-17 at the close, in your own words:** *"I'm trying to decouple the concept of test rezip from push because I am just rezipping so much."*

**Two things checked before filing rather than assumed, and the full account is in `LOG/2026-08-17-rezip-bump-collides-after-a-push-2.md`.** The clean is not a leftover from when push and release were one event — it was *added* when they were decoupled on 2026-08-04, to close the window the new ordering opened. And stripping at the release was refused that same day, on the ground that a `-testN` would then sit on the public remote between releases, as `1.16.0-test4` once did. **What is new is frequency:** that refusal reasoned about occasional rezips, and you now rezip at every run.

**Settled by you 2026-08-17: just untidy. The clean moves to the release.** That reverses the refusal recorded in [rezip-bump-collides-after-a-push] earlier the same day, and legitimately rather than arbitrarily: **that refusal rested on the suffix being harmful, and the owner of the repository says it is not.** The premise is removed, not the reasoning overruled. So a committed `plugin.json` carries `-testN` between releases, and the release bump strips it.

**What changes.** `CLAUDE.md`'s Push section loses its first step and the two paragraphs justifying it, and its clause about recognising a `-testN` diff at a close is reworded — the file is no longer dirty-then-cleaned, it is committed as it stands. `resources/release-ritual.md` gains the strip at the release bump, stated as stripping any suffix rather than assuming none is present.

**One interaction, already favourable.** The content stamp drops the version key, settled today in [push-clean-breaks-the-content-stamp], so committing a suffixed version cannot report a stale host.

**Files, derived by grepping the suffix across the repository rather than from this discussion — which is what reached the third one.** `CLAUDE.md` (the Push section and the close's diff-recognition clause), `resources/release-ritual.md` (the strip), and `plugin/throughliner/hooks/session_start.py`, whose comment explains the stamp's version exclusion with *"the rezip sets a `-testN` suffix, the push resets it"* and becomes false. `pre_tool_use.py`'s rezip write-permission and its matching test comment describe the rezip's own write and are unaffected — read, not assumed. Host-only throughout: consumers neither rezip nor release.

Rule gate: run — **the disposition is an eviction**, the push's version-clean step repealed outright with the two paragraphs defending it; no rule authored, and the release ritual gains a step rather than a rule. Failure evidence is the frequency change you named, plus this project getting it wrong at the last close.

Relates to [rezip-bump-collides-after-a-push] and [push-clean-breaks-the-content-stamp], both shipped today from the same coupling.

#### The always-loaded rules tell every consumer to run a measurement script that does not ship [word-band-script-does-not-ship]
Filed 2026-08-18 from INBOX mail sent by a consumer project running this method. **Verified here before filing:** `resources/measure_written_shape_length.py` exists in this project only, a `find` over `plugin/throughliner/` returns nothing, and line 711 of the shipped `skill-nonspecific-rules.md` says to run it. Every consumer is directed at a path their project does not have.

**Worse than a broken pointer.** That same section presents its figures as "demonstrated to be sufficient, never ideal" and a limit as "traceable and revisable rather than correct". The script is the only affordance for checking or re-deriving them, so without it the figures are precisely what the rules promise they are not.

**The second half is transfer, and nothing qualifies it.** The medians are this project's July medians, and this project writes method documentation. The sender's writes something else, where a work item carries commercial reasoning and a decision trail instead of a rule. Both corroborating samples come from this corpus, so they establish stability within it and say nothing about generalising.

**A third instance of the split-action defect, from outside this project.** Their item reached roughly 740 words with every individual addition in band, and splitting would have cut one coherent design in half with both halves naming the same file. They declined it. See [split-action-defeats-the-bands-in-aggregate], which recorded two instances here on 2026-08-17.

**Settled 2026-08-18. The script ships**, moving to `plugin/throughliner/scripts/` beside the other two, its "host-only dev artifact" docstring line repealed, and the shipped rule's pointer changed to the plugin-root form. Two build details from the scripting constraints: it carries one `reconfigure` call where `reorder_queue.py` has two, and its `subprocess` git read needs `encoding="utf-8"` confirmed.

**Their suggestion that shipping settles the transfer question is refused, and the script's own docstring is why:** *"this corpus is the bloated one, so its typical length is not a target"*, and the two modes stay separate because *"a band printed inside the distribution report would be a threshold read off the thing being questioned."* A project measuring its own corpus learns its distribution, not a defensible band. **So self-derivation per project is refused explicitly**, and transfer gets one clause instead: the figures are this corpus's, offered as a starting point, and a project writing something different should expect them to fit less well.

**The figures are re-derived, with no multiplier anywhere — the user's instruction.** The old floor and ceiling were the median times 0.5 and 1.5, both invented. The regime boundary is the docset change, not the calendar: **before 2026-08-02 is docset A on Opus 4.8, after is docset B on the 5-series.** Floor, middle and ceiling are now each read off the two regimes' own distributions and split down the middle:

- **captures** — 114 / 261 / **540**, replacing 90 / 177 / 265
- **build records** — 191 / 356 / **571**, replacing 115 / 229 / 345

**The live test is what carries it.** Against the queue as it stands, the shipped ceilings fire on 88% of captures and 73% of work items; the new ones fire on 12% and 19%. A ceiling that fires on nearly everything cannot separate a bloated corpus from a band set too tight, which the always-loaded rule already says of itself.

**Two shapes are NOT re-derived and keep their current numbers.** Planning records, because the docset B side is 42 entries with a tail starting at 1,834 words — too few samples and too extreme. And index lines, unmeasured because the script needs different handling for them. **Work items cannot be cut this way at all**: an item filed in July and enriched through August belongs to neither regime, which is [work-items-accrete-past-their-band] read as a measurement problem.

**And the shift supports the model hypothesis over the discipline one.** Captures and build records both moved by roughly 1.9× across the boundary. A discipline collapse would be patchy; a uniform shift across independent shapes looks like the writer changed. Recorded as support, not proof.

**Files:** `resources/measure_written_shape_length.py` moved to `plugin/throughliner/scripts/`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the two bands, the pointer, the transfer clause), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` describes the bands and their derivation and is rewritten in this planning session.

Rule gate: run — no new rule; two figures replaced and one clause added to the existing authoring standard, with the invented multipliers evicted. **The eviction is the 0.5 and 1.5 multipliers**, replaced by measurements. Failure evidence is a consumer report plus 88% and 73% breach rates measured here.

**They also report the growth-by-addition trap working as designed** — the rules already carried the proposal to exempt later additions and the reasoning against it, which resolved that conversation in one exchange.

#### Teach the measurement script the regime cut, and measure the three shapes still on invented figures [measurement-audits-for-the-remaining-shapes]
**Filed 2026-08-18 on your instruction** — "we need to plan the audits that measure" — after two shapes were re-derived and three were left on numbers nobody can defend.

**What is unmeasured, and why each resisted.** Planning records: the docset B side is 42 entries with a tail starting at 1,834 words, too few and too extreme to derive from. Index lines: the script returns them in a shape the regime cut could not consume, so they were never cut at all. Work items: an item filed under one docset and enriched under the next belongs to neither, so the cut is not merely missing but ill-defined.

**What changes.** The script gains the regime cut as a mode — a boundary date rather than calendar months, defaulting to 2026-08-02 — reporting each shape's floor, middle and ceiling as the midpoint of the two regimes' 10th, 50th and 90th percentiles, which is how the two adopted figures were produced. It also gains index lines, which today it can only report by month. **For work items it reports the ambiguity rather than a figure**: how many items span the boundary, so the size of the ill-defined group is known instead of assumed.

**What it does not do.** It cannot say the resulting figures are right. It replaces invented multipliers with measurements of what was written, which is a different and smaller claim — the two readings the always-loaded rule names both stay open.

**Files:** `plugin/throughliner/scripts/measure_written_shape_length.py` after [word-band-script-does-not-ship] moves it there, and `resources/testing/` for a case on the regime cut. Follows that item; the ordering is written into both.

Rule gate: run — no rule authored; a tool gains a mode. **Nothing evicted.** Failure evidence is three shapes currently carrying figures with no derivation.

#### Tersification runs on request, never at the close, with the procedure on the shelf [tersify-on-request-not-at-the-close]
**Raised by you 2026-08-18** as a step at the close, and **filed against that placement on the evidence you then supplied.** The write-up of the two passes is at `resources/research/tersifying-the-queue.md`, reproduced verbatim.

**Why not at the close.** Its measured yield was 8% then 3%, and its own conclusion is that the queue is not verbose — the length is accumulated decision history. Against that, a close already carrying the session's heaviest work would take on a whole-file read and rewrite. **And its two failure modes are the kind that must not run unattended:** a silent duplication of fifteen items that reading could not see, and a probable upgrade of a paraphrase into a quotation claim — one instance of which was found live in this queue and repaired the same day.

**What changes.** `CLAUDE.md` gains a short entry saying a tersify pass exists, runs when you ask for it, and points at the write-up. **The pass-2 method is mandatory when it runs** — item-level splice keyed by slug, unchanged blocks carried byte-identical, slug-uniqueness assertion, per-block deltas so nothing grows silently — and pass 1's rewrite-from-memory is named as the method not to repeat. **Fenced blocks are untouchable**, on the write-up's §8d and [two-column-fences-wrap-unreadably].

**What the close does instead, at no rewriting cost:** report which entries breach the ceilings, which is a measurement and needs no invented threshold now that the figures are derived.

**Files:** `CLAUDE.md`. Host-only — the write-up is a dev artifact and consumers have no such pass.

Rule gate: run — no rule authored for the corpus; one host-only entry naming an on-request pass and pointing at a procedure already on the shelf. **Nothing evicted.** The disposition is a refusal of the placement rather than of the work: at the close, rejected on measured yield and two unattended failure modes.

#### Rename `docs-b/` to `docs/`, overturning the refusal recorded the day before [rename-docs-b-folder]
Filed 2026-08-16 by Claude, on the user's decision, after she challenged the refusal during the planning session that had just cited it.

**Her words, which are the reason this exists:** *"i don't know why it's still called docs b even though i have been asking for that to be changed for weeks. there is no docs a anymore so why would it be called docs b."* She is right on the model — docset A was retired 2026-08-09, nothing picks between docsets, and the letter names a sibling that does not exist.

**The refusal being overturned, and why it does not hold.** [docs-b-name-outlives-the-two-docset-model] shipped 2026-08-16 and refused the folder rename outright, on a grep: 639 occurrences, 215 live, **424 in `LOG/` and one archived message.** The argument was that renaming moves the "B" out of a live path `CLAUDE.md` can explain and into 424 historical references pointing at a folder that no longer exists — "drift by fixing drift."

**That argument treats a session record as though it were supposed to describe the present.** It is not. A LOG entry written in August naming `docs-b/` accurately records what the folder was called in August, which is what a record is for. Nobody proposed rewriting those 424, so the choice was never between renaming and falsifying the record. The Codex-port precedent the refusal cited says the same back: that decision was about **not rewriting** history, an argument for leaving `LOG/` alone rather than against renaming a live folder going forward.

**So the real cost is the 215 live references**, across 22 files: all five skill entry points, `session_start.py`, four of the docs themselves, four test suites, `CLAUDE.md`, `SPEC.md` and the migration recipe. This project has already carried out a larger rename in a single build — "Sovereign Implementer" to "Throughliner" moved the plugin slug, the package folder, both project marker files and the positioning together.

**Who decided what, recorded because the first decision's authorship is the point.** The rename was refused by Claude, at a close, with the user's question as the trigger and no moment where the choice was put to her — the same shape as [rule-admission-has-no-independent-approver], one layer out. This reversal is her decision; the reasoning against the old argument is Claude's, given at her challenge.

**`Runs alone`, and this is the marker's textbook case.** The work moves file paths underneath anything in flight, so a run holding paths in its working file and scope-lock list would find them stale mid-build.

**Trace the ripple by grep before building, per the hook-enforced-format rule** — `docs-b` as a literal across the repository, not a file list written from this item. The counts above are from 2026-08-16 and will have moved.

**Leave `LOG/` and `INBOX/archive/` untouched.** They are the record. `resources/plugin-behaviour-retired.md` is a retired archive and is also left alone.

**`QUEUE.md` IS a live reference and must be updated, which this item's first pass missed.** Open work items carry the old path in their own Files lines — [law-prose-restyle] and [files-line-names-excluded-files] both do at the time of filing — and a queue item is an instruction to a future build, not a record of the past. Left alone they would send a run at a folder that no longer exists. The `LOG/`-is-a-record argument does not extend to the queue: the queue describes what is still to be done.

**Files:** `plugin/throughliner/docs-b/` renamed to `plugin/throughliner/docs/`, with every live reference updated — the five skill entry points, `plugin/throughliner/hooks/session_start.py`, the docs that cross-reference each other, the four suites under `resources/testing/`, `CLAUDE.md`, `SPEC.md` and `plugin/throughliner/docs/migrate-checklist.md`. `CLAUDE.md`'s refusal paragraph is deleted and replaced with a dated line recording the rename and noting that earlier session records name the old path. `QUEUE.md` — every open item's Files line carrying the old path, rewritten to the new one. Exclusions and untouched paths are named in the paragraphs above rather than on this line.

Runs alone

Rule gate: run — no rule authored and none amended. **The disposition is an eviction:** `CLAUDE.md`'s paragraph refusing the rename is deleted outright, along with the reasoning that supported it, and replaced by a dated statement of fact. Failure evidence is the refusal itself failing on its first contact with the user it was written for — she read the explanation and rejected it the next day.

#### Restyle `done.md` and `plan.md` to the law-prose standard [law-prose-restyle-heavy-docs]
Filed 2026-08-17 **on your decision that the restyle continues to the rest of the corpus.** [law-prose-restyle] shipped this morning covering `skill-nonspecific-rules.md` alone and was consumed by that build, so the continuation had no queue item at all.

**These two first** because they are the largest rule-bearing docs and both are already scheduled for subtraction work, so findings have somewhere to land.

**What changes.** Each doc rewritten to the wording standard the rule gate specifies: prohibitions restated as the action required, qualifications carried by structure rather than explanation, main clause first, one idea per provision, and rationale moved out of operative statements into the record. The shipped pass is the precedent for what that looks like in practice.

**Acceptance test, taken from the pass that worked:** rule-statement count before and after, accounted for statement by statement, with any change composed rather than asserted — `resources/rule_signals.py` reads the count. **Its stated limit is inherited too:** a flat count cannot detect a rewrite that changed a rule's meaning, so the pass claims coverage of what it read and nothing more.

**Ordering, written into both entries.** This runs before [law-prose-restyle-remaining-docs], and both run before [session-occurrence-audit], which reads these same files and would otherwise gather a list the rewrite makes stale — that is why the audit is held.

**A second lens rides this pass, folded in from [freestanding-rules-that-should-be-subordinate] on your instruction 2026-08-17.** While each doc is rewritten, look for the signature that item names: **two or more rules governing the same subject, stated at the same level, with no declared relationship** — and land them as a parent with subordinate units, which is what the admission rule already requires of a rule being authored and which nothing has ever applied backwards to rules already shipped. Candidate subjects it names besides length: what gets written where, when to ask versus proceed, and what counts as evidence.

**One interaction the fold creates, stated so the acceptance test is not misread.** Subordinating two rules under one parent **reduces** the statement count. So a fall in the count is no longer automatically an eviction: each reduction is attributed to either a merge under a parent or a deletion, and named as one or the other. Without that, this lens and the flat-count test contradict each other.

**And the gap the fold would otherwise leave, closed here.** The known instance — at least three separate statements about how long something should be, none referencing the others — is in `skill-nonspecific-rules.md`, which was restyled this morning **without** this lens. So that file is in this item's scope for the lens alone, not for a second restyle.

**A third lens, folded in from [rationale-audit-fetched-docs-gap] 2026-08-17 — and only onto these two files, which is that item's own recommendation.** The per-paragraph **delete-and-reread** test runs on every paragraph of `done.md` and `plan.md`: delete the sentence and read what remains, where a complete instruction means what you deleted was rationale and an unfinished one means it was operative.

It folds rather than auditing first because this pass cannot restyle a paragraph without already deciding which half is rationale, so a separate audit would make the same decision twice. **What that gives up is the user seeing findings before the text moves, so the record carries each rationale removal and where it went**, site by site.

**Test [rationale-in-items-flows-into-shipped-docs] before running this lens.** It asks whether the rationale in these docs arrives from the work items builds transcribe — and if it does, this lens removes text the items keep putting back, so the pass has to run again. The test costs a read; this pass is per-paragraph judgement over the two largest docs. **The distinction that item carries binds here too:** operational rationale, needed to apply a rule, stays and is written into the operative sentence; only rationale preserved for the record leaves. The ordering is written into both entries.

**Files:** `plugin/throughliner/docs-b/done.md`, `plugin/throughliner/docs-b/plan.md`, and `plugin/throughliner/docs-b/skill-nonspecific-rules.md` for the subordination lens only.

Rule gate: run — no rule is authored, amended or evicted; the standard being applied was admitted when the gate was, and this extends it to more files plus one lens the admission rule already contains. **A restyle is the one pass that can silently author a rule by rewriting one**, which is why the acceptance test is a count accounted for statement by statement rather than a reading.

#### Restyle the remaining rule-bearing docs to the law-prose standard [law-prose-restyle-remaining-docs]
Filed 2026-08-17 on the same decision of yours. **Follows [law-prose-restyle-heavy-docs]** — placement carries the order and this sentence carries the reason, since it could be built on its own and so names no `Blocked by:`.

**Why it follows rather than blocks it.** The two heavy docs are where the standard meets the hardest text, so settling those questions once stops this pass answering them ten times over.

**Scope, narrowed deliberately to the rule-bearing docs.** SPEC and the FAQ are out: the law-prose standard is a standard for *rules*, SPEC is product truth governed by its own three maintenance rules, and the FAQ is consumer-facing answers rather than instructions to Claude. Nothing is orphaned by that — "session" occurrences in SPEC and the FAQ are covered by [session-occurrence-audit], a terminology pass rather than a wording one.

**What changes.** The same standard and the same acceptance test as the heavy-docs pass, applied per file — the rule-statement count accounted for statement by statement **for each doc rather than in aggregate**, so one file's growth cannot hide behind another's cut.

**Files:** every doc under `plugin/throughliner/docs-b/` except the three already restyled — `skill-nonspecific-rules.md`, `done.md` and `plan.md`. Enumerated by listing the folder at build time rather than written out here, because [rename-docs-b-folder] may change that folder's name first and a list written today would name a path that no longer exists.

**Runs before [session-occurrence-audit]**, which is held against this item for that reason.

**Carries the subordination lens too**, folded in from [freestanding-rules-that-should-be-subordinate] on your instruction 2026-08-17: look for two or more rules governing one subject, stated at the same level with no declared relationship, and land them as a parent with subordinate units. Its terms and its interaction with the count are stated once in [law-prose-restyle-heavy-docs] rather than repeated here — including that a **fall** in the statement count must be attributed to a merge or to a deletion, since subordination reduces the count without evicting anything.

**What this item deliberately does NOT carry, stated so it reads as a decision rather than an omission.** The per-paragraph rationale test folded into [law-prose-restyle-heavy-docs] stops there. These ten docs keep the **signature-phrase** criterion for rationale, which is what they have had. The reason is measured rather than guessed: extending per-paragraph judgement across the fetched docs was costed at roughly 42,000 words of it, and that figure is why the earlier extension was refused. [rationale-audit-fetched-docs-gap] recommended the two-file limit for exactly this reason, and folding the lens everywhere would quietly overturn its own recommendation while claiming to honour it.

Rule gate: run — no rule authored, amended or evicted; an extension of an already-admitted standard to the remaining files, carrying the same silent-authoring caution as its sibling and the same lens.

#### [user] Discord post: the ordering ladder cut from six rungs to three, and every rung now costs no judgment [discord-post-context-adjacency]
Captured by you 2026-08-12; the angle is yours — the ladder and how much it improves the workflow. **Subject replaced 2026-08-15 — see the correction below. The slug is unchanged because slugs are immutable.**

**The subject this post had was deleted before it was ever posted, and that is the correction.** It was written to announce the cheap-to-settle rung — "/plan offers you the work closest to what this session has already read". Commit `0e62afe` on 2026-08-15 cut the ladder from six rungs to three and deleted that rung, the rung-6 offer and the decay rung with it. The item was sitting **cleared to run** when found, so a /next run reaching it would have walked you through drafting and posting a public claim about a mechanism that no longer exists. Caught by reading the item during processing; the digest's placement check matches a fixed set of known phrases and does not reach this shape, which it says of itself.

**The replacement subject is the deletion, and it is the better post.** Six rungs became three: an uncleared red flag, then unblock-potential by citation count, then longest-first by line count. **Every surviving rung either reads a field the digest already computes or subtracts two line numbers**, so ordering costs no judgment at all. Longest-first was also re-grounded — on cost-of-reading rather than on length predicting how finished an item is, because the settling session's own data contradicted the latter.

**What makes it worth saying rather than a changelog line.** The honest version is about subtraction: three rungs asked Claude to weigh something, and weighing is where a mechanism quietly stops being reproducible. The tool got simpler and more predictable in the same move — a harder and more interesting claim than "we added a feature".

**A judgment for you at drafting time.** The before-picture is that some deleted rungs were things this project built, used, then decided were not carrying their weight. Whether that goes public is your call; it is what makes the change legible rather than arbitrary.

**Verify before posting, not merely before drafting.** Every claim must be true of the *installed* plugin at the moment it goes out. Compare the installed host's build stamp against the target's before you post, since the cut is committed but a host that has not been reinstalled still runs six rungs.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [ladder-rung-for-context-adjacent-items] shipped and has since been refined once — the offer now leads with a recommendation rather than a flat menu (`LOG/2026-08-12-context-adjacency-offer-is-a-flat-menu.md`, `e5d169b`). Draft against the refined behaviour. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries], which absorbed the item recording this.

**Paced 2026-08-14 on the user's decision: head of a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Nothing here is unready — pacing alone held it. **The framing was repaired 2026-08-18** — it read "Her words:" over a paraphrase, which is a quote claim the text cannot support, and the three sibling post items carry the hedged form. Found by the tersification write-up's own §7, which predicted exactly this upgrade.

**Correction, 2026-08-15, in the user's own words: no post went out on 2026-08-14, "because it wasn't presented to me in next."** This item's earlier claim that she had already posted that day was wrong, and so is the same claim in [announcement-cadence-clear-to-resume]. What happened is worse than a delay: holding the item below the line made it invisible to /next, so the pacing did not slow the post down, it stopped it happening at all. That is the failure [held-items-invisible-during-normal-use] describes, observed live.

**Lifted 2026-08-15.** The holding fact — a day has passed since the last announcement — is true regardless of whether one went out on the 14th, and more clearly true if none did. Cleared to run; the three posts behind it still follow in order.

#### [user] Write the article comparing Throughliner to memory-system approaches, finishing with what shipped [competition-comparison-article]
**Captured by you 2026-08-15**, from a discussion prompted by Discord talk about "Obsidian memory systems" and "dreaming". **Your framing and your decision: the analysis reads as an article starter for the Throughliner site, and rather than sending it now it should be captured and finished with our shipped solutions, with the announcement doubling as a Discord post.**

**This is your own shipped-only rule applied correctly, and you reached it independently.** `CLAUDE.md` says a post announces only what has shipped, and that where a post describes work designed but not built, it waits for the build and is filed as a queue item naming what it waits on. That is exactly this.

**Your stance on the article's framing, recorded 2026-08-17 and NOT generalised into a rule.** Claude proposed turning it into a standing rule about all writing describing Throughliner, and you refused: it *truly depends what we are writing, and the tone required*. Claude had also flattened the position itself — writing "no stake in persuading anyone that one approach beats another" where **your actual position is that you have a stake, just not in being seen as the best thing since sliced bread.**

**Your assessment of the draft, which is the live problem with this item.** It swung from hard marketing to substantially explaining why the competition is better. You sent it to the other project for polishing rather than continuing here, because you wanted to move on — so the draft is out of this project's hands and the item covers what comes back.

**What it waited on: [digest-reports-computed-fields-not-summaries].** The article's honest weak points — manual curation, a 56,000-token queue read — are answered by that item and nothing else queued. Naming it rather than a vague "the digest work" matters, because a reference to something not yet filed is the failure this session hit twice.

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

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected).

#### [freeform] Run /setup on this project, outstanding since 1.12.0 [setup-outstanding-here]
`session_start` reports the plugin moved 1.12.0 → 1.20.0-test10 since this project was last set up, and says /setup wants a session of its own. A standing condition surfaced at every session opening and acted on by nobody, the eight-version gap itself going unremarked.

**`[freeform]` settled at processing, from the tag's own definition rather than a judgment call.** /setup refuses outright while a build is in progress, and a /next run is a build in progress — so this cannot execute inside a run, which is what `[freeform]` names. Not `[user]`: the test is whether Claude can do it at all, and Claude can. The constraint is the session, not the capability.

**Placed last in the cleared region, below the two `[user]` posts.** /next halts on a `[freeform]` item, so anything beneath it is never reached in that invocation — the bottom is the only position that lets the run clear everything else first. The `[user]` items are walked during a run and must sit above it.

**Not a prerequisite for the cleared work.** No format halt has fired, so this is the version top-up rather than a format migration, and the top-up is add-only — it never rewrites what the user has written. The doc edits queued ahead of it are not at risk from running it afterwards.

Relates to [next-presents-items-setup-will-overtake], which covers a run being presented while this is outstanding rather than the running of it.

--- Cleared to run above this line ---

#### Split the bundled gitignore offer so a private queue with a public log is reachable [queue-privacy-default]
**Subject settled at processing 2026-08-17; the slug is unchanged because slugs are immutable.** Raised by you as a consequence of cross-project captures but true today regardless. **The rescope is Claude's, deferred to in your words: "as you recommend."**

**The default does not move, on your own objection to your own proposal:** someone may want a visible queue for transparency.

**The real gap is that the offer is bundled.** Scaffolding offers `SPEC.md`, `QUEUE.md` and `LOG/` as one all-or-nothing choice. So a user who wants their plans and reasoning private while their history stays public cannot have that — the combination is unreachable rather than merely un-defaulted, and it is the combination this project itself runs on in spirit, since LOG is what it publishes and the queue is where the thinking sits.

**What changes.** `setup.md`'s privacy offer becomes per-document rather than one bundle, with the trade stated once rather than three times, and no default changed for anyone. The existing single-question shape is what earns the split: it stays one question with three answers, not three questions.

**Files:** `plugin/throughliner/docs-b/setup.md` (the privacy offer), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is not listed — its privacy-posture sentence describes the bundle and is rewritten in this planning session.

**Held below the line 2026-08-18, on inbound mail rather than on anything wrong with this design.** A consumer project reported that a `.gitignore` can leave `SPEC.md`, `QUEUE.md` and `LOG/` untracked with nothing noticing, which is [gitignored-core-docs] — the same code path this item rewrites. Shipping a per-document offer while the check beside it cannot see a fatal pre-existing entry would put a second question in front of the user at the one moment the first one is already going wrong. Settle them together.

Blocked by: [gitignored-core-docs]

Rule gate: not needed — no rule authored or amended; this widens an existing offer's answer set and evicts nothing.

#### A repeal can falsify an already-posted announcement, and the same grep would catch it [repeal-falsifies-a-posted-claim]
Split from [repeal-has-no-ripple-trace] at processing 2026-08-17, when that item reached 542 words against a 345 ceiling. Kept apart rather than merely trimmed because the two differ in readiness, not only in length: the live-doc trace is buildable now and this is not.

**The instance is your own spec-driven-development post**, which described a build that "asks first, adds SPEC.md to its own file list, and edits it in the same commit". [missed-spec-write-interrupts-the-run] inverts that — a build now hands the sentence back rather than writing it — so a claim that was true when posted became wrong through ordinary work, inside the same conversation that made it.

**The trace is identical to its sibling's.** Grep the distinctive words of the repealed sentence. What differs is only where you grep: a repeal already greps live documents, and this extends the same pass to the record of what was published.

**Why it cannot be built yet.** There is nothing to grep. Posts are not written down anywhere, which is [send-record-lacks-destination-and-intent] — the outgoing index that gives every send a line carrying its destination, its intent and what it claimed. Until that file exists this item has no target, which is why it is held rather than cleared.

**What changes when it lifts.** The repeal limb on the keep-step gains one more place to look: an item repealing shipped behaviour greps `INBOX/sent.md` for the claim, and where it finds one, a correction post is filed as its own `[user]` line rather than assumed.

**Files:** `plugin/throughliner/docs-b/plan.md` (the repeal limb, extended to the sent record) and `CLAUDE.md` (the Discord section, which is where a correction post's obligation belongs and is host-only).

Rule gate: run — one more site on the repeal limb its sibling item ships, so it is subordinate to a rule that will already exist by the time this builds, and spends no slot. Nothing evicted. Failure evidence is one instance, and it is the only one available: nothing records what was posted, so earlier cases cannot be found at all — which is itself the argument for the record rather than for this rule.

Blocked by: [send-record-lacks-destination-and-intent]

#### [audit] Classify every occurrence of "session" against the settled vocabulary, immediately before the corrections [session-occurrence-audit]
Filed 2026-08-17, absorbing five captures from [terminology-corpus-audit] that were deleted once their content was carried into this item and into [session-vocabulary-corrections].

**The vocabulary, settled by you on 2026-08-17 and recorded here because this item and the corrections both read it: a RUN is a command executing — a /plan run, a /next run — and a SESSION is the chat.** You chose it over two alternatives — a `<command>` session pattern, and keeping three named slots — because "session" is already in widespread use meaning the chat, so this splits the two ideas rather than adding qualifiers to a word doing two jobs. **Your correction to Claude's objection:** "the close" is residual language from a step that no longer exists, so it was no argument against anything.

**What the audit reads.** Every occurrence of "session" across the procedure docs, `faq-template.md` / `FAQ/faq.md` (185 each, the same document) and `SPEC.md` (88). Roughly 707 in all.

**What it produces.** One classification per occurrence: means the chat, means a run, or is correct as it stands and must be left alone. A stop-list is a constraint it inherits: "mid-session", "short session", "fresh session" and "isolated session" all correctly mean the chat and are left alone, as is `done.md`'s "session type", which classifies a chat rather than naming a run.

**Why an audit and not a script.** Finding the occurrences is a grep; deciding what each one means is judgment on every line. That is this project's own test for when an audit survives.

**Why it runs behind the restyle.** The restyling passes rewrite the same text, so a list gathered before them is stale before anything uses it. [law-prose-restyle] shipped in `7e3c1c8` — `LOG/2026-08-17-law-prose-restyle.md` — but covered one file, so the reason still stands for the rest.

**Lifted and re-held on 2026-08-17, both moves recorded because the second corrects the first.** It was lifted when [law-prose-restyle] was found shipped; you then decided the restyle **continues to the rest of the corpus**, which restores the holding fact. It now waits on [law-prose-restyle-remaining-docs].

**Re-count before starting rather than trusting the ~707 figure above:** the shipped pass covered `skill-nonspecific-rules.md` only, taking "session" there from 61 occurrences to 9, so the remaining weight sits in the procedure docs, the FAQ and SPEC.

**Why the existing survey is not enough.** [terminology-corpus-audit] enumerated collocations, not occurrences — a floor on how many meanings exist, never a ceiling — and never reached the FAQ or SPEC, which are the consumer-facing texts. The scale is measured: across five procedure docs, bare forms outnumber qualified ones by roughly nine to one — 134 bare against 29 qualified — so 134 judgment calls rather than substitutions sit in those files alone.

Blocked by: [law-prose-restyle-remaining-docs]

#### Rename every occurrence of "session" that means a run, per the audit's classification [session-vocabulary-corrections]
Filed 2026-08-17 from the same settlement. **The corrections pass, which cannot start without the audit's line-by-line list.**

**What changes.** Each occurrence the audit classified as meaning a run is reworded to say run; each classified as the chat or as correct is left untouched. The stop-list is honoured rather than re-derived.

**Scope includes the code, which is a different case.** `session_id` names the chat and is the harness's own field, so it is not renameable; what is ours is the variable names, the comments and the `_build-<session_id>.md` filename — and that filename is parsed by `pre_tool_use.py`, so changing it is a hook-enforced-format change whose ripple is traced by grep first. The code is not the loose-usage case settled by [work-item-term-in-hook-and-script-code]: there the code used a term loosely for the same thing, here it uses the word for a different thing.

Blocked by: [session-occurrence-audit]

#### [user] Discord post: Claude now knows how the work cycle actually fits together [discord-post-cycle-awareness]
Captured by you 2026-08-12; the angle is yours — awareness of the build cycle.
**Cannot be written until [cycle-summary-at-every-skill-opening] has shipped.**
**The honest before-picture, also the strongest material.** Every piece was documented — what an audit does, what a capture is, what /plan may process, what /next may build — and nothing stated the loop. Claude assembled it wrong twice in consecutive sessions, both times confidently, reasoning that a planning session between an audit's findings and their build meant the findings couldn't reach the build. That is the cycle working. Your objection the second time, rendered in Claude's words rather than quoted: this is the second planning session in a row where you've had to explain it.
**The design point worth including.** A flat list of stages would not have prevented either failure, because both were about a loop *closing*. What shipped names the return edges explicitly.
**Same judgment as the sibling post:** the before-picture is Claude getting it wrong; publishing that is yours to decide.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [cycle-summary-at-every-skill-opening] shipped — `LOG/2026-08-12-cycle-summary-at-every-skill-opening.md`. Ordinary ready work. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: second in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone holds it. It lifts when [discord-post-context-adjacency] is posted and closed.
Blocked by: [discord-post-context-adjacency]

#### [user] Discord post: how much stronger a session is from its start once /plan opens by reading recent LOG index lines [discord-post-session-start-strength]
Captured by you 2026-08-11. Your point, rendered in Claude's words rather than quoted: before, it felt shaky for the first few items; starting with log-awareness plus some maybe-relevant context massively boosts the start of sessions. The angle is yours; the correction below is Claude's.
**It cannot be written yet, which is why this is a queue item rather than a draft.** You asked believing the feature was live. It wasn't: `plan.md`'s Step 1 reads QUEUE.md and SPEC.md only, and its three `LOG/index.md` mentions are targeted lookups — has this been decided — not an orientation read. The feature is [plan-reads-recent-log-index], held below the line behind [index-line-length-proportional-cap].
**Your experience was real; the mechanism you credited was wrong.** What steadied that session was the below-line revisit reading LOG to check two blockers, plus the previous session's forward advisory naming where to start. Both live; neither is the five-recent-lines read. Worth carrying into the post — "the thing that helped wasn't the thing I thought" is the better story.
**The post's content, to draft when it ships.** The shaky-first-items problem and its cause; what the orientation read changes; and the honest scope — it doesn't carry all necessary context, it sets upcoming work against past work. Include the cost bound, since it's why the feature waited: five index lines is an unbounded read until index lines are capped, which [index-line-length-proportional-cap] fixes.
**Constraints:** 2000 characters, the Discord limit. Not posted until *everything* the post describes has shipped — standing rule in `CLAUDE.md`, adopted 2026-08-11.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside the limit. 3. You say what to change. 4. You post — Claude has no route to Discord. 5. You confirm, and the line closes.
**Unblocked 2026-08-13.** [plan-reads-recent-log-index] shipped — `LOG/2026-08-12-plan-reads-recent-log-index.md`; /plan's read-state step now opens with the five newest index lines. Ordinary ready work. Fourth item found sitting behind a shipped blocker; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: third in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone holds it. It lifts when [discord-post-cycle-awareness] is posted and closed.
Blocked by: [discord-post-cycle-awareness]

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

## Unprocessed

#### Last session advises testing [rationale-in-items-flows-into-shipped-docs] before the restyle builds [forward-advisory]
The test costs a read of git: take items whose prose carried heavy reasoning into a build, and check whether that reasoning turns up in the doc the build edited. If it does, the rationale accumulating in the always-loaded rules arrives from the items rather than from authoring discipline.

**Why before rather than after.** [law-prose-restyle-heavy-docs] carries a per-paragraph rationale lens over the two largest rule-bearing docs. If the cause is upstream, that lens removes text the items keep putting back and the pass has to run again. Both entries carry the ordering.

Also worth taking early: [plan-entry-split-wording-disagrees], because the two statements it names govern how every planning close is written, including the next one.

Four captures arrived after the last processing pass — two consumer reports and three from the ideation-loop discussion — and none has been weighed.

#### Show-first approval moments produce their text twice [approval-flow-token-doubling-simplification]
Captured by you (2026-08-01) while reviewing your Claude Code feature request anthropics/claude-code#77134. Rescoped at your direction 2026-08-13 from a larger item about approval-time doubling generally.
**The cost, narrowed to where it still exists.** Showing text in chat and writing it to a file are both the model producing those tokens, so text doing both is produced twice. That used to hit every approval moment; it no longer does — write-first shipped, and the post-write report is one line naming what landed, never a re-paste.
**What remains is the show-first set only** — the moments write-first deliberately keeps showing first, because the previous version isn't recoverable without the user: a commit message, anything leaving the machine, a wholesale conversion of a document the user already owns. There the text is composed in chat, approved, then produced again to be used.
**Why it is not buildable yet.** The saving needs the harness to surface an already-produced Write's content verbatim with no second model pass — issue #77134, which hasn't landed. Until it does there's no build to describe. Re-examine when the issue ships.
**Two things settled, not to be re-opened here.** The write-first ordering flip is decided and shipped. The convergence note about view-in-doc machinery is spent — working-mode field, Editor field and line-anchored-link promise all retired 2026-08-09.
External dependency: anthropics/claude-code#77134.

#### Routing communication feedback to memory masks the method defect that produced it — the memory-boundaries rule needs the exception [memory-masks-method-defects]
Captured by you — raised 2026-08-09 at a /done close, filed after `115f851`. Your point, rendered in Claude's words rather than quoted: if Claude's replies are affected by memory, then the method can't truly be tested.
**The conflict the shipped rule does not see.** plugin-behaviour.md's memory-boundaries rule lists what memory is free for: user preferences, working style, **communication feedback**, cross-project facts. Separately, this project's CLAUDE.md states that all use of the plugin to develop the plugin is testing it, and that any moment session memory covers for something the docs should carry is a mandatory capture. Nobody applied that second rule to *persistent* memory, and the two disagree: saving communication feedback to memory is permitted, and doing it here contaminates the only test the method gets.
**Why it is sharper than a self-hosting quirk.** Communication feedback is very often *evidence about the method's own narration rules*. This session demonstrates it: the user twice said there was too much text — evidence that the /plan checkpoint is too long, filed as [done-invoked-when-user-meant-continue]. Had that also gone to memory, Claude would simply have behaved better, the queue item would have stopped mattering, and the defect would have survived in the shipped docs. Memory would quietly buy a fix for one user while every consumer kept the bug.
**So the routing test is not "is this a preference?" but "is this evidence about the method?"** A preference no method rule governs — a name, a timezone, a tool the user likes — stays memory's. Feedback that a *method-produced behaviour* was wrong is a testing outcome and belongs in the queue, whether or not it also reads as a preference. The overlap is the problem: it is genuinely both, and the current rule names only the branch that silences it.
**To settle at processing:** the exact wording of the exception; whether it is general or scoped to projects testing the method; and whether the shipped rule should say plainly that feedback about Claude's own narration is a capture first and a preference second. Weigh against the admission gate — this may be an amendment rather than a new rule, which is cheaper.
**Files (rough):** `plugin/throughliner/docs-b/plugin-behaviour.md` (Routing and discipline, Memory boundaries), possibly `CLAUDE.md` if the self-hosting half needs stating separately. Relates to [done-invoked-when-user-meant-continue] (the live instance). It used to be a candidate payload for [self-hosting-auto-detection], deleted 2026-08-14 — the absence of any payload only detection could switch on is what settled that item.

#### The behaviour-rules read can be hook-enforced after all, and the reason it wasn't is documented wrongly [behaviour-rules-read-is-enforceable]
Filed 2026-08-10 during /plan; rides this session's /done commit. Mixed authorship: the user refused Claude's assertion that a forced read was impossible and asked for it to be checked; the research and findings are Claude's, from the Claude Code hooks reference. Full evidence, including the verbatim JSON shapes a build would need, is at `resources/research/hook-enforced-doc-reading.md`.
**Finding 1 — the shipped design's stated premise is wrong.** `session_start.py:360-384` explains that the rules are pointed at rather than pasted because the file is tens of kilobytes and "blew the cap by a wide margin". The 10,000-character cap is documented as **per hook command, not aggregate**, so several `SessionStart` commands could carry the rules in directly. The docstring's reasoning holds only for a single command and doesn't say so. Unverified: whether the harness concatenates multiple SessionStart outputs cleanly and in stable order.
**Finding 2 — a read-gate is constructible.** `PreToolUse` receives `transcript_path` and can return `permissionDecision: "deny"` (or exit 2). So a hook can scan the transcript for a completed Read of the behaviour doc and deny or ask until it finds one — genuine enforcement, same class as the scope-lock. Unverified: the transcript's on-disk format, whether a Read's target path is reliably recoverable, and behaviour on resume, after compaction, and inside a subagent.
**Finding 3 — nothing can force it at session start.** `SessionStart` hooks are context-only and cannot block. Enforcement necessarily fires at the first tool call.
**Sharpened at processing 2026-08-10, left here deliberately.** The docstring correction was split out as [session-start-cap-docstring-wrong] and cleared. What remains isn't a build: its file list would be the design's own output, so the keep-check's second limb fails by construction. Two things must be **measured** first, and neither is a lookup:
1. Does the harness concatenate multiple `SessionStart` outputs cleanly, in stable order, with no aggregate limit further up? The reference is silent, so this is an experiment.
2. Is a completed Read's target path reliably recoverable from the transcript `.jsonl`, and does that survive resume, compaction, and a subagent?
Both need a rezip and an application restart, so the experiment is Claude's work and the restart the user's — already decomposed as [statusline-test-script] plus [statusline-restart-test]. Don't build that structure until the prior question is answered: whether enforcement is wanted at all. That belongs with [rule-lifecycle-system]'s born stage.
**The ordering established when this was filed, kept as the frame for that decision:** a filename steers weakest, a first-line admission test steers better, a required close-time artifact leaves a trace, and a hook denial is the only one that cannot be skipped. Costs run the other way — a transcript scan on every tool call is the most expensive.
Relates to [extract-skill-nonspecific-rules] (whose new doc inherits the same unenforced directive), [rule-lifecycle-system] (whose "born" stage carries the same visible-but-unenforced gate problem) and [restore-plan-file-gate].

#### An "unattended" /next run is not unattended: it stops for [user] items and never closes itself [unattended-run-is-not-unattended]
Captured by you 2026-08-11 in the post-close tail. Your point, rendered in Claude's words rather than quoted: an unattended run is not actually unattended — it stops for user items and doesn't automatically run /done on itself; we can design that, but it needs consideration of where user items land.
**The claim as it stands.** `SPEC.md` calls multi-item /next "unattended in practice — the autonomous build mode the Principles name", and the Principles say execution sessions trend toward pure execution, "stopping only for what genuinely needs the user". In practice a run stops at least three ways: a `[user]` item is walked through live one step at a time; a `[freeform]` item halts it outright; and at the end it simply stops, because **/done is a command the user runs**. So a run left alone finishes its builds and sits there uncommitted until someone returns.
**Why this is worth more than a wording fix.** The word shapes real decisions. `[user]` and `[audit]` lines are placed end-preferred *because* a stop inside a contiguous build run interrupts an otherwise unattended sequence — that rule only makes sense if the run is meant to be left alone. The readiness line was made the run's sole bound on the same reasoning. If "unattended" is aspirational, several settled decisions rest on an overstatement.
**What a design has to settle, and your condition is the hard part.** Where `[user]` items land. End-preferred placement batches them at the end of the cleared region, the right instinct but only a tie-adjustment — a genuine dependency still puts a `[user]` item mid-run. Options: whether a truly unattended run must exclude `[user]` items entirely and leave them to a separate walk-through session; whether the readiness line grows a second meaning (build up to here unattended, then stop for the human); or whether the honest answer is to stop calling it unattended and describe it as a run that clears vetted work and pauses where a person is genuinely needed.
**The self-closing half carries a real tension.** A run that ran /done on itself would commit without the user present, and the commit message is one of only two things the method still shows before it happens — precisely because a commit is hard to unwind and never becomes file content. So auto-closing either overrides that rule or needs a form of it that survives nobody being there. Settle that before, not after.
**Files (rough):** `SPEC.md` (the Multi-item /next paragraph and the Principles), `plugin/throughliner/docs-b/next.md` (stopping behaviour), `docs-b/done-plan.md` (end-preferred placement, whose rationale rests on this), plus an FAQ entry — a user reading "unattended" and walking away is exactly who this misleads. Relates to [arbitrary-run-length-capping] and [processed-reorder-mostly-unnecessary].

#### The filing-claim hook fires on a slug that was only cited, not filed [stop-hook-fires-on-cited-slugs]
Filed 2026-08-13 by Claude from a live instance in this /plan session, after the last committed close, so it belongs to no committed session record.
**What happened.** A message cited `[nothing-runs-the-hook-tests-at-a-close]` while reasoning about an already-built item — quoting a planning entry's kept-list and naming that item's LOG file. The stop hook read the slug as a filing claim, found no matching `#### ` heading in QUEUE.md, and blocked with "the write did not happen". Nothing had been written, and nothing was meant to be.
**Why the detector cannot tell them apart as written.** A slug in square brackets is the method's only cross-reference notation, and the always-loaded rules positively require citing other items by slug in prose. So the hook's signal — a slug in a message — is present in the ordinary compliant case as well as the failure case. Not a tuning miss; the two shapes are identical at the level the detector reads.
**This is the second recorded shape, and the pair is what makes it structural.** [stop-hook-fires-on-drafted-not-filed-captures] records the hook firing on a capture presented as a draft for approval, also a shape the method specifies. Both fire on conduct the rules mandate.
**A harder case the fix must survive:** an item genuinely built this session is absent from QUEUE.md for the correct reason — /next consumes it — so absence can never on its own mean a write was missed.
**One thing to check rather than assume:** whether the detector distinguishes a slug in a reporting sentence from one in a citation, and whether it can consult LOG filenames before concluding a slug is unfiled. Relates to [stop-hook-fires-on-drafted-not-filed-captures] and [disposition-detector-is-format-brittle].

**Two further instances, 2026-08-17, both in one planning session and both on SHIPPED work.** The hook fired on [rename-to-throughliner] and again on [law-prose-restyle], each cited as work already built and therefore correctly absent from the queue — /next consumes an item when it builds it. Each cost an exchange. **This sharpens the fix rather than only adding weight:** in both cases a LOG entry named after the slug existed, so consulting `LOG/` before concluding a slug is unfiled would have suppressed both, and that is the check this item already suspected. It also confirms the harder case named above is the whole difficulty — absence from the queue cannot mean a missed write, because the successful case produces exactly that absence.

#### The project's two Claude Code config files point at a folder layout that has not existed for months [claude-config-points-at-dead-layout]
Filed 2026-08-13 by Claude during the identity-rename build. Filed after the last committed close, so it belongs to no committed session record.
**What was found, and it is not what the rename item predicted.** [rename-to-throughliner] listed `.claude/launch.json` and `.claude/settings.local.json` among the files the folder rename would invalidate. Neither was, because neither pointed at `plugin/si-plugin`. They point at a much older layout — a top-level `sovereign-implementer/` folder with `planning/`, `build-log/` and `Dev/Resources/` — under a user path (`C:\Users\Alex\...`) that is no longer this machine's. That folder hasn't existed for a long time.
**What this means in practice.** `launch.json` declares one dev-server configuration serving `sovereign-implementer/crash-course`, an absent directory, so it cannot start. `settings.local.json` carries roughly fifteen permission allowlist entries naming absolute paths into that dead layout; a permission entry for a path that cannot occur never matches, so they're inert rather than harmful. Two live entries in the same file *did* name the real `plugin/si-plugin/scripts/reorder_queue.py` and were corrected in the rename build.
**Why it is captured rather than fixed there.** The rename item's work is the identity change, and none of this is that — the strings were stale for an unrelated reason, before the rename started. Fixing them means deciding what `launch.json` should serve now, or whether the project needs one, which is a decision rather than a substitution.
**To settle at processing.** Whether `launch.json` is deleted or repointed; whether the dead allowlist entries are pruned (harmless, but they make the file hard to read, and this user's stated difficulty is scanning dense lists); and whether anything else in `.claude/` assumes the old layout.
**Files (rough):** `.claude/launch.json`, `.claude/settings.local.json`. Host-only — a consumer's `.claude/` is their own.

#### The superseded-research flag cannot tell a citation of the fallen part from a citation of the surviving part [superseded-flag-has-no-section-granularity]
Observed 2026-08-13 while filing [written-deliverable-length-unaddressed], which cites `instruction-file-bloat-and-subtraction.md`. The digest flagged it correctly by its own rule, and for this item it was a false alarm.
**A `Superseded by:` line can say the file fell only in part, and this one does.** `instruction-file-bloat-and-subtraction.md` records that §1's instruction-count figure was re-validated and found roughly an order of magnitude too tight, and that its other sections "stand". The item that triggered the flag relies only on the subtraction argument, which survived.
**The flag has no way to know that, because it matches on the filename.** An item citing a surviving section is flagged exactly as loudly as one built on a fallen premise, and telling them apart needs a human to open both documents.
**Why this is worth more than a shrug.** A check that fires on correct work is the failure mode this project has named twice — at the repealed index-line cap, and in the standing rule that a check which over-claims makes the corpus look guarded when it's only partly guarded. The same applies to over-firing: a flag that is usually a false alarm gets learned past, and then the real one is skimmed too.
**The mitigation used this time, offered as a possible shape rather than the answer:** the item's prose now names which section fell and which it relies on. That's a convention, not a mechanism, and nothing enforces it.
**To settle at processing:** whether the fix is a convention (an item citing a partly-superseded file states which part it rests on), a format change (`Superseded by:` naming sections, and the digest reporting them), or nothing at all — the flag's text already says it is a prompt to re-read the premise rather than a verdict, so this may be working as designed. Weigh doing nothing seriously; it is a real candidate.
**Files (rough):** `plugin/throughliner/scripts/queue_digest.py`, and `skill-nonspecific-rules.md`'s superseded-research paragraph. Shipped.

#### Clearing a conversation does not cancel a slash command queued behind it, and nothing says so [clear-does-not-cancel-a-queued-command]
Filed 2026-08-13 by Claude at its own /done close. Captured by you in substance — you asked mid-run whether Claude had seen the `/clear` you ran from remote control, having reasonably read the clear as cancelling what followed.
**What happened.** A `/clear` and a `/next` were sent together. The clear wiped the conversation; the `/next` behind it ran normally against an empty context. From your side the old text was still on screen, so it looked as though the clear had been ignored — when it had been honoured exactly, and the scrollback you could see was the app's, not Claude's context.
**Why it is worth a queue line.** Nothing in the method or the app says a clear is a context operation and not a queue operation, and both readings are natural. The cost is real: a `/next` immediately after a clear starts a build with none of the planning conversation behind it — exactly the fresh-short-session case the method designs for, but only if the user *meant* it.
**To settle at processing, and the routing is genuinely open.** This may be Claude Code's to fix, in which case the destination is a GitHub issue rather than a build. What is plausibly ours is smaller: /next's opening could say, where the context is visibly empty of prior discussion, that it is starting cold. Weigh whether that is detectable at all first — Claude cannot reliably tell an empty context from a forgotten one, the same blindness recorded in the wind-down re-scan's caveat.
**Files (rough):** none decided. Relates to the fresh-short-session design target in `CLAUDE.md`.

#### There is no way to tell where you are in a long processing run [no-position-signal-in-a-processing-run]
Captured 2026-08-14 at a /plan close, from the user losing her place live. Her words across three turns: "what is going on did we resolve the last item into work or not", "in the middle of what item? what item are we on? that's all I'm asking", and "then what was all that stuff you just did!".
**What happened.** Ten items in one session. Each produced several turns of discussion, and several produced side-work — a reply drafted and delivered, a capture filed mid-item, a rule gate opened, references repaired after a delete. From outside, side-work is indistinguishable from work on the item, so a single-word instruction like "delete" was followed by four further exchanges and the user could no longer tell whether the item was resolved, what item was current, or whether anything was open.
**A running count is NOT the fix, and this capture's first draft had it backwards.** It claimed the count was stated once at the start and never again, and offered a running position line. The user corrected both at the close; her correction, rendered in Claude's words rather than quoted: the count was in fact being stated at random points through the run for no apparent reason, it has since gone, and it is better gone. Claude had been emitting unprompted tallies — "that's five items processed and two skipped" — at moments no procedure asks for, noise dressed as orientation. Recorded rather than quietly amended, because a running counter is the intuitive fix and would otherwise be re-proposed by the next session to read this.
**What is actually missing is narrower.** Not how many items, but whether the item in hand is finished and whether what Claude is now doing still belongs to it. All three of her questions were that question, never a request for a total.
**What to weigh at processing.** Whether side-work should be announced as side-work when it starts, so a stretch of tool calls after a one-word instruction reads as "still finishing the delete". Whether a plain "that item is closed" line at the moment an item ends would do it. Neither should reintroduce a tally. Relates to [concision-build-removed-the-asks], [subset-done-has-no-stated-shape] and [claude-md-vocabulary-is-unexplained] — all four are the user unable to read her own position from what the session says.

#### A user has no answer to what happens when Claude deletes something from their queue [no-faq-entry-on-deletion-and-recovery]
Captured 2026-08-14 at a /plan close, from the user asking mid-session what git history does and what was happening to her queue. She is the method's most experienced user and still had to ask.
**The gap.** Deleting a work item is a routine, approved planning move, and the method's own reasoning leans on deletion being safe because git history keeps the text. That premise is never explained anywhere the user reads. A non-coder approving a delete is being asked to agree that something isn't worth doing, with no way to know whether "delete" means gone.
**Why it is not covered.** The FAQ has entries on the workflow's moving parts, none on what deletion does or how anything is recovered. SPEC states that git history keeps a deleted item, but SPEC is product truth, not user help.
**What to weigh at processing.** Whether one entry covers it or two — deletion specifically, and the general "is anything I approve ever unrecoverable" — and whether the answer names a recovery command or simply says to ask Claude, which is the honest route for a user who doesn't use a terminal. Ships to consumers, so an ordinary FAQ entry rather than host-only. Relates to [own-faq-diverged-from-shipped-template] — decide which FAQ the entry lands in before writing it.

#### EDITING-STATE-CONTRACT.md has a live consumer, no maintenance trigger, and an unexamined justification [editing-state-contract-status]
Captured by you 2026-08-14, mid-/next, from your proposal to delete the file. Filed after the last committed close, so it belongs to no committed session record. Three questions, yours, kept together because they are weighed against each other.
**What was established before the questions, so they are not re-derived.** Your premise was that the document is vestigial material from when MANIFEST was a doc. It is not: it documents a shipped feature — `pre_tool_use.py` writes a marker before every editing-tool call and clears it after, `session_start.py` sweeps stale ones — and it has a live consumer. that consumer project's `src/main.js` (around line 264, under "Throughliner's editing signal") reads `.throughliner/`, scans every `editing-*.json` rather than one file, applies the published reader rule that editing is happening if any marker is active and fresh, and reads the `producer` field with `throughliner` as its fallback. An archived message in that consumer project's INBOX shows the v2 format change was communicated deliberately.
**But a live consumer does NOT put a delete off the table, which is your correction and it defeats this capture's first version.** Claude wrote that it did; you pointed out that what that consumer project has is *code* that reads the markers, and that that consumer project's Claude can read the hook that writes them. That is the stronger source in every respect: `pre_tool_use.py`'s marker-writing function **is** the format, so it cannot drift, while the document can and has nothing checking it — question 2 below. The document would only be load-bearing if that consumer project couldn't reach this repository, and it can: sibling folders on the same machine, and the v2 change in fact travelled by INBOX message rather than by anyone reading the contract. So a delete is live, and question 3 is now most of the answer.
Your other point stands untouched: users will not read it, and it is not written for them.
**Question 1 — does the dependency get to be visible from both ends?** Today the citation runs one way: this project publishes a contract and doesn't know who consumes it, and that consumer project's code names the format without anything on this side recording that it does. Same one-way-citation shape the superseded-research rule was built for, one project apart. A pointer from that consumer project's side, or a note here naming the consumer, would make a v3 change reach the code that depends on it. Weigh against the standing rule that this project doesn't scan other projects — any pointer is something a person writes, never something a session goes looking for. **This question survives a delete and may be the only part that does:** knowing who reads the markers matters whether the format is documented in prose or read out of the hook, and it's the one thing neither the code nor the document records.
**Question 2 — when does it get maintained, or is it quietly decaying?** Your question, put here in Claude's phrasing. There is no trigger of any kind: not in the rule gate's path list, not in the board's growth report, not in the FAQ-sync trigger, and no close reads it. The hooks could drift from the published format and nothing would say so — the exact shape of the output-style failure built earlier in this run, where an always-loaded layer sat outside every watcher and an underived number reached it in silence. Note a conformance check here is mechanically possible in a way most of this method's checks are not: the fields the hook writes are literal strings, so a test could assert the marker matches the document.
**Question 3 — is a published interface contract standard practice, or our own invention? This is now the load-bearing question.** Yours, and with the consumer objection defeated it carries most of the decision. If it is standard practice, defended by sources, it stays and gains a trigger. If it is our invention, it duplicates what is already in the repository in executable form — the hook code *is* the format, Claude can read it, and it cannot drift the way prose can — and this project has spent this session removing second copies. Your words for why the code is the better source: it is probably way more accurate too. **This turns on an external fact, so it needs a web search rather than a judgement here** — whether published field-level contracts for local file-based signals are a recognised practice, and what maintains them where they are.
**Files:** unknown until question 3 is settled — possibly `EDITING-STATE-CONTRACT.md` (deleted, or gaining a maintenance trigger), `CLAUDE.md` and `resources/rule_signals.py` (if it gains one), `resources/testing/` (if a conformance test is the answer). Host-only in every branch. Relates to [rule-lifecycle-board-has-no-trigger] and to the superseded-research one-way-citation problem.

#### The slug in a work item's heading appeared with nothing ever explaining it [slug-never-explained-to-the-user]
Captured by you 2026-08-14. Your point, rendered in Claude's words rather than quoted: you have never actually known what the bracketed part of the title is for — it just randomly emerged one day and you didn't have time to deal with it.
**The gap.** The slug is load-bearing structure: it is what `Blocked by:` resolves against, what the queue lint checks, what a LOG entry names to say which item it built, and what Claude uses to refer to an item exactly in chat. None of that is stated anywhere the user reads. It appeared in their own documents and they worked around it for weeks.
**Why this is not solved by the slug being harmless to ignore.** It is harmless to ignore only once you know you may. Until then it is unexplained structure in a document the user is asked to read and approve, and the method's own standard is that unreadable is unapprovable.
**The likely shape, to settle at processing.** Either the queue file's header sentence gains a clause saying what the bracketed name is for and that the user never has to write one, or it becomes an FAQ entry, or both. The queue header is read by anyone who opens the file, which the FAQ is not — so the header is the stronger site and the FAQ the fuller answer. Depends on [faq-entry-criteria] if the FAQ route is taken.
**Files (rough):** `plugin/throughliner/docs-b/setup.md` (which authors the queue header) and the queue header text itself; possibly an FAQ entry. Shipped — every consumer meets the same unexplained brackets. Relates to [faq-entry-criteria].

#### The two-limb keep check pushes research into build items, beating the rule that says research is done in planning [research-packaged-as-build-work]
Captured by you 2026-08-14, from a live instance in another project minutes earlier: a planning session proposed splitting an item into "one build item where I do the research and write the findings into `resources/research/`" plus a slimmer `[user]` line. Your framing is the finding — research is never planned into work items, and if research can be done now in /plan then it is. **You also observed this is suddenly happening a lot, which is what the diagnosis below explains.**
**It happened three times in one day.** Twice in this session — research queued into [faq-entry-criteria], and research folded into [shipped-spec-maintenance-rules] — and once in the other project. Both of this session's instances were corrected on your instruction; the SPEC one needed no research at all, because `resources/research/spec-document-standards.md` already answered it.
**Nothing was deleted, and the rule is intact.** `plan.md` still carries "/plan resolves what it can in-session; capture is only for what it can't", with `research` listed first among what /plan resolves now. The defect is not a missing rule.
**Three things make it lose, and the third explains the timing.** It is not stated as a rule about research — it is one word inside a fenced list of six, so "research belongs in planning" must be inferred. It is hedged by the sentence immediately after, "A default, not an absolute", a standing licence to make the exception. And the keep-check pushes the other way with far more force.
**The mechanism, which is this capture's substance.** To keep an item, `plan.md` requires stating the build in both limbs — which files change, what changes inside them — and calls it blocking. When the answer isn't yet known, the cheapest way to pass both limbs is "research X, then change Y", which reads as a fully specified build. So the check that exists to keep undesigned work out of Processed is the same check that rewards packaging research as build work. It fires hardest exactly where the answer is unknown, which is where research is needed.
**The timing, confirmed from git rather than assumed.** The two-limb check was hardened 2026-08-10 in `f8b03ea`, which introduced "This is a blocking check, not a prompt to try harder", the instruction to state both limbs before recommending keep, and the warning that a bare file list is what undesigned work looks like. Before that it existed in a softer form; after it, a keep can be refused. Four days later the pattern is visible across projects. An earlier `git log -S` attributed the change to `989c38b` — a false positive, since `989c38b` is the rename that moved the whole package folder and shows every string as newly added. Recorded so the trace isn't run twice with the same wrong result.
**What this is not.** Not a case for weakening the keep check. It stopped undesigned work reaching Processed, a real failure with real instances. Two correct rules were put into conflict and the stronger won.
**The shape of the fix, to settle at processing.** The clause belongs on the keep check itself, where the pressure lands, not on the research bullet, which is already there and already ignored: an item that cannot state its build *because the answer is not known yet* routes to doing the research now, in this session, and only what /plan genuinely cannot resolve is captured. Weigh also whether "A default, not an absolute" should go — it is the sentence that licenses the exception, and by this project's standard a rule qualified into a default loses every contest.
**Files (rough):** `plugin/throughliner/docs-b/plan.md` — the keep-check sub-step, and the resolve-now block's hedge. Shipped, not host-only: this fires in every consumer's planning session, and the prompting instance was in another project.

#### The Claude Code GitHub app cannot be installed for an org from the flow that demands it [claude-code-github-app-org-install-dead-end]
Filed 2026-08-14 by Claude at the wind-down re-scan. **The observation is the user's, from hitting it live while trying to start a cloud session; the diagnosis is Claude's.**
**What happened.** Starting a cloud session against an org-owned repository popped "GitHub app not installed — the Claude GitHub app must be installed on your repository". The app *was* installed, on the user's personal account. Its "Install GitHub app" button led to the personal account's app settings page, which offers no route to install for the organisation that owns the repo. The org's installed-apps page showed none, and the GitHub Marketplace returned no results for Claude Code. The only working route was the direct URL, `github.com/apps/claude`, which nothing in the flow mentions.
**Why it is worth reporting rather than just fixing locally.** A non-coder hits a popup that contradicts their settings page, follows the button it offers, lands somewhere that can't resolve it, and has no next step. The user is a non-coder and did stop. By the three-way routing test this is Claude Code itself, so it belongs as a GitHub issue on `anthropics/claude-code`, not as a method capture and not as app work.
**What the work is.** Search existing issues first — knowing the adjacent reports is what lets a new one distinguish itself — then draft the issue and show the exact text before anything is posted. Nothing is filed without the user's explicit yes. The account and repository names are identifying and are scrubbed or generalised in the draft.

#### A file's date in Google Drive means "last synced", not "last edited", and both you and Claude reasoned from it as if it meant edited [drive-dates-are-not-edit-dates]
Captured by you 2026-08-14 at the /done close. **The observation is yours** — you reported that two folders had both been updated today and asked which was real; **the diagnosis is Claude's.** Filed after the last committed close, so it belongs to no committed session record.
**What happened.** You read the project through Google Drive on your phone, saw `docs-b/` and `skills/` both showing as modified today, and reasonably concluded both were live. The filesystem and git disagreed: `skills/` was last written 2026-08-13, three of its four files on 2026-08-10, with no modification in git and no commit since the rename build. The whole project sits inside My Drive, so a sync pass or re-upload refreshes what Drive displays without any byte inside the file changing.
**Why this is a method finding rather than a one-off.** You work from Drive on your phone routinely, so it will recur, and it produces a report that is honestly made and factually wrong — the worst kind for Claude to receive, because nothing about it looks uncertain. Claude then took it at face value and answered the wrong question twice before checking the filesystem, costing several exchanges and visible frustration. The general shape: **a file browser's presentation is not evidence about a repository's contents, and both parties treated it as if it were.** Third instance in one session, after `throughliner.zip` looking live in Explorer and again looking dead to the fix.
**The likely fix, to settle at processing.** Something small on the handoff-claim provenance rule, which covers Claude-authored claims but not user-reported file state: where the user reports that a file changed, was updated, or looks new, check `git log` and the filesystem before reasoning from it — and say what was checked rather than contradicting her flatly. Weigh whether this belongs in the always-loaded rules or in this project's CLAUDE.md, since it is about how *this* user works. The asymmetry is what makes it worth having: checking costs one command, not checking cost this session several exchanges.

#### A working file's `Depth:` lines are not bound to their items, so two written together silently attach to the wrong one [depth-field-has-no-binding-to-its-item]
Filed 2026-08-14 by Claude at the /done close, from a slip in this session's own build working file. Filed after the last committed close, so it belongs to no committed session record.
**What happened.** The `Depth:` field is written under an item's Progress tick, and its binding is positional — nothing names the item it describes. Two items were ticked in the same edit and their depth lines landed together, so `[setup-mid-session-is-unhandled]` carried two and `[spec-ask-in-build-reads-as-a-violation]` carried none. The close spotted it and read the second line as belonging to the second item, almost certainly right — but that was a reconstruction from context, not something the file recorded.
**Why it matters more than it looks.** `done-build.md` instructs the close to read each item's depth field rather than judge it, and to treat a missing field as short while noting the omission as a discipline slip. Both are defeated here: the field wasn't missing, it was misattached, so "missing means short" would have written the wrong form of entry for one item and the slip would have been reported against the wrong cause. A fresh short session — the design target — has no conversation memory to reconstruct from and would simply have believed the file.
**The likely fix, to settle at processing.** Bind the field to its item explicitly — `Depth: <slug> — short` — so position stops carrying meaning, the same principle the queue applies in refusing to let position encode a relationship. Weigh the cheaper alternative of instructing the close to flag any item whose depth-line count is not exactly one, which detects the fault without changing the format. Relates to [tick-conflates-built-and-confirmed] and [close-cost-scales-with-run-size].

#### An outbound report can describe a problem that was fixed days earlier, because nothing requires a live check before sending [outbound-report-not-checked-against-the-world]
Filed 2026-08-14 by Claude from inbound INBOX mail (`2026-08-14-report-page-already-live.md`), opened and archived during a /next pre-flight. Filed after the last committed close, so it belongs to no committed session record.
**What the message says.** The flintcraft.tech project reports that `flintcraft.tech/report` has been live and working since 2026-08-06, when the site was connected to Netlify — and that two invisible Netlify defaults had to be fixed alongside it (form detection off by default since April 2023, and no email notification unless configured). Its correction: a report this project sent was dated 2026-08-09, three days after the fix, so it described a problem that no longer existed.
**Why it is a method finding rather than a one-off.** `[report-url-404]` was closed correctly on 2026-08-10 by fetching the URL — check-the-world working as designed. The gap is *outbound*: the walk-through lifecycle requires an observable check before recording a `[user]` item complete, but nothing requires the same before sending a report to another project. So the strong rule guards closing work and the weak path guards sending claims, which is the wrong way round: a wrong close costs one queue line here, a wrong outbound report costs another project's time.
**The likely shape, to settle at processing.** One clause on the outbound-send flow in `feedback-and-inbox.md`: where a report's claim has an observable check — a URL, a file, a branch — run it at drafting and say in the report what was observed and when. Weigh whether this is the walk-through's check-the-world clause extended to a second site, in which case it's an amendment and spends no slot.
Relates to [cross-project-work-completes-invisibly] (the same blindness in the other direction) and [report-url-404] (the instance).

#### A reversibility claim settled at processing was never checked against the world, and the build hit the exception [processing-asserts-reversibility-without-checking]
Filed 2026-08-14 by Claude at its own /done close, as a testing outcome from using the plugin to build the plugin. Host-only in its example, general in its shape.
**What happened.** [delete-codex-port-from-history] was settled at processing with a careful paragraph choosing the cheap operation over a history rewrite, recording that the cheap one "is also the reversible one" because dropped commits stay recoverable from the reflog until garbage collection. True of commits. The worktree being deleted held 722 lines of uncommitted work across 24 files plus two untracked files, none of which is a commit and none of which the reflog holds. The build halted, surfaced it, and the user chose to discard the work after being told plainly it couldn't be recovered.
**Why the processing session could not have known, and why that is the point.** Nothing in the keep-step asks a session to look at the thing it is about to destroy. The two-limb test asks whether the item says what changes inside the files it names — which this item did, precisely. A reversibility claim is a claim about the *world*, not about the item's specification, and the method has no check that reaches it.
**The shape it shares with other findings here.** [runs-alone-premise-never-tested], built in the same run, is the same failure one layer up: a plausible sentence about what git would or wouldn't recover, written at processing, quoted forward for days, refuted the moment anyone tested it. Two instances now, both about git recoverability.
**To settle at processing, and the obvious fix may be too broad.** A rule requiring every destructive item to inspect its target before clearing would fire on a great deal of work that destroys nothing. Weigh a narrower trigger: an item whose own prose *asserts* that an operation is reversible or recoverable earns a check of that assertion before it clears. That keys on something visible in the text rather than on judging what counts as destructive.
**Do not read the build's halt as the system working.** It worked because the build happened to run `git status` in the worktree before removing it, which no step required.

#### A halt written for a non-coder used four pieces of jargon in its first sentence [halt-narration-used-unexplained-jargon]
Mixed authorship: the failure was Claude's, and you reported it in your own words — "I don't understand". Filed 2026-08-14 at the /done close, as a testing outcome.
**What happened.** A build halted to surface that a folder about to be deleted held unrecoverable work. The message opened with "the Codex port worktree has uncommitted work in it", then used *reflog*, *commits*, and *branch ref*, and offered three options in the same vocabulary. You said you didn't understand it. The second attempt — the same decision explained as "a second working copy of this same project, sitting next to it", with the loose edits existing "only as loose files on your disk" — was understood immediately and you decided in one turn.
**Why the guard did not fire.** The always-loaded vocabulary rule asks whether a term names something in *this user's* world, something you could show them. In a project whose subject matter is the method, that resolves generously — a worktree genuinely is a folder that can be opened. So the rule permitted every term. What it doesn't weigh is that a *halt* is the one moment the user has no context to lean on: the run stopped, something is wrong, and a decision is needed immediately.
**The shape to weigh at processing.** Possibly a clause on the vocabulary rule: text written at a halt or stop states the situation in terms needing no method vocabulary, because a user meeting a halt is being asked to decide rather than to follow along. Weigh against the risk of a rule that fires on every alarming-sounding moment.
**The cost was one extra turn**, which is cheap. The reason to file it anyway is that a consumer meeting the same halt has strictly less context than you do, and no way to ask a question that gets a second attempt from someone who knows the material.

#### Design the standing audit set that maintains the rule corpus once the cleanup is finished [standing-audit-programme]
**Captured by you 2026-08-14. Your instruction, rendered in Claude's words rather than quoted: design the routine audits that you will run in the future and maintain the full corpus once we're done.** The reasoning below came out of that discussion — your strategy is yours, the argument about what it can and cannot retire is Claude's, and you asked for it to be captured.

**Your strategy, recorded first because the design serves it.** Dedupe and de-contradict the corpus first, cutting the word count and therefore how much there is to process; then design the audits and edits that put the final finish on the method rules, converting them into the law-prose style; then, once the always-loaded self-authoring rules are doing their job, stop needing to run these audits at all.

**The sequencing is right and is not what is being questioned.** Deduping before restyling is correct: a restyle over a corpus holding four copies of one rule restyles it four times and creates four chances to diverge. Cutting first means each rule is rewritten once. The `done-plan.md` merge processed the same day is that shape in miniature — four items, one file, one judgment applied consistently, where deciding them apart would have answered the same question four times inconsistently.

**Where the strategy overreaches: the self-authoring rules govern ADMISSION, and audits catch DRIFT. Different jobs.** Admission asks whether a rule should exist, worded this way, in this file — it fires when someone is writing a rule. Drift is what happens to a correctly-admitted rule *afterwards*, when something changes around it and the rule is left describing a mechanism that no longer exists. **No admission gate can prevent drift, because the cause arrives after admission.** Three items in the queue at writing are pure drift and every one passed admission cleanly: [done-md-names-a-repealed-clear-step], [adopted-claude-md-describes-retired-structure], [docs-b-name-outlives-the-two-docset-model]. A perfect gate produces all three anyway.

**The harder evidence: correct wording does not make a rule fire.** The corpus documents at least four instances of an always-loaded, correctly-worded rule failing: the provenance rule, shipped and sharpened, still not holding ([invented-rationale-compounds-past-the-shipped-rule]); the file-the-blocker rule, unambiguous and explained by the user five to ten times in a month ([nothing-blocks-it-read-as-a-dead-end]); the INBOX-opening step skipped in the very session that authors it ([inbox-open-step-not-enforced]); and the subagent-cost rule broken hours after being read. The provenance item already draws the conclusion: "state the rule again, or state it harder" is no longer a candidate direction.

**The rule board is this experiment already run.** Built on the theory that the rules could watch themselves, it reported clean while five real rule defects shipped in the same session — see [rule-board-measures-paperwork-not-health], settled the same day as keep-and-rename for that reason.

**What the strategy genuinely buys, which is substantial.** Fewer rules and no duplicates means fewer sites where drift can occur, and each future retirement ripples to fewer places. An audit over a deduped corpus costs a fraction of one over the corpus as it stands. The win is real; it is a change in cost, not in necessity.

**So the goal is reframed rather than abandoned: not eliminate the audits, but make them cheap enough to run routinely without dreading them.**

**The design test this item applies, and it is the actionable part.** What retires an audit class is a **mechanical check, never a prose rule.** The queue lint and the digest genuinely removed the need to eyeball queue structure, because code reads the whole file and cannot skim. So for each drift class, ask first whether it is mechanically detectable: if yes, build the check and retire the audit; if no, the audit stays and gets a trigger. The board's retired-terms check is an existing instance of the first kind.

**What this item must produce.** The standing set itself — which audits, what each reads, what triggers each one, and how the user runs it without needing to remember it exists. A siteless audit is the failure this project has now recorded five times.

**One risk to design around.** The law-prose restyle is itself a large authoring pass over the whole corpus, and every rewrite is a chance to reintroduce what was just cut. It should be the last big pass and should be audited *after* rather than trusted to verify itself — the party doing the restyling is the party that would certify it, which is [rule-admission-has-no-independent-approver].

**The finish line this set takes over from is already assembled**, in the session that captured this item: twenty-two remaining items in five groups plus [law-prose-restyle], with five stated finish conditions. It lives in that session's LOG entry rather than in a queue item, because it is a record to be read rather than work to be done.

**Two of the five finish conditions are already mechanically checkable** by `resources/rule_signals.py` as it stands — no live rule naming a retired term, and no near-duplicate rule pairs. That is this item's own design test paying off before the design starts: the standing set inherits two conditions it never has to audit by hand, and should look for more of the same before proposing any audit a script could do instead.

**The comparison axis is split out and settled — see [audit-axis-is-parent-not-sibling].** It was the one fully designed part of this item, so on 2026-08-15 it was split off and kept into Processed on its own: audits compare a doc against its parent rather than its sibling, and each finding names where both sites fire. That half needs nothing further from this item; the standing set inherits it as a constraint every audit it designs must satisfy.

**Not kept, 2026-08-15, and why — this is design progress rather than a rejection.** The item fails the keep check's second limb by construction: its file list is whatever its own design produces, so it can never clear to run and a build would stall on it. It also should not be designed yet on its own reasoning — the set is meant to follow the dedupe and the restyle, and audits designed against a corpus about to be rewritten are audits designed against a shape that will not exist. **The user's decision was to split rather than design it now.**

**What remains to be designed, so the next session starts here.** Which audits are in the set; what each one reads; what triggers each one, given that a siteless audit is the failure this project has recorded five times; and how the user runs the set without having to remember it exists. Each candidate audit is tested first against this item's own rule — is the drift class mechanically detectable? If yes, build the check and retire the audit rather than designing it. Two of the five finish conditions already pass that test using `resources/rule_signals.py` as it stands, and the design should look for more of the same before proposing any audit a script could do instead.

**Files: not yet derivable, which is the point of not keeping it.** Likely `resources/method-compliance-audit-checklist.md`, `resources/rule_signals.py`, and `CLAUDE.md` for whatever trigger the set gets. Host-only. Relates to [rule-admission-has-no-independent-approver] for the restyle-audits-itself risk.

**Skipped again 2026-08-17, and the blocker it waits on now exists as work.** It was presented by the ladder as the longest entry in the section. Rather than skipping it silently a second time, the decision it was actually waiting on was put to you: whether the restyle stops at the one file it covered this morning. **You decided it continues to the rest of the corpus**, so this set still follows a rewrite that has not happened — and audits designed against a corpus about to be rewritten are designed against a shape that will not exist. It follows [law-prose-restyle-heavy-docs] and then [law-prose-restyle-remaining-docs]; the ordering is written into those entries too. [law-prose-restyle] is consumed and no longer names anything in the queue, which is why it is no longer cited above. The second limb still fails by construction, so this stays a capture rather than being held below the line.

#### SPEC does not say how many commits a close makes, now that the answer is exactly one [spec-silent-on-one-commit-per-close]
Filed 2026-08-14 by Claude during the build of [close-produces-multiple-commits-every-time], as adjacent work rather than folded in.

**What the build settled.** A session makes exactly one commit — the close — and the post-commit tail commits nothing, riding into the next close. The accepted cost is that the working tree is dirty between one close and the next, always, which is what makes that dirt legible rather than noise.

**Why this is a capture and not part of that build.** Nothing in SPEC becomes false: its close paragraph says the close records and commits, and says the append offer exists, without claiming a commit count or a clean tree. So there is no contradiction to halt on and no stale sentence to correct — only an addition. The build's file list named `done.md` and the session-start hook, and adding product truth is the route that asks first, which would have stopped an unattended run for a sentence nobody is blocked on.

**What a keep would decide.** Whether the commit count and the expected-dirty-tree are product truth a consumer should read in SPEC — they will see the "uncommitted changes from a previous session" line at every session opening, and SPEC is where they would look to find out whether that is normal — or whether it is implementation detail belonging only in the close procedure. Relates to [close-produces-multiple-commits-every-time], [post-close-tail-state] and [close-cost-scales-with-run-size]. [done-delta-close] was deleted 2026-08-17 as already decided against in `done.md`, so it is no longer a relative; [rescan-appends-post-close-work] is the surviving piece of that subject.

#### A build authored a shipped rule and wrote its own gate disposition, which is the thing the gate's design says cannot work [build-wrote-its-own-gate-disposition]
Filed 2026-08-15 by Claude at the close of the eighteen-item run, from a live instance in that run.

**What happened.** [close-produces-multiple-commits-every-time] was processed as a decision about *which item runs and when*, so its `Rule gate:` line honestly said "not needed at processing" and told a build that found itself authoring a rule to halt and say so. The build then did author a rule in shipped text — one commit per session, the post-commit tail commits nothing — because that is precisely what the item's body instructed it to decide. Rather than halting, the build ran the gate's four questions itself and recorded the result, flagging it in the working file and in chat.

**Why this is worth filing rather than treating as handled.** `CLAUDE.md` states the case against exactly this: a disposition written as an item is built is written after that item's rules were designed, so it improves attribution and restores no power to refuse. Refusing would have meant undoing finished work. So that build's disposition is a description, not an admission decision — the failure mode the /plan siting exists to prevent, reproduced by an item whose planning honestly could not foresee it.

**The shape of the gap, the general finding.** An item can be processed as a scheduling decision and still be specified to *decide a design* at build time. For that class the gate has no site: planning has nothing to run the gate against, and the build cannot refuse. Neither the halt instruction nor the transcribe rule reaches it — the build halting would have stopped a run over an item doing exactly what it was told.

**What a keep would decide.** Whether such an item must be split — a planning item that decides the shape, then a build item that implements it — or whether the gate acquires an explicit build-time branch honestly labelled as description rather than admission. The first preserves the gate's power to refuse and costs a round trip; the second is cheaper and concedes the ground. Relates to [rule-admission-has-no-independent-approver], [rule-gate-has-no-site-in-next] and [close-produces-multiple-commits-every-time].

#### A processed item carried its `Rule gate:` line twice, the second a truncated copy of the first [duplicate-gate-line-on-a-processed-item]
Filed 2026-08-15 by Claude at the close of the eighteen-item run, noticed while transcribing.

**What was found.** [move-section-does-not-report-line-crossings] carried two consecutive `Rule gate:` lines. The first read "not needed — this extends an existing report to a second code path and adds a refusal branch"; the second, the same without the refusal clause — evidently an earlier draft left in place when the item was revised. The build transcribed the fuller one once.

**Why it is worth a line.** The disposition is what two of the corpus checks read, and both take the line as authored. Two lines disagreeing about what the build does is a small inconsistency now and a wrong reading later — the truncated copy describes a narrower change than the item specified. It also suggests revision passes over a processed item append rather than replace, which would produce this again.

**What a keep would decide.** Whether anything mechanical should notice a duplicated disposition — the queue lint is the natural site and already parses work-item structure — or whether one instance is below the bar and this is a note about revising items in place. The bar question is real: one occurrence, which this project's own gate treats as insufficient for a freestanding rule.

#### The scaffolded "Project docs" section in every consumer SPEC describes the method's own machinery, and goes stale in a way no migration repairs [spec-scaffold-describes-method-docs]
Filed 2026-08-15 by Claude, from INBOX mail sent by a consumer project running this method running 1.20.0-test7. Their user noticed it unprompted while reading her own SPEC and asked why SPEC described the workflow's files rather than her product; they filed it without proposing a fix and said no reply was needed.

**The admission point.** `setup.md`'s SPEC scaffold writes a `## Project docs` section into every new SPEC.md, listing what SPEC, QUEUE and LOG each hold. plan.md's SPEC admission rule says a sentence describing how a mechanism is implemented belongs in the doc that owns it, and that SPEC names the behaviour instead. So the scaffold writes into every consumer's SPEC exactly the kind of sentence the rule governing SPEC edits forbids. Whether that section earns its place is the question; the sender proposed no answer.

**The staleness point, which the sender judged sharper and which is invisible from here.** That section copies how QUEUE.md is structured, and QUEUE.md's structure is what changes between format epochs. Theirs read "work batches and captured ideas" — the pre-recut shape — and had since the two-section change. They ran the format 2→3 migration and it correctly did not touch the line, because migration adds missing files rather than refreshing existing content. So the stale description survives every migration by design, in every consumer project, in the one document sessions are told to read as product truth. Theirs is now corrected by hand.

**Why it needs planning rather than an obvious patch.** Three candidate answers, not equivalent: drop the section from the scaffold; keep it but reduce it to behaviour rather than structure; or give the migration a refresh path for scaffolded content, which is a new capability rather than a wording fix. The first two are cheap and the third is not.

**A related check when this is processed:** whether anything else the scaffold writes has the same shape — content copied from the method into a consumer document, where the method can change and the copy cannot be reached.

#### The plan/build boundary keeps being treated as an open question across the last two planning sessions [plan-does-not-build-keeps-being-relitigated]
**Captured by you 2026-08-15, in your own words: "I don't know why this is even a question. Plan does not build. This confusion has been happening a lot in the last two plan sessions. I don't know what rule slipped in the build before that but it might need to be investigated."**

**What triggered it.** Processing [rescan-as-its-own-skill], Claude presented "does the new skill build its findings, or only file them?" as a genuinely open design question needing your decision. It is not open — the boundary is stated in the always-loaded rules, in plan.md's opening line, and in the work cycle itself. You spent three exchanges, including two where you said you did not understand the question, to get back to an answer the rules already gave.

**One concrete lead, so the investigation does not start from nothing.** The framing did not come from Claude in this session — it is written into [rescan-as-its-own-skill]'s own prose, authored yesterday, as a paragraph headed "the hard question this must answer" saying the resolution "is not obvious" and that the boundary might be "deliberately amended". A queue item authored in one session taught the next to treat a settled rule as undecided. Worth checking as a pattern: whether other items carry a settled rule re-opened as a question in their prose.

**The second thing to check is what you named** — whether something shipped in a recent build weakened the boundary's statement, or added a rule reading as an invitation to exceptions. That is a read of what changed in the always-loaded rules and the skill docs over the last few builds, against LOG.

**Why this matters beyond the wasted turns.** A boundary that gets re-argued eventually loses one of the arguments. The method holds this one firmly on purpose: it is what stops any session changing the project without the user having agreed to the work.

#### A rule-holding file sits outside the gate's trigger, so editing it summons no gate at all [gate-trigger-misses-the-audit-checklist]
Filed 2026-08-15 by Claude while writing a gate disposition, and raised with the user before writing.

**What is wrong.** The rule gate's trigger is mechanical and reads staged paths: a commit touching `plugin/throughliner/docs-b/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md`, or `CLAUDE.md`. `resources/method-compliance-audit-checklist.md` is not in that set, and its entire content is rules — the standing criteria every method compliance audit runs against. A session adding a criterion to it authors a rule, and nothing asks it to run the gate.

**How it surfaced.** [audit-axis-is-parent-not-sibling] adds two requirements to that checklist. Its gate ran because the session happened to notice; it would not have fired from the trigger. That is the failure this gate's design is against — a check depending on someone remembering is the shape the mechanical trigger replaced, and `CLAUDE.md` says so when it contrasts this trigger with FAQ-sync's undetectable one.

**To settle at processing, because the obvious fix may be wrong.** Adding the one path is a two-word change and closes this instance. The prior question is whether the trigger set should be a list of paths at all, given that a rule-holding file added later lands outside it again by default and nobody notices — exactly as this one did. A rule about which files hold rules has the same maintenance problem as the rules themselves. Whether there is a shape that fails safe rather than silent is the design question; if not, add the path and say so.

**Also worth checking in the same pass:** whether any other file under `resources/` holds operative rules and sits outside the trigger. `retired-terms.md` and `rule_signals.py` are the obvious candidates, and both may turn out to be data and code rather than rules.

#### Claude keeps writing two-column fenced blocks that wrap into nonsense on the user's display [two-column-fences-wrap-unreadably]
Filed 2026-08-15 by Claude at the close's re-scan, from an instance it caused in this session.

**What happened.** The rewritten ladder was presented as a fenced block with a label on the left and its explanation in a right-hand column. On the user's display the right column wrapped underneath the left, so the two ran together and half the rungs appeared to have no title. **Her words: "there's no title on half of them. what do they mean."** The content was fine; the layout destroyed it, and a second message in plain lines fixed it immediately.

**Why this is a capture rather than a one-off slip.** The corpus already contains [fences-wrap-so-prose-rule-reason-is-false], so the wrapping behaviour is known here — and the block was written anyway, in a session with that item in view. The shipped docs are also full of this format: `skill-nonspecific-rules.md`, `plan.md` and `done.md` all use two-column fenced blocks heavily, and Claude reads them at every session start, which is the likeliest reason it keeps reproducing the shape in chat.

**The distinction that matters, and what a fix has to get right.** A two-column block inside a procedure doc is read by Claude, in a wide view, and works. The same shape emitted *to the user* is read on whatever display they have. So the rule is about output, not about the docs — a fix that reformatted the procedure docs would solve the wrong half.

**To settle at processing.** Whether this is a rule about chat output ("structured content shown to the user goes one item per line, never in aligned columns"), or whether it is already covered by the existing item and should be folded in. Check that item's actual subject first — its title is about a prose rule's stated reason being false, which may be a different concern wearing the same word.

#### No test asserts that an origin claim goes unflagged, which is the whole of the provenance split [origin-claim-has-no-test]
Filed 2026-08-16 by the build of [provenance-splits-origin-from-quote], as adjacent work rather than part of it.

**What the suite covers and what it misses.** `resources/testing/test_queue_lint_flags.py` has four cases on the credit check, and all four survived the split untouched because each happens to use a quote-claim phrase alongside its `Captured by you`. So the suite still passes and still asserts only the half that did not change.

**The half that did change has no case at all:** a bare `Captured by you` with nothing quoted must now produce no warning. That is the entire point of the split — it is what stops Claude asking the user to prove her own work is hers — and a later session could restore the old phrase list with every test still green.

**Files:** `resources/testing/test_queue_lint_flags.py` — one case asserting a bare origin claim is not flagged, and one asserting a quote claim still is.

#### SPEC states the reading position more strongly than the user expressed it, and no capture records where that came from [spec-overstates-the-reading-position]
Raised by you 2026-08-17, when Claude quoted SPEC's sentence back at you as though it were settled. **Your response: that the design is "never lowered" to someone who will not read is a widening of what you expressed at the time.**

**What SPEC says today.** That the method is built for someone willing to read and approve the record, that someone who will not read is considered but is not the target, and that **the design is never lowered to them** — a workflow built around its own expected non-compliance having nothing left in it.

**Why it matters rather than being a wording quibble.** That sentence is product truth in the opening section, so it shapes what every session builds. If it states a stronger position than you hold, work gets scoped against a stance you did not take — and it is attributed to you by placement, since SPEC is your product's truth.

**The LOG search you asked for was run 2026-08-17, and it found nothing to recover.** Grepping `LOG/` and `resources/` for the sentence and its ideas returns exactly one file — `LOG/2026-08-17-chat.md` — and the only thing it records is **your correction itself**, listed among that session's corrections: that "the design is never lowered to them" widens what you expressed. **So there is no earlier capture, entry or finding in which the needs of non-reading users were considered and deliberately set aside.** The sentence sits in SPEC's opening with no recorded derivation at all.

**That changes the disposition rather than merely informing it.** Narrowing the sentence discards no decision, because none was recorded — and a positioning claim with no provenance, attributed to you by sitting in your product's truth, is the same defect as an unsupported user-credit one document over.

**What remains is yours alone: the position in your own words.** Claude cannot author it, and a guess written into SPEC would repeat the original fault.

**Skipped 2026-08-17 on your instruction, and what it is missing is named rather than left implicit.** You gave a worked example two sessions ago that made this concrete, and it is gone — not in the queue, and not reached by the phrase search above, which looked for the SPEC sentence's own wording rather than for the example. **So what would settle this is that example or a replacement for it, and it is yours to supply; the analysis above cannot substitute for it.**

**Where to look for it, recorded here rather than filed as its own item on your instruction.** Your correction to the SPEC sentence is logged in `LOG/2026-08-17-chat.md`, among the corrections for the `dc52025` session — so the example was given in that session or the one immediately before it. **The retrieval is yours: reopen that conversation and ask.** The raw transcript is also readable at `.claude/projects/<project-slug>/*.jsonl` if the conversation itself is gone, which is the route this project's own notes describe for reading a session back.

**One thing not to repeat: a session reaching for the nearest recorded stance of yours from an unrelated item and offering it as an analogue.** That was done here and removed at your correction — it imported an irrelevant position and made the item read as though the question were half-answered.

#### The build working file's Changes section falls behind its ticks, and only the ticks are enforced [changes-section-falls-behind-the-ticks]
Filed 2026-08-17 by Claude at its own close, from the reconcile against memory that `done-build.md` requires.

**What happened.** Across a twenty-six-item run, every item was ticked with a depth field and an index-entry candidate at the moment it completed — those three are named at the per-item completion step and all three held. The `Changes:` section did not: it carries per-file notes for roughly the first three items and the end-of-run summary, and almost nothing for the twenty in between. The gap was found by the close's reconcile, not by anything mechanical.

**Why the two behave differently.** The tick, the depth field and the index candidate are enumerated as a numbered set at one step, and the close reads each of them — a missing depth field is explicitly called a discipline slip. `Changes:` is described in `next-build.md` under "accumulate close notes as you go", with no step that reads it back and nothing that notices when it is thin. It is the one part of the working file whose absence costs nothing at the moment it is skipped.

**What it costs.** `done-build.md` sources each entry's `Files touched:` line from this section. With it thin, the close reconstructs the file list from memory of the run — which works in a chat that still remembers, and is exactly what fails in the fresh short session this method designs for. A crash mid-run would have left a working file that understates what was done.

**What to weigh at processing.** Whether `Changes:` joins the per-item completion set as a fourth required write, which is the shape that already works for the other three; or whether the close should read it against the ticks and flag a mismatch, which catches it later but costs nothing during the run. The first is more writes in the run, the second is a check at the one moment the information is already being reconstructed.

**One thing not claimed:** nothing was lost this time. The entries were written from a chat that still held the run, so the record is accurate — this is a defect in what the file would carry for someone else, found because the reconcile asked.

#### /setup can leave SPEC, QUEUE and LOG gitignored, and three rules resting on git recoverability go silently false [gitignored-core-docs]
Filed 2026-08-18 from INBOX mail sent by a consumer project running this method.

**What happened there.** A planning session ran to completion — a red flag cleared, three SPEC edits, eight work items, nine captures — and staging at the close revealed `.gitignore` carried `SPEC.md`, `QUEUE.md` and `LOG/`. The adoption commit's own message says it wrote SPEC.md as product truth; that commit contains no SPEC.md.

**The check that misses it.** Setup tests that a present `.gitignore` carries a `.throughliner/` line, and `setup.md` already admits "an existing `.gitignore` counts as present however little it contains". Nothing checks the inverse — that it does not contain something fatal.

**Three rules were false for that whole session.** Write-first, whose stated test is whether the previous version is recoverable without the user. The queue-states rule that a deleted item is kept by git history. And `done-plan.md`'s `git diff HEAD -- QUEUE.md`, which returns nothing, so the close's mechanical record of its own work is empty and falls back to memory — the exact substitution that command was chosen to prevent. Sharpest instance: a red flag's clearance and its informed-consent trail went into an untracked file.

**And the close deadlocks.** Removing the lines is the fix and a planning session cannot do it: the scope-lock refuses `.gitignore`, correctly by its own rule, and the close marker's permitted list omits it too. It became a `[user]` line — a non-coder hand-editing `.gitignore` mid-close.

**Their suggestions, offered as a consumer rather than a designer:** assert the negative at setup, notice before the close rather than at staging, and weigh `.gitignore` for the close marker's list on the argument that already put `README.md` there.

**[queue-privacy-default] is held against this item**, on the user's decision 2026-08-18. It splits setup's bundled gitignore offer per document — the same code path — so the two are settled together rather than shipping a second question into the moment the first one is already going wrong. The ordering is written into both entries.

#### Folding in is undescribed, appends rather than merges, and is the session's main accretion mechanism [folding-in-has-no-eviction-step]
**Raised by you 2026-08-18**, from the ideation loop's effect on new captures: before it, a capture was written to three or four times before anything else was processed, and holding the write until the design settled removed that. **Your question is whether the same principle reaches the accretion that happens afterwards, and your example is folding.**

**Your first point stands on its own: folding is native Claude behaviour the method leans on constantly and describes nowhere.** Nothing can be examined, measured or disciplined while it has no name in the docs, which is why it has no controls.

**Folding is admission without eviction.** Adding a rule to the corpus requires naming what comes out; folding content into an item requires nothing. Same asymmetry the rule gate exists to correct, one level down.

**And the transferable principle from the ideation loop is settle-first-then-write-once, which for a fold means rewriting the host item rather than appending to it.** Today's folds appended: [send-record-lacks-destination-and-intent] still carries its original framing paragraph and a later paragraph covering the same ground, because both accounts survived the merge. The accretion is the duplication, not the folded content.

**Measured in this session.** Four items absorbed content — [send-record-lacks-destination-and-intent] +255 words, [law-prose-restyle-heavy-docs] to 640, [missed-spec-write-interrupts-the-run], [stop-hook-fires-on-cited-slugs] +121. Every one grew; none shrank anything.

**Open question, and it is a measurement rather than a design.** Whether a fold that rewrites the host comes out shorter than one that appends. Testable from git by re-doing one of today's folds properly and comparing.

Relates to [work-items-accrete-past-their-band] and [split-action-defeats-the-bands-in-aggregate], which measures the same problem at whole-queue scale.

#### Rationale inside a work item may be read at build time as content to be built, and flow into the shipped docs [rationale-in-items-flows-into-shipped-docs]
**Raised by you 2026-08-18**, from the observation that decision history sits in items because the throughline preserves it at every step — but a build reads that item as its instructions.

**The hypothesis.** /next transcribes what an item carries. An item carrying three paragraphs of why offers no marker separating *what to build* from *what was preserved for the record*, so a build plausibly writes the reasoning into the doc it is editing. If that is happening, the rationale accumulating in the always-loaded rules is not an authoring slip — it is the throughline discharging itself into the wrong artifact.

**Why it is worth testing rather than assuming.** Two live efforts treat that accumulation as a discipline problem: the rationale audit, and the restyle's per-paragraph delete-and-reread lens now folded into [law-prose-restyle-heavy-docs]. Both remove rationale after the fact. **If the cause is upstream, both are chasing a symptom and will keep having to run.**

**The test, and it is cheap because both artifacts are in git.** Take items whose prose carried heavy reasoning into a build, read what that build actually wrote into the doc, and check whether the item's reasoning appears there in recognisable form. A match across several items supports it; reasoning that stayed in the item and never reached the doc refutes it.

**What it would change if confirmed.** The fix moves to the item: what a build reads carries the operative content and the recorded refusals, and points at the record for the rest. **Refusals stay** — strip "this alternative was refused because X" and the build re-proposes X and stops to ask, which is a failure two other items already cover.

**Your refinement, and the fix is wrong without it: some items need their rationale because the rationale IS the work.** An audit testing a hypothesis carries that hypothesis as its content — strip the reasoning and there is no audit left to run. So the distinction is not rationale versus none, but **operational rationale, needed to do the work, against historical rationale, preserved for the record.** The method already owns the test that separates them, stated for rules rather than items: delete the sentence and read what remains — a complete instruction means what you deleted was history, an unfinished one means it was operative. Applying it to items is the move; inventing a new test is not.

**Runs before [law-prose-restyle-heavy-docs]'s rationale lens**, because if this holds, that lens removes rationale the items keep putting back and has to run again. The ordering is written into both entries.

Relates to [folding-in-has-no-eviction-step] and [split-action-defeats-the-bands-in-aggregate], both filed the same day about where text accumulates rather than why.

#### Give the cleared region its own file so a build stops reading the whole queue, and see whether that reaches concurrent sessions [split-the-cleared-region-for-concurrent-sessions]
**Raised by you 2026-08-18**, including the merge mechanism below. **Your framing: separate the processed region off for building, and merge what is left back into the full queue for planning.**

**What it buys, measured.** QUEUE.md stands at roughly 24,800 words and a build reads it to work a handful of cleared items. Splitting the cleared region into its own file makes a run read only what it will build.

**Where it breaks, and this is the part to design.** **Planning's keep-step writes into that same build file** — a keep moves an item into the cleared region — so the collision the split was meant to remove returns at the one step that crosses the boundary. Keeps would have to land somewhere else until a merge. And underneath the file question is a git one: two sessions committing to the same repository is a separate problem no file split touches.

**A second hazard, named because it is the classic one.** If planning holds a merged copy while a build consumes an item out of the build file, merging back can resurrect an item that has already shipped.

**Your proposed mechanism is a queue merge skill.** **Weigh a cheaper route first:** `reorder_queue.py` already moves blocks byte-for-byte keyed by slug, which is what a merge is. A mode on the existing script may do it without a sixth skill — and a skill is the heaviest available answer, since every skill is loaded, documented and explained to consumers.

**The counterweight, which is yours and is real.** The one-file decision is on the record: reasoning across items splits badly when they are apart. **The distinction that may save this: the multi-file arrangement scattered items, while this scatters regions and leaves every item whole** — and planning merges them back before reasoning over them, so the split only ever binds a build. Different failure surface, not the same one.

**Not settled here** — raised at the end of a long session and filed rather than designed.

#### The rules disagree on how a planning record splits — "per item processed" against "per decision" [plan-entry-split-wording-disagrees]
Filed 2026-08-18 at the close that had to choose between them.

**The two statements.** `skill-nonspecific-rules.md`'s authoring standard says a plan entry "splits per item processed", and reasons from there: a planning decision IS a disposition on a queue item, so the build case's machinery applies unchanged. `SPEC.md` and `done.md` both say a planning record "splits per decision".

**Why the difference is not cosmetic.** They diverge whenever one decision settles several items, which is common — this session settled two SPEC items together, five mailbox items as one group, and two restyle items as a pair. Counted per item the close owed roughly 28 entries; per decision it owed 19. At the measured 316–329 words per split entry that is around 3,000 words, plus an index line each on a file read in full at every retrieve.

**What this close did, so the precedent is visible rather than silent.** Split per decision, on SPEC's and `done.md`'s wording, with the choice put to the user and deferred back.

**To settle at processing:** which wording is right, and then make the other match. Worth weighing that "per decision" is the one that survives a session where several items are settled together — and that "per item processed" is the wording in the always-loaded file, which is the one a session actually reads at the moment it decides.

Relates to [split-action-defeats-the-bands-in-aggregate], which measures what the split costs, and [plan-entry-split-action-underspecified], shipped.

