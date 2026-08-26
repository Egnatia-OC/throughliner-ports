# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Walkthroughs are silently dropped from the build view unless the heading is exactly `Walkthrough:` [build-view-walkthrough-heading-mismatch]
From a consumer project's report, read and archived at this session's opening on 2026-08-26 (`INBOX/archive/2026-08-26-from-afk-cats-walkthrough-heading-not-matched.md`). A `[user]` item there carried a full seven-step walkthrough, written and approved at planning; a /next run reached it, reported it carried no walkthrough, and halted. Two further sessions were spent on steps that were never missing.

The cause, reproduced on their side: `generate_build_view.py` matches a walkthrough heading with `^\s*\*{0,2}Walkthrough[.:]` — the label must be immediately followed by a full stop or colon. Their item headed the steps `Walkthrough — part one:` and `Walkthrough — part two:`, so neither block matched and both were dropped. Rewriting to a single `Walkthrough:` made all seven steps travel, verified against the generator.

Why it cost two sessions: the failure is silent everywhere a human looks. The queue shows a complete walkthrough, the digest reports nothing, and the run's message blames the item for missing content the item visibly has.

Kept 2026-08-26, cleared to run ahead of today's beta release ([expedite-first-beta-release]). The mechanism was read before designing: the label match at `generate_build_view.py` line 193 requires punctuation immediately after the word, and the copy runs from the label line to the entry's end — so widening the match to a word boundary carries their two-part shape whole with no other change. The fix sits at the mechanism rather than as an authoring rule in plan.md, because code that accepts the shape leaves such a rule policing nothing.

--- Build block ---
Changes: `plugin/throughliner/scripts/generate_build_view.py` — widen the walkthrough-label match so `Walkthrough` followed by a qualifier before its colon (e.g. `Walkthrough — part one:`) matches, keeping the bold-tolerant form; and where no label matches but a line beginning with the word exists, the no-walkthrough message says the label did not match rather than that no walkthrough exists.
Acceptance: the generator run against a queue copy using `Walkthrough — part one:` / `Walkthrough — part two:` yields all steps; a plain `Walkthrough:` item is unchanged; an item with no walkthrough at all still gets the halt message.
Refused: a keep-step label check in plan.md — the widened match accepts the shape, so a rule guarding it would police a handled case.
--- End build block ---

#### Planning runs on Fable, builds run on Opus 5 — write the split into the fresh-sessions rule [planning-fable-building-opus-note]
Raised by you 2026-08-26, processed the same turn. Your reasoning: the note is needed so Fable knows anything Opus might have to infer must be included in every build block, and so Fable knows it is in charge of every decision — captures made during a build are weighed knowing that session had less full-project oversight than the planning session reading them. Amends CLAUDE.md's "Design for fresh, short sessions" rule, which already names the weaker post-Fable model as the design target; this makes the current split explicit rather than implied.

Rule gate: run — amendment to the fresh-short-sessions rule, its named parent; subordinate to it, no freestanding slot spent, nothing evicted.

--- Build block ---
Changes: `CLAUDE.md` — extend the "Design for fresh, short sessions" rule with the split: planning sessions run on Fable, build sessions run on Opus 5; a build block therefore includes everything the build model would otherwise have to infer, and a capture filed from a build session is weighed at processing as coming from a session with less full-project oversight than the planning session reading it.
Acceptance: the rule reads as one amended provision (no second freestanding rule), and the sentences state actions — what to include in a block, how to weigh a build's captures — rather than a description of the models.
--- End build block ---

#### Cycles due-ness check fires at neither site: the /plan opening failed live, as the close did [cycles-check-fires-nowhere]
Found on 2026-08-25 while walking [cycles-due-check-verification], which existed to run exactly this diagnostic. Both live tests of the feature have now failed, on the same installed plugin.

The demo project carries a well-formed `CYCLES.md` at its root with one definition, `[weekly-listen]`, whose observable is the newest date in its turn record — 2026-08-10, a fixture written deliberately on 2026-08-24 so the cycle would read as due immediately. On 2026-08-25 a /plan opening ran there with that file on disk. Its opening narration named the advisory, a lift, a throughput floor, four waiting captures and the droppable skim, and said nothing about any cycle; no item under the cycle's slug appeared in that project's Unprocessed. The check is sited in plan.md's Step 1 and is [BRIEF] when it files, so a fired check would have been visible in exactly that message.

The close site failed the same way on 2026-08-24, with the same file on disk, recorded in `LOG/2026-08-24-cycles-due-check-verification.md` and filed as [cycles-close-check-did-not-fire]. That item is now built. Its premise was that a close could carry a stale belief from its own opening about whether a cycles doc existed — a real defect, but it cannot explain a fresh opening in a new session missing the file entirely.

