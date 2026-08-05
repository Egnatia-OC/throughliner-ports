---
name: migrate-checklist
docset: B
note: >
  Loaded on demand when a project's QUEUE.md is in an old format and needs
  converting to the two-section model. A guided manual pass in an ordinary
  session, usually during /setup.
---

# QUEUE.md migration checklist — old format → two-section

No new skill and no hook change: this is a guided manual pass, working item by
item, drafting the converted queue and **getting the user's approval before
writing.**

**When this applies.** A project's `QUEUE.md` format is the one project doc that
reliably falls behind as the method evolves. LOG is already per-entry + index,
CLAUDE.md is topped up by session_start, and SPEC is format-agnostic — so they need
little or nothing.

```
old multi-section shape  ->  convert with this checklist
    ## Red flags · ## Batches · ### Parked · ## Deferred tests · ## Captures
```

**Plain-language guard.** A consumer reads whatever you say while migrating. Say
"your queue" not "QUEUE.md's parse structure"; "the ready-to-build line" not "the
cleared-to-run marker". **The structural terms below are for you to read, not to
narrate.**

## How to run it

```
1. read the existing QUEUE.md; identify each old section and item
2. convert each item per the rules below
3. DRAFT the whole converted queue and show it for approval — never write first
4. after writing, the post_tool_use lint confirms the new queue is well-formed
```

## The target shape

The old sections all collapse into **two**: `## Processed` and `## Unprocessed`.

```
each work item becomes:
    a #### heading                 its one-line description
    a [slug] at the END of it      kebab-case, for LOG traceability
    rationale prose beneath
    an optional user-credit        "captured by you" — ONLY when the user
                                   personally raised it. Otherwise unmarked:
                                   AI is the default author, no AI label written.
    a red-flag marker              only if it carries a security/privacy risk:
                                   Red flag · State: cleared | uncleared
```

```
which section:
    Processed    vetted, agreed and ready (or designed and buildable).
                 Within it, --- Cleared to run above this line --- separates
                 greenlit-to-build (above) from not-yet-cleared (below).
    Unprocessed  captured but not yet fully processed (still needs thought).
```

The current header prose for each section is shipped in setup.md's scaffold —
**re-copy it rather than writing your own** (rule 3).

## The judgment rules a find-and-replace can't make

**1. Old red flags.**

```
work remains   ->  a work item carrying the Red flag · State: marker
it's done      ->  moves to LOG history
never          ->  left as a bare markerless line
```

**2. Old batch / parked / deferred-test items** → work items with a slug (and a
`captured by you` credit only where the user clearly raised it), placed **by
judgment**:

```
vetted and ready        ->  Processed
still needs thought     ->  Unprocessed
a deferred test only    ->  a [user] item with a described walkthrough
the user can run
```

**3. Method-shipped boilerplate is refreshed by re-copy, never regenerated from
guesses.** FAQ files, the QUEUE.md header prose, CLAUDE-TEMPLATE scaffolding — copy
the *current shipped template* over the stale file rather than rewriting it from
the method docs.

```
per-file discriminator:
    the user's own work   ->  migrate by judgment
    method boilerplate    ->  re-copy the template
```

(Observed: a session nearly rewrote a project's FAQ from the method docs when a
verbatim re-copy was correct.)

**4. Approval before write.** Draft, show, get the okay, then write.

**5. Drop empty section placeholders.** An empty old Red-flags / Deferred-tests /
Parked block just disappears — nothing carries over.

## Preserve everything real

**Migration must lose no content the user wants kept.**

```
each item's full rationale prose  ->  carried across verbatim (re-authored only
                                      to fit the new shape, NEVER truncated)
an old "captured by you" signal   ->  kept
an old "by Claude" label          ->  just drops (AI is the default now)
any red-flag risk                 ->  kept as a marked work item
```

**When unsure whether something is the user's own work or method boilerplate,
ask** — don't guess and overwrite.

## Validated live (Hexboard, 2026-07-29)

The ad-hoc form of this checklist passed cleanly in a consumer project (host
1.15.0-test6): the QUEUE header prose was re-copied from setup.md rather than
regenerated (rule 3 fired unprompted); empty Red-flags / Deferred-tests / Parked
placeholders were dropped; a Batches › Build item became a `[user]` work item; four
Captures became `#### ` work items with slug + provenance, full rationale
preserved; approval-before-write was honoured; the lint ran clean; no content was
lost.
