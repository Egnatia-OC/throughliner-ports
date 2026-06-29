# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Audience

The plugin's users are external non-coders building their own apps with Claude Code — not the person developing the plugin. This project is the unusual case: the developer (Alex) is also a non-coder using the plugin to build the plugin. Skill docs must be written for the external user, not for Alex.

Concretely: anything a skill causes Claude to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "plugin-behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where Claude reads them; they must not leak into output the user sees.

When editing any skill doc, check the output-facing strings against this audience before saving.

## Model target

Resolved 2026-06-15: this project targets **Opus 4.8** and will not regress to 4.6 or 4.7. We do not work around 4.8's behaviour by reaching for an older model — we focus on getting 4.8 right. When 4.8 behaves in a way the plugin doesn't want (verbosity, instruction-following, bundling), the fix is to steer 4.8 with techniques it actually responds to, recorded in `resources/research/opus-4-8-verbosity-steering.md` and `resources/research/model-instruction-compliance.md`, not to downgrade. Future models are adopted when they arrive; older ones are not a fallback.

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only uninstalling and reinstalling does.
**Target** = the editable source at `plugin/si-plugin/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**3 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — red flags (security/privacy/breach risks Claude surfaced, kept at the top, each with an open/resolved/accepted state), work batches (Build/Test/Audit subheadings), and captured ideas (plain bullets).
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`.

**4 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top queue entry, execute it (build, test, or audit).
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

- **Use absolute paths** for sub-folder lookups. `C:\Users\Alex\Desktop\Taskflow Planning\No code method\plugin\si-plugin\...`
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Cross-doc references go by name.** When editing the docs under `plugin/si-plugin/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a batch adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Author method text 4.8-shaped.** Every self-hosting build batch and spec-writing batch is run against the 4.8 section of [`resources/authoring-heuristic.md`](resources/authoring-heuristic.md) before its authored text ships — the short checklist distilling what Opus 4.8 (this project's model target) actually steers on. That doc is also the home for rule-writing rules (the model-agnostic "Rules about writing rules" section — e.g. when a slipped rule earns a hook vs. just sharper wording), so reach for it both when authoring text and when deciding how to fix a rule that slipped. Self-hosting scope: the doc is host-only and not in the plugin package, so the check stays in this project. Revisit shipping the check if the doc ever ships into the package.
- **FAQ entries are part of batch authoring.** When /plan authors a batch that introduces something a consumer would see or ask about — a new queue line, a new doc section, a new narration moment — the batch carries a `plugin/si-plugin/templates/faq-template.md` entry (plus its `faq-index-template.md` index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer? If yes, the FAQ entry ships with the batch. Host-project rule, not shipped plan.md — consumers never author FAQ entries, so the rule would misfire in their /plan sessions.
- **A new batch type touches four places.** Adding a batch type (beyond Build / Test / Audit / Freeform) must wire all four, or it ships half-working: `plugin/si-plugin/docs/next.md` (execution routing), `plugin/si-plugin/docs/done.md` (close routing), `plugin/si-plugin/hooks/post_tool_use.py`'s `ALLOWED_SUBHEADINGS` (the queue lint), and `plugin/si-plugin/docs/plan.md`'s Step 3 batch structure. The now-retired spec-edit batch type was caught half-wired once — it omitted next.md's router — and a later goal session had to finish it; the type is gone, but the half-wiring lesson is exactly why this rule exists. Host-only concern: consumers never author batch types, so this stays in this CLAUDE.md, not in shipped plan.md.
- **Old plugin history** is on GitHub (`FlintCraftTech/sovereign-implementer`, pre-rebuild commits). Not in this folder.

### Self-hosting dependency ordering

Batch ordering in QUEUE.md implicitly assumes the next batch sees the previous batch's effects. That's true for **target-side** changes — edits to files under `plugin/si-plugin/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks (`hooks/session_start.py`, `hooks/pre_tool_use.py`), the loaded skill procedure docs (`docs/setup.md`, `plan.md`, and the `next*.md` / `done*.md` families), and `docs/plugin-behaviour.md` — which only refresh after push + uninstall/reinstall.

When a batch depends on a previous batch's host-side effects, that dependency does not resolve in-session. /plan must place the dependent batch after a push marker and annotate its `Depends on:` line as `(host-side)`.

**Push-marker convention.** A line `--- Push required before continuing ---` between batches in QUEUE.md indicates /next must halt until the user has pushed and reinstalled. /plan inserts the marker when placing a host-side-dependent batch.

