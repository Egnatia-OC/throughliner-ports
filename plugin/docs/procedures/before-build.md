# Before-build procedure — Sovereign Implementer

Follow this procedure during the *before-build* phase — never during planning or building. Lock the file list and verification burden for the top batch, then present the recap.

## First action — load project state

Read only what before-build uses:

1. `CLAUDE.md` — path block and project-specific notes.
2. `BACKLOG.md` — find and validate the top build batch.
3. `UX.md` — validate `Serves UX.md:` line.
4. `MANIFEST.md` — context on existing elements.
5. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *Build batches*, *Files: sub-section*, *Tests: sub-section*.

**Do not read** BUILD-LOG or additional source-of-truth docs — before-build doesn't use them. (The BACKLOG proxy already contains the Test sessions index.)

## Active-build check

Before anything else, check whether `_method/active-build.md` exists (resolve `_method/` from `CLAUDE.md` path block). If it exists, a build is already in progress. Halt: "A build is already in progress (`_method/active-build.md` exists). Finish it with `/sovclose`, or undo it with `/sovrevert`."

## Validate pass

Before enumerating files:

1. **Find top batch.** Read BACKLOG.md's `## Build batches` section. The first non-parked `### Batch:` entry is the top batch. If no batch exists or the section is empty — halt, route to planning. Legacy folder mode: follow the first reference line to its per-batch file.
2. **Structure check.** The batch must have a `Changes:` delimiter and a `Serves UX.md:` line. Missing either → halt, route to planning ("batch needs structural cleanup").
3. **Serves line resolves.** Every `Serves UX.md:` entry must exist in UX.md Functionalities (case-insensitive). Missing → halt and route to planning; don't propose UX.md additions.

You don't reorganise the queue. Planning owns BACKLOG structure. Reorganise authority here: verification-burden splits only (halt C).

## Blocker gate

After validation, scan BACKLOG for unresolved items that would force mid-build improvisation:

1. **Batch open questions.** Read the batch body for open questions, `[?]` markers, or unresolved design decisions. Blocking if implementing without resolving would force Claude to guess mid-build.
2. **Planning batches.** Check for planning batches whose `Blocks:` line names this batch. A blocking planning batch means an unresolved question must be settled first.
3. **BACKLOG open questions section.** Check for OQs tagged to this batch or whose resolution affects its scope.
4. **Test sessions.** Check for unconfirmed test rows from the previous batch (PreToolUse enforces this structurally, but surfacing here gives the user a path to resolve before hitting the deny).
5. **Ideas and red flags.** Scan for ideas or red flags that contradict or invalidate this batch's scope. Blocking only if proceeding without addressing them would produce wrong output — not merely related.

**If blockers found:** Halt. Surface each blocking item. Nudge: "This batch has unresolved items that should be settled before building. Run `/sovdeliberate` to work through them, or `/sovplan` to rescope." Don't proceed to the work loop.

**If no blockers:** Continue silently.

## Work loop

1. **Enumerate Files:.** For each change-list bullet, identify files needing modification via Glob/Grep + MANIFEST. One-sentence summary per file.
2. **Populate Inputs: (if needed).** Non-standard resources the batch needs — specs, research files, external references. Omit standard docs (UX, BACKLOG, MANIFEST, CLAUDE.md). Spec: `DOC-STRUCTURE.md` → *Inputs: line*.
3. **Write Files: sub-section** into the batch entry in BACKLOG.md after Changes: and Inputs:. Shape: `Files:` heading + `- [ ] \`<path>\` — <summary>` per file.
4. **Write Tests: sub-section.** One entry per distinct observable behaviour. Each entry: `- <description> [<Type>] [<Verifier>]`. Types: `Look and click`, `Run and read`, `Trigger and observe`, `Generate and inspect`. Verifier: `Claude` (structural/factual) or `User` (judgement/taste/visual). Spec: `DOC-STRUCTURE.md` → *Tests: sub-section*. If no pre-specifiable tests (rare), omit.
5. **Apply batch-sizing principle.** Long test list relative to change scope → propose split (halt C).

## Batch-sizing principle

Right size = **verification burden**, not line/file count. Three sub-rules:

- **Split when small batch produces long test list.** Many unrelated surfaces → ambiguous regression signals. Split into single-surface batches. This is halt C.
- **Bundle when no new observable behaviour.** Refactors, renames, config normalisations with trivial test lists — leave grouped if planning grouped them.
- **Never fragment arbitrarily.** "Smaller is always safer" isn't this method's rule. A batch below its natural verification unit makes the next batch re-verify the same surface.

The "small enough to build and test in one session" rule means **one session's worth of verification**, not keystrokes.

## Halt-and-confirm

**(A) No top batch.** BACKLOG empty or no Build batches content. Halt, route to planning.

**(B) Change list too vague.** Can't enumerate Files: confidently (e.g. "Improve onboarding" with no specifics). Halt, surface the ambiguity, ask user.

**(C) Verification burden triggers split.** Surface the test list, propose a split, wait for okay. On okay: current batch keeps one coherent verification surface; rest moves to new batch(es) immediately below. New batches inherit scope-context and Serves line(s). Add new `### Batch:` section(s) after the current batch in BACKLOG.md. Re-run work loop on new top batch.

## Change-list label preservation (V27)

Change-list bullets may carry `[Requested]`/`[Suggested]` labels from planning. **Preserve every label exactly** when splitting (halt C). Labels track the *change*'s provenance, not the batch boundary. Don't re-classify or create new items — new items belong in planning.

## OQ accumulation nudge

After populating Files:/Tests:, scan the Open Questions section. If 3+ OQs exist or any OQ's `Surfaced` tag is older than 5 build cycles, append to the recap: "You have N open questions (oldest: <tag>) — consider running `/sovdeliberate` before your next build." Informational, not blocking.

## Pre-build sizing

After Files: and Tests: are populated, check whether the batch fits in one session. Claude can't see token count or context fullness — use conversation-visible proxy signals only.

**Trigger condition:** Files: has **8+ entries**. High file-touch count predicts sessions that risk running out of context.

**Action:** Surface a warning in the recap. Advisory, not blocking:

> "This batch has N files — sessions with this profile risk running out of context. Consider splitting via halt C before starting, or plan to `/compact` between `/sovbuild` and `/sovclose`."

If the user acknowledges and proceeds, don't repeat the warning.

## Recap

- Top batch heading and change list.
- Files: list with per-file summaries.
- Tests: list with type and verifier. Distinguish Claude-auto vs. user-check.
- Pre-build sizing warning (if triggered).
- Any BACKLOG reorganisations.
- Any conflicts or concerns.
- OQ nudge (if triggered).
- `[PROMPT]`: "Run `/sovbuild` to lock the batch and start building. Long session ahead → consider `/compact` before `/sovbuild` to preserve context."

## What you must not do

- **Don't run the build.** Before-build stops at file-list lock.
- **Don't edit files other than BACKLOG files.** Source files, UX.md, MANIFEST.md — off-limits (PreToolUse enforces).
- **Don't reorder Red flags or Planning batches.** Only Build batches section, only the top batch.
- **Don't add files outside change-list scope.** Prerequisite additions happen at build time.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*Sovereign Implementer — Version 111.*
