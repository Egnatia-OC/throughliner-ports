# QUEUE.md migration recipe — old format → two-section

## What this is

A step-by-step recipe for converting a **Sovereign Implementer** project's `QUEUE.md` from the old
multi-section format to the current **two-section** model (`## Processed` / `## Unprocessed` with
`####` work items). It exists because when the method evolves, the one project doc that reliably falls
behind is a project's `QUEUE.md` format — everything else (LOG, CLAUDE.md, SPEC) needs little or nothing.

**Status — read before relying on it.** This is the *ad-hoc recipe*, not a shipped `/migrate` skill or a
loaded procedure doc. Building it into a real shipped checklist is still queued in the method project as
`[migration-checklist]`. So run it as a **guided manual pass in an ordinary session** opened on the
old-format project: work item by item, checking each against the judgment rules below, drafting the
converted queue and getting the user's approval before writing.

**Provenance.** Drafted and validated live in the Hexboard consumer project on 2026-07-29 (host
1.15.0-test6) — it passed cleanly (see "Validated live" at the end). This file is a copy kept in the
method project's `resources/` so other projects can be pointed at it. If the shipped `[migration-checklist]`
ever lands, prefer that over this file.

## How to use it

1. Open a normal session on the old-format project (no special skill needed).
2. Read the existing `QUEUE.md` and identify each old section and item.
3. Convert per the rules below, **drafting the result and showing it for approval before writing**.
4. After writing, let the `post_tool_use` structure lint confirm the new queue is well-formed.

---

## The target shape

Old sections — `## Red flags`, `## Batches`, `### Parked`, `## Deferred tests`, `## Captures` — all
collapse into two sections: `## Processed` and `## Unprocessed`.

Each work item becomes:

- a `####` heading (its one-line description),
- a `[slug]` (kebab-case) at the **end** of that heading line — for LOG traceability,
- a **provenance label** in the block beneath — "captured by you" or "by Claude",
- the **rationale prose** in that same block,
- and, only if it carries a security/privacy risk, a `Red flag · State: cleared|uncleared` marker line
  in the block.

Which section an item lands in:
- **Processed** — vetted, agreed, ready (or already designed and buildable).
- **Unprocessed** — captured but not yet fully processed (still needs thought or design).
- Within Processed, a `--- Cleared to run above this line ---` marker separates greenlit-to-build (above)
  from processed-but-not-yet-cleared (below).

## The judgment rules a find-and-replace can't make

1. **Old red flags.** An "accepted / resolved, no work left" flag becomes a work item **if work remains**,
   or moves to LOG history **if it's done**. Never leave it as a bare markerless line.
2. **Old batch / parked / deferred-test items** → work items with a slug + provenance, placed in Processed
   or Unprocessed **by judgment** (vetted and ready → Processed; still needs thought → Unprocessed). A
   deferred test that only the user can run becomes a `[user]` item.
3. **Method-shipped boilerplate is refreshed by re-copy, never regenerated from guesses.** FAQ files, the
   `QUEUE.md` header prose, CLAUDE-TEMPLATE scaffolding — copy the *current shipped template* over the stale
   file rather than rewriting it from the method docs.
   - **Per-file discriminator:** user's own work → migrate by judgment; method boilerplate → re-copy the template.
4. **Approval before write.** Draft the converted queue, show it, get the okay, then write.
5. **Drop empty section placeholders** — an empty old Red-flags / Deferred-tests / Parked block just disappears.

## Validated live (Hexboard, 2026-07-29)

Run in the Hexboard consumer project on host 1.15.0-test6 and PASSED:

- Re-copied the QUEUE header prose from `setup.md` rather than regenerating it (rule 3 fired unprompted).
- Dropped empty Red-flags / Deferred-tests / Parked placeholders.
- A Batches › Build item became a `[user]` line.
- Four Captures became `####` work items with slug + provenance, full rationale preserved.
- Approval-before-write was honoured; the `post_tool_use` structure lint ran clean on the migrated queue.
- No content lost.
