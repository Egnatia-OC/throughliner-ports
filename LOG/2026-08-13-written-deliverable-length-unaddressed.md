# d6efa7c — The output style now reaches the files Claude writes, not only what it says in chat

Anthropic treats written-deliverable length as a control distinct from conversational verbosity: files Claude Opus 5 writes to disk — reports, Markdown documents, summaries — are often longer than on prior models, and the documented countermeasure is one sentence, matching document length to what the task needs rather than padding with filler sections, redundant summaries or boilerplate.

Nearly everything this project produces is a written deliverable — LOG entries, queue rationale, the procedure docs themselves — while every existing control here aimed at chat: the response-shape tags, the output style, the communication rules.

The item settled where it goes in favour of the output style rather than this project's own doc authoring, because consumers' LOG and QUEUE files have the same problem and the style is what reaches them.

SPEC needed care here. Its output-style paragraph scopes the style to conversational communication and says explicitly that it is never to cap length, so a new line about document length risked reading as exactly the cap SPEC disclaims. The added sub-paragraph draws the same distinction the paragraph above it already draws: substance is written in full, at whatever length it takes, and what comes out is the padding around it.

One thing this entry deliberately does not claim. The item raised a hypothesis — that the corpus growth the rule board's MEASURED report watches may be partly a model default rather than purely an authoring failure — and flagged it as a hypothesis. Nothing here tests it, and it does not excuse the authoring problem or replace the self-authoring gate.

Rule gate: run — admitted, freestanding. Same evidence class as the cadence rule, and a documented one-line countermeasure never tried here. It evicts nothing; the cost is named in the cadence entry.

FAQ: not needed because this changes how Claude writes, not how the workflow works.

**Files touched:**
- `plugin/throughliner/output-styles/concise-throughliner.md` — a new written-file length paragraph.
- `SPEC.md` — a sub-paragraph extending the output-style entry to documents written to disk, distinguishing that from the length cap it disclaims.

**Routed to Captures:** see this session's other entries.