Settled at processing 2026-08-26, without the transcripts: a grep across the plugin shows the check exists only as doc steps at three sites (plan.md's opening, next.md's pre-flight, done.md's wind-down), each tagged silent when nothing is due, with `session_start.py` never mentioning CYCLES.md — so a fresh opening's payload says nothing about the file, and a step that leaves no artifact when clean is indistinguishable from one that never ran. Both live failures fit that shape. The fix gives the check a mechanical trigger and a visible run: the hook emits facts, the doc steps narrate. If the true cause was instead a wrong computation, the brief-always narration exposes it on the next live run. Once shipped and rezipped, [cycles-due-check-verification]'s walkthrough can pass and the beta chain lifts through its existing wiring. The demo project's fixture stays in place — it is the ready test case for that verification.

Rule gate: run — amendments to the existing cycles-check steps, their named parent, across the three docs; the silent-when-clean arm for doc-present projects is evicted, replaced by one brief line naming each cycle due or not. No freestanding rule added.

--- Build block ---
Changes: `plugin/throughliner/hooks/session_start.py` — where `CYCLES.md` exists at the project root, emit a cycles fact line naming the doc, each definition's slug, and the observable as read (its last-turn date where it is a date); facts, never verdicts, same register as the queue dependency facts. `plugin/throughliner/docs/plan.md`, `next.md`, `done.md` — the cycles due-ness step at each site keys on the doc's presence and, where the doc exists, is [BRIEF] always: one line naming each cycle as due or not, filing stays as shipped; where no doc exists, silent and unchanged. Update the session_start suite under `resources/testing/` for the new line.
Acceptance: driving `session_start.py` directly over a fixture folder carrying a demo-shaped `CYCLES.md` (past-due observable) prints the cycles line; a fixture with no doc prints nothing; the three doc steps name the hook's line as their trigger; the suites pass at the close.
Refused: diagnosing from the four consumer transcripts before fixing — the structural gap (no trigger, no artifact) is established by the grep alone, and the transcripts item remains for confirmation.
--- End build block ---

#### Install-pathway review before the beta: three fixes proposed for README and INSTALL.md, one already applied outside the repo [install-pathway-review-for-beta]
Raised by you on 2026-08-26, from testing the install pathways in a browser chat ahead of tomorrow's beta. The report is at `C:\Users\Alex 2\Downloads\install-process-report.md` and is Claude-authored rather than yours, so its claims are treated as unverified until checked — some are checked below, and the rest are not.

**What was verified here.** `INSTALL.md` exists, runs 137 lines, and does carry the "Instructions for Claude" section the report praises, with a pointer to it at the top. `README.md` line 17 already gives the raw INSTALL.md URL and already says to ask Claude to guide you through setup. So of the three proposals, the wording one is nearly satisfied already — the gap between "ask Claude to guide you through setup" and "ask Claude to read this guide" is small, and whether it is worth closing is a judgment rather than a fix.

**What the report proposes, all low priority by its own account.** Make the "New to Claude Code?" path more visually distinct in the README, since it is third of three and is the one most beta users need. Reword the link line so it asks Claude to *read* the guide, on the reasoning that a browser Claude does not always fetch a URL unprompted and may answer from general knowledge instead — losing the guide's pacing rules entirely. And, marked future rather than now, give INSTALL.md a verification phrase Claude is told to say once it has loaded the guide, so the user can tell whether it was read or improvised.

**The unverified claim worth knowing about.** The report says the Discord how-to post was changed to point at the raw INSTALL.md URL rather than the repository root, and describes that as shipped. That change was made outside this repository, so nothing here confirms it and this project's own record does not carry it.

**Why this is worth taking seriously despite being low priority: it is the first thing a beta tester meets.** The install path is the only part of the method a new user experiences before deciding whether to continue, and [expedite-first-beta-release] puts the first release today. Relates to that item.

**Kept 2026-08-26 with all three proposals together, on your agreement.** The reworded link and the verification phrase are two halves of one fix — a new user cannot otherwise tell whether the assistant is working from the guide or improvising — so the "future" marking on the third is overridden rather than honoured. Neither file is a method rule file, so no rule gate.

--- Build block ---
Changes: `README.md` — make the "New to Claude Code?" path visually first-class in the Install section rather than third of three notes, and reword its line to ask Claude to *read* the guide and walk the user through setup. `INSTALL.md` — add a short verification phrase Claude says on loading the guide, and the instruction in the "Instructions for Claude" section to open with it, so the user can tell a read guide from an improvised walkthrough.
Acceptance: the README new-user route stands out and asks Claude to read the guide; INSTALL.md instructs Claude to open with the phrase and states it; both still read cleanly for a non-coder.
Refused: deferring the verification phrase as future work — it is one sentence and serves the same failure the reworded link guards.
--- End build block ---

#### Six onboarding posts were published from a browser chat, so this project's outbound record and FAQ never learned of them [onboarding-posts-outside-the-record]
Surfaced 2026-08-26 from the install-pathway report (`C:\Users\Alex 2\Downloads\install-process-report.md`). It states that six Discord how-to forum posts were written and published in that session, forming a complete onboarding sequence: installing, first /setup, first /plan, /next, /done and starting fresh, and /rescan. The claim is Claude-authored and unverified here — what is certain is only that this project has no record of them.

**Two standing obligations did not fire, because the posts did not travel through this project's own drafting route.** A posted announcement gets a line in the outbound register naming the date, the destination, what it claimed, and a pointer to the text; that register is what a later repeal is checked against, which is the whole reason it records what a post claimed rather than merely that one happened. And an FAQ entry is authored in the same turn as that line, into the shipped template and its index. Neither exists for any of the six.

**The exposure is specific rather than theoretical.** These posts describe how six commands behave. This session alone changed the behaviour of four of them — /plan's item presentation and asks, /next's edit display, /done's close obligations, /rescan's offer — and the beta ships tomorrow. A post claiming behaviour that a repeal has since falsified is exactly what the register exists to catch, and there is nothing here to grep.

**The honest limit, stated so nobody reads this as fixable in retrospect.** The register's line is written in the same turn as the approval because the exact wording exists then and nothing later reconstructs it. The report says the six posts are in a chat history rather than in any file here, so reconstructing them means recovering their text first — and a line written from memory would be a claim about what was posted rather than a record of it.

**Half of this was resolved the same day, 2026-08-26.** Alex supplied all six posts verbatim, one at a time; they are recorded in `LOG/2026-08-26-onboarding-posts-recovered.md` with each post's claims written out for the repeal check, and all six register lines now exist in `INBOX/sent.md` pointing at that file. The honest limit above is why the record says "recovered 2026-08-26" rather than pretending the lines were written at the send. The recovery immediately earned its keep: reading post two against the installed plugin found a claim that was never true, filed as [onboarding-post-claims-unreleased-popout].

**What remains is the FAQ half, and it is blocked rather than merely outstanding.** An FAQ entry is authored into the shipped template under `plugin/throughliner/templates/`, which the scope-lock deliberately excludes from a planning session's standing surface — editing a template reaches every future consumer. So the six entries these posts owe need a build, not a planning turn.

**Kept 2026-08-26 as the FAQ build, cleared to ride into today's release** — the announcement posted this morning tells the server the FAQ ships with Throughliner, so shipping it with these entries is what makes that claim strong. The route question is deliberately not carried here: the drafting-outside-the-project gap belongs to [method-report-routing-same-machine]'s keep-step, the neighbouring same-machine shape. No rule gate — FAQ content is not rule text.

--- Build block ---
Changes: author six FAQ entries — one per recovered post: installing, first /setup, first /plan, /next, /done and starting fresh, /rescan — into `plugin/throughliner/templates/faq-template.md`, each with its index line in `faq-index-template.md`, then re-copy both templates into `FAQ/faq.md` and `FAQ/index.md`. Source: the posts' verbatim text in `LOG/2026-08-26-onboarding-posts-recovered.md`; each entry is checked against shipped behaviour at authoring, with the /setup entry's pop-out claim carried as true of today's release.
Acceptance: six new entries with matching index lines in both template and `FAQ/` copies; each answers what its post teaches and contradicts nothing the installed-plus-released build does.
Refused: reconstructing the entries from memory of the posts — the recovered verbatim text is the source, per the recovery record's own limit.
--- End build block ---

#### Beta install pin: create the `beta` branch at today's release and point the install docs at it [beta-branch-install-pin]
Raised by you 2026-08-26, processed the same turn: without a ref, everyone installing lands on main and drifts onto dev state between releases. Only a git ref marks a commit, so this advances the install half of [beta-tester-pathway]'s design — the `beta` branch, fast-forwarded to each pick, with the install string `FlintcraftTech/throughliner#beta` — leaving that item's cycle wiring and announcement half where they are. The research caveat travels (`resources/research/claude-marketplace-listing-paths.md`, beta-channel section): ref handling has open feature requests, so nobody but you installs by this route until the smoke test in [beta-install-smoke-and-post-edit] passes. Changing the published install string is what that same [user] line's post edit corrects.

Rule gate: not needed — install docs and a git branch, no method rule text.

--- Build block ---
Changes: `README.md` and `INSTALL.md` — the marketplace-add string becomes `FlintcraftTech/throughliner#beta` in both (the paste prompt, the two commands, and the update instruction), with one plain-English line saying beta is the tested weekly pick while main carries day-to-day development. Then, immediately after today's release commit exists on main: create the `beta` branch at that commit and push it — the branch is created at the release, not before, so it never points at pre-release state.
Acceptance: both docs name the `#beta` route consistently; the `beta` branch exists on the remote at today's release commit; a plain `git log beta` shows the release as its tip.
Refused: pinning to a fixed tag instead of a branch — updates would then require every installer to change their install string, where a branch moves under them by fast-forward.
--- End build block ---

#### Log-index read at the /plan opening is underdesigned: relevance has no test and nothing decides what reaches the user [plan-log-index-read-underdesigned]
Captured by you on 2026-08-25, in your words: "i think that this feature is underdesigned." It surfaced while drafting the Discord post announcing the feature — you asked how the draft's claim was governed in the rules, and the answers exposed the gap rather than closing it.

The shipped rule is two sentences in plan.md's read-state step: read the top five lines of `LOG/index.md`, newest first; fold anything relevant into the opening narration; produce no separate output and no summary of the log for its own sake. Everything after "relevant" is judgment with nothing behind it.

Three things went unanswered when the rule was read against the question.

Relevance has no test. Nothing says what makes a recent line bear on the work in front of the session, so two sessions reading the same five lines could fold in different things, or nothing at all, and both would be following the rule. Nothing checks which happened.

Five is a bare number. The rule states it with no derivation — not a proportion of anything, not a figure from research — which is the failure the method's own rule gate names. Whether five is right for a project closing three sessions a day and one closing three a month is not asked.

Silence and correctness are indistinguishable from outside. Where the read happens and nothing is folded in, the output is identical to the read never happening — the same shape as the cycles check that has now failed live at both its sites. Nothing here is evidence the read runs at all.

**Settled at processing 2026-08-26, each gap given the treatment the method already uses elsewhere.** The window is derived rather than invented: the lines newer than the most recent planning session's record, the same window the dispositions listing uses — a busy day reads more, a quiet month fewer. Relevance is narrowed to a checkable intersection rather than reworded as better judgment, on your own observation (recorded on [opening-reports-uninterpretable-facts]) that a session deliberately denied material cannot judge relevance. And the read gains the required-artifact shape: one line either way, so a silent omission becomes a visible one — the same fix the dispositions listing and the advisory step each got. The related post [discord-post-session-start-strength] is now held behind this item so it cannot announce the underdesigned version.

Rule gate: run — amendment to the read-state step's orientation read, its named parent; the bare five and the untested "relevant" are evicted, replaced by the derived window and the intersection test. No freestanding rule added.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — rewrite the orientation-read paragraph in the read-state step: the read covers index lines newer than the most recent planning session's record (found by its body fields, as the dispositions window already is); a line is folded into the opening narration when it names a slug or file the current queue also names, and not otherwise; and the opening narration carries one line either way — what was read and what it touched, or that nothing read bears on today's queue.
Acceptance: the paragraph states window, test and required line with no bare number and no bare "relevant"; the [BRIEF] tagging of the opening narration is unchanged; nothing else in the step moves.
Refused: keeping "five" with a stated derivation bolted on — no defensible derivation exists for a fixed count across projects with different session rates, which is why the window replaces it.
--- End build block ---

#### Session openings report facts they cannot interpret: "nine log entries have uncommitted changes" sent the user to another session for the answer [opening-reports-uninterpretable-facts]
Captured by you on 2026-08-26, from a live instance minutes after this session's close. You opened a build session in another project and its opening said nine LOG entries carried uncommitted changes from a previous session. It read as alarming, nothing there explained it, and you went back to the previous session to ask — which correctly identified it as the automatic hash backfill and showed the diff proving it: eight entry files each changed by one line where the placeholder became a real hash, plus one index line per entry.

**The defect is that the session that raised it could not answer it.** `done.md`'s staging step carries explicit recognition for this exact signature — a dirty LOG entry or index whose only change is a placeholder becoming a hash is the backfill, folded in with at most a one-line note and no diff opened. The openings have no equivalent, so the same signature arrives as a bare count with no reading attached. A count of changed files is a fact; what it means is one document away and the opening never reaches for it.

**Your observation, and it is the part worth keeping — in your words: it "underlines how impossible 'relevant' is to define in a situation where knowledge is deliberately constrained."** The method deliberately withholds context to keep sessions cheap: a build reads a generated view rather than the queue, an opening reports computed facts rather than interpretations. Those constraints are load-bearing and are not in question. What this shows is that a rule telling a session to surface what is *relevant* cannot be applied by a session that has been denied the material relevance would be judged against — so the failure is structural rather than a slip of judgment.

This sharpens [plan-log-index-read-underdesigned], which found the same word undefined at the log-index read, and should be processed alongside it — but it is not the same item: that one is about which recent history gets folded in, this is about a session reporting something it cannot explain. Both are about the same undefined word, from opposite ends.

**Settled at processing 2026-08-26, one answer per question.** The openings gain the recognition in the hook itself — the fact and its reading arrive together, since a doc step would re-create the noticing this fails at. The generalisation is refused: "explain any fact you cannot interpret" is an untestable judgment rule, the same defect this pair removes, so further signatures earn recognitions one at a time as they are found. And "relevant" is handled at the sibling: the orientation read's instance was evicted by [plan-log-index-read-underdesigned], and any remaining instance is the compliance audit's to find.

Rule gate: not needed — hook behaviour, no method rule text.

--- Build block ---
Changes: `plugin/throughliner/hooks/session_start.py` — the uncommitted-changes line: where every change to a `LOG/` file matches the hash-backfill signature (a placeholder becoming a real hash in an entry file, plus its index line), the line names it as the automatic backfill and normal, instead of a bare count; files outside that signature keep the plain count with the existing "/done will pick them up" wording. Update the session_start suite under `resources/testing/` for both cases.
Acceptance: driving the hook over a fixture whose only LOG changes are backfill-shaped prints the recognition; a fixture with mixed changes prints the count and the recognition separately; the suites pass at the close.
Refused: a general explain-what-you-report rule — untestable judgment, the defect this pair exists to remove.
--- End build block ---

#### Method-problem routing needs a same-machine arm: your own projects draft for the public report form before the INBOX [method-report-routing-same-machine]
Raised by you 2026-08-25, from the pattern you named and the record confirms: the shipped discriminator says a method problem routes to flintcraft.tech/report, with no arm for the method's dev project living on the same machine — so sessions in your own projects draft for the public form (stripped of specifics, per that form's rules) and convert to INBOX mail only when you redirect them, which you have now done repeatedly. The demo chat's 2026-08-24 transcript shows a live instance: report drafted first, INBOXed on your correction. Your words: "we don't report when we're on the same machine as Throughliner, we inbox that project." Also from the same exchange: the "consumer report" label reads as the external feedback channel — in this repo "consumer" means a project running the plugin, all currently yours — so the terminology invites the misroute and is worth fixing alongside. **Settled at processing 2026-08-26.** The address book is the mechanism, and it makes the whole arm shippable rather than host-only: an entry exists only where the user supplied one, so external consumers never hit the arm and nothing scans the machine. The SPEC sentence was written in the same planning session (the Reporting-a-problem paragraph). The "consumer" label comes out of the headings — in this repo it means any project running the plugin, so it invites exactly this misroute.

