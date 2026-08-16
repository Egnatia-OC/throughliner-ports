# d82f538 — /setup gains a keep-everything-private option and a public-repository offer that carries the licence question

Throughliner's documents hold a project's plans, reasoning and history, and a user's repository may be public. /setup previously left that posture implicit. It now settles it, in two additions and **no sixth interview question**.

**The keep-everything-private option** is offered once during scaffolding: add `SPEC.md`, `QUEUE.md` and `LOG/` to `.gitignore` so they never enter the repository. It sits in scaffolding rather than the interview because it is answerable without knowing anything about the project, and the trade is stated when offered — those documents stop being version-controlled, so an unwanted change cannot be undone by reverting.

**The public-repository offer is made only where the user asks for one**, never volunteered, and the licence question travels with it.

**Two of the four originally captured components were refused outright, both on the user's decision after the question was finally put to her.** The standalone licence question is not asked in the interview: /setup asks five questions and this method removes asks rather than adding them, and a licence is one most non-coders cannot answer while still describing what their app is — it turns a question into a small failure with "I don't know" as the honest reply. Moving it onto the public-repo offer means nobody is asked until they have asked for the thing that makes licensing matter. **The cost was named at the decision and accepted:** a user who never asks for a public repository never considers licensing at all.

The open-source-implies-open-logging idea is not surfaced at all. The reason that decided it is stronger than "unsubstantiated": the scrub gate's third part bars the method from telling a user their artifacts are screened or safe to publish, because no pattern can tell whether a sentence quietly identifies a real person. Surfacing this idea nudges a user toward publishing their planning documents — the exact direction that rule exists to avoid nudging — so it could not be offered as a neutral option, because presenting it at all is the method leaning where it has decided not to lean. **Its cost was also named and accepted:** a user who publishes may never think about whether their logs belong in the repository.

**The wording constraint most likely to be lost between design and text, so it is written into the doc itself:** the offer may set up the repository and may **never** represent the contents as screened. Any phrasing implying the artifacts have been checked contradicts a shipped rule.

Depth: short.

Rule gate: run — admitted as an amendment to /setup's existing scaffolding and interview, which already establishes a project's documents and asks its five questions; this adds an option and an offer without adding a sixth question. Nothing evicted, and two of four originally captured components refused outright. Failure evidence is the user's own capture that this content is sensitive while a repository may be public, and the shipped scrub gate's stated limit.

FAQ: updated — "Setup offered to keep my planning documents out of the repository. What does that cover, and can I change my mind?", with its index line.

**Files touched:** `plugin/throughliner/docs-b/setup.md`, `SPEC.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/`.

**Routed to Captures:** none from this item.
