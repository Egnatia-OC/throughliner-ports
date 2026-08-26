# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Case D pop-out section carries no response-shape tags, and two of its steps wait on the user [setup-case-d-untagged]
From the compliance audit of the rule changes since 3ed3db1, lens 2 (tag placement).

`setup.md`'s Case D section (around lines 107 to 140) was added since the last audit and carries no tag on any step. Two of them stop for the user: reading the parent's SPEC and putting the inferred subpart to them in clarifier form, which fires at the very start of adopting a subfolder and cannot proceed without their answer; and drafting the pop-out message to the parent's INBOX, which fires at the close and is shown in full before an explicit yes. Both are `[PROMPT]` moments by the definition in the always-loaded rules.

Case B's peek — the sibling this section says it copies — is tagged. Untagged, the output behaviour of a step that must wait is left to chance, which is the missing-tag failure the lens names.

**Kept 2026-08-26 at the next planning session, on Claude's recommendation and your agreement.** A compliance correction, nothing designed: the two waiting steps get [PROMPT] (the send step keeping its show-first shape), the rest tagged to match Case B's register.

**Widened 2026-08-27, your decision, resolving the collision the 2026-08-26 build halted on:** setup.md's opening declares the doc tag-free while five steps carry tags — it says one thing and does another. Your call between the two coherent fixes: repeal the declaration and tag the whole doc properly. The declaration's reason is weaker than it looks — on a fresh-adoption run, where the tag definitions are not loaded, a tag is inert rather than wrong — and the tags keep creeping in because editors follow the method-wide habit, so the declaration fights the grain of every future edit. Half-tagged is the worst of the three states. This absorbs the capture the halt filed, deleted with this rewrite.

Rule gate: run — repeal of setup.md's tag-free declaration (evicted in this build) plus compliance tagging; no new rule authored.

--- Build block ---
Changes: `plugin/throughliner/docs/setup.md` — the tag-free declaration in the opening (around line 20) comes out; Case D (around lines 107–140): [PROMPT] on the confirm-the-subpart clarifier and on the pop-out INBOX message step, the section's remaining steps tagged to match Case B's register; the rest of the doc's steps reviewed and tagged consistently under the always-loaded tag rules, any conditional arm written with the condition outside the brackets; the five existing tags kept where correct.
Acceptance: no declaration of tag-freeness remains; no step that waits for the user is untagged; tag syntax matches the always-loaded tag rules; no step's substance changed.
Refused: honouring the declaration and stripping the five existing tags — labels are harmless where unread, and the declaration loses to the editing habit that keeps violating it.
--- End build block ---

#### Sessions derive "today" by assumption — anchor the date at session start and bar own date arithmetic [session-date-anchor]
Raised by you 2026-08-26, on catching a live instance: after an app restart mid-chat, Claude assumed a new day, dated a fresh capture 2026-08-27, and read a post item's `Not before: 2026-08-27` as arrived — nearly walking a post a day early against the one-a-day pacing. Your framing: this comes up constantly, mostly in little ways but sometimes in big ways. The digest had already computed that date as a day ahead; the session did its own arithmetic on an assumed "today" instead of reading the computed field.

**Kept 2026-08-26, on Claude's recommendation and your agreement.** Two halves plus the SPEC clause (written at this keep): a mechanical anchor every session opens with, and an always-loaded rule that date decisions read computed fields rather than deriving today. The rule goes through the rule gate at the build; its admission case is recorded here — it fires in every skill and in plain conversation (the miswritten capture date sat in no date field), which is the skill-nonspecific admission test.

Rule gate: run at this keep for the SPEC clause and the design — the always-loaded rule itself is authored at the build from this disposition; it amends the session-opening facts' read-as-inputs framing rather than standing free, and the build names what it displaces or that nothing is evicted.

--- Build block ---
Changes: `plugin/throughliner/hooks/session_start.py` — emit one fact line with today's date read from the system clock, worded as the date at session start (a long chat can cross midnight). `resources/testing/` — a suite case asserting the line appears and carries a real date. `plugin/throughliner/docs/skill-nonspecific-rules.md` — one rule: where a decision turns on a date, read a computed field (the digest's passed/ahead, the session opening's date line); where none exists, read the clock; never derive "today" by assumption. Written as an amendment where a parent rule fits, freestanding only if none does.
Acceptance: the hook's payload carries the date line and the suite passes; the rule reads in one of the three admissible shapes; SPEC's session_start sentence (already edited at this keep) matches the shipped behaviour.
Refused: fixing only the instance (correcting the two wrong dates) — the user reports the failure recurs across sessions, so the fix belongs at hook-plus-rule level, not at the instance.
--- End build block ---

#### Captures may name an open queue item that stops them being offered [capture-blocked-by]
Raised by you 2026-08-26, from the live instance minutes earlier: [cycles-mermaid-diagrams] waits on [weekly-release-cycle]'s build and has no way to bow out, so it returns every session and is skipped again — your framing: the problem is the noise of not-ready items coming up. A new ladder rung was considered and refused: the ladder orders, it cannot hide. The `Not before:` date cannot reach this case either — its outside-the-project restriction exists because an in-queue wait has a checkable fact a date only approximates.

**Kept 2026-08-26, on Claude's recommendation and your agreement.** On a capture, `Blocked by: [slug]` means don't offer this while any named blocker is open — the planning pass skips it silently, as it already does a future-dated capture, and when every blocker resolves the capture re-enters the ordinary order with no note (your choice, recorded). This mirrors `Not before:`, which already means a different thing per section. The ripple was traced by grep, naming the enforcing hook: `post_tool_use.py`'s lint ties the field to the held region; `session_start.py`, `queue_digest.py` and four docs also read or describe it. `done-plan.md` and `setup.md` mention the field but describe held-region behaviour that stays true — excluded from the change. First candidate once shipped: [cycles-mermaid-diagrams] gains `Blocked by: [weekly-release-cycle]`.

