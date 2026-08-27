# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Discord posting bot: an all-rounder so posts and rezip-list updates can be made straight from a session [discord-posting-bot]
Raised by you 2026-08-26, in the post-close tail, as a side-thought filed for a later /plan. The want: the test-rezips channel's posts and their updates — adding notes to previous entries when issues are reported, changing an entry's stable status — done by a bot rather than by hand, and more generally an all-rounder bot this project can post through directly during /plan or a build. That would be the first route Claude has to Discord, so the never-send-unseen guarantee has to be designed in from the start: nothing posts without you seeing the exact text and saying yes, and an automated update is still a send. Bears on the nerds-list mechanics left open on [expedite-first-beta-release] and on the eventual [weekly-release-cycle] turn.

**Kept 2026-08-26 at the next planning session, on Claude's recommendation and your agreement — "ok I'm willing to try it."** It designs out smaller than "bot" sounds: no hosted service — a bot account (the Discord-side setup split out as the `[user]` line [discord-bot-server-setup], which holds this build) plus a script making one API call per send or edit. The token risk and its informed consent are recorded on that item's red flag. Every send stays behind the exact-text-yes rule; a register line is still written per post; the route is all that changes, which falsifies CLAUDE.md's "Claude has no route to Discord" sentences — amended in this build, with the never-send-unseen rule restated where they stood.

Rule gate: run — amendment to CLAUDE.md's Discord section (the no-route sentences replaced by the route-plus-approval statement); no new freestanding rule, the send-approval rule unchanged and cited.

--- Build block ---
Changes: `resources/discord_post.py` — standard library only, UTF-8 reconfigure per the scripting constraints: send a message to a named channel, edit a previous message by id, token read from `INBOX/discord-bot-token.txt`, exact text passed in from a file; verified against Discord's current API docs before writing. `CLAUDE.md` — Discord posts section: the "Claude has no route to Discord" sentences amended to name the bot route, with the exact-text-yes approval and the sent-register line restated as unchanged; walkthrough steps in queue items keep "you post" wording only where a post genuinely stays manual. The amended text describes reading and posting separately (folded from the deleted [no-route-is-false] capture, 2026-08-27): the bot reads the channels it has been granted, while posting is gated by the approval rule stated as its own safeguard — the old sentence was doing double duty as fact and safeguard, and only the fact changed.
Inputs: `INBOX/.discord-bot-token.txt` (created by [discord-bot-server-setup]; renamed to the dot-name 2026-08-27 so the mail scan never surfaces it — see TOOLS.md), the channel ids the user names there. Entry format: every test-rezips entry the script posts carries a "Commit: <hash>" line, per [test-rezips-entries-name-obtain-route].
Draft-edit flow, settled 2026-08-27 at the prune item's processing and tested live: a draft is written to a `.txt` file and opened in Notepad for the user (the side panel opens `.md` read-only and `.txt` not at all — both tested); the user edits, saves and says done; the script posts the file's exact content after their explicit yes. The user's reason for the flow, rendered in Claude's words: editing the file directly beats negotiating wording change-by-change in chat. Post-post corrections are the bot editing its own message, since nobody can edit anyone else's Discord message.
The prune bounds ride [bot-prunes-test-rezips], placed after this item.
Acceptance: a test post to the test-rezips channel, its exact text approved by you first, appears in the channel and is then edited by the script; the token is never printed, quoted or committed; CLAUDE.md nowhere still claims Claude has no route to Discord.
Refused: a hosted always-on bot — nothing here needs to listen, only to send; per-post manual copying stays available whenever you prefer it.
--- End build block ---
**Lifted 2026-08-27 at the planning opening.** [discord-bot-server-setup] completed in the 2026-08-27 build run (`LOG/2026-08-27-discord-bot-server-setup.md`): the token file exists and the bot is in the server, which is the closing condition that item names. Facts the build needs are recorded in `TOOLS.md` (written 2026-08-27) — including that "main" still returns 403 while tips, announcements and test-rezips-for-nerds are reachable, and that channel IDs are looked up through the bot rather than kept on file.

#### Posting bot prunes old test-rezips entries after each new post [bot-prunes-test-rezips]
Your decision, 2026-08-27, given while the channel pin was being edited: pruning old entries is no longer a by-hand job — the same script that posts a new build entry prunes the old ones in the same run. Scoped as an addition to [discord-posting-bot], referenced by slug from both sides. The pin was reworded to name no mechanism, so it cannot be falsified by this shipping.