The marker is hard in only one direction. It halts /next because batches past it read host-side state — an audit reading injected rules, a live test of hook behaviour — which gives wrong results before push + reinstall; protecting that read is the one hard thing the marker does. It does **not** suspend decided rules or reasoning in any session, and it is not a wall for planning work: in-repo sessions read the queue and the discussion, not just the installed plugin, so decided-but-unshipped standards already shape sessions before any push. Treating the line as a blanket "not shipped yet, so don't apply it" suspends decided reasoning and breaks the why-pipeline. The line marks when we aim to ship by — decided rules and reasoning apply from the moment they're decided.

Worked example:
```
**[capture-parking-discipline]** ...

--- Push required before continuing ---

**[behaviour-agnosticism-audit]**
Depends on: capture-parking-discipline (host-side)
...
```

[behaviour-agnosticism-audit] reads procedure docs against criteria including capture routing rules. Those rules live in plugin-behaviour.md (host-side). Without the push between them, the audit would read the old rules.

## Rezip (local testing) and Push (release)

These are two separate actions. **Rezip** builds a fresh installable zip so Alex can dogfood the plugin privately — it never publishes. **Push** is the full release ritual that publishes to the public remote. The word "push" (said directly, or chosen at a /done close) always means the full release ritual below. "Rezip" is a separate, explicit request and never publishes — bumps no version, makes no commit, touches no remote. Do whichever Alex actually asked for; don't run a push because she asked to rezip.

### Rezip (local testing)

When Alex says "rezip" (or asks for a fresh local build to test), run this — no release version bump, no archive, no commit, no push. (The one version change is the test suffix in step 1; the release version is never bumped here.)

**The `-testN` test-build scheme.** A rezip rebuilds the zip without a release bump, because bumping the release version on every private test build would nag Alex's own projects to re-run /setup each time. But test builds still need to be distinct and unmistakably-test, so each carries a `<base>-testN` version — the release-line base plus `-test` and a number incremented each rezip-for-testing (e.g. `1.12.0-test1`, then `-test2`). Honest framing: the suffix is not what makes a reinstalled host load — the full app restart is (see the relaunch step below). `-testN`'s only job is to keep each test build a distinct, clearly-labeled version that's never mistaken for a release. The suffix lives in the working tree's `plugin.json` only and must be reset to a clean version before any push; the Push step's bump does exactly that (Push step 2), so a test suffix never ships in a release.

