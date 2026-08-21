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

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected).

#### [audit] Read the before-and-after output measurement and say whether the brevity amendment moved anything [brevity-amendment-outcome]
Filed 2026-08-21 alongside the two items it reads, because a measuring build that ships alone leaves nothing in the queue to read its output.

**What it reads.** `resources/transcript_output_length.py` run over transcripts from before [brevity-instruction-for-the-5-series] shipped and after, and reports the difference.

**What it must not do.** Declare a pass or a fail. There is no target, so there is nothing to pass — the finding is the direction and size of the change, stated plainly, including "no detectable change" where that is the answer.

**The honest limit, stated because this is the check on the one thing you most want fixed.** A shipped rule only reaches a session once the plugin is reinstalled, so an after-sample taken before a rezip and restart measures the old rules. Say which build the sample came from.

**Held because the dependency is host-side.** The amendment only reaches a session once the plugin is reinstalled and the app restarted, so this cannot resolve in the same session that builds it — it lifts once that item has shipped and a rezip has carried it into the installed plugin.

**This audit is the instrument's delete-time.** [transcript-output-measurement] is scoped as a one-off and carries a stated delete-time under the temp-file rule; the close that records this audit removes `resources/transcript_output_length.py`. The audit itself edits nothing, as an audit never does — the deletion is a close action, recorded in the same entry.

Findings become captures like any audit's.

**Lifted 2026-08-21.** [brevity-instruction-for-the-5-series] is built — `LOG/2026-08-21-brevity-instruction-for-the-5-series-2.md`, a build entry — and the rezip has carried it into the installed plugin: the host's build stamp and the target's both read `2c20f14b38aa`, so the amendment is live in sessions from now on. Both halves of the holding fact are therefore satisfied. **One constraint the lift does not remove:** the after-sample must come from transcripts written after that rezip, and the entry says which build each sample came from.

**Read this against [close-cost-scales-with-run-size] before drawing any conclusion.** That capture measured the seventeen-item run's chat output at median 20 words a message — below this project's own 55-word baseline — while its close wrote roughly 15,200 words into `LOG/`. So a large close is evidence about the record-writing step and not about narration, and this audit must not read one as the other.

--- Build block ---
Changes: none — an audit edits nothing. The one file operation belongs to the
  close that records this audit: delete `resources/transcript_output_length.py`,
  which carries a stated delete-time of "once this audit has reported".
Acceptance: a LOG entry reporting the before and after distributions, which
  installed build each sample came from, and the direction and size of any
  change. No pass/fail verdict and no target named. The instrument is gone from
  the working tree once the entry is written.
Refused: declaring success or failure — no target exists, so there is nothing
  to declare against.
--- End build block ---

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

**Lifted 2026-08-21.** [law-prose-restyle-remaining-docs] is built — `LOG/2026-08-21-law-prose-restyle-remaining-docs.md` — so the restyle has reached the rest of the corpus and a list gathered now is no longer stale before it is used.

**One thing the restyle left behind that this audit inherits.** [law-prose-pass-missed-mid-sentence-prohibitions] records that both passes found their targets by grepping for prohibitions that start a sentence, leaving roughly 150 mid-sentence ones unread. That is a gap in the prohibitions work rather than in the wording of the text this audit reads, so it does not re-hold this item — but the same shortcut is available here, and the build block below is written against it.

--- Build block ---
Changes: none — an audit edits nothing. It produces one classification per
  occurrence of "session", as a findings list in this session's LOG entry:
  means the chat, means a run, or correct as it stands and left alone.
  Files read: `plugin/throughliner/docs/` (every procedure doc),
  `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`, `SPEC.md`.
  Re-count first rather than trusting the ~707 figure in the prose above — the
  restyle passes rewrote this text after that count was taken.
  The stop-list is honoured rather than re-derived: "mid-session", "short
  session", "fresh session", "isolated session" and `done.md`'s "session type"
  all correctly mean the chat and are left alone.
Acceptance: a LOG entry carrying every occurrence with its file, its line and
  its classification — complete enough that [session-vocabulary-corrections]
  can be built from it without re-reading the corpus. The entry states how many
  occurrences were found and how the count was taken, so a later reader can tell
  a file that was read and found clean from one that was never opened.
Refused: gathering the list by grepping for qualified forms and inferring the
  rest — the reason this is an audit rather than a script is that deciding what
  each occurrence means is judgment on every line.
--- End build block ---

--- Cleared to run above this line ---

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

**Blocker repointed 2026-08-21, and the old one is resolved rather than merely replaced.** [decay-rung-unreachable-in-practice] has shipped and been confirmed, so the fact it named is gone — but the post is still held, by the one-a-day pacing chain, and [discord-post-cycle-awareness] sits at its head unposted. The field named a fact that had resolved instead of the fact actually holding the work, so every below-the-line revisit read this item as ready to lift and every one of them was wrong. Repointed at the item that genuinely holds it: the post now lifts by itself when the one ahead of it goes out, and no session has to remember today's reasoning. Claude's decision, deferred to by you. The subject rewrite is unaffected and stays required — see the paragraph above.

Blocked by: [discord-post-cycle-awareness]

## Unprocessed

#### Last session advises processing cut-length-remaining-docs next [forward-advisory]

The length cut is the work you have asked for repeatedly and it is now half done: SPEC and the always-loaded rules are repealed and re-bounded, and `plan.md` is cut, but thirteen procedure docs and CLAUDE.md are untouched. [cut-length-remaining-docs] carries the method that worked and the file list.

Worth processing alongside [law-prose-remaining-thirteen-docs], which reads the same thirteen files for a different defect — both passes read every provision in the file, so running them together halves the reading.

A /next run will not reach either: both are captures in Unprocessed and neither has been designed into a build block yet. The cleared region currently holds two audits and two `[user]` lines, and /next would walk the `[user]` items and stop.

One thing to decide when processing the length cut: whether it is `[freeform]` rather than a build. It is one file at a time, it is the work most likely to lose a rule if run unattended, and this session stopped it for exactly that reason.

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
**Files (rough):** `plugin/throughliner/docs/plan.md` — the keep-check sub-step, and the resolve-now block's hedge. Shipped, not host-only: this fires in every consumer's planning session, and the prompting instance was in another project.

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

**What is wrong.** The rule gate's trigger is mechanical and reads staged paths: a commit touching `plugin/throughliner/docs/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md`, or `CLAUDE.md`. `resources/method-compliance-audit-checklist.md` is not in that set, and its entire content is rules — the standing criteria every method compliance audit runs against. A session adding a criterion to it authors a rule, and nothing asks it to run the gate.

**How it surfaced.** [audit-axis-is-parent-not-sibling] adds two requirements to that checklist. Its gate ran because the session happened to notice; it would not have fired from the trigger. That is the failure this gate's design is against — a check depending on someone remembering is the shape the mechanical trigger replaced, and `CLAUDE.md` says so when it contrasts this trigger with FAQ-sync's undetectable one.

**To settle at processing, because the obvious fix may be wrong.** Adding the one path is a two-word change and closes this instance. The prior question is whether the trigger set should be a list of paths at all, given that a rule-holding file added later lands outside it again by default and nobody notices — exactly as this one did. A rule about which files hold rules has the same maintenance problem as the rules themselves. Whether there is a shape that fails safe rather than silent is the design question; if not, add the path and say so.

**A second instance, 2026-08-19, and it widens the question rather than repeating it.** A planning session amended a genuine rule — the no-write instruction about Taskflow, which gained an INBOX exception — living in a folder-level `CLAUDE.md` above this project. No gate was summoned, correctly by the trigger and wrongly by the subject. So the trigger misses rules held *outside the repository* as well as rules held in unlisted files inside it, and a path list cannot be extended to cover a file the repository does not contain. See [parent-claude-md-taskflow-no-write-stale].

**Also worth checking in the same pass:** whether any other file under `resources/` holds operative rules and sits outside the trigger. `retired-terms.md` and `rule_signals.py` are the obvious candidates, and both may turn out to be data and code rather than rules.

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

**Files (rough):** `plugin/throughliner/docs/plan.md` — the keep-step, read whole. Host-only in origin but shipped in effect: consumers run this step at every item they process. Relates to [research-packaged-as-build-work], which is the same step examined from the other side.

#### Both skills that detect a stale CLAUDE.md are barred from fixing it [claude-md-unwritable-by-the-skills-that-notice]
Filed 2026-08-19 from INBOX mail sent by a private legal-evidence project, and **independently reproduced here the same day**, which is what makes it structural rather than one project's bad luck.

**What they report.** /setup's migration step reads the project's CLAUDE.md for retired terms and reports what it finds, explicitly editing nothing because the file is the user's. /plan's scope-lock also excludes CLAUDE.md. So the two skills that actually detect staleness both cannot repair it, even where the user reads the finding and asks for the change in the same breath. In their session /setup found four stale lines, the user approved corrected wording immediately, and the outcome was a queue item for a build to apply text that was already written and agreed — while the file read at the start of every session stays wrong until then.

**The second instance, from a different angle.** This project hit the same wall hours earlier: a planning session found a folder-level instruction file both stale and duplicated, the user settled the correction in conversation, and the scope-lock correctly refused the write — so it became [parent-claude-md-taskflow-no-write-stale] rather than a four-line edit. Two projects, one day, the same shape: agreed text that cannot be written by the session that agreed it.

**They propose no fix and name two candidates with unweighed costs:** a permitted-edit carve-out, and letting /setup edit what it reports with approval. **A third exists and should be weighed with them** — that this is the lock working as designed, since a planning session writing rule text is exactly what the gate refuses, and the real cost is only the delay.

**To settle at processing:** which of the three, and whether the answer differs for the *project's own* CLAUDE.md versus a folder-level one above it. Relates to [parent-claude-md-taskflow-no-write-stale] (the local instance) and [gate-trigger-misses-the-audit-checklist] (rules living where no mechanism reaches them).

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

#### Sending a letter became a queue item for the first time, and sending at any moment is probably the better shape [mail-send-should-not-need-a-queue-item]
Raised by you 2026-08-20 mid-run, immediately after approving the send that prompted it. **Your view, and it is the thing to weigh: normally mail can be sent at any time, and you think that is preferable.** Filed while it can still be judged rather than settled in the run, since deciding what shape sending should take is planning work.

**What happened.** [taskflow-bridge-request] was processed into Processed as an ordinary build item whose entire work product was one message file written into another project's mailbox. So a run was scheduled, scope was locked, and a build item was ticked, in order to send a letter — where the same letter could have been drafted and approved in any chat at any moment, which is how every other outbound message this project has sent was handled.

