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
CLAUDE.md is topped up at /plan's first step, and SPEC is format-agnostic — so they
need little or nothing.

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
4. after writing, the post_tool_use lint reports any structure problems it
   recognises — it is a deny-list, so it flags known faults and passes
   anything novel in silence. A clean run means "nothing it checks for went
   wrong", never "the queue is confirmed well-formed". Read the result yourself.
```

**Step 3 is deliberately show-first, and that is an exception to the method's
general write-first rule rather than an oversight.** The doc-bound-text rule says
approval-time text destined for one of these docs is written to the doc first and
approved in place, and six step-level instructions were converted to match it. This
one was left alone on purpose. Writing an entire speculatively-rewritten queue file
before the user has approved it is a materially different risk from writing one
work item: the whole document is replaced at once, and a reject means restoring a
file rather than editing a block back out. Recorded here so the next audit finds
the reasoning instead of reopening the question.

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
                                   # but the state constrains the SECTION —
                                   # see below
```

```
which section:
    Processed    vetted, agreed and ready (or designed and buildable).
                 Within it, --- Cleared to run above this line --- separates
                 greenlit-to-build (above) from not-yet-cleared (below).
                 A red-flagged item here is ALWAYS `State: cleared`.
    Unprocessed  captured but not yet fully processed (still needs thought).
                 The only section an `State: uncleared` item may sit in.
```

**An uncleared red flag never lands in Processed, so a converted item carrying one
goes to Unprocessed whatever the old queue implied about its readiness.** Clearing
a flag is a decision the user makes at processing; a migration is not processing,
so it cannot clear anything. If the old queue had a flagged item sitting among its
ready work, that is exactly the case this rule exists for — route it to
Unprocessed and say so when presenting the converted queue for approval.

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
the project docs.

```
per-file discriminator:
    the user's own work   ->  migrate by judgment
    method boilerplate    ->  re-copy the template
```

(Observed: a session nearly rewrote a project's FAQ from the project docs when a
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
