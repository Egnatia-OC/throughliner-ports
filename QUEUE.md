# QUEUE

## Red flags

Security, privacy, and data-exposure risks Claude has surfaced — kept at the top so they're the first thing seen each session. Each carries a state: open, resolved, or accepted. Empty until a risk comes up.

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Add a screenshot of the plugin upload screen to INSTALL.md** **[install-upload-path-clarity]**

The prose half of this batch landed in a goal session (2026-06-15): INSTALL.md now states the confirmed upload path (Customise top left → + icon on the left → "Create a plugin" → browse and select the .zip), drops the hedge "usually in the top menu or settings area," and adds a heads-up that the "Create a plugin" label is the install path despite sounding like an authoring tool. Only the screenshot remains, and a goal session can't produce it — it needs a real capture of the desktop app's Plugins screen.

Build:
- INSTALL.md: add a screenshot of the Plugins screen showing the + icon and the "Create a plugin" option, so users can visually confirm they're in the right place. (User-only — needs a real desktop-app screen capture; a placeholder pointer sits in INSTALL.md's smoke-test step until the image lands.)

**Deferred-test lifecycle: tick state at determination, runnability tails, /plan batch-rolling, reinstall flag** **[deferred-test-lifecycle]**

From a capture raised at the [git-add-safety-hook-gap] /done (2026-06-12); execution channel redesigned at the 2026-06-12 /plan before building. Deferred tests have no execution trigger: the section makes pending tests visible, but nothing tasks anyone with producing the confirming event, so "Confirmed by:" lines describe observations that only happen if someone deliberately acts or happens to notice. [deferred-tests-structural-home] solved surfacing; this solves executing. The trigger-flavor observation is the spine: reinstall-gated tests, the dominant flavor in self-hosting, have a mechanically detectable runnable moment — session_start already reports a version mismatch after a plugin update. Grounded against the current eight-line backlog, runnability splits into deliberately runnable (Claude can produce the event on demand), near-automatic (the event occurs in almost any session), and observational (confirmable only by watching behaviour). Runnability is recorded at authoring time as a prose tail, not a closed taxonomy — the same move as [blocked-by-trigger-flavors]. The original design here extended /next's pre-flight from re-present to re-present-and-offer. Rejected at the amendment: at pre-flight the user came to start a batch, and the backlog is information with no action slot at that moment — host-side lines wait on a reinstall, user-run lines need their own session, and the listing sits between the user and the batch they asked for, growing as lines accumulate. Execution channels through the queue instead: /plan rolls runnable lines into test batches — several gathered into one batch, or single lines attached to a test batch already being authored. Two trigger moments, both judgment rather than a hard count, since accumulation rate is project-local: the Step 1 scan noticing rollable lines, and test-batch authoring time. Test batches only, never build batches: a user-run test riding in a build batch would stop an unattended next→done→next run, and test sessions are already where user involvement is the work itself. External-event lines can't roll; they stay in the section until their event fires. /next's pre-flight deferred-tests step is deleted outright. /done gains a cheap close-out backstop — did this session's own activity confirm a pending line? It pays mainly in self-hosting, where the session's behaviour is the thing under test; it stays universal because no mechanical self-hosting flag exists to condition on, and in a consumer close it costs one section read. Two folds ride along unchanged. From the /clear-resilience discussion: _build.md's Progress has no "couldn't run" state, so a mid-session determination that a test can't run lives only in conversation — post-/clear, /done misreads the unticked entry as unfinished work; the fourth tick state writes the determination into the file at the moment it's made. And the section's scope statement (test-only, shipped-work-only) currently exists nowhere. session_start.py is shared with [session-start-dirty-tree-check] and [plan-state-artifact] — whichever builds second sees the others' changes, per the standing convention. (The /next pre-flight deletion has been carved out to [delete-preflight-deferred-tests], which ships ahead of this batch; this batch no longer deletes that step.)

Build:
- plugin/si-plugin/docs/done.md, Deferred tests section: add the scope statement — the section holds only verification for shipped work; test failures and emergent test needs route to Captures, keeping /plan's ownership of new work. Extend the line format: "Confirmed by:" gains a runnability tail stating whether Claude can deliberately produce the confirming event, the user must, or an external event must fire.
- plugin/si-plugin/docs/plan.md Step 1 scans: read the Deferred tests section alongside Parked — lines whose tails say Claude-runnable or user-run are rolling candidates, carried into Step 2 as one move (roll these lines into a test batch, or attach to one being planned this session), not per-line interviews. External-event lines stay without comment.
- plugin/si-plugin/docs/plan.md Step 3, near the Test-section guidance: when authoring a test batch, check the Deferred tests section for pending lines that can ride along.
- plugin/si-plugin/hooks/session_start.py: when the version-change report fires and QUEUE.md's Deferred tests section is non-empty, add one line to the report — deferred tests may now be live-testable; /plan can roll them into a test batch.
- plugin/si-plugin/docs/done.md close-out: add the backstop check — read the Deferred tests section; if this session's own activity confirmed a pending line, remove it and record the confirmation in the LOG entry. One section read when nothing fires.
- plugin/si-plugin/docs/next.md Progress formats, plus next-build.md and next-test.md test-entry steps: add the fourth tick state, `- [x] Test description — deferred (reason)`, written at the moment a test is determined unrunnable in this session.
- plugin/si-plugin/docs/done-build.md and done-test.md: verify-completion treats deferred-ticked entries as closeable, not unfinished; the write-deferred-tests step converts each deferred-ticked entry into a queue line mechanically.
- Lifecycle-description sweep — four places currently say /next re-presents the section: QUEUE.md's Deferred tests intro (this project), this project's CLAUDE.md Method docs description (host-only, does not propagate), plugin/si-plugin/templates/CLAUDE-TEMPLATE.md QUEUE.md description, and plugin/si-plugin/templates/faq-template.md's deferred-tests entry. Update each to the new lifecycle: /done writes lines, /plan rolls runnable ones into test batches, /done's close check backstops confirmations.

Test:
- Claude-run: session_start.py against a fixture — version mismatch with a non-empty Deferred tests section adds the line naming /plan; mismatch with empty section stays silent; no mismatch stays silent.
- Behavioural, host-side (after push + reinstall): the first session after the update shows the hook's deferred-tests line; the next /plan proposes rolling the runnable backlog — the current eight lines are the natural exercise; a later /next pre-flight shows no deferred-tests listing. Needs the deferred-test discipline — flag at /done if it can't run.

**Drop the skill-time re-read of plugin-behaviour.md** **[behaviour-doc-double-load]**

session_start injects plugin-behaviour.md in full every session, and /plan, /next, and /done each instruct a re-read — so every skill session carries the largest doc twice. The re-read insures against compaction aging out the injected copy, but paying double on every session to insure against an occasional event is backwards, and the short-session design target (post-June-20 weak-model sessions) shrinks the compaction risk further. Alternatives weighed: dropping the injection instead would gut outside-skill behaviour — mid-session captures happen precisely outside skills — and the progressive-disclosure restructure (compact core injected, full doc at skill time) costs a content split while the doc is still in flux under the queued audits, and is the *larger* footprint for skill sessions anyway since its skill-time load lands on top of the standing core. Revisit the restructure once the compliance arc settles the doc. /setup is deliberately untouched: it runs in unadopted projects where the injection may not fire, so its own load may be the only copy.

Build:
- plugin/si-plugin/skills/plan/SKILL.md, skills/next/SKILL.md, skills/done/SKILL.md: remove the "Re-read them before continuing" instruction. Keep the sentence naming plugin-behaviour.md as governing the skill — authority stays stated; only the duplicate load goes.

Test:
- Self-verifying from doc text. Behavioural watch after reinstall: any rule-leakage observed in a long session post-change is a mandatory capture (possible future: re-inject after compaction if the desktop app ever supports a compaction hook).

**Classify reference roles in the dependency scan: dependency vs evidence** **[dependency-scan-reference-roles]**

The routing gate parks any capture that names another item — "even if Claude reads the reference as incidental." But references run both ways: the observed case (40749f7+1) cited another item as evidence, and the default would have parked the blocker behind the thing it blocks, inverting the graph. The 2026-06-10 /plan confirmed the distribution problem: four captures in one pass carried evidence citations needing narrated overrides — in a capture style that requires including reasoning and origin, evidence citations may be the majority of references, so the default is tuned backwards. As written, every correct override is a rule violation, which trains a weak model to misroute or to treat rules as optional. Fix keeps the mechanism mechanical — classification by linguistic marker, not vibes: forward-looking language ("once X ships," "after Y," "depends on," "needs") keeps the park default; backward-looking language ("observed at," "see," "surfaced during," "from") lifts it, with the recommendation required to name the reference and its role so wrong classification stays user-catchable; ambiguous keeps the park default, the safe side. Matches the "dependency or citation?" language in [queue-format-lint-hook]'s advisory check.

Build:
- plugin/si-plugin/docs/plan.md Step 2 dependency-scan sub-step: replace the "even if incidental" rule with the two-role classification and its marker lists, the narration requirement for evidence-classified references, and the ambiguity default.
- plugin/si-plugin/docs/plan.md Capture and parking discipline, "Routing gate before recommendation" bullet: same change — the canonical statement and the step must not drift apart.

Test:
- Behavioural on the next /plan pass over citation-bearing captures: evidence citations route without false parking, and each classification is named at recommend time.

**State the short-session design target in CLAUDE.md** **[short-session-design-target]**

