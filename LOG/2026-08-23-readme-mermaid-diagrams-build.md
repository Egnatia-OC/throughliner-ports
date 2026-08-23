# [HASH] — Three mermaid diagrams in the README: project structure, the work cycle, the throughline

The user's idea, scoped by her the same session: three separate diagrams, one idea each, no combined high-level view. A combined infographic drafted that day did not make sense to her, and the correction became the design principle — simplicity before any combining. Placement is hers too: the README, where GitHub renders mermaid natively.

Mermaid because it is text, so one source serves both audiences — GitHub and Claude Code render it as a diagram, and Claude reads the node-and-edge declarations directly, unlike an image (vision, lossy) or SVG (coordinate noise). Two bounds were recorded at processing and both held: diagrams are for user-facing surfaces, the method's own internal steering staying in typed text blocks; and a diagram carries structure, never reasoning, so the throughline's why stays prose with the diagram as the map beside it.

The three landed as two new sections and one addition to an existing one — project structure after "Who it's for", the work cycle inside "How to use it", and the throughline as its own section after it. The existing feature list was not touched.

**Verification is stronger than a read-through and weaker than a live render.** All three diagrams were parsed by mermaid itself, hosted in jsdom, in the session scratchpad — nothing was added to the repository. Two syntax problems were found and fixed that way before anything was claimed: a labelled dotted link written in the ambiguous `-. text .->` form, and a bare dotted link where a labelled one was meant. The pages were not viewed rendered on GitHub, which uses the same parser.

**Files touched:** `README.md`.

**Routed to Captures:** none from this item.

Tick: done, confirmed — three mermaid fences, all parsing clean; each diagram expresses one idea; the feature list is unchanged.

Rule gate: not needed — README content, no method rule text.

FAQ: not needed because documentation gaining diagrams changes nothing a user does.
