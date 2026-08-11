# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## The two-section model is what main runs

Main carries the two-section work-line model — Processed / Unprocessed, build and `[audit]` flavors with `[user]` walk-through and `[freeform]` for work /next must not run, red flags as tagged state-carrying lines. It arrived by merging the `queue-redesign` fork (LOG `execute-merge-to-main.md`), keeping main's plugin identity (`sovereign-implementer` / `flintcraft`); the founding decision is in QUEUE.md's history under `[adopt-queue-redesign]` and LOG `fable-goal-queue-drain-adopt.md`. The rollout that section used to describe as pending is done: the merged plugin has shipped, been released, and is what the other projects run.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Audience

The plugin's users are external non-coders building their own apps with Claude Code — not the person developing the plugin. This project is the unusual case: the developer (Alex) is also a non-coder using the plugin to build the plugin. Skill docs must be written for the external user, not for Alex.

Concretely: anything a skill causes Claude to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "plugin-behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where Claude reads them; they must not leak into output the user sees.

When editing any skill doc, check the output-facing strings against this audience before saving.

## Model target

**The method runs on one docset, and no model detection.** `plugin/si-plugin/docs-b/` is it. There is nothing to pick between, so nothing picks: session_start carries no docset logic and no model logic, and the skills point straight at `docs-b/`.

The docset serves the **5-series — Fable 5 and Opus 5** — which converge on wanting less prescription rather than more. It was authored by *subtraction* from the older, heavier docset A, and it is lighter for that reason: A over-explained because Opus 4.8 needed a rule's why to travel with it to follow the rule reliably, and the 5-series does not.

**Docset A is retired (2026-08-09), and 4.8 is no longer a supported target.** The two-docset design existed for one reason — a no-strand guarantee, so a bad migration to the new docset could never leave the project with no working plugin. That reason expired when both 5-series models proved out on B. A was retired once already on 2026-08-08; the emergency revert of 2026-08-09 brought it back, and this build re-applies the decision rather than making a new one. Its 4.8 steering research stays on file as history, not as a live target: `resources/research/opus-4-8-verbosity-steering.md`, `resources/research/model-instruction-compliance.md`.

**Why one docset and not N — the fork this closes for good.** The intuitive worry was one docset per model, which drifts under dual maintenance. It never got that far, because Opus 5 is not "as fussy as 4.8" — it is fussy the *opposite* way: it over-does (self-verifies, expands scope, runs verbose), so Anthropic's guidance for it is *subtraction*, and Fable 5 wants the same. Both 5-series models therefore converge on one lighter docset. With A gone the sync burden is not merely dodged but absent. Research: `resources/research/opus-5-instruction-compliance.md`, `fable-5-instruction-compatibility.md`.

**Authoring register.** Author by subtraction, in docs-b's lighter register. A future model is adopted when it arrives; the retired docset is history, not somewhere to regress to — we do not reach for an older model or an older register to dodge a newer model's behaviour.

