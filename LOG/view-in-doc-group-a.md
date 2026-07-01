# 35ccaa6 — Build [view-in-doc-group-a]: link to doc-resident text instead of re-pasting it, gated on the editor field

Second batch of the two-batch goal run. Cuts tokens by not re-rendering text that already lives in a doc: /plan's present-and-interview verbatim capture quote and its checkpoint, and /next's pre-flight top-batch quote. When CLAUDE.md records a real Editor value (the field produced by [editor-awareness-core], its only dependency), these three spots now send a one-line pointer naming the item plus a clickable link to the doc, instead of the pasted block. With no editor recorded, each degrades to the current inline verbatim quote — the safe default, unchanged for every project not yet carrying the field.

Design notes carried from the build: the editor check is defined once in plan.md's present-and-interview and referenced from its checkpoint, and stated in parallel in next.md — "an `Editor:` field with a real value (any value other than `not recorded` or an absent field)." The confirm-against-the-file re-read is kept in a pointer form: with no quoted text there's nothing to drift, so it becomes a resolves-check (the item is there, the link resolves) rather than a text-match. The token-saving path is the pointer; the inline quote stays the safe default, so nothing about the approval model changes — Group B (write-then-approve-in-place) stays parked. Checked against plugin-behaviour.md's "quoted text stays verbatim" rule: no conflict — that rule governs quoting, and the pointer path simply doesn't quote. next.md sub-step 3's heading changed from "Send the top batch verbatim" to "Send the top batch"; no other doc references the old heading by name.

**Files touched:**
- plugin/si-plugin/docs/plan.md — view-in-doc conditional in present-and-interview (sub-step 1) and the checkpoint (sub-step 6)
- plugin/si-plugin/docs/next.md — view-in-doc conditional in Step 1 sub-step 3 (top-batch send)

**Routed to Captures:** none