**Processed 2026-08-27, cleared to run, on Claude's design and your agreement.** The prune's bounds, settled at the decision step:
- keep the newest **15** entries — your figure, given at processing;
- delete only messages **the bot itself authored**, checked per message against the author field — your posts, other members' posts and the pin are untouchable by construction, not by ordering luck;
- exclude pinned messages explicitly as a second, independent guard on the pin;
- on any error partway, stop and report, with no retries — leftover old entries are simply picked up by the next post's prune, so nothing needs recovering.
The author-scoped bound costs your workflow nothing because nobody can edit anyone else's Discord message anyway — a pre-post edit happens in the draft file (the Notepad flow recorded on [discord-posting-bot]), and a post-post correction is the bot editing its own message. The one cost: entries posted by hand before the bot existed can never be pruned or edited by the bot; they are cleaned up by hand once.
Refused: pruning by position or count alone with no author check — that is what could reach the pin or a member's post.
Interaction noted on [sent-register-pointer-resolves-to-nothing]: bot-posted entries are posted from a file on disk, so their text is on record before the prune can ever remove the channel copy.

Red flag · State: cleared — designed out by the bounds above; the residue, stated plainly, is that `Manage Messages` stays granted to the bot, which you already consented to on [discord-bot-server-setup] (2026-08-26).

--- Build block ---
Changes: `resources/discord_post.py` — the prune added to the posting script, run after each new entry posts, under the four bounds above.
Acceptance: after a test post, entries beyond the newest 15 that were bot-authored are gone; the pin and all non-bot messages remain; a forced mid-prune error stops the script with a plain report and deletes nothing further.
--- End build block ---

#### Adding the GitHub marketplace would collide with the local one — same name, and it may overwrite the rezip source [marketplace-name-collision-hazard]
Found on 2026-08-27 while checking whether a commit could be used as an install ref for a test build; deliberately not tested, because the test itself was the risk. The local `flintcraft` directory marketplace is what every rezip depends on, and this repository's committed `marketplace.json` declares the same name.

**Processed 2026-08-27, cleared to run, on Claude's recommendation and your agreement — and the open question is answered, not guessed.** Research at the decision step (`resources/research/marketplace-name-collision.md`): `marketplace add` **silently overwrites** an existing registration of the same name — no warning, no error; an open, tracked Claude Code bug (anthropics/claude-code#44042). So the feared case is the confirmed behaviour: the beta install command on this machine would silently repoint `flintcraft` to GitHub, and every later rezip would install the remote while reporting success.

Red flag · State: cleared — designed out by a standing rule this build writes, plus the fact only this project's own machines are exposed: testers have no local directory marketplace to collide with. Residue, stated plainly: the bug itself is outside our control, and the rule is a rule rather than a mechanical block.

Refused: a distinctly named beta marketplace — the beta branch fast-forwards from main and cannot carry a divergent `marketplace.json` name without giving up that design. Re-examine only if #44042 ships a fix.