Observed on the first Fable day: development tipped to one long session, and three procedure gaps surfaced only because session memory covered them — gaps stop hurting under a capable model, so they stop getting found, while consumers and the post-June-20 development model still hit them. All three named gaps now have structural homes ([deferred-tests-structural-home], the push-ritual backfill folded into [hash-backfill-as-hook], and /next's blocker-gate capture scan), but the principle itself lives only in conversation memory — the exact failure mode it names. A third fix shape, a deliberate-freshness regression ritual, was considered and dropped: after June 20 the development model is the weaker model, so every session becomes the regression test naturally, and building a ritual for a ten-day window is process for its own sake.

Build:
- This project's CLAUDE.md, Rules for Claude: add the design-target rule — the system must work for fresh, short sessions on the weaker model; the files must suffice without session memory; conversation memory is a convenience, never a dependency.
- Same file, the route-observations rule (the "all use of the plugin is testing the plugin" bullet): sharpen with the named trigger — any moment Claude notices session memory covering for something the docs or files should carry is a mandatory capture.

Test:
- Self-verifying from doc text. The behavioural check arrives free after June 20: every short weak-model session exercises the contract.

**Install the scope anchor: one definition of build scope, wired through the docs** **[scope-anchor]**
Blocks: [scope-boundary-rule], [trickle-up-next-md-duplicates]

From [scope-distinction-audit]. Build scope has no canonical definition. The working definition assembles from three places, and plugin-behaviour.md — the only doc injected into every session — says "don't fix things outside current scope" without defining current scope. This batch installs one Scope statement in plugin-behaviour.md and points the skill docs at it. The statement also connects the two enforcement layers no doc currently relates: the entries' described work is the definition, enforced by judgment; the Files: list is its mechanical approximation, enforced by the hook as a backstop. A build can stay within listed files and still exceed the described work, so passing the hook never by itself makes work in-scope. The word "scope" also loses its second sense — the Dependency ownership bullet stops using it for project scope, leaving build scope as the word's only meaning. plan.md gains the authoring side: entries feed the lock, so build entries name their files, and scope gets decided at planning time instead of ask-by-ask at build time. Must land before [trickle-up-next-md-duplicates] deletes next-build.md's restatement — otherwise the rule's only remaining statement uses a term no doc defines.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the Scope statement — build scope is the active batch's entries' described work; the Files: list in _build.md is its mechanical approximation, enforced by the pre_tool_use hook as a backstop; passing the hook never by itself makes work in-scope; work outside scope routes to Captures.
- plugin/si-plugin/docs/plugin-behaviour.md, Dependency ownership: reword "The user owns scope" to "The user owns what enters the queue, what gets parked or dropped, and whether a build expands."
- Grep "scope" across the procedure docs for other project-scope-sense uses; reword those the same way. Build scope becomes the word's only remaining meaning.
- plugin/si-plugin/docs/next.md and next-build.md: point their scope-definition statements at the anchor instead of restating it; keep the skill-specific rules. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md, Scope management: reword the scope-expansion ask from file-shaped to work-shaped — name the work, then the files it needs, listed or not — so work growing inside an already-listed file triggers the same ask a new file would.
- plugin/si-plugin/docs/plan.md Step 3, near the batch structure: build entries name the files they touch; the scope-lock is populated from them; an entry naming no files leaves the lock at method-docs-only. Files that don't exist yet count as named when the entry says what gets created and where.
- plugin/si-plugin/docs/plan.md, readiness gate: add the matching check — can the Files: list be populated from these entries?

Test:
- Grep the definition phrasing across the docs after the edit: one canonical statement in plugin-behaviour.md, pointers elsewhere.
- Grep "scope" for surviving project-scope-sense uses — expect none.

**Define the boundary moves: the discovery decision rule and routing move, stated once** **[scope-boundary-rule]**
Depends on: [scope-anchor]

From [scope-distinction-audit], two findings that are one thought. First: Claude-noticed out-of-scope discoveries have no defined routing move — "note them for the queue" names no destination, no mechanics, no timing, so a weak model can hold them in conversation memory, the exact failure the short-session design target forbids. The fix collapses the three-way split by noticer: who noticed doesn't change the artifact, so Claude-noticed discoveries take the same capture flow user-raised items already get — draft, show, "anything else?", resume — at the moment of noticing. Test failures keep their at-close path; interrupting a test run is the one case with a real reason to defer. Second: the decision rule for mid-session discoveries is real but never stated — needed → ask or split; not needed → capture and continue; premise broken → halt — visible only across five separate passages. It gets stated once, in plugin-behaviour.md beside the routing move, because "not needed → capture and continue" is that move; duplicating it per skill doc recreates the drift the trickle-up arc is removing. The skill docs' sections then read as elaborations of one rule.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, Routing and discipline: replace "note them for the queue" wording with the defined move — Claude-noticed discoveries route to Captures at the moment of noticing, per the same capture flow as user-raised items (draft, show, "anything else?", resume).
- plugin/si-plugin/docs/plugin-behaviour.md, same spot: state the decision rule once — needed to complete the batch's entries → ask to add (minor) or propose splitting (significant); not needed → capture and continue; premise broken → halt and course-correct.
- plugin/si-plugin/docs/next-build.md (Rules during build) and next-test.md (Rules during test): replace their "note them for the queue" wording with a pointer to the defined move. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md and next-test.md, Scope management: open each section with a pointer to the decision rule so the existing passages read as its elaborations.

Test:
- Grep "note them for the queue" (and close variants) across the procedure docs after the edit — expect zero hits.
- Behavioural: the next /next session that meets a Claude-noticed discovery routes it at the moment of noticing, not "for the queue" at an undefined later.

**Remove rule duplicates from next.md and the per-type docs** **[trickle-up-next-md-duplicates]**
Depends on: [scope-anchor]

next.md and the per-type docs restate four rules that plugin-behaviour.md already carries: SPEC read-only (next-build.md, next-test.md), don't fix outside scope (next-build.md), state regressions plainly (next-build.md, next-test.md), one build at a time (next.md). Wording has already drifted slightly between copies — the cost of duplication made visible. Trickle-up discipline: plugin-behaviour.md is the canonical home; skill docs carry only what's skill-specific. This extends the same bet as [behaviour-doc-double-load]: post-dedup, these rules live in the session-start injection alone — the consistent direction, not a new exposure. Locate every removal by rule text, not the capture's line refs — the docs have been edited since filing.

Build:
- plugin/si-plugin/docs/next-build.md: remove the SPEC read-only, don't-fix-outside-scope, and state-regressions-plainly restatements. Keep the section's skill-specific rules (scope-expansion ask, REGISTRY not build scope).
- plugin/si-plugin/docs/next-test.md: remove the SPEC read-only and state-regressions-plainly restatements.
- plugin/si-plugin/docs/next.md: remove the one-build-at-a-time restatement. Keep entries-are-the-contract and per-entry ticking.

Test:
- Grep the four rule phrasings across next.md and the per-type docs after the edit — remaining hits should be in plugin-behaviour.md only.

**Make SPEC a normal doc: spec edits become a planned build batch** **[spec-edit-batch-type]**
Depends on: [scope-anchor]

Decided 2026-06-13. Right now SPEC.md is special. It is read-only during builds (the pre_tool_use hook enforces this) and edited directly in /plan. That special case caused confusion — a direct SPEC edit during a /plan read as off-script even to the designer. This batch makes SPEC a normal doc, changed only through a planned spec-edit build batch, like any other doc.

Dropping the read-only lock is safe because scope-lock already does the lock's real job. The lock existed to stop a build from editing the spec it builds against — grading its own homework. A feature build does not list SPEC.md in its Files, so scope-lock alone keeps it from touching SPEC. Spec changes get their own batch, separate from any feature build, so no build edits its own contract. The "decide in planning" split survives: authoring the spec-edit batch in /plan is the decision, and /next only does the typing. This sequences after [scope-anchor] because that batch hardens scope-lock's definition, and once the read-only lock is gone, scope-lock is SPEC's sole protector.

This batch creates the spec-edit mechanism but cannot use it on itself. Its build runs under the current host, where the read-only lock is still active until reinstall, so the build cannot edit SPEC.md. The one SPEC change this work implies — rewording SPEC's hooks description — is therefore deferred to the first spec-edit batch, authored after this ships and reinstalls.

Build:
- pre_tool_use.py: remove the SPEC.md read-only-during-builds rule; scope-lock alone governs SPEC. Make sure the empty-Files method-docs fallback does not let a build edit SPEC by default.
- plan.md: add spec-edit as a batch type in the Step 3 batch structure, alongside Build/Test/Audit (and Freeform once it ships). Add a /plan step that authors spec changes as a spec-edit batch.
- plugin-behaviour.md and plan.md pipeline wording: change "idea → SPEC.md → QUEUE.md" to "idea → decide in /plan → spec-edit batch → /next edits SPEC → feature batch".
- This project's CLAUDE.md: reword "Edit it only during /plan" to the new model.
- done.md / done-build.md: a spec-edit batch closes like any build.
- post_tool_use.py lint: add spec-edit to the allowed batch subheadings.

Test:
- Claude-run: pre_tool_use.py against a fixture — a build with an empty Files list cannot edit SPEC.md by default.
- Behavioural, host-side (after push + reinstall): a /next spec-edit batch edits SPEC.md without being blocked, and a normal feature build still cannot touch SPEC unless it is in scope. Needs the deferred-test discipline — flag at /done if it can't run.

**Generalize ask-when-unsure into plugin-behaviour.md** **[trickle-up-ask-when-unsure]**

next.md's "Unsure about an implementation choice? Ask. Don't guess and build wrong" is universal — /plan ordering calls, /setup scaffolding choices, /done routing decisions — but lives only in next.md, so every other skill runs without it. Trickle-up: the generalized rule belongs in plugin-behaviour.md Communication, adjacent to the web-search bullet so the two read as one decision rule with two branches — uncertain about an external fact → offer a search; uncertain about a choice the user owns → ask, don't guess and proceed. One deliberate addition beyond the capture as filed: a self-contained line in setup.md, because unadopted sessions get no behaviour-rules injection (confirmed in session_start.py this session) and /setup's scaffolding choices are a named use of the rule — setup.md carries its own copies by design. Same next.md rules area as [trickle-up-next-md-duplicates] touches; no ordering between them, placed adjacent for one-session convenience.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Communication, next to the web-search bullet: add the generalized rule — when uncertain about a choice the user owns (implementation, scaffolding, routing), ask; don't guess and proceed.
- plugin/si-plugin/docs/next.md: remove the local copy (locate by rule text, not line ref).
- plugin/si-plugin/docs/setup.md: add one self-contained ask-when-unsure line where scaffolding choices are made.

Test:
- Grep the rule phrasing after the edit: present in plugin-behaviour.md and setup.md, gone from next.md.

**Queue-visible plan markers: write predictable planning moments into the queue** **[queue-plan-markers]**

Claude keeps recommending "run /plan first" at moments that feel unexpected to the user, but a subset of those moments is predictable when the queue is authored — an audit batch will file findings the next batch depends on; a batch's dependencies can only be estimated after a design decision a planning session has yet to make. Writing those moments into the queue converts a judgment-based session-end recommendation into a mechanical gate (weak-model friendly, the same bet as the push marker), makes the planning rhythm visible before it's hit, and carries the reason inline. Floor, not ceiling: planning must happen here at minimum, for the stated reason; ad-hoc /plan elsewhere stays unrestricted. Part of the autopilot prerequisite arc named in the cruise-control trigger. The FAQ entry for the marker is deliberately not in this batch — it rides with the FAQ-trigger capture's routing.

Build:
- plugin/si-plugin/docs/plan.md Step 3 (ordering/placement work): add the authoring rule — when placement puts an audit batch ahead of batches that depend on its findings, or queues a batch whose dependencies wait on an undecided design question, insert "--- Plan session here: <reason> ---" between batches at that spot. Name the two cases as illustrations, not a closed list.
- plugin/si-plugin/docs/plan.md Step 1: when the marker sits at the queue top, addressing its stated reason is part of this session's work; remove the marker once addressed.
- plugin/si-plugin/docs/next.md pre-flight: halt on a plan marker at the queue top, sibling to the push-marker halt — tell the user a planning session is needed and name the marker's reason.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md and this project's CLAUDE.md (QUEUE.md format descriptions): document the marker line so it's recognizable in consumer projects.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry explaining the plan-marker line a consumer may meet in their queue — what it means, what to do (run /plan).

Test:
- Self-verifying from doc text. Behavioural confirmation arrives naturally: the next /plan that authors an audit batch with dependent work should insert a marker; the next /next that meets one should halt and name the reason.

**FAQ entries become part of batch authoring** **[faq-authoring-trigger]**

The FAQ ships as faq-template.md, authored in this project and scaffolded to consumers at /setup — yet nothing routinely updates it: entries happen only when a batch explicitly includes one (observed once, [narrate-build-md-purpose]), and the pre-push sweep drift-checks existing answers without ever asking whether new concepts lack coverage. This is the FAQ twin of the spec-entry trigger, keyed at the same prospective moment — batch authoring. It's a host-project rule, not shipped plan.md: consumers never author FAQ entries, so the rule would misfire in their /plan sessions. The push-sweep coverage backstop was considered and held — the observed failure is no-trigger-at-all, not a leaking trigger; the sweep is already heavy; ship the rule and watch, add the backstop only if entries still slip through. The existing backlog is [faq-coverage-audit]'s job; already-queued batches introducing consumer-visible concepts ([queue-plan-markers], [deferred-tests-structural-home]) got FAQ entries added at routing time.

Build:
- This project's CLAUDE.md (host-only, does not propagate), with the self-hosting conventions: add the rule — when /plan authors a batch that introduces something a consumer would see or ask about (a new queue line, a new doc section, a new narration moment), the batch carries a faq-template.md entry (plus its index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer?

Test:
- Self-verifying from the rule text. Behavioural: the next /plan authoring a consumer-visible batch should include the FAQ entry without prompting.

**One-time FAQ coverage audit against the current plugin** **[faq-coverage-audit]**

[faq-authoring-trigger] only fixes the future. The FAQ's 13 Q&A pairs date from its original authoring; concepts shipped since have never been coverage-checked — the pre-push sweep only checks existing answers for drift. One sweep catches the backlog; findings route to Captures per the audit contract.

Audit:
- Target: plugin/si-plugin/templates/faq-template.md and faq-index-template.md, read against the consumer-visible concept surface of the current procedure docs (setup.md, plan.md, the next and done families, plugin-behaviour.md) and the scaffolded doc formats.
- Criteria: every shipped concept a non-coder consumer would meet and ask about, checked for an answer; and the reverse gap — existing answers naming concepts that no longer ship. For each finding: the concept, why a non-coder would ask, and whether the entry is missing or stale.

**No planning work in execution skills** **[no-planning-in-execution]**

The boundary between /plan and the execution skills rode on "no thinking work," which was the wrong axis — Claude thinks plenty while executing, and the audit auto-file direction deliberately leans on Claude's thinking. The real boundary is planning work: processing captures — routing, promoting, parking, deciding their fate — and the human decision-making that entails. Capture-making stays open to every session type (the never-restrict-ideation principle); capture-processing is /plan's monopoly. Observed leak: [output-tag-audit] seeded a reconciliation item whose resolution was a planning decision made mid-/next, its reasoning landing where no planning session looks. Part of the autopilot prerequisite arc named in the cruise-control trigger: unattended next→done→next is only safe if no decision the user must own can arise mid-run. plan.md's thinking-work ground rule stays as the /plan-side gate on what gets queued ([audit-definition] is rewriting it); this rule is its execution-side counterpart, living where execution sessions actually load rules.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope, per resources/research/model-instruction-compliance.md): no planning work in any execution skill — planning work is processing captures (routing, promoting, parking, deciding their fate); making and approving captures is open to every session type; processing them happens only in /plan. Scope: all execution session types, including any added later. One clarifying line for test sessions: the user's involvement in running tests and judging outcomes is the work itself, not planning; filing those outcomes is capture-making.

Test:
- Self-verifying from the rule text. Behavioural: the next /next session that meets a routable discovery should append it to Captures and move on — no routing discussion mid-execution.

**Audit findings: one numbered set, bulk approval, contested items one at a time** **[audit-findings-bulk-approval]**

The per-finding capture-or-drop loop is the most interactive /next shape there is, and it duplicates /plan — every surviving finding judged twice. The original capture proposed removing approval entirely (mechanical auto-file); revised at routing: the [output-tag-audit] live preview validated bulk approval, not zero approval — findings 2–10 were batch-drafted and batch-approved in one pass, so the friction was the round-trips, and a session whose output the user never sees gives no reason to run it interactively. Bulk approval keeps the Captures always-show rule fully intact (no approval exemption needed — the caveat lands in the sequencing rule instead) and stays within [no-planning-in-execution]'s "making and approving captures." Full no-approval auto-file moves to cruise control's design scope: straight-to-Captures is autopilot behaviour. Double judgment still dies: one bulk ask in /next, full per-finding judgment once, in /plan. Absorbs the next-audit.md half of the [output-tag-audit] routing-loops tag finding — the new flow is authored with its tags correct from the start.

Build:
- plugin/si-plugin/docs/next-audit.md: replace the per-finding route-approved-findings loop with the bulk flow — compile all findings, present them as one numbered set in a single message, ask the user to approve the set or list the numbers they don't accept as-is, cover contested ones one at a time (reword or drop), append the approved set to Captures, report the filed count at close. Tag the bulk ask and the contested-item loop correctly from the start.
- plugin/si-plugin/docs/next-audit.md, same rewrite: the new close defines its review tail from birth — reviewing means re-examining what was already found, not raising new work; anything new routes through the existing paths (out-of-scope via scope management, thinking work via Captures). From a [close-out-audit] finding (e120f3d): the current "keep reviewing" tail is undefined, leaving open the new-work-smuggling risk next-build.md's tail was hardened against.
- plugin/si-plugin/docs/plugin-behaviour.md Communication, sequencing rule: add the bulk-approval inversion alongside the existing alternatives inversion, hardened (why-clause, positive constraint, explicit scope) — a deterministic result set produced by user-approved criteria is presented as one numbered message for bulk approval; the ask invites listing contested numbers; contested items then run one at a time. One-item-at-a-time stays the default everywhere else.
- plugin/si-plugin/docs/done-audit.md: the LOG entry records bulk-step outcomes — findings rejected or reworded at approval, with reasons — so nothing decided at audit time goes unrecorded.

Test:
- Self-verifying from doc text. Host-side behavioural (after push + reinstall): the next audit session presents one numbered set — [faq-coverage-audit] is queued as the natural first exercise. Needs the deferred-test discipline — flag at /done if it can't run.

**Tag application across the next and done families** **[next-done-tag-sweep]**

From [output-tag-audit], its headline finding. The procedure docs use response-shape tags to control when Claude speaks. In next-build.md and next-test.md, the whole Execute step — where Claude does the build work — is tagged [SILENT]. But that step contains moments that must speak: reporting a failure, asking before scope grows, handing a user-run test over. A literal-minded weak model gets two contradictory instructions at those moments. It either breaks the silence tag, or honours it by suppressing a failure report — the dangerous case. The fix has two parts. Each speaking moment gets its own tag, because a tag on the specific moment overrides the tag on the surrounding step. And Execute gets one clarifying line: silence covers routine bookkeeping when things go fine; failures, asks, and handoffs always speak. This was the only audit finding needing new wording — every other finding is plain tag placement. Sibling tag findings from the same audit fold into this batch as they route. Locate every edit by content, not by the audit's line numbers — the docs shift under other queued batches.

Build:
- plugin/si-plugin/docs/next-build.md and next-test.md, Execute step: add the clarifying line — silence governs success-path bookkeeping; failures, asks, and handoffs speak.
- Same two docs, inside Execute: tag the scope-expansion ask and the user-run test handoff [PROMPT]; tag failure noting [BRIEF].
- Same two docs, Scope management: tag the scope-growth asks [PROMPT]. In next-build.md, "Scope grows during the build" takes the tag at section level — both its paths ask and wait. In next-test.md, "Test surfaces unexpected scope" takes it on the minor-case ask only — the significant case notes for the queue and continues, so a section-level tag would force a wait that shouldn't happen. Restores symmetry with the already-tagged "User raises something out of scope" sibling.
- plugin/si-plugin/docs/next.md pre-flight: tag the push-marker halt [BRIEF]. Tag the blocker gate's surfacing moments [BRIEF]. Tag [PROMPT] where a user decision gates proceeding — the deferred-tests check and the capture-overlap recommendation. By the time this batch runs, [deferred-tests-structural-home] and [queue-plan-markers] may have reshaped this gate; tag the text as it stands then.
- done-build.md, done-test.md, done-audit.md: tag the route-to-Captures approval loops [PROMPT] — the close-out steps where leftover findings are drafted into Captures for the user's approval. The routing prose stays; only the tag is added. The matching next-audit.md loop is not in this batch — [audit-findings-bulk-approval] replaces it wholesale, tagged from birth.
- done.md and the three sub-docs, close-out moments: tag the unticked-entries ask (finish or close partial) [PROMPT] in done-build.md, done-test.md, done-audit.md. Give the staleness sweep in all three the path-split treatment next.md's pre-flight already models — [SILENT] when clean, [BRIEF] when flagging. Tag done.md's router [SILENT] to match its own "don't ask" prose. Tag the minor bookkeeping moments [SILENT]: the registry update in done-build.md, the _build.md deletion in all three.

Test:
- Self-verifying from doc text. Watch later /next sessions: failure reports and scope asks speak; success-path bookkeeping stays silent.

**Trim tag-definition restatements from plan.md** **[tag-restatement-trim]**

From [output-tag-audit]. Four spots in plan.md restate in prose what the response-shape tag definitions already say — "one item at a time" beside [SEQUENCE], "don't narrate the absence" beside [SILENT]. The audit flagged a tension: trimming prevents the copies drifting apart, but local restatement also props up weak models. Resolved at routing: the propping has already been paid for centrally — the hardened definitions carry their own why-clauses and constraints — so keeping the restatements buys the same insurance twice while leaving wording to drift. The line to apply: trim where the hardened definition fully covers the content; keep prose that adds step-specific substance. The audit also flagged next-audit.md's "Don't preview upcoming findings," but that line lives in the section [audit-findings-bulk-approval] replaces wholesale, so it dissolves on its own and stays out of this batch. setup.md is excluded entirely — its restatements are load-bearing because its sessions may never load the definitions (separate finding). Locate every spot by content, not the audit's line numbers. Folded in at the 2026-06-12 /plan, user-caught: the same Step 2 ordering line names the processing order "oldest first," but Claude-directed placement means file order and age order diverge — an item placed next to its relatives jumps the age queue by design, so the name promises an order the file no longer guarantees. The rename rides here because this batch already edits that line.

Build:
- plugin/si-plugin/docs/plan.md, four restatement spots: the ground-rules "One item at a time" line, Step 2's one-at-a-time/never-preview restatement (keep the ordering content — candidates first, file order, count scope — it's step-specific), the gap-noticing "One at a time," and "don't narrate the absence" after the Test-section [SILENT]. Apply the line above to each. Treat the ground-rules spot with care: no tag sits on the ground rules or Step 1, so the line may be covering territory the [SEQUENCE] definition doesn't reach there — if so, it stays.
- plugin/si-plugin/docs/plan.md Step 2, same ordering line: rename the processing order from "oldest first" to file order, top to bottom. Age order is only the append fallback at filing time (plugin-behaviour.md Captures placement); processing follows the file as placed. Sweep plan.md for other "oldest first" uses describing processing order and rename those too — filing-fallback uses ("oldest-first as the fallback") are correct and stay.