**The `docset: B` frontmatter stamp stays** on each `docs-b/` file. Its original job — proving a session opened B rather than A — is vestigial with one docset, but session_start's behaviour-rules redirect self-checks against it, so it has a live consumer. Removing it would be churn.

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only a `claude` CLI install/update against the committed marketplace plus a full app restart does (the desktop app's in-app plugin upload is gone; the exact commands are in the Push section below and in `resources/release-ritual.md`). A bare working-tree or zip edit changes nothing the host sees, because the host runs a frozen snapshot the CLI copied into `~/.claude/plugins/cache/...` at install time, not the live files.
**Target** = the editable source at `plugin/si-plugin/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**3 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — two sections (Processed / Unprocessed), each holding work lines as `#### ` headings with rationale beneath. A work line that carries a security or privacy risk gets a red-flag marker (a `Red flag · State:` tag) — the flag rides the work, not the other way around.
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`.

**4 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top ready work, execute it (build or audit), walk the user through `[user]` lines. Works the cleared region top-down, so one invocation can build several cleared lines back-to-back — the unattended-in-practice runner, closed by /done.
- `/done` — record what happened, clean up, commit.

**3 hooks** — two enforcing, one advisory:
- `session_start` (enforcing) — detect project state (unadopted / adopted / active build), load behaviour rules, check plugin version against .si-version.
- `pre_tool_use` (enforcing) — scope-lock to the active batch's file list (which governs SPEC.md like any other file — SPEC is editable only by a batch that lists it), git safety.
- `post_tool_use` (advisory) — QUEUE.md structure lint; flags format drift after a QUEUE.md edit, never blocks.

## Where things live

```
No code method/
  CLAUDE.md              — this file
  .gitignore
  plugin/                — plugin packaging
    si-plugin/           — target source
      .claude-plugin/    — plugin manifest
      hooks/             — session_start, pre_tool_use, post_tool_use
      skills/            — setup, plan, next, done
      templates/         — CLAUDE-TEMPLATE.md
      docs-b/            — procedure docs loaded by skills (the one docset)
    si-plugin.zip        — current installable zip
    zip-archive/         — versioned archive of past zips
  SPEC.md                — this project's spec (once /setup has run)
  QUEUE.md               — this project's work queue
  LOG/                   — this project's session logs (index.md + per-entry files)
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `<PROJECT_ROOT>\plugin\si-plugin\...` — substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on your machine.
- **Cross-doc references go by name.** When editing the docs under `plugin/si-plugin/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a batch adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Run [`resources/self-authoring-rules.md`](resources/self-authoring-rules.md) before adding any rule to the method's own text.** It is the admission-and-eviction gate: four parts in use order — does this rule get to exist, what comes out to make room, always-loaded or fetched, and how it's worded. It also settles where a rule's reasoning goes (out of the operative statement, into the LOG entry that decided it — and where a reason is genuinely needed to apply the rule, into the rule itself as operative text). Reach for it both when authoring text and when deciding how to fix a rule that slipped — the hook-versus-sharper-wording judgment is admission test 4. It replaces the retired `authoring-heuristic.md`, which was in force for the whole period the old behaviour doc grew from 6,162 to 21,445 words: it had no admission control and no eviction policy, so every addition passed it honestly. Host-only — not in the plugin package, and consumers never author method rules.
- **FAQ entries are part of batch authoring.** When /plan authors a batch that introduces something a consumer would see or ask about — a new queue line, a new doc section, a new narration moment — the batch carries a `plugin/si-plugin/templates/faq-template.md` entry (plus its `faq-index-template.md` index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer? If yes, the FAQ entry ships with the batch. Host-project rule, not shipped plan.md — consumers never author FAQ entries, so the rule would misfire in their /plan sessions.
- **README feature-list sync rides the SPEC-sync trigger.** A change that adds or removes a user-facing feature — a skill, a mode, a command, or user-visible hook behaviour — already must update SPEC.md. That same moment also syncs README.md's "What it does" feature list, which is the plain-English mirror of SPEC's feature list. One more clause on the existing trigger, not a new detection point. Host-only concern: consumers don't maintain the method's README.
- **FAQ-sync is a hard close gate with a logged disposition — a session carrying a user-facing change cannot close until the FAQ is dispositioned.** It rides the SPEC-sync close trigger's read moment, and it has the same teeth SPEC-sync has: the close does not complete until it is satisfied.

  **The disposition is written into the LOG entry, as an explicit line:**

  ```
  FAQ: updated <entry title>
  FAQ: not needed because <reason>
  ```

  **The required artifact is the whole point.** This clause used to be a soft "confirm the FAQ entry was written" self-check, and it failed on its first real test — `ea272f6` synced SPEC and not the FAQ, exactly the case it was added for. A self-check with no output is indistinguishable from a self-check that was skipped, so skipping it cost nothing and left no trace. Requiring a line in the LOG converts a silent omission into a visible, auditable one: "not needed because X" is a claim someone can later read and disagree with, and a missing line is a gap anyone can see. That difference is the entire fix — it is why SPEC-sync works and why the soft version did not.

  **Not a hook, deliberately.** "Is this change user-facing?" is not mechanically detectable the way QUEUE.md's structure is, so a hook would either miss real cases or fire on false ones, and a gate that cries wolf gets worked around. The gate rides a read that already happens, at the one close that always runs.

  **Host-only by residence**, exactly like the two rules above: it lives in this CLAUDE.md, which consumer projects don't carry, so it never fires for consumers — who don't maintain the method's FAQ and would be baffled by the obligation. That is why it is here rather than in the shipped done-plan.md / done-build.md.

  **Narration stays plain.** Lead with the decision, no process-noise about the check itself: "This change needs an FAQ entry that isn't there yet — I'll write it before we close." Not a recital of what was scanned.
- **A build that changes the document format bumps the format epoch.** `FORMAT_EPOCH` near the top of `plugin/si-plugin/hooks/session_start.py` declares the shape the method expects a project's own documents to be in. Bump it whenever a build makes an *existing* project's files structurally wrong — a new section, a renamed heading the hooks parse, a field that becomes required, a work-item shape change. Do **not** bump it for anything an old project's files survive unchanged; the epoch's whole value is that it doesn't cry wolf the way the version number would. Sibling to the README-sync and SPEC-sync triggers, and load-bearing in the same way: without the bump, session_start's migration halt never fires and every consumer project silently keeps running on the old shape. Also add a line to the epoch history comment saying what the new number means — a bare number nobody can date is a number nobody dares change. Host-only: consumers never author formats.
- **A new work-item flavor must be wired everywhere it is read, or it ships half-working.** Flavors today are build (no tag), `[audit]`, `[user]` and `[freeform]`. Adding one means: `plugin/si-plugin/docs-b/plan.md` (how it is marked and placed at the keep-step), `next.md` (execution routing — build it, walk it, or halt on it), and `done.md` (close routing, and whether the close must announce it). The queue lint in `post_tool_use.py` is **not** a fourth site: it validates slug, red-flag state and `Blocked by:`, and holds no list of valid flavors, so a new tag needs nothing from it — verified when `[freeform]` was added. Check that rather than assuming it either way. The rule exists because the retired spec-edit type was caught half-wired once, omitting next.md's router, and a later session had to finish it. Host-only concern: consumers never author flavors, so this stays in this CLAUDE.md, not in shipped plan.md.
- **A hook-enforced-format change traces its ripple by grep.** When a work item changes a format or enum the hooks enforce — a marker format, a state value, a section heading the lint parses, a work-item shape — its scope is traced by **grepping the format's literal values across the repo**, not written from the design discussion. The grep must name the enforcing hook AND every doc, template, and FAQ entry that names the values, so the file list is complete before the build starts. The why, from a real miss: the red-flag-states change (`State: cleared`/`uncleared`) was scoped from discussion and missed `post_tool_use.py`'s valid-state set — which would have rejected every new marker — plus done-family docs, setup.md, CLAUDE-TEMPLATE.md, and two FAQ entries; /next's self-scoping caught it only by halting mid-run, the interruption an unattended run shouldn't need. Same family as "A new batch type touches four places": plan-time tracing shrinks the ripples /next must catch, and when it still catches one it captures rather than blocks (see the discovery-vs-underspecification rule in next.md Step 2.2). Host-only: consumers don't author hook-enforced formats, so this stays in this CLAUDE.md, not shipped plan.md.
- **Old plugin history.** The plugin was rebuilt from scratch on 2026-06-01, and both this folder and the GitHub repo (`FlintcraftTech/throughliner`) start there — the remote is not a pre-rebuild archive. Some pre-rebuild history does survive locally, as the `v17`–`v157` orphan tags, which are not ancestors of HEAD. Anything earlier than that, if it exists at all, would be on Alex's old machine. Don't send a session chasing pre-rebuild commits on GitHub; there are none.

### Self-hosting dependency ordering

Work ordering in QUEUE.md implicitly assumes the next item sees the previous item's effects. That's true for **target-side** changes — edits to files under `plugin/si-plugin/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks, the loaded skill procedure docs (`docs-b/setup.md`, `plan.md`, `skill-nonspecific-rules.md`, and the `next*.md` / `done*.md` families) — which only refresh after a rezip or release plus a full app restart.

When an item depends on a previous item's host-side effects, that dependency does not resolve in-session. /plan holds it below the cleared-to-run line with `Blocked by: [slug]` naming the item it waits on, and says in its prose that the dependency is host-side.

**The old `--- Push required before continuing ---` and `--- Plan session here: … ---` markers are gone.** `docs-b/next.md`'s pre-flight states it plainly: there is no blocker gate, no push marker and no unpark scan — those belonged to the earlier model. Don't write either marker into QUEUE.md, and don't expect /next to halt on one. What replaced them: readiness is settled at /plan before work reaches the cleared region, host-side liveness is read from the installed build's content stamp rather than asserted by a marker, and a genuine dependency is carried by the `Blocked by:` field, which survives a reorder where a positional marker does not.

One thing the old marker's note said is worth keeping, because it was misread repeatedly: a decided-but-unshipped rule is **in force from the moment it is decided**. In-repo sessions read the queue and the discussion, not just the installed plugin. "Not shipped yet" is never a reason to suspend decided reasoning.

## Rezip (local testing), Push (routine), and Release (on request)

**Three separate actions, and the words mean what they say.** "Push" once meant the full release ritual, so a push and a release were one event; they were decoupled on 2026-08-04 and stay decoupled.

- **Rezip** refreshes the installed host from the local `plugin/si-plugin` folder so Alex can dogfood the plugin privately. Never publishes, never releases, touches no remote. It builds no zip — the local marketplace sources the folder and the CLI snapshots it directly. **A rezip runs before the push, not after it.**
- **Push** is `git push`, preceded by one small piece of housekeeping: it resets `plugin.json` to a clean version, dropping any `-testN` suffix the rezip left. Routine and cheap — it runs after every /next and at any /done, with no consistency sweep, no zip and no GitHub Release. It needs no confirmation, so don't ask for one.
- **Release** publishes a version: the release bump, the consistency sweep, the repackage, the GitHub pre-release and the host reinstall. **It runs when Alex asks for it, and at no other time.**

**Releases are on request (Alex's decision, 2026-08-09, corrected twice in her own words).** There is no automatic trigger and no release-due file check. Don't run a release because a session's commits touched `plugin/si-plugin/`, and don't run one because Alex asked to rezip or to push. Wait to be asked.

**What this supersedes, recorded so it isn't re-derived.** From 2026-08-04 to 2026-08-09 the release fired automatically at any /done whose commits touched the plugin, and this document explicitly barred asking whether a release was warranted. The reasoning behind that was sound and is not being called wrong: welding release to push had made every routine save ask "is this good enough to publish?" — a question with no honest answer on a project that will never feel finished — so releases stopped happening and the work stayed invisible. It is outweighed rather than refuted. An automatic publish that Alex has to interrupt is a worse failure than a release that waits to be asked for, and she has now stopped one twice.

**The intuitive middle option is already rejected — don't propose it.** Keeping the trigger automatic but pausing once before publishing ("about to publish v1.21.0, go ahead?") looks like a compromise and is not one: that pause *is* the readiness question, and it is the exact moment Alex stopped. If a later session feels the pull toward it, this paragraph is the answer.

**Every release is marked pre-release, and that is the honest label.** The plugin is in active testing and is not ready for the Claude marketplace. GitHub's pre-release flag states that structurally, so it never has to be re-decided or re-worded release by release, and a release is never a claim that the plugin is finished.

**A release only ever runs on `main`.** Check the branch first — `git rev-parse --abbrev-ref HEAD`. Releasing from a branch would publish unmerged work and fork the version line, so if Alex asks for a release from somewhere else, say so and stop.

Do whichever Alex actually asked for.

### Rezip and Release live in a fetched doc

Their full step-by-step is [`resources/release-ritual.md`](resources/release-ritual.md) — open it when Alex says "rezip" or "release", and not before. It also carries the project-folder-move recovery. Both rituals fire only on an explicit word from Alex, which is exactly the shape that can be fetched; keeping their ~25 steps always-loaded spent about a third of this file's instruction budget on text that never fires unprompted.

**Push stays here, deliberately**, because it runs after every /next and at any /done — a standing condition Claude has to notice, not a word Alex says. A rule that must fire unprompted cannot be fetched.

### Push (routine)

Two steps: clean the version, then `git push`. It runs when Alex says "push", after every /next, and at any /done — no sweep, no zip, no GitHub Release, and **no confirmation needed**. Never `--force`. Stage explicitly, as the file-safety rules require; never `git add -A`.

1. **Reset `plugin/si-plugin/.claude-plugin/plugin.json` to a clean version**, dropping any `-testN` suffix a rezip left (`1.20.0-test2` → `1.20.0`). Keep the same release-line number — this is not a release bump, it's removing the test marker. Stage the file with the rest of the work.
2. `git push`.

**Why the clean is part of the push, and what breaks without it.** The rezip now runs *before* the push, so the build Alex actually exercised is the build the commit carries — that ordering is the point. But it means the working tree reaches the push holding a `-testN` version, and a `-testN` version reaching the remote is the exact failure this design inherits: it happened once, when a session silenced the recurring dirty `plugin.json` by committing it, and the public repo advertised its version as `1.16.0-test4` until the next release. Cleaning at the push closes that window to a single session, so a test suffix is never on the remote and never in a release.

**A consequence worth stating, since it removes a standing annoyance rather than creating one.** `plugin.json` no longer sits dirty across sessions waiting for a release bump to tidy it; it is dirty only between a rezip and that same session's push. So there is no recurring close-time noise to carve out, and no close-time exception is needed in the shipped /done docs — which is right anyway, since those ship to consumers who never rezip.

Pushing often is the point: it decouples "the work is safely on the remote" from "I am publishing a version," so the routine action never carries a publishing decision. **No release-due check runs here.** A release happens when Alex asks for one.

## Discord posts

**Announce only what has shipped: every claim in a post is true of the installed plugin at the moment it is posted.** Where a post describes work that is designed but not built, the post waits for the build — file it as a queue item naming what it waits on.

The limit is **2,000 characters**, which is Discord's.

Claude drafts and Alex posts, because Claude has no route to Discord. The draft is shown before it goes and needs an explicit yes: that is the existing rule on anything leaving the machine, and nothing here changes it.


## Handoff-claim provenance

When a session opens from a Claude-authored handoff or context prompt — a resume note, a "here's where we left off" summary — treat its claims as unverified until the user confirms them. Claude-written content is not read in the user's voice. The why: a handoff Claude authored is not a user-vouched fact, and a fresh or weaker session can't tell which claims the user stood behind versus which Claude wrote — so a Claude-authored line ("the lint keeps flagging X") must not be used as evidence that the user reported X. Confirm before relying on it. (Resolved 2026-06-26: no claim-marking format is added — this standing rule suffices. Multi-line /next takes its instructions from the queue, user-vouched by construction, so it never reads a mixed Claude-authored directive whose claims would need marking; the one Claude-authored thing a run reads is its own working-state file (_build.md) on resume, read as mechanical state, exactly what this rule already covers.)

## Cross-platform ports

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

No Editor or Working mode field. Both were retired on 2026-08-09 — the desktop app opens `.md` in its own viewer whatever editor is named, and the location field turned out to record how much text Alex wanted pasted rather than where she was sitting. Doc-resident text now renders as a pointer + link unconditionally; the session's opening narration carries the one-line offer to paste inline instead when she's away from the desktop (skill-nonspecific-rules.md, view-in-doc rendering).

## Current state

**Status:** Target v1.20.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — two sections. **Processed** holds work discussed and agreed, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** holds captures — ideas, discoveries, and tasks not yet weighed — that the next /plan processes. A work item is a `#### ` heading (its one-line description) with a `[slug]` at the end of that heading line and its rationale as prose beneath; the block also carries a provenance label ("captured by you" / "by Claude"). A leading `[audit]`, `[user]` or `[freeform]` tag names how the item is executed; no tag means a build. A work item carrying a security or privacy risk gets a `Red flag · State: <cleared | uncleared>` marker on its own line in that block — the flag rides the work, not a separate section. Deferred verification for shipped work is not a separate section either: it lives as a `[user]` work line (below the cleared-to-run marker while it waits on something), revisited each session by plan.md Step 1's below-line revisit, which reads each item's prose lift-condition and proposes lifting when it clears. Host-side liveness is resolved by content stamp, not version: the session-start hook surfaces the installed host's build stamp (a content hash of the installed plugin's files), and /plan compares it against the target's current stamp (the same `content_stamp()` run over `plugin/si-plugin/`) — a match means host-side changes are live, with no asking the user.- **LOG/** — per-session records of what was built, tested, and decided. `LOG/index.md` for summaries (newest first), each full entry as its own file named on its index line. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`, findable by hash.
- **resources/self-authoring-rules.md** — the admission-and-eviction gate every new method rule passes through, and the home of the rationale-lives-outside-the-operative-rule split. Run at authoring time, per rule.
- **resources/method-compliance-audit-checklist.md** — the standing criteria for a routine, corpus-wide compliance audit of the method's procedure docs: three lenses — self-authoring compliance (by reference to `resources/self-authoring-rules.md`), response-shape tag placement, and narration drift. Distinct from the gate's per-rule-at-authoring use: this is the periodic sweep of already-shipped docs. Host-only dev artifact (not shipped in the plugin package). A future /plan scoping a compliance audit reuses this rather than re-deriving the criteria.

## Workflow

- `/setup` — initial project scaffolding (already done).
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build, test, or audit).
- `/done` — close the session, record what happened, commit.

