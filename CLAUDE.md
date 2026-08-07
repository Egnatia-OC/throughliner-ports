# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

Self-hosting: yes

## The two-section redesign is merged in — this is main

The `queue-redesign` fork has been merged back into `main` (see LOG `execute-merge-to-main.md`). Main now carries the full two-section work-item model — Processed / Unprocessed, build/audit flavors with `[user]` walk-through, red flags as tagged state-carrying lines — with main's original plugin identity kept (`sovereign-implementer` / `flintcraft`, not the fork's `-x` rename). The reconciliation started from main's drained `QUEUE.md` and folded forward the still-relevant fork items by judgment; the fork's bloat and shipped work were left in git history. The founding decision and reasoning are in QUEUE.md's history under `[adopt-queue-redesign]` and LOG `fable-goal-queue-drain-adopt.md`.

**Rollout and retirement path.** With the redesign on main, the next steps are: rezip + reinstall to dogfood the merged plugin here, then push + release so the other projects update via the marketplace; the old pre-redesign SI stays frozen on those projects until the new one is adopted there and the old one uninstalled. The one thing to track is *when the merged plugin is trustworthy enough to rely on* — freezing the old one, migrating the other projects, and uninstalling all follow from that.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Audience

The plugin's users are external non-coders building their own apps with Claude Code — not the person developing the plugin. This project is the unusual case: the developer (Alex) is also a non-coder using the plugin to build the plugin. Skill docs must be written for the external user, not for Alex.

Concretely: anything a skill causes Claude to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "plugin-behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where Claude reads them; they must not leak into output the user sees.

When editing any skill doc, check the output-facing strings against this audience before saving.

## Model target

**The method runs on two docsets, one active.** Resolved 2026-08-02 (superseding the single-4.8 target of 2026-06-15): the plugin ships two procedure docsets and session_start picks between them by the running model.

- **Docset A (current, heavy) — frozen 4.8 fallback.** This is the docset the method was built on: heavy, prescriptive, carrying the load-bearing why-clauses that Opus 4.8 needs to follow a rule reliably. As of the freeze (this build ships it), docset A is **not developed further** — it is kept as the known-good fallback so a bad migration to the new docset can never strand the project with no working plugin. That no-strand guarantee is the user's non-negotiable reason for freezing rather than replacing. Its 4.8 steering research stays with it: `resources/research/opus-4-8-verbosity-steering.md`, `resources/research/model-instruction-compliance.md`.

  **The freeze rule, precisely (decided by the user 2026-08-05): the freeze bars development, not corrections.** *Development* — new capabilities, new rules, register changes, anything that alters what the method does — is barred in A. *Correction* — whatever A needs to stay consistent with itself, with the hooks running underneath both docsets, and with SPEC — is permitted, because a frozen fallback that contradicts SPEC or silently misbehaves (A's surviving completion ask made a SPEC sentence untrue for 4.8 sessions; A's next.md failed open on a missing readiness marker) is not a safe fallback. The rule recurs because `setup.md` is the one file the freeze excepts (a /setup question must change in both docsets or neither), so changes touching /setup keep hitting this shape. When correcting A, **author fresh in A's register — never paste from B**: B is lighter *by subtraction*, and the why-clauses it sheds are exactly what 4.8 needs, so B's register applied back to A regresses 4.8's rule-following.
- **Docset B (new, light) — the active docset.** Authored by *subtraction* from the frozen docset A, docset B is lighter and less prescriptive, and it is where the method evolves from here. It serves the 5-series — **Fable 5 and Opus 5** — which converge on wanting less prescription, not more.
- **session_start detection.** The hook picks docset B for the 5-series, docset A for 4.8, and **defaults to A when the `model` field is absent** — the safe fallback, since A is the known-good docset.

**The fork this resolves — why two docsets, not N.** The intuitive worry was one docset per model, which drifts under dual maintenance. It collapses to two because Opus 5 is not "as fussy as 4.8" — it is fussy the *opposite* way: it over-does (self-verifies, expands scope, runs verbose), so Anthropic's guidance for it is *subtraction*, and Fable 5 wants the same. The two 5-series models therefore converge on one lighter docset. Freezing A is what dodges the dual-maintenance drift trap: only B is live, so there is no two-docset sync burden. Research: `resources/research/opus-5-instruction-compliance.md`, `fable-5-instruction-compatibility.md`.

**Authoring rule during the split.** Docset B compresses by shedding why-clauses — but those clauses are load-bearing *for 4.8*, so B's lighter register must never be applied back to docset A: doing so would regress 4.8's rule-following. A is frozen; B is authored fresh by subtraction. Future models are adopted when they arrive; A is a frozen fallback, not a model we regress *to* — we do not reach for an older model to dodge a newer one's behaviour.

**Docset B's plugin-behaviour.md stays one file — deliberately (decided 2026-08-02).** Anthropic's skill conventions name progressive disclosure, and B kept A's monolithic shape anyway. Don't split it, and don't re-raise this on seeing the file's length. Progressive disclosure works for material fetched on a trigger — a reference table, a rare procedure. It fails for standing behavioural rules, which steer behaviour that has no trigger to fetch them: a session doesn't know to go and fetch "lead with the decision," it either has it or it doesn't. Most of that file is exactly that kind of rule. Moving those behind an index doesn't defer their cost, it deletes their effect. The size premise is also half-true: B is 785 lines to A's 373, but that's hard-wrapping at 80 characters — by bytes, which is what actually costs tokens, B is already 55% smaller than A, and the ~500-line figure in Anthropic's guidance is written for SKILL.md, the entry-point file, not a reference doc a skill loads. It would also compound the redirect: B is already reached by an injected instruction to substitute `docs-b/` for `docs/`, and a split would stack an index-fetch on top of that, so a skimmed directive would leave a session governed by rules it never read with nothing detecting it. Reopen only if the redirect mechanism changes ([docset-routing-mechanism]) or the genuinely trigger-fetched minority — the red-flag lifecycle, working-mode rendering, the feedback channel — grows into a majority.