**Why it may nonetheless have been right here, stated so the weighing is honest.** The message carried three asks that were designed in a planning session, and another queue item — [taskflow-personal-bridge] — is held against the answers. Making the send a queue item is what makes that dependency visible and gives the answers somewhere to land. A send drafted ad hoc in a chat leaves no trace that anything is now waiting on a reply.

**So the question is not whether mail needs a queue item, but which sends do.** A one-off question to another project plainly does not. A send that other queued work waits on plainly leaves something behind that has to be tracked. Whether that tracking belongs on the *send* or on the *held item that names what it waits for* is the actual design question, and the second reading would remove the need for a send item entirely — the held item already carries `Blocked by:` and could as easily name what it is waiting to hear.

**Relates to [send-record-lacks-destination-and-intent]**, cleared to run in this same session, which gives every outbound artifact a line in `INBOX/sent.md` carrying destination, intent and what was claimed. That may already be the tracking this item is reaching for, in which case a send never needs to be a work item at all — which is worth checking before anything is designed here.

#### Audit this project's own claims against what Claude Code alone already delivers [claims-need-a-claude-code-delta-test]
Filed 2026-08-20 at the close, from INBOX mail sent by the flintcraft.tech site project. Their finding, not ours, and it lands on this project's SPEC rather than on their page.

**What happened there.** A friend read their Throughliner page and asked how the method stops the problems it lists. The user had to admit most of them are fixed by moving from the chat app to Claude Code at all. They audited the page's eight claims: **three are Claude Code's outright, two partly, two are skills neither tool fixes, and one is squarely Throughliner's.** They have made that a cleared work item and a new rule in their own SPEC — a claim only earns its place if Claude Code alone does not deliver it.

**Why it is work here and not only there.** Their page describes this method, so a claim that fails their test fails it wherever it is written — including in this project's own `SPEC.md`, its README, and any Discord post. Nothing here has ever applied that test. The `CLAUDE.md` Discord rule says a post announces changes to Throughliner, and the SPEC's "What it is worth to the user" section makes several claims of exactly the kind their audit found weakest.

**The test, in their words rather than ours:** does Claude Code alone deliver this? If yes, it is not a Throughliner claim.

**What this does not settle.** Whether the ratio they measured on their page holds for SPEC's claims is unknown — it is one project's audit of one artifact, and repeating it here is most of the work. It also cuts both ways: a claim Claude Code delivers may still be worth stating if Throughliner makes it *reliable*, and drawing that line is judgment rather than the binary their rule states.

**Relates to [executive-layer-positioning]**, which is the same question approached from the opposite direction — what Throughliner is for once the things Claude Code already does are subtracted. Worth processing together.

**A reply may be owed** — see `INBOX/sent.md` and the close that filed this.

#### The below-the-line revisit cannot lift anything a build session has not yet closed, and nothing says so [revisit-depends-on-a-log-that-the-close-writes]
Noticed by Claude 2026-08-20 at the close, from a question the user asked: she proposed running /plan before /done, to sort this session's loose ends while the context was fresh.

**Why that does not work, which is the finding.** `plan.md`'s below-the-line revisit decides whether to lift a held item by checking whether its blocker was built **and verified per the LOG**. A build run writes no LOG entries — its close does. So a /plan run in the same chat as a /next run, before that chat's close, sees no session record for anything the run just built and correctly declines every lift that depends on it.

**In this chat that would have been four items:** [queue-privacy-default], [concurrent-plan-and-build-sessions], [rationale-lens-after-the-build-view] and [repeal-falsifies-a-posted-claim], all of whose blockers shipped in this run. Sorting exactly those was the reason she wanted the planning session.

**The same blindness reaches the digest**, which resolves "cites shipped work" by looking for a LOG entry per slug — so every item this run built would read as unshipped for the length of that planning session.

**What is not wrong.** The revisit's rule is right: reading LOG is what makes "has this shipped?" answerable from the files rather than from memory, and a build-then-plan chat is not the shape the method designs for. Nothing here is a defect in the revisit.

**What is missing is that nobody is told.** `skill-nonspecific-rules.md` explicitly permits one chat to run /plan and /next as many times as the work needs, one after another — and that permission is what makes this reachable. A user following it in the order plan-after-build gets a silently degraded planning session, with no warning and no sign anything was skipped. The revisit skips silently by design.

**Options, none of them designed yet.** /plan's opening could notice an undeleted build working file and say plainly that lifts depending on this chat's own work will not resolve until it closes. Or the revisit could read the working file's ticks alongside LOG. Or the always-loaded permission could carry the one exception. The first is cheapest and needs no new state; the second reintroduces a second source of truth about what shipped, which is the thing LOG-as-authority exists to prevent.

**Recorded as answered in conversation and not otherwise.** The user changed course on being told, so this cost nothing here — which is exactly the siteless-noticing shape this project has recorded five times: it worked because Claude happened to say it, and it is not repeatable.

#### The plugin-managed CLAUDE.md block promises it is kept current and never is [managed-claude-md-block-never-refreshed]
Filed 2026-08-21 by Claude from INBOX mail sent by a consumer project running 1.20.0-test12.

**What they report.** A queue item had sat in their project for a week to fix four stale things in their `CLAUDE.md`: the pre-rename method name, a QUEUE.md description written for the retired batches / red-flags / deferred-tests / parked model, a `/next freeform` entry, and a rule naming `_build.md`. A /next run picked it up and halted, because **every one of those lines sits between the PLUGIN-MANAGED markers**, which read "do not edit between these markers. Updated on /setup and plugin reinstall."

**The shipped template was current the whole time.** They read `templates/CLAUDE-TEMPLATE.md` in the installed plugin and found the correct method name, the two-section queue, the cleared-to-run line, the flavour tags, the red-flag marker riding its own item, plus INBOX and `/rescan` entries their copy had never heard of. /setup has been run there since — their LOG records a migration on 2026-08-13 that updated the version marker and did not refresh the block.

**So the marker's own promise is the false part.** That is consistent with what /setup actually does — backfill what is missing, never overwrite what exists — and it is the one region of the file where the user is told not to look, so the staleness is invisible by design. That block is also the first thing every session in the project reads, so for weeks it described a queue model the project did not have to whoever was about to work on it.

**A second finding they made in passing, and it constrains any fix.** Four rules belonging to their project had ended up **inside** the managed block, carried over from an older template. A refresh firing then would have taken them silently. So whatever refreshes the block says what it is about to overwrite rather than replacing a region a consumer may have added to.

**They repaired their own copy by hand** — the block replaced with the installed template word for word, their four rules moved below the marker — so a future refresh there is a no-op rather than a conflict.

**To settle at processing.** Whether /setup gains a refresh path for the managed region, whether the marker's promise is rewritten to say what is actually true, or both. Relates to [claude-md-unwritable-by-the-skills-that-notice] and [spec-scaffold-describes-method-docs] — all three are content the method copies into a consumer document where the method can change and the copy cannot be reached.

**Files (rough):** `plugin/throughliner/docs/setup.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`. Shipped.

#### Should /setup be able to start a project from a template, and what would the unit be [setup-from-a-template]
Filed 2026-08-21 by Claude from INBOX mail sent by a project that has been running the method continuously for about two months. **It asks two questions and proposes nothing to build**, so what is captured is the question plus the evidence they attached to it.

**The idea.** /setup adopts a folder and interviews the user to fill SPEC, always starting from nothing. They ask whether it could instead start from a **template** — a pre-built folder carrying machinery, rules and empty scaffolding, chosen at setup time by what kind of work the project is.

**What they measured, from an audit of their own repository asking what a blank version of itself would consist of.** The proportions were not what they expected. The **folder structure** was the most reusable thing they had — six directories following the lifecycle of the work rather than the shape of any subject, transferring unchanged. The **scripts** transferred essentially unchanged too: about 1,500 lines across four tools, no hardcoded paths, no subject-specific logic, four lines naming people or local folders and all of those inside docstrings. Their **SPEC.md** came out entirely blank — four headings and nothing else, because every sentence of a real SPEC is about its own project.

**The rules were the real problem, and their finding there is the part worth having.** Most accumulated CLAUDE.md rules are generic in shape but proved by a dated, specific incident, and the incident does most of the work. Strip the incidents and what remains is assertions with no reason to be believed and nothing to recognise a recurrence by. Keep them and the template ships one project's private material to everyone who copies it. Their resolution: **generalise to the failure, not to the abstraction** — rewrite the incident so the mechanism survives and the people do not. What never works is reducing an incident to "a session once had a problem here", which keeps the cost of the words and loses the reason to believe them.

**The finding they say matters most if only one is taken: a template must never carry a decision the copying user has not made.** Their example is a hook capturing verbatim session transcripts into the repository — completely project-agnostic and transferable, while everything that *justifies* running it is not: a risk accepted, conditions attached, consent given by the people whose data it is. So their specification ships it disabled with the question in front of it. Any template mechanism hits this shape wherever a carried component encodes a judgement rather than a capability.

**Their two questions, unchanged.** Is a template concept in /setup wanted at all, or is starting from nothing the deliberate design? And if it is wanted, is the useful unit a whole pre-built folder, or something smaller — a rules pack, a scripts pack, a folder skeleton — chosen independently?

**To settle at processing.** The first question is the user's to answer and is a positioning decision, not a design one. **A reply is owed either way**, since they offered to supply the full specification. Relates to [executive-layer-positioning] and [claims-need-a-claude-code-delta-test], both of which ask what this product is for.

**Files (rough):** none until the first question is answered.

#### Every procedure doc ends on a terminal step, and none can tell finished from interrupted [procedure-docs-cannot-tell-finished-from-interrupted]
**Split from [rescan-does-not-hand-back] on 2026-08-21, on your decision**, once that item's three-file fix turned out to be fully specified while this half was not. The observation that started it is yours; the design question below is Claude's.

**What prompted it.** Claude Code's documentation says an invoked skill's content enters the conversation once and is never re-read, so *"write guidance that should apply throughout a task as standing instructions rather than one-time steps"* — see `resources/research/skill-content-lifecycle.md`. All five of this method's procedure docs are numbered marches ending in a final step, which is the shape that instruction warns against. /rescan is the confirmed instance: its terminal step reads as the end of the conversation's work.