Rule gate: run — amendment to the method-problem arm of the existing report discriminator, its named parent, in both copies of the discriminator; the "consumer" heading label is evicted with it. No freestanding rule added.

--- Build block ---
Changes: `plugin/throughliner/docs/feedback-and-inbox.md` — the discriminator's method arm gains the same-machine case (mail to the plugin's own project where the address book records it as a correspondent; issue/form for everyone else and as fallback), and the "Consumer feedback channel" heading becomes "Method problem reports". `plugin/throughliner/docs/skill-nonspecific-rules.md` — the same arm in its copy of the discriminator, and its section heading loses "Consumer"; the two copies must agree. `README.md` — one clause in the reporting paragraph covering the same-machine case in plain English. Check `templates/faq-template.md` for a routing entry and align it where one exists.
Acceptance: both discriminator copies state the same three-plus-one routing; no shipped heading says "consumer"; README's clause reads for a non-coder. Exclusion, stated: `ANNOUNCEMENT-IDEAS.md`'s old FAQ entry stays as it is — it describes the external user's route, which remains true.
--- End build block ---

#### Narration cadence is steered only by the brevity style, so a project without it gets none [narration-cadence-promotion-candidate]
Found by the two-way style audit, 2026-08-25. The style's fifth bullet — work quietly between tool calls, speak for the first call, for finding something important or changing direction, and for the finish led by the outcome (`plugin/throughliner/output-styles/brevity.md` lines 23-25) — has no counterpart anywhere in the always-loaded rules. A project that declined the style therefore gets no steering at all on how often Claude speaks during a run.