Test:
- Self-verifying from the doc text. Behavioural watch on later /plan sessions: one-at-a-time discipline holds without the trimmed prose; any leakage is a mandatory capture.

**Ship freeform: a fourth /next type for unqueued work** **[ship-freeform-next-type]**

Demand is observed, not speculative: twice in one day the work had no plugin path — an ad-hoc audit run with the plugin switched off, and a session that wanted captures surfaced without processing pressure — plus a general need for somewhere to discuss changes already made. Freeform is the fourth /next type for that work. Two forms ship together. Queue-driven: /plan scopes planned freeform work as a batch and /next picks it up. On-demand: `/next freeform` with no queued batch. Both pass the same gate first — could this be build, test, or audit? — with a one-line answer for why none fit; the gate runs in /plan for queue-driven and at session start for on-demand. Freeform is a refuge from ceremony, not from discipline. The scope lock holds, with files granted ask-by-ask by the user. Captures may be made but never processed — [no-planning-in-execution] already covers freeform through its written scope, no amendment needed. Freeform has no completion signal — nothing to tick — so it gets no Completion section: the session closes when the user runs /done, and the context-running-long nudge is the only close prompt Claude initiates. Expectation over time: recurring freeform shapes surface real new types, the way the audit type emerged. SPEC.md was updated at routing. Absorbs [freeform-on-demand]; both items leave Parked into this batch.