**Your evidence, and it is what makes this a design question rather than a rewrite.** Asked whether the same property affects /plan and /next, you said it is a problem sometimes: **sometimes the session ends when planning or building is done, and that is correct**; and sometimes the skills need to be alternately run depending on the conditions — not normally, but sometimes.

**So the naive fix is refused before it is proposed.** "Stop ending" is wrong, because a terminal step is right in the common case. Rewriting five docs to end conditionally, with nothing able to read the condition, replaces a doc that always ends with a doc that guesses — and a guess reads as a decision, which is worse than a consistent ending someone can learn to work around.

**The actual question: can a procedure doc tell which case it is in?** Three candidate signals, none weighed yet. What the user last asked for, which is in the conversation and is what /rescan already reads to do its job at all. Project file state, which is what the scope-lock already uses — `pre_tool_use.py` decides a session is a planning one purely from the absence of this session's build working file, so file state is a proven readable condition. Or nothing, in which case the honest outcome is that each doc's ending states plainly what it does and does not know, which is the honest-limit route this project has chosen repeatedly over a check that over-claims.

**Why it cannot be kept yet.** The file list is the audit's own output, which fails the keep check's second limb by construction. What changes inside each doc depends on which signal survives, and no signal has been tested. **Do not schedule the design into the build** — an item whose prose defers a decision to the start of a run fails the same limb.

**What would settle it, and who owns each part.** Whether a doc can read its own situation is a fact to be established by reading `pre_tool_use.py`, `rescan.md` and the conversation-reading `rescan.md` already does — Claude's to find. Whether an honest "I don't know whether you were mid-something" ending is acceptable output is yours, since it is a decision about what the tool says to a user rather than about what it can do.

**Runs behind [rescan-does-not-hand-back]**, which fixes the one confirmed instance. Placement carries that and this sentence carries the reason: no `Blocked by:` is written, because this could be designed independently — it is only cheaper afterwards, since that build establishes what a corrected ending actually looks like.

**Files (rough): not yet derivable, which is the point of not keeping it.** Likely `plugin/throughliner/docs/` across the procedure docs, and possibly nothing at all if the answer is that no signal exists. Shipped in effect: every consumer runs these docs. Relates to [plan-does-not-build-keeps-being-relitigated] and [standing-audit-programme], both of which record a doc's own wording teaching a later session the wrong thing.

#### Four inbound messages changed work here and the rule to draft a reply fired for none of them [inbound-replies-not-drafted]
Filed 2026-08-21 by Claude at a /rescan, **as a testing outcome from using the plugin to build the plugin.** The failure is Claude's own, in this session, and nobody noticed at the time.

**The rule that did not fire.** `skill-nonspecific-rules.md` says: *"When an inbound message changes work here, draft the reply unprompted in the same chat and put it in front of the user."* The send stays under the never-send-unseen guarantee; what the rule adds is the **offer**.

**What happened.** Four messages were read, triaged and archived at this session's opening. All four changed work here — they produced five new captures between them and one fold into an existing item. **Not one reply was drafted, and the rule was never reached for.** The mail step's own procedure was followed exactly: read, route, archive. It says nothing about replying, so nothing in the moment prompted it.

**The messages, and what each is owed.** Three reported defects now filed as [digest-diamond-read-as-a-loop], [lint-flags-its-own-scaffolding], [inbox-scan-counts-os-metadata-files] and a fold into [stop-hook-fires-on-cited-slugs] — those senders are owed at most an acknowledgement that the reports landed as work. **The fourth is different and is the one that actually matters**: [setup-from-a-template] asks two direct questions and offers to supply a full specification. It is a question with nobody answering it, and the sender is waiting.

**Why this is structural rather than one lapse.** The reply obligation lives in the always-loaded rules; the mail procedure lives in `feedback-and-inbox.md` and in /plan's opening step. **A rule with no site is the failure this corpus has recorded five times**, and the mail step is exactly the site it should have been written into — it is the one moment every message is in front of the session, already sorted by whether it changed anything.

**To settle at processing.** Whether the reply obligation gains a site in the mail step, or at the close, which is where a reply is already meant to be drafted for a /next run. Weigh against over-firing: an acknowledgement nobody needs is noise in another project's mailbox, and the rule's trigger is "changes work here", which three of these four meet only weakly. **The honest split may be that a message asking a question is owed a reply and a message reporting a defect is not** — which would narrow the rule rather than site it.

**One thing not claimed.** No reply is being written by this item; drafting still needs the user, and nothing is sent without exact wording approved.

**Files (rough):** `plugin/throughliner/docs/feedback-and-inbox.md` and possibly `plan.md`'s mail step. Shipped: consumers run the same mail step. Relates to [mail-send-should-not-need-a-queue-item] and [outbound-report-not-checked-against-the-world], both about the outbound half of this channel.

#### Flavour-specific close material sits in the file every close reads, and the restyle passes will not move it [done-md-carries-other-flavours-material]
**Captured on your instruction 2026-08-21**, after you asked why a planning close ran to roughly 6,000 tokens. The measurement is in `resources/research/why-the-close-is-heavy.md`; this item is the one lever that research names as unqueued.

**The measurement, in one line.** That close read **10,297 words of procedure** — `done.md` 7,443 plus `done-plan.md` 2,854 — to write **3,603 words of record**, about 2.9:1 against the output. The record is the smaller half, so shortening session records does not reach this.

**`done.md` is a fixed toll on every close in every project**, whatever the session did, and it is the second-largest doc in the method after `plan.md`. The sub-docs exist to carry flavour deltas, and a large amount of flavour-specific material is not in them.

**What a planning close reads and discards**, none of it skippable, because knowing which parts apply requires having read them:

```
the completion-verification step        build and audit only
the record-a-routing-step-sweeps block  build and audit only
the entry template's build body fields  build only
the entry template's audit body fields  audit only
the audit approval-outcomes line        audit only
the red-flag lifecycle                  only where a flag cleared
the isolated-session branch             only in a worktree
```

**Why the two queued restyle items do not cover it.** [law-prose-restyle-heavy-docs] applies the wording standard and a subordination lens; [rationale-lens-after-the-build-view] relocates rationale out of operative statements. Both make the text shorter where it stands. **Neither asks whether the text is in the right file**, which is a distribution question — the third limb of the rule gate, and the one nothing in the queue currently exercises over the close docs.

**The precedent is this project's own.** A run used to read the whole queue to build a handful of items; the build view now gives it only what it is building. This is the same shape one layer out — a close reading the whole close manual to run one flavour — and the remedy was simply never applied here.

**What to settle at processing, and the sequencing question is real.** Which material moves and which is genuinely shared; whether the entry template splits per flavour or stays whole with the sub-docs pointing into it, since a split template is the thing most likely to drift into four divergent copies — that risk is the argument the shared file was built on and it has not been weighed against the measurement. **And whether this runs before or after the two restyle passes**: moving text first means the restyle rewrites each paragraph once in its final home, but a distribution pass over text about to be reworded may move sentences that are then merged away.

**One thing not claimed.** No figure here is a target, and a shorter close manual that drops a step is worse than a long one that works — `done.md`'s length is largely accumulated repairs to real failures, several of which it names in its own text. **This item moves text; it must not delete any.** A rule that leaves `done.md` still exists, and the acceptance test is that nothing is lost.

**Files (rough):** `plugin/throughliner/docs/done.md`, `done-plan.md`, `done-build.md`, `done-audit.md`. Shipped: every consumer pays the same toll at every close. Relates to [law-prose-restyle-heavy-docs] and [rationale-lens-after-the-build-view] (the same files, a different lever), and to [split-the-cleared-region-for-concurrent-sessions] (the precedent).

#### The close cannot correct a marker /setup wrote wrongly, even with the user approving in the same breath [close-cannot-correct-a-marker-setup-wrote]
Filed 2026-08-21 by Claude at its own close, from an instance it caused minutes earlier. **A third project-independent instance of a shape already recorded twice.**

**What happened.** /setup wrote `4` into `.throughliner-format-epoch` this morning after skipping the epoch-4 conversion, so the marker asserts a shape this project does not have — and the marker is what `session_start`'s halt reads, so nothing will raise it. The defect was found at the close, put to the user, and she decided to set it back to `3`. **The scope-lock refused the write**, correctly: a planning session's standing list is QUEUE.md, SPEC.md, `LOG/`, `FAQ/`, `resources/research/` and the scratchpad, and the marker is on none of them. The close's own declaration marker permits one extra path, `README.md`, which does not help here.

**So a one-character correction, approved by the user in the same exchange, became a step inside a queue item** — recorded on [convert-cleared-items-to-build-blocks].

**Why this is not simply the lock working as designed, which is the obvious reading and is half right.** The lock exists so a planning session queues work rather than doing it, and it stopped a session from editing a file outside its remit — that much is correct. What makes it worth a line is the *asymmetry with the write that caused it*: **/setup could write the marker without any conversation, and no session can correct it.** The skill that can create the wrong state is the only one permitted to fix it, and it is the one skill that refuses to run mid-session.

**The pattern this belongs to, and the reason it is filed rather than shrugged at.** [claude-md-unwritable-by-the-skills-that-notice] records the same shape from a consumer project and from here on the same day: the skills that detect staleness are barred from repairing it, and agreed text cannot be written by the session that agreed it. [scope-lock-guards-files-not-work] records the guard firing on the trivial thing while silent on the serious one. **This is a third instance and the sharpest, because the state being corrected was created by the method itself rather than found in the wild.**

**Three candidates, none weighed, and the third may be right.** Add the epoch and version markers to the close's declaration list, which is already the mechanism for exactly this — paths a close's own obligations name that no build's file list can contain. Let /setup's migration correct a marker it previously wrote. Or accept it: the delay is one queue item, and widening a lock to admit a case the user approved is how locks stop meaning anything. **The third is a real candidate and must not be dismissed for being the do-nothing option** — this project has chosen the honest limit over a loosened guard before.

**One thing this does NOT argue for.** It is not a case for loosening the standing list generally. The list refused nothing else all session, and every other write this close made passed.

**Files (rough):** `plugin/throughliner/hooks/pre_tool_use.py` and `plugin/throughliner/docs/done.md` if the declaration list is the answer; `setup.md` if the second; nothing at all if the third. `resources/testing/` in the first two cases. Host-only in origin, shipped in effect: a consumer whose /setup writes a wrong marker is in exactly this position with no route out.

#### Allow a plan session and a build run at the same time, so ideation is never shut off [concurrent-plan-and-build-sessions]
**Split from [split-the-cleared-region-for-concurrent-sessions] at processing 2026-08-19**, which carries the single-writer split this depends on. **Raised by you, and the case is yours.**

