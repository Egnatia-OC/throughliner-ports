# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## The two-section redesign is merged in — this is main

The `queue-redesign` fork has been merged back into `main` (see LOG `execute-merge-to-main.md`). Main now carries the full two-section work-line model — Processed / Unprocessed, build/audit flavors with `[user]` walk-through, red flags as tagged state-carrying lines — with main's original plugin identity kept (`sovereign-implementer` / `flintcraft`, not the fork's `-x` rename). The reconciliation started from main's drained `QUEUE.md` and folded forward the still-relevant fork items by judgment; the fork's bloat and shipped work were left in git history. The founding decision and reasoning are in QUEUE.md's history under `[adopt-queue-redesign]` and LOG `fable-goal-queue-drain-adopt.md`.

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
      docs/              — procedure docs loaded by skills
    si-plugin.zip        — current installable zip
    zip-archive/         — versioned archive of past zips
  SPEC.md                — this project's spec (once /setup has run)
  QUEUE.md               — this project's work queue
  LOG/                   — this project's session logs (index.md + per-entry files)
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `<PROJECT_ROOT>\plugin\si-plugin\...` — substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on your machine.
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Cross-doc references go by name.** When editing the docs under `plugin/si-plugin/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a batch adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Author method text 4.8-shaped.** Every self-hosting build batch and spec-writing batch is run against the 4.8 section of [`resources/authoring-heuristic.md`](resources/authoring-heuristic.md) before its authored text ships — the short checklist distilling what Opus 4.8 (this project's model target) actually steers on. That doc is also the home for rule-writing rules (the model-agnostic "Rules about writing rules" section — e.g. when a slipped rule earns a hook vs. just sharper wording), so reach for it both when authoring text and when deciding how to fix a rule that slipped. Self-hosting scope: the doc is host-only and not in the plugin package, so the check stays in this project. Revisit shipping the check if the doc ever ships into the package.
- **FAQ entries are part of batch authoring.** When /plan authors a batch that introduces something a consumer would see or ask about — a new queue line, a new doc section, a new narration moment — the batch carries a `plugin/si-plugin/templates/faq-template.md` entry (plus its `faq-index-template.md` index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer? If yes, the FAQ entry ships with the batch. Host-project rule, not shipped plan.md — consumers never author FAQ entries, so the rule would misfire in their /plan sessions.
- **README feature-list sync rides the SPEC-sync trigger.** A change that adds or removes a user-facing feature — a skill, a mode, a command, or user-visible hook behaviour — already must update SPEC.md. That same moment also syncs README.md's "What it does" feature list, which is the plain-English mirror of SPEC's feature list. One more clause on the existing trigger, not a new detection point. Host-only concern: consumers don't maintain the method's README.
- **FAQ-sync rides the SPEC-sync close trigger too, as a host-only backstop.** The batch-authoring FAQ rule above fires at authoring time, but it doesn't reliably catch every case, so the method's own shipped FAQ drifts behind the skills. Fix: the same close that syncs SPEC (and README) for a user-facing change also confirms the FAQ entry that change should ship was actually written. One more clause on the existing SPEC-sync close trigger — same read moment, near-zero cost — not a new standalone gate, which read as too expensive. It backstops the author-time rule at the one close that always runs. Host-only, exactly like the two rules above: keeping the *method's* FAQ current is the developer's job, and consumers never author the method FAQ — so this clause lives here in CLAUDE.md, not in the shipped done-plan.md / done-build.md. When it fires and reports to the user, keep the narration considered: brief, plain-language, lead with the decision, never process-noise about the check itself. Say "This change needs an FAQ entry that isn't there yet — I'll write it before we close." — not a recital of what was scanned.
- **A new batch type touches four places.** Adding a batch type (beyond Build / Test / Audit / Freeform) must wire all four, or it ships half-working: `plugin/si-plugin/docs/next.md` (execution routing), `plugin/si-plugin/docs/done.md` (close routing), `plugin/si-plugin/hooks/post_tool_use.py`'s `ALLOWED_SUBHEADINGS` (the queue lint), and `plugin/si-plugin/docs/plan.md`'s Step 3 batch structure. The now-retired spec-edit batch type was caught half-wired once — it omitted next.md's router — and a later session had to finish it; the type is gone, but the half-wiring lesson is exactly why this rule exists. Host-only concern: consumers never author batch types, so this stays in this CLAUDE.md, not in shipped plan.md.
- **A hook-enforced-format change traces its ripple by grep.** When a work item changes a format or enum the hooks enforce — a marker format, a state value, a section heading the lint parses, a work-item shape — its scope is traced by **grepping the format's literal values across the repo**, not written from the design discussion. The grep must name the enforcing hook AND every doc, template, and FAQ entry that names the values, so the file list is complete before the build starts. The why, from a real miss: the red-flag-states change (`State: cleared`/`uncleared`) was scoped from discussion and missed `post_tool_use.py`'s valid-state set — which would have rejected every new marker — plus done-family docs, setup.md, CLAUDE-TEMPLATE.md, and two FAQ entries; /next's self-scoping caught it only by halting mid-run, the interruption an unattended run shouldn't need. Same family as "A new batch type touches four places": plan-time tracing shrinks the ripples /next must catch, and when it still catches one it captures rather than blocks (see the discovery-vs-underspecification rule in next.md Step 2.2). Host-only: consumers don't author hook-enforced formats, so this stays in this CLAUDE.md, not shipped plan.md.
- **Old plugin history** is on GitHub (`FlintCraftTech/sovereign-implementer`, pre-rebuild commits). Not in this folder.

### Self-hosting dependency ordering

Batch ordering in QUEUE.md implicitly assumes the next batch sees the previous batch's effects. That's true for **target-side** changes — edits to files under `plugin/si-plugin/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks (`hooks/session_start.py`, `hooks/pre_tool_use.py`), the loaded skill procedure docs (`docs/setup.md`, `plan.md`, and the `next*.md` / `done*.md` families), and `docs/plugin-behaviour.md` — which only refresh after a reinstall (a rezip, or the reinstall step of a release). A routine push changes nothing the host sees.

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
2. **Git worktree.** This is the `queue-redesign` worktree, so a move severs the worktree link both ways and git reports "not a repository" until both sides are repointed: this worktree's `.git` file (the `gitdir:` pointer) and the main repo's `worktrees/<name>/gitdir` back-reference.

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