Build:
- plugin/si-plugin/docs/next.md router: add the freeform branch — a queued freeform batch at the top, or `/next freeform` with none. For on-demand, run the gate: ask whether the work could be build, test, or audit; require the one-line why-none-fit before proceeding.
- New doc plugin/si-plugin/docs/next-freeform.md: the procedure. Scope lock ask-by-ask — _build.md's Files list starts empty, and each file the work needs is requested and appended once the user grants it. The captures-append constraint: when the session yields captures, warn that /next can only append them, not process them, and offer the choice — move this to /plan now, or continue and process later. No Completion section. Authored with its response-shape tags correct from birth.
- plugin/si-plugin/docs/done.md router plus new done-freeform.md: record a freeform session — LOG entry describing what happened and what changed, registry check, commit. No batch to return, nothing to tick. Authored with tags from birth.
- plugin/si-plugin/docs/plan.md Step 3: the queue-driven shape — a Freeform subheading for planned freeform work, with the authoring-time gate (one line on why build, test, and audit don't fit).
- plugin/si-plugin/hooks/ lint hook (ships earlier in the queue): add Freeform to the allowed batch subheadings — its own batch notes this list must grow when new types ship.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: describe the freeform form in the workflow section.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what a freeform session is, when to reach for it, and what it won't do (process captures).

Test:
- Self-verifying from the doc text for structure. Behavioural: the next real freeform need runs through `/next freeform` instead of switching the plugin off — the originally observed case is the natural live test. Host-side (after push + reinstall) — flag at /done if it can't run; needs the deferred-test discipline.

**Memory gets boundaries: enumerate what it must never hold, free the rest** **[memory-rule-boundaries]**

User direction, 2026-06-11. The route-observations rule's memory clause ("Not to memory, not discussed and dropped") is a blanket veto with no boundary, which makes it both too strong and too weak: it reads as forbidding memory entirely, while giving a weak model no list to check against. The tightened form enumerates what memory must never hold — project records that system docs own — and explicitly frees memory for everything else. Must-not-hold: behaviour observations and testing outcomes (Captures), design decisions and their reasoning (QUEUE, SPEC, LOG), project state and constraints (the method docs), procedure gaps noticed mid-session (Captures). Free: user preferences, working style, communication feedback, cross-project facts. Resolved at routing: consumers get their own version — their Claude has the same memory feature and a worse misroute risk, since memory is invisible to them, unversioned, and machine-local; a design decision saved there never reaches their project docs. Files over memory, in consumer clothes.

Build:
- This project's CLAUDE.md (host-only, does not propagate), the route-observations rule: replace the blanket "Not to memory" with the enumerated must-not-hold list and the explicit freed remainder, as above.
- plugin/si-plugin/docs/plugin-behaviour.md: add the consumer-facing version, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — project records belong in the project's docs, never in Claude's memory: ideas and discoveries to Captures, design decisions to QUEUE and SPEC, project state to the method docs. Memory stays free for what no project doc owns: user preferences, working style, communication feedback, cross-project facts. The why: memory doesn't travel with the project and the user can't read it; the method docs are the project's record.

Test:
- Self-verifying from the rule text. Behavioural watch: the next session where an observation or decision surfaces mid-work routes it to the docs, and memory use for preferences continues without hesitation.

**/done reads _build.md unconditionally; memory enriches, never substitutes** **[done-unconditional-read]**
Depends on: [scope-boundary-rule]

Raised by the user (2026-06-12): people may /clear between a skill's work and /done, even if advised not to. /clear can't be hooked before it happens, and blocking it isn't the design anyway — the files must suffice at that seam. The observed slip: the last /done skipped the mandated _build.md read, plausibly a judgment call because the whole build session was in memory. That call works same-session and breaks exactly when it matters — post-/clear and post-compaction, when the session feels remembered but the details are gone. A "read it if you don't remember the session" condition was considered and rejected: it hangs on Claude assessing its own memory, which fails in the post-compaction case. The decided form inverts it: the read is unconditional, and conversation memory enriches the record but never substitutes for the read. Side benefit: a same-session /done that reads the file while still remembering the build notices when ticks or Changes notes don't match what happened — the only routine check _build.md's quality ever gets before a fresh session needs it. The findings steps in all three sub-docs name "the conversation" as a source, which institutionalizes the memory dependence; they get reworded so files are the record. The dependency is real: [scope-boundary-rule] is what routes Claude-noticed discoveries to Captures at the moment of noticing, making "flagged items are already in files" true for the reworded findings steps.

Build:
- plugin/si-plugin/docs/done.md, the router's "_build.md exists → read it" line: harden into the canonical rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — the read is unconditional regardless of what the session remembers; conversation memory enriches the LOG entry (tradeoffs, learnings, colour) but never substitutes for the read; a memory-state condition fails post-compaction, when the session feels remembered but isn't. Stated once here; the sub-docs route through it.
- plugin/si-plugin/docs/done-build.md, verify-completion step: add the reconcile line — where the file and session memory disagree (work done but unticked, Changes notes missing something memory knows happened), the mismatch is itself a finding about build discipline and routes to Captures.
- plugin/si-plugin/docs/done-build.md findings step, done-test.md findings step, done-audit.md stragglers step: reword "Check _build.md and the conversation" — the record is _build.md's notes plus Captures already routed at noticing; conversation, when present, is a same-session bonus sweep, never a source the step depends on. Locate by content, not line numbers.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — "Is it safe to clear the conversation or start a new session between steps?" After /done, yes: everything is recorded and committed. Before /done, the plugin recovers from its working file, but closing with /done first is the clean habit.

Test:
- Self-verifying from doc text for the rewording. Grep "and the conversation" across the /done sub-docs after the edit — expect zero hits in findings steps.
- Behavioural, host-side (after push + reinstall): the next /done that runs in the same session as its build visibly reads _build.md before Phase 1. Needs the deferred-test discipline — flag at /done if it can't run.

**Commit messages derive from the LOG entry: two authored texts, four renditions** **[closeout-text-collapse]**
Depends on: [approval-display-blockquotes]

From a capture filed at the 2026-06-12 /done close. /done authors four renditions of the same session facts — index entry, LOG entry, commit title, commit body — and the user sits through each. The renditions correlate in pairs: the index entry and commit title are both one-liners; the LOG entry's rationale and the commit body are both the session story. The collapse makes each correlation literal. Two texts get authored: the one-liner (usually pre-existing — /next generates it as the index entry candidate) and the rationale prose. The one-liner serves as entry heading, index line, and commit title. The rationale serves as entry body and commit body. The user approves the LOG entry once; everything else derives mechanically with nothing new to read. The commit-time ask survives only for the real decision it carries — commit and push, or just commit. Weighed and rejected at routing: dropping the index in favour of reading git log — the index is curated (one line per session; history is full of push-ritual and bump commits), its line ends with the entry filename so retrieval is one hop, and post-collapse it costs nothing to keep, being a mechanical copy of approved text. Also rejected: backfilling old commit messages — rewriting a message changes that commit's hash and every descendant's, invalidating every hash the system has recorded, and needs a force-push the file-safety rules ban; unnecessary anyway, since LOG entries are committed files and the why-pipeline already lives in git as content. One correction recorded from the capture: git log -S searches diff content, not commit messages, so commit-title choice never affected the hash backfill — that consideration is neutral. Commit-title length conventions are already moot in this repo's history. The Depends on is file-collision ordering, not semantic: [approval-display-blockquotes] rewrites the commit core's presentation step (its confirmed offender is the fenced commit message), and this batch reshapes the same step after it. The post-close-captures capture still in Captures interacts — a single text finalizes earlier, widening that gap — and is deliberately left to its own routing, aware of this decision. Folded in from a capture at the plan-2026-06-12-4 /done (e51cf40): the collapse makes multiline commit bodies the norm, and the first such commit broke when passed inline. The capture's stated cause — "PowerShell 5.1 has no heredoc" — is wrong; PowerShell has here-strings (`@'...'@`), but their column-0 closing-token rule makes a generated multiline `-m` string brittle to produce correctly, and the session fell back to the Bash tool. The real lesson is broader than one shell: inline multiline strings are brittle to generate anywhere. The fix is therefore one unconditional mechanism, not a per-shell branch — write the message to a file and commit with `git commit -F`, which sidesteps quoting on every machine and matches the weak-model design target of no which-shell judgment. Folded in from a capture at the [audit-definition] /done (ef3220a), the first live run of the derived message: Claude presented the body as a description of the derivation ("the rationale as approved, plus one appended line…") rather than stating the identity plainly, and the user couldn't tell what had been done — a meta-description reads as a third text existing, defeating the nothing-new-to-read point. The presentation must state the identity in plain words and show only what is genuinely new.

Build:
- plugin/si-plugin/docs/done.md commit core: replace "Draft the commit message title and body" — the title derives from the entry's one-liner, the body from the entry's rationale prose; the entry approval already covered both, so the commit step asks only the commit-and-push question, never a fresh review. Present it by stating the identity plainly — the title is the index line's text verbatim, the body is the approved rationale verbatim — and showing only what is genuinely new, never a meta-description of the derivation. Allowance: when the commit stages extras beyond the session story (hash backfills, sweep edits, rolled-in user edits), the body appends one line naming them, and that appended line is the one genuinely-new text the presentation surfaces.
- plugin/si-plugin/docs/done.md commit core: state how the commit message is passed — write it to a file and commit with `git commit -F <path>`, then remove the file; one shell-agnostic mechanism, not inline `-m` with embedded newlines and not a heredoc branch. Flag for the build to verify: the message file must be writable at commit time despite _build.md's scope-lock — resolve by path choice, by timing (if _build.md is already deleted at the commit step), or by how the file is written.
- plugin/si-plugin/docs/done.md LOG entry files section: state the one-text identity once — the entry heading's one-liner, the index line's body, and the commit title are the same authored text in three positions.
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, done-plan.md, entry-approval steps: one line each — this approval also covers the commit message, which derives from this text; points at the commit core's statement.

Test:
- Self-verifying from doc text. Behavioural, host-side (after push + reinstall): the next /done runs one entry approval, then a commit step showing a derived title and body with only the commit-and-push ask. Needs the deferred-test discipline — flag at /done if it can't run.

**Post-close captures update the entry's routed line as a working-tree edit** **[post-close-capture-record]**

From a capture raised at the [doc-crossrefs-by-name] /done close (2026-06-12). Captures filed in a session's post-commit tail have no session record: the LOG entry's "Routed to Captures:" line is approved and committed before they exist — that session's entry said "none" while two captures originated in its tail. The fix reuses an existing pattern. When a capture is filed after the commit, the same move that appends it to QUEUE.md also updates the just-written entry's "Routed to Captures:" line as a working-tree edit, with no separate commit — the edit rides into the next session's commit, exactly as hash-backfill edits do. The entry converges to truth and attribution stays with the session the capture came up in. Checked at routing: the hash backfill resolves the entry's commit from committed history, so the uncommitted edit doesn't disturb it. Weighed and rejected: recording tail captures in the next session's entry — cross-entry attribution relies on the next session noticing, a judgment step on the path weak sessions fumble, and the log records captures by when they came up; a dedicated follow-up commit per tail capture — truth-preserving but adds ceremony exactly where the session is winding down, and tail captures arrive in clusters; accepting the gap — the capture's inline origin makes QUEUE.md a sufficient record, but it leaves the session entry knowingly false on one line. Interaction accepted: with [closeout-text-collapse], the committed copy of the entry (and commit body) permanently says what was routed as of commit time, while the entry file — the canonical record — carries the correction; git shows the correction landing in the next commit. No dependency header: the design works whether or not the collapse has shipped — adjacency, not a gate.

Build:
- plugin/si-plugin/docs/done.md, beside the LOG entry files section: add the post-close captures rule — a capture filed after this session's commit also updates the just-written entry's "Routed to Captures:" line, as a working-tree edit with no separate commit; the edit rides into the next session's commit, same pattern as the hash backfill. Carry the why: the entry is the session's record, and captures belong to the session they came up in.

Test:
- Behavioural, host-side (after push + reinstall): the next post-close tail capture updates the entry's routed line uncommitted; the next session's commit carries both; the hash backfill still resolves the entry to its /done commit. Needs the deferred-test discipline — flag at /done if it can't run.

**Recommend-next states the scan result both ways: clean case codified, audit gap absorbed** **[done-recommend-next-both-ways]**

Raised by the user at the [doc-crossrefs-by-name] /done (2026-06-12): the close-out assessment has been landing well, but only half of it is codified. The recommend-next step in the /done sub-docs runs the unprocessed-Captures overlap scan and speaks only when something blocks — overlap found → recommend /plan and name it. The clean case (captures waiting, none touching the next batch, /next can proceed) has no instruction behind it: "the three waiting captures don't touch it, so nothing blocks it" was judgment, not procedure. That's the [short-session-design-target] gap class — behaviour the user values, carried by session finesse, which a fresh weak-model session may not reproduce. The fix states the scan's result in all three states: Captures empty (nothing waiting for /plan), waiting but clean (what's waiting, with the plain verdict that nothing blocks), overlap found (the existing rule). The clean-case line reads as plain assessment, not a hedge. Absorbed: [done-audit-overlap-scan], from a [close-out-audit] finding (e120f3d) — done-audit.md is the only sub-doc whose recommendation skips the scan entirely; the gap bites when an audit routes nothing, since pre-existing captures overlapping the top batch would go unflagged and the close would recommend /next, the exact case the scan exists to catch. Folding it here lands the scan and the both-ways rule in done-audit.md in one pass and keeps the wording identical across all four sub-docs.

Build:
- plugin/si-plugin/docs/done-build.md, done-test.md, done-plan.md, recommend-next steps: extend the overlap-scan instruction to state the result either way — what's waiting for /plan (empty, or the waiting items) and whether it blocks the next batch. The clean case is a plain assessment; include one good/bad example pair pinning the tone ("Three captures are waiting; none touches the next batch — nothing blocks it," not a hedge about overlap possibly being worth checking). Identical wording in all three. Locate by content, not line numbers.
- plugin/si-plugin/docs/done-audit.md Phase 3, nothing-routed branch: add the overlap scan with the same both-ways rule and wording — the scan and the result statement land together in one edit, absorbing [done-audit-overlap-scan].

Test:
- Self-verifying from doc text. Grep the scan phrasing across the four /done sub-docs after the edit — expect four identical statements including the both-ways result line.
- Behavioural, host-side (after push + reinstall): the next /done close states the waiting-captures verdict in the clean case without prompting. Needs the deferred-test discipline — flag at /done if it can't run.

**Define the staleness-flag fix path: pointer drift fixable at close, fate decisions to /plan** **[staleness-flag-fix-path]**

Observed at the [setup-preexisting-content-handling] /done close (dc4bfee): the staleness sweep flagged two drifted line references in [setup-project-agnosticism-sweep] — the build's new Case B section had pushed setup.md's line numbers down — and Claude offered to fix them in-session with approval, the edit riding into the commit. The flag is codified (done sub-docs' §2.2 sweep says "flag, don't edit without asking"; plugin-behaviour.md's staleness watch defines the review as drop/rewrite/keep). The fix path is not: nothing says whether a flagged item is fixed at /done with approval or waits for /plan, so the move was ad hoc judgment inside the "without asking" parenthetical. The resolving distinction is sharper than mechanical-vs-judgment: the drop/rewrite/keep review is a fate decision about whether the item is still valid, and fate decisions are /plan's, always. But a drifted pointer on an otherwise-valid item — a line or location reference whose target content is unchanged — is not a fate decision; it's maintenance, and may be fixed at the flagging moment with approval, riding the current commit, the same ride-along /done already does for hash backfills and rolled-in user edits. A content change in the referenced material (the quoted wording itself moved, signalling the item's premise may have shifted) is not mechanical and goes to /plan. The location-vs-content line is written in deliberately: leaving it out just relocates the ad-hoc judgment to the next quoted-string flag. Scope note: this fix-at-close path is for skills that commit (/done) and /plan; /next's pre-flight stale scan stays surface-and-recommend-/plan, since /next doesn't edit the queue's other batches. Sibling to [plan-resolves-by-default], which states the /plan-side resolve-now rule — complementary, neither gates the other.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, Dependency ownership Staleness watch bullet: extend the canonical rule. The drop/rewrite/keep review is /plan's (a fate decision about the item's validity). A drifted pointer on an otherwise-valid item — a line or location reference whose target content is unchanged — is mechanical maintenance and may be corrected at the flagging moment with approval, riding the current commit, the same ride-along as hash backfills and rolled-in user edits; a content change in the referenced material is not mechanical and goes to /plan. Carry the why: the fate decision needs planning, a moved pointer doesn't.
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, §2.2 staleness sweep ("If so, flag (don't edit without asking)"): align all three to the fix path — flag fate-decision staleness for /plan; offer to fix a drifted pointer here with approval. Point at the plugin-behaviour.md statement rather than restating it. Locate by content, not line numbers (the same line is also tagged by [next-done-tag-sweep]; no ordering between them — locate by content).

Test:
- Self-verifying from doc text. Grep the sweep wording across the three done sub-docs after the edit — expect three aligned statements.
- Behavioural, host-side (after push + reinstall): the next /done staleness flag of a pure pointer drift offers an in-session fix with approval; a fate-decision flag defers to /plan. Needs the deferred-test discipline — flag at /done if it can't run.

**State the single-summary rule in all four /done sub-docs** **[done-single-summary-line]**

From a [close-out-audit] finding (e120f3d). The single-summary rule is stated at five close-outs, but inside the /done sub-docs only done-plan.md carries it at the entry-writing step — done-build.md, done-test.md, and done-audit.md are silent on it. The pull the rule guards against lives exactly there: just after the commit, the natural move is to recap the session while recommending what's next, and a two-sentence recap satisfies the recommend-next [BRIEF] tag while still duplicating the entry. Grep-confirmed at routing: only done-plan.md has the line. The fix copies its exact wording so the rule reads identically everywhere it appears.

Build:
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, entry-writing steps: add done-plan.md's line verbatim — "This entry is the session's summary — there is no separate chat recap." Locate each spot by content (the show-for-approval instruction in each entry step), not line numbers.

Test:
- Self-verifying. Grep "separate chat recap" across the /done sub-docs after the edit — expect four hits, identical wording.

**Fit the push offer to session shape and remote state** **[push-offer-fit]**

From a [close-out-audit] finding (e120f3d), plus one gap surfaced at routing. done.md's commit core asks "Commit and push, or just commit?" identically for every session shape. The dual ask fits build, test, and audit closes — work shipped or was verified, push is a real choice. It misfits planning closes: the staged paths are local planning state, so the standing offer treats planning work as a ship event. In the self-hosting host the cost is concrete — a push triggers the full push-and-rezip ritual off a commit that changed nothing in the plugin. A non-coder reads offered options as equally sensible defaults, so the ask teaches that pushing planning state is normal when the system reserves push for shipping. The routing-time gap: consumer repos may have no remote at all — nothing in setup or install creates one — so the ask can offer an option that errors when picked. The fix keeps the mechanics canonical in done.md and shapes the ask by context. The override is a default, not a prohibition — for consumers push is often just backup, and that stays available. Setup-shaped sessions inherit the override for free once [setup-closeout-redesign] routes them through done-plan.md.

Build:
- plugin/si-plugin/docs/done.md commit core: gate the push offer on a remote existing (one git remote check). No remote: ask about committing alone — don't offer what would error.
- plugin/si-plugin/docs/done.md commit core: add one line stating sub-docs may override the ask's default while the mechanics stay canonical here.
- plugin/si-plugin/docs/done-plan.md commit step: override the ask — planning sessions offer commit alone by default; push stays available when the user asks or is deliberately backing up. Carry the why: planning state is local bookkeeping, push is reserved for shipping, and in self-hosting projects a push triggers the full push-and-rezip ritual.

Test:
- Self-verifying from doc text. Behavioural, host-side (after push + reinstall): the next /done after a planning session asks commit-only; a /done after a build still offers the dual ask. Needs the deferred-test discipline — flag at /done if it can't run.

**Define next-test.md's completion review tail** **[next-test-review-tail]**

From a [close-out-audit] finding (e120f3d). The three /next-family completions share one shape — "Run /done to record this and commit, or X before closing" — but only next-build.md defines its X, and that definition exists deliberately to close a new-work-smuggling risk: an undefined tail can absorb fresh work past the batch's contract. next-test.md's "review what's already tested" carries no equivalent definition, so the same risk sits open there. The audit half of this finding rides in [audit-findings-bulk-approval], which rewrites next-audit.md's close; this batch covers the test half, mirroring next-build.md's wording so the rule reads the same in both places.

Build:
- plugin/si-plugin/docs/next-test.md Completion, after the "Run /done…" say-line: add the definition — reviewing means re-examining what was already tested, not raising new work; anything new routes through the existing paths (out-of-scope via Scope management, thinking work via Captures). Mirror next-build.md's tightening definition in structure and length.

Test:
- Self-verifying from the doc text. The two defined tails should read as the same rule in build and test clothing.

**Push marker: one hard direction, otherwise a ship-by aim** **[push-marker-hard-direction]**

The push-marker convention reads as a solid barrier, but it's only hard in one direction. Decided-but-unshipped standards already shape sessions before any push — in-repo sessions read the queue and the discussion, not just the installed plugin (observed 2026-06-12: blockquote displays, verbatim-first quoting, a why-pipeline judgment call, all applied pre-push). The genuinely hard case is host-side reads: work that reads installed state — an audit reading injected rules, a live test of hook behaviour — gets wrong results before push + reinstall, and the /next halt exists to protect exactly that. Left undistinguished, the risk is a session treating the line as solid and suspending decided reasoning ("not shipped yet"), which breaks the why-pipeline. Decided rationale never waits on a push.

Build:
- This project's CLAUDE.md (host-only, does not propagate), the push-marker convention in Self-hosting dependency ordering: state the distinction — the marker halts /next because batches past it read host-side state, the one hard direction; it does not suspend decided rules or reasoning in any session, and it is not a wall for planning work. The line marks when we aim to ship by. Decided rules and reasoning apply from the moment they're decided.

**Remove dash-stripping from the scope-lock parser: bare paths become the single truth** **[scope-lock-drop-dash-stripping]**

The scope-lock parser strips trailing annotations from Files: lines when a dash separator is used (" — ", " - ", " – "), but not parenthetical ones. The code is partially tolerant while the decided rule says bare paths, nothing else on the line. The split is the worst spot: a dash-annotated line works silently, so the annotating habit never gets corrected, then a parenthetical one breaks scope mid-build. The denial message shipped by [git-add-safety-hook-gap] teaches that any annotation breaks the match — the dash-stripping makes that false for one annotation style. Removing the stripping makes the rule, the denial message, and the parser agree. The teaching denial is the recovery path for anyone who annotates a line. Side benefit: a genuine path containing " - " no longer gets truncated by the stripper. _build.md is ephemeral — each build writes a fresh one — so nothing needs migrating.

Build:
- plugin/si-plugin/hooks/pre_tool_use.py: remove the dash-stripping loop from the Files: parser — entries are taken whole after the leading "- " marker. No other parser behaviour changes.
- Verify, no edits expected: the scope-lock denial text and next.md's _build.md format section already state the bare-path rule and stay accurate once the stripping is gone.

Test:
- Claude-run: pre_tool_use.py against a fixture _build.md — a dash-annotated Files: line is denied with the teaching message; a bare path still passes; an empty Files: section still locks to method docs.
- Host-side (after push + reinstall): a live denial on an annotated line. Needs the deferred-test discipline — flag at /done if it can't run.

**Audit narration volume at skill openings** **[opening-narration-audit]**
Depends on: [plan-step1-sequencing]

Raised 2026-06-14. Narration has been piling up at the start of skill sessions, and the cause looks structural: a skill's opening is where the most rules fire at once — the read-state step, the unpark and staleness scans, and several behaviour rules that each independently say "narrate" (narrate the ordering work, surface unpark candidates, flag staleness). Each was added for good reason, but nothing bounds the total, so they stack into a wall of opening narration. [output-tag-audit] already checked tag placement across all docs, and its fixes are the queued tag batches; this audit asks a different question it never measured — how much narration accumulates at one opening, and whether the fix is a tag or a rule. It depends on [plan-step1-sequencing] because that batch cleans /plan's opening, the flagship example, so auditing afterward reads the intended state instead of re-finding a queued fix.

Audit:
- Target: the opening sequences of all four skills as written in the procedure docs — setup.md's entry, plan.md Step 1, the next family's pre-flight opening, the done family's openings — plus the plugin-behaviour.md rules that drive opening narration (narrate the ordering work, the unpark watch, the staleness watch, dependency-ownership narration). If the same pile-up appears at any other high-rule-density moment while reading, report it too.
- Criteria: at each opening, separate narration the user genuinely needs (the entry question, a real unpark candidate, an actual ordering decision) from accumulated excess (scan and process narration, state restatement, over-explaining). For each excess moment, name the lever — a missing [SILENT] or [BRIEF] tag on the step, a tag that needs changing, or a behaviour rule that fires narration with nothing bounding the total when several stack on one opening. Flag especially where multiple rules pile onto the same opening — the aggregate problem per-step tagging can't catch. Where a queued fix already addresses an opening ([plan-step1-sequencing], [output-tag-audit]'s findings), note it as covered and don't re-file.

**Backfill the FAQ folder this project never scaffolded** **[faq-backfill]**

This project is missing its `FAQ/` folder — the `faq.md` and `index.md` that /setup scaffolds from templates. The cause: the FAQ scaffolding step was added to /setup after this project was first set up (commit `06c24e4`), and /setup was never re-run here, so the folder was never created. Nothing automatically re-scaffolds this project when the plugin gains new scaffolding, so the gap stayed silent.

This batch backfills the FAQ from the current templates, so the dev project has the FAQ that consumers get and can dogfood FAQ edits. It is placed late on purpose: several queued batches add FAQ entries to the templates, so running it after them captures a more current snapshot instead of one that is stale on arrival.

Two caveats are accepted, not solved here. This is a point-in-time copy, not a synced one — it will drift again as later FAQ-template edits land, and there is no detection because `.si-version` is deliberately left to the separate self-hosting design item. And once `FAQ/index.md` exists, the session-start hook injects it into every session start — small and by design, but the narration audit should treat that injection as in-scope here.

Build:
- Create the `FAQ/` folder in the project root.
- `FAQ/faq.md` — copy the current content of `plugin/si-plugin/templates/faq-template.md`.
- `FAQ/index.md` — copy the current content of `plugin/si-plugin/templates/faq-index-template.md`.

Test:
- Self-verifying: `FAQ/faq.md` and `FAQ/index.md` exist and match the current templates. The next session start will then inject `FAQ/index.md` — observable, minor.

**Brevity is a user-needs requirement, not a style preference: "be thorough" must not mean burying the user in text**

The plugin's users are non-coders who keep Claude on track by reading and approving what it does — drafts, captures, LOG entries, commit decisions, design choices. That control only works if they can actually get through the text. When an exchange runs long, attention can't hold; the user skims, and real problems in their own project slip past unnoticed for many sessions. Thoroughness that buries the signal defeats itself, and defeats the plugin's core job of keeping the user in control. Unreadable output is unapprovable — the human can't catch an error they can't get through.

So this is a requirement of the method, not a personal taste. "Be thorough" should mean "surface every important thing the user must see and act on," never "emit every word." Leading with the one decision the user must make, then stopping, serves thoroughness better than a complete-but-unread wall — the user gets the crucial item instead of wading past it.

It is fixable, and the current approach is the weak form. Research in resources/research/opus-4-8-verbosity-steering.md found that abstract, negative brevity instructions (the plugin's [BRIEF]/[SILENT] tags and "don't bundle" rules) are exactly what Opus 4.8 steers on least, while positive, quantified, exemplified instructions — plus an output structure that leads with the decision and gates detail behind an explicit request — do steer it. A Claude Code output style can carry these at system-prompt priority instead of competing at user-message priority. For /plan: redesign the verbosity rules on those lines. This is design input for [output-tag-audit] and [opening-narration-audit], and it corrects the premise in resources/research/model-instruction-compliance.md (the system prompt does not, in fact, mandate thoroughness over brevity).

**Self-hosting build and spec-writing batches should be fulfilled against a strict "4.8-ifying" heuristic**

Going forward, every self-hosting build batch and every spec-writing batch should be carried out against a strict "4.8-ifying" heuristic. As doc, procedure, or SPEC text is authored or edited, it is deliberately shaped to steer Opus 4.8 well — positive and quantified instructions over abstract adjectives, concrete exemplars of the wanted behaviour, explicit scope statements, lead-with-the-decision output structure — so the plugin is written for the model that actually runs it, not against it. This follows the Model target resolution in CLAUDE.md: target 4.8, never downgrade to 4.6/4.7, fix by steering.

The heuristic does not exist yet and must be defined first, before it can be applied. Define it against the two research files — resources/research/opus-4-8-verbosity-steering.md and resources/research/model-instruction-compliance.md — distilling them into a concrete, checkable list that can be run over a batch's output at authoring time (a short "is this 4.8-shaped?" pass). The aim is the best working relationship with 4.8 going forward.

For /plan, this is two steps in order: (1) author the heuristic as its own batch, sourced from the two research files; (2) make it a standing authoring check applied to every build and spec-writing batch. Relates to [output-tag-audit] and [opening-narration-audit], which are the first places the heuristic would bite.

### Parked

## Deferred tests

Planned tests that couldn't run in their own session (host-side, needs-user, external event). /done writes entries here when a test can't run in-session; entries sit here until a session can confirm them (/plan reads this section each session); the session that confirms one removes its line and records the confirmation in its LOG entry.

- [narrate-build-md-purpose] — verify the remaining unobserved narration moment: a one-line opener when a resume reads _build.md (scope-lock narration and rationale-carry confirmed live 2026-06-12). Confirmed by: the first /next that resumes an interrupted build.
- [next-pre-scope-lock-abort] — verify a /next that ends before a build is locked (push-marker halt, blocker-gate stop, or the user calling it off at "Ready?") routes any reshape direction to Captures and names /done, not /plan. Confirmed by: the first naturally-occurring pre-scope-lock end after push + reinstall.
- [drop-log-per-release-split] — verify a "why did we decide X" question targeting a pre-split entry in an old log-v*.md file is answered through the index plus the hash-or-title search fallback (pre-split entries have no per-entry file to open). Confirmed by: the first such why-question after push + reinstall, or a deliberate run any time after reinstall.
- [hash-backfill-as-hook] — verify the session-start hook runs the LOG hash backfill live: the first session opening after a /done that left an unfilled placeholder shows the hook's one-line housekeeping report, the placeholder is filled in the working tree, and archived prose mentioning the token survives. Confirmed by: observing that report and the filled hash in the first post-/done session after push + reinstall.
- [git-add-safety-hook-gap] — verify a live denial on a deliberate git add -A in a scratch context, with the teaching message naming explicit staging and the patterns-as-data note. Confirmed by: the first such denial observed after push + reinstall.
- [narration-vocabulary] — verify user-facing narration stays free of background-only structural terms (loop, Step N, gate, slug names), with the Vocabulary list catching what the abstract rule missed. Confirmed by: narration observed clean against the list in the first /plan or /next session after push + reinstall.
- [setup-preexisting-content-handling] — verify a Case B /setup run peeks at pre-existing content before Q1 (framing clarifier, never a pre-answer) and leaves it untouched during scaffolding while naming it in the closing message. Confirmed by: the first /setup run in a folder with pre-existing content after push + reinstall.
- [red-flags-screen-rule] — verify a genuine data-exposure risk in later work draws a plain-English red flag rather than silence; any miss is a mandatory capture. Confirmed by: the first session where a real data-exposure risk surfaces after push + reinstall.
- [red-flags-structure] — verify a red flag Claude raises lands in QUEUE.md's Red flags section with a state, and an accepted flag's decision appears in the session LOG. Confirmed by: the first red flag raised, and the first flag accepted, after push + reinstall.
- [delete-preflight-deferred-tests] — verify the /next pre-flight no longer lists pending deferred tests before the batch runs. Confirmed by: the first /next pre-flight after push + reinstall.
- [allow-parallel-sessions] — verify opening a /plan chat while a build is active is no longer refused (the active-build session-start message naming planning-alongside was confirmed in-session against a fixture). Confirmed by: the first time a /plan session is opened alongside an active build after push + reinstall.
- [make-drift-visible] — verify a session in a drifted project (missing a scaffolded file/folder) opens with Claude plainly flagging what's out of date and offering /setup, while a current project on a higher plugin version stays silent (the presence-based logic and no-false-alarm were confirmed in-session against fixtures). Confirmed by: the first session in a drifted project after push + reinstall.
- [setup-closeout-redesign] — verify a real /setup run in a fresh folder creates the git repository silently, the close-out names /done, and /done writes a setup-shaped LOG entry and commits the scaffold; a Case C migration close with a leftover _build.md recommends resuming /next instead. Confirmed by: the first /setup run in a fresh folder after push + reinstall. (host-side)
- [approval-display-blockquotes] — verify the next /plan or /done approval draft arrives as a labelled blockquote that wraps (not a fence), and the /done commit step presents title and body as blockquotes with fences gone. Confirmed by: the first /plan or /done approval draft, and the first /done commit step, after push + reinstall. (host-side)
- [show-before-write] — verify a later /plan writes nothing to QUEUE.md without the verbatim entry in the immediately preceding message; the case to watch is late-session, after compaction. Confirmed by: the first /plan batch write in a long/compacted session after push + reinstall. (host-side)
- [session-start-dirty-tree-check] — verify the live one-liner at session start with known dirt and no _build.md (the fixture test — dirty-without-build warns, dirty-with-build silent, clean silent — passed in-session this goal session). Confirmed by: the first session opened with a dirty tree and no active build after push + reinstall. (host-side)
- [plan-state-artifact] — verify the live resume offer: interrupt a /plan mid-processing, open a new session, watch for the "INTERRUPTED PLANNING SESSION" report (the fixture test — _plan.md detected, dirty-warning suppressed with _plan.md present, silent when absent — passed in-session this goal session). Confirmed by: the first interrupted /plan reopened after push + reinstall. (host-side)
- [capture-verbatim-first] — verify that /plan's present-and-interview sends the one-line preamble plus the verbatim item before any analysis (with the post-quote re-read separator), and /next's pre-flight sends the top batch verbatim before the blocker-gate findings. Confirmed by: the first /plan capture turn and the first /next pre-flight after push + reinstall. (host-side)

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

**Retire REGISTRY.md: drop the write-only inventory doc** **[retire-registry]**

Decided 2026-06-13. Remove REGISTRY.md as a project doc. The architecture goes from four docs to three: SPEC, QUEUE, LOG.

Why: REGISTRY is write-only. Grep-confirmed — it's scaffolded at setup, updated at every /done, presence-checked at session start, and listed among the editable "method docs" for the scope-lock, but nothing ever reads its content to make a decision. No read-before-edit gate, no procedure step that opens it. The only justification was a human-facing map for a non-coder. The user — the non-coder it serves — never opens it, and never opened the richer old MANIFEST either. The replacement is better: a non-coder who wants to know what their app contains asks Claude in-session, which explores the live code — accurate, contextual, zero maintenance. This is the MANIFEST echo: REGISTRY kept the inventory after the mechanisms that made it load-bearing (the read-before-edit gate, serves-lines, rationale suffixes) were already dropped.

One nuance weighed and rejected: REGISTRY could in theory give Claude a fast orientation map in a large project. But nothing reads it today, and live search beats a hand-maintained list that drifts — so it doesn't save the doc.

Removal arc — what changes (the build does a full grep sweep so no reference is missed):
- setup.md: stop scaffolding REGISTRY — the template block, the Case B mention, the SKILL.md description line.
- session_start.py: remove the REGISTRY presence check and its method-doc detection.
- pre_tool_use.py, next.md, next-audit.md: remove REGISTRY from the "method docs" editable set wherever that set is listed.
- done.md: drop REGISTRY from staged paths; done-build.md: remove the "Update REGISTRY" step; done-plan.md: drop it from staged paths.
- next-build.md: remove the "REGISTRY.md is not build scope" line.
- plugin-behaviour.md: remove REGISTRY from the doc-routing line and the route-to-artifacts list. While editing the doc-routing line, also reword the SPEC.md description project-agnostic — "what/who/how/why the project exists," not "the product exists" — which carries the folded-in [plugin-behaviour-doc-routing-agnostic] decision (otherwise lost when [setup-registry-template-and-noun] is dropped).
- SPEC.md: remove REGISTRY from the four-docs description (a spec change — rides a spec-edit batch under [spec-edit-batch-type]).
- CLAUDE-TEMPLATE.md and this project's CLAUDE.md: drop REGISTRY from the architecture and doc descriptions.
- faq-template.md + faq-index-template.md: remove the "What is REGISTRY.md for?" entry.
- This project's REGISTRY.md: delete the file.
- Consumer migration: existing adopted projects (e.g. Taskflowapp) have a REGISTRY.md that becomes orphaned — the adopt/setup re-run path should retire it, not leave it dangling.

Queue interactions: moots [setup-registry-template-and-noun] (it reworked the REGISTRY template — now dropped, with its surviving SPEC-side doc-routing reword folded into this capture's plugin-behaviour.md step). [setup-project-agnosticism-sweep] is unaffected — it deliberately holds no REGISTRY item. Relates to [spec-edit-batch-type] (the SPEC portion rides a spec-edit batch).

**Content-level scaffold drift: templates that change after a project is set up** **[scaffolding-resync]**

When a scaffolded file already exists but its template changed later — e.g. a doc template gains a new section — a project that has the file won't pick up the change. [make-drift-visible] catches *missing* files and folders, but not this content-level drift, because the file is present. Open question if this ever bites: how to detect that a present file is behind its template, without a full /setup re-run that would overwrite user content. Lower priority — no instance observed yet; the missing-file case (the one that actually hurt) is handled by [make-drift-visible].

The old framing of this item was wrong and has been dropped: it treated the drift as a self-hosting housekeeping problem tangled up with version-bump noise. The drift is general, not self-hosting (Taskflowapp, a plain consumer project, had the same missing file), and the version-bump false-alarm worry is mooted by [make-drift-visible]'s presence-based check.

---

**Trickle four /next-only rules down out of the every-session injection** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). Four rules live in plugin-behaviour.md — the doc injected into every session — but their triggers only exist during a /next build, so every /plan, /done, and setup session pays for words it can never use:
- "SPEC.md is read-only during builds" (plugin-behaviour.md:103)
- "One build at a time. Never start /next while _build.md exists" (plugin-behaviour.md:104)
- "At build completion, the only valid next-step recommendation is /done" (plugin-behaviour.md:105)
- "If context is long mid-build, suggest completing the current file and running /done" (plugin-behaviour.md:134)

Each keys to _build.md or build execution, which exist only inside /next — none can fire outside /next, and none fire in /plan, /done, or setup. Owning doc: next.md. Roughly 111 words would leave the injection (the build-completion bullet is ~75 of them).

This contradicts the trickle-up direction for these specific rules: that arc moved rules up on "cross-skill belongs in the injection," but single-skill rules don't earn it. Action for /plan: author a trickle-down batch moving these to next.md as canonical, each carrying its rationale per the why-pipeline.

Two interactions to handle when authoring:
- [trickle-up-next-md-duplicates] (queued) plans to DELETE next.md's copies of "SPEC read-only" and "one build at a time," leaving the injection as their sole home — the opposite of this finding. Amend that batch (or carve these two out of it) before it builds.
- [spec-edit-batch-type] (capture) would remove the "SPEC.md read-only during builds" rule entirely (SPEC becomes a normal doc governed by scope-lock). If it promotes, the SPEC-read-only trickle-down is mooted — sequence accordingly.

**Spec-entry pipeline rule is /plan-only — make plan.md canonical, drop the injection copy** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). The spec-entry pipeline rule at plugin-behaviour.md:100 — "New features need a spec entry before a build entry. Pipeline: idea → question (if unclear) → SPEC.md → QUEUE.md. Threshold: if a user would see or experience the difference, update SPEC.md first" — fires only in /plan. The pipeline (idea→question→SPEC→QUEUE) is /plan's authoring sequence; a feature idea captured elsewhere just gets filed, and nothing runs the pipeline until /plan picks it up. It's already restated in plan.md:17, so the injection and plan.md carry two synced copies. ~33 words sit in the injection.

Single-skill (/plan). Owning doc: plan.md. Action for /plan: make plan.md the single canonical home and drop the behaviour.md copy, rather than maintaining two synced versions.

Two interactions to handle when authoring:
- [spec-entry-trigger-rethink] (queued) rewords BOTH copies to keep them aligned. If plan.md becomes canonical, that batch should target plan.md alone — fold this decision into it rather than letting it re-sync two copies.
- [spec-edit-batch-type] (capture) would rewrite the pipeline to "idea → decide in /plan → spec-edit batch → /next edits SPEC → feature batch," adding a /next stage and pushing the firing map from single-skill to two-skill (plan + next). If it promotes, the home question changes — decide after its disposition is known.

**Middle-band rules (2–3 skills) in plugin-behaviour.md — firing data for the restructure decision** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). These rules fire in two or three skills but never outside a skill — so they don't earn the every-session injection on the "fires outside skills" test, but they aren't single-skill trickle-down candidates either. Recorded as data for the progressive-disclosure restructure, not moved (the audit proposes no move for this band).

The band:
- Index entries (plugin-behaviour.md:82-93) — 3 skills: /plan readiness gate (plan.md:105), /next pre-generate (next.md:29), /done writes it (all done sub-docs). The retrieve path reads the index but doesn't apply the authoring rule.
- Unpark watch (plugin-behaviour.md:112) — 3 skills; self-names its firing sites (/plan read-state + loop, /next pre-flight, /done close-out).
- Staleness watch (plugin-behaviour.md:113) — 3 skills, "same surfacing moments." [staleness-flag-fix-path] (queued) extends it — same band.
- Empty Batches → /plan (plugin-behaviour.md:106) — 2 skills (/next pre-flight, /done recommend-next).
- User owns scope (plugin-behaviour.md:118) — 2 skills (/plan promote-park-drop, /next whether-to-proceed). [scope-anchor] rewords it.
- Resume reads _build.md (plugin-behaviour.md:135) — 2 skills (/next resume, /done reads it).
- /plan-for-planning, /next-for-building (plugin-behaviour.md:99) — 2–3 skills; boundary rule.
- Borderline /plan-only authoring read cross-skill: Depends/Blocks headers (plugin-behaviour.md:115), stable slugs (plugin-behaviour.md:117) — authored in /plan, referenced when read elsewhere.

Why it matters: this band is what the restructure is for — compact core injected with the fuller doc loaded at skill time, or a shared sub-doc the relevant skills load, or canonical-in-one with a read-on-demand pointer. That decision is parked in [behaviour-doc-size-watch]; this record is the firing data it should be decided on, instead of a guess. No move now — fold into that item when it fires.

**Queued plugin-behaviour.md additions whose firing maps are narrower than every-session** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). The audit checked every queued batch whose build entries add or reword rules in plugin-behaviour.md (the every-session injection). Most plan correct homes — their rules fire outside skills via capture-making, approval moments, or memory-routing ([red-flags-screen-rule], [approval-display-blockquotes], [approval-ask-after-draft], [human-readable-authoring], [memory-rule-boundaries], and the Dependency-ownership trio). Four plan injection homes for rules whose triggers are narrower:

- [scope-anchor] — the Scope statement (build scope = the active batch's entries' work; the Files: list is its mechanical approximation) fires in /plan (entries name files) and /next (scope-lock, expansion asks) = 2 skills, not outside any skill. Planned for the injection.
- [scope-boundary-rule] — the discovery decision rule (needed→ask/split; not needed→capture; premise broken→halt) is /next execution, planned canonical-in-injection with next-build/next-test pointers. It also rewrites the current "Don't fix things outside current scope" rule (plugin-behaviour.md:101), itself /next-execution — deepening an execution rule's injection footprint.
- [no-planning-in-execution] — mixed: the prohibition ("no capture-processing in execution skills") fires in /next; the permission ("capture-making is open to every session type") is genuinely universal. The prohibition half is narrower than every-session.
- [audit-findings-bulk-approval] — the bulk-approval inversion fires only in /next-audit, but is added to the universal sequencing rule as an exception. Borderline: an exception co-located with its universal parent has merit.

Action for /plan: weigh each home against the firing map before these batches build — not to override their own reasoning, but so the injection-vs-skill-doc choice is made deliberately. [scope-anchor] and [scope-boundary-rule] are the clear candidates to reconsider (plan+next / next-only); [no-planning-in-execution] and [audit-findings-bulk-approval] may justify injection anyway. This is the reason the audit was placed above the rule-adding batches.