This is the mirror of the dedup finding rather than a separate subject: the same consent-gated layer, read in the other direction. `resources/research/response-length-and-bundling-steering.md` names narration as a different problem from length, calls its absence the largest identified gap, and quotes the guide's ready-made cadence instruction.

**Admitted at processing 2026-08-26.** The dedup repeal's SPEC sentence names this shape exactly: a rule living only in the consent-gated style is a defect, and promotion is the fix. The style's own bullet stays — restatement at system-prompt level is now the sanctioned mechanism, not a duplication.

Rule gate: run — subordinate bullet under the Communication shape-every-message rule, its named parent; gerund-led like its siblings, so no freestanding slot is spent and nothing is evicted. Admission: the failure is documented (the research names narration the largest identified gap), verbose models do not do it unprompted, it fires in every skill and in plain conversation, and no hook can enforce a narration cadence.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — add one subordinate bullet to the Communication "shape every message the same way" list: speaking between tool calls for the first call, a load-bearing finding, or a change of direction — and closing with the outcome first. Gerund-led, matching the list's grammar.
Acceptance: the bullet reads as a continuation of the parent's opening words alongside its siblings; no new freestanding rule appears; the style's cadence bullet is untouched.
Refused: evicting the style's cadence bullet in exchange — the repealed dedup policy is not re-applied in reverse; restatement is the style's mechanism.
--- End build block ---

