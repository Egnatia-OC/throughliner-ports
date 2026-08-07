# 96166c6 — Tagged the audit close's routing step [BRIEF], and the tie broke on a rule rather than on preference

In `next-audit.md`, three of four sibling steps carry response-shape tags. Between them sat "Route the approved set to Unprocessed", carrying nothing — and it is not a silent step: it appends captures to Unprocessed, and the placement rule requires narrating placement in one line where judgment is exercised. So its output behaviour was left to chance in a doc where every neighbour's is pinned.

It was captured rather than fixed on sight because the choice is a real call. `[BRIEF]` matches the one-line placement narration. `[SILENT]` is defensible on the reading that the findings were presented and approved one step earlier, so re-narrating where each landed is noise the consolidate-the-scans rule would rather avoid.

**Reading the step's own text is what settles it: it does not merely append — it consolidates.** A dozen approved findings can collapse into one work item with numbered points, or stay standalone where they carry design calls the user must make. So the user approved *findings* and what they end up with is a *structure* they did not choose. Silence there means the shape of their own queue changed without a word.

**The second reason is independent and stronger.** A `[SILENT]` tag here would suppress a standing rule that applies everywhere else — and tags govern **how much is said, never which rules apply**. Reading a tag as a licence to skip a rule is a misuse of the tag system, so `[SILENT]` is not merely the weaker option; it would be wrong in a way worth recording.

**Docset A is untouched even though it carries the same gap:** adding a tag is development, not correction, so the freeze bars it.

**Files touched:** `plugin/si-plugin/docs-b/next-audit.md`

**Routed to Captures:** none