**README: separate the four-commands intro line and add a best-practice usage cycle**

Observed by the user, 2026-06-14. Target is README.md at the repo root — the GitHub landing page, not a file inside the plugin package, so it's edited directly and doesn't propagate through reinstall.

Two changes wanted in the "What it does" section:
- Reword the intro so the claim and the list are separate sentences. "…walks you through it with four slash commands:" becomes "…walks you through it. It has four slash commands:".
- Add a best-practice usage section under the command list: /setup once only; then repeat the cycle of /plan → /done → /clear and /next → /done → /clear; with /plan → /done → /clear repeated as many times as needed for long-running planning.

Why it matters: a non-coder reads four one-line command descriptions but can't infer the rhythm. This cycle is how the user will present real-world use demos, and the README should teach the same pattern to anyone who isn't watching them — mirroring what the demos show. It also keeps the repo honest. The four commands look like something you can pick up and use freely, but a fair bit of invisible process sits on top — not a huge amount, but enough that skipping the rhythm gives you a bad time. The load-bearing habit is closing every session with /done before /clear: the design relies on each session being recorded before the context is cleared. Presenting the commands without the cycle oversells how freely they can be used and drifts from how the demos present it.

To settle when this is promoted: the paired-cycle layout can read as strict one-/plan-then-one-/next alternation. In practice /next repeats across many batches between planning sessions, so the final wording should make /next-repeats as visible as /plan-repeats.

**Self-install branch in the guided install: let Claude Code install SI via terminal**

Raised by the user, 2026-06-14, building on the existing guided install (INSTALL.md). For repo visitors who already have Claude Code, add a branch where Claude Code installs the SI plugin itself via the terminal, instead of the human doing the GUI zip-upload (Customise → Create a plugin).

Mechanism is confirmed (research: resources/research/claude-code-plugin-install-mechanisms.md). The desktop app's Code tab is Claude Code with an integrated terminal, and there is a non-interactive `claude plugin install <name>@<marketplace>` command the agent can run. So Claude Code can do the install in both the CLI and the desktop app.

Two things shape how this branch must be written:
- INSTALL.md is consumed by a claude.ai chat, which has no terminal — it can only instruct the human, not run the install. So this branch is a handoff: the already-has-Claude-Code user is routed to run the install through Claude Code itself, not through the claude.ai guide. This overlaps the experienced-user bypass queued in [install-separate-ai-instructions] and the app-identification check in [install-app-identification-check] — likely the same branch point.
- Prerequisite: the clean install command installs from a marketplace, and SI's repo has no marketplace manifest today. The repo must publish `.claude-plugin/marketplace.json` pointing at si-plugin before `claude plugin marketplace add FlintCraftTech/sovereign-implementer` + `claude plugin install` will work. The raw-local-zip alternative is the unreliable path (open upstream feature request). So this idea carries a prerequisite build: publish the marketplace manifest.

Ripple for /plan to weigh at promote time: publishing a marketplace manifest makes "add our marketplace and install" the standard, robust install flow, which could simplify or partly moot some queued INSTALL.md batches (all of which assume the GUI zip-upload). Decide the interaction with those batches when this is promoted.

**SI teaches the user the working rhythm in-product, not just in the README**

Raised by the user, 2026-06-14, sibling to the README usage-cycle capture above. That capture puts the /setup-once-then-cycle rhythm on the repo front page for visitors. This one is the in-product counterpart: SI itself should show the user the rhythm during use, so someone who installed SI without reading the README still learns it.

Same content as the README capture (the cycle: /setup once; then repeat /plan → /done → /clear and /next → /done → /clear, planning repeated as needed). Same why: the rhythm is load-bearing and not inferable from the four one-line command descriptions — every session closes with /done before /clear so it's recorded before the context is cleared. Different surface: in-product teaching, not a repo-front-page reference.

Candidate homes (to settle at promote time):
- The /setup close-out — the natural onboarding moment, right after scaffolding, when the user is about to start the cycle. This interacts directly with [setup-closeout-redesign], which is already rewriting that close to recommend /done; coordinate with or sequence after it.
- A FAQ entry (faq-template.md + index line) as the durable in-product reference the user can return to.
- Not session-start: the rhythm is onboarding teaching, and repeating it every session would be noise.

Authoring note: the setup close-out and FAQ are user-facing (external non-coder), so the rhythm must read in plain English with no internal terms, and the cycle wording should stay consistent across the README, the setup close-out, and the FAQ.

**Hook-count descriptions lag the QUEUE.md lint hook**

Found during the v1.12.0 pre-push consistency sweep, 2026-06-14. This project's CLAUDE.md Architecture section enumerates "2 hooks (session_start, pre_tool_use)," but post_tool_use.py — the QUEUE.md structure lint, shipped after v1.11.0 — makes three hook files. SPEC.md's "Two hooks enforce discipline mechanically" is arguably still accurate, because the lint hook advises rather than enforces. So this is a framing decision, not a clear error: update CLAUDE.md's enumeration to three, and decide whether SPEC should mention the advisory lint hook at all. Host-only / this-project docs; nothing consumer-facing was stale (CLAUDE-TEMPLATE.md and faq-template.md don't enumerate hooks).

**Deferred tests vs test batches: do two mechanisms earn their keep?**

Raised by the user, 2026-06-14, during a /next pre-flight. The user didn't follow what the Deferred tests section is for. Her model: all user-run testing gets queued as a Test batch. So a separate floating list of tests read as redundant.

The boundary between the two really is fuzzy. A test batch is a whole /next session of testing only the user can do. A deferred test is a single leftover line from a build batch's Test part that couldn't run at build time — usually because the change is host-side and only goes live after reinstall, or because it waits on an external event. Most deferred tests get confirmed just by watching the next real session. But a few are active user-run actions (e.g. deliberately trying `git add -A` to confirm the denial), and those overlap directly with what a Test batch is for.

The section also looks far larger than it really is because this project is the plugin building itself. Almost every change here is host-side, so almost every test defers. A normal consumer project would barely populate this section — its tests would be "Claude checks now" or a queued Test batch.

For /plan to weigh: is the deferred-test mechanism distinct enough from Test batches to keep as its own section, or should the user-run ones fold into Test batches and the passive-observation ones be reframed? One signal worth carrying: if the section confuses the person who built the plugin, it will confuse external consumers too.

Touches /next's pre-flight (re-presents deferred tests) and /done (writes them). Citation, not a blocker.

**/setup on the dev project: two test outcomes + a cross-session contradiction about what /setup actually fixes**

Observed 2026-06-14, triggered by the user running `/setup` in this project (the self-hosting dev project) root. /setup detected Case C with a missing `.si-version` and routed to migration scaffolding. Two test outcomes, plus a contradiction the user surfaced.

**Outcome 1 — /setup is consumer-framed and an awkward fit on the self-hosting dev project.** The procedure's framing is "the method is being applied to *their* project" — written for a consumer adopting the method, not for the project that *develops* it. Running it here surfaced two frictions: (a) the host/target oddity isn't acknowledged anywhere in the flow, and (b) the migration step would scaffold a `FAQ/` folder this project never adopted, which would immediately make CLAUDE.md's "Where things live" tree (lists only SPEC/QUEUE/REGISTRY/LOG) stale — scaffolding creating a fresh drift. Concrete state found: this project is missing `.si-version` (never created, not gitignored, never committed) and `FAQ/`; CLAUDE.md also carries pre-existing drift ("Target v1.11.0" in two spots vs plugin.json 1.12.0; "2 hooks" vs three hook files — the latter already captured separately in the hook-count item above).

