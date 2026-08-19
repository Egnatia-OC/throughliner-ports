# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Ask Taskflow for an additive import and a completions export, so the bridge has something to talk to [taskflow-bridge-request]
Filed 2026-08-19 by Claude, from the design agreed with you in the same session. **It gates [taskflow-personal-bridge]**, which cannot state its build until these answers exist.

**Three asks, concrete rather than a conversation.** Confirm that Claude acting on the user's behalf does not breach their local-first principle — their SPEC says Taskflow "does not import from, sync to, or export to any external task app", and the reading here is that Throughliner is not a task app being synced but Claude, which their paid tier explicitly sanctions. **That reading is theirs to make, not ours.** Then: an **additive** import that adds named tasks and leaves the rest of the database alone, distinct from the existing whole-database restore. Then: completions readable from an export, so a parent's roll-up state can be seen from outside.

**The permission question was raised and settled by you in the same session, 2026-08-19.** The parent-folder instruction says Taskflow may be read freely and never written to, which as written forbids putting a file in their mailbox. **Your decision: INBOX is an exception to it, and the one sanctioned pathway — your reason, in your own words, that it is a communication method, "not part of the product itself."** The no-write rule protects Taskflow's own contents; a mailbox is correspondence rather than contents, so nothing it protects is touched. The rule text itself is amended by [parent-claude-md-taskflow-no-write-stale], which this does not wait on — a decision is in force from the moment it is made, not from the moment it ships.

**Files:** one message file written into Taskflow's `INBOX/`, carrying the three asks above. Nothing in this project changes.

**Nothing is sent without you seeing the exact text and saying yes**, as with every outbound message.

#### The parent-folder no-write rule about Taskflow is duplicated, stale in both copies, and now needs an exception [parent-claude-md-taskflow-no-write-stale]
Filed 2026-08-19 by Claude, from your decision that INBOX is an exception to it. Three faults in one paragraph, found by reading both copies rather than the version pasted into the session.

**The rule.** "Read Taskflowapp freely from here to answer questions or check state. Do not write to it — no edits, new files, deletions, renames, moves, or shell commands that change anything inside." It lives in `My Drive/CLAUDE.md` and in `Taskflow Planning/CLAUDE.md`, word for word the same, and both load into every session opened in this project.

**Fault one — it needs your exception written into it.** INBOX is the one sanctioned pathway, on your reasoning that a mailbox is a communication method rather than part of the product. Until the text says so, every future session reads a flat prohibition and stops exactly where this one did.

**Fault two — both copies name a path that is not this machine's.** One says `C:\Users\Alex\Desktop\Taskflow Planning\...` and the other `G:\My Drive\Desktop\Prioritiy projects\...`; the project is actually at `C:\Users\Alex 2\My Drive\Desktop\Prioritity projects\...`. Same class as [claude-config-points-at-dead-layout], one folder up.

**Fault three — two copies of one rule with no declared relationship**, so an edit to either can silently diverge from the other. Whether the fix is one canonical copy or a pointer is part of what a keep decides.

**Why it is a capture rather than an edit made here.** A planning session's scope-lock permits this project's own documents and nothing above them, so both files are outside what /plan may write. **This is the lock working as designed, and it is worth noting that neither file is in the rule gate's trigger set either** — the same siteless shape as [gate-trigger-misses-the-audit-checklist], one level further out.

**Measured at processing 2026-08-19, and the duplication is total rather than confined to that paragraph.** Both files are 17 lines and byte-identical apart from the path string, so one is a whole copy of the other at a different level. The Drive-root copy describes folders three levels beneath it — `No code method/` and `Planning in here/` — so it is misfiled as well as duplicated: orientation for the Taskflow Planning folder, sitting at the top of the whole Drive.

**Neither file is under version control, which changes how the build must proceed.** My Drive is not a git repository and `Taskflow Planning/` sits above this project's repo. So write-first's own test — is the previous version recoverable without the user? — returns no, and **every edit here is shown before it happens**, including the deletion. That is the untracked branch [gitignored-core-docs] is adding to the rules, reached here first by accident rather than by design.

**What changes, settled with you at processing.** `Taskflow Planning/CLAUDE.md` becomes the single owner: its path corrected to this machine's actual one, and the INBOX exception written in — a mailbox is correspondence rather than Taskflow's contents, so the no-write rule does not reach it. The Drive-root copy is **deleted**. Nothing is orphaned: it describes a folder three levels down, and `Desktop/CLAUDE.md` already orients anything opened above this project.

Rule gate: not needed — a rule is genuinely amended, and it is not in the method's own text. These are folder-level instructions for one machine, so nothing under `docs-b/`, this project's `CLAUDE.md`, `self-authoring-rules.md` or `rule-maintenance.md` is touched and the mechanical trigger never fires. **That silence is itself a second instance of [gate-trigger-misses-the-audit-checklist]**, noted on that item rather than treated as new here.

**Files:** `Taskflow Planning/CLAUDE.md` (path and exception) and `My Drive/CLAUDE.md` (deleted). Host-only, and arguably not even that: these are folder-level instructions for this machine rather than anything the method ships.

#### Let a capture carry `Not before:`, so work waiting on the world stops being re-offered every session [not-before-reaches-unprocessed]
Raised by Claude 2026-08-19 mid-planning, from three items in one session whose only fault was waiting on something outside this project, and worked immediately on your instruction rather than filed. **The decision that the prior refusal does not reach this is yours**, given after it was put to you.

**The gap.** `Not before: YYYY-MM-DD` is the one hold that resolves itself — nobody confirms it and the hooks read it off the calendar. It is available only to an item in Processed, and Processed requires passing the keep check. An entry with nothing to build cannot pass it, so the hold designed for "come back later, nobody needs to think about it" is out of reach for exactly the entries that want it, and they are offered again every session.

**Failure evidence from this session alone.** [standing-audit-programme] reached its third skip for the reason both earlier sessions gave. [approval-flow-token-doubling-simplification] has been re-offered since 2026-08-01 against a GitHub issue with no maintainer response. [taskflow-personal-bridge] was filed and deferred within the hour, waiting on another project's reply. None of the three can name a queue item as its blocker, because nothing here can do the thing each is waiting for.

**The prior refusal, cited rather than walked past.** plan.md's skip rule bars a durable marker for skips, and bars a file to hold them, as a phantom queue state. **What that refused is a record of "Claude skipped this", written by the session that skipped it.** This is a date approved at processing, saying when an entry is worth looking at again, on work waiting on the world rather than on anyone's attention. Put to the user, who ruled the refusal does not reach it.

**Three readers were read before this was described, and two need nothing.** `queue_digest.py` already prints `Not before: <date> -> passed/ahead` on every entry, ungated by section, so an Unprocessed date reports correctly today. `session_start.py` scopes its date scan to Processed and stays that way — its facts are about *held* work, and a capture is not held. `post_tool_use.py` skips Unprocessed entirely, so there is no false warning to fix — but its malformed-date check sits behind that same skip, and a date nothing can parse holds an entry forever.

**What changes.** `skill-nonspecific-rules.md`'s capture line-format block: the `Not before:` annotation stops saying below-the-line-only, and gains its second meaning — on a capture it means do not offer this again before this date. `plan.md`: the opening passes over an Unprocessed entry whose date is still ahead and takes it up once the date has passed, and the skip-recommend step is where a date is proposed and approved. `post_tool_use.py`: the date-format check extended to Unprocessed, with the above/below checks left scoped to Processed. `resources/testing/`: a case for each. Plus `faq-template.md` with `FAQ/faq.md` and both index lines — a new line appears in the user's own queue and entries stop being offered, which changes what they answer.