## Rules for Claude

- SPEC.md is a normal doc any batch can edit — the spec-edit batch type is retired. A SPEC change decided in /plan is edited in that same /plan session; a build that discovers it needs a SPEC change asks the user, adds SPEC.md to its Files, and edits it inline; a large SPEC rework is a normal build batch that lists SPEC.md. The scope-lock still denies SPEC unless the active batch lists it in Files, so a build can't touch SPEC silently. Drift is prevented by two close-out spec-sync gates (done-plan.md at the /plan close, done-build.md at the /done-build close): a session can't close with SPEC behind the decision that changed it — the SDD same-commit atomicity the gates protect is why they replace the old batch.
- Design for fresh, short sessions. The system must work for a fresh, short session that carries none of a prior session's memory: the files (SPEC, QUEUE, LOG, _build.md) must suffice on their own, and conversation memory is a convenience, never a dependency. Short sessions on the weaker post-Fable development model (from ~2026-06-20) are the design target — and every consumer is already in this case. A long session that remembers everything is the exception, never the case to design for. (This is about robustness to session-memory loss; it does not change the Model target above — 4.8 stays the model the plugin is tuned for.)
- All use of the plugin to develop the plugin is testing the plugin. Any observation of Claude's behaviour — wrong, unexpected, or improvable — is a testing outcome and must be routed to Captures, not discussed and dropped. In particular: any moment you notice session memory covering for something the docs or files should carry — a step that worked only because you remembered the conversation — is itself a mandatory capture. That gap stops hurting under a model with strong session memory, so it stops being found, while fresh short sessions and consumers still hit it.