#### Brevity style is about a third prohibitions, against its own research and the method's wording rule [style-negatives-to-rewrite-positive]
Found by the two-way style audit, 2026-08-25. Four of nine bullets are stated as things not to do: never preview later items, no internal procedure vocabulary in what the user reads, no summary of a change on top of the record, and never shorten by compressing into fragments or jargon (`plugin/throughliner/output-styles/brevity.md` lines 20, 27, 30, 32).

Two standards say this is the wrong shape. `resources/research/response-length-and-bundling-steering.md` lists negative instructions among the confirmed dead ends and names telling Claude what to do instead as one of the few formatting levers documented to work. The method's own rule-wording rule says anything described in terms of what not to do means the rule of what TO do was never adequately described, and treats a prohibition as a signal to go back and specify the action.

The work is rewriting each as the action it wants. The research also records the strongest local evidence available on this: the one site where bundling was actually fixed was plan.md's checkpoint, fixed by showing a specimen message rather than by stating a rule — so a specimen is worth weighing alongside the rewrite.

**Kept 2026-08-26.** The four actions, settled at processing: give exactly the current item, then stop; say it in the reader's words, translating procedure terms into what they mean for them; report a change as one line naming what landed and where; shorten by dropping detail that changes nothing for the reader, in full sentences.

Rule gate: not needed — the style file is not on the gate's trigger paths; the wording rule still governs the authoring.