1. Bump the test suffix in `plugin/si-plugin/.claude-plugin/plugin.json`: read the current version and increment N (`-test1` → `-test2`), or start at `-test1` if the base carries no suffix (`1.12.0` → `1.12.0-test1`).
2. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never ships in the zip (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
3. Repackage, overwriting the existing zip: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip" -Force` (zip the folder, not its contents — internal paths must start with `si-plugin/`). Verify: list the zip's entries and confirm none contain `__pycache__` — if any do, stop and fix.
4. Tell Alex: "Zip rebuilt — nothing has been published. Uninstall/reinstall to test the new host privately." Note that loading the new host needs a **full app restart, not just a new session** — plugin skills register at app launch, and on Windows a normal quit can leave the app running, so fully quit (confirm the process exited via Task Manager if needed) and relaunch before testing.

### Push (release)

When Alex says "push" (or a push happens as part of /done), run this automatically before pushing — no confirmation needed per step:

1. Backfill any unfilled commit-hash placeholders anywhere in `LOG/` before proceeding. The session-start hook only fires at session start, so a /done that ran earlier in this same session leaves its placeholder unfilled at push time — this step catches it. Same rules as the hook: replace the token only in hash position (an entry heading line or the start of an index line), never in body prose, which may mention the token literally; resolve each to the **oldest** `git log -S "<entry title>"` match, never the newest commit touching the file.
2. Bump version in `plugin/si-plugin/.claude-plugin/plugin.json` to a clean patch/minor — patch for fixes/incremental, minor for new capabilities — and in doing so **drop any `-testN` suffix** the working tree carries from rezip testing (`1.12.0-test3` → `1.12.1` or `1.13.0`), so a test suffix never ships in a release. (The release bump lives here, not in rezip — rezip only ever touches the `-testN` test suffix, never the release line: bumping the release version on every private test build would make Alex's own projects nag "version changed, re-run /setup" each time she tests.)
3. Pre-push consistency sweep — two passes, run in order:

   **Pass A — Gather the feed:** Run `git log --oneline origin/main..HEAD` to list unpushed commits. Read their LOG entries (each session's own file under LOG/) to understand what changed (files touched, features added/removed/renamed, concepts that shifted).

   **Pass B — Check for staleness against those changes:**
   - **Target internal consistency:** Do templates match the procedure docs they ship alongside? Compare FAQ templates and CLAUDE-TEMPLATE.md against current procedure docs (field names, doc structure, workflow descriptions). Update any that fell behind.
   - **Project docs:** Check QUEUE.md, SPEC.md, and LOG/ for references to removed features, renamed fields, or old formats that the unpushed commits changed. Fix any found.
   - **CLAUDE.md:** Check this file's descriptions (Architecture, Method docs, Rules) against current target state. Update any stale references.
4. Archive current zip: `mv plugin/si-plugin.zip plugin/zip-archive/si-plugin-v<OLD_VERSION>.zip`
5. Prune `plugin/zip-archive/` to the three most recent zips (delete oldest).
6. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never ships in the zip (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
7. Repackage: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip"` (zip the folder, not its contents — internal paths must start with `si-plugin/`). Verify: list the zip's entries and confirm none contain `__pycache__` — if any do, stop and fix before pushing.
8. Stage every dirty path in `plugin/si-plugin/` (run `git status --porcelain plugin/si-plugin/` and stage each listed path — catches any sweep edits from step 3), plus the zip in `plugin/`, archive changes in `plugin/zip-archive/`, plugin.json, and the LOG/ changes (including step 1's backfill edits). Commit: "Bump to v<VERSION> and repackage".
9. `git push`.
10. Publish a GitHub Release for the new version, so users who subscribed via Watch → Releases get notified — a plain `git push` does not fire that notification; only a published Release does. Use `gh`:
    - Tag and title = the new version (e.g. `v1.13.0`). Notes = a short summary of what shipped, drawn from this release's LOG entries / commit messages.
    - Attach the zip: `plugin/si-plugin.zip`.
    - Command shape: `gh release create v<VERSION> plugin/si-plugin.zip --title "v<VERSION>" --notes "<summary>"`.
    - If `gh` isn't authenticated in this session (the command errors on auth), don't silently skip the Release — tell Alex how to publish it from the GitHub web UI instead: on the repo's **Releases** page, click **Draft a new release**, create the tag `v<VERSION>`, set the same title, paste the summary as the notes, attach `plugin/si-plugin.zip`, and **Publish release**. The step never silently does nothing.
11. Tell Alex: "Pushed, released, and rezipped. Uninstall/reinstall to update the host."

**Archive accuracy.** Push keeps archiving the previous zip as above. Git history is the authoritative record of released zips — each push commits `si-plugin.zip`. So if a private rezip overwrote `si-plugin.zip` since the last push, the copy that lands in `plugin/zip-archive/` at the next push is a convenience that may reflect a test build rather than the prior release. This is cosmetic: git holds the true releases.

LOG entries are per-entry files — no log capping or push markers at push time. Existing `LOG/log.md` and `LOG/log-v*.md` files stay in place untouched: index references work by hash, so old entries remain findable.

## Goal sessions

A goal session is the developer's autonomous-build workflow: Claude works through several build batches back-to-back in one chat, closed by a manual /done. Cruise control is the consumer-facing version that will grow from it. The shape below is defined — run it this way rather than re-improvising it each time.

**Running it plugin-off — the intended state, and how to actually get there.** A goal session is meant to run with the plugin off, so Claude sequences freely without the scope-lock firing. But disabling a plugin mid-session does NOT stop its hooks: plugin components only re-apply on /reload-plugins or a restart, and an open Claude Code bug has disabled plugins still firing SessionStart hooks. So "plugin off" isn't achievable inside an already-started session — it takes disabling the plugin AND starting a fresh session, which on the desktop app means a full app restart. See `resources/research/plugin-enable-disable-session-lifecycle.md` for the why. Treat plugin-off as the aim, not a guaranteed state.

**Robust to the plugin being left on.** Because off isn't guaranteed, the procedure must hold with the hooks active:
- The aggregate `_build.md` must list every file across all the batches in its `Files:` section, so that if the scope-lock is live it can't deny an edit the run legitimately makes. Write that section as bare bullet paths, with no inline "Files: a, b, c" line sitting above it — the scope-lock parser binds to the first `Files:` it sees, so a shadowing inline line would mis-scope the lock.
- The hand-backfill LOG-hash step at the close is a backstop: if the session-start hook did fire (plugin left on), it already auto-backfilled, so the hand step may correctly find nothing to fill. Run it anyway — finding nothing is a pass, not a miss.

**The run.** Claude works the batches back-to-back in one session, plugin off, owning the sequencing itself and stopping only for what genuinely needs the user. It uses a single aggregate `_build.md` that lists the batches it will work through, kept purely as a working-state and resume record. With the plugin off the scope-lock hook does not fire, so this aggregate `_build.md` is primarily a working-state and resume record — what a resumed session reads to recover where the run was. But list every file across the batches in its `Files:` section regardless (see "Robust to the plugin being left on" above), because if the plugin was left on the lock is live and reads that list.

**The close.** One manual /done closes the whole run:
- It writes a separate LOG entry per batch — one entry file and one index line each — and lands them all in a single end-of-run commit. Per-batch entries keep the history granular and retrievable, matching the one-batch-one-entry norm; the single commit keeps the autonomous run atomic.
- It runs the shipped-slug cross-check in done.md's commit core, so every batch the run shipped is confirmed gone from QUEUE.md's Batches before the commit.
- It runs the deferred-test and staleness sweeps once across all the batches at the close, not once per batch.
- It does the LOG-hash backfill by hand, because if the session ran plugin-off the session-start hook never fired, so its automatic backfill did not run. (If the plugin was left on, the hook may already have backfilled — then this step correctly finds nothing, which is a pass.) Fill any `[HASH]` placeholders in `LOG/` using the Push step's rule — replace the token only in hash position (an entry heading or the start of an index line), resolve each to the **oldest** `git log -S "<entry title>"` match — and fold the edit into the run's commit. The current session's own entries can't be filled until their commit exists; the next session's hook, or the Push step's backstop, fills those.

Handoff-claim provenance. When a session opens from a Claude-authored handoff or context prompt — a goal directive, a resume note, a "here's where we left off" summary — treat its claims as unverified until the user confirms them. Claude-written content is not read in the user's voice. The why: a handoff Claude authored is not a user-vouched fact, and a fresh or weaker session can't tell which claims the user stood behind versus which Claude wrote — so a Claude-authored line ("the lint keeps flagging X") must not be used as evidence that the user reported X. Confirm before relying on it. (Resolved 2026-06-26, [cruise-control] concern (5): no claim-marking format is added — this standing rule suffices. Cruise control takes its instructions from the queue, user-vouched by construction, so it never reads a mixed Claude-authored directive whose claims would need marking; the one Claude-authored thing a run reads is its own working-state file on resume, read as mechanical state, exactly what this rule already covers.)

## E2E testing

**Taskflowapp** at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

### Reading session transcripts

Self-hosting and E2E testing increasingly evaluate Claude's behaviour from the raw session transcript. How to get and read one:

1. **Source the raw transcript** from `.claude/projects/<project-slug>/*.jsonl` — the authoritative, unedited record of the session. Read that file rather than asking Claude to regenerate or recall the conversation: a regenerated transcript is a lossy reconstruction, and it hits the handoff-provenance problem (Claude-authored content read as fact rather than as the user's own words).
2. **When the .jsonl is large enough to swamp context, preprocess it.** Run a short Python pass that strips the file to just the conversation text — drop the tool_use / tool_result blocks, the thinking, and metadata — write a slim file, then read that.

The why, weighed against the alternatives: reading the raw file in chunks does NOT save context (the same bytes accumulate across turns); a subagent keeps Claude's context clean but adds a reconstruction layer one step from the evidence; preprocess-then-read keeps Claude on the primary evidence at moderate cost; a targeted grep is lighter still but risks missing findings phrased without the search term. Applies both to the consumer E2E project (Taskflowapp) and to goal/dev sessions here.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

## Current state

**Status:** Target v1.14.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Red flags (security, privacy, and breach risks Claude surfaced) sit at the top — the first thing seen each session — each carrying an open, resolved, or accepted state. Batches use Build/Test/Audit subheadings. Deferred tests holds verification for shipped work that couldn't run in its own session, one line each (source batch slug, what to verify, what confirms it, and two axes: the deferral reason — host-side / needs-user / external — and the runnability once unblocked — Claude-runnable / user-run) — /done writes entries here; /plan reads the section each session, asks which deferrals have cleared, and rolls the now-runnable user-run ones into a test batch; /done's close-out backstops by removing any line this session's activity already confirmed; the confirming session removes the line and records it in its LOG entry. Host-side liveness is resolved by content stamp, not version: the session-start hook surfaces the installed host's build stamp (a content hash of the installed plugin's files), and /plan compares it against the target's current stamp (the same `content_stamp()` run over `plugin/si-plugin/`) — a match means host-side changes are live, with no asking the user. This replaces the older version-base rule (host base ≥ target ⇒ live), which was blind to build-batch edits that change host-side files without bumping any version. Captures are split by `---` (processed above with slugs, raw appended below). Items removed from active flow carry `Blocked by:` (trigger-based, auto-surfaces) or `Parked:` (indefinite, conscious revisit) headers. A `--- Plan session here: <reason> ---` marker between batches is a planning gate: /next halts there until a /plan session addresses the named reason, sibling to the push marker but for planning rather than host-side state.
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