**Your two reasons, and the second is the stronger one.** You already switch every minute or so because of wait times — today between whole *projects*, losing the context each time, where switching within one project would be a straight focus win. And a semi-autonomous run occupies the only session you have, so for the whole time it runs you cannot capture anything. **SPEC's first principle — that the user must be able to ideate at any point in the build cycle — is therefore false today**, and this is what makes it true.

**What it repeals.** The always-loaded rule says work on a project from one chat at a time, because a capture filed in one chat is invisible to the other and the two disagree about the queue from the moment either writes. The build view answers exactly that: one writer, and a view regenerated rather than merged. The old objection does not reach this shape — but it was settled after the arrangement "fell over every time it was tried", so the repeal is written as a repeal, naming what changed rather than quietly dropping it.

**What is still to design, and it is the whole of this item.** Two sessions committing to one working tree is a git problem no file split touches. The plumbing exists — `session_start` already detects worktrees, reports commits a checkout does not have, and offers the merge back — so the choice is whether a build runs in its own worktree or both share the tree with a single committer. Then the shipped-slug cleanup at the next /plan opening, and the guard against resurrecting finished work, which rests on status being re-derived from LOG.

**Files (rough, settled once the git question is):** `skill-nonspecific-rules.md` (the one-chat rule), `plan.md` (the cleanup at the opening), `session_start.py`, `faq-template.md` plus `FAQ/faq.md` and both index lines, and `SPEC.md`.

**Returned to Unprocessed 2026-08-21. Its blocker shipped and that is precisely why it could not stay where it was.** [split-the-cleared-region-for-concurrent-sessions] landed on the 20th with five suites passing, so nothing holds this item any more and the `Blocked by:` line is dropped. But the below-the-line region is for work that is designed and buildable and held by a named item or a date — and this item's own text says the opposite, that the git question *"is the whole of this item"* and its file list is provisional. Lifting it would have put an item that fails the keep check's second limb into the region /next builds from, where a run would halt on it as underspecified. Undesigned work belongs in Unprocessed, which is the queue's own four-state model applied rather than an exception invented for this item.

**Nothing designed here is lost, which is the reason this is a return rather than a deletion.** The two reasons, the repeal and what it must name, and the git question stated precisely enough to answer — all of it stays. A later planning session starts from a named question rather than from the beginning.

**What would settle it, and who owns each part.** Whether a build runs in its own worktree or both sessions share the tree with a single committer is a fact to establish by reading `session_start.py`'s existing worktree detection and testing both arrangements — Claude's to find. Whether the resulting arrangement is one you would actually work in is yours, since it changes how you use the tool rather than what it can do.

**Claude's decision, deferred to by you.** The alternative — leaving it held below the line — was refused because nothing was holding it: an item sitting in the held region with no blocker is reported as ready to lift at every opening, which is the false signal this whole disposition exists to remove.

Rule gate: not needed at processing — the repeal is decided here but its wording waits on the git question, so the rule text is authored when this is next processed rather than at the build.

#### Agreeing to something should file it, not produce a question about filing it [agreement-should-file-itself]
**Raised by you 2026-08-21, in your own words:** *"sometimes I agree to things Claude is saying because I don't want to have to remember them myself later so I just want them done. in reality it should capture them without offering/asking."*

**Why it is sharp rather than a preference about tone.** The reason you agree is to stop carrying the thing in your head. A question — *shall I file that?* — hands it straight back, and it does so at the exact moment the offload was supposed to happen. So the ask defeats the purpose it is attached to.

**What is genuinely undecided, and it is not whether you are right.** The method deliberately asks in several nearby places, each for a reason that survives this: an ask before a **delete** is terminal approval; an ask before a **send** is the never-send-unseen guarantee; the process-now offer exists so an idea is not parked without you. None of those is the moment described here. **The one being objected to is narrower: a thing already agreed, where the only open question is whether it gets written down.** Locating that moment precisely is the work.

**A live tension to settle rather than ignore.** [ask-before-writing-a-user-raised-capture] is cleared to run and moves the process-now offer to *before* the write, on your own estimate that you answer "process now" about nine times in ten. That is about **which** of two routes a capture takes. This is about whether the writing itself is worth a question at all. They are compatible on that reading and must be checked against each other rather than assumed to be — the two touch the same carve-out.

**And the general rule already points this way**, which is why this may be an enforcement gap rather than a new rule: the always-loaded routing rules say to route to artifacts rather than memory, and that nothing unrouted survives a chat. An agreement that produces a question instead of a capture is unrouted for as long as the question is open.

**To settle at processing.** Whether the moment is definable without swallowing the three legitimate asks above; whether this is a new clause or an application of route-to-artifacts that nothing enforces; and what the report looks like afterwards, since a capture filed silently still has to be visible enough that you can reject it.

**One thing observed today rather than argued.** Three separate items in this session existed only because a decision made in conversation had nowhere to live — [two-held-items-await-a-disposition] was filed for exactly that, and [advisory-step-does-not-fire] is the same failure inside the close. This is the same class seen from the user's side rather than Claude's.

**Files (rough):** `plugin/throughliner/docs/skill-nonspecific-rules.md` — the /plan carve-out in Communication, beside the clause [ask-before-writing-a-user-raised-capture] rewrites. Shipped, not host-only: every consumer agrees to things in conversation.

#### A build writes rules and can no longer see the disposition it is supposed to be transcribing [build-view-strips-the-gate-disposition]
**Raised by you 2026-08-21, from one question:** if `CLAUDE.md` is editable in a build, then that document can just be used to justify what was built. The confirmation below is Claude's, found by generating the build view and reading it.

**Your objection is the SPEC argument transferred, and it transfers cleanly.** A build may not write product truth because *one instance of Claude describing its own work in product truth is justification, not specification*. Rules are not product truth, but the shape of the risk is identical: the party that did the work writes the text that says the work was right.

**The defence on record is a decide-versus-type split.** `pre_tool_use.py`'s own comment states it: the gate runs at the keep-step and its output is a **disposition** on the queue item; the rule TEXT is written by the build that item schedules. What the gate refuses is a build deciding whether a rule may exist, never a build typing out a rule /plan already admitted. `CLAUDE.md` backs it with a hard instruction — *"A build that finds itself authoring a rule with no disposition to transcribe halts and says so."*

**That defence stopped being enforceable when the build view shipped on 2026-08-20, and this was not weighed.** The view was generated against this live queue and read: it carries `Changes:`, `Acceptance:`, `Red flag:` and `Refused:`, and **no `Rule gate:` line**. The disposition sits outside the `--- Build block ---` delimiters, in the item's rationale, which the view strips deliberately as decision history.

**Two consequences, and the second is a live contradiction rather than a weakness.**

- A build cannot read the disposition it is transcribing, so "transcribes rather than decides" is unverifiable from inside the build — the exact thing the split was asserting.
- By the letter of the halt instruction, **every** rule-authoring build must halt, because there is never a disposition present to transcribe. Either the instruction is dead text or every such build stops. Neither was intended.

**The failure has an instance predating the view, which is why this is not speculative.** [build-wrote-its-own-gate-disposition] records a build in the eighteen-item run finding itself authoring a shipped rule and, rather than halting, running the gate's four questions itself and recording the result — a description of an admission decision written by the party that had already done the work. That is your objection, observed, before the view made the disposition unreachable.

**The likely fix has a precedent inside the same block.** `Refused:` is already carried into the view for exactly this reason: a build that cannot see why an option was rejected proposes it again and stops to ask. A disposition is the same class of thing — the minimum history a build needs in order not to re-decide something. Carrying `Rule gate:` into the view would make the transcriber claim true for the first time since the split was written.

**To settle at processing, and the alternatives are not equivalent.** Whether the disposition moves inside the block delimiters or the generator learns to pull it from the item's prose — the first changes an authoring convention every existing item already follows, the second changes only the script. Whether the halt instruction survives unchanged once a build can see the line. And whether anything should verify that the rule a build typed matches the rule the disposition admitted, which nothing does today and which may be undetectable.

**What must not be reached for, stated because it is the intuitive move.** Barring a build from `CLAUDE.md` the way SPEC bars one leaves nowhere for rule text to be written at all — planning is barred from that file by the same lock, and the two bars together would make the method's rules unwritable. The asymmetry is deliberate; what is missing is the evidence travelling with the work, not the permission.

**Superseded in part, 2026-08-21, by your proposal in the same exchange: /plan should be the session that writes `CLAUDE.md`.** The paragraph above assumes both bars stay in place and concludes that the rules would become unwritable. Your proposal removes that premise by lifting the planning bar rather than adding a build one, so the conclusion does not reach it. What the paragraph still rules out is barring the build *alone*, which is untouched and stays refused.

**The prior refusal is cited rather than treated as settling this, because it answered a different objection.** `LOG/2026-08-17-scope-lock-denies-claude-md-2.md` (`7e3c1c8`) refused a permission change and recorded the exclusion as intended. The objection it met was that the gate's only-plan-can-refuse design forces a planning session to queue as a build the text it just admitted; the answer was that deciding is not writing, evidenced by fifteen rule changes dispositioned at a keep-step with nothing blocked. **That answer assumes the build faithfully types what planning admitted — which is the assumption this item shows has failed**, since the disposition no longer travels into the view the build reads. So the refusal rests on a premise that has since gone.

**Two arguments for your proposal, the second of which appears nowhere in the record.** A build that writes rules is the party that did the work writing the text saying the work was right, which is the SPEC-symmetry argument this whole item is about. And **/plan is the session the user is in**: a rule the user is meant to read and approve would be written where she can see the words, where today the wording of every method rule is produced in a run that is unattended in practice.

**Two costs, and the first is the user's own objection from elsewhere in this queue.** [plan-does-not-build-keeps-being-relitigated] records her words — *"I don't know why this is even a question. Plan does not build."* Letting /plan write rule text moves that boundary, and she filed an item because it keeps being moved. A candidate answer is that writing a document is not building, since /plan already writes SPEC, but that is exactly what needs settling rather than assuming. The second cost is load: a planning session admitting fifteen rules would then write fifteen rules, on top of already being the heavy session.

**Deliberately not decided here.** It changes who authors the method's rules, it was raised at the end of a long session, and the honest sequencing is that it is settled together with the disposition-in-the-view question above rather than ahead of it — the two are the same subject approached from opposite ends.

**One thing observed in passing and not folded in.** `BUILD-VIEW.md` is neither tracked nor gitignored, so every run leaves an untracked file at the repository root. Not this item's subject; noted so it is not lost.