**No epoch bump:** the field is optional and nothing in an existing project becomes structurally wrong.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plugin/throughliner/docs-b/plan.md`, `plugin/throughliner/hooks/post_tool_use.py`, `resources/testing/`, `plugin/throughliner/templates/faq-template.md` with `FAQ/faq.md` and both index lines. **Checked and excluded:** `queue_digest.py` and `session_start.py`, for the reasons above. `SPEC.md` is not listed — its "Lifting shelved work" paragraph is rewritten in this planning session.

Rule gate: run — admitted as an amendment widening one existing field's scope, subordinate to the capture line-format block that already defines it, so no freestanding rule. **The eviction is the below-the-line-only restriction on `Not before:`**, repealed in the same move. Failure evidence is three instances in one session. **A new state was not proposed and must not be**: this is one field reaching one more section, which is why it survives the phantom-state refusal that has defeated three earlier proposals here.

#### The decay rung terminates in theory and is unreachable in practice, so nothing old is ever taken [decay-rung-unreachable-in-practice]
**Raised by you 2026-08-19**, in your own words: *"you can stay stuck on size forever, never reaching the decay rung by the end of any plan session."*

**You are right, and the arithmetic is the argument.** Rung 3 was partitioned at the section's median line count so that it terminates — a finite group that shrinks as it is worked. That fixed the formal defect, which was a rung that ranked every entry and so could never yield. It did not fix the practical one: the above-median group is by construction **half the section**, roughly 16 items in Unprocessed today, and reaching rung 4 means processing all of them in one session. This session processed four. So the decay rung is reachable in principle and, at any realistic session length, never.

**Your proposed fix does not work, and the reason is worth recording.** Combining the two rungs as "date by size" or "size by date" is a lexicographic order — one key dominates and the other only breaks ties. Whichever goes first, the second starves exactly as rung 4 starves now. The ordering is relabelled rather than repaired.

**Two fixes do work, and only one avoids inventing a figure.** A single composite score mixing age and size needs weights, and a weight is a bare number with no derivation, which this project bans; the same objection kills any ageing rate. **Interleaving needs neither: alternate between the above-median group and the oldest-filed item, one from each in turn.** Starvation becomes impossible by construction rather than merely unlikely, every pick still reads a field the digest already computes, and no figure is written into the method's text.

**What interleaving costs, stated because it is real.** Longest-first rests on cost-of-reading — taking long entries first shortens the queue fastest — and alternating halves that rate. The trade is half the benefit of a rung that works against the full benefit of a rung that is never reached, which is what rung 4 currently is.

**Checked against a second real queue and kept 2026-08-19, with your amendment.** The trial session adopted the interleave for its own remaining picks and reached a 17-day-old entry on the first decay pick, which the ladder had never once selected. The planning session that kept it reproduced the defect from the other direction: it worked unblock-potential to exhaustion, fell to longest-first, and never came close to the decay rung — the above-median group stood at roughly fifteen entries and a handful were processed. **The oldest entry was reached in that session too, and not by the ladder** — it surfaced because a pattern was noticed across three deferrals, which is the siteless-noticing failure recorded five times here: it worked, and it is not repeatable.

**Your amendment, and it is a better design rather than a preference.** Order the above-median set by **oldest first** rather than by length, and interleave that with oldest-first across the whole section. **The argument is that line count is not stable:** entries gained 193, 344 and 472 words *while being processed* in the keeping session, so longest-first ranks by a key that mutates as the session works, and the entry ranked last can overtake the one ranked first with nobody touching the ladder. First seen cannot change. Length therefore stops deciding order anywhere and survives only as membership in the long half, which is where its cost-of-reading justification actually sits. In plain terms: oldest first, with every other pick required to be one of the long ones.

**A rung sits above the alternation, added on your second amendment the same session — and this paragraph replaces the ladder described above rather than sitting beside it.** Work first the entries that are **both** above the section's median line count and above its median age, oldest first; when that set is empty, the alternation begins. **The set is an intersection of two medians**, each a proportion of the section the digest already computes and each fixed at the opening, so it is derivable rather than judged.

**It is bounded by construction, which is what stops it recreating the defect this item exists to fix.** The old rung was half the section — roughly fifteen entries, never drained in any session. An intersection of two halves is roughly a quarter: seven as the queue stands, reachable within a session. That is the whole reason it may sit above the alternation without starving it.

**Its stated justification is the opposite of the original hope, and is the stronger of the two.** Your recovered intent for longest-first was reaching the best-designed entries first, which the record already says did not bear out; your question was whether length **and** age together might do what length alone did not. **The evidence in the queue runs the other way and you accepted the point:** [standing-audit-programme] is the longest entry and one of the older ones, and it is the single entry that provably cannot be kept — third skip today — because at the top of the distribution length tracks repeated enrichment without resolution. **One counter-example is not a refutation and none is claimed**, but it reframes the rung honestly: it reaches the entries that keep coming back and bleeding sessions, not the well-designed ones. A later session testing the hypothesis has both halves here rather than having to rediscover either.

**One immediate consequence, answered by work kept the same session.** [standing-audit-programme] sits squarely in that intersection and would be handed to the user first every session while remaining un-keepable. That is tolerable only because [not-before-reaches-unprocessed] lets a capture carry a date that stops it being re-offered. **The two interlock and neither is sound alone:** this rung surfaces the contested entries, and the date field is what lets one genuinely bow out.

**The dilution is accepted as a price rather than argued away — your decision, in your framing:** it is what elevating the hard-to-reach decay rung costs.

**The set is fixed at the opening, and recomputing it would be wrong rather than merely expensive.** Your question was whether membership could instead be recomputed mechanically as entries grow. It could — the digest computes line counts and the median, and re-running costs one command. It must not be: an entry could swell past the median and re-enter a group already worked past, so the group stops shrinking and the termination defect returns. That is the same reason `plan.md` already fixes the median at the opening.

**Both arms are still needed**, checked rather than assumed: with the long arm ordered by age it would be tempting to think the whole-section arm is redundant, but it is the only one that ever reaches a **short** old entry.

**What it costs, stated rather than discovered.** Longest-first existed to shrink the queue fastest. Taking the oldest long entries rather than the longest ones dilutes that a second time — the long half is still worked, but not worst-first. Against a rung never once reached, the trade holds.

**Files:** `plugin/throughliner/docs-b/plan.md` (the fallback ladder, and the median-fixed-at-opening sentence) and `SPEC.md`, whose processing-flow paragraph enumerates four rungs and goes wrong — **rewritten in this planning session** rather than listed. **No FAQ entry:** ordering is applied and narrated, and the user sees one line either way, so nothing they do changes.

Rule gate: run — admitted as an amendment merging the ladder's bottom two rungs into one alternating rung, subordinate to the ladder that already exists. **The eviction is those two rungs as separate statements**, and it is flagged explicitly because a falling rule count must be attributed to a merge rather than read as a deletion. **No figure is introduced anywhere** — alternation needs no weight, which is what defeated the composite-score and ageing-rate alternatives. Failure evidence is two sessions in which the decay rung was unreachable, plus one trial pick that recovered a 17-day-old entry.

Relates to the ladder's history: the decay rung was deleted once and restored, its deletion recorded as a forced choice rather than a finding against it, so this is the second time it has come close to being lost.

#### Give the build a derived view of the cleared region, carrying instructions and no decision history [split-the-cleared-region-for-concurrent-sessions]
**Raised by you 2026-08-18 as a read-cost saving, and redesigned at processing on 2026-08-19 once the rationale hypothesis was tested and confirmed. The slug is unchanged because slugs are immutable. The design is yours;** the projection-rather-than-a-move shape came out of the discussion.

**Why the subject moved.** The build view was filed to stop a run reading 24,800 words to build a handful of items. That saving stands, but it is now the second reason. The first is that a build cannot transcribe rationale it was never given — and it does transcribe it today, confirmed against git in `resources/research/rationale-flows-from-items-into-shipped-docs.md` rather than argued here.

**What changes.** The keep-step authors a delimited **build block** on each item, carrying what changes in which files, the acceptance test, the red-flag state, and **any recorded refusal** — refusals stay, because stripping "X was refused because Y" makes the build re-propose X and stop to ask. A script copies those blocks byte-for-byte, keyed by slug, into a generated view. **That view also lists every entry in both sections by heading and slug alone, with no rationale**, so a build can still tell whether something is already filed. /next reads that view instead of QUEUE.md. The build's close resolves each slug against QUEUE.md as **one targeted read of one entry**, so the record still carries the history forward.

**The view is read-only and regenerated, which is what removes the merge.** Nothing rejoins because nothing left — the only write-back is deleting the slugs that shipped, which `reorder_queue.py --delete` already does. **Your queue-merge skill is refused on that ground**, not on its merits: a sixth skill is the heaviest answer available, since every skill is loaded, documented and explained to consumers.

**Why the separation is authored and not computed.** Telling history from instruction is judgment, so no script can do it. The keep-step can, with you present — the same siting the rule gate uses, and for the same reason.

**The throughline rule is untouched.** The full queue keeps its rationale inline and whole. What the build reads is a projection, never a deletion.

**Designed for concurrency from the start**, on your point that a semi-autonomous run currently occupies the only session you have and so blocks capture outright: planning writes the full queue and a build never does. The session mechanics are held separately in [concurrent-plan-and-build-sessions].

**The capture-quality objection is settled here, 2026-08-19, and [build-view-narrows-capture-context] is deleted into this paragraph.** A consumer project sent evidence deliberately ahead of this change: during a `[user]` walk-through, an aside produced two good captures, and their claim was that none of what made them good came from the build. Checked rather than accepted, two of their four limbs land — knowing the captures were not already filed, and knowing what queued work depends on the detail. Both are queue-wide knowledge. Reading SPEC and knowing how items get processed are unaffected, since /next reads SPEC at run start and the procedure docs load either way.

**So the view carries the whole queue's headings and slugs, and none of the history** — which restores duplicate-detection at almost no cost. **What it does not restore is the second limb, recorded rather than papered over:** a heading says an item exists and says nothing about what it depends on, so the cross-item awareness behind the second capture stays lost. **Routing walk-throughs to a planning session is refused rather than deferred:** concurrency is held below the line behind this very item, so that mitigation would wait on the thing it mitigates.

**The timing point survives the narrowing and is why the cheap fix is worth taking.** The aside happened during a walk-through, which is the phase where the user is talking freely and unprompted material arrives most — a context cut applied evenly across a run bites hardest exactly where the raw material is richest.

**Bumps the format epoch** — every existing project gains a generated file and its items gain a block — so `migrate-checklist.md` is refreshed in the same build.

**Files, traced by grepping `QUEUE.md` across the package rather than written from the discussion:** `plan.md` (the keep-step authors the block), a new `plugin/throughliner/scripts/` generator, `next.md` and `next-build.md` (read the view), `done-build.md` (the targeted read at close), `pre_tool_use.py` (the scope-lock refuses QUEUE.md to a build), `post_tool_use.py` (the lint checks a cleared item carries a block), `session_start.py` (the epoch), `migrate-checklist.md`, `resources/testing/`, plus `faq-template.md` with `FAQ/faq.md` and both index lines. `SPEC.md` is written in this planning session.

**Long, and not split — stated rather than passed over.** The evidence is already relocated to the research file above, which is the move that shortens an item holding one coherent design; dividing what remains would put the same Files line on both halves. **No ceiling is invoked**, since [retire-word-band-caps-keep-measurement] retires them.

Rule gate: run — no freestanding rule. The build block is a clause on the existing two-limb keep check, which already governs what a kept item must state. **The eviction is the always-loaded assumption that a build reads QUEUE.md**, repealed across the readers named above. Failure evidence is two transcription cases confirmed against git, plus the measured proportion in one hunk: eight lines of rule against seventeen of explanation.

Relates to [folding-in-has-no-eviction-step] (the same accretion one level down), [rationale-lens-after-the-build-view] (held until this ships) and [unattended-run-is-not-unattended]. The item that carried the hypothesis was deleted once its test was run and its evidence filed as research — it was a finding, not work.

#### Retire the word-band caps and keep the measurement as a report [retire-word-band-caps-keep-measurement]
**Your decision 2026-08-19**, in your own words: the numbered caps are *"too arbitrary and we have realer leads now."*

**The argument that settles it comes from the tool itself.** `measure_written_shape_length.py`'s docstring refuses to print a band beside a distribution, because *"a band printed inside the distribution report would be a threshold read off the thing being questioned."* The shipped bands are exactly that — the middle of what this corpus already wrote. The script declines to do the thing the rules did.

**This project has already accepted that argument once, one layer up.** The rule-corpus ceiling was removed on the ground that it had lost its derivation and no defensible replacement threshold existed; `rule_signals.py` still carries the reasoning and now reports growth with no verdict. The word bands are the surviving instance of a pattern already retired.

**Three facts behind it rather than a mood.** The rules' own caveat calls the figures lengths *demonstrated to be sufficient, never ideal*, which describes past behaviour rather than setting a standard. The 2026-08-18 re-derivation had to exclude three shapes of five for want of defensible data, including work items. And acting on a breach has a measured yield of 8%, 3% and 9% across three passes.

**What must not happen, because it is a known failure.** A prose instruction to be concise shipped first and measurably did nothing, which is the recorded reason the bands are figures at all. Retiring figures back to prose walks into that. The replacement is neither: it is structure — the build block and relocation along the seam it creates, in [split-the-cleared-region-for-concurrent-sessions]. That is the first lever aimed at where text lives rather than how it is worded, and it is untried.

**What changes.** Bands, ceilings, floors and breach actions come out of the always-loaded authoring standard, out of the keep-step read and out of the close. The measurement script stays and still ships, printing distributions and no thresholds — the shape this project already trusts everywhere else, stated in the queue-growth hook's own output as *bare facts, no threshold, no judgment, and none is implied*.

**What stays is the position, not the arithmetic.** SPEC keeps the stance that both failures are real: a record too thin to rebuild intent from fails as surely as one too long to get through. That is a stance you hold; only the numbers claiming to locate it go.

**Files, traced by grepping `band` and `ceiling` across the package:** `skill-nonspecific-rules.md` (the authoring standard's table and the paragraphs deriving it), `plan.md` (the keep-step read), `done.md` (the entry and index-line reads, and the index-line band reference further down), `resources/measure_written_shape_length.py` and its shipped copy (the band mode goes, the distribution report stays), plus `faq-template.md` with `FAQ/faq.md` and both index lines for "how long should my queue items be?". **Checked and out of scope:** `next-build.md`'s ceilings are the retired runner's iteration and spend limits, `session_start.py`'s is the hook output cap, and `rule_signals.py`'s is the already-removed rule-corpus ceiling. `SPEC.md` is rewritten in this planning session.

Rule gate: run — **the disposition is an eviction and nothing is authored.** Five figures and their breach actions are repealed across four live files, along with the derivation paragraphs defending them; no rule replaces them, and the replacement is a structural item already in the queue. Failure evidence is the tool's own refusal to self-derive, three shapes left unmeasurable at the last re-derivation, and three passes yielding 8%, 3% and 9%.

Relates to [word-band-script-does-not-ship], [split-action-defeats-the-bands-in-aggregate] and [tersify-on-request-not-at-the-close], each of which rested on a band and was amended alongside this. A fourth, which existed only to derive figures for the three unmeasured shapes, was deleted in the same session — there were no figures left to derive.

#### Name the two operations that fold into a work item, and require the merge to rewrite [folding-in-has-no-eviction-step]
**Raised by you 2026-08-18** from the ideation loop's effect on new captures: holding the write until the design settled stopped a capture being written to three or four times. **Your question was whether the same principle reaches the accretion that happens afterwards, and folding was your example. Designed at processing on 2026-08-19.**

**Your first point is confirmed by grep and is the whole reason there are no controls.** Folding a capture into an existing item is described in no procedure doc. `done.md`'s "fold it in" is a different operation — uncommitted work folding into the close — so nothing anywhere governs the one you named.

**What the design adds is that two operations wear that one name.** A **merge** takes two accounts of the same thing; a **supersession** records that a decision changed. They want opposite treatments, and conflating them is the measured failure: [send-record-lacks-destination-and-intent] carries its original framing paragraph *and* a later paragraph covering the same ground, because a merge was performed as an append.

**So the rule is to say which one you are doing, and each has its own move.** A merge **rewrites the host item** and states what came out, which is the rule gate's eviction step applied one level down — adding names what it replaces. A supersession **appends, dated, naming what it overturns and why the old reasoning lost**, because the throughline requires a defeated alternative and its reason to survive; rewriting one away is how a settled decision gets relitigated.

**Live evidence from the session that designed this, recorded because it cuts both ways.** Nine items were edited in one planning session: eight grew, by 1,285 words between them, and one shrank. Most of the growth was dated supersession — decisions that changed hours apart — which this rule says is correct. The accretion is not appending. It is appending where the two accounts describe one thing.

**The open measurement this item filed has its first answer, from the one item that shrank.** [law-prose-restyle-heavy-docs] had been given a lens and then had it taken away by an appended paragraph, leaving the item describing the lens as both in scope and removed — the failure this rule names, committed in the same session that wrote the rule. Merging it properly collapsed four paragraphs into one and took **63 words off**, against an item that would otherwise have kept growing. **One data point, in the predicted direction, and no rate is claimed from it** — but it is the only measurement anyone has that a rewrite comes out shorter than an append, and it was produced by a contradiction the digest could not see and a person asked for.

**The taxonomy objection, answered rather than left for a later session to raise.** The throughline rules ban forcing rationale into a typed taxonomy. This types the *edit being made*, not the reason being carried, and the test is binary with an observable answer: are these two accounts of one thing, or is one overturning the other?

**No FAQ entry:** Claude performs the fold, so nothing the user does changes.

**Files:** `plugin/throughliner/docs-b/plan.md` — the keep-step, where an item's rationale is authored and where folds happen. **Checked and excluded:** `done.md`, whose folds are a different operation, and the always-loaded rules, which fail the four-skills test here since /setup and /next never fold into an item.

Rule gate: run — admitted as a clause on the keep-step's existing authoring of an item's rationale, subordinate rather than freestanding, and sited in a fetched doc so no always-loaded slot is spent. **Nothing is evicted, and that is stated plainly rather than dressed up: folding was undescribed, so there was nothing there to replace.** Failure evidence is one measured duplication plus four folds in one session that each grew their host. **A hook was considered and refused** — merge versus supersession is a judgment about whether two paragraphs describe the same thing, which nothing mechanical can read.

Relates to [split-the-cleared-region-for-concurrent-sessions], whose build block gives a fold a defined target once it ships, and to [split-action-defeats-the-bands-in-aggregate], which measures the same accretion at whole-queue scale.

#### Correct the claim that a run is unattended, and keep the true half it is doing all the work with [unattended-run-is-not-unattended]
**Captured by you 2026-08-11**, in substance: an unattended run is not actually unattended — it stops for `[user]` items and does not run /done on itself. **Designed at processing 2026-08-19, and the design is narrower than the item expected.**

**The grep is what narrowed it.** "Unattended" appears at 23 sites, and almost all of them are *justifications* — do not stop the run to ask, do not narrate a passing check, do not block on adjacent work. Every one of those leans on something true: the run does not confirm each item and moves faster than a person can follow, so a stop costs disproportionately. **The item feared that settled decisions rest on an overstatement. They rest on the true half**, so end-preferred placement and the readiness line as the run's bound are both sound and are not reopened.

**What is false is the description, and there are four ways it fails rather than the two captured.** The run stops to walk a `[user]` item live; it halts outright on `[freeform]`; it never closes itself, because /done is yours to run, so a run left alone finishes and sits uncommitted; and — **your point 2026-08-19** — it occupies the only session there is, so for as long as it runs you cannot capture anything at all.

**What changes.** SPEC's claim that the run is "unattended in practice — the autonomous build mode the Principles name", and the Principle that execution stops "only for what genuinely needs the user", are corrected to say what happens: a run clears vetted work without confirming each item, and pauses at the three points above. `next.md` states that definition once, so the twenty justificatory uses read against something that no longer over-claims. **Rewriting all 23 is refused** — the phrase is correct wherever it means "do not interrupt this", and mass rewording would spend a large pass to change nothing.

**The fourth failure is fixed by other work rather than by wording.** [concurrent-plan-and-build-sessions] gives you a planning session alongside the run, which is what makes ideation-at-any-point true instead of aspirational.

**Self-closing is refused outright and recorded so it is not re-proposed.** A run that ran /done on itself would commit with nobody present, and a commit message is one of only two things the method still shows before it happens, precisely because a commit is hard to unwind and never becomes file content. Auto-closing overrides that guard or invents a version of it that survives nobody being there. Neither is worth the saving of one command.

**No new session type and no second meaning for the readiness line**, the item's other two options. Both invent a container, which this method has refused repeatedly, and the walk-through problem they were solving is answered by concurrency instead.

**Files:** `SPEC.md` (the multi-item /next paragraph and the execution Principle) — **rewritten in this planning session**; `plugin/throughliner/docs-b/next.md` (the definition, stated once), `done-plan.md` (the end-preferred rationale, re-grounded on the true half), and `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. **The FAQ entry is required rather than optional:** a user who reads "unattended" and walks away comes back to a finished run sitting uncommitted, which changes what they do.