--- Build block ---
Changes: `CLAUDE.md` — one sentence in the Rezip/Push/Release section: never run `claude plugin marketplace add` against the GitHub repository on a machine using the local `flintcraft` directory marketplace, because the CLI silently overwrites same-name registrations (anthropics/claude-code#44042; `resources/research/marketplace-name-collision.md`).
Acceptance: the sentence is present in CLAUDE.md's rezip section, names the bug number, and the research file it cites resolves.
--- End build block ---

Rule gate: run — amendment to CLAUDE.md's Rezip section (a guard clause on the existing rezip instructions, naming its derivation: a verified external bug); nothing evicted, no freestanding rule added.

#### Hand-over messages get one pre-send checkpoint carrying all three composition checks [handover-composition-checkpoint]
Merged 2026-08-27 at the decision step from three same-day captures — [capability-just-granted-not-considered], [walkthrough-jargon-broken-by-its-own-author] and [file-link-not-offered-at-hand-over] — on Claude's recommendation and your agreement. All three instances are from the 2026-08-27 build run, and together they are one finding, not three.

**The evidence the merge carries.** Three shipped, clearly written rules each failed to fire at the moment they applied, in one run: the tool-check — a Discord message's text was handed to the user to supply by hand, twenty minutes after the same session provisioned a bot with Read Message History for exactly that (your words: *"you're supposed to have read message history access through the bot"*); the jargon rule — broken within the hour by the session that authored it, a hand-over step naming four UI terms with no location and no read-back (your words: *"I don't understand what you want me to do"*); and the view-in-doc link rule — months shipped, correctly applied elsewhere in the same run, yet a file was named in prose with no link until you asked (*"please link to the file so it opens in sidebar"*). Not recency, not unclear wording: all three failures happened while composing a message handing something over, and none while editing a file. Hand-over composition had no checkpoint; file edits have several.

**A fourth instance, added at processing later the same day, sharpens the theory rather than widening the scope:** the shared-vocabulary rule (shipped the day before) was broken in this planning session itself — a capture was presented as a "standing note" and a "guard note", aliases minted for what the method simply calls a capture, and the user had to ask whether that was a real feature. Again while composing a message to the user, not while editing a file. The checklist's first question carries the alias arm for it.

**The design.** The jargon rule's pre-send read-back of hand-over steps already exists and is the right moment; it currently checks one thing. This build widens that read-back into the single hand-over checkpoint, carrying three questions in one pass:
1. does any step use a term naming nothing on the user's own screen or files — and is any method thing called by anything other than its own name — and does each step name the thing to click or type and the thing to look for;
2. is there a tool that could do this work instead of the user — including anything this session itself set up, read from `TOOLS.md` rather than from memory of what the project can do;
3. is every file the message points at given as a link, per the view-in-doc rendering rule.

The tool-check and view-in-doc rules stay canonical where they are and are cross-referenced, not restated — this is an amendment to the read-back, consuming no new slot and evicting nothing.

**The honest limit, which the wording must state:** this makes the checks more likely to fire by giving the moment one named checklist instead of three scattered rules; nothing verifies the read-back ran. A rule per instance was refused (the admission gate's own bar), and so was another freestanding remember-to rule — the second capture's own text records that shape as the one this project has found does not hold.

Rule gate: run — amendment to the hand-over read-back rule shipped by [general-jargon-translate-and-walkthrough-readback]; parent named, the other two rules cross-referenced rather than restated, nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` and `plugin/throughliner/docs/next.md` — the read-back rule at both its sites widened to the three-question checkpoint above, worded with the honest limit; grep for the current read-back wording first so both sites are found and no third copy is created.
Acceptance: a grep for the read-back rule finds the three questions at its existing sites and nowhere new; the tool-check and view-in-doc rules are cited by cross-reference, not duplicated.
--- End build block ---

#### Posting rule gains the tips kind, and the rituals gain the tip pipeline [posting-rule-two-kinds-and-tip-pipeline]
From your channel restructure of 2026-08-27, designed at the decision step from the deleted capture [discord-channel-purposes-split]: **some** of what has gone into *announcements* is from now on a **tip**, announcements narrows to **news only**, and old posts may be recycled into future ones. A tip explains one Throughliner feature — maybe newish, but with no release or big event behind it; news is releases and big happenings. The bot may post in tips, announcements and test-rezips-for-nerds.

**The pipeline, your design rendered in Claude's words:** tip candidates are noticed at the rezip (the moment a feature lands in the installed build) and pooled in `ANNOUNCEMENT-IDEAS.md`; the release is what makes a candidate postable, so the release ritual marks which pooled candidates its shipped features clear and leaves a note; the next /plan reads that note and files the cleared candidates as dated `[user]`/post items on the one-a-day rhythm — new or updated features first, historical tips on slow news days. Tip staleness is covered by the existing repeal-grep over `INBOX/sent.md` once the register records the channel per post.

**How-to posts ride the same check, added on your instruction in the same discussion:** the forum's how-to topics exist for welcoming and onboarding, their number must stay small (a new one is your call, never accumulated by drift), and each tip, rezip entry or announcement may bear on one — so the posting step checks the how-to topics' register lines for claims the new post touches, and a needed tweak is a bot edit of its own how-to post, under the approval rule like any send. Bot maintainability requires bot authorship — the migration is [howto-posts-bot-authorship].

Rule gate: run — amendment to CLAUDE.md's Discord posts section: the "and nothing else" clause reworded to carry the tips kind with its own test ("explains one Throughliner feature"); the did-Throughliner-change test stays for news; the exclusion of general Claude Code tips stands; nothing else evicted.

--- Build block ---
Changes: `CLAUDE.md` (Discord posts section) — the two kinds with their two tests, the channel recorded in each sent-register line, the how-to check on each outbound post, and the how-to set's welcoming-purpose bound stated without a number. `resources/release-ritual.md` — the rezip gains a tip-candidate check writing to `ANNOUNCEMENT-IDEAS.md`; the release gains a step marking which pooled candidates its shipped features clear, leaving a note for the next /plan.
Reads but does not change: `ANNOUNCEMENT-IDEAS.md` (the pool; its format is whatever it already uses), `INBOX/sent.md`.
Acceptance: CLAUDE.md names both kinds and their tests and the how-to check; the ritual doc carries both steps; the grep for "and nothing else" in its old absolute form returns nothing.
--- End build block ---

#### Register pointers verified to resolve at the turn they are written [register-pointer-verified-at-write]
From the deleted capture [sent-register-pointer-resolves-to-nothing], processed 2026-08-27. Two register lines claimed post text sat "verbatim" in a record holding no quoted text — one repair had even pointed back at the register in a circle — and the fault was findable only because a session happened to need the text. Both instances were repaired in-session through the bot (the pin, and the "living dangerously" post recovered from announcements); this build fixes the rule so the fault cannot be written silently again.

**The design:** the always-loaded write-verify-point rule (write, then re-read to confirm the content is there, then point) applied to one more site — the sent-register line. A register line claiming text is on file "verbatim in X" is written only after X actually holds the quoted text, confirmed by re-read in the same turn, which is the only moment the text is guaranteed on hand. Where the text is not yet stored, the line says so plainly instead of pointing.

Rule gate: run — amendment to the register-line specification in feedback-and-inbox.md (the "written in the same turn" paragraph gains the resolve check); parent named, the write-verify-point rule cited rather than restated, nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/feedback-and-inbox.md` — the sent-register section's same-turn paragraph gains the requirement that a verbatim pointer is confirmed to resolve to the quoted text by re-read before the line is written, with the no-text-stored arm stated ("say so plainly instead of pointing").
Acceptance: the section states the resolve check and the no-text arm; a grep for "nothing later reconstructs it" finds the amended paragraph carrying both.
--- End build block ---

#### Test-rezips entry posts at the close once one plan and one next have run on the build [rezip-posts-its-entry]
Captured by you on 2026-08-27 after the unposted 1.21.0-test2 rezip; **redesigned by you at processing the same day, superseding the capture's rezip-sited step** — your design, rendered in Claude's words: an entry describes a build that has been exercised, not a fresh one, so it posts at **/done**, and the readiness test is sessions, not time. There is no timing to this.

**The design.** At a close, check whether at least one full /plan session AND one full /next session have run on the installed build since its rezip — read from LOG records dated after the install date the session opening reports. Both run → the new entry is ready to draft (Notepad flow, exact-text yes, bot posts, register line with verified pointer). **The posting step also builds and attaches the zip** — your decision at processing, answering where a nerd's download comes from: the script zips `plugin/throughliner/` as it stands into the temp scratchpad and attaches it to the entry (~270KB, well under Discord's file limit), so every entry carries the exact build it describes and the channel's name is literally true. The zip is not kept locally — the release archive stays release-only pruned to three, Discord holds the download, and the entry's commit line lets any build be rebuilt byte-for-byte from git. **And on your instruction (2026-08-27), that folder is renamed `plugin/zip-archive/` → `plugin/release-zip-archive/` in this build**, so its name says what it holds; the build greps `zip-archive` across the project first and updates every live reference (release-ritual.md and CLAUDE.md at least — the grep is the authority), leaving LOG history and dated records untouched. The install-from-zip route (extract, add the folder as a local marketplace) is described once in the pin or how-to as part of this build, honestly framed as bleeding-edge work. **Posting the new entry unlocks the edit of the previous entry**: a short testing-outcomes summary from the LOG plus a **usability rating out of 5**, given by you at that moment. A fresh entry carries **no** rating — too new to rate is what "under testing" says. Entry format otherwise per the pin's promises: one of the three labels, a `Commit: <hash>` line, the version.

**First iteration, stated because it differs:** the entry currently in the channel is your own post, so its backfill (outcomes + your rating of 3/5, given 2026-08-27) is yours to paste once; every entry after is bot-authored and bot-editable.

**Placement is host-only by construction:** the check lives in CLAUDE.md's Discord section, never in the shipped close docs — consumers have neither the bot nor the channel. The posting and editing mechanics ride [discord-posting-bot]'s script; the prune runs in the same pass per [bot-prunes-test-rezips].

Rule gate: run — amendment to CLAUDE.md's Discord posts section (host-only by residence); supersedes the capture's own rezip-sited suggestion on your redesign; the approval rule cited unchanged.

--- Build block ---
Changes: `CLAUDE.md` (Discord posts section) — the close-time readiness check (one plan + one next on the installed build since its rezip, read from LOG against the install date) and the two-step entry lifecycle (fresh entry unrated; superseded entry gains outcomes summary + rating out of 5 from the user). `CLAUDE.md` (host/target section) — the "rezip builds no zip" sentence widened to the full truth so the word stops misleading (from the deleted [rezip-name-promises-a-zip] capture): a rezip refreshes the install from the folder and builds nothing; a posted entry attaches a zip of that exact build, built at posting. Renaming the word was refused: the channel name keeps it public, and docs saying "refresh" against a channel saying "rezips" would mislead more, not less. `resources/release-ritual.md` — one pointer sentence in the rezip section naming where the entry now posts, so the ritual doesn't read as missing the step.
Acceptance: CLAUDE.md states the check and both lifecycle steps with the approval rule cited; the ritual's rezip section points at it; no step claims an entry posts at rezip time.
--- End build block ---

Relationship written both ways: [discord-posting-bot] carries the script, [test-rezips-entries-name-obtain-route] carries the pin's promise, [bot-prunes-test-rezips] shares the posting pass.

#### Criterion never restated as a calendar claim [criterion-not-restated-as-time]
Raised by you 2026-08-27, mid-processing, after the second arbitrary time claim in one session — your words: *"There's no timing to this."* A readiness criterion of one plan and one next had been announced as "nothing goes up today", when the sessions could both run the same day. The first instance was the same shape earlier in the session.

**The rule:** when saying when something can happen, state the criterion and check the world against it; never convert a criterion into a calendar or time claim ("today", "tomorrow", "later") unless the criterion itself is a date.

Rule gate: run — amendment to the always-loaded date rule (the read-a-computed-field rule barring "today" by assumption); same subject one clause wider, parent named, no new slot, nothing evicted. Admission: two recorded failures in one session, both caught by the user.

--- Build block ---
Changes: `plugin/throughliner/docs/skill-nonspecific-rules.md` — the date rule's paragraph (Research and evidence filing, "Where the answer is a date, read a computed field") gains the clause: nor restate a non-date criterion as a time claim; a time word is justified only where the criterion is a date.
Acceptance: the paragraph carries both arms; grep for "never derive today's date by assumption" finds the amended paragraph and no second statement of the new clause anywhere.
--- End build block ---

#### setup.md Step 3 heading drops its stale two-settings promise [setup-step3-heading-stale]
From the 2026-08-27 build run's noticing, processed 2026-08-27: the heading reads "Step 3: Interview (adaptive discovery + two settings)" while the step's own body states there is no settings question anywhere — the last one was dropped in favour of ignoring `INBOX/` on both paths. A heading is what a session jumping into a step reads first, so the stale half steers the read before the correcting sentence is reached. Left out of the tagging build deliberately (a heading rewrite is not tagging).

Rule gate: not needed — a stale-heading correction; no rule is authored, amended or repealed.

--- Build block ---
Changes: `plugin/throughliner/docs/setup.md` — the Step 3 heading becomes "Step 3: Interview (adaptive discovery)"; grep the docs for the two-settings phrasing to confirm nothing else promises it (cross-doc references go by name, so none is expected).
Acceptance: the heading carries no settings mention; the grep returns nothing live.
--- End build block ---

#### Throughliner bot icon: white linework on the Chagora background, striations on the cord [bot-icon-house-style]
Captured by you 2026-08-27 with the reference files you named; processed the same day. **The SVG at the project root, `throughlinerprojectboticon.svg`, is confirmed by you as the intended line art** (the wrench-and-pencil figure), which turns the job from a redraw into a recolour-and-composite. **Your addition at processing: the spinal cord at the bottom gains a couple of striations — up-and-down lines running along the cord, not cross-lines (your correction)** — to make it more recognisable for what it is meant to be. Claude attempts the vector edit and shows you the render; if it doesn't convince, the drawing goes back to you.

The house style, read from `Casual Projects/Chagora/icon.png` and `chagoraiconw.svg`: flat white stroke-only line art, no fill or shading, on a circular badge — thin dark rim, dark diagonal gradient running deep red at the left to desaturated teal-blue at the right, darkening toward the centre.

Refused: converting the rendered mascot draft (`Throughliner-icon.png`) — a filter cannot turn a shaded illustration into line art; it stays a draft, superseded by the vector route. AFK-cats is out of scope; this item sets the pattern its `assets/` folder is staged for.

--- Build block ---
Changes: `throughlinerprojectboticon.svg` — strokes white, striations added to the cord, page fitted to the art; a new composited icon PNG at the project root (both files kept in the repo, matching how Chagora keeps its pair). Uses Inkscape's command line (installed on this machine — see TOOLS.md's Python note) for compositing and export.
Reads but does not change: `Casual Projects/Chagora/icon.png`, `chagoraiconw.svg` (style references), `Throughliner-icon.png` (superseded draft, left as is).
Acceptance: the PNG at the root shows white line art with visible cord striations on the Chagora-style gradient disc; the user approves the render; on that yes the bot sets its own avatar through the API (an outward-facing change, made only on the explicit yes), and the avatar visibly updates in the server.
--- End build block ---

