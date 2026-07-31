# efeb5d7 — Added the shipped-slug cross-check to done.md's commit core [close-shipped-slug-crosscheck]

From the /goal fork. A multi-batch close removes many batches in a loop with no mechanical check that each shipped slug actually left the queue — a prior goal session shipped fourteen batches but left one in QUEUE.md, so it re-presented the next session as unbuilt and wasted the first move rediscovering it was done. This adds the safety net.

It went into the shared commit core in done.md — a bolded "Shipped-slug cross-check (batch closes)" lead-in run before staging — not into each close sub-doc. The commit core is the one place every batch-closing close (build, test, audit, freeform) routes through, so one edit covers them all, and the sub-docs stayed out of this batch's scope (Files: done.md only). The step is scoped to batch closes — a planning close names no slug, so it no-ops — and stays silent unless it finds a stray slug. The why-exemplar (the fourteen-batch incident) travels inline, per the 4.8-authoring heuristic.

The cross-check was exercised live this session: this goal session's own three-batch close ran it (plugin off, reading the target done.md) and confirmed all three shipped slugs left QUEUE.md's Batches before commit. The installed-host confirmation is deferred — done.md is host-side, so the installed host carries the step only after push + reinstall. No FAQ entry: the step is a silent safety net a non-coder never meets in normal use.

**Files touched:**
- plugin/si-plugin/docs/done.md — added the Shipped-slug cross-check lead-in to the commit core.

**Routed to Captures:** none.
