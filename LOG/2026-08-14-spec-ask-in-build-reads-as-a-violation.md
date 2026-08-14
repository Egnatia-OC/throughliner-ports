# 78fa417 — The build's sanctioned SPEC-change ask now names itself as the normal route

Mixed authorship: the observation is the user's, in her own words — a spec edit was happening in a /next run in another project, and she said those are not supposed to be allowed in /next. The diagnosis and the fix are Claude's.

Established by reading the shipped procedure rather than from memory: the run was on next-build.md's third branch, which is the documented path. Where a build establishes new product truth SPEC does not yet carry, it asks, adds SPEC.md to its file list, and edits inline. The run named the new behaviour, said the item's file list did not include SPEC.md, and asked before writing. The user approved. Nothing was violated.

What she was remembering is real but is a different rule. The retired behaviour is the close silently *syncing* SPEC to match whatever was built, removed because a sync on a document the build never read can only record what the build did. "Builds don't edit SPEC" is a near-miss for "builds don't silently reconcile SPEC at the close", and the two collapse easily.

**The finding is a narration defect, and that bounds the fix.** The wording told the user *what* the run wanted to do and not *that asking was the sanctioned route*. Read cold, an unexpected request to edit product truth mid-build looks like a run asking permission to break a rule rather than one following it — and **the person who read it that way wrote the method.** An external non-coder has strictly less context, so the same reading is more likely, not less, and the likely consequence is worse than confusion: a user who believes the run is out of bounds says no to a change the method wanted, and SPEC silently falls behind the behaviour. Nothing about when a build may touch SPEC changed.

**The SPEC-contradiction halt was explicitly excluded**, written into the doc as a guard rather than left to judgment. That branch has the opposite problem: it is a genuine "something is wrong here" and must stay alarming. A build doing a wording pass would otherwise sweep both branches into the same reassuring register.

**The FAQ entry explains how the route works, not what it replaced** — the user's correction, in her own words: the FAQ does not need to carry history, it needs to explain how things work, because otherwise Claude has to infer how it works. The capture's original proposal to use the FAQ to explain the retired sync mechanism is therefore withdrawn. The entry says when a build may touch SPEC, why it always asks, how to answer, and that the contradiction halt is a different and more serious moment.

Rule gate: not needed — a narration change to an existing sanctioned route, plus an FAQ entry. No rule was authored or amended.

**Files touched:** `plugin/throughliner/docs-b/next-build.md` (the scope-grow ask's wording, a worked example, the read-cold explanation, the contradiction-halt guard), `plugin/throughliner/templates/faq-template.md` and `faq-index-template.md`.
**Routed to Captures:** none
