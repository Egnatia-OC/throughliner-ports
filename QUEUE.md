# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**done.md recommend-next: capture-overlap scan + continuation ask + reorder offer** **[recommend-next-overlap]**
Depends on: push-in-commit

done.md's Plan close-out Step 4 and Build close-out Phase 3 currently hard-code "Run /next when ready" whenever batches exist, with no branch for dependency-aware recommendations. That shape silently encourages deferring to the user — the recommendation collapses to /next regardless of unprocessed captures sitting in the queue or how they relate to the top batch. Three additions tighten the close-out: (1) before recommending, mirror next.md Step 1.4's blocker-gate scan — check Captures for items relevant to the top batch (contradict, invalidate, or would benefit) and recommend /plan first if any are found, naming the overlap; (2) ask whether the user is continuing into another /next now, since cranking through batches back-to-back (remote control or similar) makes the next /next imminent; (3) when continuing and a reorder is applicable, offer to reorder the queue now so the next /next picks the right item. The reorder offer follows the general rule added to plugin-behaviour.md Dependency ownership.

Build:
- plugin/si-plugin/docs/done.md Plan close-out Step 4 (Recommend next): before the recommendation, scan unprocessed captures for overlap with the top batch — mirror next.md Step 1.4 (contradict / invalidate / would benefit). If overlap exists, recommend /plan first and name the overlap. Then ask whether the user is continuing into another /next now; if yes and a reorder is applicable, offer to reorder per plugin-behaviour.md Dependency ownership.
- plugin/si-plugin/docs/done.md Build close-out Phase 3 (Recommend next): same change.

**Sweep done.md Plan close-out for removed-concept leftovers** **[sweep-removed-concepts]**

done.md Plan close-out Step 1 (Recap) still lists "Questions resolved" as a bullet type — leftover from when OPEN-QUESTIONS existed as a tracked concept. That concept was removed but the recap field wasn't swept. Small fix on its own, but worth doing as a sweep — drift checks were also removed during the V47 OQ-promotion era, and any other Plan close-out field referencing concepts that no longer exist should go on the same pass. Stale field names in a recap template train Claude to fabricate content to fill them.

Build:
- plugin/si-plugin/docs/done.md Plan close-out Step 1 (Recap): drop "Questions resolved" from the bullet list.
- Same pass: sweep done.md Plan close-out for any other field referencing removed concepts — OPEN-QUESTIONS, drift check, or anything else from the V47 OQ-promotion era. Drop any found. If nothing else surfaces, the batch is the single bullet removal.

**Stage sweep edits at push; warn on dirty plugin tree at session start** **[stage-sweep-dirty-warn]**

push-and-rezip step 8 stages a fixed list (zip, archive, plugin.json, LOG/) that doesn't include whatever the pre-push sweep modified. Sweep edits — prose tightening in plugin/si-plugin/ to keep templates and skill docs aligned with the procedure changes being pushed — fall out of the commit and sit orphaned in the working tree across sessions. The next /next can then layer build edits on top of orphaned sweep changes, mixing unrelated work into one commit. Two complementary fixes addressing the two failure modes: at push, stage every dirty path in plugin/si-plugin/ rather than a named list (catches sweep edits automatically); at session start, when no build is in progress, warn if plugin/si-plugin/ has uncommitted state (catches existing orphans before a new build layers on top). Both edits land in this project's CLAUDE.md — the push-and-rezip workflow lives there, not in the shipped plugin.

