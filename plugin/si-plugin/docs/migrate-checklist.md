# QUEUE.md migration checklist — old format → two-section

Claude loads this on demand when a project's `QUEUE.md` is in an **old format** and needs converting to the current **two-section** model. No new skill and no hook change: this is a guided manual pass run in an ordinary session (usually during /setup on an out-of-date or migrated project), working item by item, drafting the converted queue and getting the user's approval before writing.

**When this applies.** The one project doc that reliably falls behind when the method evolves is a project's `QUEUE.md` format. LOG is already per-entry + index, CLAUDE.md is topped up by session_start, and SPEC is format-agnostic — so they need little or nothing. If a project's `QUEUE.md` still uses the old multi-section shape (`## Red flags`, `## Batches`, `### Parked`, `## Deferred tests`, `## Captures`), convert it with this checklist.

**Plain-language guard.** A consumer reads whatever you say while migrating. Keep internal terms out of the chat — say "your queue" not "QUEUE.md's parse structure", "the ready-to-build line" not "the cleared-to-run marker" when talking to the user. The structural terms below are for you to read, not to narrate.

## How to run it

1. Read the existing `QUEUE.md` and identify each old section and item.
2. Convert each item per the rules below.
3. **Draft the whole converted queue and show it for approval before writing** — never write first.
4. After writing, the `post_tool_use` structure lint confirms the new queue is well-formed.

## The target shape

The old sections all collapse into **two**: `## Processed` and `## Unprocessed`.

Each work item becomes:
- a `#### ` heading — its one-line description;
- a `[slug]` (kebab-case) at the **end** of that heading line — for LOG traceability;
- the **rationale prose** in the block beneath;
- an optional **user-credit** in that block — `captured by you`, written only when the user personally raised the item; an item is otherwise unmarked (AI is the default author, and no AI label is written);
- and, only if it carries a security/privacy risk, a `Red flag · State: cleared | uncleared` marker line in the block.

Which section an item lands in:
- **Processed** — vetted, agreed, and ready (or already designed and buildable). Within Processed, a `--- Cleared to run above this line ---` marker separates greenlit-to-build (above) from processed-but-not-yet-cleared (below).
- **Unprocessed** — captured but not yet fully processed (still needs thought or design).

The current header prose for each section is shipped in `setup.md`'s scaffold (the `## Processed` / `## Unprocessed` blocks) — re-copy it rather than writing your own (rule 3).

## The judgment rules a find-and-replace can't make

1. **Old red flags.** An "accepted / resolved" flag becomes a work item **if work remains**, or moves to LOG history **if it's done**. Never leave it as a bare markerless line. A risk with work still to do becomes a work item carrying the `Red flag · State:` marker.
2. **Old batch / parked / deferred-test items** → work items with a slug (and a `captured by you` credit only where the user clearly raised the item), placed in Processed or Unprocessed **by judgment** (vetted and ready → Processed; still needs thought → Unprocessed). A deferred test that only the user can run becomes a `[user]` item with a described walkthrough.
3. **Method-shipped boilerplate is refreshed by re-copy, never regenerated from guesses.** FAQ files, the `QUEUE.md` header prose, CLAUDE-TEMPLATE scaffolding — copy the *current shipped template* over the stale file rather than rewriting it from the method docs. **Per-file discriminator:** the user's own work → migrate by judgment; method boilerplate → re-copy the template. (Observed: a session nearly rewrote a project's FAQ from the method docs when a verbatim re-copy was correct.)
4. **Approval before write.** Draft the converted queue, show it, get the okay, then write — per the method's capture and approval-time rules.
5. **Drop empty section placeholders.** An empty old Red-flags / Deferred-tests / Parked block just disappears — nothing carries over.

## Preserve everything real

Migration must lose no content the user wants kept. Carry each item's full rationale prose across verbatim (re-authored only to fit the new shape, never truncated), keep a `captured by you` credit where the old item shows the user raised it (an old `by Claude` label just drops — AI is the default now), and keep any red-flag risk as a marked work item. When unsure whether something is the user's own work or method boilerplate, ask — don't guess and overwrite.

## Validated live (Hexboard, 2026-07-29)

The ad-hoc form of this checklist was run in the Hexboard consumer project (host 1.15.0-test6) and passed cleanly: the QUEUE header prose was re-copied from `setup.md` rather than regenerated (rule 3 fired unprompted); empty Red-flags / Deferred-tests / Parked placeholders were dropped; a Batches › Build item became a `[user]` line; four Captures became `#### ` work items with slug + provenance, full rationale preserved; approval-before-write was honoured; the `post_tool_use` structure lint ran clean; no content was lost.