#### Rescan recommended before the close, and the close's scan stands down when one just ran [rescan-before-done]
Captured by you 2026-08-27 at the session's rest, processed in the same exchange. Two halves, one build.

**One: recommend the rescan wherever the method names the close as the next step.** The end-of-queue gate's wording ("we can close the session and record it…") and its sibling at /next's close hand-off each gain one clause recommending the rescan command first, named in words. The suggestion arrives exactly when closing is on the table and nowhere else — never mid-work.

**Two: the close's wind-down scan does not re-run when a rescan literally just ran.** The window rule already limits the close's scan to what the last rescan didn't reach; this adds the final step: where nothing has happened since that rescan — no work, no decisions, only the close being invoked — the close performs no second pass, and its record carries one line, "covered by the rescan just run", so a stood-down scan stays distinguishable from one that never happened. Conversation between the rescan and the close still gets scanned under the existing window rule.

Rule gate: run — both halves are amendments to existing steps (the gate's wording; the wind-down's window rule), parents named, nothing evicted.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the end-of-queue gate's close wording gains the rescan-first clause; `done.md` — the wind-down scan gains the stood-down arm with its one-line record; `next.md` — the close hand-off wording gains the same clause where it names /done. Grep the docs for the close-naming sentences first so every site is found and no fourth copy is created.
Acceptance: both gate wordings carry the rescan recommendation; done.md states the stood-down arm and its required line; the grep finds no close-naming sentence without the clause.
--- End build block ---