**Outcome 2 — cross-session overpromise: "run /setup to bring everything up to standard" is wrong.** A prior session told the user everything is out of date and the only way to bring things up to standard is to run /setup. That oversells what /setup does. Migration scaffolding (setup.md Step 2C) only backfills *missing* scaffold files and stamps `.si-version` to the current version — it explicitly does NOT overwrite or reconcile existing-doc content, so it does nothing about the actual content drift (stale CLAUDE.md enumerations, etc.). Running /setup would clear the "out of date" *signal* (by writing `.si-version`) without raising the docs to standard — which is exactly the contradiction the user hit ("none of this makes sense"). This is already half-understood in the queue: [scaffolding-resync] records that content-level drift is NOT a job for a /setup re-run (it'd overwrite user content), and [make-drift-visible] is the queued redesign that detects drift by missing files and surfaces a user-readable catch-up offer. For /plan: the catch-up story those two batches describe needs to define what "catch up" actually remediates and what its user-facing message promises, so a future session doesn't again tell the user /setup is a cure-all. Possible follow-on: a self-hosting branch in /setup (relates to parked [self-hosting-support-during-setup]) so the dev project isn't run through consumer framing.

Full verbatim exchange — including Claude's internal reasoning at each step and the rest of the session (reconciliation, the "I don't know what to do" exchange, the `.si-version` fix) — is recorded in [resources/captures/2026-06-14-setup-on-dev-project-session.md](resources/captures/2026-06-14-setup-on-dev-project-session.md). Session outcome: `.si-version` written (1.12.0) to silence the false drift signal; `FAQ/` deliberately not created (deferred to /plan).

**First autonomous `/goal` session saved as a test outcome — decide: formally allow `/goal`, or stop shelving cruise control and build it**

Saved 2026-06-15. The first autonomous `/goal` session ran successfully: the user disabled the plugin, Claude implemented five top-of-queue build batches back-to-back in one chat ([delete-preflight-deferred-tests], [allow-parallel-sessions], [decouple-rezip-from-push], [make-drift-visible], [setup-q4-no-expansion]), and the user re-enabled the plugin and had Claude run `/done` by hand. The full transcript — every user and assistant message, Claude's reasoning, and every action — is recorded in [resources/captures/2026-06-14-goal-session-five-batches.md](resources/captures/2026-06-14-goal-session-five-batches.md). The user judged it successful and intends to repeat the shape several more times.

The session exposed that the method has no explicit "goal session" shape. It assumes one batch per session — one `_build.md`, one slug-named LOG entry, one commit — so the multi-batch run had to improvise an aggregate `_build.md`, a multi-thread LOG entry, and a single commit covering all five batches. The improvised close was clean, but it is improvisation, and it now recurs.

The decision /plan must make is a fork, not a tweak. Either **pivot to formally allowing `/goal`** — define how a goal session represents multiple batches (or skips `_build.md`), how its LOG entry and index line are shaped, and how the deferred-test and staleness sweeps run across several batches at once — **or** treat `/goal` as the working proof of the long-shelved "cruise control" (autopilot / unattended-execution) idea and stop deferring that idea, actually starting to implement toward it. The user's point: `/goal` is cruise control working in practice, and the method keeps putting the formal version off. Pick a direction rather than letting both sit.

**/done's commit message STILL isn't derived from the LOG entry — repeatedly asked for, fix designed but never shipped**

Raised again 2026-06-15, with real frustration: across multiple sessions the user has asked that /done's commit message come straight from the LOG record — the entry's summary line as the commit title, the entry's body as the commit body — instead of /done authoring a separate message. It keeps not happening.

The design is not the problem. The fix is already fully specified as the queued batch **[closeout-text-collapse]**, which makes both the commit title and body derive from the one approved LOG text (one approval, nothing new to read at commit time). The problem is that batch is **unbuilt and sits far down the Batches list**, and it is host-side (needs build + push + reinstall), so until it ships every /done re-authors the commit by hand and the user re-lives the broken behaviour. So this is not the user mis-instructing; it is a known fix that has never been prioritized to land.

Asks for /plan (or for a goal session): (1) **move [closeout-text-collapse] to the top of the Batches list** so the next build ships it — it is small and high-pain; until then, (2) manual /done closes derive the commit from the LOG entry by hand (done this session). Compounding cause the user named, and it is real: Claude's over-long discussion at every turn makes it hard for her to catch when /done drifts off-process, so the error slips past unnoticed. This is the documented model-compliance problem in resources/research/model-instruction-compliance.md — brevity instructions in CLAUDE.md and the plugin lose to the system prompt's helpfulness/thoroughness, so adding more or louder instructions does not fix it. The verbosity fix needs a mechanism at a higher priority than instructions, not stronger instructions.

**Self-hosting notes inventory — findings from [self-hosting-notes-audit]**

Audit run 2026-06-15 (goal session). The complete inventory of every self-hosting rule, convention, and judgment in the project, with where each lives, a candidate home, and whether its rationale is written. This is the committed inventory the [self-hosting-notes-audit] design called for: the next /plan authors the follow-on relocation batches from these findings (relocation, never copying — the new home lands and the CLAUDE.md source comes out in the same batch). Candidate homes are candidates only; the decision is /plan's. Homes: (a) shipped-generalized, (b) this project's CLAUDE.md, (c) the parked [self-hosting-support-during-setup] /setup-scaffolding scope.

1. **Note:** The plugin exists as "host" (installed, governs the live session) and "target" (editable source at `plugin/si-plugin/`). Target edits do nothing until packaged and reinstalled. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (c) — host/target is the defining self-hosting concept any plugin-building consumer needs. **Rationale written:** yes.

2. **Note:** Ambiguous references to "the plugin / the hooks / the procedures" must specify host or target; default is target. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (b) — local disambiguation convention for the developer's chat. **Rationale written:** yes (also MEMORY.md).

3. **Note:** Most target changes become host changes on reinstall, but changes outside the plugin package (project doc structure, this CLAUDE.md) don't propagate and need manual updates. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (b) — concerns this repo's own non-propagating files. **Rationale written:** yes.

4. **Note:** Batch ordering assumes the next batch sees the previous batch's effects — true for target-side edits (readable at author time), false for host-side changes (hooks, loaded skill docs, plugin-behaviour.md) that only refresh after push + reinstall. **Lives:** CLAUDE.md "Self-hosting dependency ordering". **Candidate home:** (c) — [self-hosting-support-during-setup] lists this discipline. **Rationale written:** yes (worked example).

5. **Note:** When a batch depends on a previous batch's host-side effects, /plan must place it after a push marker and annotate its `Depends on:` line as `(host-side)`. **Lives:** CLAUDE.md "Self-hosting dependency ordering". **Candidate home:** (a) — /plan authoring behaviour; shipped plan.md has never heard of push markers. **Rationale written:** yes.

6. **Note:** The line `--- Push required before continuing ---` halts /next until the user has pushed and reinstalled. **Lives:** split — convention/authoring side in CLAUDE.md "Push-marker convention"; the halt ships in next.md pre-flight. **Candidate home:** (a) — the /next halt already ships; the authoring half should join it. This split-across-homes is the audit's named trigger case. **Rationale written:** yes.

7. **Note:** The push marker is hard in only one direction — it halts /next because batches past it read host-side state; it does NOT suspend decided rules/reasoning, and is not a wall for planning work. It marks a ship-by aim. **Lives:** queued batch [push-marker-hard-direction], not yet written into CLAUDE.md. **Candidate home:** (b) — the batch routes it to this project's CLAUDE.md. **Rationale written:** yes.

8. **Note:** Rezip and Push are distinct. Rezip builds a fresh zip for private dogfooding (no bump, commit, or remote). Push is the full release ritual that publishes. **Lives:** CLAUDE.md "Rezip and Push". **Candidate home:** (c) — [self-hosting-support-during-setup] lists "push-and-rezip steps". **Rationale written:** yes.

9. **Note:** Rezip procedure: delete `__pycache__` under `plugin/si-plugin/`, repackage overwriting the zip (zip the folder so internal paths start with `si-plugin/`), verify no `__pycache__` entries, tell Alex nothing was published. **Lives:** CLAUDE.md "Rezip" steps. **Candidate home:** (b) — exact commands/paths are this-machine specific; the concept (clean bytecode before zipping) is the scaffolding-level note. **Rationale written:** yes.

10. **Note:** Push ritual: backfill LOG hashes, bump version (patch vs minor), run the two-pass pre-push sweep, archive the old zip, prune to three, clean `__pycache__`, repackage+verify, stage paths+zip+archive+plugin.json+LOG, commit "Bump to v… and repackage", push, tell Alex to reinstall. **Lives:** CLAUDE.md "Push" steps 1–10. **Candidate home:** (b) — full ritual with literal commands is local; the high-level shape is the scaffolding abstraction. **Rationale written:** yes.

11. **Note:** Version bumping lives on push, never rezip — bumping on every test build would make Alex's own projects nag "re-run /setup". **Lives:** CLAUDE.md Push step 2. **Candidate home:** (c) — [self-hosting-support-during-setup] lists "version bumping". **Rationale written:** yes.

12. **Note:** Pre-push consistency sweep — two passes: gather unpushed commits and their LOG entries, then check target internal consistency (templates vs docs), project docs, and CLAUDE.md for staleness. **Lives:** CLAUDE.md Push step 3. **Candidate home:** (c) — [self-hosting-support-during-setup] lists "pre-push consistency sweep". **Rationale written:** yes.

13. **Note:** Zip-archive mechanics — archive the previous zip as `si-plugin-v<OLD>.zip`, prune to three; git history is the authoritative record, so a test-build overwrite in the archive is cosmetic. **Lives:** CLAUDE.md Push steps 4–5 + "Archive accuracy". **Candidate home:** (b) — specific to this repo's packaging layout. **Rationale written:** yes.

14. **Note:** Clean `__pycache__` before any zip so Python bytecode never ships. **Lives:** CLAUDE.md Rezip step 1 + Push step 6. **Candidate home:** (b) — tied to this plugin shipping Python hooks; literal command is local. **Rationale written:** yes.

15. **Note:** At session start with no `_build.md`, run `git status --porcelain plugin/si-plugin/`; if dirty, warn and list paths (possible orphaned sweep edits). **Lives:** CLAUDE.md "Session-start dirty-tree check". **Candidate home:** (a) — queued [session-start-dirty-tree-check] moves this into session_start.py for every consumer and removes the manual section. **Rationale written:** yes.

16. **Note:** A "goal session" runs with the plugin off so Claude works autonomously through several build batches in one chat, closed by manual /done. **Lives:** CLAUDE.md "Goal sessions (plugin off)". **Candidate home:** (b) — the developer's own autonomous-dev workflow; its formalization is an open fork (/goal vs cruise control). **Rationale written:** yes.

17. **Note:** In a goal session the session-start hook never fires, so its LOG-hash backfill doesn't run; manual /done must backfill by hand (oldest-`git log -S` rule), folding the edit into the commit. **Lives:** CLAUDE.md "Goal sessions (plugin off)". **Candidate home:** (b) — interim handling tied to the not-yet-supported /goal mode. **Rationale written:** yes (labelled interim; thin — no permanent home yet).

18. **Note:** The session's own behaviour is the thing under test — all use of the plugin to develop the plugin is testing it; any observed Claude behaviour routes to Captures, not memory. **Lives:** CLAUDE.md "Rules for Claude". **Candidate home:** (b) — defining self-hosting judgment, specific to the developer dogfooding. **Rationale written:** yes.

19. **Note:** Host-side deferred tests (confirmable only after push + reinstall) are the dominant deferred-test flavor in self-hosting; nearly every change here defers, making the section look far larger than a consumer's would. **Lives:** QUEUE.md Deferred tests + [deferred-test-lifecycle] + "Deferred tests vs test batches" capture. **Candidate home:** (a) for the lifecycle / (b) for the "self-hosting inflates the count" observation. **Rationale written:** yes.

20. **Note:** The /done close-out backstop ("did this session's own activity confirm a pending deferred line?") pays mainly in self-hosting but stays universal because no mechanical self-hosting flag exists to condition on. **Lives:** QUEUE.md [deferred-test-lifecycle]. **Candidate home:** (a) — ships into done.md universally, self-hosting reasoning travels as rationale. **Rationale written:** yes.

21. **Note:** `.si-version` records which plugin version set a project up; the hook compares it to the installed version only for the "an update just happened" signal — drift warnings are presence-based, not version-based (version bumps every release, would cry wolf). **Lives:** session_start.py + setup.md; [scaffolding-resync] / dev-project capture. **Candidate home:** (a) — shipped behaviour; the self-hosting friction (missing `.si-version`/`FAQ/`) is a (b) local capture. **Rationale written:** yes.

22. **Note:** The dev project drifts because nothing re-scaffolds it when the plugin gains new scaffolding — `.si-version` and `FAQ/` were missing because /setup was never re-run here. **Lives:** QUEUE.md [faq-backfill] + dev-project capture. **Candidate home:** (b) — self-hosting maintenance gap specific to this repo. **Rationale written:** yes.

23. **Note:** /setup is consumer-framed and fits awkwardly on the dev project — the host/target oddity isn't acknowledged, and migration scaffolding would create fresh drift. **Lives:** QUEUE.md "/setup on the dev project" capture. **Candidate home:** (c) — the capture proposes a self-hosting branch in /setup. **Rationale written:** yes.

24. **Note:** Telling the user "run /setup to bring everything up to standard" is an overpromise — migration only backfills missing files and stamps `.si-version`; it does nothing about content drift. **Lives:** QUEUE.md "/setup on the dev project" Outcome 2. **Candidate home:** (a) — bears on what the [make-drift-visible] / [scaffolding-resync] catch-up message promises any consumer. **Rationale written:** yes.

25. **Note:** [self-hosting-support-during-setup] — if a user builds a plugin with the plugin, /setup should scaffold the self-hosting workflow into their CLAUDE.md (push-and-rezip, host/target, pre-push sweep, version bumping, dependency-management discipline). **Lives:** QUEUE.md Parked. **Candidate home:** (c) — this *is* that scope; the destination for most consumer-facing notes here. **Rationale written:** yes.

26. **Note:** The first /goal session exposed that the method has no explicit goal-session shape — it assumes one batch per session, so a multi-batch run improvised an aggregate `_build.md`, multi-thread LOG entry, and single commit. **Lives:** QUEUE.md "First autonomous /goal" capture + LOG 018152a. **Candidate home:** (b) — developer's autonomous-mode workflow, not yet shipped. **Rationale written:** yes.

27. **Note:** Pushing planning state in self-hosting is costly — a push off a no-plugin-change commit triggers the full push-and-rezip ritual, so /done's push offer should default to commit-only for planning closes. **Lives:** QUEUE.md [push-offer-fit]. **Candidate home:** (a) — ships the commit-only default into done-plan.md; self-hosting is the sharpest motivating case. **Rationale written:** yes.

28. **Note:** Cross-doc references in `plugin/si-plugin/` docs name their target ("the blocker gate in next.md's pre-flight"), never a step number, because step numbers silently retarget on renumbering. **Lives:** CLAUDE.md "Working conventions" + LOG 9f1b80b. **Candidate home:** (b) — host-only authoring rule for editing the plugin's own source. **Rationale written:** yes.

29. **Note:** post_tool_use.py's `ALLOWED_SUBHEADINGS` must grow when new batch types ship — a maintenance coupling between the lint hook and the queue format the plugin defines for itself. **Lives:** post_tool_use.py docstring + denial text; echoed in [spec-edit-batch-type], [ship-freeform-next-type]. **Candidate home:** (b) — code-maintenance note for whoever edits this hook. **Rationale written:** yes (only as code comment — thin; not a stated convention).

30. **Note:** git-safety denials match command text, not intent, so a denial can fire on a command that carries the pattern only as data; the note tells Claude to assemble such strings at runtime. **Lives:** pre_tool_use.py `PATTERN_AS_DATA_NOTE` + LOG 61bfd2f. **Candidate home:** (a) — shipped in the hook; the surfacing case (writing the pattern as a test string) is a plugin-dev scenario. **Rationale written:** yes.

31. **Note:** This project's "Where things live" tree and Architecture enumerations describe the self-hosting repo layout (plugin/, zip-archive/, target source) that no consumer has. **Lives:** CLAUDE.md "Where things live" + "Architecture". **Candidate home:** (b) — describes this repo's dev layout. **Rationale written:** n/a (descriptive). Note: stale counts already captured separately ("2 hooks" vs three, "Target v1.11.0" vs 1.12.0).

32. **Note:** Taskflowapp is the E2E test consumer; Alex runs E2E in a separate session and observations come back as queue items — the self-hosting project uses a real external consumer to test what it can't test on itself. **Lives:** CLAUDE.md "E2E testing". **Candidate home:** (b) — names a specific external project and cross-session workflow. **Rationale written:** yes.

33. **Note:** Reading QUEUE.md as audit target means decided-but-unshipped notes enter the inventory without waiting to land — the queue itself is treated as authoritative target state. **Lives:** QUEUE.md [self-hosting-notes-audit] rationale. **Candidate home:** (b) — meta-judgment about this audit/distribution arc. **Rationale written:** yes.

34. **Note:** Distribution discipline — each relocated note lands in its new home AND its CLAUDE.md source comes out in the same batch (relocation, never copying), so no danglers survive; the arc ends with a CLAUDE.md sweep for stragglers. **Lives:** QUEUE.md [self-hosting-notes-audit] rationale. **Candidate home:** (b) — process discipline for this arc. **Rationale written:** yes.

Coverage note: the shipped procedure docs and templates carry essentially no self-hosting content — the single exception is next.md's push-marker halt (finding 6). That absence is the audit's thesis: self-hosting knowledge lives in CLAUDE.md and session judgment, not in the method. Two rationales are thin: finding 29 (lives only as a code comment) and finding 17 (labelled interim, no permanent home). Factual confirmation, not new findings: CLAUDE.md still reads "Target v1.11.0" and "2 hooks" while plugin.json/`.si-version` are 1.12.0 and three hook files exist — both already captured.

**Goal session removed 13 of 14 batches it recorded removing — [user-edits-rollup-on-commit] survived in the queue**

Observed 2026-06-15 (goal session). The previous goal session (215f96e, LOG goal-2026-06-15.md) built [user-edits-rollup-on-commit] and its LOG entry said it removed 14 build batches plus 1 audit from QUEUE.md. But [user-edits-rollup-on-commit] was still at the top of the Batches list this session. done.md already carried its implementation — the dirty-path rollup sub-step in the commit core — so the batch was genuinely built; only its queue removal was missed. The other 13 batches were removed correctly. So this is a single-batch slip, not a systemic failure. This session removed the stale batch as queue hygiene and built on from there. Why it matters: a goal session closes by hand, and removing every shipped batch is a manual loop with no mechanical check that each shipped slug actually left the queue. A built-but-not-removed batch re-presents at the next session as if unbuilt, so the session's first move is wasted rediscovering that it is already done. Possible fix for /plan to weigh: at goal-session /done, cross-check the shipped-batch list in the LOG entry against QUEUE.md and confirm each slug is gone before committing. Relates to the open /goal-vs-cruise-control fork (the "First autonomous /goal session" capture above).

**Test-build version labelling so rezips reinstall cleanly** **[rezip-test-version-scheme]**

Raised 2026-06-15. A rezip rebuilds the zip but deliberately doesn't bump the version (CLAUDE.md: bumping on every test build would nag the user's own projects to re-run /setup). So a rezipped build carries the same version string as the build it replaces. Observed this session: after a full uninstall and reinstall of a same-version rezip, the new host didn't take — the desktop app appears not to register a reinstall when the version string is unchanged, even after a clean uninstall. That breaks the whole point of rezip, which is private dogfooding of an unpushed build.