Rule gate: run — supersession of the field-belongs-to-the-held-region-alone clause, for this one added meaning; the old rule loses because it left in-queue waits with no bow-out, which the refused skip-marker design never addressed. Amendment to the existing Blocked-by rules, nothing freestanding.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the capture line-format's `Blocked by:` comment gains the capture meaning (don't offer while a named blocker is open), written as the per-section split `Not before:` already uses. `plugin/throughliner/docs/plan.md` — the ranking pass-over extends to captures whose named blocker is still open, silent like the date pass-over. `plugin/throughliner/hooks/post_tool_use.py` — the lint accepts the field on a capture and validates its slugs resolve, instead of reading it as misplacement; suite cases added under `resources/testing/`. `plugin/throughliner/scripts/queue_digest.py` — capture lines print the named blocker's resolved state, so the skip is checkable.
Inputs: `plugin/throughliner/hooks/session_start.py` — confirm its blockers-still-in-Unprocessed count is not distorted by a capture carrying the field; edit only if it is.
Acceptance: lint suite passes with a blocked capture accepted and a bad slug flagged; the digest prints the blocker state on such a capture; the docs read per-section, matching the `Not before:` shape.
Refused: a new ladder rung — rungs order, they cannot hide. A `Not before:` date for in-queue waits — a date guesses what the queue can check. A surfaced-with-note return — the user chose silent re-entry.
--- End build block ---

#### Warn, don't enforce: a direct do-it-now request gets one warning turn, then the work [warn-dont-enforce-immediate-requests]
Raised by you, filed 2026-08-27 from the audit finding [walkthrough-answers-request-with-sequencing], which this keep closes: you asked four times for two approved Discord drafts and the first two answers enforced the posting brief's sequencing at you instead of handing them over — and you were not even out of order: `[user]` items surface during a build run, you were collecting the drafts to post after the release, and the release can only run after the close since a session's one commit is the close's. Your principle, extended by you at processing: this covers any do-it-now request — unplanned work, out-of-order work, anything — the warning fires and then the work commences.

**Kept 2026-08-27, on your direction; the turn shape is yours too.** The rule: when the user asks for anything to be done immediately, the session answers with one warning turn — what standing rule or ordering the request crosses and what that risks, plus a briefly-worded alternative to doing it now — and stops there; on the user's next word the work runs; the work and the warning both land in the session's record, so a later reader can see the rule fired and was overridden. The warning never substitutes for the work, and the warning turn is standalone — never bundled with the work, so the user can withdraw. Carve-outs stated so the rule cannot widen into them: anything leaving the machine keeps the exact-text yes, and unrecoverable destruction keeps its ask. Skill-nonspecific by your direction, and it passes the admission test on its face: a do-it-now request can arrive in any skill or in plain conversation.

