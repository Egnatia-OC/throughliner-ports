# [HASH] — Enumerated the editable set instead of naming it, and retired "method docs" as a collective term

The capture's central claim — that "project docs" and "method docs" denote the same set — was checked at processing and is **false**, and what is actually true is worse. They denote two different sets, and they differ on the one file that matters: "project docs" means SPEC.md, QUEUE.md and LOG/, while the hook's always-editable set is QUEUE.md, LOG/ and the session's working file, with **SPEC.md explicitly excluded**. That exclusion is the containment which stops a build silently rewriting what the project is meant to be.

So this was a correctness problem in the description of a safety boundary, not a naming inelegance. A reader taking "method docs are always editable" to mean the three project documents concludes that a build may rewrite SPEC.md at will. The capture's framing — pick one good name for one thing — cannot fix that, because there is no one thing. And a third reading is real too: the method also ships its own procedure docs, and "method docs" reads at least as naturally as those.

**The design, the user's call: in the scope rule, do not name the set — list it.** The queue, the log, and the session's working file. Four more words, and there is no wrong reading available — **a name always invites one; a list has none.** Deliberately the least clever option, and it is the part carrying the safety consequence.

"Project docs" keeps its existing meaning and is now used consistently for the ordinary conversational case where no boundary is being asserted. "Your own files" becomes the standard term for the user's own content — deliberately plain, because it needs no definition and cannot be inverted, which is exactly what a coined alternative failed at: one was tried, defined explicitly, and immediately misread the other way round by the first person to read it. "Method docs" is retired rather than redefined; a term with three live readings is not repairable by adding a fourth definition somewhere.

Scoped by grepping the literals at build time per the tracing rule, not from the item's list.

**The docset-A freeze call was made explicitly: A is not touched.** Renaming vocabulary is development, which the freeze bars, and A's wrong reading fails *safe* rather than silently — a 4.8 build concluding it may edit SPEC.md would be denied by the shared hook, loudly. The correction carve-out is for A contradicting the hooks or misbehaving quietly; this does neither.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/next.md`, `plugin/si-plugin/docs-b/next-audit.md`, `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/done-plan.md`, `plugin/si-plugin/docs-b/migrate-checklist.md`, `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`, `SPEC.md`, `README.md`, `INSTALL.md`

**Routed to Captures:** none