--- Build block ---
Changes: `plugin/throughliner/output-styles/brevity.md` — rewrite the four prohibition bullets (lines 20, 27, 30, 32 at filing) as the actions above, keeping each bullet's subject and place in the list.
Acceptance: no bullet states only what not to do; the style's total length does not grow materially, since it is paid at every session start.
Refused: a specimen message inside the style file — a style is system-prompt text paid by every session in every conversation, where the checkpoint's specimen evidence comes from a procedure doc paid only when its skill runs; reconsider only if the rewrite alone does not move behaviour.
--- End build block ---

#### [audit] Compliance audit of the rule changes since the last one, scoped to the files this run touched [compliance-audit-lag]
Filed by the audit-lag check in `resources/rule_signals.py`, run at this session's close on 2026-08-26. One rule-bearing commit since `2026-08-24-compliance-audit-lag-build.md` has not been covered by a compliance audit, and this run adds a second and much larger one — twenty rule amendments across the always-loaded rules and every skill doc.

Delta scope, as the check printed it: `CLAUDE.md`, `plugin/throughliner/docs/done.md`, `feedback-and-inbox.md`, `next.md`, `plan.md`, `rescan.md`, `setup.md`, `skill-nonspecific-rules.md`. `next-build.md` and `templates/CLAUDE-TEMPLATE.md` were also touched by this run and belong in the scope when the audit is designed.

The criteria are standing and are not re-derived: `resources/method-compliance-audit-checklist.md` carries the four lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history in operative text via the delete-and-read test. This is the periodic sweep of already-shipped text, distinct from the rule gate's per-rule use at authoring time.

Worth knowing when this is scoped: the previous audit of this kind produced four findings that were all real and all built, three of which this run shipped. That is the argument for running it against a batch this size rather than deferring it further.

**Kept 2026-08-26, cleared with the end group.** The scope is recomputed at run time from the record rather than frozen at filing — this planning session's own close adds another rule-bearing commit (the cycles-step amendments and the Fable/Opus split note), and a frozen list would miss the newest batch.

Rule gate: not needed — an audit authors no rules; it reads shipped text and files findings as captures.

--- Build block ---
Changes: none — an audit edits nothing. Read the rule-bearing files changed by commits since the most recent compliance-audit record (recompute the delta at run time; at filing it was CLAUDE.md, done.md, feedback-and-inbox.md, next.md, next-build.md, plan.md, rescan.md, setup.md, skill-nonspecific-rules.md, templates/CLAUDE-TEMPLATE.md) against the four lenses in `resources/method-compliance-audit-checklist.md`. Each finding becomes a capture in Unprocessed.
Acceptance: every file in the recomputed delta read under all four lenses; findings filed as captures, or the clean pass recorded in the run's record.
--- End build block ---

#### [audit] Transcript pair analysis, AFK-cats: the planning session and the failed build read together [transcripts-two-failed-builds-analysis]
Captured by you on 2026-08-26 as a four-transcript item; split at processing the same day into one item per project pair, on Claude's recommendation and your agreement — four at 1.1 to 1.9 MB are more than one session's reading, and each pair must be read together because a build that went wrong may have been set up to by what its planning run agreed. The sibling is [transcripts-taskflowapp-pair-analysis]. Both are evidence against 1.20.0-test18 (stamp 4ecaf49c1305), the version today's release leaves behind — a finding is checked against the current build before being filed as live.

The pair:
- `C:\Users\Alex 2\.claude\projects\C--Users-Alex-2-My-Drive-Desktop-AFK-cats\028fb28e-c466-494f-b0e9-a07a72994f1b.jsonl` (1.1 MB)
- `C:\Users\Alex 2\.claude\projects\C--Users-Alex-2-My-Drive-Desktop-AFK-cats\da1599f2-1983-4d79-b78c-93a8efcea3a1.jsonl` (1.3 MB)

