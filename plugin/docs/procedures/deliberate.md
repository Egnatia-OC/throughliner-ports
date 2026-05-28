# Deliberate procedure — no-code method

Follow this procedure to work through accumulated open questions in BACKLOG. Never during builds, setup, or migration.

## First action — load project state

1. `CLAUDE.md` — path block and project-specific notes.
2. `BACKLOG.md` — full read. Focus on Open Questions and Ideas sections, but scan queued batches for context (OQ dispositions often reference them).
3. `MANIFEST.md` — context on existing elements.
4. `UX.md` — scope context for promotion decisions.
5. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *BACKLOG structure*, *Open questions*, *Ideas section*.

## Procedure order

1. **[BRIEF] Present OQ inventory.** List every open question with its `Surfaced` tag and a one-line summary. State the count. Flag entries older than 5 build cycles as potentially neglected.

2. **[BRIEF] Present Ideas inventory.** If the Ideas section has entries, list them with dates. These are candidates for promotion to OQs or direct routing to batches.

3. **[DISCUSS, SEQUENCE] Work through OQs.** The user picks the order, or work top-to-bottom. For each OQ:
   - Read the full entry aloud (question, why-it-matters, next-step if present).
   - Surface relevant context: what's changed since the OQ was surfaced, related batches or shipped work that bears on it.
   - Three dispositions — ask the user:
     - **Promote** — becomes a new build or planning batch (scaffold per BACKLOG editing rules below). Or fold into an existing queued batch if scope fits.
     - **Drop** — remove from BACKLOG. Reason is mandatory; logged in the session's build-log entry.
     - **Re-park** — keep as OQ with updated rationale. Rewrite the `Next step` line to reflect current reasoning.
   - Wait for this OQ's disposition before moving to the next.

4. **[BRIEF] Work through Ideas.** For each Ideas-section entry the user wants to address:
   - Discuss fit: does it overlap existing OQs or batches? Does it need UX.md grounding first?
   - Route: promote to OQ (write full OQ entry), fold into existing batch, scaffold new batch, or drop.
   - Remove the one-liner from Ideas section once routed.

5. **[SILENT] Edit BACKLOG directly.** Apply all dispositions. Remove dropped OQs and routed Ideas entries. Write new batch scaffolds per BACKLOG editing rules. Update re-parked OQ text.

6. **[BRIEF] Recap.** What changed: OQs promoted (name batch destination), OQs dropped (one-line reason each), OQs re-parked (what changed in rationale), Ideas routed. Name any deferred decisions.

7. **[SILENT] Write build-log entry.** Deliberate sessions produce project history. Allocate filename per close.md conventions (scan `build-log/`, next number, kebab suffix). Format:

   ```markdown
   # <Session> — YYYY-MM-DD — OQ deliberation

   **Dispositions.** <N promoted, N dropped, N re-parked, N ideas routed.>

   **Promoted.** <OQ name → batch NNNN or new batch "<heading>".>

   **Dropped.** <OQ name — reason.>

   **Re-parked.** <OQ name — what changed in rationale.>

   **Ideas routed.** <idea → destination.>
   ```

   Prepend index line to `_method/proxies/build-log.md` (or fallbacks per close.md conventions). Idempotency: skip if same-numbered line exists.

8. **[SILENT] Regenerate proxies.** If `_method/proxies/` exists (or legacy `.proxies/`), regenerate any proxy whose source doc was edited this session. Skip if neither proxies directory exists.

9. **[PROMPT] Commit.** "Ready to commit. I'll stage the changes and commit with a `deliberate:` prefix."

   On user okay:
   - Stage changed files explicitly (never `git add -A`).
   - Commit: `deliberate: <one-line summary of dispositions>`.
   - No tag. No push. `/sovgit` available afterward for ad-hoc push.

## BACKLOG editing rules

Same rules as `/sovplan` — Claude holds structural authority over BACKLOG. Every change is direct; the user reviews after.

When scaffolding new build batches from promoted OQs, write the full two-region structure per `DOC-STRUCTURE.md` → *Build batches → Batch structure — full shape*. Include `Serves UX.md:` line only if the OQ resolution identified a matching UX entry. If the OQ needs UX.md grounding first, scaffold a planning batch instead.

New-feature pipeline applies: ideas that need UX.md backing enter as planning batches first, not build batches.

## What you must not do

- **Don't start a build.** Deliberation is planning-adjacent, not building.
- **Don't edit source files.** Method docs only.
- **Don't skip the per-OQ sequence.** Each OQ gets its own discussion turn.
- **Don't infer dispositions.** Ask the user for each one.
- **Don't treat Ideas as OQs.** Ideas are lighter — quick routing is fine. Don't force full deliberation on a one-liner.
- **Don't edit UX.md.** UX.md edits belong in `/sovplan` where drift checks run.

## Behavioural rules

Universal-behaviour rules apply — push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 97.*