**Files (rough):** `plugin/throughliner/scripts/generate_build_view.py`, `plugin/throughliner/docs/plan.md` (the build block's field list at the keep-step), `CLAUDE.md` (the halt instruction, host-only), and `resources/testing/`. Shipped in effect: a consumer's build reads the same view, though only this project authors method rules.

Relates to [build-wrote-its-own-gate-disposition] (the instance), [rule-admission-has-no-independent-approver] (the same question one layer out — who checks the party that decided), and [split-the-cleared-region-for-concurrent-sessions] (the build view this is a consequence of).

#### The close announces freeform work and never hands over the words to start it [freeform-close-gives-no-opening-prompt]
**Raised by you 2026-08-21, immediately after the close that should have covered it.** Your framing, and it carries the design: freeform users need an opening prompt every time freeform is the next thing to run — and because freeform has to run without a skill having been invoked, it needs a fresh chat, so the only place that prompt can be handed over is the end of the session before it.

**The step already exists and did its job.** `done.md`'s "Announce a `[freeform]` item if Processed holds one" says /next will not build it, that a close recommending /next without saying so sends the user into a stop, and to say plainly that it needs a session where the work is done by hand rather than run from the queue. That is what happened here. It named the item, said it was freeform, said /next would not reach it, and explained why.

**And you still had to ask how to take it.** Your question, verbatim: *"how would I imagine that I TAKE that next freeform session — do I just open a new session without running plan, and then instruct Claude to take the next thing from the top of the queue and build it?"* Two of the three guesses in it are wrong — the item is at the end of the cleared region rather than the top of the queue, and "build it" is /next's verb for a route that cannot reach it.

**So the gap is between describing a situation and being able to act in it**, which is the same distance this method already closes everywhere else it appears. A `[user]` line must carry a walkthrough naming the thing to click and the thing to look for, because a description of what needs doing is not an instruction for doing it. A freeform hand-off is the identical shape — a session the user has to start, from nothing, with no skill to guide them — and it is the one hand-off that ships no words.

**Why the prompt has to come from the close and can come from nowhere else.** Freeform work runs in a chat where no skill has been invoked, so there is no procedure doc loaded to explain itself, and the queue item is not read until someone tells Claude to read it. The session that ends is the last moment anything can put the words in front of the user.

**What it should carry, from what actually worked here:** the slug, the flavour, and where the recipe lives — enough that a fresh chat needs nothing else. Rendered as a paste target under the existing render rules, since its exact characters are the substance.

**One thing to settle at processing.** Whether this is the freeform announce step alone, or whether the same gap exists wherever the close hands work to a session it cannot start — a `[user]` item the user will do between sessions is the obvious neighbour, and it already carries a walkthrough, which may be why it does not have this problem. Check before widening.

**This is the second instance today of a shipped step firing correctly and still leaving you stuck** — [advisory-step-does-not-fire] is the other, where the recommendation was made and never written down. Both are the same class: the step describes and does not deliver. Worth reading together rather than separately.

**Two additions from running it, 2026-08-21, and the first is tested rather than designed.** The prompt this close actually handed over was used, and you amended it before pasting: *"the freeform item at the end of the cleared region **in QUEUE**"*. Your stated reason — that Claude does not know about QUEUE at session start — is wrong and the edit is right anyway, which is worth recording because the correct reason is what the fix has to encode. `session_start` does report the file (`QUEUE.md: found`) and its dependency facts, so Claude knows a queue exists and what shape it is in; what it has not got is the **contents**. So "the cleared region" names nothing until the file is opened, and the prompt has to say which file to open rather than assume the term resolves. **A prompt this item ships must be tested the way this one was — by being pasted into a blank chat — rather than judged readable in the session that wrote it.**

**Second, the prompt says the session ends with /done, and this half is weaker evidence — marked as such rather than carried on the strong half's back.** The run did ask for /done at the end, so the behaviour worked and your own reading was that it therefore does not matter much. It earns its place on one case: a session interrupted, or walked away from before it finishes, never reaches the step that asks, and a user who never knew a close was owed has no reason to come back to it. Cheap to include, and it is what makes an abandoned freeform session recoverable.

**One thing settled in passing, because it was asked and the answer is not obvious from the docs.** Every `[freeform]` queue item implies a session of its own, and not every freeform session comes from an item — most freeform work never passes through /plan at all and reaches the close as ordinary hand edits. The tag's job is telling the close what it is looking at, so the item-to-session direction holds and the reverse does not.

**Files (rough):** `plugin/throughliner/docs/done.md` — the freeform announce step. Possibly `templates/faq-template.md` with `FAQ/faq.md` and both index lines, since what the user *does* changes: today they work out how to start the session, and after this they paste a line. Shipped, not host-only: every consumer with a freeform item meets the same blank chat.

Filed after this chat's close, in the post-commit tail, so it belongs to no committed session record until the next close picks it up.

#### SPEC owes a sentence: the close now records whether it filed a forward recommendation [spec-silent-on-advisory-disposition]

[advisory-step-does-not-fire] shipped a required disposition line in every session
record — `Advisory: filed — <slug>` or `Advisory: not needed — <why>` — and a close
cannot complete without it. That line appears in the user's own session records, so
it is user-visible behaviour and belongs in product truth.

SPEC's forward-recommendation advisory paragraph describes the note being filed at
a close and consumed at the next planning session's opening. It says nothing about
the disposition, and nothing about the close being unable to complete until the
line is written. The sentence SPEC owes, roughly:

> The close records whether it filed that note or judged one unnecessary, as an
> explicit line in the session record, and cannot complete until it has — because
> a step that produces no artifact when it is skipped is indistinguishable from
> one that ran and found nothing to file, which is how it came to fire about half
> the time.

A build never writes product truth, so this is filed rather than written. SPEC lags
this one sentence until the next planning session.

Filed during the /next run of 2026-08-21; commit at filing time is the tip of main
at `461c999`.

#### A build read queue items through a grep window shorter than the items, and reasoned from the truncated read twice [build-reads-item-through-a-truncated-window]

The 2026-08-21 run had to transcribe each built item's `Rule gate:` disposition, which
the build view does not carry (see [build-view-strips-the-gate-disposition]). It went
to QUEUE.md for them and read each item through a `sed`/`grep` window of about 36
lines. All three items run past 50. Both the labelled `Rule gate:` line and the
item's FAQ disposition sit below where the window stopped.

**Two wrong outputs came out of that one read, and neither announced itself.**

First, a capture was filed asserting that [advisory-step-does-not-fire] carried its
gate reasoning as unlabelled prose with no `Rule gate:` line. The item carries a
properly labelled line. That capture was deleted at the close on the same day it was
filed.

Second — and this is the one that reached the user — the close concluded the FAQ gate
fired on that item, put the question to her, and got approval to add four FAQ files
and write an entry. The item had already dispositioned it: *"**No FAQ entry**, on the
FAQ trigger's own test: a consumer sees one more line in their session record and does
nothing different."* Planning had considered the identical question and answered it
the other way. The entry was written, then reverted on her instruction once the
recorded decision was found.

**The rule that would have caught it is already shipped and was not followed.**
`skill-nonspecific-rules.md`: page the whole file before any queue-wide reasoning, and
name a read that stopped short rather than reasoning from it quietly — with the reason
stated in the rule itself, that a truncated read looks like a complete one to whatever
reasons over it. That is exactly what happened, and it is why nothing downstream
flagged either error.

**So this is a rule-does-not-fire instance, not a missing rule**, and it joins the
class this corpus already tracks — the provenance rule, the file-the-blocker rule, the
INBOX-opening step, the subagent-cost rule, the gate's own halt instruction, and the
advisory step this very run was built to fix. The corpus's recorded conclusion about
that class applies: stating the rule again, or harder, is not a candidate direction.

**What is arguably new here is the shape of the trigger.** The paging rule reads as
being about *whole-file* reasoning — the queue digest, a queue-wide reorder — and a
build fetching one item's disposition does not feel like queue-wide reasoning. It is
still reasoning over a unit read short. Whether that is a wording gap in the rule or
simply an instance of it is the question for the keep-step.

**Two candidate directions, neither designed:** the build view could carry the gate
disposition and the FAQ disposition, which removes the need to read QUEUE.md at all
and is what [build-view-strips-the-gate-disposition] already proposes for half of it;
or the close's fetch could be specified as read-the-whole-item-block, keyed on the
`####` heading and the next one, rather than left to a hand-written window.

**A third thing this exposes, worth stating separately: a close overrode a recorded
disposition and the user could not have known.** She was asked a well-formed question
and answered it. Nothing in the ask told her a decision already existed, because the
session asking had not read it. Whatever else changes, an ask that re-opens a
dispositioned question should say that it is doing so.

Filed at the close of 2026-08-21; commit at filing time is the tip of main at
`461c999`.

#### A cleared item's refusal describes a mechanism this run changed underneath it [plan-entry-split-refusal-describes-old-mechanism]

[plan-entry-split-wording-disagrees] sits cleared to run. Twice in its prose, and once
inside its build block's `Refused:` line, it states that `queue_digest.py`'s
`shipped_slugs()` "resolves shipped-ness from **filenames** — `<date>-<slug>.md`, one
directory listing". That stopped being true at [log-entry-kind-not-distinguished],
built in the same run: the function now opens each entry and classifies it built,
processed or unknown by reading the body.

**The refusal's conclusion is untouched, which is why this is a flag and not a
blocker.** Its argument is that a decision settling three items produces one file named
for one of them, so the other two read as never shipped. That still holds exactly —
the change was to how a record's *kind* is read, not to whether a record exists. A
build reading the `Refused:` line will correctly decline to re-propose "per decision".

**What is wrong is the supporting description**, and it is wrong in a way that matters
to a reader rather than to a build: someone checking the refusal against the code would
find the code doing something else and have to work out for themselves whether the
refusal survived. It does. Saying so is a one-sentence edit to reasoning, which is
planning work rather than something a close should rewrite.

Found by this run's own staleness sweep, on the mover's citation notice after
[split-action-defeats-the-bands-in-aggregate] was removed.

Filed at the close of 2026-08-21; commit at filing time is the tip of main at
`461c999`.

#### The advisory step has no branch for a spent advisory already sitting in the slot [advisory-step-collides-with-a-spent-note]

`done.md`'s forward-recommendation step says to file the advisory as a capture at the
top of Unprocessed, under the reserved literal slug `[forward-advisory]`. It also says,
correctly and for good reasons, that clearing a spent advisory is the next /plan's job
at the moment it reads it — *"Nothing about clearing it is this close's job."*

**Those two hold together only while a planning session runs between every pair of
closes.** When one build close follows another, the close arrives at its own advisory
step and finds the slot occupied by a note whose subject has already shipped. Filing
alongside it would put two entries under a slug that is reserved and must be unique —
which the queue lint flags and which stops the queue mover dead on the whole file.
Leaving it alone means this close's recommendation is not written down, which is the
exact failure [advisory-step-does-not-fire] was built to end.

**Met live at the close of 2026-08-21**, immediately after building that very item. The
close resolved it by deleting the spent note and filing its own in the freed slot, then
moving it to the top — three mover calls where the step describes one. That is a
reasonable resolution and it is not what any doc says to do.

**Two candidate directions, neither designed.** The step could gain an explicit branch:
where a spent advisory is present, replace it rather than appending, and say in the new
note that it replaced one. Or the clearing rule could be narrowed from "never the
close's job" to "never the close's job to clear one it is not replacing", which keeps
the reason the rule exists — a close should not consume advice aimed at a session that
has not happened — while letting a close reuse the slot it is about to write to.

**The reason the clearing rule is worded as it is should be preserved through either
fix.** Clearing at the read, rather than at the previous close, is what stopped a build
session passing between two planning sessions from leaving a consumed note behind. That
is a different problem from this one and the fix must not reintroduce it.

Filed at the close of 2026-08-21; commit at filing time is the tip of main at
`461c999`.

#### The work-cycle block explains the commands in sequence and never says who types them [work-cycle-block-omits-who-invokes]

**Raised by you 2026-08-21**, from watching two sessions in a row mishandle how the
commands relate to each other — *"I keep constantly having these interactions where
claude doesn't really know how the skills even play out."* The diagnosis below and the
proposed fix are Claude's.

**What the block does and does not carry.** `skill-nonspecific-rules.md`'s "The work
cycle" section is the only place the commands are described as a loop rather than one
at a time: the standing capture step, /plan, /next, /done, the fresh chat that follows,
and three return edges. It is thorough about *what each command does* and *how work
moves between them*. It never states that the user types them and Claude does not.

**That fact lives in the same file, about ninety lines away**, as one bullet under
Communication: *"The method's own skills are one of those cases — name the command and
hand it over, never attempt it."* A session reading the loop gets the sequence with no
connected sense that it is never the one driving.

**The fix is to move that bullet into the work cycle block**, not to write a second
statement of it. Relocation within one file, so no always-loaded slot is spent and
nothing is duplicated — which matters, because a near-identical second rule is exactly
what the near-duplicate check exists to catch. A candidate shape, matching the block's
existing `STANDING` label:

```
  WHO RUNS THESE — the user types every command. Claude names the one
     that fits and hands it over.
```

**A first draft of that line was refused by you at authoring time, and the refusal is
the useful part.** It read *"You never invoke any of these. The user types them."* —
a prohibition, which the wording rule bans on the ground that anything stated as what
not to do means the action was never specified. Correcting it to the positive form
above produced text nearly identical to the bullet already in the file, which is what
turned this from "add a line" into "move the existing one".

**Evidence, one instance observed directly and one reported.** The observed one is
Claude's own: at the close of 2026-08-21 Claude handed you a paste-ready starter prompt
for a build run with the slash command written into it three times, and the prompt
addressed a session already inside a run while being given to you to paste into one
that was not. Neither you nor the receiving session had a clear answer to who acted
next, and you said the result was *"really fucking confusing"*. That prompt also broke
the shipped rule about naming a command in words rather than as a slash string.

The reported one is that the receiving session *"didn't seem to understand how the
skills work"*. **Claude has not seen that session and is inferring that it shares the
same root, which may be wrong** — the fix below is designed against the observed
instance only, and the keep-step should weigh whether the reported one needs its own
item.

**What this does not claim.** Moving the bullet makes the who-invokes fact reachable at
the moment the sequence is read. It does not make it fire — this is the eighth recorded
instance in this corpus of a correctly worded rule with a stated site not firing, and
relocation is a better-siting move rather than an answer to that class.

Filed 2026-08-21 from a chat outside any skill; commit at filing time is `ae84933`.

#### You cannot name the parts of the method you want changed, so you cannot ask for changes to them [user-has-no-handle-on-the-methods-own-parts]

**Raised by you 2026-08-21, in your own words:** *"I have also lost control because I
don't know what the place were we explain this is called. I have some vague idea it's
in skill-nonspecific-behaviours but I wouldn't have a clude how to refer to it and
actually ask for improvements on it that yield better outcomes."*

**The near-miss is the evidence.** The file is `skill-nonspecific-rules.md` and the
section is "The work cycle". You were close enough to be clearly reaching for the right
thing and not close enough to name it — and naming it is what a request has to survive
in order to reach the right place.

**This is the cost side of a rule that is otherwise working.** The vocabulary rule
keeps internal terms out of what Claude says to you: procedure-doc filenames, step
numbers, tag names are translated or omitted. That is right for a consumer building an
app, who never needs them. It has a different effect here, where the method **is** the
product: the parts you most need to direct are the ones you are never told the names
of. This project is the unusual case the audience note in CLAUDE.md already describes,
and this is a consequence of it that nobody had written down.

**Two directions, and they are not exclusive.**

The first is Claude's side and costs you nothing: **a request that describes a behaviour
should be enough**, and Claude should locate the file. *"When you hand me a prompt to
paste, never put a command inside it"* is complete and actionable as it stands. Needing
a filename to make a request land is itself the defect. Whether anything needs writing
for that, or whether it already follows from rules in place, wants checking rather than
assuming.

The second is a **map you can hold** — one short list naming the parts and what each
governs, in your language rather than the corpus's: the always-loaded rules and what
kinds of behaviour live there, the one doc per command, this project's own CLAUDE.md,
SPEC. Where it lives is an open question. This project's CLAUDE.md is the obvious home
and is also already long; the FAQ is consumer-facing and this is not a consumer's
problem.

**Not designed, and deliberately so.** The right shape depends on which of the two
actually restores the control you lost, and that is your judgment rather than Claude's.

**One thing worth not losing:** you said you had lost control, not that you were
confused. Those are different complaints and the second is easier to answer than the
first. A fix that leaves you able to follow what Claude is doing but still unable to
direct it has answered the wrong one.

Filed 2026-08-21 from a chat outside any skill; commit at filing time is `ae84933`.

#### Claude surfaced the forward advisory and argued against it in the same message [advisory-surfaced-then-overridden]
Filed 2026-08-21 by Claude at its own close, from an instance it caused at this session's opening.

**What happened.** The opening narration surfaced the advisory correctly, first line, above the rule, exactly as `plan.md` specifies — it recommended a planning session before the next build run and named the two captures behind it. Within the same session Claude then recommended closing and running the build, having never checked whether the advisory's reasons still held. **The user caught it**, in her own words: *"The last session said to run plan though"*. Checking took one grep: one of the two reasons was dead, and the other — roughly forty open items naming a folder that no longer existed — was live and sat on the first two items of the run being recommended.

**Why the shipped step does not cover this.** `plan.md` requires the advisory to be surfaced and then deleted as spent, and says it is orientation rather than a command. Both were followed. What nothing requires is that the session **read the advisory's stated reasons against the current state** before recommending anything that contradicts it. Surfacing is a display obligation; nothing makes it an input.

**Why it is worth a line rather than a shrug.** The advisory mechanism exists because a recommendation made in one session otherwise dies with it — [advisory-step-does-not-fire] shipped a required disposition to guarantee the note gets written. This is the same failure one step later: the note was written, delivered, read aloud, and then ignored by the session reading it. A note that is surfaced and overridden in one message is worth no more than one never filed.

**To settle at processing.** Whether the advisory step gains a limb requiring its reasons to be checked before the session recommends a course that contradicts it, or whether this is one instance of the wider class this corpus now records eight times — a correctly worded rule with a stated site not firing. **Do not reach for stating it harder**, which the record says is no longer a candidate direction.

**Files (rough):** `plugin/throughliner/docs/plan.md` — the advisory step. Shipped: every consumer's planning session reads an advisory the same way.

#### The dispositions listing prints the full history where it claims to print one session's [dispositions-listing-window-not-bounded]
Filed 2026-08-21 by Claude at its own close, from running the listing at this session's opening.

**What was seen.** `py resources/rule_signals.py . --dispositions` printed a header reading "102 on record (since the last planning session)". `CLAUDE.md` states the bound: the listing is "bounded to entries since the most recent planning LOG entry", with `--dispositions-all` as the separate flag for the full history. Planning sessions here run most days, so 102 is not one session's worth.

**Why the bound matters rather than being cosmetic.** The window was tightened to "since the last planning session" deliberately, and the recorded reason is the user's own question — how would she even know to demand it. A listing short enough to read is what makes a refusal visible; a hundred entries is the same as none, and it goes quiet by itself only if the window works.

**Not diagnosed, deliberately.** The header may be mis-labelled, the window may be computed wrongly, or "the most recent planning LOG entry" may not be findable now that entries split per item. **Read the code before designing anything** — this capture carries an observation, not a claim about the cause.

**Files (rough):** `resources/rule_signals.py`. Host-only — the listing does not ship.

#### SPEC states 4.8-era results as current product truth, and only two were found by accident [spec-carries-4-8-era-claims]
Filed 2026-08-21 by Claude at its own close. **The finding is the user's**: told that rationale must ride a rule for the rule to be followed, she identified it as a 4.8-era claim. She was right, and the correction reached two sentences.

**What was corrected here.** SPEC's claim that rationale is what makes a rule get followed, and its claim that a brevity instruction was tried and measurably did nothing. Both were true of Opus 4.8 and are contradicted for the current target by this project's own research — `resources/research/opus-5-instruction-compliance.md` and `fable-5-instruction-compatibility.md`, both live and unsuperseded since 2026-07-31.

**Why the class is worth an item when two instances are already fixed.** The docset was re-authored by subtraction when 4.8 was retired, but SPEC was not audited against the model change — it describes the product, so nobody read it as carrying model-specific claims. The two found were found because a conversation happened to touch them. **The second one had a live cost**: it talked this project out of the one lever its own current-model research recommends, for a whole model generation.

**To settle at processing.** Whether this is an audit of SPEC against the two research files, or whether it folds into [claims-need-a-claude-code-delta-test], which already proposes auditing SPEC's claims against what Claude Code alone delivers — a different question over the same sentences, and one pass could serve both. **Weigh folding seriously**: two audits of one document, filed days apart, is the shape this project's near-duplicate check exists to catch.

**Files (rough):** `SPEC.md`. Relates to [claims-need-a-claude-code-delta-test] and to [brevity-instruction-for-the-5-series], which rests on the corrected claim.

#### The rationale lens covered done.md whole and plan.md only in part, so plan.md's acceptance test is unmet [rationale-lens-plan-md-coverage-incomplete]

[rationale-lens-after-the-build-view] required every paragraph of `done.md` and
`plan.md` to go through the delete-and-reread test, with each removal recorded
against its destination. The build on 2026-08-21 met that for `done.md` and did
not meet it for `plan.md`.

**What was actually done.** `done.md` was read end to end across four reads and
worked section by section, so every paragraph was seen and judged: 959 lines
down to 794, statement count 244 to 235. `plan.md` is 1,594 lines, and the pass
there worked from targeted identification — grepping for the signatures of
history paragraphs ("Why both", "recorded because", "was rejected", "used to",
"weighed and lost") and reading around each hit. Roughly 40% of the file was
read. Eight sites were reduced; 1,594 lines down to 1,549, statement count 318 to
322.

**Why the count ROSE while the file shrank**, recorded because it looks wrong: a
paragraph carrying an operative rule buried in prose was, in several places,
restated as a bold-led sentence. That is what the pass is supposed to do — an
operative rule belongs in a countable shape — but it means the statement count is
not a proxy for how much history came out. Line count is the better signal here.

**What is left.** The unread ~60% of `plan.md`, which is not a list anyone holds:
the identification was signature-based, so a rationale paragraph phrased without
one of those openings was never looked at. That is the same class of miss as
[law-prose-pass-missed-mid-sentence-prohibitions], found the same day, by the
same shortcut.

**What a build would need to settle.** Whether the remaining pass reads the file
straight through — the only method that can honestly claim the acceptance test —
or whether the acceptance test itself should be restated as something a build can
actually discharge and evidence. The second is worth weighing: "every paragraph
has been through the test" is unfalsifiable from the artifacts, since a paragraph
correctly judged operative and left alone looks identical to one never read.
That is the same defect the required-artifact rules elsewhere in this project
exist to fix, and it is arguably the more valuable half of this item.

#### The close's cost scales with run size and nothing bounds it — a 17-item run wrote 15,000 words into the record [close-cost-scales-with-run-size]

**Raised by you 2026-08-21**, immediately after the close of the seventeen-item run:
that was the longest close you had ever seen, at over 30k tokens. Filed after that
session's commit, so it belongs to no committed session record — the measurement below
is Claude's, taken with the instrument built earlier the same day.

**The measurement, and it points away from the obvious cause.** Chat output across that
whole session was **3,843 words in 49 messages, median 20 words when speaking** —
*below* the project's own baseline of 55, and far below /plan's 119. By the one thing
this project measures about talking, the session was not verbose.

**The cost was the record, not the talking.** The close wrote **19 LOG entries totalling
13,758 words**, median 722 per entry, range 486–1,124, plus **1,452 words of index
lines** across 26 lines. Roughly 15,200 words written into `LOG/` in one close.

**So the brevity amendment shipped that morning is not what is at fault, and neither is
any narration rule.** Those govern messages. The close's output is governed by
`done.md`'s entry-writing step and the authoring standard, which are a different lever
entirely. A fix aimed at narration would move none of this.

**The structural driver, stated plainly.** `done.md` holds that one entry per built item
is **unconditional**, however long the run. The readiness line bounds how much a run
*builds*; nothing bounds what the close then *writes*. So close cost is linear in run
size, and the queue's own throughput ambitions — clear more items per run — drive it
directly. The bigger the run, the worse the close, with no ceiling anywhere and no
session positioned to notice, because each entry looks reasonable on its own.

**The depth field exists for exactly this and did not work.** `next.md` requires a
`Depth: short` or `Depth: full` line per ticked item, written at the tick, precisely so
the close does not treat every item as worth telling at length. That run marked 13 short
and 4 full — and **the median "short" entry still ran about 700 words.** Nothing anywhere
defines what short *means* in output terms, so the field recorded a judgment and changed
nothing. That is the same defect this project has fixed twice elsewhere by requiring an
artifact rather than a self-assessment, and here the artifact exists and carries no
consequence.

**What a build would need to settle, which is why this is a capture.** Whether the fix is
(a) giving the depth field a definition with teeth, (b) letting a decision that settles
several items write one entry with siblings citing it — which
`[plan-entry-split-wording-disagrees]` just shipped for planning entries and which was
NOT applied to build entries, (c) bounding what the close writes rather than what the run
builds, or (d) accepting the cost and saying so. **Option (b) is the cheapest and is
already half-built**, and its absence on the build side may simply be an oversight rather
than a decision — that is the first thing to check.

**Do not reach for a word count.** Caps are retired here on measured grounds, and the
retirement is recorded in SPEC. The lever this project settled on is *where text lives*,
which is exactly what option (b) is.

**Relates to** `[plan-entry-split-wording-disagrees]` (shipped the sibling-citation
clause for planning entries), `[rationale-lens-plan-md-coverage-incomplete]` and
`[law-prose-pass-missed-mid-sentence-prohibitions]` (the same run's other captures), and
`[brevity-amendment-outcome]` (the held audit — which should be told that chat output was
already at median 20 in this session, so it must not read a close's size as evidence
about narration).

#### The rezip ritual names a verification but supplies no words for it, so Claude re-invents the prompt every time and got it wrong today [rezip-supplies-no-verification-prompt]

**Raised by you 2026-08-21**, immediately after a rezip: you are tired of having to get
Claude to redesign this prompt on every rezip, and want it supplied ready-made.

**The gap.** `resources/release-ritual.md` step 9 says to prove the hooks are alive by
asking a fresh session what the session-start hook actually reported to it, and explains
correctly why that step exists — a hook that is well-formed, installed and silently
dropped looks exactly like a working one from the source side, so only a session saying
what it received distinguishes them. **It supplies no prompt.** So the words are composed
fresh at every rezip, at the end of a long ritual, by whichever session is running.

**The failure is today's instance, observed end to end.** Claude told you to check what
the next session's opening line said. You relayed it as *"please tell me what its
session-start line says"*. The fresh session replied that it was not sure what "its"
pointed at — correctly, because it has no memory of the chat the instruction came from.
The verification did not happen, and the only reason it was not simply skipped is that
you came back and said so.

**Why the fresh-composition is the defect rather than that one wording.** This prompt has
an unusual authoring constraint: it is pasted into a session with **zero context**, so
every referring word has to resolve inside the prompt itself. A prompt composed by a
session that has been immersed in the work for hours is exactly the wrong author for that
— pronouns that are obvious here resolve to nothing there. The method already knows this
failure shape: it is the same reason `done.md` fixes the compaction caveat as a verbatim
sentence rather than an instruction to explain the limit honestly, and records that
inviting improvement is what went wrong.

**What a build would supply**, sketched from the version that worked today rather than
designed from scratch. A verbatim fenced block at step 9, plus two things around it:

- **Where to paste it** — any project in the state that reproduces the bug: **version
  marker stale, epoch current, nothing missing.** Name the state rather than a project.
  Claude's first attempt at this said "a project that was actually exhibiting the
  symptom, not this one", which was wrong twice over: it sent the user hunting for the
  right project when the dev project was already in the reproducing state, and a project
  picked that way may halt for a *legitimate* stale-epoch reason, which muddies the
  result rather than confirming anything.
- **How to read the answer** — which reply means the fix landed, which means a real and
  correct halt, and which means the app did not fully restart. Without that the report
  comes back and still needs interpreting.

The four questions the working version asked: quote the `[Throughliner]` block verbatim;
does it mention `/setup` and for which of the three reasons; does it tell you to stop or
close what is running; what version and build stamp does it report. Plus one instruction
that carries most of the value — **if the block did not arrive at all, say so plainly
rather than reconstructing it from the project's files**, which is the one answer that
distinguishes a delivered hook from a dropped one and is exactly what step 9 exists for.

**Host-only, and it goes in `resources/release-ritual.md`.** Consumers never rezip, so
this reaches no shipped doc.

**One thing to settle at processing.** Whether the block is fixed text that must be pasted
as written — the `done.md` compaction-caveat precedent, which exists because improving it
is what broke it — or a template a session may adapt per rezip. The failure recorded above
is an argument for the first, and the first is also cheaper.

**The prompt was then run and it worked, so a build starts from something proven rather
than from a sketch.** The reply came back as a straight paste of the whole
`[Throughliner]` block, and that single instruction — quote it verbatim — answered all
four questions on its own without the reader working through them one by one. So the
verbatim quote is the load-bearing part and the four questions are the fallback for a
session that paraphrases instead. **Design the block that way round.**

**What the run confirmed, recorded because it is also the worked example a build can put
in the ritual.** The dev project recorded `1.20.0-test13` against an installed
`1.20.0-test14`, with epoch 4 against a declared 4 and nothing missing — exactly the
state that produced the halt reported that morning. A fresh session opened in that state
and its block mentioned `/setup` nowhere. That is what a passing result looks like, and
it is worth showing rather than describing.

**One piece of expected noise the ritual should warn about**, or the next reader files it
as a finding: the returned block carries the INBOX line flagging `INBOX/sent.md`, which
is the outbound register rather than waiting mail. Already known as
`[sent-record-surfaced-as-waiting-mail]`. A verification step that returns a block
containing a known false positive needs to say so, or it manufactures work.

**Relates to** `[close-cost-scales-with-run-size]`,
`[law-prose-pass-missed-mid-sentence-prohibitions]` and
`[rationale-lens-plan-md-coverage-incomplete]`, all filed the same day. All four are the
same family: **a step that names a check and leaves its artifact unspecified**, so
whether it was really performed cannot be told afterwards. That family is worth processing
together rather than four separate repairs.

#### Heading word-order rule did not fire on a fresh capture, and the user could not find it in her outline [heading-rule-did-not-fire-on-a-fresh-capture]

Filed 2026-08-21 by Claude at its own close, from an instance minutes earlier.

A capture was filed with the heading "The brevity work went to narration…" into
an outline where eleven consecutive headings already began with "The". The user
scrolled the outline, could not find it, and had to ask for it by name. The
shipped rule — put a heading's distinguishing words first, because the outline
truncates mid-phrase — is always-loaded, was in context, and did not fire; the
heading was corrected only after the user reported the failure.

Joins the class this corpus records as correctly-worded rules with a stated site
not firing (ninth instance). Per that record, stating it harder is not a
candidate direction. What may be mechanical here where the others are not: a
heading's first word is text a lint can read, and "starts with The/A/An" is
checkable at zero judgment — though that catches only the article case, not a
generically front-loaded heading, and the limit would need stating wherever it
reports.

**Files (rough):** `plugin/throughliner/hooks/post_tool_use.py` and
`resources/testing/` if the lint arm is taken; nothing if judged below the bar —
one instance, which the gate treats as insufficient for a rule, though this
would be a lint check rather than a rule.

#### The autonomous keep-step kept two rule-amending items without writing the gate disposition, and the next build halted on it [keep-step-skipped-gate-disposition]
Filed 2026-08-21 by Claude, on the user's report of the halt. The 2026-08-21 autonomous planning run kept [cut-length-everywhere] and [sent-record-surfaced-as-waiting-mail] — both amend the method's own rules — and wrote no `Rule gate:` line on either. The following /next run halted before locking scope, correctly, and the user had to intervene: the gate was then run in conversation and the two dispositions written onto the items. The halt worked; the keep-step did not. The question a /plan should weigh: whether the keep-step's gate obligation needs a mechanical backstop for autonomous runs — e.g. the disposition-presence check running at the plan close over items kept that session, not only at rule-bearing commits — or sharper wording at the keep-step itself. Relates to [rule-gate-dispositions-missing] (the check's hash timing) and [build-view-strips-the-gate-disposition] (the view not carrying the line).

#### Length cut: thirteen procedure docs and CLAUDE.md still uncut [cut-length-remaining-docs]

Filed 2026-08-21 by Claude, mid-run, on your instruction to capture the remainder and carry on.

**What [cut-length-everywhere] actually covered.** The repeal landed in full: SPEC no longer says written shapes are uncapped, and both SPEC and `skill-nonspecific-rules.md` now bound every written shape by the median of that shape in the project's own measured distribution, printed by `measure_written_shape_length.py`. A median is a proportion of the corpus rather than an invented figure, so it satisfies the stated-derivation requirement, and it ratchets — writing to it pulls it down. `plan.md` was cut from 1,565 lines to 1,315.

**What is left.** The same treatment across `skill-nonspecific-rules.md` (1,230 lines), `done.md` (794), `next.md` (692), `setup.md` (640), `next-build.md` (416), `CLAUDE.md` (379), `done-plan.md` (366), `feedback-and-inbox.md` (274), `migrate-checklist.md` (199), `done-build.md` (195), `rescan.md` (145), `recovery.md` (126), `next-audit.md` (98), and the remainder of `plan.md`.

**Why it stopped.** The run halted and reported that one build session does not have room to cut fifteen files while reading everything it deletes — and reading everything it deletes is what the acceptance test requires, since no operative rule may be lost. Your call was to capture the rest and move on.

**The method that worked, so the next session does not re-derive it.** Cut by deleting decision history, not by rewriting rules: every bullet, every bold-led rule statement and every typed block stays, and what comes out is the plain-prose paragraphs explaining why. Where a bold-led paragraph is itself pure explanation, absorb its one operative clause into the rule above it and delete the rest — and name each of those in the session record, because `rule_signals.py` counts bold-led paragraphs as rule statements and will otherwise report an unexplained fall. Nine came out of `plan.md` on that basis (328 statements to 319).

**This is probably `[freeform]` rather than a build.** It is large, it is one file at a time, and it is the work most likely to lose a rule if run unattended — which is the freeform test rather than a size complaint.

Relates to [law-prose-pass-missed-mid-sentence-prohibitions], which reads the same fourteen docs for a different defect, and to [keep-step-accretes-from-five-items].

#### Law-prose restyle: thirteen docs still unread for mid-sentence prohibitions [law-prose-remaining-thirteen-docs]

Filed 2026-08-21 by Claude, mid-run, at the file boundary the parent item told the pass to stop at.

**What [law-prose-pass-missed-mid-sentence-prohibitions] covered.** `plan.md` only. 68 occurrences of "don't", "do not" and "never" were found by re-count — the ~150 figure in the retired item's prose was taken before the restyle passes rewrote this text, and 298 is the corpus-wide total. 45 were restyled into the action the rule requires; 23 were left as protected kinds and are itemised with their line numbers in that session's record.

**What is left, with today's counts.** next.md (52), skill-nonspecific-rules.md (47), setup.md (28), done.md (23), feedback-and-inbox.md (21), done-plan.md (18), next-build.md (17), migrate-checklist.md (7), done-build.md (7), rescan.md (5), recovery.md (3), next-audit.md (2). done-audit.md has none and needs no pass.

**The three protected kinds are unchanged** and are the reason a grep cannot do this: a typed-block `write:`/`never:` contrast pair, an honest-limit statement, and prose describing what a mechanism does not cover. Deciding which of the three an occurrence is takes reading the provision around it, which is why the parent item refused gathering the remainder by grepping for the protected shapes and restyling whatever was left.

**What the plan.md pass learned, so the next session starts further along.** Most occurrences are of the form "X, never Y" where X already states the action — there the tail is redundant and comes straight out, which restyles and shortens in one move. The ones that need real rewriting are the few where the prohibition carries the only content: "never build", "a build never writes product truth", "never keep a mixed item by papering over the failing limb". Those become the positive rule they imply.

Relates to [cut-length-remaining-docs], which reads the same thirteen files for length — worth running the two together, since both passes read every provision in the file.

#### A slug built earlier in the same run is in neither the queue nor the log, so the filing-claim hook can still fire on it [stop-hook-blind-between-tick-and-close]

Filed 2026-08-21 by Claude, noticed while building [stop-hook-fires-on-cited-slugs] and testing the fix against this project's own state.

**The gap.** That item's fix suppresses the block where a slug absent from QUEUE.md has a session record in `LOG/`, on the reasoning that a record means the slug names shipped work rather than a failed filing. It closes the case it was filed for — citing work built in an earlier session.

**What it does not reach is the same run's own work.** A build removes each item from QUEUE.md at the moment it is ticked, and its LOG entry is not written until the close. Between those two events the slug is in neither file, so a message citing an item this run has just built looks exactly like a report of a write that never happened. Confirmed live: at the moment of writing, [cut-length-everywhere] had been ticked and removed and had no LOG entry, so a citation of it would still have blocked.

**Why it is not urgent.** The block downgrades after one fire per claim, so it cannot trap a chat, and the run's own narration names built items constantly without the hook seeing most of them. It is a false block in the one window where the session is most confident it is right.

**What would close it, undesigned.** The build working file already carries a Progress tick per built item, and it is per-session and readable from the hook's cwd. Reading ticked slugs out of it would cover the window exactly. Whether a hook should read that file at all is the open question — nothing else does, and it is deleted at the close.

Relates to [stop-hook-fires-on-cited-slugs], whose fix this extends, and to [changes-section-falls-behind-the-ticks], which is about the same file's reliability.

#### The shell-write guard sees neither the target nor the computation when a write's path is built by a call [shell-guard-blind-to-call-built-paths]

Filed 2026-08-21 by Claude, found while reproducing [shell-write-guard-blocks-the-scratchpad].

**The hole.** `open(os.path.join(d, 'x.md'), 'w').write(...)` passes the guard entirely. `structured_write_targets` returns nothing, so there is no target to check, and `has_computed_write_target` returns False, so it is not denied as unreadable either. The command runs.

**Why both halves miss it.** `PY_OPEN_WRITE_ANY` matches `open(` followed by `[^,()]+?` up to the mode argument. A path built by a call contains both a comma and parentheses, so the pattern does not match at all — and the computed check only fires on arguments it matched. The result is a shape that is neither literal nor computed as far as this code is concerned.

**Why it matters.** This is the exact failure the guard was written for. Its own docstring records that "a computed target slipped past an earlier version of this check and silently corrupted QUEUE.md, and the only difference from the version that was correctly blocked was one variable assignment." `open(p, 'w')` with a bare variable is correctly denied today; wrapping the same path in `os.path.join(...)` is not.

**Verified, not inferred.** Driven directly against the target hook: `targets=[] computed=False` for the join form, against `targets=[] computed=True` for the bare-variable form.

**Not fixed in that item's build,** because its described work was the disagreement between the guard and its own message — a raw-string literal being read as computed — and this is a different defect in a different function. Widening `PY_OPEN_WRITE_ANY` to tolerate nested calls needs its own design: the obvious `.+?` risks matching across unrelated arguments, which is the fragile general-parsing this module deliberately rejects.

Relates to [shell-write-guard-blocks-the-scratchpad], whose reproduction found it.

#### An item whose described work is queue CONTENT can be cleared but never built, and nothing at the keep-step catches it [queue-content-items-are-unbuildable-by-a-run]

Filed 2026-08-21 by Claude, from a build run that met one.

**What happened.** [cut-length-everywhere] listed QUEUE.md among its files — "every item cut to its build block plus a short rationale". The scope-lock refuses a build any direct Edit or Write on QUEUE.md, by design: a build reads the generated view, and the only queue writes a run makes are the mover's per-item removal and an appended capture. So that limb of the item was unbuildable from the moment it cleared, and nothing said so until the run was already scope-locked. [lint-flags-its-own-scaffolding] had the same shape in its local half.

**Why the keep-step misses it.** The two-limb buildability check asks whether the item names its files and says what changes inside them. Both items passed: the files were named and the changes were described. The limb that does not exist is whether the named files are ones a build is *permitted* to write.

**The mechanical form, which is what makes this cheap.** The scope-lock's own refusal list is short and known — QUEUE.md is the only project doc a build cannot edit at all. An item naming QUEUE.md in its Files line is either a queue-content rewrite, which is planning work, or a mistake. Either way it should not clear to run.

**Worth checking whether the answer is a keep-step limb or a lint rule.** The queue lint already parses each item's build block, so a cleared item naming QUEUE.md could be flagged with no judgment at all — which would fire before a run ever locks scope. That is the cheaper site if it works.

**Not urgent.** The failure is visible and recoverable: the run halted, said so, and the user redirected. Nothing was silently skipped.

Relates to [cut-length-remaining-docs], whose remaining work includes the same queue limb, and to [keep-step-accretes-from-five-items] — which is a reason to weigh this against the keep-step's existing load rather than adding a sixth clause without looking.

