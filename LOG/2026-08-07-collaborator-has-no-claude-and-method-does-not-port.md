# 5993a10 — The outside-contributor rationale gap named, with the ask that scales and the honest statement that it cannot be closed

The why-pipeline assumes one person, working with Claude, recording rationale as they go. A second contributor working outside the method produces changes with **no rationale in the record at all** — and the obvious patch is already barred, because reconstructing intent from a diff is what the compare-never-explain rule rules out. So a shared project's record covers one person's half.

**The recommended ask, framed as an ask and never as a step the method performs:** the contributor gets their own AI tool to write the reasoning into the pull request before opening it. That is the only route that scales, because the reasoning is produced by the same thing producing the changes — a hand-written paragraph over an AI-sized change collapses fifty decisions into one label, the exact compression the pipeline exists to prevent.

**The scoping is the design decision, not a trimming of it.** The ask depends entirely on a person *outside* the project choosing to do it. The method cannot enforce it, verify it, or detect its absence. Writing it up as a *mechanism* would produce precisely what the item warns against — something nobody follows. So it ships as the ask to make.

**The structural fallback:** give the contributor an area of the codebase, so thin history is contained at a boundary the log can honestly describe rather than interleaved through everything.

**And the part that must not be engineered away, carried forward in substance from the capture:** part of a shared project will simply have thinner history than the rest. That is a cost of having the collaborator, not a fault to fix, and a design pretending otherwise produces a mechanism nobody follows.

`done.md` gained the recording half — an outside contributor's *recorded* reasoning folds into the LOG entry credited to them; where they recorded nothing, the entry says so plainly, because an honest gap reads correctly to a later session and an invented rationale does not. **The credit's format is explicitly deferred to [provenance-credit-second-person-ambiguous]** and was checked rather than assumed: that item already owns the multi-person question and names a single stored identity field as reintroducing the exact failure crediting exists to prevent.

Consumer-facing, so SPEC and a FAQ entry pair ship with it. Explicitly out of scope: specifying the collaborator's behaviour as though the method could require it, and re-deciding the identity field.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/done.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`
**Routed to Captures:** none
**FAQ:** updated — new entry "Someone else is contributing to my project and they don't use this. Does that break anything?" plus its index line
