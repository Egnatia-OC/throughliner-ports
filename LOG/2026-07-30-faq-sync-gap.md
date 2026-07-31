# 3ca0e2e — CLAUDE.md: added an FAQ-sync clause to the SPEC-sync close trigger (host-only backstop, with considered narration) [faq-sync-gap]

The method's own shipped FAQ drifts behind the skills because its two keep-current triggers — the batch-authoring rule and the Push sweep — don't reliably fire. Rather than a new standalone gate (rejected in /plan as too expensive), added one clause to the existing SPEC-sync close trigger in CLAUDE.md working conventions, exactly as README's feature-list sync already rides it: same read moment, near-zero cost. When a user-facing change syncs SPEC/README at close, the close also confirms the FAQ entry that should ship with it was actually written. Host-only — keeping the method's FAQ current is the developer's job, not the consumer's — so the clause lives in CLAUDE.md, not the shipped done docs. The clause also specifies the considered narration to use when it fires (brief, plain-language, lead-with-the-decision) with an exemplar line.

**Files touched:**
- CLAUDE.md

**Routed to Captures:** none