Which file is the planning session is read off the transcripts. One defect from this pair is already diagnosed and patched — the walkthrough-heading mismatch ([build-view-walkthrough-heading-mismatch], from that project's own report) — so the reading notes it as handled and looks for what else the pair shows.

Rule gate: not needed — an audit authors no rules; findings become captures.

--- Build block ---
Changes: none — an audit edits nothing outside the scratchpad. Preprocess both transcripts with a short Python pass to conversation text alone (drop tool calls, tool results, thinking, metadata), written as slim files in the session scratchpad; read the pair together, planning session first; file each defect as a capture, checked against the current build before being filed as live.
Acceptance: both slim files read end to end; findings filed as captures, or the clean pass recorded in the run's record.
--- End build block ---

#### [audit] Transcript pair analysis, Taskflowapp: the planning session and the failed build read together [transcripts-taskflowapp-pair-analysis]
Split 2026-08-26 from [transcripts-two-failed-builds-analysis], which carries the shared reasoning: pairs read together, evidence against 1.20.0-test18, findings checked against the current build before filing.

The pair:
- `C:\Users\Alex 2\.claude\projects\C--Users-Alex-2-My-Drive-Desktop-Prioritity-projects-Taskflow-Planning-Planning-in-here-Taskflowapp\536b761a-8e4d-4a3e-ab88-5793a902589a.jsonl` (1.9 MB)
- `C:\Users\Alex 2\.claude\projects\C--Users-Alex-2-My-Drive-Desktop-Prioritity-projects-Taskflow-Planning-Planning-in-here-Taskflowapp\8731b6b2-3edf-4c4c-aea3-1f93b8e8a625.jsonl` (1.2 MB)

Rule gate: not needed — an audit authors no rules; findings become captures.

--- Build block ---
Changes: none — an audit edits nothing outside the scratchpad. Preprocess both transcripts to conversation-text slim files in the session scratchpad; read the pair together, planning session first; file each defect as a capture, checked against the current build before being filed as live.
Acceptance: both slim files read end to end; findings filed as captures, or the clean pass recorded in the run's record.
--- End build block ---

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

#### [user] Verify the cycles due-ness check live: one capture filed when due, no duplicate on the next opening [cycles-due-check-verification]
Filed 2026-08-22 at the keep-step, on Claude's recommendation and your agreement. The cycles build ("Cycles shipped", record `2026-08-22-cycles-definitions-and-due-checks-build.md`) ticked done with one behaviour UNCONFIRMED: only the no-doc silent path was exercised, because this project has no cycles doc. Confirming it needs a live session in a project whose `CYCLES.md` carries a past-due observable — user work, since it happens in another project's session during your testing days. The release-cycle definition item ("Define this project's weekly release cycle") is held on this verification and lifts when it closes — timed so the definition can build before Wednesday 10am.
**Walkthrough.**
1. In any project you're testing the rezip in (not Taskflowapp's product files — its INBOX is the only sanctioned write there, so pick another test project), ask Claude to create a test `CYCLES.md` at the project root with one definition whose observable is already past due — say a weekly cycle whose last completed turn reads as two weeks ago.
2. Run /plan (or /next) there. Look for: one capture appearing in that project's queue under the cycle's slug, naming the due step.
3. Run another opening in that project without touching the capture. Look for: no second capture — the check is satisfied while one is open.
4. Ask Claude there to delete the test `CYCLES.md` and the test capture.
5. Tell this project what you saw; this line closes and the definition item lifts.
**Held 2026-08-26 at the planning close.** The feature this verifies is confirmed not to fire on the installed build ([cycles-check-fires-nowhere], whose fix is cleared to run) — walking this before that fix ships and a rezip lands can only reproduce the known failure. The dependency is host-side: it lifts once the fix is built and the host reinstalled.
Blocked by: [cycles-check-fires-nowhere]

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

#### First beta ships today from the current build; still open: the Wednesday stable-label selector and the nerds-list mechanics [expedite-first-beta-release]
Your decision, settled 2026-08-26 in this planning session: the first beta releases **today**, Wednesday 2026-08-26, from the **current build** — your words: fake it until we make it — grounded in your own testing of /plan, /next and /done on this build, which you judge almost stable. The announcement went out on Discord this morning; its verbatim text and claims are recorded in `LOG/2026-08-26-beta-announcement-recovered.md` with its register line in `INBOX/sent.md`. The reach-back question is closed: no older version. Cleared work runs before the release — [build-view-walkthrough-heading-mismatch] (the patch for the issue a consumer project mailed today) and [planning-fable-building-opus-note]. The install-route check ([install-route-latest-release-check]) was run at processing and deleted as satisfied: the marketplace route serves whatever main holds, never the release artifact, so no doc sentence needed correcting — the consequences accepted on your yes are that today's release runs as the day's last act (so main equals the beta at that moment) and that installers drift onto dev state between releases until [beta-tester-pathway]'s `beta` branch ships. Today is beta-only: a hand-driven Wednesday turn with no prior beta to promote to stable. The transcript hard-rescan ([transcripts-two-failed-builds-analysis]) is deliberately deferred until you supply the files. Releasing from the current build also resolves [onboarding-post-claims-unreleased-popout] down its nothing-to-change branch — pop-out ships with today's release; its walkthrough's read-through step remains.

**The beta chain stays exactly as wired — your decision today.** [beta-tester-pathway] blocked by [weekly-release-cycle], blocked by [cycles-due-check-verification], with [beta-launch-announcement] behind the pathway: today's release proceeds beside that chain, not through it. This morning's announcement lands ahead of [beta-launch-announcement], so that item's premise needs re-reading at its keep rather than assuming it still describes what to post.

**What is not in question:** every release is marked pre-release and runs only from main, and a release happens when you ask for one. Nothing here changes that.

**The nerds list, raised 2026-08-26 and now partly real.** A running record of test rezips in a Discord channel, each entry carrying one of three labels in your own wording — "stable - [caveats]", "not stable - [problems]", or "under testing - use at your own risk" — with a download link and instructions link, inside the 2,000-character limit; you post each entry and prune by hand past fifteen. **You created the channel today: a locked test-rezip channel readable only by the "nerd" role, given to people present today or yesterday or who ask.**

**One check on it before it is designed. Downloadable zips do exist** — `plugin/zip-archive/` is committed and browsable on GitHub, and you can link straight to a file in it. Claude's first account of this said there was nothing to download, which was wrong and you corrected it.

