# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Writing a LOG entry can silently destroy an existing one, and the collision is only visible in git status [log-entry-write-can-clobber-an-existing-entry]
Filed 2026-08-14 by Claude at its own /done close, from destroying two committed LOG entries during that close. Captured by you in substance — you asked for it to be filed after it was reported.
**What happened.** The close wrote its entry to `LOG/2026-08-14-plan.md` without checking whether the name existed. It did: a committed entry from an earlier planning session the same day, 110 lines, overwritten in full. The restore was attempted at `LOG/2026-08-14-plan-2.md`, also taken by a second earlier session. Both were recovered intact with `git checkout HEAD --`, and the entry landed at `-plan-3.md`.
**The proximate cause is Claude skipping a rule that exists.** `done.md`'s LOG-entry-files section states it: `name already taken -> append -2, -3, …`. Nothing was missing. This item is not a request to add that rule again — restating a skipped rule is the failure shape this project has named twice.
**What is worth fixing is that the collision is SILENT.** A successful overwrite looks exactly like a successful create: the write reports success, the file exists, the index line resolves, and the entry reads correctly because it is the one just written. The only trace is `git status` showing ` M` where `??` was expected — one character, in a list of twenty-odd paths, at a step whose job is detecting *out-of-scope* dirt rather than checking the close's own writes. It was caught by chance.
**Why this project collides more than most.** The filename derives from close date plus session type, so every planning session on a day competes for the same name. This day had three. A consumer running one session a day would never see it; a self-hosting day, or any day with a morning and afternoon session, hits it immediately.
**Settled 2026-08-17. The fix belongs at the hook, not in a doc** — which is the level question asked deliberately, since restating the skipped rule is already ruled out above.

**The build.** `pre_tool_use.py` refuses a **Write** whose target is an existing file under `LOG/`, naming the collision and pointing at the next free suffix. Mechanical, unskippable, and invisible on correct work: a genuinely new entry filename does not exist, so the check never fires on a correct close.

**Narrow by design: Write only, never Edit.** A close legitimately edits the index and appends a tail to an existing entry, and those go through Edit. So nothing correct is caught.

**The staging check is refused.** It catches what the hook prevents, and it fires at every close including all the correct ones — the cry-wolf pattern this project has repealed measures for twice.

**The unverified paragraph below stands as written and must not be built on.**

**Why it was processed ahead of its turn**, on your instruction: the close following this session writes roughly twenty-five entries at once, the largest exposure this defect has ever had.

