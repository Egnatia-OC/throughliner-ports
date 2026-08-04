# f832385 — Detect repo visibility at /setup as a safety input, then settle licensing and publishing

The dependency inverted, which is why this could no longer sit behind the scrub work. The item originally waited on the scrub build — don't encourage publishing until the leak risk is closed — but that build turned out to depend on the repo-visibility fact recorded *here*, because the write-time rule is conditional on whether the repo is public. Mutually dependent, so they were built as one, with the visibility half first.

Visibility is a **safety input before it is a publishing choice**, and that reframing is the substance of this item. It was originally framed as a decision ("do you want this on GitHub?"). Its more important job is that knowing the repo is public is what makes the privacy rule urgent rather than theoretical — and that applies to every project, including ones with no interest in publishing, because a private repo can be shared or made public later without the method noticing.

It is **detected, not asked**. A recorded answer goes stale silently, which is exactly what happened: this repo's visibility was set long ago and nobody knew it until one command was run mid-session, six weeks into a live exposure. Detection costs a single command and is never out of date. Asking is the fallback where detection isn't available — no remote, no tooling, a non-GitHub host — and that answer is recorded explicitly as a stated fallback rather than a detected fact, so a later session knows which it's reading.

Licensing and publishing follow, unchanged in substance and second in order: ask about the licence in plain terms, then offer public-repo setup framed off that choice, with capture-for-later as a real answer rather than a formality. Offer, never push. For the maximally-private posture, an offer to gitignore all project docs.

The open question stays open and now has evidence against it. Whether open source implies open logging was flagged as the user's own unsettled opinion, deliberately not baked into a recommendation. This project supplies a data point on the sceptical side — it is open source, its logging was open, and a third party's private matter was publicly readable for six weeks as a direct result. Not decisive, since the failure was a missing rule rather than open logging as such, but it belongs on the record before anyone turns the intuition into guidance.

**Files touched:** `plugin/si-plugin/docs-b/setup.md` and `docs/setup.md` (new Step 3b — detection, licence, publishing), `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` (the Repo visibility field), `CLAUDE.md` (this project's recorded visibility), `SPEC.md`, `faq-template.md` and `faq-index-template.md`.
**Routed to Captures:** none.
