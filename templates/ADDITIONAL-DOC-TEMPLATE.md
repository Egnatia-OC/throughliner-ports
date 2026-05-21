# [DOC NAME].md — [Project Name]

[Brief intro: what this doc is for, who its audience is (the user? Claude at runtime? a third party?), and when it applies (e.g. "paid tier only", "internal API only"). Treat this header with the same care as `UX.md`'s header — it's the orientation a future reader needs to know whether to read on.]

This doc only describes what has been decided. Open questions live in `BACKLOG.md` as planning batches, not here as placeholders or as sentences that gesture at the doc's own undecidedness. (Same rule as `UX.md`. Full source-of-truth-doc rules: see `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.)

This doc is read-only to Claude (the agent) — the PreToolUse hook in the no-code-method plugin enforces it. Edits happen by hand during planning sessions. If Claude thinks something here should be reworded or reorganised, it flags it in chat at the end of the response.

---

## [Section name — a coherent area of behaviour the doc covers]

[Decided content. Sub-sections as needed. Stay at intent level — describe what the consumer of the doc experiences and why, not how it's wired underneath.]

## [Section name — another area]

[As above.]

<!--
Optional sections that often help in additional source-of-truth docs.
Add only the ones that earn their place; do not stub them out empty:

- An audience-appropriate "what this project is" intro near the top
  (e.g., for a system-prompt doc: "what the app is, in Claude's terms" —
  short, since the *concepts* of the app live in UX.md).

- A "Tone and presentation" section for cross-cutting rules that apply
  across every section above.

- Cross-references to UX.md or other docs, in italics, where features
  compose.

Do NOT add an "Open questions" section pointing at BACKLOG.md. Open
questions live in BACKLOG.md, not here. If you need to look up what's
open for this doc, read BACKLOG.md's planning batches.
-->

---
*No-code method — Version 39.*
