# Tersify procedure — no-code method

Guided compression of source-of-truth docs to reduce token cost. Two phases: **triage** (rank and flag) then **audit** (compress user-selected targets one at a time).

**Planning phase only.** Source-of-truth docs must be unlocked. If a `Status: active` batch exists in BACKLOG, deny with: "Source-of-truth docs are locked during build. Run `/sovtersify` in a planning session."

## Phase gate

Before anything else, check BACKLOG for an active batch:

1. Read BACKLOG (resolve path from `CLAUDE.md` path block — `_method/proxies/backlog.md`, `BACKLOG/INDEX.md`, or `BACKLOG.md`).
2. If any batch has `Status: active` → stop. Tell the user: "Source-of-truth docs are locked during build. Run `/sovtersify` in a planning session."
3. Otherwise proceed.

## Phase 1 — Triage

**Goal.** Show the user which docs cost the most context and what kinds of savings exist, so they can choose where to spend effort.

**Step 1 — Collect the doc list.** Read `CLAUDE.md` path block. Collect all source-of-truth doc paths: `UX.md`, `MANIFEST.md`, additional docs declared in the path block, `CLAUDE.md` itself. Exclude method-internal docs (BACKLOG, TEST-LOG, build-log, proxies, research) — those have their own maintenance cycles.

**Step 2 — Measure.** For each doc, count lines. Sort descending by line count.

**Step 3 — Flag issues.** Read each doc and flag issues in three categories:

- **Wrong-home content.** Content that belongs in a different doc — implementation details in UX.md, UX rationale buried in MANIFEST.md, scope discussion in a source-of-truth doc instead of BACKLOG. Name the content and where it should go.
- **Structural problems.** Redundancy (same point made twice), poor grouping (related content scattered), unnecessary nesting, sections that could merge.
- **Verbose prose.** Passages where the same meaning could be said in fewer words without losing rules or nuance. Flag specific passages, not vague "this section is wordy."

**Step 4 — Present triage summary.** `[PROMPT]` One table, ranked by line count:

| Doc | Lines | Wrong-home | Structural | Verbose | Est. savings |
|---|---|---|---|---|---|
| ... | ... | N issues | N issues | N passages | ~N lines |

Below the table, one-line summary per flagged issue (grouped by doc).

Ask: "Which docs do you want to audit? You can pick specific ones, or say 'all' for a full pass."

## Compact gate

If the user selects **all** (full audit), recommend compacting first: "The triage analysis is filling context that won't be needed during editing. I'd recommend running `/compact` now, then continuing with the audit. Want to do that?"

If the user selects specific docs, skip this — the triage context is small enough to keep.

## Phase 2 — Audit

Work through selected docs **one at a time**. `[SEQUENCE]` — state how many docs are queued, start with the first.

**Per doc:**

1. **[BRIEF] State the doc name and its line count.**

2. **Wrong-home content.** For each flagged item: show the content, name the destination, and propose the move. `[PROMPT]` — wait for approval before editing. If approved, edit both source and destination in this step. If the destination is a locked doc (e.g. moving something into BACKLOG during build), flag it for later instead of editing.

3. **Structural problems.** For each: describe the problem, show the proposed restructure. `[PROMPT]` — wait for approval. Edit on approval.

4. **Verbose prose.** For each passage: show the original, show the compressed version, explain what was cut and why it's safe to cut. `[PROMPT]` — wait for approval. Edit on approval.

5. **[BRIEF] Per-doc summary.** Lines before → lines after. What changed.

After all selected docs are done:

6. **[BRIEF] Final summary.** Total lines saved across all docs. List of docs edited and their before/after line counts.

## Rules

- **Never cut rules or constraints.** Compression means fewer words for the same meaning, not fewer rules. If a sentence carries a constraint Claude needs, it stays — even if it's verbose.
- **Never merge distinct concepts.** Two rules that look similar may have different enforcement points. Keep them separate unless they genuinely say the same thing.
- **User approves every change.** No silent edits. The user sees what's being cut and why before it happens.
- **One doc at a time.** Don't batch changes across docs. Finish one, move to the next.
- **Explain what was cut.** For every compression, state what words were removed and why the meaning survives without them. The user can't judge safety without this.

## Behavioural rules

Universal-behaviour rules apply. Keep triage output tight — the point is saving tokens, not spending them on the analysis.

---

*No-code method — Version 86.*
