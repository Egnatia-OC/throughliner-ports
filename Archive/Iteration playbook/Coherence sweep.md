# Coherence sweep

*Single-instance. Symptom-anchored. Single broken spot that cascades; each fix exposes the next inconsistency.*

## Trigger

A specific event, not routine maintenance: a single visible broken spot in the doc that you can't resolve alone. Specifically: a symptom that *can't be fixed in isolation* — fixing it forces edits to adjacent sections that depend on it. If the broken spot is self-contained, you don't need this pass; you just fix it.

The signal that you're in coherence-sweep territory: each fix exposes another inconsistency.

Distinguished from [[Catch consolidation]] by shape: Catch consolidation handles a predefined list of independent items. Coherence sweep follows a cascade — you don't know how big the work is until it stops surfacing new inconsistencies.

## Steps

Unprompted:

- Read the current method doc in full to load state before responding.
- Diagnose the named symptom and state the gap back in plain English.
- After each fix lands, scan outward and surface the next inconsistency the fix has exposed.
- Push back on user-side complexity proposals when the existing flow already covers it. Pushback is part of the cascade — adding ceremony to cover a perceived gap can be the wrong move when the gap was illusory.
- Flag tangential issues found during reads — broken heading, orphan divider, jargon line — without bundling them into the work.

User asks for:

- Initiation of the pass itself.
- Permission/scope decisions: stay in current version vs. open a new version, restructure headers manually, introduce or remove a tag/labeling system.
- Pushback on over-reach if Claude introduces rules that bloat other docs.
- Confirmation to apply each round of edits.

Generalised: name symptom → read doc in full → state gap → propose fix → confirm → apply → scan outward for what the fix exposed → repeat until no new inconsistencies surface → flag tangential finds without auto-bundling them.

## Output

A single file with a series of traceable edits, each tied to a specific named gap from the conversation. Future-you can verify by running `git diff` and checking that every changed block traces back to a gap that was named explicitly in chat.

## When wasted

- No specific symptom to anchor on. If you can't name one broken spot, you're guessing.
- The symptom *is* contained — fixing it doesn't touch anything else. Just fix it directly.
- The doc was written from scratch in one go and hasn't accumulated drift across sessions. No cascade to surface.
- You're about to do a major restructure. Coherence work done before restructure gets thrown away.
- Time pressure. This pass cascades unpredictably — each fix can surface more, and you can't reliably scope it ahead of time.

## Refinements

- **Read manual edits more carefully before pushing back on them.** Distinguish "the user did this on purpose" from "this is a side effect of editing in a hurry." A merged-bullet stylistic choice can look like a bug from outside.
- **Run the "is this rule too broad" check before proposing, not after the user pushes back.** Self-check saves a turn.
- **Make smaller granular edits during multi-sub-section work.** Smaller diffs = better review surface.
- **Periodically state which thread you're on.** In a long cascade, an occasional "we're still following the test-notes thread; the new finding is X" helps orientation. Drift between threads without signposting is disorienting.
- **Distinguish flagging from proposing.** When flagging a tangential issue (heading bug, orphan divider), make it explicit whether you're asking the user's call or proposing a fix. A consistent format ("flag, not asking" vs. "proposing fix") tightens this.