Build:
- CLAUDE.md push-and-rezip step 8: replace the fixed stage list ("zip, archive changes, plugin.json, LOG/ changes") with an instruction to stage every dirty path in `plugin/si-plugin/` (via `git status --porcelain plugin/si-plugin/`) plus the zip in `plugin/`, archive changes in `plugin/zip-archive/`, and LOG/ changes. Sweep edits get caught automatically.
- CLAUDE.md (this project's, root): add a session-start dirty-tree check. When a session starts with no `_build.md` present in the project root, run `git status --porcelain plugin/si-plugin/` and warn the user if non-empty, listing the dirty paths. Surfaces orphaned sweep edits before /next layers build changes on top.

**Fix /clear-before-/done close-out order** **[fix-clear-before-done]**
Blocks: sweep-clear-compact

next.md Step 7 and plan.md Step 4 close-outs both tell the user "Run /done to record this and commit, or keep adjusting. Run `/clear` first to keep context clean." The "first" places /clear *before* /done, but /done reads the conversation to write a faithful LOG entry — clearing first strips exactly what /done draws on. The /clear advice already lives correctly at the end of /done itself, where it recommends clearing before the next skill. Fix is to drop the misplaced sentence from both offering close-outs; the post-/done placement carries the advice in the right spot.

Build:
- plugin/si-plugin/docs/next.md Step 7 (line 142): remove the "Run `/clear` first to keep context clean." sentence from the close-out. Keep the /done offer.
- plugin/si-plugin/docs/plan.md Step 4 (line 85): same change — drop the /clear sentence, keep the /done offer.

**Sweep all `/clear` and `/compact` references from skill and procedure docs** **[sweep-clear-compact]**
Depends on: push-in-commit, fix-clear-before-done

The two prior batches (**[push-in-commit]** and **[fix-clear-before-done]**) remove every known `/clear` site in skill close-outs. This batch is the safety sweep behind them: confirm nothing survives. `/compact` gets swept on the same pass — the principle is the same. When to clear or compact is a user judgment call about session continuity, not a procedural step Claude should issue routinely; surfacing it as close-out boilerframe trains both Claude and the user to treat it as default behaviour when in practice it depends on what's coming next. Skill and procedure docs should not nudge either way.

Build:
- Grep `plugin/si-plugin/` for `/clear` and `/compact`. For each hit in a skill doc (skills/*) or procedure doc (docs/*.md), remove the reference — close-out sentences, reminder lines, "run /clear before X" guidance.
- Hits in plugin-behaviour.md get reviewed case-by-case. Per the capture's reasoning, even a single principle-level statement there counts as a routine nudge; default is to remove unless there's a specific reason to keep.
- After edits, re-grep to confirm no `/clear` or `/compact` references survive in skill or procedure docs.

**Sweep "disposition" jargon from plugin/si-plugin/** **[sweep-disposition-jargon]**

Alex flagged she has trouble parsing "disposition" herself — external non-coders will too. The term currently appears in procedure docs as the label for the promote/park/drop choice, and leaks through into user-facing chat during /plan Step 2 ("Disposition?"). The audience anchor in CLAUDE.md already rules out the user-facing leak, but the term should go from the procedure docs as well — the docs read more clearly with plain phrasing, and there's no internal-vs-external split worth maintaining. One vocabulary across docs and chat.

Build:
- Grep `plugin/si-plugin/` for `disposition` and `dispose` (case-insensitive). Replace each hit with "promote, park, or drop" or equivalent plain phrasing — procedure docs, skill docs, anywhere else. Where the surrounding sentence reads awkwardly after substitution, rewrite locally.
- Re-grep after edits to confirm no surviving hits.

**Tighten next.md Step 4: drop general add-to-scope offer, keep narrow coherence exception** **[next-step4-coherence]**

next.md Step 4 ("User raises something out of scope") currently has an "Adding to scope instead" sub-section letting Claude offer to fold the raised item into _build.md as a new entry. The framing reads as a user-convenience workaround, but the effect is that out-of-scope ideas leak into the active build's commit and log entry — polluting what should be one coherent change. The new default: anything raised mid-/next that isn't already in the batch routes to Captures, full stop. The exception is narrow and keyed to why-pipeline coherence — the raised item is part of the same change if it would share the build's log entry and index line, and folding it in makes the batch easier to find later, not harder. Evaluated against the why-pipeline and index-entry rules (which the queued batches define), not against whether the user wants it in.

Build:
- plugin/si-plugin/docs/next.md Step 4 ("User raises something out of scope"): delete the "Adding to scope instead" sub-section as currently written. Replace with a narrower coherence exception. Default: route to Captures. Exception: if the raised item shares the build's log entry and index line per plugin-behaviour.md Index entries (per the queued index-entry batch) and would make the batch easier to find later, fold into _build.md as an additional entry. Evaluation is against the why-pipeline coherence rules, not user convenience. Cross-reference the index-entries rule rather than restating its criteria.

**Document next.md build-abort mechanics** **[build-abort-mechanics]**

next.md Step 5 mentions "abort and requeue" as one course-correction option but never spells out what that means mechanically. The gap leaves Claude to improvise: is _build.md deleted? Does the batch return to QUEUE.md as-was, or with progress notes? What happens to captures surfaced during the aborted attempt? Where does the abort land in the LOG? Without an answer, abort becomes a path Claude avoids because the mechanics are unclear, which means salvage-attempts get pushed past their useful point. Fix: define the abort procedure inline at Step 5 — delete _build.md, return the batch to QUEUE.md (at its original position or top, Claude's call per Dependency ownership), route any captures surfaced during the attempt as normal, and write a LOG entry capturing what was attempted and why it was aborted so the reasoning carries forward. The abort entry uses the normal Build close-out shape but the "what was built" content describes the attempt rather than a completion.

Build:
- plugin/si-plugin/docs/next.md Step 5: expand the "abort and requeue" option from a phrase to a small procedure. Specify (1) delete _build.md, (2) return batch to QUEUE.md (placement per Dependency ownership), (3) route any captures surfaced during the attempt to Captures as normal, (4) write a LOG entry describing the attempt and why it was aborted (uses the normal Build close-out shape, "what was built" describes the attempt). Cross-reference done.md so the user invokes /done normally — /done's mode detection still sees _build.md exists, runs Build close-out, the only difference is the LOG entry content and that the batch returns to QUEUE.md rather than getting completed.

**Rewrite next.md Step 7 "keep adjusting" close-out language** **[keep-adjusting-rewrite]**

next.md Step 7's close-out invites the user to "keep adjusting" alongside the /done offer. The phrase is doing useful work — sometimes a build needs a small within-scope tightening pass before /done — but it reads as permission for ad-hoc mid-build ideation, which is exactly what plugin-behaviour.md Scope discipline rules out. The fix narrows the language: adjustments are for tightening within-scope work that's already in _build.md, not for raising new in-scope or out-of-scope items (those route through Captures or Step 4 respectively, both already covered). Small wording change, but it removes a quiet contradiction with the broader scope-discipline rules.

Build:
- plugin/si-plugin/docs/next.md Step 7 close-out: rewrite the "keep adjusting" framing. New shape: the adjust-or-/done choice is between (a) running /done now, or (b) tightening already-built entries before /done. Anything new — in-scope or out-of-scope — routes through the existing paths (Step 4 for out-of-scope, captures for thinking work), not through the close-out as ad-hoc continuation.

**Route mid-build discoveries of unplanned user testing to Captures** **[route-unplanned-testing]**

When /next surfaces a need for user-runnable testing during a build — beyond what the batch's Test section specifies — the discovery currently has no defined home. Claude might inline-prompt the user, queue it ad hoc, or forget. None of those preserve scope discipline: inline-prompting breaks the build's flow and pollutes the commit and log entry, ad-hoc queuing skips the /plan dialogue that batches need, and forgetting loses the discovery entirely. Routing through Captures puts the surfacing in the same path as every other out-of-scope discovery, and a future /plan converts it to a test-only batch with the dialogue it needs to be specified properly.

Build:
- plugin/si-plugin/docs/next.md: add a routing rule (Step 5 course-correction is the natural home) stating that when /next discovers a need for user-runnable testing beyond what the batch's Test section specifies, route it to Captures as a future test-only batch. Don't attempt it inline. Don't extend the current batch's scope to include it. Frame as a parallel to the existing out-of-scope-item rule — same destination (Captures), different surfacing source (Claude's own discovery rather than user input).

**Speed up LOG hash backfill with `git log -S`** **[hash-backfill-speedup]**

The backfill instruction in plan.md and next.md suggests `git log --diff-filter=A` or blame, both of which return a wider set of commits that Claude has to scan and match to entry titles by eye, plus often reading the full log files for orientation. `git log -S "<entry title>" --pretty=%h -- LOG/` returns the hash mechanically per placeholder — no scanning, no matching, no log reading. Pair it with a batch-read of every file containing `[HASH]` upfront so Edit's read-first rule is satisfied in one round-trip instead of one per placeholder. The instruction lives in two places (plan.md Step 1, next.md Step 1) and gets the same rewrite in both. Three further simplifications tighten the common case. A `git grep -l '\[HASH\]' -- LOG/log.md LOG/index.md` gate up front makes the step a true no-op with zero reads when nothing matches. The common case is one new entry — one placeholder in log.md and one in index.md sharing the same hash — so a single `git log -n 1 --pretty=%h -- LOG/log.md` handles both without per-placeholder lookups; `git log -S` falls back in only when the common case doesn't apply (multiple entries waiting, or hashes don't match). Restrict the scan to `LOG/log.md` and `LOG/index.md` specifically (or use the stricter patterns `^## \[HASH\]` and `^- \[HASH\]`) so archived files like log-v1.6.1.md, which contain the literal string `[HASH]` in prose about the placeholder mechanism, don't false-positive.

Build:
- plugin/si-plugin/docs/plan.md Step 1 "Backfill LOG hashes first": rewrite the instruction. New shape: (1) run `git grep -l '\[HASH\]' -- LOG/log.md LOG/index.md` first — if empty, return immediately; (2) batch-read the matching files; (3) common case: if there's one placeholder in each, run `git log -n 1 --pretty=%h -- LOG/log.md` and use that hash for both; (4) fallback: for each remaining placeholder, run `git log -S "<entry title>" --pretty=%h -- LOG/` and use the returned hash; (5) replace `[HASH]` in place. Drop the `--diff-filter=A` and blame fallbacks.
- plugin/si-plugin/docs/next.md Step 1 "Backfill LOG hashes": same rewrite, same shape.

**Add install guide for non-coders pointing at fresh Claude chats** **[install-guide]**
Blocks: e2e-install-guide

The README currently has a 3-step Install section that assumes the reader already has Claude Code installed and just needs to drop the zip in. That covers the existing-user path but skips the harder one: non-coders who don't yet have Claude Code, don't know they need a paid plan, and don't want to touch a terminal. The current install section is also positioned mid-page, so even the fast path requires scrolling. Fix is two-part: rework the README to give the existing-user path a one-liner at the top, then bridge into a pointer aimed at non-coders telling them to open a fresh Claude chat and ask it to guide them through setup. The bridge points at a new INSTALL.md written for Claude reading on the user's behalf — opens with framing (desktop app only, no terminal except where strictly necessary, assume zero terminal experience), interviews the user to figure out where they are (OS, Claude Code installed yet, paid plan?), then branches into Claude Code install + paid plan setup, then plugin install. The guide embeds the one-item-at-a-time guidance block from Alex's global CLAUDE.md so Claude paces the walkthrough properly. The new shape preserves the fast path for already-set-up users while removing the biggest non-coder friction point: not knowing what to install first.

Build:
- README.md: move Install section to position #1 (above "Who it's for"). Rewrite as two parts. (a) One-line shortcut at top — direct zip link + condensed 3-step Customise > Plugins flow for already-set-up readers. (b) Bridge paragraph for non-set-up readers — "New to Claude Code? Open a fresh Claude chat at claude.ai, paste this link [link to INSTALL.md], and ask it to guide you through setup. The guide walks you through Claude Code install, paid plan setup, and plugin install. Built to assume no terminal experience."
- New INSTALL.md at repo root. Opens with a framing block aimed at Claude (this guide is being read on a user's behalf; desktop app only; don't route to terminal except where strictly necessary; assume zero terminal experience). Then an opening interview: questions Claude asks to determine OS, whether Claude Code is installed, whether they have a paid plan. Then two branches: (A) install Claude Code desktop app, with the paid-plan requirement stated honestly; (B) install the SI plugin (expand the existing 3-step Customise > Plugins flow for someone who's never touched the plugin UI). Embed verbatim the one-item-at-a-time guidance block from C:\Users\Alex\.claude\CLAUDE.md so Claude paces the walkthrough.

**E2E: install guide drives a fresh Claude chat through SI setup** **[e2e-install-guide]**
Depends on: install-guide

Once INSTALL.md and the README reframing exist, the only meaningful verification is the actual flow it's meant to support: a fresh Claude chat with no prior context, given the repo link and "guide me through setup." This catches three things at once — whether Claude finds INSTALL.md from the README pointer, whether the opening interview questions land for a real user, and whether the branched walkthrough (Claude Code install → paid plan → plugin install) runs cleanly. Splitting this from the build batch keeps the build commit clean and gives the test its own LOG entry, since the result is feedback (does the guide work?) not changed files.

Test:
- E2E (user-run, separate live session): open a fresh Claude chat at claude.ai with no prior context. Paste the SI repo URL. Say "guide me through setup." Observe whether Claude finds INSTALL.md, runs the opening interview, and walks through the branches cleanly. Report findings as captures (anything Claude missed, mis-paced, or routed to the terminal when it shouldn't have).

### Parked

- **[sizing-gates-rework]** Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- /next's Step 7 completion close-out says "Run /done to record this and commit, or keep adjusting" — but Claude has been observed instructing the user to run /next instead, while still inside /next after the batch completed. Two problems with that drift: (1) it skips /done entirely, leaving the build uncommitted and _build.md in place, which then blocks the next /next via the "one build at a time" rule; (2) it nudges the user toward a back-to-back build pattern that bypasses the close-out judgment steps /done exists to enforce. The doc says the right thing already, so the fix isn't a wording change at Step 7 — it's tightening whatever lets Claude substitute /next for /done at completion. Candidates: tag Step 7 [SEQUENCE] or add an explicit "never recommend /next from inside /next" rule under Scope discipline in plugin-behaviour.md, since "one build at a time" is the same principle in different framing. Pairs with **[keep-adjusting-rewrite]** — that one narrows what "keep adjusting" means; this one closes the larger /done-skip drift.

### Parked

- Trickle-up audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for rules that are repeated across multiple docs or aren't skill-specific. Move them to plugin-behaviour.md so they're stated once and apply everywhere. Parked pending the audit-as-batch-type batch landing — once /next handles audit batches, this gets promoted as an audit batch with the target (the four procedure docs) and criteria (repetition, non-skill-specific rules) already defined here.

- Output tag overhaul audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for prose that describes output behaviour where a tag ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) should be used instead. Includes: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report). Parked pending the audit-as-batch-type batch landing — same reason as the trickle-up audit capture.

- In-scope / out-of-scope distinction audit: review plan.md, next.md, and plugin-behaviour.md for whether the in-scope vs out-of-scope distinction is stated explicitly enough, or whether it's currently load-bearing on Claude's judgment without being written down. The capture this came from also flagged build-abort mechanics and the "keep adjusting" close-out language; both of those got promoted as their own batches. This audit is the remaining thread. Parked pending the audit-as-batch-type batch landing — same dependency as the trickle-up and output-tag audits.

- Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Queue ordering rule: builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into a mechanical rule. (The companion /next-time check — recommend switching to /plan if related captures exist for the top batch — shipped as the next.md blocker-gate capture scan.)
- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