Rule gate: run — no rule is authored. **The disposition is a correction plus two refusals**: self-closing and a new walk-through session type, both rejected on the record above with their reasons, so a later session meets the argument rather than the conclusion. Nothing is evicted; the justificatory uses stand. Failure evidence is four ways the description is false, three of them observable in any run.

Relates to [concurrent-plan-and-build-sessions] (which fixes the fourth), [arbitrary-run-length-capping] and [processed-reorder-mostly-unnecessary].

#### Detect which core docs are untracked and state the consequences, rather than treating it as a fault [gitignored-core-docs]
Filed 2026-08-18 from INBOX mail sent by a consumer project. **Reframed at processing on 2026-08-19, against the sender's own reading, after checking the source.**

**What happened there.** A planning session ran to completion — a red flag cleared, three SPEC edits, eight work items, nine captures — and staging at the close revealed `.gitignore` carried `SPEC.md`, `QUEUE.md` and `LOG/`. The adoption commit's message says it wrote SPEC.md as product truth; that commit contains no SPEC.md.

**The reframe, and it changes the whole design: this is not a fault, it is an offer.** `setup.md` already offers to add exactly those three paths to `.gitignore`, and [queue-privacy-default] widens that offer per document. So a check asserting the state is wrong would fire on a configuration the method itself creates on request — and would fire hardest right after the user chose it. **What was actually missing is that nobody was ever told what follows.**

**Three rules go quietly false, and one of them already knows how to handle it.** Write-first's own test is *"is the previous version recoverable without the user's help?"* — and for an untracked file the answer is no. The rule has always had the right test and never had the fact. So **where a doc is untracked, its writes become show-first**, by the existing test rather than by a new rule. The other two are stated rather than repaired: a deleted queue item is not kept by git history, and `done-plan.md`'s `git diff HEAD -- QUEUE.md` returns nothing, so the close's mechanical record of its own work falls back to memory.

**Detection goes in `session_start`, not in setup.** Setup fires once; the reporting project was already adopted, so a setup-only check would have missed the very case that produced this. `session_start` already runs git in seven places, and `git check-ignore` answers this in one call with no judgment.

**And that timing dissolves the deadlock the sender hit.** Their close could not fix it — the planning scope-lock refuses `.gitignore`, correctly, and the close marker's permitted list omits it — so it became a `[user]` line asking a non-coder to hand-edit `.gitignore` mid-close. **No permission change is needed.** Detected at the session's opening, before any work, the same walkthrough costs nothing and interrupts nothing. **Their third suggestion, adding `.gitignore` to the close marker's list, is therefore refused** — it widens a deliberate refusal to solve a problem that timing solves.

