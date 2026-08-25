# [HASH] — Provenance generalises from "you" to the named person, with channel identity, a consented roster, and co-author trailers

Multi-user Throughliner had never been developed: the provenance conventions hard-coded a single addressee, so a session with three people had no way to say which of them raised a capture, argued a decision, or supplied a rationale that another corrected. A consumer project running exactly that shape reported it, and named the hard half honestly — recording a name is easy, deciding whose idea something was mid-session without interrogating people is not.

The design was settled in discussion with the user. Identity: she wanted it harder than declaration, and the handshake exists natively on the consumer side, so the method records only that identity is the authenticated identity the channel supplies where one exists, with declaration as the stated weaker fallback. A project may keep a roster of recurring participants carrying only details each person chose to share, which the scrub checklist reads.

Attribution, agreed on Claude's recommendation: credit follows the named person whose message raised the idea, under the exact tests that already govern the single user — agreement is not authorship, the containment test applies per person, an unmarked item stays Claude's. So "you" becomes "the named person" and no new machinery guesses whose idea something really was. That is why nothing was evicted: the single-user wording is the case the general wording contains, and a one-person project sees no change in practice.

GitHub-side credit rides the close's existing commit step as a `Co-authored-by:` trailer, only for a participant whose recorded consent covers it and only with details they chose to share — never details looked up on their behalf.

Refused at planning: machine-level identity from git config and setup-time identity, both blind to who is actually present in a given session; and any mechanism for deciding whose idea something "really" was beyond whose message carried it, which would be interrogation by design.

Verified the trailer format by making a real commit in a scratch repository and reading it back with `git interpret-trailers --parse`, rather than assuming the shape.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/done.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment generalising the provenance rule's addressee, its parent, and extending it with the channel-identity and roster provisions; the co-author trailer rides the close's existing commit step. Nothing evicted.