#### rescan's numbered set gains the process-now arm — no capture written for an item taken now [rescan-processnow-no-double-write]
Found live 2026-08-27, raised by the user mid-planning: /rescan's candidate set was answered "process now" and captures were written first anyway, because rescan.md's Step 2 says unconditionally that "the writes then land" while plan.md's process-now rule says an item taken now is never written as a capture — it is written once, as a work item, after the interview. Two shipped docs disagreed and the session followed the wrong one; the user's words: *"Claude is not supposed to write until it has checked the user wants to process now or not."*

The planning rule is the load-bearing side: filing first spends a write that is thrown away, and process-now is the common answer by the user's own recorded estimate. The fix is one amendment to rescan.md's Step 2: items answered *file* land as captures exactly as now; an item answered *process now* is not written — it enters the planning loop and is written once as a work item, the plan.md rule cited rather than restated.

Rule gate: run — amendment to rescan.md Step 2; the conflicting unconditional sentence is reworded, which is the eviction; plan.md untouched; nothing else added.

--- Build block ---
Changes: `plugin/throughliner/docs/rescan.md` — Step 2's "the writes then land" sentence gains the two arms (file → capture written; process now → no capture, enters the planning loop, written once as a work item), with plan.md's process-now rule cited by name.
Acceptance: the Step 2 paragraph states both arms; a grep for the old unconditional "the writes then land" phrasing returns nothing.
--- End build block ---

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
**Lifted 2026-08-27 at the planning opening.** [cycles-due-check-verification] closed as passed (`LOG/2026-08-27-cycles-due-check-verification.md`), and the host is live at the current stamp, so the checks that will read the definition are installed.
**Files:** `CLAUDE.md`, the new cycles doc. The dependency is host-side: the checks that read the definition must ship first.

