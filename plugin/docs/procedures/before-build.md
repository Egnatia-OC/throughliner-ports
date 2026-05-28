# Before-build procedure — no-code method

Follow this procedure during the *before-build* phase — never during planning or building. Lock the file list and verification burden for the top build batch, then present the recap.

## First action — load project state

Read only what before-build uses:

1. `CLAUDE.md` — path block and project-specific notes.
2. `BUILD-PLAN.md`/`BUILD-PLAN/INDEX.md` — find and validate the top build batch. In folder mode, read the per-batch file.
3. `UX.md` — validate `Serves UX.md:` line.
4. `MANIFEST.md` — context on existing elements.
5. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *Build batches*, *Files: sub-section*, *Tests: sub-section*.

**Do not read** BUILD-LOG, TEST-LOG, or additional source-of-truth docs — before-build doesn't use them.

## Validate pass

Before enumerating files:

1. **Parses.** Resolve BUILD-PLAN path from `CLAUDE.md`, then: `python "$CLAUDE_PLUGIN_ROOT/scripts/parse_backlog.py" "<BUILD-PLAN absolute path>"` (both paths quoted — Windows spaces break unquoted). A `{}` outcome means no real batch found — halt and route to planning.
2. **Serves line resolves.** Every entry on `Serves UX.md:` must exist in UX.md Functionalities (case-insensitive). Missing → halt and route to planning; don't propose adding to UX.md yourself.

You don't reorganise the build queue. Planning owns BUILD-PLAN structure. Reorganise authority here exists only for verification-burden splits (halt C).

## Work loop

1. **Enumerate Files:.** For each change-list bullet, identify files needing modification via Glob/Grep + MANIFEST. Write one-sentence summary per file.
2. **Populate Inputs: (if needed).** Non-standard resources the batch needs — specs, research files, external references. Omit standard docs (UX, BUILD-PLAN, MANIFEST, CLAUDE.md). Full rules: `DOC-STRUCTURE.md` → *Inputs: line*.
3. **Write Files: sub-section** into the batch's BUILD-PLAN file (per-batch file in folder mode) after Changes: and Inputs:. Shape: `Files:` heading + `- [ ] \`<path>\` — <summary>` per file.
4. **Write Tests: sub-section.** One entry per distinct observable behaviour. Each entry: `- <description> [<Type>] [<Verifier>]`. Types: `Look and click`, `Run and read`, `Trigger and observe`, `Generate and inspect`. Verifier: `Claude` (structural/factual) or `User` (judgement/taste/visual). Full spec: `DOC-STRUCTURE.md` → *Tests: sub-section*. If no pre-specifiable tests (rare), omit entirely.
5. **Apply batch-sizing principle.** Long test list relative to change scope → propose split (halt C).

## Batch-sizing principle

Right size = **verification burden**, not line/file count. Three sub-rules:

- **Split when small batch produces long test list.** Many unrelated surfaces → ambiguous regression signals. Split into single-surface batches. This is halt C.
- **Bundle when no new observable behaviour.** Refactors, renames, config normalisations with trivial test lists — leave grouped if planning grouped them.
- **Never fragment arbitrarily.** "Smaller is always safer" isn't this method's rule. A batch below its natural verification unit makes the next batch re-verify the same surface.

The "small enough to build and test in one session" rule means **one session's worth of verification**, not keystrokes.

## Halt-and-confirm

**(A) No top batch.** BUILD-PLAN empty or no Build batches content. Halt, route to planning.

**(B) Change list too vague.** Can't enumerate Files: confidently (e.g. "Improve onboarding" with no specifics). Halt, surface the ambiguity, ask user.

**(C) Verification burden triggers split.** Surface the test list, propose a split, wait for okay. On okay: current batch keeps one coherent verification surface; rest moves to new batch(es) immediately below. New batches inherit scope-context and Serves line(s). In folder mode: create new per-batch file (allocate number by Glob scan), add reference to INDEX.md after current batch's line. Re-run work loop on new top batch.

## Change-list label preservation (V27)

Change-list bullets may carry `[Requested]`/`[Suggested]` prefixes from planning. **Preserve every label exactly** when splitting (halt C). Labels are provenance of the *change*, not the batch boundary. Don't re-classify. Don't create new change-list items — new items belong in planning.

## OQ accumulation nudge

After populating Files:/Tests:, scan the Open Questions section. If 3+ OQs exist or any OQ's `Surfaced` tag is older than 5 build cycles, append to the recap: "You have N open questions (oldest: <tag>) — consider running `/sovdeliberate` before your next build." Informational, not blocking.

## Pre-build sizing

After Files: and Tests: are populated, check whether the batch is likely to fit in one session. Claude has no visibility into token count or context fullness — use conversation-visible proxy signals only.

**Trigger condition:** Files: has **8 or more entries** AND the batch's scope-context includes unresolved **Decisions to make this batch** entries. Either condition alone is manageable; together they predict extended deliberation mid-build plus high file-touch count — the combination that blows out sessions.

**Action:** Surface a warning in the recap. Advisory, not blocking:

> "This batch has N files and open design questions — sessions with this profile have a higher risk of running out of context. Consider splitting via halt C before starting, or plan to `/compact` between `/sovbuild` and `/sovclose`."

If the user acknowledges and proceeds, don't repeat the warning.

## Recap

- Top batch heading and change list.
- Files: list with per-file summaries.
- Tests: list with type and verifier. Distinguish Claude-auto vs. user-check.
- Pre-build sizing warning (if triggered).
- Any BUILD-PLAN reorganisations.
- Any conflicts or concerns.
- OQ nudge (if triggered).
- `[PROMPT]`: "Run `/sovbuild` to lock the batch and start building. If this will be a long session, consider `/compact` before invoking `/sovbuild` to preserve context."

## What you must not do

- **Don't run the build.** Before-build stops at file-list lock.
- **Don't edit files other than BUILD-PLAN files.** Source files, UX.md, MANIFEST.md — off-limits (PreToolUse enforces).
- **Don't reorder Red flags or Planning batches.** Only Build batches section, only the top batch.
- **Don't add files outside change-list scope.** Prerequisite additions happen at build time.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 93.*
