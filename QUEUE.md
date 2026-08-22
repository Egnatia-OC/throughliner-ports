# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Evict the two rules the shipped brevity style now carries better — quiet-work and regression-tone [style-dedup-evictions]
From the [style-level-rule-dedup-audit] run of 2026-08-22, all findings approved. The style-level dedup audit compared each rule in the shipped output style against its lower sites, parent-axis only. Seven of nine rules stay below: their lower sites carry machinery or operative detail the style deliberately omits (the [SEQUENCE] tag, the inversion block's second arm, the vocabulary decision table, command-naming detail). Two are near-verbatim duplications of pure tone steering that degrades gracefully where the style is absent, and those are the evictions: "Speak when something warrants it, and work quietly between" (skill-nonspecific-rules.md, Communication) and "State a regression in the same plain terms as a success, and move on" (same section). SPEC's dedup rule is the ground: a rule carried at style level is stated there and nowhere below it.

**Kept 2026-08-22, scope narrowed at processing.** The audit's third finding — a "state the count" clause carried three times — did not survive verification: the Communication bullet carries no count clause in the file as it stands, so only the [SEQUENCE] tag and the style state it, which is the correct two-site shape. The trim limb is dropped as already satisfied. The re-weighed caveat is accepted: a declined-style project loses the explicit statement, and that is tolerable because both rules are pure tone steering that degrades gracefully — a session without them runs slightly more verbose, nothing breaks. `INBOX/sent.md` was grepped for both sentences: no post announced either rule, so no correction post is owed.

Rule gate: run — pure eviction, nothing added; the shipped brevity style is the named replacement, already carrying both rules near-verbatim at a level above the docs.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — delete two bullets from the Communication section: the "Speak when something warrants it, and work quietly between" bullet (including its what-warrants-it sentences) and the "State a regression in the same plain terms as a success, and move on" bullet. Nothing else changes.
Acceptance: neither sentence remains anywhere in `docs/`; the brevity style still carries both; the Communication section still reads whole.
Refused: trimming a "state the count" clause from the Communication bullet — the clause does not exist there; only the [SEQUENCE] tag and the style carry it, which is correct.
--- End build block ---
**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

#### Plan-only capture-offer rule sits in the always-loaded file, duplicating plan.md's process-now section [plan-only-rule-in-always-loaded-file]
From the [post-restyle-compliance-audit], findings 1 and 2, approved 2026-08-22. The "Inside /plan only, an un-agreed idea gets an offer, put before the write" block in skill-nonspecific-rules.md's Communication section is a /plan-only rule in the file whose own admission test requires firing in all four skills or with no skill running. plan.md's "Process-now offer after a user raises something" section states the same offer at the child level — a parent-axis duplication where the child is loaded with the parent.

**Kept 2026-08-22.** plan.md's process-now section was compared clause-by-clause against the always-loaded block and carries everything it does — both branches, the recommendation, the write-saving reason, the no-further-solicitation bar — so the always-loaded copy deletes with nothing relocated. What stays in the always-loaded file: the close-by-who-raised-it rule and the already-agreed-is-written-without-asking carve-out, both of which genuinely fire everywhere. Two references repoint: the "The offers above are for un-agreed ideas" sentence, and the discovery-rule table's "INSIDE /plan" comment — both now cite plan.md's process-now section rather than the deleted block.

Rule gate: run — eviction by relocation; the rule's one home becomes plan.md, which already states it in full, and the always-loaded file's own admission test is the ground.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` only. In the capturing-mid-skill bullet, delete from "**Inside /plan only, an un-agreed idea gets an offer…**" through "…immediately rewritten as a work item.", and reword the later reference so it reads that the /plan-time offer lives in plan.md's process-now section and is for un-agreed ideas. In the Routing section's discovery table, repoint the "INSIDE /plan" comment from "the /plan carve-out in Communication above" to plan.md's process-now section. plan.md itself changes nothing — verified complete at processing.
Acceptance: "Inside /plan only" no longer appears in skill-nonspecific-rules.md; the close-by-who-raised-it rule and the already-agreed carve-out still read whole; both repointed references name plan.md.
--- End build block ---
**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

#### One history clause rides the work-from-one-chat rule in the always-loaded file [snr-one-chat-history-clause]
From the [post-restyle-compliance-audit], finding 5, approved 2026-08-22. In skill-nonspecific-rules.md's "One chat runs /plan and /next" bullet, the clause "— a shape supported here for a period, which fell over every time it was tried" is history riding the work-on-a-project-from-one-chat rule; the delete-and-read test leaves a complete instruction without it. Small, but it is in the always-loaded file, where each clause costs every session.

**Kept 2026-08-22.** The rule reads whole without the clause: "Work on a project from one chat at a time, because a capture filed in one chat is invisible to the other and the two disagree about the queue from the moment either writes to it." The reason stays — it is operative, saying why the rule binds — and only the tried-and-fell-over history goes. The history survives in the audit's own record and in git, which is where evicted whys live.

Rule gate: run — history eviction under the rationale-lives-outside-the-operative-rule split; nothing added, nothing else displaced.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — in the "One chat runs /plan and /next" bullet, delete the clause "— a shape supported here for a period, which fell over every time it was tried" and rejoin the sentence cleanly. Nothing else changes.
Acceptance: the clause is gone; the surrounding rule reads as a complete instruction; "fell over every time" appears nowhere in `docs/`.
--- End build block ---
**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

#### done-build.md's reply step still carries the broad changed-work trigger the reply rule just dropped [done-build-reply-trigger-stale]
The reply obligation was narrowed to question-asking messages ([inbound-replies-not-drafted]): feedback-and-inbox.md's triage and the always-loaded rule now both say a question is owed a reply and a defect report is owed nothing. done-build.md's step 1.5 ("Reply to mail the run opened") still fires on "a message that changed work here" — the broad trigger the amendment evicted elsewhere. That file was outside the item's described work, so the build filed this rather than folding it in. The fix is one wording change aligning 1.5's trigger with the question form.

**Kept 2026-08-22.** Verified live at done-build.md's step 1.5: "a message that changed work here". Straight alignment with the already-decided narrowing — no new decision here.
Rule gate: run — transcription of an amendment already admitted under [inbound-replies-not-drafted]; nothing new authored.

--- Build block ---
Changes: `plugin/throughliner/docs/done-build.md` — in the reply-to-mail step, replace the "a message that changed work here" trigger with the question form: a message that asked a question is owed a drafted reply; a defect report is owed nothing.
Acceptance: "changed work here" no longer appears in done-build.md; the step's trigger matches feedback-and-inbox.md's triage wording.
--- End build block ---
**Files:** `plugin/throughliner/docs/done-build.md`.

#### Re-scan candidates are written before the user sees them, and the user's position is that in-progress captures should be shown first [rescan-candidates-precede-approval]
Raised by the user 2026-08-22 at a close, in her words: there's "no point actually writing them to file until they have been approved." Her distinction: the show-first switch and remote reading cover captures *already written* — what can't be read anywhere is a capture *being formed*. She names the parent herself: this is the ideation-loop rule ("offer to capture and hold the write until the user says go") extended to the wind-down re-scan's candidates, which the step currently exempts — its text says "nothing waits on approval before reaching disk," resting on the write-first recoverability test. Prior decision cited: write-first's trade was stated when it shipped; this narrows it at one site rather than reversing it.

**Kept 2026-08-22, on your position.** The cost rounds to zero: the candidates already go out as one numbered message, and showing it before the writes changes order, not length. The named trade — a close now waits at this step — is accepted: /done is user-invoked, so someone is there when it runs.
Rule gate: run — amendment extending the ideation-loop parent to the re-scan sites; the exemption sentence it replaces ("nothing waits on approval before reaching disk") is named and comes out in the same move.

--- Build block ---
Changes: `plugin/throughliner/docs/rescan.md` and `plugin/throughliner/docs/done.md` (the wind-down re-scan step) — the candidate set is shown as one numbered message before anything is written; the user contests by number or says go; the writes then land. Delete the "nothing waits on approval before reaching disk" exemption wherever the two files state it.
Acceptance: both files show-then-write; the exemption sentence appears nowhere in `docs/`; the numbered-set shape is unchanged otherwise.
--- End build block ---
**Files:** `plugin/throughliner/docs/rescan.md`, `plugin/throughliner/docs/done.md`.

#### migrate-checklist.md is tag-free without declaring it, and its approval moment is prose where a tag belongs [migrate-checklist-untagged]
From the [post-restyle-compliance-audit], finding 6, approved 2026-08-22, tag-placement lens. setup.md declares itself tag-free with a stated reason (it runs where the tag definitions may not be loaded); migrate-checklist.md runs in the same situations, carries no tags, and states no reason — so a reader cannot tell deliberate from omitted.

**Kept 2026-08-22 on the declare-tag-free design.** Tagging was refused: the checklist runs where setup.md runs, so the same reason setup.md is tag-free applies, and the consistent fix is the same declaration. The prose approval moment stays prose, now covered by the declaration.
Rule gate: not needed — a declaration matching an existing sibling's; no rule authored.

--- Build block ---
Changes: `plugin/throughliner/docs/migrate-checklist.md` — add a one-line tag-free declaration mirroring setup.md's, stating the doc carries no response-shape tags because it runs where the tag definitions may not be loaded.
Acceptance: the declaration reads the same way setup.md's does; nothing else in the file changes.
Refused: encoding the approval moment as [PROMPT] — inconsistent with the doc being tag-free for the same reason as setup.md.
--- End build block ---
**Files:** `plugin/throughliner/docs/migrate-checklist.md`.

#### Cycles: a definitions doc plus due-ness checks at the work cycle's openings and closes [cycles-definitions-and-due-checks]
**Your concept, raised 2026-08-22 in this planning session; the definitions/position split is Claude's.** A user can put an artifact on a cycle — recurring work with its own rhythm, independent of the work cycle's — by defining it once. Your framing: no new skill; a template-like concept; checks at the open and close of /plan and /next for what cycles exist and where each is up to; possibly a new doc. Your examples: posts, articles, videos, and this project's own release timing.

**The design settled in-session.** Definitions live in a dedicated cycles doc, created by /plan the first time a user asks for one; a project with no cycles has no doc and pays nothing. Position is never stored — the board and merge-cycle failures, plus rule_signals' nothing-is-stored rule, are the grounds — instead each definition names the observable that marks a completed turn, and the checks compute due-ness from the world. A due step files one capture, satisfied while an open capture with its slug exists, so due work enters the queue rather than standing as a notice. Cadence may be declared (arbitrary) or derived; the definition says which. SPEC's cycles paragraph was written in this session, ahead of the build.

**Added at your instruction, 2026-08-22, before close: Claude proactively suggests a cycle where one suits.** The site is /plan's keep-step — the moment work is being weighed with you in the room: where an item is recurring-shaped (the same artifact worked repeatedly — posts landing one after another, releases, a maintenance pass done before), Claude offers a cycle once, in the item's own message, and never nags. Suggestion only; creating one stays your call.

Rule gate: run — a new fetched-doc mechanism plus one check clause at each of the three sites (plan.md's opening, next.md's pre-flight, done.md's wind-down), and one suggest-clause at the keep-step; the doc is fetched on a named trigger (its own presence), so nothing joins the always-loaded set; nothing is displaced at the three sites and that is stated rather than hidden; the file-a-capture pattern is copied from rule_signals rather than invented.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the opening gains the cycles check (if the project's cycles doc exists, read it, compute due-ness per definition from its observable, file one capture per due step unless one is open) and the keep-step's route for a user asking to create a cycle (author the definition into the doc with the user present, including artifact, steps, cadence and observable), plus the suggest-clause: where an item is recurring-shaped, offer a cycle once in that item's message, never as its own turn. `plugin/throughliner/docs/next.md` — the same check in the pre-flight, filing only. `plugin/throughliner/docs/done.md` — the same check in the wind-down, filing only. `plugin/throughliner/templates/faq-template.md` — a "What is a cycle?" entry and its index line; then re-copy `FAQ/faq.md` and `FAQ/index.md` from the templates.
Acceptance: all three sites carry the check; a hand-made definition with a past-due observable produces exactly one capture across repeated checks; a project with no cycles doc produces no output at any site; FAQ/ matches the template.
Refused: a new skill (your call); stored position in the doc (a state file the first forgetful session makes lie); a standing board of cycle positions (the notice nobody is obliged to read — the board failure re-run).
--- End build block ---
**Files:** `plugin/throughliner/docs/plan.md`, `plugin/throughliner/docs/next.md`, `plugin/throughliner/docs/done.md`, `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

#### SPEC and README rest the throughline on total amnesia, which current Claude Code no longer has [throughline-claim-overstates-amnesia]
Finding from [claims-need-a-claude-code-delta-test], approved 2026-08-21. SPEC ("Claude's memory resets each session") and the README claim a fresh session carries nothing forward — current Claude Code ships an auto memory directory and context summarization that carries work across windows, so the delta test fails the claim on its own terms. The throughline's real delta is structured, user-vouched product truth versus Claude's private notes; restate the claim on that ground.

**Kept 2026-08-22, split by writable surface.** SPEC's sentence was rewritten in this planning session, with the user present: the claim now rests on the vouched-versus-private delta ("different in kind, not just in durability") rather than on total amnesia, and keeps the fresh-session case as the floor rather than the premise. What remains is the build half — README's mirror claim and the FAQ template's "Why does the method record the reasoning" entry, restated on the same ground, in the same register as the SPEC sentence.
Rule gate: not needed — consumer-facing description, no method rule authored.

--- Build block ---
Changes: `README.md` — restate the throughline claim on the vouched-versus-private ground, dropping any sentence saying a fresh session carries nothing forward. `plugin/throughliner/templates/faq-template.md` — the "Why does the method record the reasoning" entry gets the same restatement; after editing the template, re-copy `FAQ/faq.md` and `FAQ/index.md` from the templates, which are canonical.
Acceptance: no doc claims total amnesia; all three surfaces (SPEC, README, FAQ) state the same delta; FAQ/ matches the template byte-for-byte.
--- End build block ---
**Files:** `README.md`, `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

#### INBOX framing predates Claude Code's live session messaging [inbox-claim-predates-live-messaging]
Finding from [claims-need-a-claude-code-delta-test], approved 2026-08-21. "Projects message each other instead of you carrying notes between chats" reads as if no channel exists at all; Claude Code can now message live sessions on one machine. The INBOX's delta — durable, offline, approval-gated mail between projects — is real and currently implicit.

**Kept 2026-08-22, split by writable surface like its sibling [throughline-claim-overstates-amnesia].** SPEC's INBOX paragraph gained the clause in this planning session: live messaging exists, and the INBOX's delta is durable, offline, approval-gated mail. The build half restates the same delta where README and feedback-and-inbox.md describe the feature.
Rule gate: not needed — consumer-facing description, no method rule authored.

--- Build block ---
Changes: `README.md` — where the INBOX is described, add the one-clause delta (durable, offline, approval-gated mail, versus Claude Code's live-session messaging). `plugin/throughliner/docs/feedback-and-inbox.md` — the same clause in its opening description.
Acceptance: neither file implies no other channel exists; both name the same delta SPEC now states.
--- End build block ---
**Files:** `README.md`, `plugin/throughliner/docs/feedback-and-inbox.md`.

#### SPEC's advisory paragraph owes the replace-branch sentence [spec-owes-advisory-replace-sentence]
Filed by the build close, 2026-08-21. [advisory-step-collides-with-a-spent-note] shipped: a close meeting a spent advisory in the reserved slot now replaces it — deletes the spent note and files its own, saying it replaced one. SPEC's forward-recommendation paragraph still said clearing happens only at the next /plan's read.

**Kept 2026-08-22, SPEC half done in-session.** The owed sentence is written into SPEC's forward-recommendation paragraph with the user present. What remains is the FAQ half: the template is canonical and a planning session cannot edit it, so the one-clause update to the "Last session advises…" entry is the build.
Rule gate: not needed — consumer-facing description of shipped behaviour; no method rule authored.

--- Build block ---
Changes: `plugin/throughliner/templates/faq-template.md` — the "Last session advises…" entry gains the replace-branch clause: a close filing its own advisory over a spent one replaces it, and read-clears-it covers only notes a close is not replacing. Then re-copy `FAQ/faq.md` and `FAQ/index.md` from the templates.
Acceptance: the FAQ entry states both clearing routes; FAQ/ matches the template byte-for-byte.
--- End build block ---
**Files:** `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

#### CLAUDE.md's folder-rename note says "renamed from `docs/` to `docs/`" — the old name is missing [claude-md-rename-note-lost-old-name]
Filed 2026-08-21 by Claude at a freeform close's wind-down, noticed while reading CLAUDE.md in full for the length cut. The Model target section's note about the 2026-08-21 folder rename gives the same path twice, so the sentence no longer says what the folder used to be called — the old name (`docs-b/`, per the installed plugin cache's layout) was presumably lost in an earlier edit.

**Kept 2026-08-22.** A one-line restore, not a deletion: the note is what explains why old records legitimately carry the old path, so it must keep saying what that path was.
Rule gate: not needed — restoring a lost word in a history note; no rule authored or amended.

--- Build block ---
Changes: `CLAUDE.md` — in the Model target section's folder-rename note, restore the old name so it reads "renamed from `docs-b/` to `docs/` on 2026-08-21".
Acceptance: the note names two different paths; nothing else in the sentence changes.
--- End build block ---
**Files:** `CLAUDE.md`.

#### A reversibility claim settled at processing was never checked against the world, and the build hit the exception [processing-asserts-reversibility-without-checking]
Filed 2026-08-14 by Claude at its own /done close, as a testing outcome from using the plugin to build the plugin. Host-only in its example, general in its shape.
**What happened.** [delete-codex-port-from-history] was settled at processing with a careful paragraph choosing the cheap operation over a history rewrite, recording that the cheap one "is also the reversible one" because dropped commits stay recoverable from the reflog until garbage collection. True of commits. The worktree being deleted held 722 lines of uncommitted work across 24 files plus two untracked files, none of which is a commit and none of which the reflog holds. The build halted, surfaced it, and the user chose to discard the work after being told plainly it couldn't be recovered.
**Why the processing session could not have known, and why that is the point.** Nothing in the keep-step asks a session to look at the thing it is about to destroy. The two-limb test asks whether the item says what changes inside the files it names — which this item did, precisely. A reversibility claim is a claim about the *world*, not about the item's specification, and the method has no check that reaches it.
**The shape it shares with other findings here.** [runs-alone-premise-never-tested], built in the same run, is the same failure one layer up: a plausible sentence about what git would or wouldn't recover, written at processing, quoted forward for days, refuted the moment anyone tested it. Two instances now, both about git recoverability.
**To settle at processing, and the obvious fix may be too broad.** A rule requiring every destructive item to inspect its target before clearing would fire on a great deal of work that destroys nothing. Weigh a narrower trigger: an item whose own prose *asserts* that an operation is reversible or recoverable earns a check of that assertion before it clears. That keys on something visible in the text rather than on judging what counts as destructive.
**Do not read the build's halt as the system working.** It worked because the build happened to run `git status` in the worktree before removing it, which no step required.

**Kept 2026-08-22, as an amendment rather than a freestanding rule.** The parent exists in plan.md's keep-step: "where an item asserts how a mechanism behaves, read the mechanism before describing the build — a capture's account of how something works is a claim to test, not a fact to build on." A reversibility assertion is exactly such a claim, about git rather than about the method, and both recorded instances are git-recoverability claims. So the fix is one sentence extending that clause, consuming no slot: an assertion that an operation is reversible or recoverable is such a claim, and the check is against the actual target — look at the thing about to be destroyed, not at whether the sentence sounds right. The broad alternative — inspecting every destructive item's target — stays refused as firing on work that destroys nothing.

Rule gate: run — amendment to the named keep-step parent; two recorded instances ([delete-codex-port-from-history]'s worktree loss, [runs-alone-premise-never-tested]) satisfy the has-it-failed-more-than-once test; nothing evicted, since the sentence extends an existing clause rather than adding a rule.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — extend the keep-step clause "where an item asserts how a mechanism behaves, read the mechanism before describing the build" with one sentence: an assertion that an operation is reversible or recoverable is such a claim, and checking it means inspecting the actual target (what would be destroyed and whether it is genuinely held elsewhere) before the item clears.
Acceptance: the clause reads whole with the new sentence; no new freestanding rule or heading is added; nothing else in plan.md changes.
Refused: a general inspect-before-clearing rule for every destructive item — fires on work that destroys nothing.
--- End build block ---
**Files:** `plugin/throughliner/docs/plan.md`.

#### The keep-step's research-index check restates the always-loaded Research rule at a second site [keep-step-index-check-restated]
Finding from [keep-step-accretes-from-five-items], approved 2026-08-21. plan.md's shelf question ("check resources/research/index.md for an entry covering this item's subject") restates the always-loaded rule "before offering a search, read resources/research/index.md" — two rules on one subject at two sites, the shape the law-prose pass hunts. A cross-reference from the keep-step to the always-loaded rule could replace the restatement. The audit judged every other keep-step clause correctly sited; this is the only merger candidate.

**Kept 2026-08-22 as the merger.** The keep-step keeps its what-is-on-the-shelf moment — that siting is right — and loses the restated instruction: the bullet becomes a cross-reference to the always-loaded Research rule, `subject to <X>` style, with the keep-step-specific clause (cite the file rather than restating it) kept since only it is new at that site.
Rule gate: run — merger under the eviction step; the always-loaded rule is the surviving statement, and plan.md's copy is what comes out.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — in the keep-step's two-questions block, reword the shelf bullet to point at the always-loaded rule ("run the always-loaded research-index check") rather than restating it, keeping the clause that a finding the reasoning draws on is cited by filename.
Acceptance: plan.md no longer restates the read-the-index instruction; the cross-reference names the always-loaded rule; the cite-the-file clause survives.
--- End build block ---
**Files:** `plugin/throughliner/docs/plan.md`.

#### The ordering ladder's fixed-at-opening medians were re-derived mid-session by the session that knows the rule [ladder-medians-re-derived-mid-session]
Filed 2026-08-22 by Claude at its own close, from the wind-down re-scan. Mid-session this planning run briefly ranked Unprocessed against a re-computed median (11 lines, from a re-run digest) instead of the medians fixed at the opening (10 lines), skipping two qualifying 10-line entries for a few picks before self-correcting. plan.md states the rule and its reason — a recomputed median lets the group stop shrinking — and the rule was in context and did not govern the pick. Joins the correctly-worded-rule-not-firing class (tenth instance); per that record, stating it harder is not a candidate direction.

**Kept 2026-08-22 on the quote-the-medians design.** One clause added to plan.md's floor narration: the narration quotes the two opening medians (line count and first-seen date). The noise cost is two numbers in a line that already fires every session; what it buys is that a mid-session re-derivation becomes a visible mismatch against a number already said out loud, rather than a silent substitution.
Rule gate: run — amendment to the floor-narration parent in plan.md's start-of-processing step; no freestanding rule, no slot spent.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — in the start-of-processing floor narration, add the clause that the narration quotes the opening medians the digest printed (section line-count median and first-seen median), which are the figures the ladder's membership stays fixed to for the whole pass.
Acceptance: the floor-narration text requires the two medians; the fixed-at-opening rule itself is unchanged.
Refused: sharper wording of the existing rule — tenth instance of the class where that does not work.
--- End build block ---
**Files:** `plugin/throughliner/docs/plan.md`.

#### A processed item carried its `Rule gate:` line twice, the second a truncated copy of the first [duplicate-gate-line-on-a-processed-item]
Filed 2026-08-15 by Claude at the close of the eighteen-item run, noticed while transcribing.

**What was found.** [move-section-does-not-report-line-crossings] carried two consecutive `Rule gate:` lines. The first read "not needed — this extends an existing report to a second code path and adds a refusal branch"; the second, the same without the refusal clause — evidently an earlier draft left in place when the item was revised. The build transcribed the fuller one once.

**Why it is worth a line.** The disposition is what two of the corpus checks read, and both take the line as authored. Two lines disagreeing about what the build does is a small inconsistency now and a wrong reading later — the truncated copy describes a narrower change than the item specified. It also suggests revision passes over a processed item append rather than replace, which would produce this again.

**What a keep would decide.** Whether anything mechanical should notice a duplicated disposition — the queue lint is the natural site and already parses work-item structure — or whether one instance is below the bar and this is a note about revising items in place. The bar question is real: one occurrence, which this project's own gate treats as insufficient for a freestanding rule.

**Kept 2026-08-22 as a lint check, on the user's stated preference for mechanisation.** The one-occurrence bar governs freestanding rules; the gate's own fourth question sends a failure to a hook where the hook costs no attention, and an advisory lint line costs none. The cause is structural rather than one-off — a revision pass over a processed item appends rather than replaces, so the shape recurs by default. The check is judgment-free: more than one `Rule gate:` line inside a single item block is a flag, whatever the lines say.

Rule gate: run — escalation to a hook rather than a rule; no method text changes and no slot is spent; the lint's advisory posture is unchanged.

--- Build block ---
Changes: `plugin/throughliner/hooks/post_tool_use.py` — the queue lint gains one advisory check: an item block containing two or more `Rule gate:` lines is flagged by slug ("duplicate Rule gate: line — keep the authored one"). `resources/testing/` — the lint suite gains assertions: two gate lines flag, one line does not, zero lines do not.
Acceptance: suite passes as a plain script via `py`; a hand-made two-line item flags; the lint still never blocks.
Refused: a rule in method text about revising items in place — one occurrence, below the gate's bar.
--- End build block ---
**Files:** `plugin/throughliner/hooks/post_tool_use.py`, the lint suite under `resources/testing/`.

#### The autonomous keep-step kept two rule-amending items without writing the gate disposition, and the next build halted on it [keep-step-skipped-gate-disposition]
Filed 2026-08-21 by Claude, on the user's report of the halt. The 2026-08-21 autonomous planning run kept [cut-length-everywhere] and [sent-record-surfaced-as-waiting-mail] — both amend the method's own rules — and wrote no `Rule gate:` line on either. The following /next run halted before locking scope, correctly, and the user had to intervene: the gate was then run in conversation and the two dispositions written onto the items. The halt worked; the keep-step did not. Relates to [rule-gate-dispositions-missing] (the check's hash timing) and [build-view-strips-the-gate-disposition] (the view not carrying the line).

**Kept 2026-08-22 as a lint check, the mechanical backstop.** Sharper wording was refused: the record holds ten instances of a correctly-worded rule not firing, and this run's own opening rule was in context when the keep-step skipped it. A plan-close check was refused as too late — /next can run the same day, before any close, which is exactly what happened. The lint fires at the write, before a run exists: a cleared item whose Files line names a gate-trigger path (`plugin/throughliner/docs/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md`, `resources/method-compliance-audit-checklist.md`, this project's CLAUDE.md) and whose block carries no `Rule gate:` line is flagged, same shape as the existing no-build-block flag. Consumer items never name those paths, so the check structurally never fires for them.

Rule gate: run — escalation to a hook; no method text changes; the trigger-path set is the gate's own, already enumerated in CLAUDE.md.

--- Build block ---
Changes: `plugin/throughliner/hooks/post_tool_use.py` — the queue lint gains one advisory check: an item above the cleared-to-run marker whose Files line names any gate-trigger path and whose block has no `Rule gate:` line is flagged by slug ("rule-touching item cleared with no gate disposition"). `resources/testing/` — suite assertions: cleared rule-path item without gate line flags; with gate line does not; a rule-path item below the line does not; a non-rule-path item without gate line does not.
Acceptance: suite passes via `py`; the lint still never blocks.
Refused: sharper keep-step wording (tenth-instance class); a plan-close check (fires after /next can already have run).
--- End build block ---
**Files:** `plugin/throughliner/hooks/post_tool_use.py`, the lint suite under `resources/testing/`.

#### An item whose described work is queue CONTENT can be cleared but never built, and nothing at the keep-step catches it [queue-content-items-are-unbuildable-by-a-run]

Filed 2026-08-21 by Claude, from a build run that met one.

**What happened.** [cut-length-everywhere] listed QUEUE.md among its files — "every item cut to its build block plus a short rationale". The scope-lock refuses a build any direct Edit or Write on QUEUE.md, by design: a build reads the generated view, and the only queue writes a run makes are the mover's per-item removal and an appended capture. So that limb of the item was unbuildable from the moment it cleared, and nothing said so until the run was already scope-locked. [lint-flags-its-own-scaffolding] had the same shape in its local half.

**Why the keep-step misses it.** The two-limb buildability check asks whether the item names its files and says what changes inside them. Both items passed: the files were named and the changes were described. The limb that does not exist is whether the named files are ones a build is *permitted* to write.

**The mechanical form, which is what makes this cheap.** The scope-lock's own refusal list is short and known — QUEUE.md is the only project doc a build cannot edit at all. An item naming QUEUE.md in its Files line is either a queue-content rewrite, which is planning work, or a mistake. Either way it should not clear to run.

**Worth checking whether the answer is a keep-step limb or a lint rule.** The queue lint already parses each item's build block, so a cleared item naming QUEUE.md could be flagged with no judgment at all — which would fire before a run ever locks scope. That is the cheaper site if it works.

**Not urgent.** The failure is visible and recoverable: the run halted, said so, and the user redirected. Nothing was silently skipped.

Relates to [cut-length-remaining-docs], whose remaining work includes the same queue limb, and to [keep-step-accretes-from-five-items] — which is a reason to weigh this against the keep-step's existing load rather than adding a sixth clause without looking.

**Kept 2026-08-22 as a lint check.** The keep-step clause was refused on [keep-step-accretes-from-five-items]'s ground: the lint fires with no judgment and no added planning load, and it fires before a run ever locks scope. The check: an item above the cleared-to-run marker whose Files line names QUEUE.md is flagged — queue-content work is planning work, and a build cannot write the queue. The known limit rides along from the digest's own: the check reads backticked paths on the Files line, and the existing convention already keeps exclusions off that line, so a flagged item is either a queue-content limb or a convention breach — both worth the flag.
Rule gate: run — escalation to a hook; no method text changes and no keep-step clause is added.

**Widened 2026-08-22 to absorb [audit-cannot-read-queue-prose], deleted the same day.** The check covers `[audit]` items too — an audit pointed at queue prose can't reach it from inside a run either, and reading queue prose is within /plan's own reach, so such an audit is in-session planning work rather than a queued item. The residual limit, stated: the lint reads Files lines only, so an audit scoped at queue prose solely in its rationale escapes — the same told-apart-by-reading limit the digest already records.

--- Build block ---
Changes: `plugin/throughliner/hooks/post_tool_use.py` — the queue lint gains one advisory check: a cleared item whose Files line names `QUEUE.md` is flagged by slug ("names QUEUE.md — a run cannot reach the queue; queue content is planning work"), whatever the item's flavor. `resources/testing/` — suite assertions: cleared item naming QUEUE.md flags; a cleared [audit] item naming QUEUE.md flags; the same item below the line does not; a cleared item naming other files does not.
Acceptance: suite passes via `py`; the lint still never blocks.
Refused: a sixth keep-step clause — planning-load accretion, and the lint fires earlier than a run.
--- End build block ---
**Files:** `plugin/throughliner/hooks/post_tool_use.py`, the lint suite under `resources/testing/`.

#### The shell-write guard sees neither the target nor the computation when a write's path is built by a call [shell-guard-blind-to-call-built-paths]

Filed 2026-08-21 by Claude, found while reproducing [shell-write-guard-blocks-the-scratchpad].

**The hole.** `open(os.path.join(d, 'x.md'), 'w').write(...)` passes the guard entirely. `structured_write_targets` returns nothing, so there is no target to check, and `has_computed_write_target` returns False, so it is not denied as unreadable either. The command runs.

**Why both halves miss it.** `PY_OPEN_WRITE_ANY` matches `open(` followed by `[^,()]+?` up to the mode argument. A path built by a call contains both a comma and parentheses, so the pattern does not match at all — and the computed check only fires on arguments it matched. The result is a shape that is neither literal nor computed as far as this code is concerned.

**Why it matters.** This is the exact failure the guard was written for. Its own docstring records that "a computed target slipped past an earlier version of this check and silently corrupted QUEUE.md, and the only difference from the version that was correctly blocked was one variable assignment." `open(p, 'w')` with a bare variable is correctly denied today; wrapping the same path in `os.path.join(...)` is not.

**Verified, not inferred.** Driven directly against the target hook: `targets=[] computed=False` for the join form, against `targets=[] computed=True` for the bare-variable form.

**Not fixed in that item's build,** because its described work was the disagreement between the guard and its own message — a raw-string literal being read as computed — and this is a different defect in a different function. Widening `PY_OPEN_WRITE_ANY` to tolerate nested calls needs its own design: the obvious `.+?` risks matching across unrelated arguments, which is the fragile general-parsing this module deliberately rejects.

Relates to [shell-write-guard-blocks-the-scratchpad], whose reproduction found it.

**Kept 2026-08-22, design settled at processing.** The fix is one additional regex used only by the computed-target check: it matches `open(` with an argument tolerating exactly one level of nested parentheses before the write-mode string, so `open(os.path.join(d, 'x.md'), 'w')` is seen — and anything it matches is computed by construction, since a call argument is never a quoted literal. One bounded nesting level is the whole widening; a doubly-nested call still escapes, and the docstring states that limit. The obvious `.+?` widening stays refused as matching across unrelated arguments.

Rule gate: not needed — hook code fix, no method rule text touched.

--- Build block ---
Changes: `plugin/throughliner/hooks/pre_tool_use.py` — add a pattern alongside `PY_OPEN_WRITE_ANY` matching an `open(` call whose first argument may contain one level of nested parentheses, followed by a write-mode string; `has_computed_write_target` also iterates its matches, treating any call-built argument as computed. Docstring states the one-level limit. `resources/testing/` — suite assertions: the `os.path.join` form is now computed=True and denied; the bare-variable form still computed=True; the literal form still passes; a read-mode `open` with a call-built path does not trigger.
Acceptance: suite passes via `py`; driving the hook directly shows `computed=True` for the join form.
Refused: widening `PY_OPEN_WRITE_ANY` itself with `.+?` — matches across unrelated arguments.
--- End build block ---
**Files:** `plugin/throughliner/hooks/pre_tool_use.py`, the suite under `resources/testing/`.

#### Walk-through steps do not travel into the build view, so a run cannot drive a `[user]` item [user-walkthrough-missing-from-view]
Finding from this run, approved 2026-08-21. The view prints "No build block — the run halts on it as underspecified" for a [user] item, and the run may not read QUEUE.md — but next.md's walk-through branch says to drive the steps "the item records", which live only in queue prose. This run reached [competition-comparison-article] and [discord-post-context-adjacency] with no steps available to drive.

**Kept 2026-08-22 on the view-carries-the-walkthrough design.** The alternative — letting the walk-through branch read the queue — was refused: it breaches the run-never-reads-the-queue design for one flavor, and the reasons that design exists (transcription into shipped docs, whole-queue reads) do not stop applying to [user] items. The mechanism mirrors the disposition carry: for a [user] item the view copies the paragraph led by the item's Walkthrough label byte-for-byte, keyed by slug; a [user] item with no walkthrough paragraph gets the honest line that no steps travelled and the run halts on it as underspecified, which the queue lint can already surface at authoring time.
Rule gate: not needed — script and procedure-doc plumbing for an already-decided lifecycle; no method rule authored.

--- Build block ---
Changes: `plugin/throughliner/scripts/generate_build_view.py` — for a [user] item, copy the block led by its Walkthrough label (bold or plain, `.` or `:` after the word) byte-for-byte into the view; where none exists, print that no walkthrough travelled and the run halts on the item. `plugin/throughliner/docs/next.md` — the walk-through branch names the view as where the steps come from. `resources/testing/` — assertions: a [user] item's walkthrough appears verbatim in the view; a [user] item without one gets the halt line; build items are unaffected.
Acceptance: suite passes via `py`; regenerating this queue's view shows both cleared [user] post items carrying their steps.
Refused: the walk-through branch reading QUEUE.md directly — breaches the run-never-reads-the-queue design.
--- End build block ---
**Files:** `plugin/throughliner/scripts/generate_build_view.py`, `plugin/throughliner/docs/next.md`, the suite under `resources/testing/`.

#### Audit-lag boundary matches a planning record named for the audit item, silencing the check [audit-lag-boundary-matches-processing-record]
Found on the audit-lag check's first run, in the build that added it ([standing-audit-programme]). The check's boundary is the newest LOG entry whose filename contains "compliance-audit" — but a planning session writes a record per item it processes, named for the item's slug, so 2026-08-22-post-restyle-compliance-audit.md (a processing record) satisfied the boundary before the audit itself had run. The check then reports rule-bearing commits as covered when they are not. The filename alone cannot tell an audit's record from a processing record of the audit item — the same told-apart-by-reading problem SPEC already records for the digest.

**Kept 2026-08-22 on the read-the-entry design.** The check opens each filename-matched entry and accepts it as a boundary only where the body carries the markers an audit record writes (the artifacts-read list); a processing record of the audit item lacks them and is passed over. Keying the boundary on a new artifact only an audit close writes was refused — a new format for one check to consume.
Rule gate: not needed — a check's own defect fixed in script code; no method rule touched.

--- Build block ---
Changes: `resources/rule_signals.py` — the audit-lag boundary reads each filename-matched entry's body and accepts only entries carrying the audit-record markers; where a filename matches but the body does not, the entry is skipped and the search continues older.
Acceptance: with the current LOG, the check no longer treats 2026-08-22-post-restyle-compliance-audit.md as the boundary; a genuine audit record still satisfies it; `py resources/rule_signals.py .` runs clean of errors.
Refused: a boundary artifact only an audit close writes — a new format for one consumer.
--- End build block ---
**Files:** `resources/rule_signals.py`.

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

**Lifted 2026-08-21.** [discord-post-cycle-awareness] was posted and closed — `INBOX/sent.md` records the send on 2026-08-21, for completion, with the posted text in that item's LOG entry — so the head of the pacing chain is done and nothing holds this item. Under the one-a-day pacing this post goes out no earlier than 2026-08-22; the walkthrough's drafting step is where the required third subject rewrite happens.

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
Blocked by: [cycles-definitions-and-due-checks]
**Files:** `CLAUDE.md`, the new cycles doc. The dependency is host-side: the checks that read the definition must ship first.

## Unprocessed

#### Last session advises processing [style-dedup-evictions] next [forward-advisory]
Filed at the 2026-08-22 planning close. The cleared region holds 21 items, ordered so the three always-loaded-file evictions build first, the hook and script work sits grouped by file, and the two Discord walk-through posts sit last — the ladder post goes out no earlier than 2026-08-23 under the one-a-day pacing, with its draft already in LOG/2026-08-22-discord-post-context-adjacency.md. A /next run works this region top-down; nothing unprocessed blocks it. The rezip planned for the evening of 2026-08-22 is still the gate on all deferred host-side verification — until it and a full app restart happen, committed host-side changes are not what the session runs, so nothing should be read as testing them. Unprocessed holds only held or waiting work: two date-held captures, one waiting on its named settler, and the marketplace/beta pair waiting on the community-listing update-cadence research and the user's go.

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

#### Every procedure doc ends on a terminal step, and none can tell finished from interrupted [procedure-docs-cannot-tell-finished-from-interrupted]
**Split from [rescan-does-not-hand-back] on 2026-08-21, on your decision**, once that item's three-file fix turned out to be fully specified while this half was not. The observation that started it is yours; the design question below is Claude's.

**What prompted it.** Claude Code's documentation says an invoked skill's content enters the conversation once and is never re-read, so *"write guidance that should apply throughout a task as standing instructions rather than one-time steps"* — see `resources/research/skill-content-lifecycle.md`. All five of this method's procedure docs are numbered marches ending in a final step, which is the shape that instruction warns against. /rescan is the confirmed instance: its terminal step reads as the end of the conversation's work.

**Your evidence, and it is what makes this a design question rather than a rewrite.** Asked whether the same property affects /plan and /next, you said it is a problem sometimes: **sometimes the session ends when planning or building is done, and that is correct**; and sometimes the skills need to be alternately run depending on the conditions — not normally, but sometimes.

**So the naive fix is refused before it is proposed.** "Stop ending" is wrong, because a terminal step is right in the common case. Rewriting five docs to end conditionally, with nothing able to read the condition, replaces a doc that always ends with a doc that guesses — and a guess reads as a decision, which is worse than a consistent ending someone can learn to work around.

**The actual question: can a procedure doc tell which case it is in?** Three candidate signals, none weighed yet. What the user last asked for, which is in the conversation and is what /rescan already reads to do its job at all. Project file state, which is what the scope-lock already uses — `pre_tool_use.py` decides a session is a planning one purely from the absence of this session's build working file, so file state is a proven readable condition. Or nothing, in which case the honest outcome is that each doc's ending states plainly what it does and does not know, which is the honest-limit route this project has chosen repeatedly over a check that over-claims.

**Why it cannot be kept yet.** The file list is the audit's own output, which fails the keep check's second limb by construction. What changes inside each doc depends on which signal survives, and no signal has been tested. **Do not schedule the design into the build** — an item whose prose defers a decision to the start of a run fails the same limb.

**What would settle it, and who owns each part.** Whether a doc can read its own situation is a fact to be established by reading `pre_tool_use.py`, `rescan.md` and the conversation-reading `rescan.md` already does — Claude's to find. Whether an honest "I don't know whether you were mid-something" ending is acceptable output is yours, since it is a decision about what the tool says to a user rather than about what it can do.

**Skipped 2026-08-21, settler named: process after [rescan-does-not-hand-back]'s fix has shipped**, since that build establishes what a corrected ending looks like and this design is cheaper read against a worked example. No date and no blocker line — it stays a capture because its file list is its own design's output.

**Runs behind [rescan-does-not-hand-back]**, which fixes the one confirmed instance. Placement carries that and this sentence carries the reason: no `Blocked by:` is written, because this could be designed independently — it is only cheaper afterwards, since that build establishes what a corrected ending actually looks like.

**Files (rough): not yet derivable, which is the point of not keeping it.** Likely `plugin/throughliner/docs/` across the procedure docs, and possibly nothing at all if the answer is that no signal exists. Shipped in effect: every consumer runs these docs. Relates to [plan-does-not-build-keeps-being-relitigated] and [standing-audit-programme], both of which record a doc's own wording teaching a later session the wrong thing.

#### The beta channel: each Wednesday's pick offered via Discord and a GitHub pre-release [beta-tester-pathway]
**Your idea, 2026-08-22, designed in the same session into a three-channel model — the standard release-channel shape (Chrome/Firefox), adopted on your terminology question.** Your day-to-day rezips are dev builds, yours alone and unchanged by this. Each Wednesday's pick becomes the **beta**: announced on the Throughliner Discord, hosted as a GitHub pre-release (Discord cannot host an install; the release ritual already builds and attaches zips), and offered to willing testers while it soaks for a week — you as the only tester at first, which is better than nothing and still a beta channel. After its week it promotes to **stable** and goes to the community listing ([marketplace-submission]). This superseded the earlier two-route question (repo-at-HEAD versus per-rezip artifacts): the weekly-pick artifact route won because it gives testers your chosen moments rather than every commit, and it reuses release machinery rather than adding a publish step to every rezip.
What a keep must still settle: the exact install walkthrough a Discord-recruited non-coder follows (marketplace-add against the repo at the pre-release tag, or zip download — must be scripted for the audience); how the beta offer is worded (honestly early, testing framing); and how this rides the [weekly-release-cycle] definition, since the Wednesday turn now produces two events — a new beta and a stable promotion. Waits on [weekly-release-cycle] conceptually and names no blocker; the design here is settled enough that a keep mostly writes the walkthrough.
**Your sequencing, 2026-08-22, revised the same day: the channels launch together rather than beta-then-listing** — the community listing is itself part of how testers arrive, so the chain is beta channel + community listing (honestly framed as early), then YouTube videos pointing at them. Written on both items per the known-ordering rule.

#### Submit Throughliner to Anthropic's community marketplace, as step one toward in-app browsability [marketplace-submission]
**Your goal, 2026-08-22: actual release to the Claude marketplace so people can browse for it inside the desktop app.** The research (`resources/research/claude-marketplace-listing-paths.md`) found two routes: the official marketplace is the only one browsable in-app by default, is curated at Anthropic's discretion, and has no self-serve path — the submission form feeds the community marketplace instead. So the realistic sequence is community first: submission via the clau.de/plugin-directory-submission form, automated security scanning plus human review, a public listing at claude.com/plugins pinned to a commit SHA; then official at Anthropic's discretion.
What a keep must settle: ending the pre-release posture CLAUDE.md declares ("in active testing, not ready for the Claude marketplace") — the user's decision; version-consistency discipline (plugin.json, changelog, git tags — the commonest reported rejection cause; the weekly release cycle [weekly-release-cycle] supplies the cadence for it, and a changelog does not yet exist); and confirming the name is final, since a marketplace slug is immutable once published and a rename breaks every install. The submission itself is a `[user]` step — a web form Claude cannot submit.
Runs behind [weekly-release-cycle] in spirit — a regular release rhythm is what makes the version discipline real — carried as this sentence rather than a blocker, since the submission decision is independently the user's.
**Reframed 2026-08-22, same session: the listing is the stable channel of the three-channel model settled on [beta-tester-pathway].** Each Wednesday the week-aged pick promotes to stable and updates the community listing. **Research needed before keeping, flagged rather than guessed at:** community listings are pinned to a commit SHA, and whether a weekly update is a lightweight refresh or re-enters Anthropic's review each time is unknown — the answer decides whether the Wednesday push to the listing is a one-minute step or a queue to wait in, and belongs in `resources/research/claude-marketplace-listing-paths.md` once found.
**Your sequencing, 2026-08-22, revised the same day: the listing launches alongside the beta channel rather than after it** — your first thought was beta testers before any listing, revised when it emerged the listing may be the only realistic way testers arrive; the listing is framed honestly as early instead. YouTube videos come after both, on your reasoning that videos without a listing would look bad to viewers while YouTube may bring the very first users. Written on both items per the known-ordering rule.

#### PowerShell text-splitting mangled queue appends — encoding not declared on the read [powershell-append-mojibake]
Filed 2026-08-22 by Claude at its own close. Mid-session, three appended queue items arrived with every em-dash as mojibake ("â€”"): a PowerShell step read a UTF-8 scratchpad file with `Get-Content -Raw` and no `-Encoding`, mangled the text, and wrote the mangled bytes back out through a correctly-UTF-8 write. Repaired in-session by a replace-all, verified clean by reading raw bytes per the existing check-`ascii()`-first rule. The existing scripting constraints cover subprocess reads and stdout reconfiguration but not PowerShell's own file reads; a /plan should weigh whether the constraint list gains a clause (every PowerShell file read of repo or scratchpad text names its encoding) or whether the instance stays a record — one occurrence, and the gate's bar applies.

#### A heading whose subject begins with a flavor tag reads as that flavor [heading-leading-tag-collision]
Filed 2026-08-22 by Claude at its own close. A build item's heading began "#### [user] walkthroughs do not travel…" — the tag was the sentence's subject, but the digest (and /next's routing) read the leading `[user]` as the item's flavor and classified a build as a walk-through. Caught at this close and fixed by rewording the heading; the slug is unchanged. Worth weighing whether anything mechanical should notice the shape — a `[user]`-flavored cleared item with no walkthrough paragraph is already a flag the view work ([user-walkthrough-missing-from-view]) will surface, which may cover this for free — or whether the fix is a one-line authoring note where headings are written.