#### [user] Smoke-test the `#beta` install on your second machine, then edit the how-to post's install command [beta-install-smoke-and-post-edit]
Filed 2026-08-26 with [beta-branch-install-pin]. Two sequential user steps: the ref-pinned route is unverified against the open feature requests the research names, so it is proven on a real second machine before any tester is pointed at it; and the published "How to install" forum post claims the plain two-command route, which the pin falsifies — the correction is yours to make, per the repeal-falsifies-an-announcement rule.
**Walkthrough.**
1. On your second machine, open a fresh Claude Code chat and ask it to add the plugin marketplace `FlintcraftTech/throughliner#beta` and install `throughliner@flintcraft`. Look for: both commands succeed without a ref error.
2. Fully quit and reopen the app, open any empty folder, and type `/setup` in the chat box. Look for: the setup command appears in the menu — the smoke test from INSTALL.md.
3. If either step fails, tell this project the exact error and stop — the install post stays as it is and the pin gets re-examined.
4. On success, edit the "How to install" forum post so its install ask names `FlintcraftTech/throughliner#beta`. Look for: no live claim pointing new users at the unpinned route.
5. Tell this project; the register line for the install post is updated with the corrected claim and this line closes.

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
**Lifted 2026-08-27 at the planning opening.** [discord-post-session-start-strength] was posted and closed in the 2026-08-27 build run (`LOG/2026-08-27-discord-post-session-start-strength.md`), so the chain ahead of this correction is clear. One-a-day pacing applies at posting time: a post went out today, so this goes out on a later day no other Throughliner post does.