Proposed scheme (applied this session as a first trial): test builds carry a `<base>-testN` version — the release-line base version, plus `-test` and a number that increments each rezip-for-testing. This build was set to `1.12.0-test1`. The next test rezip would be `1.12.0-test2`, and so on. A real push resets to a clean number with no suffix (the push "bump version" step sets a clean patch/minor and the `-testN` is dropped); test numbering restarts under the new base after a push.

Why this shape: a distinct version string per test build is what forces the app to treat each upload as a genuinely new install; the `-test` label makes it unmistakable the build is a private test, not a release; keeping the base version shows which release line the test is based on. Note the interaction with the session-start hook: a test version differs from the project's `.si-version` (1.12.0), so the hook's "an update just happened" signal will fire — that's tolerable, even a useful confirmation the new build loaded, and the drift warning stays quiet because [make-drift-visible] made drift detection presence-based, not version-based.

For /plan to decide and formalize: whether `-testN` is the right format (vs a build-metadata `+` suffix, which semver treats as equal-precedence and so would not help here; or bumping a throwaway patch); where the scheme is documented (CLAUDE.md Rezip section); and whether the rezip procedure should auto-increment the suffix. Open question to confirm by testing: does `1.12.0-test1` actually make the reinstall take where bare `1.12.0` did not — this trial is the test. Caveat carried: the test suffix lives in the working tree's plugin.json only and must be reset to a clean version before any push.

Confirmed 2026-06-15: the `1.12.0-test1` build installed and its skills registered correctly once the app was fully restarted — so the `-testN` pre-release format loads fine and is not a blocker. The reinstall failure that prompted this was not the version string at all; it was the app-restart requirement, captured separately in [reinstall-needs-full-restart]. The remaining open question for /plan is therefore just formatting and where to document the scheme, not whether it works.

**Reinstalling the plugin needs a full app restart, not just a new session** **[reinstall-needs-full-restart]**

Observed 2026-06-15 while testing a rezipped build. After a clean uninstall and reinstall of the local zip, the plugin appeared in the Customise → Plugins list, but its slash commands (/setup, /plan, /next, /done) did not appear when typing "/" in a new chat. A new chat alone did not fix it, and a normal close of the app did not fix it. What fixed it: fully quitting the desktop app — the user had to end it via Task Manager because a normal quit left the process running — then relaunching. After the full restart the commands registered. So plugin skills register at app launch, and on Windows the desktop app can keep running after a window close, which means "open a new session" is not sufficient — the app process must actually be killed and restarted.

Two doc implications for /plan:
- Consumer-facing INSTALL.md: the smoke-test diagnostic ladder currently says "start a fresh session, since skills register at session start." That under-specifies the fix — a fresh chat was not enough here. It should say to fully quit and relaunch the app, and on Windows to confirm the process has actually exited (via Task Manager if a normal quit leaves it running). This corrects a line written in this same goal session.
- This project's CLAUDE.md Rezip step ("Uninstall/reinstall to test the new host privately") should add that a full app restart is needed for the new host's skills to load.

Relates to [rezip-test-version-scheme] — the same test session confirmed both that the `-testN` version loads and that the restart, not the version, was the blocker.

### Parked

- **[narration-vs-menu-drift]** Observed during 1b7d359 /plan: Claude defaulted to menu-style options ("file as capture, drop it, or commit to the rule now?") when narrating a recommendation would have been more appropriate. Dependency ownership's narration rule ("narrate the ordering work" — exercise judgment, recommend) is supposed to catch this. The mechanism failed under exploratory back-and-forth tone — the pull toward "lay out the options" was stronger than the pull toward "state the recommendation, let user push back." Worth watching whether this generalizes: when the conversation gets exploratory, does Claude soften from recommendation-narration into menu-listing? If so, the narration rule needs tightening — possibly explicit text that menu-style enumeration of equally-weighted options is *not* narration when Claude actually has a preference, and the recommendation must come first with the menu as fallback.
  Blocked by: a second observed instance of menu-style enumeration where a recommendation was due — behavioural trigger, no slug; fires at the /plan that processes such a capture.

- **[parked]** Decide whether to add an inline marker for internal-only terms in procedure prose. The marker would let procedure docs flag internal terms inline so the translate-or-omit rule fires mechanically rather than relying on Claude matching against the vocabulary list each time.
  Blocked by: [narration-vocabulary] + observed leakage after it ships

- **[user-execution-batch-shape]** When the user is the executor of a batch (gather these receipts, identify the lender, call the ATO) rather than Claude, the existing build/test/audit shapes don't quite fit. Build batches assume Claude executes; test batches are about verification; audit batches are read-and-route. A user-execution batch sits closest to a test batch in mechanics (user runs steps, Claude facilitates), but it's not verification — it's the primary work. Observed during /setup on a tax-prep folder: queueing batches that were mostly user-action items felt weird, even though step-by-step communication rules in plugin-behaviour.md would handle the running well. Three possible landings: (a) new `User:` subheading alongside Build/Test/Audit, (b) covered by existing types + freeform once shipped, (c) framing-only — "build" means "user does it" in non-coder projects, no new structure. Decision premature without running several user-execution batches first.
  Blocked by: experience from 2–3 user-execution batches run in the tax project — external behavioural trigger, no slug; fires when that experience reaches a /plan session here.

- Add scenarios to reader-test-workflow.js — evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Promote as one or more build batches once scenarios are picked. The refresh itself shipped at 2356cb7 ([reader-test-refresh]), so only the run remains.
  Blocked by: refreshed workflow run once — behavioural trigger; the first refreshed run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity.

- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed; (4) the red-flags gate — an open red flag in the active scope blocks the unattended run, only resolved or accepted flags let it proceed, and a user who leaves a flag open stays on hand to approve each step (the gate is a hook reading the three flag states defined by [red-flags-screen-rule]).
  Blocked by: the autopilot prerequisite arc shipping — the no-planning-in-execution rule ([no-planning-in-execution]), queue-visible plan markers ([queue-plan-markers]), and audit bulk approval ([audit-findings-bulk-approval]); fires when those have shipped and an unattended next→done→next run is plausible. Full no-approval auto-file of audit findings is in this item's own design scope — interactive audits keep bulk approval. Named as the end-goal in the thinking-work capture, 2026-06-10.

- **[self-hosting-support-during-setup]** Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping, **and the dependency-management discipline** (host-vs-target distinction as it governs batch ordering, the host-side-after-push-marker rule, the `--- Push required before continuing ---` queue convention, and the `(host-side)` annotation on `Depends on:`). All of this carries into the new project's CLAUDE.md. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
  Blocked by: a second self-hosting consumer appearing — a user reports building a plugin (or any project that ships itself) with the plugin, or Alex starts one; external behavioural trigger, no slug. The scoping decision (interview question vs skill vs template) waits for that real case to design against.

- **[done-spec-sync-check]** /done spec check at build close — when the session being closed was a /next build (not test or audit), /done reads SPEC.md against the just-landed changes and applies the spec-entry trigger test (post-[spec-entry-trigger-rethink] form: would these changes make SPEC.md's description wrong or incomplete?). If yes, /done files a mandatory capture naming the gap — it never edits SPEC.md directly; product-truth edits stay in /plan. Decided 2026-06-10: detect-and-file wins over sync-in-/done, keeping SPEC authorship in /plan while making the backstop mechanical. Evidence the backstop is needed: the prospective /plan gate leaked at [tag-definitions-compliance-rewrite] — no spec entry preceded the build, and the gap was caught only because the /done session noticed by judgment and filed a capture. This makes that lucky catch structural: prospective gate at /plan, mechanical detect-and-file at /done.
  Blocked by: [spec-entry-trigger-rethink] — the /done check applies the rewritten trigger wording, so it can't be authored until that wording has shipped.

- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md.
  Blocked by: Anthropic adding token data to hook event input — external trigger, no slug.

- **[lint-citation-refire]** Observed at [queue-format-lint-hook] build testing, 2026-06-12: the prose-citation check re-fires on every QUEUE.md edit for references it has already flagged. The check is stateless — it reads the whole file, not the edit — so a reference the user has judged "citation, fine" gets flagged again on every later edit, indefinitely. The build already cut the worst noise by flagging only references to slugs still defined in the file: a dry run showed references to shipped work were the bulk (~2.5KB of advisory text per edit), and a reference to shipped work can only be a citation. The residue is real: the first live run flagged ~21 batches, all naming pending items, and any judged-as-citation among them will keep re-firing. Candidate fixes if live use shows this as noise: an inline convention marking a reference as a deliberate citation, which the lint would skip (new format design, /plan's call); or accepting the re-fire as cheap advisory background. The hook is not yet in the installed host — it was built after the v1.11.0 push — so no live session has run with it yet.
  Blocked by: live experience with the lint hook — behavioural trigger; fires once a few /plan sessions have edited QUEUE.md with the hook installed and the re-fire can be judged noisy or tolerable.

- **[behaviour-doc-size-watch]** Filed at the 2026-06-13 /plan, from a doc-size review. plugin-behaviour.md is the largest doc by content (~3,074 words / 135 lines at counting time) and the most expensive position in the system: it is injected at every session start, and skill sessions pay it twice until [behaviour-doc-double-load] ships. Many queued batches add rules to it — the approval rules, authoring standards, scope anchor, memory boundaries, no-planning-in-execution — so it will grow before it settles. Decided at the review: no blanket terseness pass. The rationale-everywhere style is the compliance bet; stripping why-clauses to save tokens buys back the failure mode they were installed to fix. Duplication-targeted trims are already queued ([tag-restatement-trim], [trickle-up-next-md-duplicates], [trickle-up-ask-when-unsure], [behaviour-doc-double-load]). The remaining lever is the progressive-disclosure restructure — compact core injected, full doc loaded at skill time — already noted as a revisit in [behaviour-doc-double-load]'s rationale. This capture is the re-measure trigger: when it fires, re-count plugin-behaviour.md, compare against ~3,074 words, and weigh the restructure on real numbers instead of trimming mid-flux.
  Blocked by: the compliance arc's plugin-behaviour.md additions landing — behavioural trigger, no single slug; fires at the /plan after the queued rule-adding batches have shipped and the doc's contents have settled.

- **[full-tag-placement-recheck]** A fresh full placement re-check of response-shape tags across all procedure docs — setup.md, plan.md, the next and done families, plugin-behaviour.md — to grade the corrected state after [output-tag-audit]'s fixes ship, and to catch any tag drift since that audit (commit 0405315). Distinct from [opening-narration-audit], which measures narration volume at openings; this one re-checks per-step tag placement everywhere, the same lens [output-tag-audit] used, re-run on the post-fix docs. Deferred deliberately: running it before [output-tag-audit]'s findings build would mostly re-discover gaps already sitting in the queue.
  Blocked by: the queued tag-fix batches from the last full tag audit shipping — chiefly [next-done-tag-sweep], [plan-step1-sequencing], and [setup-self-contained-no-tags]; fires once those findings have landed, so the re-check grades corrected docs, not the pre-fix state.