**Files:** `plugin/throughliner/hooks/session_start.py` (the check and the plain-words consequences), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (write-first's untracked branch), `plugin/throughliner/docs-b/setup.md` (the offer states the consequences at the moment of choosing), `resources/testing/` (a case per ignored path), and `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is rewritten in this planning session. **No epoch bump** — no file changes shape.

**[queue-privacy-default] lifts when this ships** and is held against it for that reason; both edit the same privacy offer, so the consequences and the per-document choice land in the right order rather than the second contradicting the first.

Rule gate: run — **no new rule.** Write-first gains a branch from a fact it can now read, which is its existing test applied rather than amended; the rest is a hook check and honest wording. Nothing evicted. **One refusal on the record:** widening the close marker's permitted list, rejected because the deadlock is caused by late detection rather than by the refusal. Failure evidence is one consumer instance in which three always-loaded rules were false for a whole session and the red flag's informed-consent trail went into an untracked file.

#### Compress the log index's longest lines, cutting the retrieve's fixed toll by about 40% [split-action-defeats-the-bands-in-aggregate]
**Subject replaced at processing 2026-08-17; the slug is unchanged because slugs are immutable.** Raised by you at the close that first applied the plan-entry split: *"That was almost 17k tokens. I am concerned that the bands won't reach this new record keeping model."*

**The aggregate half was measured and refuted, and that finding is in this session's record rather than here.** Per-entry cost *fell* after the split — 518 words per entry before it, then 329 and 316, against July's own 341. The 17k came from recording 26 items, so a per-close band would measure run size, which is your decision and not a length defect.

**What survives is the index toll, larger than the item claimed.** `LOG/index.md` is 817 lines and 48,165 words, read in full on every retrieve. 351 lines sit at or above 61 words and carry 32,408 of those words. 265 of the 351 are August's. **That 61 is a measured cut-off marking this item's work list, not a limit anyone must write to** — it selects which lines to look at, and each one is then judged against the index line's own contract rather than against a number.

**What changes.** Each of the 351 is rewritten to the artifact touched, the nature of the change and the entry filename, working from the line's own text only: a long line is long because it restates the entry it points at, so no entry needs re-reading. Commit hashes are preserved — the digest and the hash backfill read them.

**The band is no longer the reason, revised 2026-08-19 by [retire-word-band-caps-keep-measurement], and this item survives that intact.** The 20–40 figure goes with every other cap. What justified this work was never the figure: it is that `LOG/index.md` is read **in full, by Claude, on every retrieve**, so its length is a fixed toll rather than something a reader skims past — 48,165 words to point at entries, with one 337-word line pointing at a 1,710-word entry. The test is the index line's own stated contract, that it carries enough to decide open-or-skip and does not restate the entry. That is a judgment, applied line by line, and it was always the real test; the number was standing in front of it.

**This edits a pointer, not the record.** Every entry file stays byte-for-byte and no claim changes, which is what separates it from editing a session record to agree with a later decision.

**The intuitive fix was refused: monthly index files.** Four mechanical readers would each have to glob a directory, and the digest must resolve a slug from any month, so it would read all of them regardless — a format change, an epoch bump and a migration path for a smaller saving.

**Acceptance test:** line count, total words and median line before and after; expect roughly 28,000 words.

**Files:** `LOG/index.md` only. The ripple was traced by grep — `session_start.py`, `queue_digest.py`, `rule_signals.py` and `measure_written_shape_length.py` all read the file, none reads line length.

Rule gate: not needed — no rule authored and no always-loaded text touched. This rewrites a backlog of index lines against the index line's own stated contract: carry enough to decide open-or-skip, and do not restate the entry. **Reworded 2026-08-19** — it previously invoked the index-line band, which [retire-word-band-caps-keep-measurement] retires.

**The measurement this item asked for was run 2026-08-18, and it moves the subject: the problem is the queue's TOTAL length, of which item length is one term.** Across one full planning session the file went **21,512 words to 24,771 — up 15% — with the item count unchanged at 58**, and words per item rising 370 to 427. Twelve items were processed, four deleted and three folded away, and it still grew, because **processing an item is what lengthens it**: every keep adds a settlement, a Files line and a gate disposition. Only building an item out or deleting it shrinks the file. **This is the user's framing and it supersedes the per-artifact one this item was filed under.**

**So a wording pass is not the lever, which is measured rather than argued.** Two tersify passes over this queue yielded 8% and 3%, and their own write-up concludes the file is not verbose — its length is accumulated decision history. A tightening pass over seventeen freshly authored entries the same day cut 9%, 8,343 words to 7,585, leaving fifteen still over ceiling. Both passes removed meta-commentary and barely moved the totals.

**And the ceiling those passes were measured against is derived from a shape that no longer exists.** 45 of 54 entries breach it, the worst at 1,347, 1,102 and 805 words — corpus-wide rather than one session's authoring, so **an earlier claim on this item that the over-length was newly written text is withdrawn as false.** The band is July's median; dispositions moved onto the item on 2026-08-13, and the ripple-trace and SPEC-question limbs on 2026-08-17. A July item carried none of them. Re-derived figures without multipliers are in [word-band-script-does-not-ship]'s discussion.

**One narrower finding survives, though what it now feeds has changed.** Splitting an entry in two worked where it genuinely held two pieces of work and failed where it held one clause plus a long narrative — there the remedy was relocating the narrative to the record and citing it, 558 words to 407 and 571 to 442. **This no longer amends a breach action, because there is no breach to act on**: relocation-not-division is instead the measured precedent behind the build block's seam in [split-the-cleared-region-for-concurrent-sessions], which is where it does its work now. Both figures are also the only evidence anyone has that relocation moves the totals at all, and neither reached what was then the ceiling.

**The accretion mechanism is now filed separately** as [folding-in-has-no-eviction-step] — folding content into an item requires naming nothing that comes out, and appends rather than merges.

Relates to [bands-fire-on-the-median-artifact], [plan-entry-split-action-underspecified] and [index-line-length-is-a-toll-on-every-retrieve].

#### Planning writes the SPEC sentence ahead of the build, and a build that finds one missing files it rather than writing it [missed-spec-write-interrupts-the-run]
Raised by you 2026-08-17 when a run stopped in its second minute to ask for one SPEC sentence. **Subject settled at processing the same day; the slug is unchanged because slugs are immutable.**

**Your principle, which is the whole of this and which Claude missed twice before you stated it.** SPEC is managed across a session boundary so that no one instance of Claude is both the party that made a choice and the party that certifies it in product truth. Claude proposed deferring the write to that same run's close; you refused it on exactly that ground — the close is the same session, so it moves the self-certification later rather than crossing anything.

**Already settled one layer over:** `CLAUDE.md` says a disposition written as an item is built "improves attribution and restores no power to refuse," and that only /plan can refuse. That failure has a recorded instance here: a build in the eighteen-item run wrote its own gate disposition rather than halting, now carried as the fifth instance in [standing-audit-programme] after its own item was deleted as already decided.

**What changes, in three steps.** The keep-step asks whether an item changes what SPEC says, and **planning writes the sentence then**, with the user present. The build then builds against it and never touches SPEC. Only where planning missed one does the build record the sentence, file it as work, and leave SPEC alone for the next planning session.

**So SPEC leads the build rather than trailing it**, which is what "read at build time" requires. The cost, stated: on a miss, SPEC lags that sentence by one planning session. It is a queue item rather than silence, and the keep-step question is what makes the miss rare.

**Folded in from [batch-spec-writes-at-the-end-of-a-run], deleted at processing:** deferring SPEC writes inside a run was tried live on your instruction — four sentences held in the working file, written in one pass, nothing lost and the run never stopped again. That is the evidence the file-it fallback is safe. The rest of that item dissolved, because under this model a run owes no SPEC sentences.

**Files:** `plugin/throughliner/docs-b/plan.md` (the keep-step question, and the two-other-routes paragraph loses the build-asks route), `next-build.md` (the scope-grow SPEC ask and step 4's establishes-new-product-truth branch, both replaced by the file-it path), `done-build.md`, `CLAUDE.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`, `faq-template.md` plus `FAQ/faq.md` and both index lines for the entry. `SPEC.md` is **not** listed — its sentence was rewritten in this planning session, which is the rule applied to itself. The eight sites were traced by grep before this list was written.

**The SPEC-contradiction halt is untouched and must not be softened** — built work conflicting with SPEC still stops the run and names the sentence.

Rule gate: run — admitted as a clause on plan.md's existing two-limb keep check, not a freestanding rule, so no always-loaded slot is spent. **The eviction is the build-asks route, repealed outright across seven live files.** Failure evidence is one recorded instance, which is thin for a new rule and is what the amendment-plus-eviction shape carries; the same defect is independently recorded for dispositions as the fifth instance in [standing-audit-programme], carried there when its own item was deleted 2026-08-19.

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

**Superseded in part by [retire-word-band-caps-keep-measurement], your decision on 2026-08-19, the day after this was settled: the caps go and the measurement stays.** What survives here is the shipping defect this item was filed for — the always-loaded rules point every consumer at a script their project does not have, and that is fixed by moving the script into the plugin package. **What falls is the second half:** the re-derived figures are not shipped as bands, because the argument that retired every cap retires these two as well. The re-derivation's finding is not wasted — it is what showed the old ceiling to be tighter than the era it came from, which is part of why the caps went at all — but it lands as a record rather than as a rule.

**Files:** `resources/measure_written_shape_length.py` moved to `plugin/throughliner/scripts/`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the pointer only — the band table and the transfer clause are removed by the retirement item rather than rewritten here), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. `SPEC.md` is rewritten in this planning session.

Rule gate: run — no new rule; two figures replaced and one clause added to the existing authoring standard, with the invented multipliers evicted. **The eviction is the 0.5 and 1.5 multipliers**, replaced by measurements. Failure evidence is a consumer report plus 88% and 73% breach rates measured here.

**They also report the growth-by-addition trap working as designed** — the rules already carried the proposal to exempt later additions and the reasoning against it, which resolved that conversation in one exchange.

#### Tersification runs on request, never at the close, with the procedure on the shelf [tersify-on-request-not-at-the-close]
**Raised by you 2026-08-18** as a step at the close, and **filed against that placement on the evidence you then supplied.** The write-up of the two passes is at `resources/research/tersifying-the-queue.md`, reproduced verbatim.

**Why not at the close.** Its measured yield was 8% then 3%, and its own conclusion is that the queue is not verbose — the length is accumulated decision history. Against that, a close already carrying the session's heaviest work would take on a whole-file read and rewrite. **And its two failure modes are the kind that must not run unattended:** a silent duplication of fifteen items that reading could not see, and a probable upgrade of a paraphrase into a quotation claim — one instance of which was found live in this queue and repaired the same day.

**What changes.** `CLAUDE.md` gains a short entry saying a tersify pass exists, runs when you ask for it, and points at the write-up. **The pass-2 method is mandatory when it runs** — item-level splice keyed by slug, unchanged blocks carried byte-identical, slug-uniqueness assertion, per-block deltas so nothing grows silently — and pass 1's rewrite-from-memory is named as the method not to repeat. **Fenced blocks are untouchable**, on the write-up's §8d and [two-column-fences-wrap-unreadably].

**The close reports nothing about length, revised 2026-08-19 by [retire-word-band-caps-keep-measurement].** This item had given the close a breach report in place of the pass; with the ceilings retired there is no breach to report, and a distribution printed at every close would be a measurement nobody asked for at the moment they are least able to act on it. The on-request pass is the whole of what this item ships.

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

#### Claude keeps writing two-column fenced blocks that wrap into nonsense on the user's display [two-column-fences-wrap-unreadably]
Filed 2026-08-15 by Claude at the close's re-scan, from an instance it caused in this session.

**What happened.** The rewritten ladder was presented as a fenced block with a label on the left and its explanation in a right-hand column. On the user's display the right column wrapped underneath the left, so the two ran together and half the rungs appeared to have no title. **Her words: "there's no title on half of them. what do they mean."** The content was fine; the layout destroyed it, and a second message in plain lines fixed it immediately.

**Why this is a capture rather than a one-off slip.** The wrapping behaviour was already known here when the block was written anyway. **The item that recorded it is gone, checked at processing 2026-08-19 rather than assumed:** [fences-wrap-so-prose-rule-reason-is-false] was filed 2026-08-07, grew to roughly 1,500 words, and left the queue — it survives only as a line in `resources/research/written-shape-length-growth.md`. Its subject was a prose rule whose stated *reason* was false, which is an argument about a justification rather than about what Claude emits, so there was nothing to fold into. This item's own instruction to check that first is what caught it. The shipped docs are also full of this format: `skill-nonspecific-rules.md`, `plan.md` and `done.md` all use two-column fenced blocks heavily, and Claude reads them at every session start, which is the likeliest reason it keeps reproducing the shape in chat.

**The distinction that matters, and what a fix has to get right.** A two-column block inside a procedure doc is read by Claude, in a wide view, and works. The same shape emitted *to the user* is read on whatever display they have. So the rule is about output, not about the docs — a fix that reformatted the procedure docs would solve the wrong half.

**Settled at processing 2026-08-19, and the shipped rule already answers this one sentence short of the point.** The always-loaded render rule states what a fence is *for*: a paste target, or content whose exact characters **are** the substance — code, shell commands. A labelled two-column layout is neither; it is explanation wearing a fence. So the block that broke on your display was already outside the rule. What the rule never says is that using a fence for anything else is wrong, and the procedure docs model the wrong shape at scale, which is why it recurs.

**What changes.** One clause on `skill-nonspecific-rules.md`'s "How inline text is formed" block, beside the two entries already there: structured explanation shown to the user goes **one item per line, never in aligned columns**.

**Reformatting the procedure docs is refused, on this item's own reasoning.** A two-column block inside a procedure doc is read by Claude in a wide view and works. The rule governs output; rewriting the docs would fix the half that is not broken.

**Placed before the restyle passes deliberately**, so [law-prose-restyle-heavy-docs]'s subordination lens meets this clause as part of the file rather than after it, and does not have to handle the same text twice.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — the View-in-doc rendering section's inline-forming block. **No SPEC sentence is owed**, asked at the keep-step rather than left implicit: SPEC describes pointer-versus-inline rendering and says nothing about what a fence is used for, so nothing there goes wrong or incomplete. **No FAQ entry** — this changes what the user sees, not anything they do.

Rule gate: run — admitted as a subordinate clause on the existing render rule's inline-forming block, so no freestanding rule and no always-loaded slot spent. **Nothing is evicted, stated plainly rather than dressed up as a merge.** Failure evidence is thin by count — one clear instance, your own display — and carries on cost rather than weight: the failure is visible to the user, wastes a whole message, and the fix is a sentence. **A hook was considered and refused: nothing mechanical reads Claude's chat output.**

#### Explain the slug once in the queue header, and say what an item is for every time one is shown to the user [slug-never-explained-to-the-user]
Captured by you 2026-08-14. Your point, rendered in Claude's words rather than quoted: you have never actually known what the bracketed part of the title is for — it just randomly emerged one day and you didn't have time to deal with it.
**The gap.** The slug is load-bearing structure: it is what `Blocked by:` resolves against, what the queue lint checks, what a LOG entry names to say which item it built, and what Claude uses to refer to an item exactly in chat. None of that is stated anywhere the user reads. It appeared in their own documents and they worked around it for weeks.
**Why this is not solved by the slug being harmless to ignore.** It is harmless to ignore only once you know you may. Until then it is unexplained structure in a document the user is asked to read and approve, and the method's own standard is that unreadable is unapprovable.
**Widened at processing 2026-08-19 to carry a second half you raised in the same session, and this entry is rewritten rather than appended to.** What came out is the original three-way choice between header, FAQ or both, now settled as both. Your point: the way captures are presented at processing must not assume the reader already knows their content, and at minimum **a referent should be given not by name but also by its purpose.** A second item was refused in favour of the merge — two entries on one notation would answer the same question twice.

**Two halves, at opposite ends of the same subject.** The notation is explained **once**, in the queue's own header, where anyone opening the file meets it: what the bracketed name is for, and that the user never has to write one. Then each **use** stops being opaque: a slug shown to the user carries what that item is for on its first appearance in a message.

**Scope is output, never documents**, which is the same split [two-column-fences-wrap-unreadably] settled the same day. Inside queue prose slugs stay bare — the always-loaded rule deliberately requires citing items by slug there, that text is read by Claude, and glossing every citation would inflate the entries this queue already struggles with.

**First use per message, not per chat.** Per chat makes a message readable only to someone holding the scrollback in their head, which is the assumption being objected to. The cost is a clause each time, stated rather than presented as free.

**The parent is the vocabulary rule**, which already asks whether a term is used in passing or explained and already lists a dozen internal terms to translate or omit. **A slug cannot simply join that list**: omitting it loses the one handle the user has on an item. So it is a third arm on an existing table.

**Evidence, unusually strong for this corpus.** Two recorded instances in the user's own words — *"I don't know what 'checkpoints' is"* and *"I don't know what 'fixing on the spot' means"* — this entry's own account of working around the brackets for weeks, and the planning session that settled it, whose every checkpoint named an item by bare slug while several messages cited three or four more.

**One cost stated rather than discovered.** The header clause reaches new projects only: an existing project's queue header is the user's own text, and the method's migration is barred from rewriting user prose. For them the FAQ entry is the whole answer.

**Files:** `plugin/throughliner/docs-b/setup.md` (the queue header it authors), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the vocabulary rule's third arm), and `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. **No epoch bump** — no existing file becomes structurally wrong. `SPEC.md` is not listed: it describes the queue's structure without describing the slug notation, so no sentence there goes wrong or incomplete. Shipped, not host-only — every consumer meets the same unexplained brackets.

Rule gate: run — admitted as a third arm on the always-loaded vocabulary rule's existing in-passing/explained table, subordinate rather than freestanding. **Nothing is evicted, stated plainly rather than dressed up as a merge of rules.** Failure evidence is four instances, two of them the user's verbatim words. **A hook was considered and refused: nothing mechanical reads Claude's chat output** — the same finding reached independently by [two-column-fences-wrap-unreadably] hours earlier, which is what makes it a property of the surface rather than of either item.

#### Routing communication feedback to memory masks the method defect that produced it — the memory-boundaries rule needs the exception [memory-masks-method-defects]
Captured by you — raised 2026-08-09 at a /done close, filed after `115f851`. Your point, rendered in Claude's words rather than quoted: if Claude's replies are affected by memory, then the method can't truly be tested.
**The conflict the shipped rule does not see.** plugin-behaviour.md's memory-boundaries rule lists what memory is free for: user preferences, working style, **communication feedback**, cross-project facts. Separately, this project's CLAUDE.md states that all use of the plugin to develop the plugin is testing it, and that any moment session memory covers for something the docs should carry is a mandatory capture. Nobody applied that second rule to *persistent* memory, and the two disagree: saving communication feedback to memory is permitted, and doing it here contaminates the only test the method gets.
**Why it is sharper than a self-hosting quirk.** Communication feedback is very often *evidence about the method's own narration rules*. This session demonstrates it: the user twice said there was too much text — evidence that the /plan checkpoint is too long, filed as [done-invoked-when-user-meant-continue]. Had that also gone to memory, Claude would simply have behaved better, the queue item would have stopped mattering, and the defect would have survived in the shipped docs. Memory would quietly buy a fix for one user while every consumer kept the bug.
**So the routing test is not "is this a preference?" but "is this evidence about the method?"** A preference no method rule governs — a name, a timezone, a tool the user likes — stays memory's. Feedback that a *method-produced behaviour* was wrong is a testing outcome and belongs in the queue, whether or not it also reads as a preference. The overlap is the problem: it is genuinely both, and the current rule names only the branch that silences it.
**Settled at processing 2026-08-19, and the scope goes the opposite way to the one this entry proposed.** It asked whether the exception should be scoped to projects testing the method. **Your decision: general.** A consumer's complaint that Claude narrated badly is evidence about the method too, and it is the **only** such signal originating outside this project — routed to memory it makes their Claude quieter and tells the method's author nothing. Scoping the rule to self-hosting would have protected the one project that already has other ways of noticing and left every other project silently absorbing the evidence.

**So the fix needs no new machinery, because the route already exists.** The three-way discriminator already sends "the method is misbehaving" to the feedback channel and "my app" to the queue. The memory-boundaries rule simply never cross-references it: it names communication feedback as memory's and stops there.

**What changes.** The bare term **communication feedback** comes off memory's list and is replaced by the qualified form — feedback about a behaviour the *method* produced routes by the discriminator, while a preference no method rule governs (a name, a timezone, a tool the user likes) stays memory's.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — Routing and discipline, the memory-boundaries rule. **The file named when this was captured, `plugin-behaviour.md`, was retired 2026-08-10** and the rule moved; the stale pointer is corrected here rather than left for the build to discover. Plus `plugin/throughliner/templates/faq-template.md` with `FAQ/faq.md` and both index lines — the FAQ fires because what the user *does* changes: feedback that used to be absorbed silently now becomes a report they are asked to approve and send. **`SPEC.md` is not listed, checked rather than assumed:** it describes no memory routing anywhere, so no sentence there goes wrong or incomplete.

Rule gate: run — admitted as a qualification on the existing memory-boundaries rule, subordinate rather than freestanding, so no always-loaded slot is spent. **The eviction is the bare `communication feedback` entry on memory's list**, which is what made the two rules disagree. Failure evidence is one recorded instance here plus the structural argument that the affected signal is the only external evidence the method receives.

Relates to [done-invoked-when-user-meant-continue] (the live instance). It used to be a candidate payload for [self-hosting-auto-detection], deleted 2026-08-14 — the absence of any payload only detection could switch on is what settled that item, and this settlement is the same conclusion reached from the other end: the rule wanted widening, not detecting.

#### The rules disagree on how a planning record splits — "per item processed" against "per decision" [plan-entry-split-wording-disagrees]
Filed 2026-08-18 at the close that had to choose between them.

**The two statements.** `skill-nonspecific-rules.md`'s authoring standard says a plan entry "splits per item processed", and reasons from there: a planning decision IS a disposition on a queue item, so the build case's machinery applies unchanged. `SPEC.md` and `done.md` both say a planning record "splits per decision".

**Why the difference is not cosmetic.** They diverge whenever one decision settles several items, which is common — this session settled two SPEC items together, five mailbox items as one group, and two restyle items as a pair. Counted per item the close owed roughly 28 entries; per decision it owed 19. At the measured 316–329 words per split entry that is around 3,000 words, plus an index line each on a file read in full at every retrieve.

**What this close did, so the precedent is visible rather than silent.** Split per decision, on SPEC's and `done.md`'s wording, with the choice put to the user and deferred back.

**Settled at processing 2026-08-19 by reading the code, and it goes against the lean recorded above.** `queue_digest.py`'s `shipped_slugs()` resolves shipped-ness from **filenames** — `<date>-<slug>.md`, one directory listing — so a slug has shipped if and only if an entry is named after it.

**"Per decision" therefore breaks two mechanisms rather than merely costing less.** A decision settling three items produces one file named for one of them, and the other two read as never shipped. The digest's shipped-citation flag misses them, and the below-the-line revisit — which reads shipped-ness off LOG to decide what may lift — would leave a held item waiting on a blocker that had in fact been settled. That is the failure this queue has recorded four times, reintroduced by a wording choice.

**So "per item processed" is right and the always-loaded file was already correct**, which matters because it is the wording a session reads at the moment it decides. `SPEC.md` and `done.md` are what change.

**The measured cost is real and is not paid in full.** The instance that filed this owed roughly 28 entries per item against 19 per decision, about 3,000 words plus an index line each. **Where one decision settles several items, one entry carries the reasoning and its siblings cite it rather than restating it** — each still named for its own slug, so every mechanical reader keeps working, and the argument is written once. That is the relocate-and-cite pattern already used for research findings and for narrative moved into a chat entry; nothing new is invented.

**This entry's own premise was half wrong, checked at processing rather than trusted.** It states that `SPEC.md` and `done.md` both say "per decision". **SPEC says no such thing** — it never describes how a planning record splits at all, and grepping it for the wording and for every paraphrase returns nothing. So the repeal is one file rather than two, and no SPEC sentence is owed.

**Files:** `plugin/throughliner/docs-b/done.md` — the "per decision" wording at the entry-splitting statement, plus the sibling-citation clause, sited there rather than in the always-loaded file because the close is where it is read. **No FAQ entry:** this changes how records are written, not anything the user does.

Rule gate: run — admitted as an amendment reconciling two live statements to the one already in the always-loaded file, plus one clause on `done.md`'s existing entry-writing step; no freestanding rule and no always-loaded slot spent. **The eviction is the "per decision" wording, repealed in two live files.** Failure evidence is one measured divergence and one mechanical dependency, the second of which involves no judgment at all.

Relates to [split-action-defeats-the-bands-in-aggregate], which measures what the split costs, and [plan-entry-split-action-underspecified], shipped.

#### Restyle `done.md` and `plan.md` to the law-prose standard [law-prose-restyle-heavy-docs]
Filed 2026-08-17 **on your decision that the restyle continues to the rest of the corpus.** [law-prose-restyle] shipped this morning covering `skill-nonspecific-rules.md` alone and was consumed by that build, so the continuation had no queue item at all.

**These two first** because they are the largest rule-bearing docs and both are already scheduled for subtraction work, so findings have somewhere to land.

**What changes.** Each doc rewritten to the wording standard the rule gate specifies: prohibitions restated as the action required, qualifications carried by structure rather than explanation, main clause first, one idea per provision, and rationale moved out of operative statements into the record. The shipped pass is the precedent for what that looks like in practice.

**Acceptance test, taken from the pass that worked:** rule-statement count before and after, accounted for statement by statement, with any change composed rather than asserted — `resources/rule_signals.py` reads the count. **Its stated limit is inherited too:** a flat count cannot detect a rewrite that changed a rule's meaning, so the pass claims coverage of what it read and nothing more.

**Ordering, written into both entries.** This runs before [law-prose-restyle-remaining-docs], and both run before [session-occurrence-audit], which reads these same files and would otherwise gather a list the rewrite makes stale — that is why the audit is held.

**A second lens rides this pass, folded in from [freestanding-rules-that-should-be-subordinate] on your instruction 2026-08-17.** While each doc is rewritten, look for the signature that item names: **two or more rules governing the same subject, stated at the same level, with no declared relationship** — and land them as a parent with subordinate units, which is what the admission rule already requires of a rule being authored and which nothing has ever applied backwards to rules already shipped. Candidate subjects it names besides length: what gets written where, when to ask versus proceed, and what counts as evidence.

**One interaction the fold creates, stated so the acceptance test is not misread.** Subordinating two rules under one parent **reduces** the statement count. So a fall in the count is no longer automatically an eviction: each reduction is attributed to either a merge under a parent or a deletion, and named as one or the other. Without that, this lens and the flat-count test contradict each other.

**And the gap the fold would otherwise leave, closed here.** The known instance — at least three separate statements about how long something should be, none referencing the others — is in `skill-nonspecific-rules.md`, which was restyled this morning **without** this lens. So that file is in this item's scope for the lens alone, not for a second restyle.

**This pass carries TWO lenses, not three. The per-paragraph rationale lens was folded in on 2026-08-17 and taken back out on 2026-08-19** — do not restore it here; it lives in [rationale-lens-after-the-build-view], held until [split-the-cleared-region-for-concurrent-sessions] ships. What removed it was evidence, not preference: the test that lens was waiting on came back confirmed, in `resources/research/rationale-flows-from-items-into-shipped-docs.md`, showing that reasoning written into a work item reaches the doc a build edits — in the settling case with the clause order intact and the final sentence identical, where the item had directed nothing. So the rationale in these two docs arrives from upstream, and a per-paragraph pass would strip text the next build writes back. **The other two lenses are untouched and this item is otherwise unchanged**: the wording restyle and the subordination lens read the docs as they stand and owe nothing to where the text came from.

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

**What this item deliberately does NOT carry, stated so it reads as a decision rather than an omission.** The per-paragraph rationale test does not run here — and as of 2026-08-19 it does not run in the heavy-docs pass either, having moved to [rationale-lens-after-the-build-view]. These ten docs keep the **signature-phrase** criterion for rationale, which is what they have had, and that is unaffected by the move. The reason is measured rather than guessed: extending per-paragraph judgement across the fetched docs was costed at roughly 42,000 words of it, and that figure is why the earlier extension was refused. [rationale-audit-fetched-docs-gap] recommended the two-file limit for exactly this reason, and folding the lens everywhere would quietly overturn its own recommendation while claiming to honour it.

Rule gate: run — no rule authored, amended or evicted; an extension of an already-admitted standard to the remaining files, carrying the same silent-authoring caution as its sibling and the same lens.

#### [user] Discord post: Claude now knows how the work cycle actually fits together [discord-post-cycle-awareness]
Captured by you 2026-08-12; the angle is yours — awareness of the build cycle.
**Cannot be written until [cycle-summary-at-every-skill-opening] has shipped.**
**The honest before-picture, also the strongest material.** Every piece was documented — what an audit does, what a capture is, what /plan may process, what /next may build — and nothing stated the loop. Claude assembled it wrong twice in consecutive sessions, both times confidently, reasoning that a planning session between an audit's findings and their build meant the findings couldn't reach the build. That is the cycle working. Your objection the second time, rendered in Claude's words rather than quoted: this is the second planning session in a row where you've had to explain it.
**The design point worth including.** A flat list of stages would not have prevented either failure, because both were about a loop *closing*. What shipped names the return edges explicitly.
**Same judgment as the sibling post:** the before-picture is Claude getting it wrong; publishing that is yours to decide.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [cycle-summary-at-every-skill-opening] shipped — `LOG/2026-08-12-cycle-summary-at-every-skill-opening.md`. Ordinary ready work. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: second in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone held it.

**Lifted to the head of the chain 2026-08-19, on your instruction, and the pacing is untouched.** What moved is which post goes first, not how often one goes out. [discord-post-context-adjacency] gave up the head because its subject was overtaken by the ladder work settled the same day; this post's own feature shipped 2026-08-12 and nothing about it has changed since, so every claim in it is true of the installed plugin. The three posts behind it still follow in order, one a day.

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

**Lifted 2026-08-15.** The holding fact — a day has passed since the last announcement — is true regardless of whether one went out on the 14th, and more clearly true if none did.

**Held again 2026-08-19, on your instruction, and its subject has now been overtaken a second time.** The post announces a ladder of three rungs where every rung costs no judgment. [decay-rung-unreachable-in-practice] was settled the same day and replaces that ladder with four rungs — an intersection rung and an alternating one — so the claim survives only until that work ships. **Posting it first would have announced a mechanism this project had already decided to replace**, which is [repeal-falsifies-a-posted-claim] happening rather than being guarded against. [discord-post-cycle-awareness] took the head of the chain instead.

**Waiting improves the post rather than merely deferring it.** The honest subject becomes the whole sequence: six rungs cut to three, then the bottom rung found to be unreachable in practice and the ladder rebuilt so it cannot starve. A mechanism got wrong twice and corrected in public is the register that has worked here before. **Rewrite the subject when this lifts — it will be the third.**

Blocked by: [decay-rung-unreachable-in-practice]

#### Allow a plan session and a build run at the same time, so ideation is never shut off [concurrent-plan-and-build-sessions]
**Split from [split-the-cleared-region-for-concurrent-sessions] at processing 2026-08-19**, which carries the single-writer split this depends on. **Raised by you, and the case is yours.**

**Your two reasons, and the second is the stronger one.** You already switch every minute or so because of wait times — today between whole *projects*, losing the context each time, where switching within one project would be a straight focus win. And a semi-autonomous run occupies the only session you have, so for the whole time it runs you cannot capture anything. **SPEC's first principle — that the user must be able to ideate at any point in the build cycle — is therefore false today**, and this is what makes it true.

**What it repeals.** The always-loaded rule says work on a project from one chat at a time, because a capture filed in one chat is invisible to the other and the two disagree about the queue from the moment either writes. The build view answers exactly that: one writer, and a view regenerated rather than merged. The old objection does not reach this shape — but it was settled after the arrangement "fell over every time it was tried", so the repeal is written as a repeal, naming what changed rather than quietly dropping it.

**What is still to design, and it is the whole of this item.** Two sessions committing to one working tree is a git problem no file split touches. The plumbing exists — `session_start` already detects worktrees, reports commits a checkout does not have, and offers the merge back — so the choice is whether a build runs in its own worktree or both share the tree with a single committer. Then the shipped-slug cleanup at the next /plan opening, and the guard against resurrecting finished work, which rests on status being re-derived from LOG.

**Files (rough, settled once the git question is):** `skill-nonspecific-rules.md` (the one-chat rule), `plan.md` (the cleanup at the opening), `session_start.py`, `faq-template.md` plus `FAQ/faq.md` and both index lines, and `SPEC.md`.

Blocked by: [split-the-cleared-region-for-concurrent-sessions]

Rule gate: not needed at processing — the repeal is decided here but its wording waits on the git question, so the rule text is authored when this is next processed rather than at the build.

#### Run the per-paragraph rationale lens over `done.md` and `plan.md`, once the transcription is stopped at source [rationale-lens-after-the-build-view]
**Split out of [law-prose-restyle-heavy-docs] on 2026-08-19**, when the test that item was waiting on came back confirmed. The other two lenses in that pass are unaffected and stay with it; only this one moves.

**Why it moved rather than staying folded in.** The lens deletes a paragraph, reads what remains, and keeps the sentence only where the instruction is left incomplete without it. That works on text that is going to stay put. It does not work while the work items are still feeding rationale into these docs at every build — the pass would strip text the next build writes back, and have to run again. The evidence that this is actually happening is `resources/research/rationale-flows-from-items-into-shipped-docs.md`, tested against git rather than argued.

**What changes when it runs.** Every paragraph of `done.md` and `plan.md` gets the delete-and-reread test: a complete instruction after the deletion means what came out was history and it goes to the record; an unfinished one means it was operative and is written into the rule. The record carries each removal and where it went, site by site — which is what this pass gives up by folding judgement into the rewrite rather than auditing first.

**Files:** `plugin/throughliner/docs-b/done.md` and `plan.md`, plus `LOG/` for the site-by-site record of what moved.

Blocked by: [split-the-cleared-region-for-concurrent-sessions]

Rule gate: not needed — no rule is authored or amended. A pass that relocates rationale out of operative statements applies a standard already admitted, and the operational-versus-historical distinction it uses is the method's own delete-and-reread test.

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

**Skipped again 2026-08-19, and it is the item that produced the fix for its own condition.** Presented, found unchanged, and in being presented it made the pattern visible: three entries in one session waiting on something outside this project, none able to name a blocker, all re-offered every session. That is [not-before-reaches-unprocessed], kept and cleared in the same session. **This is its first candidate** — once `anthropics/claude-code#77134` ships, or a date is worth guessing at, the field goes here and the re-offering stops. Until the field is built there is nothing to write, so the skip stands.

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

**A fifth instance, carried here 2026-08-19 from [build-wrote-its-own-gate-disposition] when that item was deleted as already decided, and it is the sharpest of the five because the rule that failed was the gate's own.** A build in the eighteen-item run found itself authoring a shipped rule with no disposition to transcribe. `CLAUDE.md` instructs exactly that build to halt and say so. It had the instruction, and instead ran the gate's four questions itself and recorded the result — a description of an admission decision, written by the party that had already done the work, which is the failure the /plan siting exists to prevent. The design gap the deleted item suspected turned out not to exist: [stated-open-design-question-passes-the-keep-step] shipped 2026-08-17 in `7e3c1c8` and now refuses at the keep-step any item whose prose schedules a design decision into its build. What was left was a correctly worded rule that did not fire.

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

**A second instance, 2026-08-19, and it widens the question rather than repeating it.** A planning session amended a genuine rule — the no-write instruction about Taskflow, which gained an INBOX exception — living in a folder-level `CLAUDE.md` above this project. No gate was summoned, correctly by the trigger and wrongly by the subject. So the trigger misses rules held *outside the repository* as well as rules held in unlisted files inside it, and a path list cannot be extended to cover a file the repository does not contain. See [parent-claude-md-taskflow-no-write-stale].

**Also worth checking in the same pass:** whether any other file under `resources/` holds operative rules and sits outside the trigger. `retired-terms.md` and `rule_signals.py` are the obvious candidates, and both may turn out to be data and code rather than rules.

#### No test asserts that an origin claim goes unflagged, which is the whole of the provenance split [origin-claim-has-no-test]
Filed 2026-08-16 by the build of [provenance-splits-origin-from-quote], as adjacent work rather than part of it.

**What the suite covers and what it misses.** `resources/testing/test_queue_lint_flags.py` has four cases on the credit check, and all four survived the split untouched because each happens to use a quote-claim phrase alongside its `Captured by you`. So the suite still passes and still asserts only the half that did not change.

**The half that did change has no case at all:** a bare `Captured by you` with nothing quoted must now produce no warning. That is the entire point of the split — it is what stops Claude asking the user to prove her own work is hers — and a later session could restore the old phrase list with every test still green.

**Files:** `resources/testing/test_queue_lint_flags.py` — one case asserting a bare origin claim is not flagged, and one asserting a quote claim still is.

#### The build working file's Changes section falls behind its ticks, and only the ticks are enforced [changes-section-falls-behind-the-ticks]
Filed 2026-08-17 by Claude at its own close, from the reconcile against memory that `done-build.md` requires.

**What happened.** Across a twenty-six-item run, every item was ticked with a depth field and an index-entry candidate at the moment it completed — those three are named at the per-item completion step and all three held. The `Changes:` section did not: it carries per-file notes for roughly the first three items and the end-of-run summary, and almost nothing for the twenty in between. The gap was found by the close's reconcile, not by anything mechanical.

**Why the two behave differently.** The tick, the depth field and the index candidate are enumerated as a numbered set at one step, and the close reads each of them — a missing depth field is explicitly called a discipline slip. `Changes:` is described in `next-build.md` under "accumulate close notes as you go", with no step that reads it back and nothing that notices when it is thin. It is the one part of the working file whose absence costs nothing at the moment it is skipped.

**What it costs.** `done-build.md` sources each entry's `Files touched:` line from this section. With it thin, the close reconstructs the file list from memory of the run — which works in a chat that still remembers, and is exactly what fails in the fresh short session this method designs for. A crash mid-run would have left a working file that understates what was done.

**What to weigh at processing.** Whether `Changes:` joins the per-item completion set as a fourth required write, which is the shape that already works for the other three; or whether the close should read it against the ticks and flag a mismatch, which catches it later but costs nothing during the run. The first is more writes in the run, the second is a check at the one moment the information is already being reconstructed.

**One thing not claimed:** nothing was lost this time. The entries were written from a chat that still held the run, so the record is accurate — this is a defect in what the file would carry for someone else, found because the reconcile asked.

#### A personal bridge pushing `[user]` items into Taskflow as tasks, and reading completions back [taskflow-personal-bridge]
**Raised by you 2026-08-19**, from executing in another of your projects where the work is mostly `[user]` items. Your framing: Throughliner becomes an executive layer over projects Claude only half-implements, and sometimes you do not want to complete things in conversation — you want the to-do list. **The mapping is yours: a `[user]` item is a task, and its steps are subtasks.** The assessment below and the decomposition are Claude's.

**Your mapping is Taskflow's own model rather than an approximation, which is what makes the completion half work.** Taskflow's subtasks inherit their parent's Project, date and placement, and a parent has no checkmark of its own — it is complete only when every subtask is, and un-checking any child pulls the parent back out of the completed tray. So completion arrives as one derived signal per item, and a half-done item cannot read as done.

**Two decisions of yours, in your own words.** Route: *"design this against the file-based route now, with MCP as the later transport."* Scope: *"agreed, personal bridge to start."* So this is host-only tooling in this project, assuming your own Drive setup, and it ships nothing to consumers; promoting it to a shipped feature is a later decision this does not pre-empt.

**Why file-first rather than MCP.** Taskflow's paid tier already designs the channel — Claude reaching Taskflow through a remote MCP server — so Throughliner would be a client of a route Taskflow intends rather than an integration Taskflow's local-first principle forbids. But `[0020-remote-mcp-server]` and `[0019-ai-choice-flow-and-mcp-setup]` are unbuilt over there and cloud sync is their precondition. The same reasoning is already on their queue in `[strategy-doc-preview]`, in your words there: *"We're just here, so we don't need the MCP."*

**Two hazards found by reading their SPEC rather than assumed.** Taskflow runs on the phone against a local Room database, so a file route means producing a file that is carried onto the device, not writing where Taskflow reads. And their existing `[0014-json-export-and-import]` is a whole-database export and restore — pushing tasks through it would replace every other task in the app. What this needs is an **additive** import, which Taskflow has neither built nor designed.

**Not designable here yet, and that is why this is a capture.** The file contract, which Taskflow Project a pushed item lands in, and when a push happens all depend on what Taskflow agrees to build — so the second limb cannot be stated. It waits on [taskflow-bridge-request].

**One thing to settle at processing regardless of their answer:** a `[user]` item's text can name real people or client details, so what crosses the boundary needs the scrub the queue already gets, and a pushed task is leaving this project's records.

#### Five cleared items each add a clause to the same keep-step, and nothing looks at the total [keep-step-accretes-from-five-items]
Filed 2026-08-19 by Claude, from a coherence check across the cleared region that you asked for at the end of a planning session.

**What was found.** Five items sitting cleared to run each add a limb or a clause to **one step** — `plan.md`'s two-limb keep check. [folding-in-has-no-eviction-step] adds the merge-versus-supersession rule where an item's rationale is authored. [missed-spec-write-interrupts-the-run] adds the SPEC question. [cross-project-work-completes-invisibly] adds the names-what-would-show-it-done clause. [repeal-has-no-ripple-trace] adds a third limb requiring a grep. [not-before-reaches-unprocessed] adds the date approval. Each was admitted separately, each is defensible on its own, and **no item names any of the others** or states what the step looks like once all five have landed.

**Why that matters rather than being tidy-mindedness.** The gate's own admission test asks what a rule replaces, which catches a rule competing with the corpus — it does not catch five rules converging on one step from five different sessions. A two-limb check becomes a seven-part one that nobody designed, in the doc a planning session reads at every item.

**And an unprocessed item already argues that step pushes too hard.** [research-packaged-as-build-work] records that the two-limb check's own force is what drives research into build items, measured three times in one day. Adding five more requirements to the same check is the direction that item warns about, decided piecemeal by sessions none of which could see the others.

**What this item is NOT.** Not a proposal to drop any of the five, each of which was admitted on evidence. Not a new rule about rules. **What it asks for is one reading of the finished step** — write out what the keep check says once all five have shipped, and decide there whether it is a step a session can actually run, or whether some of it belongs at a different site.

**When it runs matters.** It is worth nothing before the five are built and nearly nothing long after, so it belongs immediately behind the last of them rather than in the general queue. Which five ship together is not yet known, so no `Blocked by:` is written here — that is settled at processing, when their build order is.

**Files (rough):** `plugin/throughliner/docs-b/plan.md` — the keep-step, read whole. Host-only in origin but shipped in effect: consumers run this step at every item they process. Relates to [research-packaged-as-build-work], which is the same step examined from the other side.

#### The scope-lock guards files, and work that leaves the machine passes unguarded [scope-lock-guards-files-not-work]
Filed 2026-08-19 from INBOX mail sent by a private legal-evidence project running 1.20.0-test12. **Their user raised it; the sending project's Claude wrote the diagnosis, and she asked for both halves to be sent.** Identifying details from the message — the correspondent's folder path and the people it names — are deliberately not carried here.

**What happened there.** In one /plan session, that chat drafted a substantive letter to an external professional and the user sent it — the most consequential act of the session by a wide margin — and nothing gated it, because an email is not a file in the project. In the same session the scope-lock twice refused a four-line correction to that project's own CLAUDE.md, which the user had already read and approved.

**The guard fired on the trivial thing and was silent on the serious one, and that is not an argument for loosening it.** "What leaves the machine" and "what files get written" have come apart. The method's own rules already treat the first as the graver category — nothing is sent without the user seeing the exact text — but only the second is mechanically enforced, and the approval rule is a behavioural one that a session can simply not reach for.

**Their user's framing, which is the part worth carrying.** Throughliner governs work wherever it is conducted, not only work touching this machine. Her example: a `[user]` item in another project that involves unpicking a physical dress, nowhere near a filesystem, still work, still governed, still running under /next. The principle exists in the method; the enforcement stops at the file boundary.

**A vocabulary gap they also surfaced.** That session's Claude reached for `[freeform]` to describe what the session was doing, as though it were a mode a /plan session could slip into. It is not — it is a work-item flavour. Their user corrected it, which leaves live unqueued work happening inside a planning session with no name in the method at all.

**To settle at processing, and the obvious fix may be wrong.** A hook cannot see an email. Weigh whether this wants a rule at all, or whether the honest move is to state the limit plainly — the scope-lock covers files and nothing else — rather than implying coverage the mechanism cannot deliver. This project has repeatedly chosen the honest-limit route over a check that over-claims.

#### Both skills that detect a stale CLAUDE.md are barred from fixing it [claude-md-unwritable-by-the-skills-that-notice]
Filed 2026-08-19 from INBOX mail sent by a private legal-evidence project, and **independently reproduced here the same day**, which is what makes it structural rather than one project's bad luck.

**What they report.** /setup's migration step reads the project's CLAUDE.md for retired terms and reports what it finds, explicitly editing nothing because the file is the user's. /plan's scope-lock also excludes CLAUDE.md. So the two skills that actually detect staleness both cannot repair it, even where the user reads the finding and asks for the change in the same breath. In their session /setup found four stale lines, the user approved corrected wording immediately, and the outcome was a queue item for a build to apply text that was already written and agreed — while the file read at the start of every session stays wrong until then.

**The second instance, from a different angle.** This project hit the same wall hours earlier: a planning session found a folder-level instruction file both stale and duplicated, the user settled the correction in conversation, and the scope-lock correctly refused the write — so it became [parent-claude-md-taskflow-no-write-stale] rather than a four-line edit. Two projects, one day, the same shape: agreed text that cannot be written by the session that agreed it.

**They propose no fix and name two candidates with unweighed costs:** a permitted-edit carve-out, and letting /setup edit what it reports with approval. **A third exists and should be weighed with them** — that this is the lock working as designed, since a planning session writing rule text is exactly what the gate refuses, and the real cost is only the delay.

**To settle at processing:** which of the three, and whether the answer differs for the *project's own* CLAUDE.md versus a folder-level one above it. Relates to [parent-claude-md-taskflow-no-write-stale] (the local instance) and [gate-trigger-misses-the-audit-checklist] (rules living where no mechanism reaches them).

#### The shell-write guard blocked a scratchpad write while its own message says the scratchpad passes [shell-write-guard-blocks-the-scratchpad]
Filed 2026-08-19 by Claude at its own close, from an instance it caused minutes earlier.

**What happened.** A close needed to split one scratch file into two. The command was `py -c` writing two files inside the session scratchpad — outside the repository, self-clearing, and named explicitly rather than computed. `pre_tool_use.py` refused it. **The refusal text itself says: "If you genuinely need scratch space, the session scratchpad sits outside the repo and still passes."** It did not pass.

**Why this is worth a line rather than a shrug.** The guard is correct in substance — the fix was to use the editing tools, which worked — so nothing was lost this time. What is wrong is that the message tells the session a route is available and the same hook then refuses that route, which is the cry-wolf shape this project has repealed measures for twice. A session that believes the message will retry into the same wall.

**Two possibilities, and the item should not assume which.** Either the path check does not recognise the scratchpad directory at all, or it recognises it and the shell-write rule is deliberately unconditional — in which case the refusal text is what is wrong, not the behaviour. **Read the hook before designing anything**, since the whole defect is a mismatch between what the code does and what its own message claims.

**Files (rough):** `plugin/throughliner/hooks/pre_tool_use.py` and `resources/testing/` for whichever half turns out to be wrong. Host-only in origin; shipped in effect, since every consumer meets the same message.

#### The dispositions listing was run at a planning opening and never surfaced to the user [dispositions-listing-run-not-surfaced]
Filed 2026-08-19 by Claude at its own close, as a testing outcome from using the plugin to build the plugin.

**What happened.** `CLAUDE.md` requires the rule-gate dispositions listing to be surfaced at a /plan opening, alongside the digest and the held work. The session ran `rule_signals.py --dispositions`, read its output, and then folded nothing from it into the opening narration. The user never saw it.

**Why the omission matters more than the content did.** The listing exists because a refused rule proposal leaves one sentence inside one entry and nothing scannable — the user's own recorded question is *"how would I even know to demand it?"*. A listing that is run and not reported reproduces exactly the condition it was built to remove, and does so invisibly, since running it leaves no trace either.

**This is the siteless-check failure with a site.** The obligation has a stated moment and was still skipped, which is the harder case: the corpus already records four instances of a correctly worded rule failing to fire, and this is a fifth in a rule whose whole subject is making things visible.

**To settle at processing.** Whether the fix is wording, placement, or a required artifact — the last being the shape that has proven teeth here, as FAQ-sync and the gate line both show. Weigh against the cost: a line at every planning opening saying "nothing refused since the last planning session" is noise on most sessions, which is the objection that kept this a prose obligation in the first place. Relates to [gate-trigger-misses-the-audit-checklist] and to [standing-audit-programme]'s record of correctly worded rules that do not fire.

**Files (rough):** `CLAUDE.md`. Host-only — the listing does not ship and consumers never author method rules.

#### Throughliner as an executive layer over work Claude only partly does [executive-layer-positioning]
**Raised by you 2026-08-19**, from executing in another of your projects. Your framing: that project involves far more `[user]` work than Claude work, which turns Throughliner into an executive layer over projects that are only half-implemented by Claude, if that — *"and that's fine, but sometimes you don't want to complete things in conversation, you just want the to-do list."*

**Why this is filed separately from the bridge work.** [taskflow-personal-bridge] and [taskflow-bridge-request] carry the mechanism — pushing `[user]` items out as tasks and reading completions back. Neither carries the positioning claim, and the claim is the larger thing: it says what the tool is for in a case SPEC does not currently describe.

**What SPEC says today.** It describes a workflow for non-coders building apps with Claude Code, where the throughline keeps intent alive across sessions. Every example is Claude building software. A project whose work is mostly the user's own — physical, external, or simply done away from the machine — is not excluded anywhere, and is not described anywhere either.

**Two other things arrived the same day pointing the same way**, which is why this is worth processing rather than noting. A consumer project reported that Throughliner is meant to govern work wherever it is conducted rather than only work touching this machine, with a `[user]` item about unpicking a physical dress as the example — see [scope-lock-guards-files-not-work]. That is the same observation from the enforcement side.

**To settle at processing:** whether this is a SPEC addition describing a use the product already supports, or a positioning change that would pull design decisions with it. **It is product truth either way, so it is written at a planning session with you present** — and it must be your position rather than a rendering of it, which is the fault that produced the reading-position sentence struck from SPEC the same day.

**Files (rough):** `SPEC.md`. Relates to [taskflow-personal-bridge] and [scope-lock-guards-files-not-work].

#### A restyle item cites a source that is in neither the queue nor the log [restyle-item-cites-unreachable-source]
Filed 2026-08-19 by Claude, from a coherence check across the cleared region.

**What was found.** [law-prose-restyle-remaining-docs] justifies its two-file limit on the per-paragraph rationale lens by citing `[rationale-audit-fetched-docs-gap]` — *"recommended the two-file limit for exactly this reason"*. That slug is not a queue entry and has no LOG entry named after it, so a reader cannot reach the recommendation the item rests on. The same slug is cited from the heavy-docs restyle item.

**Why it is worth a line rather than a silent repair.** The reasoning may be sound and is probably recoverable from git or from an entry filed under a different name — but the item currently asserts a costed recommendation (roughly 42,000 words of per-paragraph judgement) on the authority of something nobody can open. That is the one-way-citation problem the superseded-research rule was built for, appearing between a queue item and a source that has gone.

**Deliberately not repaired at the moment of finding.** The coherence check that surfaced it was running at the end of a long planning session, and rewriting an item's justification is a keep-step decision rather than a tidy-up. Eight other unreachable citations in the same region were checked and are all correct as written — each names work deliberately deleted and states its fate in the same sentence — so this is the one residue rather than a class.

**To settle at processing:** find where that recommendation actually lives, by searching `LOG/` for the costing rather than for the slug; then either repoint the citation or restate the limit on its own evidence. If it cannot be found, say so in the item rather than leaving a citation that resolves to nothing.

**Files (rough):** `QUEUE.md` only — the two restyle items' prose. Host-only.