**What is missing is narrower: none of them is a rezip.** The folder holds `si-plugin-v1.14.0.zip`, `si-plugin-v1.15.0.zip` and `si-plugin-v1.16.0-reverted.zip`, with `plugin/throughliner.zip` one level up — verified against `origin/main`, not just the working copy. Every one was produced by a **release**, which runs `Compress-Archive`, archives the previous zip and prunes the folder to three. A rezip runs none of that: the local marketplace sources the folder and the CLI snapshots it directly, so today's rezip adds nothing to that folder and the newest archived zip is four minor versions behind the installed build. So "keep fifteen rather than three" describes the release archive, and a link labelled as this week's test rezip has no file to point at yet.

That leaves two shapes, and they cost very differently. Either the rezip ritual gains a packaging-and-upload step so a test rezip becomes downloadable — new work in a ritual deliberately kept cheap — or the thing being listed is simply a more frequent pre-release, which is what a release already is, since every one is marked pre-release. The second shape needs almost no machinery and mostly needs the labels and the posting rhythm; whether it still feels like less stress is yours to judge.

Two consequences to carry into whichever is chosen: fifteen zips kept in the repository is real weight, worth deciding deliberately rather than by raising a number; and the posting-and-pruning is recurring work you do by hand, which is the shape a cycle exists for — an offer for planning to make, not a decision here.

**Your synthesis, 2026-08-26: the nerds list feeds the beta cycle — each Wednesday's pick is the most recent zip labelled stable.** That supplies something the beta chain never had, a defined candidate set with a readable state on each candidate, and it is why this stops being an alternative to the beta and becomes an input to it.

**It does touch a decision those items made deliberately, and planning should meet that head-on rather than discover it mid-build.** [weekly-release-cycle] fixes the Wednesday pick as *the newest rezip at least a week old* and explicitly refuses choosing among candidates each Wednesday, because the release model's recorded failure was the prospective readiness question — "is this good enough to publish?" — which stopped releases happening at all. Picking the most recent *stable-labelled* zip is a different selector, and it reads as reintroducing judgment.

**The argument that it does not, stated so it can be attacked rather than assumed:** the label is applied when the rezip is posted, describing a build that already exists, so the Wednesday pick reads a state rather than forming an opinion. The property that made the cycle safe was that nothing at release time asks whether the work is ready; a label written days earlier preserves that. What changes is that a build nobody could vouch for is skipped instead of shipped on age alone — which is what the seven-day soak was standing in for.

**The two do not collide on the tester side.** [beta-tester-pathway] refuses zip downloads for testers in favour of a ref-pinned marketplace add on a `beta` branch. The nerds list is zips for people who want raw dev builds; beta testers still install from the branch. Both can be true at once, and the list is the shop window that makes a Wednesday pick meaningful.

**One consequence worth checking at planning, because it may cut the chain that is currently stuck.** Both held items are blocked behind [cycles-due-check-verification], which cannot close while [cycles-check-fires-nowhere] stands. If the Wednesday turn is something you do by hand — post the entry, pick the stable one, fast-forward the branch — then the cycles due-ness check is a convenience on top rather than the thing the pathway depends on, and the blocker may be repointable or droppable. That is a real question rather than a recommendation: the cycle definition is what carries the two-event turn, and whether it can wait needs reading rather than asserting.

Still for processing, at the release-cycle and beta-pathway keep-steps: whether the Wednesday pick becomes the most recent zip labelled stable (the selector question above, argued both ways), whether the chain's far-end blocker can be repointed off the broken cycles check, and the nerds-list packaging shape (labelled pre-releases versus new rezip machinery). Today's release is settled above and is not among them.

#### Process-now "yes" was spent as disposition approval: two items written and cleared with no recommend-and-wait turn [process-now-yes-spent-as-disposition]
Raised by you 2026-08-26, in a live /plan on this project: after the process-now offer for the beta install pin, your "yes, process it now" — an answer to *when* — was treated as approval of a design first shown in the offer message, and two items were written and cleared with no recommendation turn. Your words: "you skipped processing and landed stuff straight to queue like was always happening with 'keep' in the last version." Repaired in-session: you reviewed and kept both items as written.

The rule already forbids this — plan.md's fold conditions say a design first shown in the offer message cannot fold, and the process-now section says either branch is subject to them — so this is an instance of a shipped rule not being followed, not a missing rule. Evidence for the keep-step: the one site where bundling was actually fixed was the checkpoint, fixed by a specimen message rather than a rule statement ([style-negatives-to-rewrite-positive] carries the citation) — so the candidate fix is a specimen at the process-now section showing the offer turn and the separate recommend turn, weighed against accepting it as a slip. Runs on the version installed today, so check the current text before scoping.

#### Should cycles get mermaid diagrams? [cycles-mermaid-diagrams]
Captured by you, 2026-08-24, mid-planning — your framing: seems reasonable. Filed at your direction without discussion, so the idea is unshaped: what a diagram would show (a cycle's steps? the turn's two events? due-ness over time?), where it would live (in CYCLES.md beside the definition, or generated), and who reads it are all open for the keep-step. Context worth having there: the desktop app renders mermaid in its markdown viewer, and the cycles doc is user-facing by design.
Skipped 2026-08-26 on Claude's recommendation and your agreement: what settles it is a build that must ship first — [weekly-release-cycle] creating this project's first real cycles doc, with the due-ness check working ([cycles-check-fires-nowhere]'s fix). A diagram designed before any real cycles doc exists would be guessing at a document nobody has seen; take it up once there is one to draw.

