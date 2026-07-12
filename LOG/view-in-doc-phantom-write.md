# [HASH] — view-in-doc pointer treatment: added a write-then-verify-then-point ordering rule to plugin-behaviour.md and applied it at the pointer-emit sites in plan.md and next.md

The view-in-doc pointer path splits "say it's filed" from "actually file it," so the model can emit a "filed as [slug]" pointer without ever running the Write — observed 2026-07-09 in a consumer /done, where a capture pointer went out and the user opened an empty queue. Fix: a canonical "Write, then verify, then point" rule — a pointer for content written this turn is emitted only after the Write returned success AND a re-read confirms the content is in the file. Authored as a new "View-in-doc pointers" subsection in plugin-behaviour.md (so it governs every skill, including done.md where the failure struck) and applied at the five pointer sites: the read-back sites (next.md "Send the run", plan.md present-item and checkpoint) tie to the resolves-check half, since they point at pre-existing text; the write-then-point sites (next.md reshape-capture, plan.md keep-execution) tie to the full ordering, since they point at text written that turn. The two halves are kept distinct on purpose — the write-first half binds only the just-written case, the re-read-before-point half holds for both.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added the "### View-in-doc pointers" subsection with the canonical ordering rule.
- plugin/si-plugin/docs/next.md: applied at the "Send the run" and reshape-capture pointer sites.
- plugin/si-plugin/docs/plan.md: applied at the present-item, keep-execution, and checkpoint pointer sites.

**Routed to Captures:** [readable-edit-reveal-view-in-doc] — readable-edit reveals should link to the doc by line number in local mode rather than paste the text inline.