Rule gate: run — authored freestanding after a parent was looked for and not found (the repeated-request rule in the run's procedure covers scope growth, not compliance-vs-enforcement); the recorded failure earning the slot is the four-ask instance in the 2026-08-26 build transcript; the build names what it displaces or that nothing is evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the rule above added in an admissible shape (bold-led paragraph), stating: one standalone warning turn naming what the request crosses, the risk, and a briefly-worded alternative to doing it now; work commences on the user's next word; work and warning logged in the session's record; carve-outs for off-machine sends (exact-text yes stands) and unrecoverable destruction, written as subject-to cross-references, not restatements.
Acceptance: the rule reads in one of the three admissible shapes; the warning turn and the log requirement are both operative text; the carve-outs cross-reference the existing rules rather than restating them.
Refused: warn-and-comply in the same turn — the user's decision: the warning is standalone so the request can be withdrawn. Enforcement of any non-carve-out rule against a direct request — the failure this rule exists to end.
--- End build block ---

#### Walk-through presents every [user] item it reaches — no outside precondition filter [walkthrough-no-batch-precondition-skip]
Filed from the ordering-rigidity audit of the 2026-08-26 build session: the run's walk-through pass reached six `[user]` items, drove two, and dropped four without presenting any — its own words: "every one of them opens on a step conditioned on the release being published." No rule licenses that filter. This is the mechanism under the withheld-drafts finding, and it fired before the user had complained about anything — the earlier and more general defect of the two. The record-keeping sibling — what got written afterwards — is [walkthrough-outcome-not-reached], processed 2026-08-27 from the capture this sentence used to name.

**Kept 2026-08-27, on Claude's recommendation and your agreement.** The rule composes with [warn-dont-enforce-immediate-requests] rather than duplicating it: that one governs answering the user's direct requests; this one governs the run's own conduct unasked.

Rule gate: run — amendment to next.md's walk-through branch, parent named; no freestanding rule and nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/next.md` — walk-through branch: every `[user]` item the pass reaches is presented, one at a time; a precondition is tested inside the item's own drive, never applied as an outside filter that batches items away; where a drive's first step cannot proceed, that fact is shown to the user on that item's turn and their word settles it.
Acceptance: the branch's text carries the present-every-item rule and the inside-the-drive precondition rule; no step's existing substance changed.
Refused: a precondition field on items the run could evaluate mechanically — it recreates the outside filter with a schema, and the decision belongs in front of the user.
--- End build block ---

#### Walk-through outcomes get three values — done, deferred, not reached — and "deferred" only from the user's word [walkthrough-outcome-not-reached]
Filed from the ordering-rigidity audit of the 2026-08-26 build session: records wrote "all six user steps deferred in place" when the user deferred two and the other four were never presented. "Deferred" is an origin claim crediting the user with a decision they were never asked to make — the provenance rules' problem appearing in session records — and it bit the same day: a later walk-through believed a wrong "deferred" line and re-presented finished work — that failure's resolution is [completion-ask-carveout-post-close-handover], processed 2026-08-27.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** The outcome vocabulary: driven to its end (done); deferred (only where the user said so); not reached (the run ended before presenting it — a fact about the run, not the user). "Not reached" is what a later session needs: present the item fresh rather than resume a decision nobody made. Composes with [walkthrough-no-batch-precondition-skip]: with both shipped, not-reached only ever means the run genuinely ended first.

Rule gate: run — amendment to the walk-through branch's outcome recording and the close's record writing; parents named; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/next.md` — the walk-through branch's outcome recording carries the three outcomes, with "deferred" written only from the user's own word. `plugin/throughliner/docs/done.md` (and its build-close doc where records are written) — the close's record writing carries the same three values, so a record cannot say deferred of an item the run's trail shows was never presented.
Acceptance: both docs name the three outcomes; "deferred" is tied to the user's word at both sites; the not-reached value tells a later session to present the item fresh.
Refused: a completion ask to disambiguate — the no-completion-asks bar stands; the vocabulary removes the need to ask.
--- End build block ---

#### Release ritual opens the queue item that scheduled it and writes its record at the end [release-ritual-opens-its-record]
Filed from the release-failure trace over the 2026-08-26 sessions: the v1.21.0 ritual ran after /done had committed, [expedite-first-beta-release] was never opened at the moment it mattered, and its final steps executed with no record under its slug. The general shape: work running outside a skill reads no queue item, so the queue's record of what was decided has no reader.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** The capture's alternative — barring a release after the close — loses on structure: post-close is effectively the only slot a release has, since the ritual makes its own commit and a session's one commit is the close's. So the ritual gains its own record discipline instead. Host-only: consumers have no release ritual.

Rule gate: run — amendment to the release ritual's steps in a host-only fetched doc; no method rule authored, nothing shipped.

--- Build block ---
Changes: `resources/release-ritual.md` — Release section gains an opening step: search the queue for an item that scheduled or constrains this release; where one exists, read it in full and run against what it says. And a closing step: write the session record under that item's slug — LOG entry plus index line — and close or update the item, so post-close release work leaves the same trail as any walked item.
Acceptance: the Release section's first numbered step is the queue read and its last is the record write; both say what happens when no scheduling item exists (proceed, and record under a plain release entry).
Refused: barring a release after the close — post-close is structurally the only slot. A hook to detect an unrecorded release — the ritual is fetched-on-demand host tooling; a hook cannot see "a release is happening".
--- End build block ---

#### "As planned" phrases resolve by reading the record, and a release compares stamps before packaging [as-planned-reads-the-record-and-stamps]
Filed from the release-failure trace over the 2026-08-26 sessions: the instruction was to release "this currently installed version… as planned" — installed was 1.20.0-test20 — and what shipped as v1.21.0 was the working tree, test20 plus two doc fixes never packaged or run anywhere. Two failures met: a phrase pointing at a recorded plan was accepted without the plan being opened, and the release was cut from the working tree rather than the artifact named.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** **Your invariant, stated in this item because you had to correct the session twice to land it (2026-08-27, absorbing the deleted capture on the dissolved soak step):** a release releases a tested rezip — never an untested build — and rezips do not imply releases: a release runs only on your ask. The ritual as written packages the working tree as it stands, which is the mechanical reason the invariant could break silently (v1.21.0 shipped test20 plus two unrun fixes); edits landing after the tested rezip belong to a current or future rezip, not to the release. The stamp step below is what turns your invariant from an assumption into an enforced fact, and the ritual's text must state plainly that it packages the tree and that this step is the invariant's guard. Two fixes of different kinds. Mechanical: the ritual compares the content stamp of what is about to be released against the installed host's stamp before packaging; where they differ, one standalone warning turn says the release would ship code nobody has run, and it proceeds on the user's word — the warn-don't-enforce shape applied at the point it was missed. Reading: the Prior decisions retrieve gains one clause — an instruction referencing a recorded plan by phrase ("as planned", "as agreed", "like we discussed") is resolved by reading the record before acting, never from memory of it. Composes with [release-ritual-opens-its-record], which makes the release case's record findable at the ritual's top.

Rule gate: run — the reading clause is an amendment to the always-loaded Prior decisions rule, parent named, admission earned by this recorded failure; the stamp step is host-only ritual text, no method rule.

--- Build block ---
Changes: `resources/release-ritual.md` — Release section, before the repackage step: compare content_stamp() over `plugin/throughliner` against the installed host's stamp; where they differ, one standalone warning turn stating the release would ship code nobody has run, proceeding only on the user's word. The section also gains two plain sentences: a release releases a tested rezip, and the packaging reads the working tree as it stands — so the stamp step is the invariant's guard, and edits landed since the tested rezip belong to a current or future rezip, never silently to the release. `plugin/throughliner/docs/skill-nonspecific-rules.md` — Prior decisions: one clause added — a user instruction that references a recorded plan by phrase is resolved by reading the record before acting.
Acceptance: the ritual carries the stamp comparison ahead of packaging with the standalone warning turn; the Prior decisions rule carries the clause in an admissible shape; no other rule text changes.
Refused: blocking a mismatched release outright — warn-don't-enforce governs; the user may knowingly release the working tree. Detecting "as planned" mechanically — it is a reading discipline; no hook can parse intent.
--- End build block ---

#### Uncommon execution markers are assigned only against their re-read definition [uncommon-flavor-definition-check]
Filed from the ordering-rigidity audit of the 2026-08-26 planning session: Claude recommended tagging the release pick `[freeform]` and placing it last in the cleared region, and the user corrected it twice — "freeform implies seperate run. I want to just be able to pick at the end of the next build", "freeform always runs alone" — both statements being what the docs already say. The definitions were loaded, so this was a slip, but of a repeatable kind: `[freeform]` and `Runs alone` are rare, similar-sounding, and the pair that got confused — a rarely-used tag is the one a session misremembers confidently. A flavor is settled at the disposition step and decides where work can run, so a wrong flavor is an ordering mistake at the one moment ordering is settled.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Your sharpening of the distinction, rendered here, travels into the clause: `[freeform]` runs alone in the sense of running *without the method* — a skilless work item done by hand, for whatever unforeseen reason, outside any /next run; `Runs alone` is method-governed work /next builds in an isolated run of its own. The check: before assigning either marker, re-read its definition in that turn and name in the recommendation why the work matches it — a sentence that is unwritable for a marker being misapplied.

Rule gate: run — amendment to plan.md's disposition step, parent named; admission earned by the recorded double correction; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the disposition step: one clause requiring that an uncommon execution marker (`[freeform]`, `Runs alone`) is assigned only after its definition is re-read in that turn, with the recommendation naming why the work matches it; the `[freeform]`/`Runs alone` contrast sentence updated to carry the without-the-method vs isolated-method-run distinction.
Acceptance: the disposition step carries the clause; the contrast sentence states the distinction in the sharpened form; no marker's meaning changes.
Refused: dropping it as a recorded slip with no build — the clause is one line and the failure cost the user two corrections at the ordering-settling moment.
--- End build block ---

#### Queue mover runs are confirmed from the tool's report before continuing — no blind retries [mover-report-confirmed-before-continuing]
Filed from the ordering-rigidity audit of the 2026-08-26 planning session: the mover was run three times to place the readiness marker, with the usage read only after two wrong placements. The verify-before-handing-over rule deliberately excludes commands Claude runs itself — a wrong flag costs one turn and self-corrects — and that reasoning holds for read-only commands but is weaker for a tool that rewrites the queue in place, where a wrong placement is a silent edit to the file the whole method reads.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** The actual failure was retrying blind: the mover announces what it did ("marker now sits after X"), and both wrong placements were announced and unread. The clause targets that rather than taxing every routine move: after every mover run, read its report and confirm the marker's stated position matches the intent before continuing; where it does not, open the tool's usage before any second attempt — never trial-and-error against the live queue. The general verify rule's hand-over scope is untouched, as the capture itself wanted.

Rule gate: run — amendment to plan.md's mover guidance, parent named; the general verify rule unchanged; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the mover guidance (where its forms and the marker hazards are documented): one clause — read the mover's report after every run and confirm the marker's stated position matches the intent before continuing; on a mismatch, read the tool's usage before any second attempt.
Acceptance: the clause sits with the existing mover guidance; the verify-before-handing-over rule's text is untouched.
Refused: read-the-usage-first on every mover run — taxes routine moves the report already confirms. Widening the general verify rule — the capture's own boundary.
--- End build block ---

#### Walkthroughs name where each stored text lives, and a verification step lists the claims it checks [walkthrough-artifacts-named-and-verify-enumerated]
Filed from the ordering-rigidity audit of the 2026-08-26 build session: asked for the first test-rezips channel entry, the session showed the pinned welcome text instead — caught by the user — and the actual queued draft claimed the entry was "cut from [rezip name]", which would have read as the release being test20 when it was test20 plus two later fixes. The item's re-verification step had run, but only over timing claims, so neither error was reached.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Both lessons extend the existing walkthrough-authoring requirement (each step names the thing to do and the thing to look for): where a walkthrough involves more than one stored text, each is named where it lives — which file, which item — so a request for one resolves to an identified artifact; and a verification step enumerates the claims it checks — the claims list is that step's thing-to-look-for, and a step without one silently checks whatever lens gets picked.

Rule gate: run — two clauses amending the walkthrough requirement in skill-nonspecific-rules.md, parent named; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the walkthrough-carrying requirement gains two clauses: a walkthrough involving more than one stored text names where each lives; a verification step lists the claims it checks.
Acceptance: both clauses read as subordinate units of the existing requirement; plan.md needs no change (it applies the requirement by reference).
Refused: a separate verification-step rule — it is the existing thing-to-look-for requirement applied, so it amends rather than stands free.
--- End build block ---

#### Checkpoint carries the remaining-to-process count [checkpoint-carries-remaining-count]
Raised by you 2026-08-27, mid-session, with the wording that settled the shape: the disposition line "might more usefully have read 'Processed and cleared as [slug] — 20 ready. X yet to be processed.'" The shipped checkpoint bans a count outright ("no menu of routes, no count, no tally"), a de-cluttering decision aimed at the four-route recital; the count it also swept out is the one number the user paces the session with, and you had to ask for it.

**Processed 2026-08-27, cleared to run, on your direction.** The checkpoint's message shape gains one element: the remaining-to-process count, stated as plain arithmetic ("5 yet to be processed"), with dated and skipped entries excluded since they are not offered. The no-count clause is narrowed to what it was aimed at — no tally of dispositions so far, no menu — and the build names that supersession.

Rule gate: run — amendment to plan.md's checkpoint shape; the no-count clause narrowed and the narrowing recorded as a supersession with this instance as its ground.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the checkpoint's message-order block gains the remaining-to-process count as its own element (dated and skipped entries excluded); the "no count, no tally" line narrowed to bar the disposition tally and route menu only; the checkpoint specimen updated to show the count.
Acceptance: the specimen ends with the count; the narrowed clause still bars tally and menu; no other checkpoint element changes.
Refused: a full progress tally (done/deleted/skipped so far) — the clutter the original ban was for.
--- End build block ---

#### Audit findings file straight to Unprocessed, marked not yet reviewed — the write-time approval is repealed [audit-findings-file-unapproved]
Captured by you during the 2026-08-26 ordering-rigidity audit, on seeing the same findings put to you twice: the audit shows every finding as one numbered set and waits for approval before filing, and /plan then evaluates each again at processing — the identical material assessed twice, once with no queue context and once with it. Your direction: findings are written straight to Unprocessed marked as not yet reviewed, the run carries on without waiting, and the single evaluation happens at /plan, where Claude gives a heads-up that the capture came from an audit. Consistent with write-first: a finding is doc-resident and recoverable, so the recoverability test answers yes.

**Processed 2026-08-27, cleared to run, on your direction.**

Rule gate: run — repeal of next-audit.md's present-and-wait step and contested-findings pass, with the bulk-approval inversion's audit example evicted in the same move; the mark is a prose convention the disposition step reads, not a new parsed field.

--- Build block ---
Changes: `plugin/throughliner/docs/next-audit.md` — the present-and-wait step and the contested-findings pass are repealed; findings file directly to Unprocessed, each capture carrying a prose provenance line ("from the <name> audit, not yet reviewed"). `plugin/throughliner/docs/skill-nonspecific-rules.md` — the bulk-approval inversion's example list drops "an audit's findings", since the set no longer waits for approval. `plugin/throughliner/docs/plan.md` — the disposition step: a capture carrying the audit mark is introduced as unreviewed audit output, so the user's single evaluation happens knowingly.
Acceptance: next-audit.md contains no approval wait; the inversion example is gone; plan.md carries the heads-up clause; a grep for the repealed step's distinctive words returns nothing shipped.
Refused: keeping a light confirm before filing — it recreates the double assessment the user pointed at. A parsed not-reviewed field — a prose line the disposition step reads suffices, and a new field needs machinery nothing else wants.
--- End build block ---

#### Suite runner discovers and runs every test, and the ritual's stale three-suite step points at it [testing-suite-runner-discovers-all]
Noticed while checking `resources/release-ritual.md` during the piped-exit-code build: its suite step invokes `python` — which this machine resolves to Inkscape's bundled interpreter, the exact trap the scripting constraints name (`py` is the rule) — and it enumerates three suites when `resources/testing/` holds about twenty, so the release's stop-on-failure gate covers a shrinking fraction and reports a pass over suites it never ran.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Discovery replaces enumeration: a standard-library runner finds every test script in the folder and runs each as a plain script, exiting non-zero on failure, so new suites are picked up automatically and the instruction can never go stale. CLAUDE.md's hook-touching close rule already says "the suites under resources/testing/" without naming them — excluded, no edit. Host-only: consumers have no test suites.

Rule gate: run — the enumerated list in the ritual is superseded by the runner call; no method rule authored; host-only ritual text.

--- Build block ---
Changes: `resources/testing/run_all.py` — new, standard library only with the UTF-8 reconfigure block, discovers every test script in `resources/testing/` (the .py suites, not transcripts or fixtures), runs each as a plain script via `py`, prints per-suite results, exits non-zero on the first failure. `resources/release-ritual.md` — the rezip's suite step and the release's suite step both changed to `py resources/testing/run_all.py`, replacing the three named suites and the `python` invocation.
Acceptance: the runner run by hand reports every suite in the folder and passes; both ritual steps invoke it with `py`; no ritual step names an individual suite.
Refused: keeping an enumerated list — it goes stale every time a suite is added, which is the recorded failure. pytest — barred by the scripting constraints (Inkscape's python has no pytest and the error misleads).
--- End build block ---

#### Walkthroughs end at the item's observable, and a step in another project is filed, never driven [user-item-ends-at-observable-cleanup-separate]
Captured by you in the moment — your word for it: infuriating — during the 2026-08-26 build run's walk-through of the cycles verification. Steps 2 and 3, the whole verification, had passed, confirmed from the world; step 4 was fixture cleanup in a different project, and the run handed it over as the next step — leave the build, open a chat elsewhere, do housekeeping, come back — for work the build neither needed nor waited on. Two further exchanges went on what "the fixture" meant (that half was processed as [general-jargon-translate-and-walkthrough-readback]). Your framing: this must not happen to consumers — a non-coder walked out of their build into a second project to delete a test artifact has been handed the method's internals as a chore.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Two rules, one per defect. Authoring: a `[user]` item ends at its observable — once the thing it names has been seen, the item's purpose is served; tidy-up after the test is separate work, filed as its own item and ordered like anything else. Run-time: a step requiring action in another project is never driven inside a run — it stalls the run by construction, since no session touches another project's files — the run files it and moves on.

Rule gate: run — two amendments: the walkthrough-authoring requirement in skill-nonspecific-rules.md (ends-at-observable, cleanup separate) and next.md's walk-through branch (another-project steps file rather than drive); parents named; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the walkthrough-carrying requirement gains: a `[user]` item's walkthrough ends at the item's observable, and cleanup after the test is filed as its own item rather than written as trailing steps. `plugin/throughliner/docs/next.md` — the walk-through branch gains: a step requiring action in another project is not driven; the run files it as a capture and continues.
Acceptance: both clauses sit with their parents in admissible shapes; the run's branch names filing as the route for another-project steps; no existing step's substance changes.
Refused: keeping cleanup steps but driving them last — the stall is the leaving-the-project, not the ordering. A cross-project write to do the cleanup for the user — no session writes another project's files, standing rule.
--- End build block ---

#### Completion-ask carve-out for work handed over at a close with no reachable observable [completion-ask-carveout-post-close-handover]
Resolves two audit captures processed together 2026-08-27, their facts carried here. A run re-presented two Discord drafts the user had already posted — "they've already been posted why are you presenting them to me?" — because the item's only record said "deferred", written before the posting, and nothing running afterwards could correct it. The walk-through behaved correctly and the record lied to it. Minutes later the same run, against the no-completion-asks bar, asked whether the next post item was done — and that produced the day's best outcome: a screenshot, the register written from the posted text, the item closed. So the corpus held a rule barring the cheap fix, a recorded disaster from obeying it, and a recorded success from breaking it. Of the three routes weighed, the records fix is shipped ([walkthrough-outcome-not-reached]) but cannot help lines already wrong or work done after a close; /rescan works only if the user runs it, and the failing case is a chat already closed. The general bar stays — "have you done this one? and this one?" down the queue is worse than either recorded failure — and the deleted captures' warning against softening it generally is honoured by the keying.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** The carve-out keys on two recorded facts together: the item's own record shows it was handed to the user for completion after the close, AND it names no observable the method can reach. Only then, at the moment the item would otherwise be re-driven, one ask — "the record says this was handed to you to do after the close; where did it land?" — instead of re-presenting the work. An item without a recorded hand-over never qualifies, which is what stops the carve-out widening into a sweep. SPEC's no-completion-asks paragraph gained the sentence at this processing.

Rule gate: run — an exception to the no-completion-asks rule, taken through the restatement test: the bare rule cannot be restated to cover this case because all three inference routes (walked to the end, user volunteers, observable check) are shut by construction; the admitting instances are the re-presentation failure and the successful barred ask, both in the 2026-08-26 build transcript.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the `[user]` walk-through lifecycle: the carve-out added beside the completion-inference routes, keyed on the two recorded facts, with the one-ask wording. `plugin/throughliner/docs/next.md` — the walk-through branch's open-the-record step: where the record shows a post-close hand-over and no reachable observable, the drive is replaced by the one ask.
Acceptance: both sites carry the carve-out with its two-fact key; the general bar's text otherwise unchanged; SPEC's sentence (already written) matches.
Refused: softening the bar generally — worse than either recorded failure. Relying on /rescan — the failing case is a closed chat. A notification or watcher — mail is fire-and-forget, standing refusal.
--- End build block ---

#### Developer and testing vocabulary joins the translate-away list, and walk-through steps are read back for it [general-jargon-translate-and-walkthrough-readback]
Noticed at the close of the 2026-08-26 build run, on the user's asking: walking the cycles verification, the run wrote "the fixture has done its job" and "if you'd rather have the fixture gone" into a step being handed over, and the user had to ask — "what is 'the fixture'?" — costing two exchanges mid-step, the worst place for a vocabulary lesson by the rule's own halt-and-stop clause. A gap rather than a slip, on the capture's two grounds: the rule's offender list is method vocabulary, and "fixture" is ordinary testing vocabulary a session may not recognise as jargon; and the walk-through branch is where the reader is most reliably a non-coder performing an unfamiliar action.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** Sits beside [shared-vocabulary-not-standing-names] without tension: method terms are the shared language, but "fixture" is not a method term and names nothing in the user's files, so it stays on the translate side.

Rule gate: run — two amendments to named parents: the vocabulary rule's in-passing list gains the general developer-and-testing class, and the walk-through branch gains the read-back clause the halt-text clause already models; nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the vocabulary rule's translate-in-passing list gains general developer and testing vocabulary — terms naming nothing in the user's own files — with "fixture" as the recorded specimen. `plugin/throughliner/docs/next.md` — the walk-through branch: a step being handed over is read back for such terms before it goes out, the halt-text check extended to hand-over steps.
Acceptance: the list carries the class and specimen; the branch carries the read-back clause; the explained-once arm and the shared-vocabulary rule are untouched.
Refused: enumerating banned words — the class is open-ended; the test is whether the term names anything in the user's files.
--- End build block ---

#### README marks LOG/ and resources/ as historical records [readme-marks-history-folders]
Surfaced by /rescan 2026-08-27, from your report that Gemini, asked to make presentation items from the repo, keeps describing BACKLOG.md as though it still exists — it was reading old records and archives as current truth. The one live mention aside (the ADHD-article seed, which already flags it as a defect to fix), "BACKLOG.md" survives only in history: LOG entries, research files, and the frozen archive folder next door. Any whole-repo reader, human or AI, hits the same trap.

**Processed 2026-08-27, cleared to run, on your decision.** One sentence in README.md: `LOG/` and `resources/` are historical records — they describe the project as it was when each entry was written; what the project is now is SPEC.md and this README. True and harmless for consumers reading their own projects' repos too.

Rule gate: not needed — a README sentence, no method rule touched.

--- Build block ---
Changes: `README.md` — one sentence, placed where the repo's contents are described, stating that `LOG/` and `resources/` are historical records and that SPEC.md and the README describe the present.
Acceptance: the sentence is present and reads for an outside reader; nothing else in README changes.
Refused: sweeping old records for retired names — records keep the vocabulary of their time, standing rule.
--- End build block ---

#### Spec-sync gate aligned to the SPEC-leads model — the false-SPEC paragraph is repealed [spec-sync-gate-aligned-to-spec-leads]
Surfaced at the 2026-08-27 planning close's look-back and processed in the same session on your call — "too important to skip". Two shipped texts answer the same question opposite ways: plan.md (and SPEC itself) say product truth is written at planning time, ahead of the build — SPEC leads, because /next reads SPEC at run start and builds against it — while done-plan.md's spec-sync gate still says editing SPEC for a decided-but-unbuilt change makes "a false SPEC, not a synced one", SPEC moving only when the behaviour does. The second is the older answer that lost when the lead model was decided, never repealed. This session complied with the lead rule three times, so SPEC now describes decided-but-unbuilt behaviour by design.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement.** The residual cost stays stated, not solved: a reader of SPEC alone, between plan and build, sees behaviour not yet installed — bounded by the cleared item that will build it.

Rule gate: run — repeal inside done-plan.md's spec-sync gate, superseded by the lead model already operative in plan.md and SPEC; the gate's purpose survives (catching a decision whose sentence was never written); nothing else evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/done-plan.md` — the spec-sync gate's paragraph beginning "A decision made this session but not yet built satisfies the gate…" and containing "a false SPEC, not a synced one" is repealed; in its place: the gate checks that every decision's SPEC sentence was written at the processing step, and a sentence describing decided-but-unbuilt behaviour is the designed lead, not drift, bounded by the cleared item that builds it. Grep the repealed paragraph's distinctive words across the project before editing; anything else carrying them is reworded in the same build.
Acceptance: the gate carries the lead-model statement; "a false SPEC, not a synced one" appears nowhere shipped; the gate still stops a close where a decision's sentence was never written.
Refused: reverting to SPEC-moves-with-behaviour — it contradicts SPEC being read at build time, the architecture already shipped and relied on.
--- End build block ---

#### Droppable-set ask carries no recommendation at a batch of one [droppable-set-ask-lacks-recommendation-singular]
Raised by you 2026-08-26: a planning opening presented a single droppable capture ending on a flat "Drop it, or keep it?" with no recommendation, and you had to ask where it was. Partly an instance of the bundling defect already fixed in [first-item-presentation-reads-as-bundling-build] (built but not installed at the time), but one narrow piece survives that fix: plan.md's droppable-set specimen ("Drop both, or name any to keep?") leans toward dropping only by plural grammar, and at a batch of one that degrades to a bare either/or. The one-at-a-time delete branch already requires a recommendation explicitly ("my recommendation is to drop this"). **Kept 2026-08-26, on Claude's recommendation and your agreement.** An amendment to an existing step's wording, no new rule slot; SPEC describes the triage without specifying the ask's grammar, so no SPEC sentence changes. The live plan.md was read before designing.

Rule gate: run — amendment to the droppable-set step in plan.md, parent named; no freestanding rule, nothing evicted beyond the specimen wording it rewords.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the droppable-set step at the session opening: one sentence added stating the ask recommends the drop explicitly and offers exceptions, at any batch size; a singular specimen added alongside the existing plural one (e.g. "One looks droppable — **[old-slug]**: its premise is gone. My recommendation is to drop it — keep it instead?"). The plural specimen stays; the step's mechanics are unchanged.
Acceptance: the step's text requires an explicit recommendation whatever the batch size, and both specimens show it; no other part of the step changed.
Refused: widening the one-at-a-time delete branch's rule to cover this — the fix belongs at the step whose specimen breaks, not at a second site.
--- End build block ---

#### Shared vocabulary replaces standing plain-English names — the method's own terms are spoken with the user [shared-vocabulary-not-standing-names]
Raised by you 2026-08-27: the standing-names idea is recursively feeding the method — every planning session mints new plain-English terms that get fed back in, and things inherit new names all the time. Your decision, in your words rendered here: drop the standing-names idea, not the plain-language effort; give it a specific rule allowing Throughliner jargon — your users and you will use the same vocabulary, even if it's hard for them at first, so that you can actually help them.

**Kept 2026-08-27, on your direction and Claude's design.** The sharpening Claude added, agreed: "the ready list" is itself a minted alias for a thing whose artifact shows different words — the marker reads "Cleared to run above this line" — so shared vocabulary means using the words the user's own files show. The repeal grep found every site: the declaration (skill-nonspecific-rules.md, Vocabulary), the keep-ask usage (plan.md), three FAQ mentions across faq-template.md and faq-index-template.md plus their FAQ/ copies, and the queued post draft [discord-post-plain-english-consent], now held behind this item. Nothing in INBOX/sent.md claims the name publicly, so no correction post is owed. The post draft's reword and its Blocked-by drop are planning work, done at the below-line revisit when this ships — deliberately outside the build block, which a run cannot point at the queue. The translate-away half of the vocabulary rule is untouched: internal mechanics naming nothing the user can see (step numbers, rungs, passes, doc filenames) still never reach output.

Rule gate: run — supersession of the ready-list standing-name declaration (evicted in the same move) and amendment of the Vocabulary rule's explained arm into the shared-vocabulary rule; the standing-names idea loses because each admitted name is a second name for a thing the method already names, and the corpus was growing names faster than sessions could translate them.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — Vocabulary section: the ready-list declaration comes out; in its place the shared-vocabulary rule: the method's own terms — the words its artifacts and commands actually show (capture, work item, Processed / Unprocessed, cleared to run, red flag, `[user]` item, walkthrough) — are the vocabulary spoken with the user, each explained once on first need; no plain-English alias is minted for a thing the method already names; the translate-away arm for internal mechanics is unchanged. `plugin/throughliner/docs/plan.md` — the keep-ask specimen reworded to method words ("move it into Processed, cleared to run?"). `plugin/throughliner/templates/faq-template.md` and `faq-index-template.md` — the three "ready list" mentions reworded to "cleared to run" / the cleared region; `FAQ/faq.md` and `FAQ/index.md` re-copied from the templates. Acceptance: no shipped doc, template or FAQ copy contains "ready list"; the Vocabulary section carries the shared-vocabulary rule in an admissible shape; the translate-away arm's text is unchanged.
Refused: dropping the plain-language effort whole — the user kept it explicitly, and the jargon failures it exists for are real, one processed 2026-08-27 as [general-jargon-translate-and-walkthrough-readback]. Keeping "the ready list" as grandfathered — it is the live instance of the recursion being dropped.
--- End build block ---

#### Builds return to reading the queue whole — the generated view and build blocks are retired [builds-read-the-queue-again]
Your decision, 2026-08-27, at the end of a long design exchange — a supersession of the build-view architecture. Your reasons, rendered here: build blocks duplicate each item's rationale into a second in-file artifact and are bloating the queue; a build stripped of the why infers one and infers wrong — the live specimen being the "fresh short sessions" framing, which missed the true reason (compensating for a build model with less capability and less cross-project knowledge than the planner); and Throughliner must not be designed FOR authoring Throughliner — it is project-agnostic, and the view was a fix for this project's own transcription failure generalised into everyone's architecture. The debloat is worth the trade, accepted with the counter-argument heard: the purpose-instruction is an untested replacement for a structural guard, on the less capable model — your words rendered: we go into this smarter than last time.

What replaces the structural guard, designed in the same exchange:
- **The purpose instruction, in the run's own procedure:** an item's reasoning is read to aim the work — it explains why the thing should be built and is not itself part of what is built.
- **The boundary rule, stating what unwarranted inclusion looks like:** reasoning lands in a file the build writes only where that file is the record of the decision — the LOG entry — or where the item specifically instructs it; in every other file (a doc, a rule, code, a template) the build writes the action the reasoning justifies, and not the reasoning.
- **The block-authoring rule's survivor, promoted in capability-gap wording:** a kept item's instructions are written for a reader with less context and possibly less capability than the session writing them. Acceptance softens to the observation that shows the change landed — never invented verification work. Refusals stay carried, one bare line each. (This merges and closes [build-blocks-must-not-require-inference], whose content is fully carried here; her three refinements from that discussion — the capability-gap why, the softened acceptance, the refusal bound — are the promoted form. The per-step executable-or-checkable constraint was considered and left out: the keep-step's files-plus-what-changes check already tests executability at the site that can refuse, and blocks legitimately carry non-step content.)

What the record held against this, carried forward as the throughline requires: the view was adopted on a measured failure — reasoning reaching shipped docs near-verbatim when builds read it — and on cost, a run once reading ~56,000 tokens of queue to build a handful of items. The structural guard loses because both its wins came bundled with the duplication bloat and the wrong-why inference, and because the failure it fixed was this project's own self-hosting pathology, not a consumer's. The cost of the whole-queue read returns, accepted knowingly.

Rule gate: run — supersession of the build-view architecture and of plan.md's build-block authoring rules; the purpose instruction and boundary rule are authored as amendments to next-build.md's existing run discipline; eviction is the block machinery itself. Retired artifacts named in the block per the retiring-a-step rule.

--- Build block ---
Changes: `plugin/throughliner/docs/next.md` and its build branch — the run reads SPEC and then the queue's cleared region whole (each item's full text, rationale included; the queue file itself is not edited by this build), carrying the purpose instruction and the boundary rule (with the unless-specifically-instructed carve-out); the halt-on-blockless-item rule retires. `plugin/throughliner/docs/plan.md` — the build-block authoring rules come out of the keep-step; in their place the promoted instruction-authoring rule in capability-gap wording, with acceptance-as-observation and one-line refusals written into the item's prose; the two-limb check is untouched. `plugin/throughliner/docs/done.md` — close reads items directly (already does); view-cleanup steps retire. `plugin/throughliner/scripts/generate_build_view.py` — deleted (retired artifact of the retired step, with any generated view files). `plugin/throughliner/hooks/pre_tool_use.py` — view-file references in the scope-lock retire; suites updated. `plugin/throughliner/hooks/post_tool_use.py` and `plugin/throughliner/scripts/queue_digest.py` — the cleared-item-with-no-block checks retire; suites updated. `plugin/throughliner/templates/faq-template.md` and `faq-index-template.md` — the two view mentions rewritten to the new model, `FAQ/` re-copied. `CLAUDE.md` — the two-models rule shrinks to naming which model runs which session here plus a pointer to the shipped rule; the QUEUE.md description and any view references updated.
Inputs: the existing build blocks on cleared items — left in place in the queue; the run under the new model simply reads them as part of each item's text until a planning session folds them into prose.
Acceptance: no shipped doc, hook, script or template references the generated view or requires a build block; the run's procedure carries the purpose instruction and boundary rule; all suites pass.
Red flag: none.
Refused: keeping the view but carrying rationale alongside the block (the middle shape) — the duplication bloat survives it. Instructing the build while still withholding the queue — the wrong-why inference survives it. A per-step executable-or-checkable constraint — duplicates the keep-step's existing check and constrains block content that is legitimately not a step.
--- End build block ---

#### Retire "line" as the name for a [user] work item across the shipped docs [user-line-terminology-retired]
Raised by you 2026-08-27: `[user]` work items were being called "lines" again in yesterday's sessions — old terminology from when work was a single line, long untrue of the format (an item is a `#### ` heading with prose beneath). Sits under [shared-vocabulary-not-standing-names]: one thing, one name, the name the artifact shows.

**Kept 2026-08-27, on Claude's recommendation and your agreement.** The repeal grep found six files carrying "`[user]` line/lines": `skill-nonspecific-rules.md` (heaviest, ~7 mentions), `plan.md`, `next-build.md`, `done.md`, `SPEC.md`, `CLAUDE.md`. FAQ templates and README are clean. The reword is judgment-applied, not blind substitution — a sentence leaning on line-ness ("file it as a line") is rephrased around the item.

Rule gate: run — no rule authored; existing text corrected to one term. The build's LOG entry carries the Retired: line ("line" as the name for a `[user]` work item), appending to resources/retired-terms.md so the standing checks can catch it returning.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/plan.md`, `plugin/throughliner/docs/next-build.md`, `plugin/throughliner/docs/done.md`, `SPEC.md`, `CLAUDE.md` — every "`[user]` line / lines" reworded to "`[user]` item / items", with sentences that lean on line-ness rephrased around the item; no meaning changes.
Acceptance: a grep for the variants ("[user] line", "[user]` line", plural forms) returns nothing in shipped docs, SPEC or CLAUDE.md; the retired-terms record gains the entry via the close's Retired: line.
Refused: sweeping LOG/ and old queue prose — records keep the vocabulary of their time.
--- End build block ---

#### Retire "keep" as the disposition term — an entry is processed, with the outcome named [keep-term-retired-for-processed]
Raised by you 2026-08-27: "keep" as the universal word for processing a capture into a work item makes no sense — captures don't necessarily describe work, and the operation is a transformation, not retention. Your decision after discussion: the operation is *processing*, and the ask names the outcome in the words the artifacts already show — moved into Processed cleared to run, moved into Processed held below the line, or deleted. Sits under [shared-vocabulary-not-standing-names]: no second name for a thing the artifacts already name.

**Processed 2026-08-27, cleared to run, on your decision.** The disposition ask becomes "process it in — cleared to run?"; stamps written into items from now on read "Processed <date>" with the outcome; existing "Kept" stamps stay — records keep the vocabulary of their time. Internal mechanics rename in the same sweep ("the keep-step" → the disposition step, procedure-facing only). The grep found term-of-art uses concentrated in plan.md (the keep/delete step, its asks and specimens), skill-nonspecific-rules.md, next.md and done.md families, SPEC.md and CLAUDE.md, amid much ordinary-English "keep" the sweep must not touch — a judgment reword, not substitution.

Rule gate: run — terminology correction under the shared-vocabulary supersession already gated on [shared-vocabulary-not-standing-names]; no new rule. The build's LOG entry carries Retired: "keep" (the disposition term for processing a capture into a work item), appended to resources/retired-terms.md.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the keep/delete disposition step reworded: the operation is processing, the ask and every specimen name the outcome (into Processed cleared to run / held below the line / deleted); "the keep-step" renamed wherever docs cite it by name — and the build picks a plain name for it rather than "the disposition step": "disposition" itself needed explaining to the user in the session that decided this (2026-08-27), so a candidate like "the decision step" is preferred, chosen at the build. `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/next.md` and family, `plugin/throughliner/docs/done.md` and family, `SPEC.md`, `CLAUDE.md` — term-of-art "keep"/"Kept"/"keep-step" uses reworded the same way; ordinary-English "keep" untouched; cross-doc references by name updated to the new step name.
Acceptance: no shipped doc, SPEC or CLAUDE.md uses "keep" as the disposition term or "keep-step" as the step name; asks and specimens name outcomes in artifact words; retired-terms gains the entry via the close.
Refused: rewording old "Kept" stamps in QUEUE.md and LOG/ — records keep the vocabulary of their time. Blind substitution — most "keep" occurrences are ordinary English.
--- End build block ---
Ordering: builds after [shared-vocabulary-not-standing-names] and [user-line-terminology-retired], which touch the same files — carried by placement and this sentence, not a blocker, since one run can build all three in order.

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