**Files:** none — the artifact is a Discord post. Relates to [self-authoring-rules].

#### [user] Discord post draft: plain-English consent [discord-post-plain-english-consent]
Drafted 2026-08-25 at the planning close under the close-sweep design ([plan-close-post-drafting]); approved as a candidate by you, with your addition of the terse-docs mention. [keep-approval-reading-burden] shipped 2026-08-26 and its claims held — then held again 2026-08-27 behind [shared-vocabulary-not-standing-names], whose build retires "the ready list", which this draft's example quotes. **Lifted 2026-08-27 at the planning opening** — that build shipped (`LOG/2026-08-27-shared-vocabulary-not-standing-names-build.md`) and is live on the installed host; the example below is reworded to the method's own words in the same move. Before posting: re-verify the whole draft against the shipped build, then post on a day no other Throughliner post goes out — a post went out today.
**Draft (under 2,000 characters):**
> **Plain-English approvals.** When you and Claude go through your captured ideas in a planning session, each one now opens with a plain-English summary of what the idea says — right there in the chat, before any analysis. And when Claude recommends what to do with it, it says in plain words what would actually change ("this would move into Processed, cleared to run — the part of the queue the build command works from") and asks whether you agree, in those words. No procedure jargon, no needing to open the queue file to know what you're saying yes to: you approve what's in front of you.
>
> The files themselves stay tidy through a companion rule: everything written into your project's documents is bounded by the project's own measured norms, so records stay terse enough to actually read when you do open them. The summary serves the moment; the documents serve the return visit.

#### [audit] Features requiring a tip post — coverage sweep [features-needing-tips-audit]
Filed 2026-08-27 at the decision step, from your instruction on the tips restructure ([posting-rule-two-kinds-and-tip-pipeline]): a load of longstanding features have never had a post, and those are fed in by date rather than by release. This audit is what finds them.

Reads SPEC.md's feature set against `INBOX/sent.md`, the FAQ index and `ANNOUNCEMENT-IDEAS.md`, and files one capture per longstanding feature with no tip coverage — a post candidate naming the feature and what a tip about it would teach. Findings go straight to Unprocessed marked unreviewed, per the audit discipline; the next /plan weighs them against the number-mustn't-overwhelm concern rather than posting everything found. Edits nothing.

#### [audit] Compliance audit over the rule changes since the last audit [compliance-audit-lag]
Filed by the rule checks at the 2026-08-27 build close, under the slug they print. `py resources/rule_signals.py .` reported 3 rule-bearing commits since `2026-08-26-compliance-audit-lag-build.md` uncovered by any compliance audit — and this session's own commit makes a fourth, much the largest, so the real scope is wider than the figure the check printed before the commit landed.

Scoped to the changed files (delta scope, as the check computes it): `CLAUDE.md`, `plugin/throughliner/docs/done-build.md`, `done.md`, `feedback-and-inbox.md`, `next-build.md`, `next.md`, `plan.md`, `rescan.md` — plus, from this session, `skill-nonspecific-rules.md`, `next-audit.md`, `done-plan.md`, `setup.md` and `migrate-checklist.md`. The audit run should recompute the list rather than trusting this one, since the check reads it from git.

The criteria are already written and are not re-derived: `resources/method-compliance-audit-checklist.md` carries the four lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history sitting in operative text (the delete-and-read test).

**This session is an unusually good reason to run it rather than a routine one.** It authored or amended roughly twenty rules in a single run, several by supersession and repeal, and it added +47 always-loaded rule statements for consumers and +144 across the fetched procedure docs — the largest single movement the growth report has recorded. Two of the four lenses are exactly what a run that size is most likely to have degraded: rationale creeping into operative text, and tags placed by habit rather than by the arm they govern.