Rule gate: run — admitted as one refusal added to `pre_tool_use.py`'s existing write guard, which already refuses writes by path; no freestanding rule, no always-loaded slot, no new mechanism. **One alternative refused outright.** Failure evidence is one recorded instance: two committed entries destroyed in a single close, recovered only because the collision was noticed by chance in `git status`.
**One observation recorded without a claim attached.** The Write tool is documented to refuse an overwrite of an existing file not read in the session, and it did not refuse here. Whether that contract works differently than described, or the file counted as read, is unknown and uninvestigated — do not build on this sentence without checking it.
**Files (rough):** `plugin/throughliner/docs-b/done.md` (the LOG entry files section, possibly the commit core's staging check). Shipped — consumers write LOG entries the same way.

#### A Files line naming an excluded file makes it a false merge candidate in the digest [files-line-names-excluded-files]
Filed 2026-08-16 by Claude, from the digest run that verified [law-prose-restyle]'s placement in this same planning session. Processed immediately on the user's decision to work it rather than file it.

**What happened.** [law-prose-restyle]'s Files line ends "`CLAUDE.md` and `SPEC.md` are both out of scope under the decisions above." The digest then listed that item under both files in its "files named by two or more items" block — the block whose purpose is surfacing work that could be settled together. Two false merge candidates, generated by a sentence saying the opposite.

**The mechanism, read rather than assumed.** `FILES_PATH_RE` in `queue_digest.py` extracts every backticked string from the Files line and keeps whatever ends in a file extension or a slash. It has no notion of scope, so an excluded path is indistinguishable from an included one. The digest is not guessing wrongly; it is being told wrongly.

**The fix is at the authoring end, not in the detector.** Teaching the script to recognise exclusion phrases would be brittle exactly as [disposition-detector-is-format-brittle] records. Same shape as [rule-counter-blind-to-bold-prose-rules], settled the day before: an authoring constraint replaced a counting change there, for the same reason — a pattern cannot tell an excluded path from an included one any more than it can tell prose from a rule.

**So the Files line names only files that change.** An exclusion is a different statement and goes in its own sentence outside the line. Its parent is the two-limb keep check in `plan.md`, which already governs what a Files line must state, so this ships as a subordinate clause on that rule rather than as a freestanding one.

**Files:** `plugin/throughliner/docs-b/plan.md` — the two-limb keep check gains the clause above. `QUEUE.md` — [law-prose-restyle]'s Files line reworded so its exclusion sentence sits outside the line. No change to `queue_digest.py`.

Rule gate: run — admitted as a subordinate clause on `plan.md`'s existing two-limb keep check, which already defines what a Files line must state; no freestanding rule and no always-loaded slot spent. Nothing evicted. One alternative refused: phrase-detection inside the digest, on the brittleness ground recorded at [disposition-detector-is-format-brittle]. Failure evidence is one recorded instance, produced in this session by the item being processed at the time.

#### Restyle `skill-nonspecific-rules.md` into the law-prose wording standard, with a rule count taken either side [law-prose-restyle]
**Filed 2026-08-14 while assembling the remaining-cleanup inventory (recorded in that session's LOG entry), from finding it absent.** The restyle is the final step of your stated strategy — dedupe, then "put the final finish on all the method rules, putting them all into the new law-prose style format" — and it existed only in conversation. Grepping `QUEUE.md`, `SPEC.md`, `CLAUDE.md` and `resources/` returned nothing but the sentence recording that strategy, written an hour earlier. **The largest single piece of the plan had no queue item**, precisely the failure the method's own rule names: executable work lives in the queue as work items, and anything held only in conversation is invisible to /next and vanishes when the session ends.

**What it is.** A pass over the method's rule text converting it to the wording style the rule gate specifies — state the action the rule requires rather than the prohibition; express a qualification as structure rather than explanation; main clause first, conditions after; one idea per provision; every exception at the same level as the rule it qualifies. The gate states that standard for rules being *authored*; nothing has applied it to the rules already shipped.

**Why it runs last, a hard ordering rather than a preference.** A restyle over a corpus still holding duplicates restyles each copy separately and gives every copy its own chance to diverge — so it follows the deduplication work (group A) and the drift work (group C). Those groups are enumerated in that session's LOG entry; the sequencing argument is in [standing-audit-programme].

**The risk it carries, which shapes how it must be run.** A large authoring pass over the corpus, where every rewrite is an opportunity to reintroduce what earlier passes cut — rationale creeping back into operative sentences being likeliest. It must be audited *after* rather than trusted to verify itself, because the party restyling is the party that would certify it: see [rule-admission-has-no-independent-approver].

**Scope settled at processing, 2026-08-15: `skill-nonspecific-rules.md` alone, the other twelve files deliberately excluded.** The user's decision, taken between three shapes offered — this one file, file by file, or whole-corpus in one pass. It is the only file loaded in every session, so it carries the most value per paragraph rewritten, and one file is small enough that the after-the-fact audit this item demands is affordable. Whether the remaining files follow is a decision for after this pass shows what one file costs; not filed as work now, because a speculative item for twelve untouched files would be exactly the undesigned shape this item was rescued from.

**Narrowing the scope does not dissolve the ordering, which is why this stayed held.** A rule stated both here and in a skill doc still has two copies, and rewriting one of them is what starts the drift. So the pass still runs after the deduplication and drift work.

**Returned to Unprocessed 2026-08-15, on the blocker rather than the design.** The scope decision and the acceptance test stood; what could not be written is a `Blocked by:` value that is true. The item was briefly held against [standing-audit-programme] on the reasoning that the audit set sequences the cleanup groups. That is backwards, and the record says so: the inventory in `LOG/2026-08-14-plan-4.md` files this restyle as group F, "runs last, audited afterwards", and one of the five finish conditions is that the restyle has run and been audited by a pass that did not write it. The audit set follows this item; it does not gate it.

**The true gate is a condition over a group, and the queue has no field for one.** This runs after groups A, B and C are clear — group B being [rationale-audit-second-pass], scoped to the same single file in the same planning session and kept ahead of this deliberately, so its findings can still change the rewrite. Around seven items were open, among them [own-faq-diverged-from-shipped-template], [freeform-documented-as-the-wrong-thing], [docs-b-name-outlives-the-two-docset-model] and [adopted-claude-md-describes-retired-structure]. A fifth, [spec-names-a-count-the-style-dropped], left by deletion: its SPEC target had already been rewritten, so it was a finding rather than work. `Blocked by:` takes exactly one slug, so any single value would report this liftable the moment that one item shipped. Holding it on a proxy was weighed and refused: a field that resolves early is worse than no field, because the revisit trusts it. The gap is captured as [blocked-by-cannot-express-a-group-condition].

**Re-kept and cleared 2026-08-16: groups A and C are done, and the group condition no longer needs writing.** The gate was checked against the record rather than this item's own day-stale count. Group A — five duplicate-rule items — is four shipped and one, [done-build-restates-no-subset-rule], refused outright and deleted 2026-08-15. Group C — eight stale-description items — is six shipped, one deleted as a finding, and one folded into the output-style removal. So the condition expired by being satisfied, not by gaining a field; [blocked-by-cannot-express-a-group-condition] stays filed on its own merits, because the next item needing a group condition will still have nowhere to write one.

**Group B did not clear the same way, and folding it in is what resolved it.** [rationale-audit-second-pass] shipped 2026-08-16, but an audit edits nothing — it filed nine findings, eight against this same file. Building those separately and then restyling would be two per-paragraph passes over the same sentences, each able to undo the other's wording: the cost this item already refused when it absorbed the "session" terminology fix. **So the eight are deleted into this item and their findings carried below.** The ninth, [rationale-audit-fetched-docs-gap], stays in Unprocessed — it is about the twelve files this pass does not touch.

**The acceptance test is mechanical, and it answers this item's own stated risk.** A restyle authors no new rule and evicts none, so the count of always-loaded rule statements must not rise across the pass. `resources/rule_signals.py` already computes that count for its CONTRADICTED check. Take it before, take it after: a rise means the pass smuggled something in, and that addition is justified at the gate or reverted. This does not detect a rewrite that changes a rule's meaning while keeping the count flat, and must not be described as if it did.

**The test has a hole this pass could walk through, found 2026-08-16 when [rule-counter-blind-to-bold-prose-rules] built.** The count reaches three shapes only — a bullet, a paragraph whose bold leads the line, and a line inside a typed block — so **a rule rewritten into plain prose disappears and the count FALLS**, which the test reads as success. A restyle is a rewriting pass over exactly those sentences, so this is the likeliest failure rather than a theoretical edge. **So a fall is not a pass either: any fall must be accounted for rule by rule against the evictions claimed.** The authoring constraint settled on [rule-counter-blind-to-bold-prose-rules] — an always-loaded rule takes one of those three shapes, now stated in `CLAUDE.md`'s rule gate and in the file's own opening — is what keeps the count honest, and that item should ship first for that reason.

**The "session" terminology fix is folded into this pass, absorbed from [session-conflates-chat-and-run] on 2026-08-15 when that item was deleted into this one and [terminology-corpus-audit].** The user's words, which are the decision: *stop using the word "session" because it conflates a chat with a use of plan or next — only say "plan session" or "next session".* Said while correcting a rule that used both meanings inside four sentences. The vocabulary is already shipped in this same file — one chat runs /plan and /next as often as needed, and a plan session and a next session are runs of a command inside it — so nothing needs defining; this applies it.

**Why it folds in here rather than running as its own pass.** This file has 61 occurrences, each needing a judgment about which meaning rather than a substitution. Resolving them is a wording decision, and this pass already rewrites every rule statement in the file. Run separately it would be the third per-paragraph pass over the same sentences in one plan — after the rationale audit and this restyle — each able to undo the previous one's wording. The remaining 646 occurrences across SPEC, both FAQs, `done.md`, `plan.md` and the rest belong to [terminology-corpus-audit], where "session" is already the first term listed.

**The eight rationale findings absorbed 2026-08-16, each with the site it names and the disposition settled at this keep-step.** Filed by [rationale-audit-second-pass] and approved as that audit's numbered set; they are the specific work this pass carries beyond the wording standard.

1. **The work-cycle fenced block, from [cycle-block-carries-rationale-in-a-fence].** Two sentences inside the fence at the top of the file: step 5's "A planning session between a finding and its build is the cycle working, not an obstacle to it", and step 4's "The loop's boundary is a new session with no memory of this one, which is why every return edge below routes through a FILE and never through what someone remembers." Both fail the delete-and-reread test. The build weighs one thing before cutting: the fence is orientation whose job is conveying a shape, so check whether either sentence is doing operative work there. This shape was invisible to the first audit pass, which matched prose and never looked inside a fence.
2. **The cadence rule, from [cadence-rule-rationale-and-numeral].** Cut the trailing "How often to speak is a separate question from how long any one message is, and in a session full of tool calls it is the one that decides how much the user reads" — an argument for the rule's importance, not part of applying it. **And drop the "Three occasions warrant it" numeral, settled here as recommended.** It does not breach the derivation rule, being descriptive of the list that follows; it is dropped on maintenance grounds — a session admitting a fourth occasion has to notice a numeral three lines above the list, and a numeral silently disagreeing with its list is worse than none. Reword to name the three without counting them.
3. **Two unmarked opening rationale paragraphs, from [unmarked-rationale-paragraphs-open-two-rules].** The scrub-before-writing section opens "QUEUE.md, SPEC.md and LOG entries get committed, and a commit keeps the text even after it's deleted. Many users' repos are public" — both deletable, the instruction beneath stands. Research-and-evidence-filing opens "Offering a web search is a capable move, not an admission of ignorance. The bar is low — offering is cheap because the user can decline." **Apply the test to that second sentence on its own rather than cutting the paragraph as a block**: "the bar is low" is arguably an instruction about how readily to offer. This is the commonest shape the first pass could not see.
4. **The captures-placement explanation, from [captures-placement-rationale].** "Placement: append to the bottom of Unprocessed, always" is the whole operative statement; the seventy-word "Two reasons, the second being the real one…" paragraph goes to the LOG entry that settled the placement rule. It fails the test cleanly — the rule names one position and admits no judgment.
5. **The throughline's "what it buys" paragraph, from [throughline-rationale-duplicated-in-spec].** Stated twice in two always-read documents: once here, once at greater length in SPEC's opening as product truth. **Cut the always-loaded copy and leave SPEC's.** SPEC is where the product's reason for existing belongs and it has a floor a rule list does not. **No SPEC edit follows**, so the single-file scope holds.
6. **Two of three evidence clauses, from [evidence-clauses-attached-to-three-rules].** Cut the vocabulary rule's "this was explained repeatedly to a user who still did not have it, because nobody had opened a file and pointed", and the inversion rule's "Reading 'deliver together' as 'show for approval first' is what once put the close's capture re-scan in conflict with the write-first rule that governs above it." Both are recorded instances belonging in the LOG entry admitting the rule.
7. **The third evidence clause is KEPT and reclassified as operative — the user's decision, 2026-08-16, asked at this keep-step because the item required it.** The sentence is the one-chat-at-a-time rule's "Two chats at once was supported for a period and never worked: a capture filed in one is invisible to the other, and the two disagree about the queue from the moment either writes to it." The test reads it as rationale. It is kept on the user's own recorded behaviour as evidence: meeting a stale FAQ entry describing two-chat coordination as supported, she rejected it in her own words — *"has NEVER successfully happened and EVERY time we have tried to ship that behaviour, it has fallen over"* — and she recognised it as wrong **because she knew the history**. A bare prohibition with the history stripped reads as arbitrary, and arbitrary rules are the ones that get argued with; see [plan-does-not-build-keeps-being-relitigated]. Written into the operative sentence per the gate's reclassification route, so it cannot be removed later without leaving the rule incomplete.
8. **The inline-switch paragraph, from [inline-switch-paragraph-is-justification].** Only its last sentence — "Default off means today's behaviour" — is operative. The two before it argue for a decision already taken and restate a mechanism the typed block above already carries, which makes this the eviction rule's own case: a clearer restatement leaving the original standing has doubled the text rather than merged it. Keep the operative sentence, cut the rest.
9. **The truncated-read sentence is REWRITTEN, not cut, from [truncated-read-sentence-reclassify].** Under "Reading a whole file before reasoning over it": "The failure is silent by construction: a truncated read looks like a complete one to whatever reasons over it, so nothing downstream can detect it — which is why the check belongs at the read, not later." Delete the whole sentence and *where the check belongs* goes with it; delete only the first two clauses and the instruction survives. Lead with the operative half — the check runs at the read — and let the reason follow inside that sentence. **This is the one finding that keeps text, and it is the failure mode of the technique itself**: an auditor applying the test mechanically would cut this and silently move a check to nowhere.

**Why nine numbered findings and eight absorbed items:** [evidence-clauses-attached-to-three-rules] splits into entries 6 and 7 because its three sites now have two different dispositions.

**One thing the fold must not silently swallow:** the machine's use of the word — `session_id`, the working file's name, the hooks' own messages — is a separate question with probably the same answer as [work-item-means-processed-only] gave for code. This pass touches prose only, and where a rule statement names the machine's term it stays as it is.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — every rule statement reworded to the standard: prohibitions restated as the action required, qualifications carried by structure rather than explanation, main clause first with conditions after, one idea per provision, exceptions at the same level as the rule they qualify, and every use of "session" resolved to chat, plan session or next session. Plus the nine numbered rationale findings above, each at the site it names: two sentences cut from the work-cycle fence, the cadence rule's trailing argument and its "Three occasions" numeral, two unmarked opening paragraphs, the captures-placement explanation, the throughline's "what it buys" paragraph, two of three evidence clauses, the inline-switch paragraph down to its last sentence, the one-chat-at-a-time clause rewritten as operative text, and the truncated-read sentence led by its operative half. No other file changes; `CLAUDE.md` and `SPEC.md` are both out of scope under the decisions above.

**Run the count before and after in the same session, and record both numbers in the LOG entry** — `py resources/rule_signals.py .` supplies it. A rise means something was smuggled in; a fall must be accounted for rule by rule against the evictions claimed above, since a rule rewritten out of the three counted shapes disappears silently.

Rule gate: run — no rule authored, none evicted, and no rule moves between always-loaded and fetched. The pass restates shipped rules in the wording standard the gate's fourth part already specifies, which is why it needs no admission argument of its own: the standard was admitted when the gate was. The count check above is the evidence that this stayed true, not a claim that it did. **The fold of the nine rationale findings adds no rule and evicts none beyond what those findings already carried; the one addition it makes is a reclassification — entry 7 moves a sentence from rationale into operative text, on the user's decision, which is the gate's own stated route rather than a new rule.**

#### The vocabulary rule bans a term it should sometimes teach once [vocabulary-rule-has-no-teaching-branch]
**Captured by you 2026-08-16, in your own words:** *"I think that a little bit of learning is ok. we need to design jargon sensitively around this which is tricky.. but arguably NO jargon at all is even trickier (and possibly impossible)."*

**What the shipped rule says.** `skill-nonspecific-rules.md`'s vocabulary test asks whether a term names something in this user's world that you could show them. Yes means say it and show the thing the first time. No means don't say it — translate or omit. There is no third answer.

**The gap your position names.** A term can name nothing in your world and still be worth one teaching moment, because the alternative is a longer sentence every time it comes up, forever. Zero jargon may not be reachable at all.

**The instance that raised it.** Claude used "crying wolf" and "synthetic test" unexplained, then treated both as violations. One is an ordinary English idiom and the other a craft term; the rule's own examples are procedure vocabulary — `[SILENT]`, "Step 2.4", doc filenames — so the rule was probably never aimed at either, and applying it there is what makes it look unworkable.

**The second half, added 2026-08-16 after the same conversation continued. Your position, in your own words:** *"I don't know that we need to be prescriptive to Claude how it explains things, demanding it show first. Claude is perfectly capable of explaining things responsively."*

**So the same paragraph over-prescribes twice.** The first half bans a term outright where it should sometimes be taught once; the second dictates the *form* the teaching takes — "Show it, don't define it" — rather than leaving Claude to answer the question it was actually asked.

**The evidence behind the show-first form is one instance, and the user says it is misread.** The rule's text claims something was explained repeatedly to a user who still did not have it, until somebody opened a file and pointed. **Her account of that moment, 2026-08-16, in her own words:** *"no that just happened to be when I relented."*

**So the sole justification is a coincidence recorded as a cause.** What the rule reads as "pointing is what made it land" was the user giving up on the argument. Claude wrote the rule from its own reading of a moment it could not see inside, and the reading has stood as evidence since. [law-prose-restyle] has already settled that this sentence is cut as rationale, so it was about to leave the corpus without ever being checked against the person it describes.

**One thing to weigh at processing, without inventing a pattern from a single case.** A rule whose evidence is "and then it worked" rests on Claude's reading of whether it worked. This is one such misreading, found only because the user was present when it was quoted back. Whether that is worth looking for elsewhere is a judgment for a planning session; recorded here rather than filed separately, because one instance is not a pattern and this project bans speculative work.

**A live counter-instance, from the exchange that raised this.** Asked what a hook had to do with tracing a change, Claude opened `post_tool_use.py`, showed the line holding two literal words, and explained from it — because that was the clearest answer available, not because a rule required it. Responsive explaining reached the show-first outcome on its own.

**Settled 2026-08-17, and the second half is the user's correction of Claude's proposal.** Claude proposed narrowing the ban to procedure vocabulary. Her answer reshaped it: *"well obviously if claude is explaining the procedure then it may name things from it. but it can't just use terms in passing and expect people to understand."* So the ban is not on the term — it is on **unexplained passing use**. Where the procedure is what the user is asking about, Claude names its parts and teaches each term once.

**The build.** In `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, the Vocabulary section: replace the two-answer test with one keyed on whether the term is being used in passing or explained; add the teaching branch, so a term naming nothing showable can still earn one explanation rather than a longer sentence forever; and cut the "Show it, don't define it" paragraph with its evidence clause, leaving what good explanation achieves and no prescribed form.

**Placed after [law-prose-restyle]**, which restyles the same file and already schedules that evidence clause for cutting — running this second means the paragraph is rewritten once.

Rule gate: run — admitted as an amendment to the existing vocabulary rule, which already governs which terms are said and how; no freestanding rule and no slot spent. The eviction is the show-first form and its evidence clause, repealed outright. Failure evidence is two recorded instances: "crying wolf" and "synthetic test" treated as violations by a rule never aimed at them, and [halt-narration-used-unexplained-jargon], the same failure a day earlier.

#### An ideation loop: Claude offers to capture and holds the write until the user says they are done [ideation-loop-holds-the-write]
**Captured by you 2026-08-16, in your own words:** *"maybe we need an ideation loop in skill nonspecific behaviours. one where Claude offers write to capture and doesn't until user is done and says yes. might save tokens and also make captures shorter as they'll be less cumulative and meandering?"*

**Measured in the conversation that raised it.** Six writes across one continuous design discussion — three on [vocabulary-rule-has-no-teaching-branch], three on [teaching-method-looked-up-on-demand] — each a full re-authoring of text that was not finished. A capture written repeatedly reads like several conversations stacked on each other, because it is.

**The lengths, measured the same day by `resources/measure_written_shape_length.py --bands`:** the two written across three turns came to 634 and 586 words; this one, held and written once, came to 354. Band top is 177 and the ceiling 265.

**Read that as direction, not proof, and the caveats belong in the item.** One held instance is one data point. It still breaches the ceiling by a third, so writing once is not sufficient alone. And the two long items absorbed genuinely more content across those turns, so part of their length is substance rather than repetition. The stronger evidence is adjacent: the five captures filed the same day by [run-the-written-shape-measurement], each written in a single pass on comparable subjects, landed three inside the band and two just over, at 185 and 211. Nothing here isolates the loop from everything else that changed that day.

**The gap is narrow and the write-first rule is not wrong.** Its test — is the previous version recoverable without the user? — holds. What it assumes silently is that the text is *finished*. Mid-ideation it is not, so it fires at every turn of a design that has not settled. This targets that assumption without touching the rule's logic.

**The objection, and your answer to it.** Holding means a chat ending unexpectedly loses the design, against the standing rule that nothing unrouted survives a chat. **Your answer, in your own words:** *"if it's missed and rescan isn't run, the done rescan will catch it at least."* The close's wind-down re-scan runs at every close and /rescan runs on demand, so a held design is no more exposed than anything else in the chat.

**The open question you named, settled 2026-08-17 on Claude's recommendation and your agreement: no wording change to /rescan or the close re-scan.** Their existing wording — *decided, noticed or asked for and never written into a file* — already reaches a held design, which is all three. A clause saying so would restate what is there.

**Scope, on your instruction: the loop covers ideation in any skill AND the processing of captures in /plan.** Both are the same shape — text being worked out rather than finished — so a loop written for one and not the other would fire in half the places it applies.

**The build.** One clause on the write-first rule in `plugin/throughliner/docs-b/skill-nonspecific-rules.md`: while a design or a disposition is still being worked out, offer to capture and hold the write until the user says go. The rule's own test is untouched — this names when text counts as finished.

Rule gate: run — admitted as a clause on the existing write-first rule, which already decides which text is written before it is reported; no freestanding rule and no slot spent. Nothing evicted. Failure evidence is six re-writes measured in one discussion, with the two re-written items landing at 634 and 586 words against a ceiling of 265.

**Placement.** `skill-nonspecific-rules.md` on the merits, since ideation happens in all four skills, which is that file's stated admission test.

#### SPEC says mail has no size limit while a shipped test caps the payload that carries it [inbox-size-contradicts-the-payload-cap]
Filed 2026-08-16 by Claude at the close of the twenty-one-item run, from a suite failure that halted the commit.

**What happened.** The close ran the hook suites, as this project's rules require when staged paths include `plugin/throughliner/hooks/`. `hook_schema_check.py` failed: the SessionStart payload measured 10,978 characters against a 10,000-character cap, 110%.

**The cause is mail, not this run's edits.** Two messages arrived from that consumer project partway through the session and were still unarchived — mail arriving mid-session waits for the next session start, so nothing had triaged them. They total 7,107 characters, and `session_start` delivers each waiting message **in full**. The rest of the payload is roughly 3,900. This run's changes to `session_start.py` made the payload *shorter*: the parallel-sessions coaching came out of all three isolation messages.

**The contradiction, which is the actual finding.** `SPEC.md` states that delivering full message bodies is deliberate, that the cost is knowingly accepted — an unarchived message rides in every session's opening until archived — and that **no size limit is set, because a limit would be a number with no derivation**, the channel being deliberately low-traffic. `hook_schema_check.py` asserts a 10,000-character cap on the payload carrying those messages. **Both cannot hold.** A project doing exactly what SPEC describes will fail a shipped test.

**It is transient here and that must not be mistaken for harmless.** These two archive at the next session start and the payload drops back under on its own. But it recurs for any user whose mail sits unread, and it recurs at a close, where it halts a commit — a hard stop landing on someone who has done nothing wrong.

**To settle at processing, and the cap's own derivation is the first question.** Where did 10,000 come from? If it is a real harness constraint, SPEC's no-limit sentence is wrong and mail needs a bound after all — derived from the harness figure minus the rest of the payload, which is a derivation and therefore admissible. If the cap is a bare number someone chose, it is the exact thing this project bans and the test should not assert it. **Read the cap's origin before deciding anything else.**

**Now known: the cap is Claude Code's, not ours.** Hook output is capped at 10,000 characters, sourced to Anthropic's hooks reference and two issue reports. Past it the harness discards the whole payload and substitutes a ~2KB preview plus a file path — so enough unread mail costs the session its project state, its queue facts and its rules directive, not merely the mail.

**Settled 2026-08-17 on your argument, which overturns the full-delivery decision of 2026-08-16.** Your question: why does the hook carry entire letters when the same payload already carries a *directive* to read the behaviour rules, a far larger file. It is not different in kind. The old mail directive failed because it was a bare instruction with nothing confirming the read — not because directives cannot work; the rules directive is trusted because it has a self-check. Inlining was the expensive answer to a problem the payload had already solved cheaply one line earlier. Two shapes Claude proposed were refused before this: truncate-and-say-so, and deliver-what-fits — the second by your objection that what fits is unknowable, since the rest of the payload varies session to session.

**The build.** `session_start.py` stops inlining message bodies and emits a count, the filenames and a directive to read them, with a self-check in the shape of the rules redirect. `hook_schema_check.py`'s body-delivery test is rewritten to assert the directive and the absence of bodies. `SPEC.md`'s INBOX paragraph drops the full-delivery guarantee and states the real constraint. `plan.md`, `next.md` and `feedback-and-inbox.md` each name delivery-of-bodies and are reworded.

**And on your instruction, /plan's opening ask carries the mail:** where mail is waiting, the opening question becomes *process the mail first, or start most-unblocking-first?* That is where the read gets its teeth — a question the user answers, rather than a step that can be passed over.

Rule gate: run — admitted as an amendment to the existing session-start delivery rule, which already fixes what the hook hands a session and what it redirects to; no freestanding rule and no slot spent. **The eviction is the full-delivery guarantee, repealed outright.** Failure evidence is one measured instance: a 10,978-character payload at 110% of the cap, halting a commit.

**What actually happened at the close, corrected — an earlier draft recorded a decision the user had not made.** She was told the check had failed and did not authorise committing over it. Her instruction was to fix the cause: file the two waiting messages as captures, archive them, and capture that the rule needs inspecting. That was done, and **the suite passed on the re-run** — so nothing was committed over a failing check and no informed-consent trail is needed.

**Her reading of the rule, this item's starting point.** In her words: the briefing-size rule was *probably written before INBOX existed as a feature and should be inspected.* The dates support it — a payload cap predating a feature that injects arbitrary external text into that payload is a limit that never accounted for its largest input.

**One thing she corrected that changes nothing mechanically and matters anyway.** Claude described this as text "printed into the briefing" without saying whose. It is context the hook hands Claude at session start; the user never reads it. The conflation made a technical explanation land as nonsense to the person being asked to decide on it.

Relates to the INBOX delivery design in `SPEC.md` and to [inbox-delivery-unconfirmed].

#### Look up how to teach a concept at the moment it fails, rather than fixing a teaching form in advance [teaching-method-looked-up-on-demand]
**Captured by you 2026-08-16, in your own words:** *"maybe once something has been explained twice, Claude can reach to the internet for better examples the third time? or look first for 'what is the best way to teach x' then choose the best or second best according to its ability (its ability to display text)"*

**Your reason for rejecting the obvious alternative, also your words:** researching best learning approaches up front *"doesn't make sense because we don't know what concept Claude will be explaining to people."* Generic pedagogy filed once is too abstract to reach any particular concept; a lookup at the moment of need is aimed at the concept that actually failed.

**It replaces a prescription with an escalation.** [vocabulary-rule-has-no-teaching-branch] records that the shipped rule dictates one form of explanation on evidence the user says was misread. This proposes nothing fixed: explain normally, and only where that fails, go and find out how this specific thing is taught.

**The medium constraint is load-bearing rather than a caveat, and it has two arms — your words:** *"Best available to me in this channel"* OR *"best I can refer them to"*, the second being *"the shortest video demonstrating a part of whole concept related to explaining the thing."* So the option set is what Claude can perform in text, plus what Claude can point at. Most teaching advice assumes a whiteboard, a physical object, or a room, and neither arm reaches those.

**Shortest is the right criterion for the referral arm, because it is checkable.** Duration is a fact; "best" would be Claude judging content it has not consumed.

**The vouching risk was raised and you resolved it, which is why the referral arm survives.** The objection: Claude can find a video and cannot watch it, so recommending one vouches for something unconsumed — the same shape as the shipped rule that a command is verified before being handed over to be pasted, since a non-coder cannot tell a bad resource from a good one and the failure arrives in their hands. **Your answer, in your own words:** *"it can check the full cc if we specify YouTube... let's say video or articles or any audio whose transcript is available."*

**So the criterion is readable text, not medium.** Anything whose content Claude can read before pointing at it qualifies — captions, an article, a transcript — and Claude reads it rather than vouching blind. **And your second point narrows the search usefully:** an explainer for one *part* of a concept is easier to match than one for the whole, so a narrow ask has more good answers.

**One residual, recorded rather than argued.** A transcript is not the demonstration. Where the value is visual — someone pointing at a screen — the transcript reads "and then you click here", and auto-generated captions can be poor. Claude can confirm a source is on-topic; it cannot confirm the presentation works.

**The trigger, settled 2026-08-17: the user asking about the same thing again.** "Explained twice" requires Claude to notice its own explanation did not land, and noticing-based triggers do not fire here — a session satisfied with its answer notices nothing. A repeat question is a fact rather than a self-assessment.

**Placement, settled the same day: an amendment to the research-and-evidence rule**, whose *what would answer this?* trigger already covers reaching outward. This points the same question at how something is taught rather than at an external fact, so it costs no new slot.

**The first step, on your objection — a repeat question may be too vague to search on.** "I still don't get it" names no concept, and searching the whole subject returns the generic pedagogy you already rejected. So the clause opens by working out which part did not land, asking the user where that is not obvious. It also feeds the search the narrow target this item says gets better answers.

**The limit, stated in the rule rather than assumed.** This converts a vague question into a specific one or it visibly fails to. Where neither party can name the missing part, no lookup helps and the answer is a different explanation, not a search.

**The build.** One clause on the research-and-evidence rule in `plugin/throughliner/docs-b/skill-nonspecific-rules.md`: on a repeat question, name the part that did not land, then look up how that specific thing is taught, choosing from what Claude can perform in text or point at — shortest source whose content Claude can read first, read before pointing.

Rule gate: run — admitted as a clause on the existing research-and-evidence rule, which already governs when Claude reaches outward; no freestanding rule and no slot spent. Nothing evicted. Failure evidence is the instances behind [vocabulary-rule-has-no-teaching-branch] and [halt-narration-used-unexplained-jargon], where explanation failed and nothing escalated.

#### Filing a blocker mid-session can move the ordering rung back UP, and nothing says so [rung-can-move-back-up]
Captured by you 2026-08-17, from this session: after we agreed to file an audit that blocks a corrections build, you observed that the rung should now go back up, and that this is not obvious.

**What the rule says today.** `plan.md` requires the rung to be re-checked at every pick, narrating in one clause only where it changed. So the check exists.

**What it does not say.** "Re-check" reads as *has this rung run out yet* — a downward-only reading, since the ladder is written as a fall-through. Filing a blocker mid-session creates unblock-potential where there was none, which is rung 2 becoming live again after the session had already fallen past it.

**Why it matters here rather than in theory.** A planning session that files blockers is the ordinary case, not an edge one — this session did it twice in an hour. Each time, the item that now blocks something else is the one worth processing next, and the ladder as written would not reach it until the current rung emptied.

**Settled 2026-08-17, with one correction to the case that prompted it.** The two blockers filed in that moment went straight into Processed, so nothing in Unprocessed changed and the rung did not in fact move. Recorded because the item would otherwise send a build looking for a fault at the wrong site.

**Where it genuinely fires, and the method requires this route.** Where a held item names a blocker not yet in the queue, the blocker is written into Unprocessed first. That is a new entry other work cites, so rung 2 becomes live again after the session had already fallen past it.

**A second effect the capture did not reach: the throughput floor goes stale the same way.** The floor is derived from how many blockers sit in Unprocessed. Filing one mid-session changes that count, and nothing re-derives it, so the number stated at the opening quietly stops being true.

**The build.** One clause on `plan.md`'s existing re-check-the-rung sentence: a rung can become live again rather than only run out, filing a blocker into Unprocessed is the move that does it, and the throughput floor is re-derived at the same moment.

Rule gate: run — admitted as a clause on the existing re-check-the-rung sentence, which already fixes when the rung is examined and how a change is narrated; no freestanding rule and no always-loaded slot spent, since it lives in `plan.md`. Nothing evicted. Failure evidence is one instance, thin and admitted as such: the user noticed the gap unprompted while the ladder was in use, and the cost of the clause is a sentence in a doc the step has just read.

#### An item can state a design question as open, schedule it into the build, and pass the keep-step [stated-open-design-question-passes-the-keep-step]
Filed 2026-08-16 by Claude from an INBOX message sent by a consumer project running this method, triaged and archived at the close of the twenty-one-item run on the user's instruction.

**What they hit.** A /next run halted on a build item that had been through /plan, kept, and cleared to run. The item is a large feature and unusually well designed: it names its files, says what changes inside three of them, records two rejected architectures with reasons, and lists the SPEC sentences that stop being true when it ships.

**Then it states, in its own prose, that one design question is left open** — and instructs that it "should be settled at the start of the build rather than during it". Its file list, for the fourth file, reads: "any affordance the link-address question settles on".

**Why this passes the keep-step, the part worth attention.** The readiness test asks whether an item says what changes inside the files it names. This item satisfies that on a plain reading: three files precisely, and for the fourth a grammatically complete phrase naming a file and a purpose. **What it does not supply is a decision.** The test catches an item *silent* about a gap. It does not catch one that *states* the gap, explains that stating it was deliberate, and schedules it into the build.

**The phrasing is what makes it hard to spot.** "Settled at the start of the build rather than during it" reads as care about sequencing. It does the opposite — moving a design decision across the boundary the method rests on, dressed as diligence. A keep-step reading that sentence has to notice that the start of the build is still the build.

**It hands the build two conflicting directions.** /next's underspecification branch says an item that cannot be scoped halts, because building it means inventing scope the user never agreed to; the item instructs the opposite, and the one carrying the item's own authority is the wrong one. **Their user resolved it in the room** — reported words: *this is design work in a next session, not permitted.* Unattended, the likely outcome is a build that invents the affordance, ships it, and logs it as designed.

**Their suggested shape, one project's reading rather than a specification.** A stated-open design question refuses at the keep-step whatever the file list says, on a nearly mechanical trigger: prose announcing a question is left open, or a file-list entry phrased as a dependency on an unmade decision ("whatever X settles on", "the affordance chosen for Y"). The disposal is probably not rejecting the whole item — most of theirs is finished — but splitting the open question into its own small item and holding the large one against it, machinery that already exists.

**Their closing observation, which explains the survival.** The item calls the question "a small self-contained design question", which is true and is exactly why it travelled. A small unmade decision is still an unmade decision, and small ones are the only kind that survive a keep-step.

**How this relates to what shipped the same day.** [next-halt-test-drops-the-second-limb] built in this run and widened /next's halt to both limbs, so a build meeting this item would now halt as underspecified rather than improvising. **That is the downstream catch, not the fix.** This report is about the keep-step letting it through, which is upstream and untouched — and the argument for the /plan-sited gate is that refusing costs a conversation there and costs undoing finished work anywhere later.

**They ask for nothing and nothing is blocked on us**; the item stays in their queue and goes back to their /plan. Relates to [next-halt-test-drops-the-second-limb] and [plan-does-not-build-keeps-being-relitigated].

**Settled 2026-08-17. The build.** One clause on `plan.md`'s two-limb keep check: a Files entry whose content depends on a decision not yet made fails the second limb rather than partly passing it, and prose scheduling a design decision into the build fails it the same way however carefully phrased. **Name the phrasing explicitly** — "settled at the start of the build rather than during it" reads as care about sequencing and does the opposite, because the start of the build is still the build; a keep-step can only catch what it has been shown.

**The disposal is a split, not a refusal**, which is their recommendation and needs no new machinery: the open question becomes its own small item and the large one is held against it by slug. Most of such an item is usually finished, and rejecting it whole would discard that.

**The level, asked and answered: a rule at the keep-step, not a hook.** A hook could only match hedging words in a Files line, which would fire on honest text; this project has twice repealed measures for crying wolf.

Rule gate: run — admitted as a clause on `plan.md`'s existing two-limb keep check, which already governs what a kept item must state; no freestanding rule and no always-loaded slot spent. Nothing evicted. Failure evidence is one reported instance from a consumer project, where the item passed the keep-step, halted a run, and was resolved in the room by their user — *this is design work in a next session, not permitted.*

#### Routing a message names its sender in a committed document, against the address-book rule [routed-mail-names-its-sender]
Filed 2026-08-17 by Claude, from a violation found while sending a reply in this session. Worked immediately on the user's instruction rather than deferred.

**The rule and the breach.** The address book is write-and-send only: a session may pass a recorded path to a send, and may never name a correspondent in any document. Yet three queue items filed from mail named the sending project in their prose, and those items are committed. The mailbox is gitignored, so the leak was never the mailbox — it was a session reading a name out of it and copying it into `QUEUE.md`.

**Claude's first reading was wrong and the user corrected it.** Claude argued the rule was over-broad, because the message convention requires a sender to identify itself, so routing appeared to compel the breach. **Her correction:** INBOX is supposed to be gitignored — so the sender naming itself inside a mailbox is safe, and only the copy into a committed document is not. The rule stands; the practice broke it.

**The build.** One clause on the inbound routing step in `plugin/throughliner/docs-b/feedback-and-inbox.md`: a capture or LOG entry made from a message describes its source generically — "a consumer project running this method" — rather than naming it. The same rewrite-at-the-same-usefulness the scrub checklist already requires, and nothing is lost, since an item's reasoning never depends on which project sent it.

**Already done in this session, so the build is the rule only:** every mention still in `QUEUE.md` was reworded generically.

**The residual, stated rather than fixed.** Committed LOG entries cannot be rewritten, and one slug — [line-anchor-answer-from-understudy] — carries the name and is immutable by rule and already in git history. Renaming it would remove the name from a live path and leave it in history, the same trade already refused over the `docs-b/` rename.

Rule gate: run — admitted as a clause on the existing inbound routing step, which already says what a routed message becomes; no freestanding rule and no always-loaded slot spent. Nothing evicted — the address-book rule stands unchanged, which was the disputed point. Failure evidence is three committed items found in one grep.

#### Filing a capture has no mechanical route, so it is hand-anchored to a neighbouring item and can land in the wrong section [no-mechanical-route-for-filing-a-capture]
Filed 2026-08-16 by Claude at the close, from an error it made in this planning session and did not catch itself.

**What happened.** A capture the user asked to be filed was written into **Processed, above the readiness line**, where a /next run would have tried to build an item whose entire content is three undesigned routes. It was found only because the user asked for an unrelated summary and the digest listed it as cleared.

**The mechanical cause, which is not carelessness.** `reorder_queue.py` has `--move-section` and `--delete`, and nothing for appending a new entry. So every capture is filed by an ordinary text edit anchored to whatever text sits at the end of the file. Here the anchor was read, the file changed underneath it — an item was moved from Unprocessed into Processed by the mover — and the append landed after the anchor's **new** position. Two safe operations composed into an unsafe one.

**Why the existing guards did not catch it.** The queue lint checks slug, red-flag state and `Blocked by:`; a capture sitting in Processed above the line is structurally valid, so there is nothing to flag. The digest reports it correctly as cleared, but only if someone reads that line and knows it should not be there. Both worked as designed and neither could help.

**This is the argument that made the mover the primary path for moves, applied to the operation the mover does not cover.** Already recorded: an exact-string edit can only place a block by reproducing or anchoring text, and doing it by hand once cost 6,253 output tokens and corrupted a neighbouring item. Filing is the last queue operation still done that way.

**It reaches consumers unchanged.** Every session files captures, and the always-loaded rule says to append to the bottom of Unprocessed — an instruction with no tool behind it, in the one file the method treats as authoritative.

Relates to [mover-cannot-add-a-new-item], which shipped the *move* half of this gap, and to [move-section-does-not-report-line-crossings].

**Settled 2026-08-17 — all three yes.** `reorder_queue.py` gains an append placing a new entry at the bottom of a named section; `pre_tool_use.py`'s script-write ban gains the same exemption the mover already has; and the always-loaded filing rule names the tool the way the keep-step names the mover, which is the part that makes it get used.

**The body arrives by file, not on the command line.** A multi-paragraph rationale passed as an argument breaks on this platform over quoting, newlines and em-dashes. Claude writes the text to a scratchpad file with the ordinary editing tools, and the script reads it — the scratchpad is already permitted, and the queue itself is still only ever touched by the script.

**On your instruction, two constraints on the shape.** It is reachable from **every** skill, since a capture may be filed at any moment: the rule naming it lives in `skill-nonspecific-rules.md` beside the filing rule it amends, and the guard exemption is not scoped to one skill. And it is **subordinate to the ideation loop** — the append is what runs once the loop releases the write, never a reason to write earlier.

**The gain is the mover's, on the operation the mover never covered:** no anchor to go stale, so a file that changes underneath the edit cannot send the append into the wrong section. That is the recorded failure exactly, and it nearly recurred while this item was being processed.

Rule gate: run — admitted as a clause on the existing filing rule, which already says where a capture goes; no freestanding rule and no slot spent, and the tool it names replaces a hand procedure rather than adding one. Nothing evicted. Failure evidence is one recorded instance — a capture landing in Processed above the readiness line, found only by an unrelated request — plus three hand-anchored appends in the session that processed this.

#### The four-skills admission test rejects a rule that fires when NO skill is running, for the wrong reason [four-skills-test-cannot-admit-a-no-skill-rule]
Filed 2026-08-15 by Claude while processing [post-close-tail-state], from the admission problem that item hit and worked around.

**The test and what it was built to do.** `skill-nonspecific-rules.md` admits a rule only if it fires in all four skills, and its name states that test. The purpose is sound and not in question: it keeps a rule belonging to one skill out of the file every session pays for, and pushes it down into that skill's own doc where it costs only the sessions that run it.

**The gap.** A rule governing conduct when *no* skill is running fails that test — it fires in zero of four, not four of four — so the test rejects it. But for the opposite of the intended reason: the rule is not narrow, it is *wider* than any skill, and the always-loaded file is the only place reaching a session outside a skill at all. A test written to catch over-specific rules is silently catching over-general ones too, and the two are indistinguishable at the point the test is applied, because both answer "no".

**The recorded instance.** [post-close-tail-state] carried a clause about Claude routing an informal verification urge into a skill. That clause fires in the post-close tail, when no skill is running. The item's own prose names the problem and works around it by siting the clause in `done.md` instead. That workaround is sound there and does not generalise: it happens to have a doc the tail has just read, and a rule firing outside a skill will not always have one.

**Why this is worth settling rather than working around each time.** The always-loaded file is loaded at session start and governs every reply, including conversation with no skill running — `CLAUDE.md` says so explicitly. So the file's actual scope is already wider than its admission test describes. The test and the file disagree about what the file is for, and the test is the one that gets applied.

**Settled 2026-08-17: add a limb, do not restate the test.** "Fires whatever is running" would be vaguer than the enumeration it replaced and easier to talk oneself into. The enumeration stays and the missing case is appended: a rule earns the always-loaded file if it fires in all four skills **and** in conversation with no skill running. That is a fifth condition, so admission control is tightened rather than weakened — which answers the item's one real risk in the opposite direction to the way it was posed.

**The other two questions fall out of it.** A no-skill rule needs no separate home: the always-loaded file already is that home, being the only thing loaded when nothing is running. And the filename stays — "skill-nonspecific" already means not tied to a skill.

**The build.** Two sentences. `plugin/throughliner/docs-b/skill-nonspecific-rules.md`'s opening admission test gains the no-skill limb; `CLAUDE.md`'s distribution clause, which states the same test, is reworded to match so the two cannot disagree. Host-only — consumers never author method rules.

Rule gate: run — admitted as a limb on the existing admission test, which already fixes what earns a place in the always-loaded file; no freestanding rule and no slot spent, since it constrains authoring rather than conduct. Nothing evicted. Failure evidence is one recorded instance: [post-close-tail-state] hit the gap and worked around it by siting its clause in a doc that happened to be read at the right moment, which does not generalise.

Relates to [post-close-tail-state], which hit this and worked around it, and to [freestanding-rules-that-should-be-subordinate], the same gate examined from a different side.

#### The README-sync obligation fires at the close, after scope is locked, so the file it names is always out of scope [readme-sync-fires-after-scope-locks]
Filed 2026-08-16 by Claude at the close of the twenty-one-item run, from a denial the scope-lock produced live.

**What happened.** The close reached the README feature-list sync, which `CLAUDE.md` says rides the SPEC-sync trigger: a change adding or removing a user-facing feature updates SPEC, and the same moment syncs README's "What it does" list. Three corrections were genuinely needed. **All three writes were denied**, because `README.md` was not in the run's file list. The user was asked and approved adding it, costing an exchange in a close that is supposed to be quiet.

**It is not a scoping mistake, which is what makes it structural.** /next self-scopes by reading the items it is about to build and working out which files they change. Not one of the twenty-one items named `README.md`, and none should have: each was scoped to its own change, and the README obligation is a *consequence* of several together. So the file could not have entered the list at scope-lock time by any correct application of the rule.

**The three corrections it was blocked from making**, as evidence the trigger is real: /setup's description missed the privacy option and public-repository offer built this run; the hands-off/freeform description still gave the machinery repair as the definition rather than one example; and the isolation paragraph described advice about running two conversations at once that this same run deleted from the hook.

**Why the third matters most.** It is stale text about a withdrawn permission — the family the user reacted to earlier the same day when she met an FAQ entry claiming two-chat coordination was supported, in her words: *it "has NEVER successfully happened and EVERY time we have tried to ship that behaviour, it has fallen over."* A sync obligation that structurally cannot fire is how that text survives.

**To settle at processing, and the obvious fix has a cost.** Adding `README.md` to every run's file list by default would work and would widen every build's scope permanently, the opposite of what the lock is for. Two narrower shapes: the close could be permitted to add a file when a *close obligation* names it, a small named exception rather than a standing widening; or `README.md` could join the standing list `pre_tool_use.py` keeps for planning chats, on the host-only-by-residence reasoning that admitted `plugin.json` this run — except README is not host-only, so that reasoning does not transfer and this option is probably wrong.

**Same shape as [scope-lock-blocks-the-rezip], built this run**: a legitimate, required write with no permitted moment to make it. Relates to that item, and to [scope-lock-denies-claude-md], the same complaint one document over.

**Settled 2026-08-17 on the first of the two narrow shapes, with one change that makes it implementable.** "The close may add a file when a close obligation names it" cannot be checked by the hook, which has no way to know which obligation fired. But the obligations are fixed and written down, so the files they name are knowable in advance.

**The build.** `pre_tool_use.py` gains a **close-phase standing permitted set** — the files the method's own close obligations name, `README.md` among them — held separately from the build's agreed list and widening it not at all. A build still cannot touch `README.md`; a close can, because the close is where the method requires it. Same fix as [scope-lock-blocks-the-rezip]: a required write with no permitted moment gets one, narrowly, at the moment it is required.

**The cost, stated rather than discovered.** It is a second standing list to maintain. A close obligation added later that names a new file must be added to the list in the same build, or the identical denial recurs one file over.

**Your question about the rezip, answered by reading the hook rather than reasoning about it: it is the same shape, and it is already fixed.** `pre_tool_use.py` already permits `plugin/throughliner/.claude-plugin/plugin.json` unconditionally, added by [scope-lock-blocks-the-rezip], with the reasoning recorded in the code — a rezip runs after a close, the close has already deleted the build working file, so every chat a rezip could run in was classified as planning and its first step denied. Nothing further is needed there.

Rule gate: run — admitted as one entry added to `pre_tool_use.py`'s existing standing-list mechanism, which already carries a planning set and a single rezip path; no new mechanism and no always-loaded rule. Nothing evicted. Failure evidence is one recorded instance: three genuinely required README corrections denied at a close, costing an exchange in a close designed to be quiet, with one of the three being stale text about a withdrawn permission.

#### The rezip's version-bump rule picks a number that already exists whenever a push has run since the last rezip [rezip-bump-collides-after-a-push]
Filed 2026-08-14 by Claude while running a rezip, from the rule misfiring on that run. Filed after the last committed close, so it belongs to no committed session record.
**The two rules disagree, and each is right alone.** The rezip's first step says read the current version and increment the test suffix, "or start at `-test1` if the base carries no suffix". The push's first step strips the suffix, so the committed version always carries none. So every rezip following a push reads a bare version and takes the start-at-`-test1` branch — naming a build that already exists in the plugin cache.
**What that costs, which is worse than an untidy number.** The rezip exists to make the installed host match the source, and the update command matches on the **version string**. Re-installing a string the CLI has seen is the silent no-op the bump rule was written to prevent: it reports success, re-snapshots nothing, and the session carries on believing it runs new code. That failure already happened on 2026-08-09 and cost most of a session.
**How it was avoided this time, which is not a fix.** The cache directory was listed before choosing — `1.20.0-test1`, `-test2` and `-test3` were present, so `-test4` was used. That worked because the cache was checked, and nothing in the ritual says to check it. The content-stamp comparison at step 6 would have caught the no-op afterwards — a real backstop, but a late one.
**Second live instance, 2026-08-15**, at the rezip after that day's /next close. `plugin.json` again read `1.20.0` because the close's push cleaned it, so the ritual again named `-test1` — which the cache showed as long gone, along with `-test2` through `-test7`. `-test8` was used. Twice wrong the same way, twice saved by the cache listing: a standing defect, not a one-off. Any rezip following a push hits it, and that is the order the ritual prescribes.
**What to weigh at processing.** Whether step 1 should read the highest existing suffix from the plugin cache rather than `plugin.json` (the cache is what the CLI matches against, so it's authoritative here); or whether the reset should preserve the suffix somewhere the next rezip can read; or whether the start-at-`-test1` branch should simply be deleted, since after the first rezip on any release line it is never right. Also decide whether the release bump resets the test counter, since a new release line genuinely has no prior test builds.
**Settled 2026-08-17, from your observation that the rezip has been getting steadily more complex and that tying it to the push was a habit rather than a requirement.** You now rezip at every /next, so a per-rezip judgment is paid constantly rather than occasionally.

**What was checked before deciding, because Claude's first hypothesis was wrong.** The `-testN` suffix is not merely a label that could be dropped: `claude plugin update` matches on the version string, so an unchanged version reports "already at the latest" and re-snapshots nothing. The bump is what forces the install.

**The build.** `resources/release-ritual.md`'s rezip step 1 stops reading the next number from `plugin.json` and reads it from the installed builds in the plugin cache, taking the highest present and adding one. The start-at-`-test1` branch is deleted outright — it is the branch that misfires, and with the cache as the source there is nothing for it to do. `CLAUDE.md`'s push clause is untouched.

**Why this over full decoupling.** The alternative was to stop stripping at the push and strip at the release instead, which removes the coupling entirely. It was refused because the committed version would then carry a test suffix between releases, and a `-testN` version reaching the public remote has already happened once and was treated as a defect. This keeps the remote clean, removes the per-rezip judgment, and changes one step's wording rather than what the push does.

**It makes the rule match the practice.** Both recorded misfires were avoided by listing the cache, which nothing in the ritual asked for. Writing that in is the fix.

Rule gate: run — admitted as a rewording of the rezip's existing step 1, which already says where the next version number comes from; no freestanding rule, no new mechanism, and nothing always-loaded. **The eviction is the start-at-`-test1` branch, deleted rather than left standing.** Failure evidence is two recorded instances, 2026-08-14 and 2026-08-15, both saved only by an unwritten habit.

**Files:** `resources/release-ritual.md`, the rezip's step 1. Host-only. Relates to [push-clean-breaks-the-content-stamp], which is the other consequence of the same coupling and is **not** settled by this.

#### The push's version-clean makes the content stamp report the host as stale immediately after every rezip [push-clean-breaks-the-content-stamp]
Filed 2026-08-13 by Claude, measured live in its own post-close tail. Filed after the last committed close, so it belongs to no committed session record. Host-only.
**The two rules that collide, both correct in isolation.** The rezip bumps `plugin.json` to a `-testN` version and installs that snapshot; the push then resets the suffix so a test marker never reaches the remote. Separately, `session_start` publishes a content stamp of the installed plugin, and CLAUDE.md tells sessions to compare it against `content_stamp()` over `plugin/throughliner/` — a match meaning host-side changes are live.
**The measurement, taken rather than reasoned about.** Immediately after installing, source and installed stamps both read `b4bb37b9c1b6`. After the push's version-clean and no other edit, source read `654c88680de8` against an installed `b4bb37b9c1b6`. Nothing about the host changed; the only differing byte is the version string inside a file the stamp hashes.
**Why it matters rather than being cosmetic.** The mismatch is documented to mean "it hasn't been reinstalled since the most recent host-side change" — false here, and false in exactly the sessions most likely to be checking, namely the ones right after a rezip. A check that reports a wrong answer in its most common case is the cry-wolf shape this project has repealed measures for before.
**Why it may have gone unnoticed.** A rezip is usually followed by a release, which bumps to a clean version *and* reinstalls, so the stamps re-converge. The rezip-then-push-without-release path is what exposes it, and this session took it.
**Settled 2026-08-17: exclude the `version` key, not the file.** The version string is the one field the two rituals deliberately disagree about — the rezip sets it, the push resets it, and neither changes what the plugin does. Excluding the file wholesale was refused on the item's own objection: a renamed plugin or an altered description would then become invisible to a stamp built to catch edits that bump no version.

**The build.** `content_stamp()` in `plugin/throughliner/hooks/session_start.py` reads `plugin.json` as JSON, drops the `version` key, and hashes the rest. One function, run on both sides, so the two cannot disagree. `CLAUDE.md`'s description of the stamp and `resources/release-ritual.md`'s stamp-comparison step are reworded to say what is excluded and why.

**One consequence, written down rather than discovered later.** A pure release bump, where only the version changes, will no longer move the stamp. That is correct rather than a loss: the stamp answers whether the installed host matches the source, and in that case it does.

Rule gate: run — admitted as a narrowing of the existing `content_stamp()` definition, which already fixes what the stamp covers; no freestanding rule, no new mechanism, nothing always-loaded. Nothing evicted. Failure evidence is one measured instance: identical stamps immediately after installing, then `654c88680de8` against `b4bb37b9c1b6` after the version-clean and no other edit.
**Files (rough):** `plugin/throughliner/hooks/session_start.py` (`content_stamp`), `CLAUDE.md` (the stamp's description), `resources/release-ritual.md`. Host-only — consumers never rezip. Relates to [py-dash-c-escapes-the-script-write-guard], filed from the same tail.

#### A planning session cannot edit CLAUDE.md, which is where planning sessions author rules [scope-lock-denies-claude-md]
Filed 2026-08-15 by Claude while reading `pre_tool_use.py` to design the fix for [scope-lock-blocks-setup]; raised with the user first and filed on her instruction. **A third instance of the same oversight, or intended behaviour — which it is has not been established, and this item must not assume.**

**What is true of the code.** The standing list is QUEUE.md, SPEC.md, `LOG/`, `FAQ/`, `resources/research/`, the memory directory, the scratchpad and `INBOX/`. `CLAUDE.md` is not on it, so a planning session's edit to it is denied outright.

**Why that looks wrong here.** In this project `CLAUDE.md` holds the rule gate, the release rituals and most of the method's operative rules, and /plan is where rules are authored — the gate's design argument is that only /plan can refuse a rule, because at /plan nothing has been built. A planning session that runs the gate, admits a rule, then cannot write it has to queue the write as a build, putting the authoring back into a build session: the placement the gate explicitly rejects.

**Why it may nonetheless be right.** `CLAUDE.md` governs how Claude works on the project, and letting a planning session rewrite its own governing document without the change passing through a build is a real hazard — arguably bigger than the inconvenience above. The scope-lock's stated purpose is that work outside the planning surface is queued rather than done, and rule text may simply be work.

**Settled 2026-08-17: the lock is right, and this is intended behaviour rather than a fourth oversight.** The item conflates deciding with writing. The gate runs at the keep-step and its output is a **disposition on the queue item**; the rule text is written by the build that item schedules. What the gate rejects is a build deciding whether a rule may exist — not a build typing out a rule /plan already admitted.

**The evidence is the session that settled it.** Fifteen rule changes were dispositioned here at the keep-step and every one queued its text as a build. Nothing was blocked and no decision moved downstream.

**And it is genuinely unlike the three fixed the same day.** [scope-lock-blocks-the-rezip], [readme-sync-fires-after-scope-locks] and the `plugin.json` path were required writes with no permitted moment anywhere in the method. This write has a proper home.

**The build, which is what remains.** A comment in `pre_tool_use.py` beside the standing list saying why `CLAUDE.md` is excluded, and a clause in the gate's account in `CLAUDE.md` stating that the disposition is /plan's and the text is the build's. Host-only, and it changes no permission.

**Why it is worth writing at all.** The question has now been raised three times from the same reading of the same code, because nothing records the answer. A denial with no stated reason gets re-litigated by every session that meets it.

Rule gate: run — no rule authored or amended in shape; **the disposition is a refusal**, of a proposed permission change, plus a clarification of an existing rule's account. Nothing evicted, nothing added to the standing list.

#### Work that waits on a GROUP of items has no way to say so, so it cannot be held at all [blocked-by-cannot-express-a-group-condition]
Filed 2026-08-15 by Claude, from the item it stopped in the same planning session.

**What happened.** [law-prose-restyle] was processed, scoped and given an acceptance test, then could not be placed. Its real gate is a condition over a group — it runs once the cleanup's groups A and C are clear, around seven items — and `Blocked by:` takes exactly one slug. Any single value would have reported the item liftable the moment that one item shipped, with the rest outstanding, and the below-the-line revisit trusts the field. So the item went back to Unprocessed carrying a finished design, purely because there was nowhere to write its condition.

**Why a proxy blocker is worse than none.** The revisit reads `Blocked by:` and proposes a lift when the named item ships. A field that resolves early does not merely fail to help — it produces a wrong lift, and the lift is a clearing move, so the item would reach the ready region and be built out of order by an unattended run. A missing field at least leaves the work in Unprocessed where a human meets it again.

**Why the existing rules do not answer this, checked first.** The method says a thing in the world that work waits on is filed as its own queue item, and that is right — it turned an invisible wait-sentence into visible work. But it assumes the awaited thing is *one* thing. "This group is finished" is not a thing that can be filed: filing it would create a tracking item carrying no work of its own, which the red-flag rules ban everywhere else for the same reason.

**Settled 2026-08-17 on the first of the three shapes, with the other two refused on the record.**

**The build: `Blocked by:` accepts several slugs and the item lifts only when all of them resolve.** An extension of a field that already exists rather than a new mechanism; the lint already parses one slug, and the revisit already asks one question per held item.

**The named-group shape is refused** — it is a new state with its own lifecycle, and inventing states is the failure this method has caught repeatedly.

**The do-nothing shape is refused too, and it was the tempting one** because it costs nothing: leave group-gated work in Unprocessed and let the revisit read its prose. It misfiles designed, buildable work as a capture, and reading a wait out of prose is precisely what `Blocked by:` was built to replace — recorded in this item already, where one item sat shelved for weeks because its wait was a sentence nobody could see as work.

**The ripple, traced by grep before the file list was written, as a hook-enforced format change requires.** Live sites: `post_tool_use.py`'s lint, `queue_digest.py`, `session_start.py`'s dependency facts, `reorder_queue.py`, `plan.md`, `done-plan.md`, `setup.md`, `skill-nonspecific-rules.md`'s line-format block, `faq-template.md` and `FAQ/faq.md`, `SPEC.md`, `CLAUDE.md`, and three suites under `resources/testing/`.

**The cost is stated because it is the real objection, and it was accepted knowingly:** about fifteen live files for a problem that has arisen once. Your decision, given the alternative is work that cannot be held at all.

Rule gate: run — admitted as a widening of the existing `Blocked by:` field, which already carries the held relationship; no freestanding rule and no new state. **Two alternatives refused outright**, both recorded above. Failure evidence is one recorded instance, and the item it stopped is named in this item's own filing line.

**Relates to [standing-audit-programme]**, where the cleanup's groups are enumerated, and to [law-prose-restyle], the item that exposed this.

#### Nothing triages waiting mail on its own, so the cost recurs on every message and only the user breaks the loop [mail-triage-depends-on-the-user-noticing]
**Raised by you 2026-08-16 at the close, in your own words:** *"every message that lands in inbox will have to be triaged to captures again and nothing automatically captures that it leaves it up to me"*.

**The loop, as it ran this session.** Two messages arrived mid-chat. Mail arriving mid-session waits for the next session start, so nothing triaged them. They stayed in `INBOX/`, `session_start` delivers waiting mail in full, and the briefing grew past the size a shipped test asserts. The close ran that test, failed, and halted the commit. **What broke the loop was you telling Claude to file them as captures and archive them.** Nothing in the method did that, and nothing would have.

**Why the sites that look like they cover this do not.** /plan and /next both open mail at their openings — but only mail already waiting when the session started, and only if one of those skills is run. A chat that runs neither, or one where mail lands after the opening, leaves it sitting. The close has no mail step at all. So triage depends on a session happening to begin after the mail arrives *and* happening to be /plan or /next.

**This is the siteless-mechanism failure, the fifth or sixth recorded instance.** A duty exists, nothing owns the moment it fires, and the gap is invisible until a person notices — exactly what the queue's history says about the dispositions listing, the rule-corpus checks, and the wind-down re-scan.

**What makes it worse than an unrun check.** The skipped triage produces a *failing test at a later close*, landing on whoever is committing, with a cause several steps removed from anything they did. This session diagnosed it in three exchanges, one of which was Claude asserting a wrong explanation.

**Settled 2026-08-17. The build is one step at the close: triage any waiting mail through the standard three-way routing, then archive it** — the same thing /plan and /next already do at their openings. The close is the one skill that always runs, which is the argument that sited the wind-down re-scan there, and this is the same siteless-duty shape.

**The second question needed no decision: archiving already follows triage.** The routing procedure moves a message to `INBOX/archive/` as part of routing it. The gap was only that triage never happened.

**The third is overtaken by [inbox-size-contradicts-the-payload-cap], settled the same day.** Message bodies leave the session briefing entirely and become a directive plus a check, so a pile of unread mail can no longer push the briefing past the limit. That item still stands, but its justification is now the honest-SPEC half rather than the size crisis.

**Your ordering instruction was not followed, and it is recorded rather than glossed.** You asked at the close that the cap item wait until this one was settled. The cap item was processed first, without that instruction being checked. The outcome is unaffected — the two settlements agree — but the order was Claude's error, not a decision.

Rule gate: run — admitted as a step added to `done.md`'s existing close, which already carries the wind-down re-scan for the same reason; no freestanding rule and no always-loaded slot spent. Nothing evicted. Failure evidence is one recorded instance: two messages sat untriaged, the briefing outgrew a shipped test, and a close halted on a failure several steps removed from anything the person committing had done — broken only by the user telling Claude to file them.

Relates to [inbox-size-contradicts-the-payload-cap] and [inbox-delivery-unconfirmed].

#### The `Also in this chat` section has no defined home when a close writes one entry per item [also-in-this-chat-has-no-home-in-a-multi-item-close]
Filed 2026-08-16 by Claude at the close that first applied the rule, from a gap found while applying it.

**What shipped this morning.** [log-records-the-run-not-the-chat] added an `Also in this chat:` section to the shared LOG entry format, for corrections given, decisions reached in conversation, errors made and fixed, and hand work between runs — the class belonging to no work item.

**What it does not say: where the section goes when the close writes twenty-one entries.** The rule was authored against one entry per session, which is what a planning close writes. A build close writes **one entry per built item**, and the chat-level content belongs to none of them. On every entry duplicates one text twenty-one times; on none loses it.

**What this close did, as a stopgap rather than a decision.** It went on the first item's entry, with a sentence saying it carries the chat-level record for the whole session. That works and is arbitrary — a later reader has no rule telling them which entry to open, and the index line had to flag it explicitly for that reason.

**Settled 2026-08-17: its own entry, named for the chat rather than a slug.**

**The build.** `done.md`'s LOG entry format gains one condition. A close writing a **single** entry keeps `Also in this chat:` inline, unchanged — which is every planning close, so that path is untouched. A close writing **several** entries writes the chat-level record as its own entry, with its own line in `LOG/index.md`.

**Why this over the two placement conventions.** Both alternatives — the last entry written, or naming which entry carries it — attach chat-level content to an item it does not belong to, and then need a convention for a reader to find it. This matches what the content is: it belongs to the chat, so it gets a chat-level record, findable the ordinary way from its own index line. It is not a new kind of artifact either, only a log entry with a different filename, so the index format is unchanged.

**The condition falls out rather than being an exception**, which is what the authoring standard asks for: the rule reads off how many entries the close writes, and needs no carve-out.

**The cost:** one extra file and one extra index line per multi-item close, against duplicating one text across twenty-one entries or losing it.

Rule gate: run — admitted as a condition on the `Also in this chat:` section shipped the day before, which already fixes what that section carries; no freestanding rule and no always-loaded slot spent. Nothing evicted. Failure evidence is one recorded instance, in the close that first applied the parent rule and had to improvise a placement it recorded as arbitrary.

**One thing worth weighing that is not a placement question.** A planning close already writes a single entry, so the rule works there unchanged. This gap exists only for build and audit closes, which is where the method's largest sessions are — so the case it fails on is the one it most exists for.

Relates to [log-records-the-run-not-the-chat], which shipped it, and to [close-cost-scales-with-run-size], which records why one entry per item is not negotiable.

#### The word bands fire on the median artifact in four shapes out of five [bands-fire-on-the-median-artifact]
Filed 2026-08-16 by the audit that first ran the measurement, in the same session that shipped the bands.

**Measured medians against their ceilings:** captures 329 against 265, work items 412 against 345, build entries 400 against 345, index lines 62 against 60. Only plan entries sit under, at 408 against 485.

So the breach action does not fire on an outlier — it fires on the typical case, and will keep firing on nearly every write for as long as the corpus takes to come down. That is the cry-wolf shape this project has repealed measures for twice, arriving this time from the figures rather than from the wording.

**Settled 2026-08-17, together with the four sibling captures from the same measurement. Your concern is the governing one and it is answered in the text rather than in conversation.** You put it as: the July figures may have been elevated into THE standard when they are only what we used to have — real evidence that the work can be done at lower counts, and no evidence at all about what an ideal length is.

**That is conceded, and written into the rule.** The bands mark lengths **demonstrated to be sufficient**, not ideal ones. The method's own limit rule already says a stated derivation makes a figure traceable and revisable rather than correct; what was missing is that sentence attached to these bands, so it does not have to be re-argued.

**The honest ambiguity, stated because it cannot be resolved from the firing rate.** A band firing on the typical artifact is equally consistent with a bloated corpus and with a band set too tight. Nothing in the measurement distinguishes them.

**What pushes against the too-tight reading is the second population, not the first.** Measured across 157 entries from the project's earlier life, in the combined pre-split logs: median 183, mean 197, maximum 656 — inside the 115–229 build-entry band. (An earlier estimate of "roughly 250–460" for the same entries was wrong on the low side, which makes August's build median of 485 a 2.7-fold rise rather than 1.5.) Two independent samples agreeing that the work was done at that length is the strongest evidence available short of an outcome measure — sufficiency shown twice, never optimality.

**The transition, settled: the advisory says its piece once per run, not on every write.** That removes the constant firing without weakening the figure, and it is the cry-wolf remedy this project already uses.

Relates to [written-shape-word-bands], shipped 2026-08-16.

#### A work item accretes past its band between capture and build, and no band reaches that [work-items-accrete-past-their-band]
Filed 2026-08-16 by the audit that first ran the measurement.

**Measured:** items first filed in August grew a median of 145 words between capture and Processed, with a maximum of 4,425. July's median growth was zero, so the accretion is recent.

**The bands govern the moment text is written.** An item can pass its band at capture, be enriched at five successive planning sessions, and reach the build at three times its ceiling without any single write ever breaching anything. Every author was in band; the artifact is not.

The keep-step's band read partly covers this, since re-processing rewrites the item — but only where a session rewrites the whole block rather than appending a paragraph to it, and appending is the common move.

**Settled 2026-08-17: the band applies to the item as it stands, not to the text being added**, and it is read at the keep-step where the item is already in front of you. An author whose own paragraph is short has still produced an over-length item, and the item is what gets read.

**Demonstrated in the session that settled it.** Every item processed that day was extended by appending a settlement paragraph. No single write came near a band; several items passed their ceiling. Relates to [written-shape-word-bands] and to [bands-fire-on-the-median-artifact], where the shared framing is settled.

#### An index line's length is a toll paid on every retrieve, not a page a reader skims [index-line-length-is-a-toll-on-every-retrieve]
Filed 2026-08-16 by the audit that first ran the measurement. **The reframing is the user's, in her own words:** *"the reader is Claude though for index. not a human. the human accesses log mostly by asking Claude to read it. so it's not like a table of contents in a book."* The measurement and the figures are Claude's; the first draft argued from human scannability and was wrong about who reads it.

**Measured:** 306 of 594 index lines are over ceiling, median 62 against a 20–40 band. At the current median the index runs about 37,000 words; at the band top it would run about 24,000.

The index is read in full, by Claude, to decide which single entry to open — so its total length is a fixed cost on every lookup rather than something a reader skips past. The extreme case shows what the breach buys: a 337-word line pointing at a 1,710-word entry, where reading the line costs a fifth of simply opening the entry it exists to save you from opening.

`skill-nonspecific-rules.md` already states that the index is Claude-facing and that terseness for human scannability is not the criterion. What it does not state is this cost model, which is the argument the band actually rests on.

**Settled 2026-08-17: write the cost model into the rule.** The index is read in full, by Claude, on every retrieve, so its total length is a fixed toll rather than something a reader skims past — and that, not scannability, is what the band is for. The extreme case is the argument in one line: a 337-word entry pointing at a 1,710-word file, where reading the pointer costs a fifth of opening the thing it exists to save you opening.

**It also removes an apparent contradiction rather than adding a rule.** The same file says the index has no length cap of any kind, absolute or proportional, while the band gives it 20–40 words. Both stand once the cost model is stated: the band is what the line costs the retrieve, not a cap on what it may say. Shares its framing with [bands-fire-on-the-median-artifact].

#### The plan-entry breach action says split per decision without saying where a split lands [plan-entry-split-action-underspecified]
Filed 2026-08-16 by the audit that first ran the measurement.

**Planning entries are the fastest-growing shape measured:** July median 323 to August 901, a 2.8-fold rise, with a maximum of 3,658 words. Build entries rose 2.1-fold over the same span and captures 1.9-fold.

**The shipped breach action for a plan entry is "split per decision", and a build entry's is "split per item built".** The build case is well defined — an item is a named unit with its own slug and its own index line. A planning session's decisions reference each other, have no slugs of their own, and no rule says what the resulting files are named, how they cross-reference, or which one the index line points at.

So the shape under the most pressure has the least defined remedy.

**Settled 2026-08-17: a plan entry splits per item processed, exactly parallel to a build entry splitting per item built.** The premise that a planning session's decisions have no slugs is false — a planning decision **is** a disposition on a queue item, and that item carries a slug, its own file name and its own index line. So the build case's machinery applies unchanged, and nothing new is defined.

**What remains genuinely chat-level** — a correction given, an error found and fixed, a decision belonging to no item — has its own home already, settled the same day by [also-in-this-chat-has-no-home-in-a-multi-item-close]: its own entry named for the chat. Between the two, every part of an over-length planning entry has somewhere to go.

Shares its framing with [bands-fire-on-the-median-artifact], and relates to [written-shape-word-bands].

#### The digest stops replacing the read: it prints what only a script can compute, and the queue is read whole alongside it [digest-stops-replacing-the-read]
Raised by you 2026-08-17, from noticing that Claude seemed not to have read the whole queue and that the feeling was about a week old. Corroborated: `queue_digest.py` landed 2026-08-11, six days before.

**What is true today.** `plan.md`'s opening says to run the digest **instead of** reading QUEUE.md, and the always-loaded rule blesses that, calling a mechanical digest a stronger satisfaction of the read-the-whole-file duty than paging. The digest prints one line per item and deliberately omits the rationale prose.

**Why that costs the thing the single file exists for.** Your reasoning: the queue is one file because Claude reasons across items badly when they are split, and a digest of headings restores exactly that split — headings together, reasoning apart. **Blockers can be anywhere in the queue, and so can the right place to fold something in, so every item bears on any planning session** — and arguably on any /next, since ideation can happen anywhere and new work must be weighed against everything already queued.

**The live instance, from the session that raised it.** [mail-triage-depends-on-the-user-noticing] carried your instruction that [inbox-size-contradicts-the-payload-cap] should wait for it. The instruction was in the prose, not on the digest line, so the cap item was processed first.

**The measurement, which changes the cost argument.** The queue is 34,287 words across 75 items — 457 per item against a work-item band top of 229. At band it would be roughly 15,000 words, about 20,000 tokens, which is affordable to read whole at an opening. **So the word bands largely dissolve the reason the digest replaced the read.**

**But not the digest**, because half of what it prints cannot be got by reading: how long an item has been held, where a named blocker sits, which files two items both name, and whether an item's premise cites work that has shipped. Reading gives prose; the script gives computed facts.

**So the settlement is both, not either** — and the framing matters: this is not "fix the digest". The word-band items it waited on were settled the same day, so nothing holds it.

**The build — three sites, all of which currently say the digest replaces the read.** `plan.md`'s opening stops saying to run the digest *instead of* reading QUEUE.md and says both, digest first for the computed fields, then the file. `skill-nonspecific-rules.md`'s clause that a mechanical digest satisfies the read-the-whole-file duty **more strongly** than paging is narrowed rather than deleted: true for what the script computes, false for the prose. `SPEC.md`'s account of the opening is corrected to match, since it goes wrong the moment the other two change.

**The cost is the trade, accepted knowingly:** about 45,000 words to read at an opening today, roughly 20,000 once the bands bring lengths down. A conditional read was offered and refused in favour of every opening, on the ground that a condition would have to predict which items bear on each other — the thing the read exists to discover.

Rule gate: run — admitted as a narrowing of the existing digest instruction and of the always-loaded clause that blessed it; no freestanding rule and no new mechanism. **The eviction is the "instead of reading QUEUE.md" wording**, repealed outright. Failure evidence is one recorded instance in the session that raised it, plus the user noticing the behaviour change six days after the digest shipped without knowing a mechanism had changed.

**One thing not claimed.** Multi-file queues were far worse — your words: an absolute disaster. This is an occasional feel that something is wrong, and must not be written up as a failure of comparable size.

#### Two always-loaded rules say capture-first while plan.md says ask-first, and the always-loaded pair wins every time [capture-first-contradicts-ask-first]
Raised by you 2026-08-17, from noticing the behaviour was consistent across sessions rather than a one-off — *"in fact i thought it was what we had designed, that's how consistent it was."*

**The three sites.** `skill-nonspecific-rules.md` says a mid-session discovery not needed for the current work is "capture and continue — the common case", and that a Claude-raised capture closes by "confirm and resume, naming what you filed". Both presume the write already happened. `plan.md` says that when Claude raises something mid-planning it must ask once, **before any write**, whether to file it or work it now, and recommend working it now.

**Why the wrong one wins, mechanically.** The always-loaded file is read by every session; `plan.md` only by planning sessions. Two statements against one, in the file that always fires.

**Why it matters beyond tidiness.** Offering only the capture costs a write that is thrown away when the answer was "work it now", because the capture is then rewritten as a work item. Your point.

**Settled 2026-08-17 after reading the mechanism, which narrows the diagnosis: it is not a contradiction and no rule needs adjudicating.**

**The carve-out already exists and was never lost.** The always-loaded capture rule ends by saying that inside /plan both branches get an offer, and that a Claude-raised one asks once whether to file it or work it now. It landed on 2026-08-13 in the same build as the plan.md rule.

**Two defects in it, both small.** It omits **before any write**, which is the entire point of the plan.md version — and it is attached to a sentence that says to confirm and resume "naming what you filed", which presumes the write already happened. So it reads as guidance on *what to say after capturing* rather than on *asking before capturing*. Separately, the mid-session discovery rule still says a discovery not needed for the current work is "capture and continue — the common case", with nothing pointing at the /plan exception.

**That explains the consistency better than a contradiction would.** The right rule was not outvoted; it was written where it reads as being about wording rather than about sequence.

**The build.** In `plugin/throughliner/docs-b/skill-nonspecific-rules.md`: the /plan carve-out gains the ordering it was missing, and the mid-session-discovery block gains a pointer to it. `plan.md` is unchanged.

Rule gate: run — no rule authored or admitted; **the disposition is a correction to two existing statements**, one gaining an omitted clause and one gaining a cross-reference. Nothing evicted, no slot spent. Failure evidence is the behaviour being consistent enough across sessions that the user took it for the design.

#### An unprocessed capture has no way to express a dependency, so ordering there can only be prose [unprocessed-capture-cannot-hold-a-dependency]
Raised by you 2026-08-17, on noticing that a dependency Claude had just written into a capture's prose was one that should have been a field.

**What the format allows.** `Blocked by:` is defined for the held region below the readiness line, where it is required. A capture in Unprocessed has nowhere to put one, so a real dependency between two captures can only be a sentence.

**Two instances in one session, from opposite ends.** Your instruction that the payload-cap item wait on the mail item was prose, and the cap item was processed first against it. Claude's note that [digest-stops-replacing-the-read] waited on the word-band items was also prose, and was honoured only because you happened to ask for the bands first — chance, not mechanism.

**The method half-knows this already.** [mail-triage-depends-on-the-user-noticing] says in its own text that its ordering is "carried in prose because this sits in Unprocessed where no holding field exists". Nothing names it as a defect.

**Third member of a family, all live.** `Blocked by:` cannot express a group ([blocked-by-cannot-express-a-group-condition]), cannot reach another project ([cross-project-mail-versus-direct-captures]), and cannot exist in Unprocessed at all.

**Settled 2026-08-17: no new field. Your reframing is what settles it, and it defeated the field Claude proposed.**

**The dependency is not "process this after that".** It is that the work a capture may produce could block work described anywhere else in the queue — and **not every unprocessed item describes work at all; the work is often inferred and only becomes definite at processing.** So a field filled in at filing time would ask Claude to name a fix before anyone has designed one, using space meant for describing the problem. Your objection, and it is decisive: a rule requiring a possible fix at every capture bloats the capture and may record no input of yours at all.

**So the general case has no field-shaped answer**, and it does not need one: an undiscoverable dependency becomes visible when an item is processed, which is the moment [digest-stops-replacing-the-read] now covers by restoring the whole-queue read.

**The residual is the narrow case where an ordering is already KNOWN**, which is what both of today's instances were — stated knowledge, not inferred dependency. **The method already has the device: a relationship written as a slug in the prose of BOTH items**, so opening either surfaces it. The standing rule already says a relationship not written as a slug does not exist; what failed was writing it on one side only, so it survived by luck.

**The build.** One clause in `plugin/throughliner/docs-b/skill-nonspecific-rules.md` beside the existing slug-reference rule: where an ordering between two entries is known at the time, write it into both. No format change, nothing for the hooks to parse, no ripple.

**Two proposals refused.** A `Process after:` field, on your objection above. And permitting `Blocked by:` in Unprocessed, because it means "cannot be built until X ships" and would make the lint, the digest and the dependency facts wrong about a section they do not describe.

Rule gate: run — admitted as a clause on the existing slug-reference rule, which already governs how a relationship between entries is recorded; no freestanding rule and no slot spent. Nothing evicted. Failure evidence is two instances in one session, in opposite directions, each a known ordering written on one item only.

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

#### [user] Discord post: the ordering ladder cut from six rungs to three, and every rung now costs no judgment [discord-post-context-adjacency]
Captured by you 2026-08-12; the angle is yours — the ladder and how much it improves the workflow. **Subject replaced 2026-08-15 — see the correction below. The slug is unchanged because slugs are immutable.**

**The subject this post had was deleted before it was ever posted, and that is the correction.** It was written to announce the cheap-to-settle rung — "/plan offers you the work closest to what this session has already read". Commit `0e62afe` on 2026-08-15 cut the ladder from six rungs to three and deleted that rung, the rung-6 offer and the decay rung with it. The item was sitting **cleared to run** when found, so a /next run reaching it would have walked you through drafting and posting a public claim about a mechanism that no longer exists. Caught by reading the item during processing; the digest's placement check matches a fixed set of known phrases and does not reach this shape, which it says of itself.

**The replacement subject is the deletion, and it is the better post.** Six rungs became three: an uncleared red flag, then unblock-potential by citation count, then longest-first by line count. **Every surviving rung either reads a field the digest already computes or subtracts two line numbers**, so ordering costs no judgment at all. Longest-first was also re-grounded — on cost-of-reading rather than on length predicting how finished an item is, because the settling session's own data contradicted the latter.

**What makes it worth saying rather than a changelog line.** The honest version is about subtraction: three rungs asked Claude to weigh something, and weighing is where a mechanism quietly stops being reproducible. The tool got simpler and more predictable in the same move — a harder and more interesting claim than "we added a feature".

**A judgment for you at drafting time.** The before-picture is that some deleted rungs were things this project built, used, then decided were not carrying their weight. Whether that goes public is your call; it is what makes the change legible rather than arbitrary.

**Verify before posting, not merely before drafting.** Every claim must be true of the *installed* plugin at the moment it goes out. Compare the installed host's build stamp against the target's before you post, since the cut is committed but a host that has not been reinstalled still runs six rungs.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [ladder-rung-for-context-adjacent-items] shipped and has since been refined once — the offer now leads with a recommendation rather than a flat menu (`LOG/2026-08-12-context-adjacency-offer-is-a-flat-menu.md`, `e5d169b`). Draft against the refined behaviour. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries], which absorbed the item recording this.

**Paced 2026-08-14 on the user's decision: head of a one-post-per-day chain.** Her words: one a day, don't drown out the server. Nothing here is unready — pacing alone held it.

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

#### [audit] Classify every occurrence of "session" against the settled vocabulary, immediately before the corrections [session-occurrence-audit]
Filed 2026-08-17, absorbing five captures from [terminology-corpus-audit] that were deleted once their content was carried into this item and into [session-vocabulary-corrections].

**The vocabulary, settled by you on 2026-08-17 and recorded here because this item and the corrections both read it: a RUN is a command executing — a /plan run, a /next run — and a SESSION is the chat.** You chose it over two alternatives — a `<command>` session pattern, and keeping three named slots — because "session" is already in widespread use meaning the chat, so this splits the two ideas rather than adding qualifiers to a word doing two jobs. **Your correction to Claude's objection:** "the close" is residual language from a step that no longer exists, so it was no argument against anything.

**What the audit reads.** Every occurrence of "session" across the procedure docs, `faq-template.md` / `FAQ/faq.md` (185 each, the same document) and `SPEC.md` (88). Roughly 707 in all.

**What it produces.** One classification per occurrence: means the chat, means a run, or is correct as it stands and must be left alone. A stop-list is a constraint it inherits: "mid-session", "short session", "fresh session" and "isolated session" all correctly mean the chat and are left alone, as is `done.md`'s "session type", which classifies a chat rather than naming a run.

**Why an audit and not a script.** Finding the occurrences is a grep; deciding what each one means is judgment on every line. That is this project's own test for when an audit survives.

**Why it runs immediately before the corrections, not now.** [law-prose-restyle] rewrites the same files in between, so a list gathered today is stale before anything uses it.

**Why the existing survey is not enough.** [terminology-corpus-audit] enumerated collocations, not occurrences — a floor on how many meanings exist, never a ceiling — and never reached the FAQ or SPEC, which are the consumer-facing texts. The scale is measured: across five procedure docs, bare forms outnumber qualified ones by roughly nine to one — 134 bare against 29 qualified — so 134 judgment calls rather than substitutions sit in those files alone.

Blocked by: [law-prose-restyle]

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

#### Add a lightweight post-close "done delta" — commit everything since the last /done without a full-session rescan [done-delta-close]
Captured by you — filed after `fa2f8e5`. /done is expensive: the full close re-scans the whole session's discussion, runs the spec-sync gate, reorder, marker positioning, advisory management, LOG authoring, staleness sweep. When a /done already committed this session and the tail only filed a few captures, most steps no-op but Claude still pays the reading cost to *reach* each no-op. (Seen live 2026-08-01: a second /done banked six post-close captures; nearly every step was a silent no-op and the full path was still walked.)
**The idea:** a delta close handling only *everything since the last /done commit* — stage, write a light delta LOG entry, commit — **bounding the rescan to since-the-last-close** and skipping reorder/marker/advisory when nothing relevant changed.
**Coexists with, doesn't replace, the free path:** post-close captures already ride the next session's commit ([post-close-tail-state]), so doing nothing stays valid. The delta close is the explicit "bank it now, cheaply" option.
**Design questions (for /plan):**
- **Trigger:** separate mode/command, or auto-detected? Auto-detect is cleaner — /done notices a commit already happened this session — but that needs a reliable signal (session marker, or git log since session start).
- **Keep vs skip:** commit + light LOG entry kept; wind-down shrinks to since-last-commit; reorder/marker/advisory fire only if the delta touched them. Preserve the full close's safety without re-paying its cost.
- **LOG shape:** a fresh delta entry (as this session did with render-verify-and-captures.md) vs appending to the prior entry.
**Relates to:** [post-close-tail-state], the done-family dedup audit findings (done.md is already heavy — reuse the shared core, don't duplicate), and captures-filed-after-commit.
**Files (rough):** done.md (the delta path + trigger), possibly session_start.py if a session-commit marker is needed, SPEC/FAQ if user-visible.

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

#### Work that finishes in another project has no way to tell this one, so an item can sit ready long after it is done [cross-project-work-completes-invisibly]
Filed 2026-08-10 during a /next walk-through, at your instruction. Mixed authorship: you raised the question that found it — why the site was being edited from here when it belongs to another project — and the diagnosis is Claude's. Rides this session's commit.
**What happened.** [report-url-404] was a `[user]` line waiting on a page existing at flintcraft.tech/report, work on a different project. The page had been up for some time. Nothing here learned that, and the item sat in the cleared region as ready work until a /next walk-through fetched the URL and found it live.
**No harm this time, and that is not the point.** The item recorded an observable check, so the walk-through ran the check instead of asking whether the work was done — the check-the-world rule working as designed. The cost was one wasted run slot and a moment of reasonable confusion about whether Claude was reaching into another project.
**The general shape.** Any item whose completion happens outside this repo is invisible here until someone looks. An observable check rescues cases where "done" leaves a trace a fetch or file test can find. It rescues nothing where completion is visible only to the user or inside another project's records — the larger class.
**To settle at processing.** Whether the answer is an INBOX message from the doing project (the mechanism exists and this is close to what it's for), or whether observable checks are as far as this goes and the docs should say so. Weigh against [inbox-delivery-unconfirmed], which records that INBOX mail is fire-and-forget in both directions — a notification nobody is guaranteed to read would move this, not fix it. Note also that this project cannot write into another project's queue; the most it can do is post a message they have to read.
Relates to [inbox-delivery-unconfirmed], [inbox-mail-has-no-place-in-the-ladder] and [report-url-404] (the instance).

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

#### A user-named subset of items, once processed, has no stated shape — so the session reaches for the empty-queue gate and leans toward stopping [subset-done-has-no-stated-shape]
Filed 2026-08-13 by Claude from a live instance in this /plan session, caught by you. Filed after the last committed close, so it belongs to no committed session record.
**What happened.** You named three items at the opening. When the third was processed, Unprocessed still held 35 items, and the session offered "anything else to capture or discuss, or shall we close out?" — `plan.md`'s **neutral end-of-queue gate**, specified for the case where Unprocessed *empties*. You had to ask why continuing wasn't offered.
**The gap, a missing case rather than a misread one.** `plan.md` states the four routes once at the start of processing and specifies the end-of-queue gate for an empty queue. Between those sits an unhandled state: a user-named subset exhausted while the queue is not. Nothing says what the session does there, so the nearest gate gets reached for — and it names closing.
**Why that substitution is worse than a neutral miss.** The end-of-queue gate is carefully worded not to lean toward closing *given an empty queue*. Applied to a full one it stops being neutral: it silently reclassifies 35 unprocessed items as nothing left to do. The same failure the checkpoint recital was stripped back for.
**To settle at processing:** whether the fix is a stated shape for subset-exhausted (return to the ladder and present the next item, continuing as the default), or whether the end-of-queue gate should test that the queue is actually empty before it may be used. Relates to [close-invites-same-session-next] and [plan-gates-say-close-out-for-a-retired-phase] — three records of a close being offered where continuing was better.

#### A `Runs alone` item placed last can be overtaken indefinitely and never reached [runs-alone-at-the-end-can-be-starved]
Filed 2026-08-13 by Claude, from your question about why the rename hadn't happened. Filed after the last committed close, so it belongs to no committed session record.
**The live instance.** [rename-to-throughliner] is cleared to run and has been for some time. Not held, not blocked, and nothing is wrong with its placement — it carries `Runs alone` and sits last, exactly what `plan.md` prescribes for unrelated work so a run clears the buildable items before stopping. You had assumed it was stuck below the line; it never was.
**Why correct placement produces starvation anyway.** A run reaches a last-placed item only after everything ahead of it is built. Every planning session adds newly cleared work *ahead* of it, because that's where kept items land. So the position that guarantees a clean run also guarantees the item recedes each time the queue is worked. This session alone placed three items ahead of it.
**What makes it invisible.** Nothing reports how long an item has been cleared, and nothing may — a bare age threshold is the kind of invented number this project bans. The item isn't flagged by the digest, isn't held by any rule, and reads as healthy at every inspection. It surfaced only because you asked after it by name.
**To settle at processing, and both obvious answers are weak.** Placing `Runs alone` work first inverts the problem — it stops every run at the top. Reporting cleared-age needs an indefensible threshold. Weigh whether the honest fix is narrative: /plan naming, when it places work into an already-cleared region, that it has just placed something ahead of a `Runs alone` item. Relates to [digest-reports-computed-fields-not-summaries] and [held-items-invisible-during-normal-use].

#### The project's two Claude Code config files point at a folder layout that has not existed for months [claude-config-points-at-dead-layout]
Filed 2026-08-13 by Claude during the identity-rename build. Filed after the last committed close, so it belongs to no committed session record.
**What was found, and it is not what the rename item predicted.** [rename-to-throughliner] listed `.claude/launch.json` and `.claude/settings.local.json` among the files the folder rename would invalidate. Neither was, because neither pointed at `plugin/si-plugin`. They point at a much older layout — a top-level `sovereign-implementer/` folder with `planning/`, `build-log/` and `Dev/Resources/` — under a user path (`C:\Users\Alex\...`) that is no longer this machine's. That folder hasn't existed for a long time.
**What this means in practice.** `launch.json` declares one dev-server configuration serving `sovereign-implementer/crash-course`, an absent directory, so it cannot start. `settings.local.json` carries roughly fifteen permission allowlist entries naming absolute paths into that dead layout; a permission entry for a path that cannot occur never matches, so they're inert rather than harmful. Two live entries in the same file *did* name the real `plugin/si-plugin/scripts/reorder_queue.py` and were corrected in the rename build.
**Why it is captured rather than fixed there.** The rename item's work is the identity change, and none of this is that — the strings were stale for an unrelated reason, before the rename started. Fixing them means deciding what `launch.json` should serve now, or whether the project needs one, which is a decision rather than a substitution.
**To settle at processing.** Whether `launch.json` is deleted or repointed; whether the dead allowlist entries are pruned (harmless, but they make the file hard to read, and this user's stated difficulty is scanning dense lists); and whether anything else in `.claude/` assumes the old layout.
**Files (rough):** `.claude/launch.json`, `.claude/settings.local.json`. Host-only — a consumer's `.claude/` is their own.

#### A one-line reply cannot be told apart from a suggestion chip, so every user-credit resting on one is unverifiable [chip-replies-are-indistinguishable-from-user-authorship]
Captured by you (2026-08-13). Your objection, rendered in Claude's words rather than quoted: those are ALL chip answers, i don't write like that. The metadata check and containment test are Claude's.
**What was being checked.** You asked where `Runs alone` came from, saying you didn't remember okaying it. The item that introduced it recorded two user-credits: that you directed settling it before the next run, and that the marker was "the route, chosen by the user". Claude read the raw transcript, judged the first accurate and the second wrong, and said so confidently. You then said all those replies were chips.
**The metadata settles it, against the record rather than for it.** Every user message in `.claude/projects/<slug>/*.jsonl` carries `origin: {kind: "human"}` and `promptSource: "sdk"`. Messages you plainly typed — including ones carrying your own typos — are byte-for-byte indistinguishable from one-line affirmatives. The transcript records who **sent** a message, never who **composed** it. So the primary evidence this project relies on for provenance cannot answer the provenance question.
**The loop, which makes this structural rather than a discipline failure.** Claude proposes a design; the harness renders Claude's proposal as a suggestion chip; the user clicks it to move on; Claude records "chosen by the user, in their own words". Claude's recommendation is laundered into the user's authorship, and the artifact is indistinguishable from a real user decision — to a later session, to an audit, and to the session that wrote it. It was believed and asserted twice in the exchange that discovered it.
**The one signal that still works is content, not metadata.** A real user message contains something Claude's preceding message didn't: a disagreement, a new fact, a redirect, a question, a correction. A reply wholly contained in what Claude just proposed cannot evidence authorship, because the chip could have supplied every word. Checkable with no harness support and no new field.
**To settle at processing:** whether the credit rule in the always-loaded rules gains that containment test explicitly; whether existing credits can be audited by it or should be treated as unreliable in bulk; and whether a wrongly-credited decision needs re-deciding rather than only re-labelling — the `Runs alone` marker is shipped and may be entirely right on its merits, a separate question from who chose it.
**What this does NOT establish.** That the decisions were bad. `Runs alone` may be correct; the objection is to the record claiming an authorship it cannot support.

**The user-side answer, added 2026-08-17 and raised by you — the half no mechanism can supply.** Your realisation, rendered in Claude's words: answering in the affirmative with a chip reads as understanding and agreement, so it should never be used to defer; when deferring to Claude's judgement, say **"as you recommend"** instead. That makes the deferral explicit at the one point where the ambiguity is otherwise unresolvable.

**Claude cannot detect a chip reply, so a one-time session notice was designed and refused.** The proposal was that Claude say once per session that a chip must not be used to defer. It fires on a detection that does not exist — a chip reply is byte-identical to typed text, which is this item's whole finding — so it would have to fire at every user every session, including those who never use the chips. **Your own words on it: "seems a bit much."**

**Why folding it here rather than filing it separately.** This item records the problem as unsolvable from Claude's side. The answer belongs beside the problem, so a later session reading the item finds both. Nothing is built for it.
**Files (rough):** the provenance rules in `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (Captures, provenance; and the rationale-provenance clause). Shipped, not host-only — every consumer's queue carries these credits. Makes [invented-rationale-compounds-past-the-shipped-rule] structural rather than a discipline problem, and relates to [message-ending-drives-the-suggestion-chip] and [runs-alone-at-the-end-can-be-starved].

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

**Files: not yet derivable, which is the point of not keeping it.** Likely `resources/method-compliance-audit-checklist.md`, `resources/rule_signals.py`, and `CLAUDE.md` for whatever trigger the set gets. Host-only. Relates to [law-prose-restyle], the last piece of cleanup this set follows, and to [rule-admission-has-no-independent-approver] for the restyle-audits-itself risk.

#### No pass looks for freestanding rules that should be subordinate units of a parent [freestanding-rules-that-should-be-subordinate]
**Captured by you 2026-08-14, in your own words: "are you saying we've added rules that now contradict other rules? Shouldn't they be conditions under other rules according to the self authoring rules?"** Raised about one case and it generalises, which is why it is filed rather than left inside that case.

**The specific case, fixed on the spot.** A design for migrating the output style's written-file-length rule proposed wording it carefully so it couldn't be misread against the two standing rules saying the opposite — completeness beats compression for captures, and no length cap of any kind for index lines. That is the *explanation* remedy the admission rule rejects in favour of structure. It was rewritten to require naming the parent and landing the rule as a subordinate unit, in [output-style-earns-its-place].

**The general gap, and no existing pass covers it.** The admission rule requires naming a parent and shipping a rule as a subordinate unit wherever that holds, with freestanding as the fallback. That governs rules being *authored*. Nothing has ever applied it backwards to the rules already shipped. So the corpus plausibly holds freestanding rules that should be subordinate clauses, and two rules that look independent while actually qualifying each other read as a contradiction to anyone meeting both.

**Why the existing passes miss it.** [rationale-audit-second-pass] looks for rationale inside operative rules — a different defect. [law-prose-restyle] converts wording — sentence shape, not relationships between rules. Neither asks "does this rule have a parent it should sit under?", a question about the corpus's *structure* rather than any one rule's text.

**The signature to search for, which makes this scopeable.** Two or more rules governing the same subject, stated at the same level, with no declared relationship. Length is the known instance — at least three separate statements about how long something should be, in one always-loaded file, none referencing the others. Other candidate subjects: what gets written where, when to ask versus proceed, what counts as evidence.

**Weigh at processing whether this is its own pass or a lens added to [law-prose-restyle]**, since that pass already reads every rule and restructuring is closer to its work than to the rationale audit's. Folding it in is cheaper and may be right; filing it separately stops it being forgotten either way. Belongs in the cleanup inventory's group B either way.

#### SPEC does not say how many commits a close makes, now that the answer is exactly one [spec-silent-on-one-commit-per-close]
Filed 2026-08-14 by Claude during the build of [close-produces-multiple-commits-every-time], as adjacent work rather than folded in.

**What the build settled.** A session makes exactly one commit — the close — and the post-commit tail commits nothing, riding into the next close. The accepted cost is that the working tree is dirty between one close and the next, always, which is what makes that dirt legible rather than noise.

**Why this is a capture and not part of that build.** Nothing in SPEC becomes false: its close paragraph says the close records and commits, and says the append offer exists, without claiming a commit count or a clean tree. So there is no contradiction to halt on and no stale sentence to correct — only an addition. The build's file list named `done.md` and the session-start hook, and adding product truth is the route that asks first, which would have stopped an unattended run for a sentence nobody is blocked on.

**What a keep would decide.** Whether the commit count and the expected-dirty-tree are product truth a consumer should read in SPEC — they will see the "uncommitted changes from a previous session" line at every session opening, and SPEC is where they would look to find out whether that is normal — or whether it is implementation detail belonging only in the close procedure. Relates to [close-produces-multiple-commits-every-time], [post-close-tail-state], [done-delta-close] and [close-cost-scales-with-run-size].

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

#### A run can be presented whose top item is already void because /setup is outstanding [next-presents-items-setup-will-overtake]
Filed 2026-08-15 from INBOX mail sent by a consumer project running this method, which flagged it as the less clear-cut of their two findings and possibly working as designed.

**What happened.** Their project's recorded plugin version was behind the installed one, so session_start correctly said /setup wanted a session of its own. /next then presented a run as normal. Its top item was a fix to a stale description inside CLAUDE.md's plugin-managed block — exactly what /setup rewrites, from a template already carrying the correct text. The item was void before the run began, and the run had to be closed with nothing built to free /setup.

**Nothing malfunctioned, which is why it is a design question rather than a bug.** Each part did its job. But session_start already knows the project is behind, and /next's pre-flight has no branch that says so when presenting a run.

**Their proposed fix, worth weighing rather than adopting.** One line at the present-the-run beat saying setup is outstanding and may overtake items touching plugin-managed content. Against: this project keeps removing per-run narration, and a line firing on every run in a behind project is the cry-wolf shape it has repealed measures for twice. In favour: the condition is mechanically known, it is rare, and it cost a whole run and close here. **Note the ordering interaction with [scope-lock-blocks-setup]** — while that bug stands, /setup cannot run at all, so telling a user to run it first sends them into a denial.

#### Claude keeps writing two-column fenced blocks that wrap into nonsense on the user's display [two-column-fences-wrap-unreadably]
Filed 2026-08-15 by Claude at the close's re-scan, from an instance it caused in this session.

**What happened.** The rewritten ladder was presented as a fenced block with a label on the left and its explanation in a right-hand column. On the user's display the right column wrapped underneath the left, so the two ran together and half the rungs appeared to have no title. **Her words: "there's no title on half of them. what do they mean."** The content was fine; the layout destroyed it, and a second message in plain lines fixed it immediately.

**Why this is a capture rather than a one-off slip.** The corpus already contains [fences-wrap-so-prose-rule-reason-is-false], so the wrapping behaviour is known here — and the block was written anyway, in a session with that item in view. The shipped docs are also full of this format: `skill-nonspecific-rules.md`, `plan.md` and `done.md` all use two-column fenced blocks heavily, and Claude reads them at every session start, which is the likeliest reason it keeps reproducing the shape in chat.

**The distinction that matters, and what a fix has to get right.** A two-column block inside a procedure doc is read by Claude, in a wide view, and works. The same shape emitted *to the user* is read on whatever display they have. So the rule is about output, not about the docs — a fix that reformatted the procedure docs would solve the wrong half.

**To settle at processing.** Whether this is a rule about chat output ("structured content shown to the user goes one item per line, never in aligned columns"), or whether it is already covered by the existing item and should be folded in. Check that item's actual subject first — its title is about a prose rule's stated reason being false, which may be a different concern wearing the same word.

#### The rationale audit has covered one file per paragraph and twelve by signature phrase only [rationale-audit-fetched-docs-gap]
Filed 2026-08-16 by [rationale-audit-second-pass], recording its own scope so the gap is visible rather than assumed closed.

**What has happened to each file.** `skill-nonspecific-rules.md` has had both passes: the signature-phrase criterion in the first, and the per-paragraph delete-and-reread test in the second, which produced the eight findings filed alongside this one. The twelve fetched procedure docs under `docs-b/` have had the first pass only.

**The decision this was waiting on can now be taken.** Both earlier items — this audit and [law-prose-restyle] — carried the same condition: whether to extend to the fetched docs waits until one file shows what the technique yields. It has. One file produced eight findings by reading, several substantial, and the two heaviest fetched docs (`done.md` and `plan.md`) are each larger than the file just audited.

**What weighed against extending, from the earlier refusal.** Roughly 42,000 words of per-paragraph judgement, which is why the first pass reached for a mechanical criterion; and findings on files nobody intends to restyle produce work with no home, generating captures faster than the queue absorbs them.

**What has changed since.** The yield is measured rather than guessed, and [close-cost-scales-with-run-size] independently scoped a subtraction pass over `done.md` — so at least one fetched doc will be worked regardless, which removes the no-home objection for that file.

**A recommendation, not a decision: extend to `done.md` and `plan.md` only**, the two largest and the two already scheduled for work, and leave the remaining ten on the signature-phrase pass. Relates to [close-cost-scales-with-run-size] and [law-prose-restyle].

#### that consumer project answered the line-anchor question: nothing is built, and Claude Code drops the line number before any app sees it [line-anchor-answer-from-understudy]
Filed 2026-08-16 by Claude from an INBOX message sent by a consumer project running this method, triaged and archived at the close of the twenty-one-item run on the user's instruction. **They ask for nothing; this is filed so the answer is not lost, and because it has a small piece of real work in it.**

**The answer to what we asked on 2026-08-10.** Can their reader open a document at a given line? **Not today — nothing is built.** It is designed and queued on their side, held below their readiness line. Would it work beyond `.md`? Probably, since the design is not format-specific and their reader already opens any text file it can display — but that is a reasoned expectation rather than an observation, and the same unbuilt answer applies.

**The part worth our attention is not their code.** They researched this on 2026-08-06 and found that a `.md:N` reference **fails silently inside Claude Code before any app is launched** — they cite `anthropics/claude-code` issue #83475 — and that where line numbers do get through, they appear to reach a *configured editor* rather than the file type's default handler. Nothing they found confirms that a default-handler launch on Windows ever receives a line number at all.

**So two independent observations point the same way.** We observed the desktop app's viewer silently ignoring the anchor; they cannot confirm anything downstream ever receives one. Being the reader does not help if the number never arrives.

**What they ask us to do: nothing.** Keep rendering a plain file link with the line named in the prose, and change nothing on their account until they send an observation rather than a hope. **That is exactly what the shipped rule already says**, so no method change follows and none should be invented.

**The small real work.** This is external evidence about a tool we do not control, and it currently lives only in a message about to be archived. It belongs in `resources/research/` with an index line, so a later session weighing link rendering finds it instead of re-deriving it — the always-loaded rule requires a finding that informed a decision to be filed as part of using it, and this one is load-bearing for a rule we ship.

**What would settle it, on their side and not ours.** One click: a `path.md:42` reference in Claude Code once their reader is the registered handler. That step is written into their queue but sits behind building and installing an installer and registering the handler, and they decline to guess a date. If the answer turns out to be no, they say their own item is to delete it honestly rather than keep it as a permanent maybe, and they will tell us that outcome too.

#### No test asserts that an origin claim goes unflagged, which is the whole of the provenance split [origin-claim-has-no-test]
Filed 2026-08-16 by the build of [provenance-splits-origin-from-quote], as adjacent work rather than part of it.

**What the suite covers and what it misses.** `resources/testing/test_queue_lint_flags.py` has four cases on the credit check, and all four survived the split untouched because each happens to use a quote-claim phrase alongside its `Captured by you`. So the suite still passes and still asserts only the half that did not change.

**The half that did change has no case at all:** a bare `Captured by you` with nothing quoted must now produce no warning. That is the entire point of the split — it is what stops Claude asking the user to prove her own work is hers — and a later session could restore the old phrase list with every test still green.

**Files:** `resources/testing/test_queue_lint_flags.py` — one case asserting a bare origin claim is not flagged, and one asserting a quote claim still is.

#### Repealing a shipped clause has no ripple-trace rule, so an unattended run stops to ask [repeal-has-no-ripple-trace]
Filed 2026-08-16 by Claude, from a failure observed twice in one run rather than reasoned about.

**What happened.** [spec-control-model-not-what-happens] repealed one sentence from the always-loaded rules and its Files line named that one file, stating in its own prose that "the defect is in the always-loaded rules, not in SPEC." The repealed clause was in fact restated verbatim in three more live places — `SPEC.md`, the shipped FAQ template, and the FAQ copy. The run therefore stopped twice to grow scope, in a run whose whole premise is that it does not stop.

**The rule that should have caught it does not reach this.** `CLAUDE.md` requires a ripple traced by grep when a work item changes a **format or enum the hooks enforce**. A repealed sentence is neither. Yet the trace needed is identical and just as mechanical: grep the clause's distinctive words across the repository before writing the Files line.

**Not a judgment call, which is what makes it fixable.** Where an item says a sentence is repealed, the sentence is a literal string. Nobody has to weigh anything — the item either grepped for it or it did not.

**What to settle:** whether this widens the existing ripple-trace rule to cover any item that repeals or rewords shipped text, or whether it becomes a limb of the keep-step's two-limb check, which is where the Files line is written. Relates to [fix-level-has-no-site], shipped this session, which asks the same question about levels.

#### Splitting an over-length entry satisfies every band while multiplying the total, and nothing measures a close [split-action-defeats-the-bands-in-aggregate]
Raised by you 2026-08-17 at the close that first applied the split, from the cost as you actually paid it: *"That was almost 17k tokens. I am concerned that the bands won't reach this new record keeping model."*

**What happened.** The plan-entry split settled earlier the same day turned one over-ceiling entry into twenty-four entries, each comfortably inside the 160–323 band. Every band passed. The total is far larger than the single long entry would have been.

**Why the bands cannot see it.** Each band governs one artifact. The breach action for a plan entry is to split, so the remedy for an over-length artifact is *more artifacts* — and nothing anywhere measures a close, a session, or a day.

**The index pays it twice.** Twenty-four new lines, each within its band, added to a file read in full on every retrieve. That is the toll model written into the index rule the same day; the band caps a line's length and says nothing about how many lines a close adds.

**Same shape as [work-items-accrete-past-their-band], one level up.** That one was per-write against per-artifact. This is per-artifact against per-session.

**To settle at processing, and neither route is cheap.** A per-close figure needs a derivation nobody has, and inventing one is the bare-number failure this project bans. Or the split action itself is reconsidered — whether an over-ceiling planning entry should split at all, or should instead be written shorter, which is what a ceiling normally means. **Do not treat the split as settled merely because it shipped this morning.**

Relates to [bands-fire-on-the-median-artifact], [plan-entry-split-action-underspecified] and [index-line-length-is-a-toll-on-every-retrieve], all settled the same day.

#### SPEC states the reading position more strongly than the user expressed it, and no capture records where that came from [spec-overstates-the-reading-position]
Raised by you 2026-08-17, when Claude quoted SPEC's sentence back at you as though it were settled. **Your response: that the design is "never lowered" to someone who will not read is a widening of what you expressed at the time.**

**What SPEC says today.** That the method is built for someone willing to read and approve the record, that someone who will not read is considered but is not the target, and that **the design is never lowered to them** — a workflow built around its own expected non-compliance having nothing left in it.

**Why it matters rather than being a wording quibble.** That sentence is product truth in the opening section, so it shapes what every session builds. If it states a stronger position than you hold, work gets scoped against a stance you did not take — and it is attributed to you by placement, since SPEC is your product's truth.

**A related question left unanswered in the same exchange.** You asked whether a capture exists recording that the needs of users who do not read the queue were considered but that the plugin is not designed for them. `QUEUE.md` was searched and holds none; `LOG/` was not searched.

**To settle at processing:** what the position actually is in your words; whether SPEC's sentence is narrowed to match; and whether the LOG search is worth running to recover the original reasoning before rewriting it.

#### A send is recorded without its destination or its intent, so it cannot clear the work it hands over [send-record-lacks-destination-and-intent]
Raised by you 2026-08-17 while asking whether an article had been passed to another project. Checked rather than assumed: the LOG entry says only *"she approved the exact text before it was sent"* — no recipient, no purpose.

**Your rule, in your own framing.** A message sent may clear a work item where the send defers that item to another project **for completion**. Where it defers only **continuation**, the item stays and a later capture is what wakes it up. The two need telling apart, and nothing in the record does.

**What is missing is the record, not the rule.** A send cannot clear an item on evidence that names neither where it went nor what it was for. So the record has to carry destination and intent before the rule can have teeth.

**The live inconsistency this exposed.** [competition-comparison-article] sits cleared to run as work for you while the draft is in another project being polished. Its fate is unsettled pending this.

#### `INBOX/` holds no record of what was sent, which is where anyone would look for one [inbox-has-no-outgoing-record]
Raised by you 2026-08-17, in your framing: if the mailbox is where you would naturally look, maybe that is where it should be.

**What is true today.** Outbound mail is written straight into the recipient's `INBOX/` and nothing is kept here. `INBOX/archive/` holds inbound messages only — twenty-two of them — so the folder reads as a complete mailbox while recording half a correspondence.

**Why the LOG is not the answer on its own.** It records what a session did, so a send belongs there, but nobody looking for "what did we send that project" opens a session record. Locality is the argument: the sent copy beside the received ones is where the question is asked.

**To settle:** whether an outgoing folder is added, what it stores, and whether it duplicates or replaces the LOG's account. Relates to [send-record-lacks-destination-and-intent], which is the same gap read from the record's side.

#### Should cross-project work travel as mail at all, or as captures written straight into the other project's queue [cross-project-mail-versus-direct-captures]
Raised by you 2026-08-17: *"it feels like inbox shouldn't exist and it should all just be captures to the other project's queue"*, with items allowed to name blockers that live in another project.

**What it would replace.** The mailbox, its delivery step, its triage step, its archive, and the routing rules that carry a message into a capture — a message becomes the capture directly.

**What it would need.** A blocker that resolves outside this project, which today is impossible: `Blocked by:` names a slug in this queue, and every check assumes it.

**Why it is not obviously simpler.** It removes a whole mechanism and adds cross-project references that nothing can currently verify. Your own reading: simplifying and complicating at the same time.

**Weigh it against the mailbox work already settled** — bodies leaving the session briefing, and the close gaining a triage step — which reduce the mailbox's cost without removing it.

#### Whether QUEUE.md should be private by default, leaving LOG as the public artifact [queue-privacy-default]
Raised by you 2026-08-17, as a consequence of cross-project captures but true today regardless.

**The question.** Gitignoring QUEUE.md by default would keep a user's plans and reasoning out of any published repository, leaving LOG as the one public artifact. Against it: **someone may want a visible queue for transparency**, which is your own objection to your own proposal.

**It is independent of the mailbox question**, which is why it is filed separately. Whether work travels as mail or as direct captures changes nothing about what a repository exposes.

**The existing machinery probably answers it.** Scaffolding already offers once to gitignore SPEC, QUEUE and LOG together, with the trade stated. So this may be a change to that offer's default rather than a new mechanism — settle whether the default moves, not whether the option exists.

