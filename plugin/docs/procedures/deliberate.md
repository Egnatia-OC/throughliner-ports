# Deliberate procedure — Sovereign Implementer

Follow this procedure to work through accumulated open questions in BACKLOG, capture new thoughts, or both. Not in the same session as a build, and not during setup or migration. Under V90 snapshot architecture, BACKLOG is unlocked during builds — deliberation in a parallel session is safe.

## First action — load project state

1. `CLAUDE.md` — path block and project-specific notes.
2. `BACKLOG.md` — full read. Focus on Open Questions, but scan queued batches for context (OQ dispositions often reference them).
3. `MANIFEST.md` — context on existing elements.
4. `UX.md` — scope context for promotion decisions.
5. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *BACKLOG structure*, *Open questions*.

## Procedure order

1. **[BRIEF] Present OQ inventory.** List every OQ with its `Surfaced` tag and one-line summary. State the count. Flag entries older than 5 build cycles as neglected. If a legacy Ideas section exists, list those entries too with dates.

2. **[DISCUSS] Explore the user's topic (if they have one).** If the user invoked this skill with a specific thought or question:
   - Discuss: what they're proposing, why it matters, how it relates to what exists.
   - Push back if the idea conflicts with UX principles.
   - Check for overlaps: scan BACKLOG batches and OQs for similar ground. Surface matches.
   - Assess fit: Does this need a UX.md entry first? Enough clarity to scope a batch, or should this become an OQ? Slot into an existing queued batch?
   - Route: write a new OQ (light or full), scaffold a new batch, fold into existing batch, or drop. Light OQ (heading + Surfaced + one sentence) is the default for quick captures.
   If the user didn't bring a topic, skip to step 3.

3. **[DISCUSS, SEQUENCE] Work through existing OQs.** The user picks the order, or work top-to-bottom. For each OQ:
   - Read the full entry aloud (question, why-it-matters, next-step if present).
   - Surface relevant context: what's changed since surfacing, related batches or shipped work.
   - Three dispositions — ask the user:
     - **Promote** — new build or planning batch (scaffold per BACKLOG editing rules below), or fold into existing queued batch if scope fits.
     - **Drop** — remove from BACKLOG. Reason mandatory; logged in build-log entry.
     - **Re-park** — keep as OQ with updated rationale. Rewrite `Next step` to reflect current reasoning.
   - Wait for this OQ's disposition before moving to the next.
   If a legacy Ideas section exists, handle its entries here — route each to an OQ, batch, or drop.

4. **[DISCUSS] Claude-offered ideas (optional).** After the user's items are handled, offer: "I notice a gap / pattern in the current roadmap — want to hear it?" One idea at a time. Route the same way.

5. **[SILENT] Edit BACKLOG directly.** Apply all dispositions. Remove dropped OQs and routed legacy Ideas entries. Write new batch scaffolds per BACKLOG editing rules. Update re-parked OQ text.

6. **[BRIEF] Recap.** What changed: OQs promoted (name batch destination), OQs dropped (one-line reason each), OQs re-parked (what changed in rationale), new OQs captured. Name any deferred decisions.

7. **[SILENT] Write build-log entry.** Deliberate sessions produce project history. Allocate filename per close.md conventions (scan `build-log/`, next number, kebab suffix). Format:

   ```markdown
   # <Session> — YYYY-MM-DD — OQ deliberation

   **Dispositions.** <N promoted, N dropped, N re-parked, N new.>

   **Promoted.** <OQ name → batch NNNN or new batch "<heading>".>

   **Dropped.** <OQ name — reason.>

   **Re-parked.** <OQ name — what changed in rationale.>

   **New captures.** <topic → OQ or batch.>
   ```

   Prepend index line to `_method/proxies/build-log.md` (or fallbacks per close.md conventions). Idempotency: skip if same-numbered line exists.

8. **[SILENT] Regenerate proxies.** If `_method/proxies/` (or legacy `.proxies/`) exists, regenerate any proxy whose source was edited this session. Skip if no proxies directory.

9. **[PROMPT] Commit.** "Ready to commit. I'll stage the changes and commit with a `deliberate:` prefix."

   On user okay:
   - Stage changed files explicitly (never `git add -A`).
   - Commit: `deliberate: <one-line summary of dispositions>`.
   - No tag. No push. `/sovgit` available afterward for ad-hoc push.

## BACKLOG editing rules

Same rules as `/sovplan` — Claude holds structural authority over BACKLOG. Direct edits; user reviews after.

When scaffolding build batches from promoted OQs, write full two-region structure per `DOC-STRUCTURE.md` → *Batch structure — full shape*. Include `Serves UX.md:` only if the resolution identified a matching UX entry. UX grounding needed first → scaffold a planning batch instead.

New-feature pipeline applies: ideas needing UX.md backing enter as planning batches, not build batches.

## Legacy Ideas section

Consumer projects may still have an `## Ideas` section in BACKLOG. Handle gracefully: present entries alongside OQs in step 1, route them in step 3 (same dispositions), remove from the Ideas section once routed. Don't delete the section heading — the user may remove it during a planning session.

## What you must not do

- **Don't start a build.** Deliberation is planning-adjacent, not building.
- **Don't edit source files.** Method docs only.
- **Don't skip the per-OQ sequence.** Each OQ gets its own discussion turn.
- **Don't infer dispositions.** Ask the user for each one.
- **Don't force full deliberation on quick captures.** Light OQ is the default for quick thoughts — don't insist on full Why/Next-step structure unless the user wants to develop it.
- **Don't dump multiple Claude ideas at once.** One at a time, user-approved.
- **Don't edit UX.md.** UX.md edits belong in `/sovplan` where drift checks run.

## Behavioural rules

Universal-behaviour rules apply — push back, plain English, ask on ambiguity, engage with pushback.

---

*Sovereign Implementer — Version 110.*
