# Ideate procedure — no-code method

Follow this procedure when the user arrives with a fresh concept, or wants to explore new ideas. Exploratory by design — lighter than planning or deliberation.

## First action — load project state

1. `CLAUDE.md` — path block and project-specific notes.
2. `BUILD-PLAN.md` — scan for existing batches, OQs, and Ideas section. Needed to avoid duplication and find natural homes for new ideas.
3. `UX.md` — scope context. New ideas often need UX grounding.
4. `MANIFEST.md` — what already exists.

## Procedure order

1. **[DISCUSS] Explore the idea.** Open-ended discussion. Understand what the user is proposing, why it matters, and how it relates to what exists. Push back if the idea conflicts with existing UX principles — surface the conflict, don't quietly route around it.

2. **[BRIEF] Check for overlaps.** Scan BUILD-PLAN batches, OQs, and Ideas for anything that covers similar ground. Surface matches: "This overlaps with OQ '<name>' / batch NNNN — fold in or keep separate?"

3. **[DISCUSS] Assess fit.** Three questions:
   - Does this need a UX.md entry first? (If yes, it enters as a planning batch, not a build batch.)
   - Is there enough clarity to scope a batch, or should this become an OQ?
   - Does this slot into an existing queued batch?

4. **[SILENT] Route the idea.** Based on discussion:
   - **New OQ** — write full OQ entry in BUILD-PLAN Open Questions section. Include `Surfaced` tag with current session.
   - **New batch** — scaffold per BUILD-PLAN editing rules (planning batch if UX.md entry needed first, build batch if UX entry exists).
   - **Fold into existing batch** — append to the batch's scope or change list, with `[Suggested]` label. Confirm with user first.
   - **Ideas section** — if the idea isn't ready for any of the above, park it as a one-liner: `- YYYY-MM-DD — <one-line description>`. Lightest-weight capture.
   - **Drop** — user decides it's not worth pursuing. No BUILD-PLAN entry. Note in recap.

5. **[DISCUSS] Claude-offered ideas (optional).** After the user's idea is routed, offer: "I notice a gap / pattern in the current roadmap — want to hear it?" One idea at a time. The user routes it the same way. Don't dump multiple suggestions.

6. **[BRIEF] Recap.** What was added to BUILD-PLAN and where. Name dropped ideas with one-line reason.

7. **[SILENT] Regenerate proxies.** If `_method/proxies/` exists (or legacy `.proxies/`), regenerate any proxy whose source doc was edited this session. Skip if neither proxies directory exists.

8. **[PROMPT] Commit.** "Ready to commit. I'll stage the changes and commit with an `ideate:` prefix."

   On user okay:
   - Stage changed files explicitly (never `git add -A`).
   - Commit: `ideate: <one-line summary of what was added>`.
   - No tag. No push. `/sovgit` available afterward for ad-hoc push.

## BUILD-PLAN editing rules

Same rules as `/sovplan` — Claude holds structural authority over BUILD-PLAN. Direct edits, user reviews after.

New-feature pipeline applies: if an idea needs UX.md backing, it enters as a planning batch first, not a build batch. Don't skip the pipeline — surface it as routing, not refusal.

When scaffolding new build batches, write the full two-region structure per `DOC-STRUCTURE.md` → *Build batches → Batch structure — full shape*.

## What you must not do

- **Don't start a build.** Ideation is exploration, not building.
- **Don't edit source files.** Method docs only.
- **Don't force routing.** If the user wants to park an idea as a one-liner in the Ideas section, let them. Not everything needs full scoping immediately.
- **Don't dump multiple Claude ideas at once.** One at a time, user-approved.
- **Don't edit UX.md.** UX.md edits belong in `/sovplan` where drift checks run.

## Behavioural rules

Universal-behaviour rules apply — push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 95.*