This is phase 1 of three: this build records the decision and freezes A. Phase 2 authors docset B by subtraction ([opus5-docset-b-authoring]); phase 3 wires the session_start model detection ([opus5-session-start-detection]).

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only a `claude` CLI install/update against the committed marketplace plus a full app restart does (the desktop app's in-app plugin upload is gone; see the Rezip and Release rituals below for the exact commands). A bare working-tree or zip edit changes nothing the host sees, because the host runs a frozen snapshot the CLI copied into `~/.claude/plugins/cache/...` at install time, not the live files.
**Target** = the editable source at `plugin/si-plugin/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**3 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — two sections (Processed / Unprocessed), each holding work items as `#### ` headings with rationale beneath. A work item that carries a security or privacy risk gets a red-flag marker (a `Red flag · State:` tag) — the flag rides the work, not the other way around.
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`.

**4 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top ready work, execute it (build or audit), walk the user through `[user]` work items. Works the cleared region top-down, so one invocation can build several cleared lines back-to-back — the unattended-in-practice runner, closed by /done.
- `/done` — record what happened, clean up, commit.

**3 hooks** — two enforcing, one advisory:
- `session_start` (enforcing) — detect project state (unadopted / adopted / active build), load behaviour rules, check plugin version against .si-version.
- `pre_tool_use` (enforcing) — scope-lock to the active run's file list in `_build.md` (which governs SPEC.md like any other file — SPEC is editable only by a run that lists it), git safety, and mechanical denial of scripted shell file-writes.
- `post_tool_use` (advisory) — QUEUE.md structure lint; flags format drift after a QUEUE.md edit, never blocks.

## Where things live

```
No code method/
  CLAUDE.md              — this file
  AGENTS.md              — a pointer at this file, nothing more. A Codex-era
                           copy of CLAUDE.md, gutted 2026-08-05 after it
                           drifted; kept as a redirect in case any tool loads
                           AGENTS.md by name.
  .gitignore
  plugin/                — plugin packaging
    si-plugin/           — target source
      .claude-plugin/    — plugin manifest
      hooks/             — session_start, pre_tool_use, post_tool_use
      skills/            — setup, plan, next, done
      templates/         — CLAUDE-TEMPLATE.md
      docs/              — procedure docs loaded by skills
    si-plugin.zip        — current installable zip
    zip-archive/         — versioned archive of past zips
  SPEC.md                — this project's spec (once /setup has run)
  QUEUE.md               — this project's work queue
  LOG/                   — this project's session logs (index.md + per-entry files)
```

**Worktrees (recorded 2026-08-05).** This folder is the main working tree. One linked worktree shares its object store: the shelved Codex port at the sibling folder `..\Sovereign Implementer - Codex port\`, on branch `codex/si-port`. The merged `queue-redesign` worktree (an orphaned folder under the old `C:\Users\Alex\` profile) was removed from git's registry on 2026-08-05 — its branch was fully merged into main; the leftover folder on disk is the user's to delete, and `origin/queue-redesign` still exists on the remote pending the history-rewrite's branch-coverage decision.

## Working conventions

- **Use absolute paths** for sub-folder lookups. `<PROJECT_ROOT>\plugin\si-plugin\...` — substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on your machine.
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Cross-doc references go by name.** When editing the docs under `plugin/si-plugin/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a batch adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Author method text 4.8-shaped.** Every self-hosting build batch and spec-writing batch is run against the 4.8 section of [`resources/authoring-heuristic.md`](resources/authoring-heuristic.md) before its authored text ships — the short checklist distilling what Opus 4.8 (this project's model target) actually steers on. That doc is also the home for rule-writing rules (the model-agnostic "Rules about writing rules" section — e.g. when a slipped rule earns a hook vs. just sharper wording), so reach for it both when authoring text and when deciding how to fix a rule that slipped. Self-hosting scope: the doc is host-only and not in the plugin package, so the check stays in this project. Revisit shipping the check if the doc ever ships into the package.
- **FAQ entries are part of batch authoring.** When /plan authors a batch that introduces something a consumer would see or ask about — a new queue line, a new doc section, a new narration moment — the batch carries a `plugin/si-plugin/templates/faq-template.md` entry (plus its `faq-index-template.md` index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer? If yes, the FAQ entry ships with the batch. Host-project rule, not shipped plan.md — consumers never author FAQ entries, so the rule would misfire in their /plan sessions.
- **README feature-list sync rides the SPEC-sync trigger.** A change that adds or removes a user-facing feature — a skill, a mode, a command, or user-visible hook behaviour — already must update SPEC.md. That same moment also syncs README.md's "What it does" feature list, which is the plain-English mirror of SPEC's feature list. One more clause on the existing trigger, not a new detection point. Host-only concern: consumers don't maintain the method's README.
- **FAQ-sync is a hard close gate with a logged disposition, host-only.** The batch-authoring FAQ rule above fires at authoring time and doesn't reliably catch every case, so the method's own shipped FAQ drifts behind the skills. It was first written as a soft "confirm the entry was written" self-check riding the SPEC-sync close trigger, and it failed on its first real test — a close synced SPEC and skipped the FAQ, and nothing recorded that it had. It borrowed SPEC-sync's trigger but not its teeth: SPEC-sync works because it is a *blocking* gate whose result lands in the same commit, which a close cannot step past.

  So: **a session whose commits carry a user-facing change cannot close until the FAQ is dispositioned, and the disposition is written into the LOG entry as its own explicit line.** Same trigger as SPEC-sync — a change that adds, removes, or alters something a non-coder would meet — and the same read moment, so it costs nothing extra to detect. What is new is that the close cannot proceed on a silent skip, because the LOG entry is missing a line it is required to carry:

  ```
  FAQ: updated <entry name>
  FAQ: not needed because <reason>
  ```

  The logged line is the teeth. A skip is still allowed — plenty of user-facing changes genuinely need no entry — but it becomes a visible, auditable statement someone can later disagree with, rather than an omission nobody can see. **A pure hook was rejected:** "is this change user-facing?" isn't mechanically detectable the way QUEUE structure is, so a hook would either miss cases or fire falsely. The gate rides a read that already happens.

  Host-only by residence, exactly like the two rules above: this clause lives in this project's CLAUDE.md, which consumer projects don't carry, so it never fires for consumers — who don't maintain the method's FAQ. Keeping the *method's* FAQ current is the developer's job, so it stays here rather than in the shipped done-plan.md / done-build.md.

  When it fires, keep the narration considered: brief, plain-language, lead with the decision, never process-noise about the check itself. Say "This change needs an FAQ entry that isn't there yet — I'll write it before we close." — not a recital of what was scanned.
- **A hook-enforced-format change traces its ripple by grep.** When a work item changes a format or enum the hooks enforce — a marker format, a state value, a section heading the lint parses, a work-item shape — its scope is traced by **grepping the format's literal values across the repo**, not written from the design discussion. The grep must name the enforcing hook AND every doc, template, and FAQ entry that names the values, so the file list is complete before the build starts. The why, from a real miss: the red-flag-states change (`State: cleared`/`uncleared`) was scoped from discussion and missed `post_tool_use.py`'s valid-state set — which would have rejected every new marker — plus done-family docs, setup.md, CLAUDE-TEMPLATE.md, and two FAQ entries; /next's self-scoping caught it only by halting mid-run, the interruption an unattended run shouldn't need. Same family as "A new batch type touches four places": plan-time tracing shrinks the ripples /next must catch, and when it still catches one it captures rather than blocks (see the discovery-vs-underspecification rule in next.md Step 2.2). Host-only: consumers don't author hook-enforced formats, so this stays in this CLAUDE.md, not shipped plan.md.
- **And the same trace generalises from formats to rules: any work item that alters a rule's content greps for that rule's other statement sites, and every hit either joins the Files list or gets a one-line leave-alone reason.** The rule immediately above covers formats and enums, where the literal values make the grep obvious. This is the same discipline aimed at prose: when a work item changes what a rule *says*, grep the rule's key terms and names across the corpus **before the file list is finalised**, and record every statement site found — each one either joins `Files:` or carries an explicit `left alone because …` line in the item.

  **The evidence, because this is the method's most common failure rather than a hypothetical.** The 2026-08-07 pre-compression audit found that nearly every contradiction it turned up had one cause: a rule was changed at one of its statement sites and shipped, leaving its other statements behind — the Claude-raised capture closer, the write-order split, the scaffolded red-flag text, the scope-lock's allow-set stated three different ways. None of these was an authoring error at the changed site. Each was ripple that nothing traced. The planning session that processed those findings was itself a live demonstration: the write-first rule had changed in `plugin-behaviour.md` while six step-level instructions kept saying the opposite, and `setup.md` kept scaffolding a contradicting red-flag line into every consumer's queue.

  **The grep pays for itself immediately, which is the argument for it.** In that one session it found a sixth show-first site the capture's own list had missed, falsified a capture's confident "docset A's copy is correct too" by finding the identical bug in A, and established that no third instance existed so nobody re-runs that sweep. Each cost under a minute, and each changed the file list.

  **Keep the leave-alone line prominent — it is what makes this a gate rather than an intention.** "Grep for ripples" cannot be checked after the fact; nothing distinguishes a grep that found nothing from a grep nobody ran. "Every hit either joins `Files:` or carries a one-line *left alone because …*" is visible in the item, so a reader can tell whether it happened. That asymmetry is the whole mechanism.

  Host-only, exactly like its sibling above: a consumer's corpus is SPEC plus CLAUDE.md plus a queue — a restatement surface small enough that the payoff would not cover a grep per rule-change. Not shipped to `plan.md`.
- **Old plugin history survives in THIS repo as orphan tags — and those tags must never be deleted.** The plugin was rebuilt from scratch on 2026-06-01, and both this repo's and GitHub's *branch* histories start there (earliest branch commit `a69534c`, v1.5.2). But the pre-rebuild history from May 2026 was not lost: it is a **disconnected commit graph** in this same repo, reachable only through 135 tags named `v17`–`v157`, dated 2026-05-12 to 2026-05-29, the earliest being "Initial commit". None is an ancestor of `HEAD`, which is why a clone — which follows branches — appears to show no early history. `git ls-remote` confirms 134 of them are on the remote, so this history is published, not merely local.

  **What the tags actually hold — the project's first month, not just old code.** At tag `v157` alone there are 142 files under `_method/build-log/`, the pre-rebuild logging format: the project's entire record from May 2026, in a folder nobody searching `LOG/` would find (`LOG/` starts on 2026-06-12). Anyone asking "where is the pre-June logging?" finds the answer here, not by searching the tag trees.

  **Do not delete that tag range.** Those tags are the only references keeping that history reachable; deleting them is the single action that would actually destroy it, and git would then garbage-collect the commits. The reason this warning is written down rather than left to judgment: `v17` and `v1.16.0` sort together in a tag list, so the range reads as clutter in a confusing namespace, and tidying it up is exactly the plausible mistake.

  Two questions are open and undecided: whether to rename the range to remove that sorting confusion, and whether to connect the two histories with a graft or replace-ref so the record reads continuously, or leave them disconnected and merely documented here.

  Privacy has been checked: a scrub sweep over the whole orphan history on 2026-08-04 — 179 reachable commits, 3,085 distinct prose files — found no occurrence of the known third-party name.

### Self-hosting dependency ordering

Work-item ordering in QUEUE.md implicitly assumes the next item sees the previous item's effects. That's true for **target-side** changes — edits to files under `plugin/si-plugin/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks (`hooks/session_start.py`, `hooks/pre_tool_use.py`), the loaded skill procedure docs (`docs/setup.md`, `plan.md`, and the `next*.md` / `done*.md` families), and `docs/plugin-behaviour.md` — which only refresh after a reinstall (a rezip, or the reinstall step of a release). A routine push changes nothing the host sees.

When an item depends on a previous item's host-side effects, that dependency does not resolve in-session. **It is not cleared to run.** /plan leaves it below the readiness line with a lift-condition naming what must ship — "once [slug] has been reinstalled into the host" — exactly like any other dependency on something outside the queue.

**The push marker is retired (2026-08-04).** A line `--- Push required before continuing ---` used to sit between batches and was documented here as halting /next. It never did: /plan placed the marker and /next ignored it, so an item needing a shipped, reinstalled host got built against the old host silently — and the wrong results read as the design being wrong rather than the sequencing having failed. This file asserted the halt for months while the shipped docset said the mechanism didn't exist.

So the readiness line is the single gate, for host-side waits like everything else. "Waiting on a shipped host" is one kind of external event, not a category of its own. The dependency model is two routes, not three: `Blocked by: [slug]` for queued work, a lift-condition below the line for everything else.

**What is genuinely lost:** mid-run sequencing. A run can no longer be "build these three, push, then build these two" — the second group waits for the next /plan. In practice a run ends at /done and a push falls naturally there, so the loss is smaller than it reads, but it is a real trade.

**What has not changed:** a decided rule applies from the moment it is decided. There was never anything about a push boundary that suspended reasoning, and there still isn't. In-repo sessions read the queue and the discussion, not just the installed plugin, so decided-but-unshipped standards shape sessions before any push. Treating "not shipped yet" as "doesn't apply yet" breaks the why-pipeline.

Worked example:
```
--- Cleared to run above this line ---

#### Audit the procedure docs against the new capture-routing rules [behaviour-agnosticism-audit]
Blocked by: nothing queued. Lift-condition: once [capture-parking-discipline]
has been pushed and the host reinstalled — this audit reads the injected rules
from the installed plugin, so before the reinstall it would read the old ones.
```

## The branch cycle — and the audit gate that stands before a merge

Work on this project runs in cycles, and the cycle has a shape worth writing down because its most important step is the one nothing forces:

**branch → builds → soak → differential audit over the whole branch span → reconcile (one /plan + /next over the audit's repair captures) → merge → branch again.**

**The gate: a branch does not merge to main until a differential consistency audit has run over its span and the audit's repair captures have been cleared.** Main only ever receives a reconciled state. The audit runs `resources/consistency-audit-plan.md`, which carries both modes — the routine differential one and the occasional full-corpus one.

**Differential means only the rules this branch's commits touched**, each checked against its other statement sites. That is the same check the ripple-grep rule below runs at authoring time, re-run across the branch's whole span as a catch-net for what authoring missed. The **full ten-pass corpus audit stays occasional** — before a compression pass, or when differential audits keep finding things. The one full audit run so far cost eight subagents, which is far too heavy to repeat every merge.

**The audit sits at soak-end, immediately before the merge — not at the end of the build night.** Soak-day work lands on the branch *after* a build-night audit would have run, so such an audit is muddied by construction: the merge outruns it. At soak-end the span is "everything on the branch since main" — builds plus soak in one sweep, with nothing landing after it but the merge itself. Soak days are mostly ordinary queue work rather than rule changes, so the incremental span stays cheap.

**Leakage is tolerable by design, and saying so is part of the rule.** The differential is span-based, so anything one merge lets through is covered by the next cycle's span, with the ripple-grep as the authoring-time first line. The rhythm shortens the distance between a divergence and its detection; it does not promise to catch everything once.

**This is a convention, not a mechanism — and that distinction is the risk.** Nothing enforces this gate. No hook checks it, no script blocks a merge, no lint flags a branch that skipped it. That is precisely the shape of the **retired push marker**: documented in two docs, implemented in neither, silently letting work run against a stale host until the wrong results read as the design being wrong rather than the sequencing having failed. This gate escapes that fate only because **the merge is itself a queue item whose prose carries the gate**, and this section is what tells whoever writes the *next* merge item to include it. If a merge item is ever written without it, nothing will notice. Don't mistake the convention for enforcement.

### The soak-end sequence — the merge-and-rebranch mechanics, written down

The rhythm above names the phases; this is how the merge-and-rebranch moment is actually run, recorded from the first merge that completed (2026-08-08) so it is repeated rather than rediscovered:

```
1. commit everything on the branch, INCLUDING the hash backfill
2. git checkout main
3. git merge <branch>                    # fast-forward when nothing landed on main
4. verify: git branch --merged main      # the branch appears
           queue structure survives      # item count, both sections, ONE marker
5. git push
6. git checkout -b <next-branch>         # the "branch again" step — easy to skip,
                                         # and skipping it lands the next blitz
                                         # straight onto main
7. rezip + FULL app restart              # so sessions run the build being tested
```

**Two blockers recur at every soak-end, and both are the method's own mechanisms colliding with a branch switch.** First, the hash backfill dirties `LOG/index.md` every session by design, and an uncommitted backfill aborts `git checkout` because that file differs between branches — the error names a file the user has no reason to connect to the hook, so step 1 commits it first, always. Second, a file the branch deletes but the *stale installed host* still writes gets regenerated untracked and blocks the checkout (the payload-sample file did exactly this); move it to the scratchpad and let the merge remove it from main for good. One inversion worth keeping in mind: a merge can be what *removes* an exposure from main — main carried the tracked payload sample publicly for as long as that branch went unmerged, so holding a merge is not automatically the cautious option.

Two things deliberately left open rather than decided here: whether the blockers deserve mechanical help (a pre-merge check reporting "these files will block the switch" would be cheap and fire once per cycle), and whether step 7 rightly follows the merge — the first run did it before, by accident rather than design.

**A release fires from `main` after the merge, never from the branch.** The Release ritual's trigger carries a branch condition (see the Push ritual's release check below) written as this gate's reciprocal: the two were originally written without each other in view, which is how a branch close once ran the release check thirteen commits ahead of main and had to be held by hand. When a held release contains an actively-spreading fix, the escape is to expedite the merge, not to release from the branch.

`resources/overnight-blitz-plan.md` defers to this: its own sweeps now name the soak-end differential audit as their one home, and its handoff names the audit-then-reconcile gate as what "earned trust" means before a merge is offered.

## Rezip (local testing), Push (routine), and Release (automatic)

**Three separate actions — and the vocabulary changed on 2026-08-04. The old meaning of "push" is retired.** "Push" used to mean the full release ritual, so a push and a release were one event and the word had to be watched for. They are now decoupled and the words mean what they say.

- **Rezip** refreshes the installed host from the local `plugin/si-plugin` folder so Alex can dogfood the plugin privately. Never publishes, never releases, makes no commit, touches no remote. It no longer builds a zip — the local marketplace sources the folder and the CLI snapshots it directly.
- **Push** is `git push` and nothing else. Routine and cheap: it runs after every /next and at any /done, with no version bump, no consistency sweep, no zip and no GitHub Release. Its only question is "is the work on the remote yet?"
- **Release** publishes a version: the bump, the consistency sweep, the repackage, the GitHub pre-release and the host reinstall. It fires **automatically** at any /done whose commits touched files under `plugin/si-plugin/`.

**Why the release trigger is mechanical, and why it must stay that way (Alex's reason, 2026-08-04).** Welding release to push meant every routine save asked "is this good enough to publish?" — a question with no answer when the honest one is that the project is unfinished and will never feel finished. That made releasing something to avoid, so releases stopped happening and the work stayed invisible. Tying the release to a file check removes the question rather than making it easier to answer. **Nothing in this ritual may reintroduce a readiness judgment:** don't ask whether a release is warranted, don't propose holding one back until something is tidier, and don't add a quality condition to the trigger. If the commits touched the plugin, it releases.

**Every release is marked pre-release, and that is the honest label.** The plugin is in active testing and is not ready for the Claude marketplace. GitHub's pre-release flag states that structurally, so it never has to be re-decided or re-worded release by release, and a release is never a claim that the plugin is finished.

Do whichever Alex actually asked for; don't run a release because she asked to rezip.

### Recovering from a project-folder move

Moving this project folder breaks two path-based links that both hold absolute paths and don't self-heal — fix both, then fully restart the app:

1. **Local-directory marketplace.** The desktop app's marketplace registration keeps pointing at the old path: slash commands stop autocompleting and get flagged "invalid" (the cached snapshot still runs when forced). Re-point it in place — `claude plugin marketplace add "<new project path>"` (re-registers the path; no `remove` needed) — then `claude plugin install sovereign-implementer@flintcraft`.
2. **Git worktrees.** This folder is the **main working tree** (`git worktree list` reports it as `main` — corrected 2026-08-05; this section previously claimed it was the `queue-redesign` worktree, which was wrong). One linked worktree hangs off it: the shelved Codex port. A move of either side severs that link both ways — the linked worktree's `.git` file (the `gitdir:` pointer) and this repo's `.git/worktrees/<name>/gitdir` back-reference both hold absolute paths — and git reports "not a repository" in the linked tree until both are repointed.

Consumers are unaffected — they install from the GitHub marketplace, which has no local path to break.

### Rezip (local testing)

When Alex says "rezip" (or asks for a fresh local build to test), run this — no release version bump, no archive, no commit, no push. (The one version change is the test suffix in step 1; the release version is never bumped here.)

**The `-testN` test-build scheme.** A rezip installs a build without touching the release line. **The reason this doc used to give for that is stale, and was checked on 2026-08-04:** it said bumping the release version would nag Alex's own projects to re-run /setup each time. It doesn't — `session_start.py` emits a plain informational line ("an update has been installed") with no re-run prompt. The suffix survives for its real job, which this doc already stated as its honest framing: test builds need to be distinct and unmistakably-test, so each carries a `<base>-testN` version — the release-line base plus `-test` and a number incremented each rezip-for-testing (e.g. `1.12.0-test1`, then `-test2`). Honest framing: the suffix is not what makes a reinstalled host load — the full app restart is (see the relaunch step below). `-testN`'s only job is to keep each test build a distinct, clearly-labeled version that's never mistaken for a release. The suffix lives in the working tree's `plugin.json` only and must be reset to a clean version before any release; the Release ritual's bump does exactly that (Release step 2), so a test suffix never ships in a release. A routine push does **not** reset it — pushes carry no version change at all, so the suffix can and does sit on the remote between releases.

**So `plugin.json` sitting dirty between a rezip and the next release is expected, and it must stay that way.** Every close will see it as an uncommitted file. Leave it. Don't stage it, don't "tidy" it, and don't treat the repetition as a problem to make go away — the reset happens at the Release bump and nowhere else. This has already gone wrong once: faced with the same file surfacing at every close, a session made it stop by committing it, and the public repo advertised `1.16.0-test4` as its version until the next release. The close carries a matching carve-out (`docs-b/done.md`) so it no longer asks.

1. Bump the test suffix in `plugin/si-plugin/.claude-plugin/plugin.json`: read the current version and increment N (`-test1` → `-test2`), or start at `-test1` if the base carries no suffix (`1.12.0` → `1.12.0-test1`).
2. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never gets snapshotted into the installed host (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`. (No zip is built here — the local marketplace sources the plugin from the `plugin/si-plugin` folder, and the CLI snapshots that folder directly. The zip only changes at Push, so a test build never touches it.)
3. Prune the plugin cache at `~/.claude/plugins/cache/flintcraft/sovereign-implementer/`, keeping the current build and the three most recent others — same shape as the Push ritual's zip-archive prune. Nothing else ever removes these, so every test build ever installed accumulates there (ten by 2026-08-04), and the pile makes "which host is actually live?" harder to answer than it should be, which has already cost real time. Command: `Get-ChildItem "$env:USERPROFILE\.claude\plugins\cache\flintcraft\sovereign-implementer" -Directory | Sort-Object LastWriteTime -Descending | Select-Object -Skip 4 | Remove-Item -Recurse -Force`.
4. Refresh the installed host from the local-folder marketplace via the `claude` CLI, then fully restart the app. The desktop app no longer has an in-app plugin upload, and a working-tree or zip edit alone changes nothing the installed host sees — the host runs a frozen snapshot the CLI copied into `~/.claude/plugins/cache/...` at install time, not the live files. So testing the new build means re-running the install/update so the CLI re-snapshots the current `plugin/si-plugin`. Claude runs these commands; Alex types nothing in a terminal.

   **`claude` is NOT on PATH in the desktop app's Bash/PowerShell tools — invoke it by full path.** A bare `claude plugin …` fails with "command not found"; this is the single reason the reinstall has repeatedly been handed to Alex instead of run by Claude, and the workaround previously lived only in LOG entries (so every rezip rediscovered it). The executable is at `~/.local/bin/claude.exe` (equivalently `C:\Users\<you>\.local\bin\claude.exe`); if it isn't there, it's under `AppData/Roaming/Claude/claude-code/<version>/claude.exe`. Run every CLI step in this ritual by full path, e.g. `"/c/Users/<you>/.local/bin/claude.exe" plugin update sovereign-implementer@flintcraft`. Locating and running it is Claude's job — don't hand the reinstall to Alex just because a bare `claude` failed.

   **This is observed on this machine and has never been confirmed as general — don't harden it into a claim about every user's environment.** What is known: the native installer puts the binary in `~/.local/bin` and does not add that folder to PATH (running `claude update` on 2026-08-04 printed exactly that warning), so on this machine the gap is an install-method artefact rather than anything about the desktop app. Whether other users hit it depends on how they installed. That is why the shipped install guide states a *fallback* — "if the command isn't found, find the binary and run it by full path" — rather than asserting the command won't work.

   **Check the CLI against the app before using it.** Compare `claude --version` (the standalone binary this ritual drives) against the desktop app's version, and say plainly when they differ. They drift silently: on 2026-08-04 the CLI was on 2.1.146 while the app ran 2.1.219, and marketplace features have real version floors (the `renames` map needs 2.1.193 or later), so an old CLI fails in a way that reads as the plugin design being wrong rather than the tool being stale. If it's behind, update it first — `& "$env:USERPROFILE\.local\bin\claude.exe" update` — then carry on.
   - First time only — register the local marketplace (the committed `.claude-plugin/marketplace.json`, marketplace `flintcraft`, which points at `plugin/si-plugin`): `claude plugin marketplace add "<PROJECT_ROOT>"` — substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on your machine.
   - Each rezip after — re-snapshot the current build: `claude plugin update sovereign-implementer@flintcraft` (or `claude plugin install sovereign-implementer@flintcraft`).
   - Then a **full app restart, not just a new session** — plugin skills register at app launch, and on Windows a normal quit can leave the app running, so fully quit (confirm the process exited via Task Manager if needed) and relaunch before testing.

   Tell Alex: "Host refreshed via the CLI — nothing has been published. Fully restart the app to load it for private testing."

5. **Prove the hooks are alive, in the first session after the restart.** Two checks, and they answer different questions — neither substitutes for the other.

   - **Shape, before the restart:** run `python resources/testing/hook_schema_check.py`. It drives each hook with a sample payload and asserts the output against the published contract. This is what would have caught `session_start` emitting a shape Claude Code silently discards.
   - **The queue mover, before the restart:** run `python resources/testing/test_reorder_queue.py`. Same reasoning that put the schema check here: `reorder_queue.py` is invoked many times in every planning session, it rewrites the whole queue file each time, and its failure mode is silent — a marker moved as a side effect prints "reordered" and looks fine. The suite guards the marker-position cases specifically, including the observed defect where a `--move` of the marker's anchor dragged the readiness boundary and cleared deliberately-shelved work. It ran green but unwired for weeks, guarding nothing, which is why it is named in the ritual rather than left to be remembered.
   - **The shell-write matcher, before the restart:** run `python resources/testing/test_pre_tool_use_shell_writes.py`. It drives `pre_tool_use` with the scripted-write shapes that actually slipped live (heredoc appends and multi-site substitutions) and asserts the denial fires on out-of-scope targets while the deliberate computed-path fail-open still passes. Wired here for the same reason as the other two suites: an unwired suite guards nothing.
   - **Delivery, in the fresh session:** ask that session **what it actually received in its context** — the exact words that arrived — and check the state lines are there. Never ask whether the output "looks right", and never ask Claude to confirm the hook ran.

   Why the wording matters that much: when the hook was dead, sessions kept working, because Claude read CLAUDE.md and the queue directly and reconstructed roughly what the hook would have said. That reconstruction is indistinguishable from success unless the question is "what arrived?". The same trap applies to *any* mechanism whose output Claude could plausibly rebuild from other context. And "it ran" is not "it worked": running a hook through the CLI with `--include-hook-events` echoes its raw stdout whether or not the harness accepts it. This step lives in the ritual rather than in the queue because a queue item fires once, and this is a bug that returns silently.

### Push (routine)

`git push`. That is the whole action. It runs when Alex says "push", automatically after every /next, and at any /done — no version bump, no sweep, no zip, no GitHub Release, no confirmation needed. Never `--force`. Stage explicitly, as the file-safety rules require; never `git add -A`.

Pushing often is the point: it decouples "the work is safely on the remote" from "I am publishing a version," so the routine action never carries a publishing decision.

**Then check whether a release is due — a file check, not a judgment.** At a /done close, after the commit:

```bash
git fetch --tags && git diff --name-only "$(gh release list --limit 1 --json tagName -q '.[0].tagName')"..HEAD -- plugin/si-plugin/
```

Non-empty output means the commits since the last release touched the plugin, so the **Release** ritual below fires. Empty means it doesn't. Run the check and act on it; don't ask whether a release feels warranted. If no release exists yet, treat that as "release due" and let the ritual create the first one.

**The trigger fires only on `main` (decided 2026-08-07).** Check the branch first — `git rev-parse --abbrev-ref HEAD` — and on any other branch the release check does not run at all: the work stays local or pushed, and the check fires at the first /done after the merge. **This is not a quality condition and must not be read as precedent for adding one.** The ritual bars "is this good enough to publish?" because that question has no answer and asking it is what stopped releases happening; a branch check is the same *kind* of check as "did the commits touch `plugin/si-plugin/`" — mechanical, answerable, no judgment. Why the condition exists: releasing from a branch would publish work that has not passed the pre-merge differential audit gate (the branch-cycle section above) — a release reaches consumers, which is further than a merge goes — and it forks the version line, since the next main release must then skip a number or overwrite the story. **The escape when a held release carries an actively-spreading fix is to MERGE SOONER, never to release from the branch**: the red-flag triage's spreading-versus-sitting-still distinction supplies the trigger, and expediting the merge unblocks the release while keeping the audit gate and the single version line intact. Branch releases with their own version convention were considered and rejected — a permanent version fork accepted for a temporary situation that every merge resolves anyway.

**Both halves of that command are load-bearing, and were verified on 2026-08-04 rather than assumed.** `git fetch --tags` is required because release tags are created by `gh release create` on the remote and are **not** in the local clone until fetched — without it the range fails to resolve. And the last-release tag is read from `gh release list`, not from `git describe --tags`, because this repo carries 135 unrelated local tags (`v95`, `v103`, …) from some other history, none of them ancestors of HEAD; `git describe` failed outright here. `gh release list` reads the actual published releases, which is the thing the range is meant to mean.

### Release (automatic, when the check above says so)

Run this whole ritual automatically, no confirmation needed per step. Every step that says "push" here means the ordinary `git push` above.

1. Backfill any unfilled commit-hash placeholders anywhere in `LOG/` before proceeding. The session-start hook only fires at session start, so a /done that ran earlier in this same session leaves its placeholder unfilled at push time — this step catches it. Same rules as the hook: replace the token only in hash position (an entry heading line or the start of an index line), never in body prose, which may mention the token literally; resolve each to the **oldest** `git log -S "<entry title>"` match, never the newest commit touching the file.
2. Bump version in `plugin/si-plugin/.claude-plugin/plugin.json` to a clean patch/minor — patch for fixes/incremental, minor for new capabilities — and in doing so **drop any `-testN` suffix** the working tree carries from rezip testing (`1.12.0-test3` → `1.12.1` or `1.13.0`), so a test suffix never ships in a release. (The release bump lives here, not in rezip — rezip only ever touches the `-testN` test suffix, never the release line, so a locally-installed test build stays visibly distinct from a published one.)
3. Pre-release consistency sweep — two passes, run in order:

   **Pass A — Gather the feed:** List the commits since the last release, using the same tag lookup as the release check above (fetch tags first; read the tag from `gh release list`, never `git describe`):

   ```bash
   git fetch --tags && git log --oneline "$(gh release list --limit 1 --json tagName -q '.[0].tagName')"..HEAD
   ```
 Read their LOG entries (each session's own file under LOG/) to understand what changed (files touched, features added/removed/renamed, concepts that shifted). **The range is since-the-last-release-tag, not `origin/main..HEAD`** — that older range meant "unpushed," which under routine pushing is usually empty, so the sweep would silently read nothing and pass. The release span is what this sweep is actually about, and Pass A's output is also the feed the release notes are written from in step 10.

   **Pass B — Check for staleness against those changes:**
   - **Target internal consistency:** Do templates match the procedure docs they ship alongside? Compare FAQ templates and CLAUDE-TEMPLATE.md against current procedure docs (field names, doc structure, workflow descriptions). Update any that fell behind.
   - **Project docs:** Check QUEUE.md, SPEC.md, and LOG/ for references to removed features, renamed fields, or old formats that the release span's commits changed. Fix any found.
   - **CLAUDE.md:** Check this file's descriptions (Architecture, Method docs, Rules) against current target state. Update any stale references.
   - **The install path:** re-read README.md's Install section and INSTALL.md against the way the plugin is actually installed today — the commands, the marketplace name, the minimum Claude Code version. This one earns its own clause because nobody who already has the plugin ever exercises it, so it can break completely and stay broken; the only person who would notice is a brand-new user who by definition can't diagnose it. Every other doc gets read by someone eventually. This one doesn't, so the release sweep is where it gets read.
4. Archive current zip: `mv plugin/si-plugin.zip plugin/zip-archive/si-plugin-v<OLD_VERSION>.zip`
5. Prune `plugin/zip-archive/` to the three most recent zips (delete oldest).
6. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never ships in the zip (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
7. Repackage: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip"` (zip the folder, not its contents — internal paths must start with `si-plugin/`). Verify: list the zip's entries and confirm none contain `__pycache__` — if any do, stop and fix before pushing.
8. Stage every dirty path in `plugin/si-plugin/` (run `git status --porcelain plugin/si-plugin/` and stage each listed path — catches any sweep edits from step 3), plus the zip in `plugin/`, archive changes in `plugin/zip-archive/`, plugin.json, and the LOG/ changes (including step 1's backfill edits). Commit: "Bump to v<VERSION> and repackage".
9. `git push`.
10. Publish a GitHub Release for the new version, so users who subscribed via Watch → Releases get notified — a plain `git push` does not fire that notification; only a published Release does. Use `gh`:
    - Tag and title = the new version (e.g. `v1.13.0`).
    - **Always `--prerelease`.** The plugin is in active testing and is not marketplace-ready; the flag says so structurally so it never has to be re-decided per release. Drop it only when the project genuinely leaves testing, which is a deliberate decision, not a judgment made inside this ritual.
    - **Notes summarise everything since the previous release, and must never be the commit message.** Write them from step 3's Pass A feed — the LOG entries across the whole release span, which will usually cover several sessions. The commit message describes one commit; the notes describe a release. So a note that restates the commit message is wrong **even when the span holds a single commit**, because it reports what was typed at a commit rather than what changed for a reader. Group by theme rather than listing commits, say what changed and why it matters in plain English for the Discord reader, and name it plainly as a testing build.
    - Attach the zip: `plugin/si-plugin.zip`.
    - Command shape: `gh release create v<VERSION> plugin/si-plugin.zip --title "v<VERSION>" --prerelease --notes "<summary>"`.
    - If `gh` isn't authenticated in this session (the command errors on auth), don't silently skip the Release — tell Alex how to publish it from the GitHub web UI instead: on the repo's **Releases** page, click **Draft a new release**, create the tag `v<VERSION>`, set the same title, paste the summary as the notes, attach `plugin/si-plugin.zip`, and **Publish release**. The step never silently does nothing.
11. Update the installed host via the `claude` CLI, then tell Alex to fully restart the app. Same mechanism as the Rezip reload step — the host reads a frozen cache snapshot, so without a CLI update + full restart it keeps running the old build. The marketplace is already registered from earlier testing, so this is just: `claude plugin update sovereign-implementer@flintcraft`. **Invoke `claude` by full path — it is not on PATH in the desktop app's shell tools (see the Rezip reload step's PATH note); a bare `claude` fails, but running it is Claude's job, not a hand-off to Alex.** Then tell Alex: "Pushed, released, and rezipped. I've updated the host via the CLI — fully quit and relaunch the app to load it." Before running the update, apply the Rezip step's **CLI-vs-app version check** and its **plugin-cache prune** — same commands, same reasons; they belong to every reinstall, not only the private ones.
12. **Prove the hooks are alive after the restart**, exactly as in the Rezip ritual's step 5: run `python resources/testing/hook_schema_check.py` for shape, then ask the first fresh session **what it actually received in its context** for delivery. A release is the worst moment to ship a silently-dead hook, and this is the only step that would notice.

**Archive accuracy.** Release keeps archiving the previous zip as above. Because only Release ever builds the zip (neither Rezip nor a routine push touches it), the zip in the working tree is always the last release, so the copy archived into `plugin/zip-archive/` at the next release faithfully reflects the prior one. Git history remains the authoritative record either way — each release commits `si-plugin.zip`.

LOG entries are per-entry files — no log capping at release time. Existing `LOG/log.md` and `LOG/log-v*.md` files stay in place untouched: index references work by hash, so old entries remain findable.

## Handoff-claim provenance

When a session opens from a Claude-authored handoff or context prompt — a resume note, a "here's where we left off" summary — treat its claims as unverified until the user confirms them. Claude-written content is not read in the user's voice. The why: a handoff Claude authored is not a user-vouched fact, and a fresh or weaker session can't tell which claims the user stood behind versus which Claude wrote — so a Claude-authored line ("the lint keeps flagging X") must not be used as evidence that the user reported X. Confirm before relying on it. (Resolved 2026-06-26: no claim-marking format is added — this standing rule suffices. Multi-line /next takes its instructions from the queue, user-vouched by construction, so it never reads a mixed Claude-authored directive whose claims would need marking; the one Claude-authored thing a run reads is its own working-state file (_build.md) on resume, read as mechanical state, exactly what this rule already covers.)

## Cross-platform ports

**Why porting cannot work, not merely why it was shelved.** SPEC's "Who it's for" section carries the reasoning: the method *is* model-tuned prose, so a port stops producing the behaviour the wording was written for, and correcting it means rewriting rules until what remains is a different method wearing the same name. Precisely: rewording changes the method unless fidelity is actively maintained, and a port has neither a maintainer nor a neutral middle version to maintain toward. Read anything proposing a port against that before weighing its enthusiasm — the decision below is a structural finding, not a policy that a keen contributor's offer should reopen.

This project — the **canonical** SI for Claude Code — is the only port under active development. A **Codex** port once existed as a separate distribution with its own procedure docs and hooks, but it has been **shelved indefinitely** (dormant since 2026-07-28). The method now evolves solely on the Claude side; there is no live two-way relationship to maintain, and no Codex-side work to weigh against.

The shelved Codex port is downstream-only: its source (at `<PROJECT_ROOT>\..\Sovereign Implementer - Codex port\` — a sibling folder alongside this project, with its own QUEUE.md/SPEC.md/LOG) survives as read-only history. Read it only if you ever need to check what an old Codex-side slug meant — never to build, sync, or reconcile against it. If the port is ever revived, this section gets rewritten to describe a live relationship again; until then, treat Codex as archived.

## E2E testing

**Taskflowapp** at `<TASKFLOWAPP_ROOT>` (its folder on your machine; on this machine it sits under `Taskflow Planning\Planning in here\Taskflowapp`) is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

### Reading session transcripts

Self-hosting and E2E testing increasingly evaluate Claude's behaviour from the raw session transcript. How to get and read one:

1. **Source the raw transcript** from `.claude/projects/<project-slug>/*.jsonl` — the authoritative, unedited record of the session. Read that file rather than asking Claude to regenerate or recall the conversation: a regenerated transcript is a lossy reconstruction, and it hits the handoff-provenance problem (Claude-authored content read as fact rather than as the user's own words).
2. **When the .jsonl is large enough to swamp context, preprocess it.** Run a short Python pass that strips the file to just the conversation text — drop the tool_use / tool_result blocks, the thinking, and metadata — write a slim file, then read that.

The why, weighed against the alternatives: reading the raw file in chunks does NOT save context (the same bytes accumulate across turns); a subagent keeps Claude's context clean but adds a reconstruction layer one step from the evidence; preprocess-then-read keeps Claude on the primary evidence at moderate cost; a targeted grep is lighter still but risks missing findings phrased without the search term. Applies both to the consumer E2E project (Taskflowapp) and to goal/dev sessions here.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

## Model

Model: Opus 5

The model this project mostly runs. `session_start.py` uses it to choose which docset a session loads, layered under the payload's `model` field where that arrives — which, in the desktop app, it doesn't. Before this field existed the choice was made from that field alone, so docset B was inert here despite being fully built. Change it by saying so.

**Claude cannot read its own context level in the desktop app, by any route.** The status line was the only one, and the desktop app **silently ignores the `statusLine` setting** — reported as `anthropics/claude-code#41456`. [statusline-context-reader] was built as a probe against exactly this and deleted on its own pre-agreed condition once the setting was found to be ignored, taking the probe and the setting with it.

This lives here rather than only in the LOG because the question has already come back twice: once as that item, and again when the editor-switch route was considered partly for this reason and then closed (the desktop app is the platform — SPEC.md, Who it's for). So any design reaching for context-awareness — a compaction guard, a size-the-run heuristic, a "context is filling" warning — has no input to read and must not be built as though it might. The one available signal is the user's own report that a session is degrading, which the behaviour rules already treat as the trigger for offering a fresh-session handoff.

## Repo visibility

Repo visibility: public — verified 2026-08-06 via `gh api` and `gh repo view` against `FlintcraftTech/throughliner`, and re-confirmed as a deliberate choice.

**The project's GitHub identity changed outside the method on 2026-08-06, and these are the current values.** The repo is `FlintcraftTech/throughliner` (public), owned by an organisation. The user's own login is now `its-coughfee`, numeric id `283077209` — the old username was given up to create an organisation holding that name. The local remote was repointed at the user's instruction and verified reachable, so this working tree no longer depends on GitHub's redirect from the old path; everyone else's clone still does, and nobody has verified what that redirect does now the old username belongs to an organisation. **Check that rather than assuming it.**

Two consequences worth keeping here. The plugin's own identity is deliberately unchanged — plugin name `sovereign-implementer`, marketplace id `flintcraft`, install target `sovereign-implementer@flintcraft` — so the install instructions read slightly oddly (add a marketplace at `throughliner`, install something called `sovereign-implementer`) and that is correct rather than broken; renaming the product is [rename-to-throughliner]'s job. And [history-rewrite-third-party-scrub] requires setting `git config user.email` to the account's GitHub no-reply address *before* the rewrite, or the next commit reintroduces what the rewrite removed — on today's values that is `283077209+its-coughfee@users.noreply.github.com`, but re-derive it with `gh api user` at build time, since the id isn't guessable and the login has changed once already.

This is a safety input, not a preference. Everything committed to this repo — LOG entries included — is readable by anyone, permanently, and deleting text later does not remove it from git history. It is what makes the never-write-other-people's-private-details rule urgent here rather than theoretical. Re-check it rather than trusting this line if anything depends on it.

## External communication

Announcements about the method go to the project's Discord server — https://discord.gg/Z7ftKnSjR — currently five people, one of whom is a programmer. Write for that reader: plain English, but no pandering to novices.

Announcement text is recorded **in full** in the session's LOG entry. There is no pointer to link to, because Discord posts aren't addressable from here, and the full text is what lets a later session draw on them — release notes in particular. They are not duplicated as repo docs or a changelog; the LOG is the single home for them, and the LOG already serves as this project's decision record.

The invite link above is deliberately public. Alex was told plainly that committing a working invite to a repo that may be public lets any reader join, and chose to proceed on the grounds that anyone who finds this repo is welcome by that fact alone.

## Current state

**Status:** Target v1.17.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — two sections. **Processed** holds work discussed and agreed, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** holds captures — ideas, discoveries, and tasks not yet weighed — that the next /plan processes. A work item is a `#### ` heading (its one-line description) with a `[slug]` at the end of that heading line and its rationale as prose beneath; the block also carries a provenance label ("captured by you" / "by Claude"). A leading `[audit]` or `[user]` tag names how the item is executed; no tag means a build. A work item carrying a security or privacy risk gets a `Red flag · State: <cleared | uncleared>` marker on its own line in that block — the flag rides the work, not a separate section. Deferred verification for shipped work is not a separate section either: it lives as a `[user]` work item (below the cleared-to-run marker while it waits on something), revisited each session by plan.md Step 1's below-line revisit, which reads each item's prose lift-condition and proposes lifting when it clears. Host-side liveness is resolved by content stamp, not version: the session-start hook surfaces the installed host's build stamp (a content hash of the installed plugin's files), and /plan compares it against the target's current stamp (the same `content_stamp()` run over `plugin/si-plugin/`) — a match means host-side changes are live, with no asking the user. The readiness marker is the **only** in-queue halt marker. Its two former siblings are both retired: the push marker (see Self-hosting dependency ordering) and, as of 2026-08-07, the `--- Plan session here: <reason> ---` planning gate. That second one was described as live here, in the shipped FAQ, and in a lint comment — and was implemented in no procedure doc in **either** docset, so it was never a gate at all, only a claim that one existed. Exactly the push marker's shape, and killed for the same reason: a gate maintained in several places and honoured in none is worse than no gate. Work needing a planning pass before it runs sits below the readiness line, which is the boundary the method actually maintains, tests, and surfaces at every close. The honest cost: the readiness line marks *where* the boundary is and carries no *reason*, so we lose the ability to say why a particular point in the queue needs planning attention — judged worth it, since a reason nothing acts on is a comment, and an item's own prose already carries the reasons for the work it belongs to.
- **LOG/** — per-session records of what was built, tested, and decided. `LOG/index.md` for summaries (newest first), each full entry as its own file named on its index line. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`, findable by hash.
- **resources/method-compliance-audit-checklist.md** — the standing criteria for a routine, corpus-wide compliance audit of the method's procedure docs: three lenses — 4.8 authoring-compliance (by reference to the 4.8 section of `resources/authoring-heuristic.md`), response-shape tag placement, and narration drift. Distinct from the authoring heuristic's per-text-at-authoring use: this is the periodic sweep of already-shipped docs. Host-only dev artifact (not shipped in the plugin package). A future /plan scoping a compliance audit reuses this rather than re-deriving the criteria.

## Workflow

- `/setup` — initial project scaffolding (already done).
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build, test, or audit).
- `/done` — close the session, record what happened, commit.

## Rules for Claude

- SPEC.md is a normal doc any batch can edit — the spec-edit batch type is retired. A SPEC change decided in /plan is edited in that same /plan session; a build that discovers it needs a SPEC change asks the user, adds SPEC.md to its Files, and edits it inline; a large SPEC rework is a normal build batch that lists SPEC.md. The scope-lock still denies SPEC unless the active batch lists it in Files, so a build can't touch SPEC silently. Drift is prevented by two close-out spec-sync gates (done-plan.md at the /plan close, done-build.md at the /done-build close): a session can't close with SPEC behind the decision that changed it — the SDD same-commit atomicity the gates protect is why they replace the old batch.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Design for fresh, short sessions. The system must work for a fresh, short session that carries none of a prior session's memory: the files (SPEC, QUEUE, LOG, _build.md) must suffice on their own, and conversation memory is a convenience, never a dependency. Short sessions on the weaker post-Fable development model (from ~2026-06-20) are the design target — and every consumer is already in this case. A long session that remembers everything is the exception, never the case to design for. (This is about robustness to session-memory loss; it does not change the Model target above — 4.8 stays the model the plugin is tuned for.)
- Route discoveries to QUEUE.md rather than acting on them immediately.
- All use of the plugin to develop the plugin is testing the plugin. Any observation of Claude's behaviour — wrong, unexpected, or improvable — is a testing outcome and must be routed to Captures, not discussed and dropped. In particular: any moment you notice session memory covering for something the docs or files should carry — a step that worked only because you remembered the conversation — is itself a mandatory capture. That gap stops hurting under a model with strong session memory, so it stops being found, while fresh short sessions and consumers still hit it.
- Memory boundaries — what memory must never hold, and what it's free for. Memory must never hold the project's records, because the system docs own them: behaviour observations and testing outcomes (Captures), design decisions and their reasoning (QUEUE, SPEC, LOG), project state and constraints (the method docs), and procedure gaps noticed mid-session (Captures). The why: memory doesn't travel with the project and you can't read it, so a project record saved there is a record the project has lost. Memory is free — and a good home — for everything no project doc owns: user preferences, working style, communication feedback, cross-project facts. The old blanket "not to memory" was both too strong (it read as forbidding memory outright) and too weak (it named nothing to check against); this is the boundary that replaces it.