Worth checking specifically, because they were done fast and late in the run: the response-shape tags added across `setup.md` (fifteen steps tagged in one pass, several with conditional arms), and whether the terminology renames left any sentence whose grammar no longer works around the new word.

As an `[audit]` this edits nothing — it reads and files findings as captures, which the next planning session weighs.

#### [user] Delete the test cycle fixture and its filed capture from the demo project [cycles-fixture-cleanup]
Split out of [cycles-due-check-verification], whose verification passed on 2026-08-26 (`LOG/2026-08-26-cycles-due-check-verification-2.md`). What remains is housekeeping in another project, not verification: `DEMOS/Polit Fart Announcer 1` still carries the made-up `CYCLES.md` with its `[weekly-listen]` definition and fixture observable of 2026-08-10, plus the `[weekly-listen]` entry the check filed into that project's Unprocessed.

Both are downstream of a fixture rather than work that project chose — the user's correction on 2026-08-26: the whole cycle was made up as a test, not just its date. The three items the filed entry overlaps ([reload-persistence-check], [other-chimes-unheard], [honorifics-never-fired]) were queued on their own merits and are untouched by this.

Filed as its own item because a walkthrough ends at the item's observable and cleanup after a test gets its own line — and because no session here writes another project's files, so this can only be done in that project's own chat. It blocks nothing: the verification it follows has already passed.

**Walkthrough.**
1. Open a chat on `DEMOS/Polit Fart Announcer 1`. Ask Claude there to delete `CYCLES.md` from the project root. Look for: the file gone from the folder listing.
2. In the same chat, ask Claude to delete the `#### [user] Weekly listen-through of the page is due [weekly-listen]` entry from that project's Unprocessed. Look for: the entry gone from QUEUE.md, and the three items it named still present.
3. Tell this project it is done; this item closes.

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

#### [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]
Filed 2026-08-27 with [posting-rule-two-kinds-and-tip-pipeline], from your instruction that the how-to topics be editable and maintainable by the bot. The constraint that makes this an item at all (recorded in `TOOLS.md`): a bot can only edit messages it authored itself, and the existing how-to posts are yours — so bot maintainability requires each one re-posted by the bot once, after which every later tweak is a bot edit under the approval rule.

**Walkthrough.**
1. Once the posting script exists, Claude fetches each how-to post's current text through the bot and shows it to you unchanged. Look for: the text matching what the forum shows.
2. On your yes per post, the bot posts the replacement in the same topic. Look for: the new post appearing under the bot's name.
3. You delete your original post of each (only you can — the bot cannot delete or edit your messages in a forum topic it doesn't manage, and your authorship is the thing being replaced). Look for: the topic showing only the bot's copy.
4. The register line for each how-to post is updated to point at the bot's copy, with the channel named; this item closes when every how-to topic's live text is bot-authored.
Blocked by: [discord-posting-bot]

## Unprocessed

#### Last session advises running a build next [forward-advisory]
Advice from the 2026-08-27 second planning close, not work. The next planning run reads this and deletes it in the same breath.

**Build next.** 19 items are cleared to run and nothing unprocessed overlaps them — Unprocessed holds only six date-held captures (none due before 2026-08-28) and [close-removes-completed-user-items], whose premise the close that filed this has already spent: that capture is a first candidate for the droppable set. The run's shape: thirteen builds first — the Discord posting stack (bot script, prune, collision guard, tips model, entry lifecycle), the hand-over checkpoint, and five doc fixes — then the walk-throughs and two audits batched at the end. The compliance audit recomputes its scope from git, so it covers the rule builds the same run ships.

**One caution for the run:** [discord-posting-bot] is the stack's foundation — several later items call its script — so if it halts, expect the prune, the entry lifecycle and the how-to migration to wait on it.

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
Held 2026-08-27 with the new capture bow-out field, so it stops being re-offered while the wait runs: the blocker is now cleared to run, and this returns by itself once it is built.
Blocked by: [weekly-release-cycle]

#### Close removes the four completed walk-through items — guard note [close-removes-completed-user-items]
Filed by /rescan 2026-08-27 as belt-and-braces. This session's close is due to remove five completed `[user]` items from Processed, four proven done by their LOG records — [discord-bot-server-setup], [cycles-due-check-verification], [discord-post-session-start-strength], [test-rezips-entries-name-obtain-route] — and [bot-token-reset], walked to its verified end in this session (new token authenticated, old one dead). The intent otherwise lives only in this conversation. Once the close has done it, this capture's premise is gone and the next planning session deletes it in the droppable set.

