# [HASH] — plan — [setup-case-d-untagged] widened: setup.md's tag-free declaration repealed, whole doc to be tagged

The 2026-08-26 build run halted on this item because setup.md declares itself tag-free while carrying five tags. The user chose between the two coherent fixes: repeal the declaration and tag the whole doc properly. The declaration's reason is weaker than it looks — a tag on a fresh-adoption run, where the tag definitions are not loaded, is inert rather than wrong — and tags keep creeping in because editors follow the method-wide habit, so half-tagged was the worst of the three states. The item at the top of the ready region is buildable again; the halt's capture was absorbed and deleted.

**Queue changes:** [setup-case-d-untagged] rewritten and re-cleared; capture [setup-md-tag-free-declaration-contradicted] deleted as absorbed.
**Work processed:** kept (widened) — [setup-case-d-untagged].
Rule gate: run — repeal of setup.md's tag-free declaration, evicted in the item's build.