## Editor

Editor: Zettel — the `.md` editor Alex works in. This is the editor field the view-in-doc treatment reads (plan.md's capture quotes, next.md's top-batch quote): because it's recorded, those quotes render as a pointer + link to the doc rather than a re-pasted block. A project with no editor recorded degrades to the inline quote.

Working mode: local — governs how doc-bound text is surfaced (plugin-behaviour.md Working mode and view-in-doc rendering). `local` = Alex is at the desktop, so doc-resident text renders as a pointer/link where an editor is recorded; `remote` = she's driving from her phone, so it's pasted inline. Persistent default set here, not asked each session; flip it for one session with a word. This field replaces the temporary "ask remote or local every session" section that used to sit near the top of this file.

## Model

Model: Opus 5

The model this project mostly runs. `session_start.py` uses it to choose which docset a session loads, layered under the payload's `model` field where that arrives — which, in the desktop app, it doesn't. Before this field existed the choice was made from that field alone, so docset B was inert here despite being fully built. Change it by saying so.

## Repo visibility

Repo visibility: public — verified 2026-08-03 via `gh repo view` against `FlintCraftTech/sovereign-implementer`, and re-confirmed as a deliberate choice.

This is a safety input, not a preference. Everything committed to this repo — LOG entries included — is readable by anyone, permanently, and deleting text later does not remove it from git history. It is what makes the never-write-other-people's-private-details rule urgent here rather than theoretical. Re-check it rather than trusting this line if anything depends on it.

## External communication

Announcements about the method go to the project's Discord server — https://discord.gg/Z7ftKnSjR — currently five people, one of whom is a programmer. Write for that reader: plain English, but no pandering to novices.

Announcement text is recorded **in full** in the session's LOG entry. There is no pointer to link to, because Discord posts aren't addressable from here, and the full text is what lets a later session draw on them — release notes in particular. They are not duplicated as repo docs or a changelog; the LOG is the single home for them, and the LOG already serves as this project's decision record.

The invite link above is deliberately public. Alex was told plainly that committing a working invite to a repo that may be public lets any reader join, and chose to proceed on the grounds that anyone who finds this repo is welcome by that fact alone.

## Current state

**Status:** Target v1.16.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — two sections. **Processed** holds work discussed and agreed, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** holds captures — ideas, discoveries, and tasks not yet weighed — that the next /plan processes. A work item is a `#### ` heading (its one-line description) with a `[slug]` at the end of that heading line and its rationale as prose beneath; the block also carries a provenance label ("captured by you" / "by Claude"). A leading `[audit]` or `[user]` tag names how the item is executed; no tag means a build. A work item carrying a security or privacy risk gets a `Red flag · State: <cleared | uncleared>` marker on its own line in that block — the flag rides the work, not a separate section. Deferred verification for shipped work is not a separate section either: it lives as a `[user]` work line (below the cleared-to-run marker while it waits on something), revisited each session by plan.md Step 1's below-line revisit, which reads each item's prose lift-condition and proposes lifting when it clears. Host-side liveness is resolved by content stamp, not version: the session-start hook surfaces the installed host's build stamp (a content hash of the installed plugin's files), and /plan compares it against the target's current stamp (the same `content_stamp()` run over `plugin/si-plugin/`) — a match means host-side changes are live, with no asking the user. A `--- Plan session here: <reason> ---` marker between items is a planning gate: /next halts there until a /plan session addresses the named reason. It is now the only in-queue halt marker — the push marker that was once its sibling is retired (see Self-hosting dependency ordering).
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
