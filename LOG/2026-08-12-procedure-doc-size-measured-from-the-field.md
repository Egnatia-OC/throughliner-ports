# [HASH] — done.md becomes a real router: a build close reads 15% less, a planning close is unchanged

Understudy measured a /next-plus-/done run reading about 24,000 tokens of procedure before opening a single project file, and named three causes. Two were absorbed by other work processed the same day, so this item was narrowed at the user's decision to cause 1 alone: **the router does not actually route.** `done.md` held every close shape in one file, and a planning close used roughly half of it and could not read half a file.

Three sections moved down into `done-plan.md`, each because it is cleanly assignable to exactly one shape: the **Spec-sync gate**, whose own text said the plan close "is the only one" that runs it; the **Completed `[user]`-item close**; and the **Standalone handmade-work close**. `done-plan.md` is renamed in its own header from "Plan close-out" to "No-build close-out" and opens with a three-way shape picker, since all three shapes arrive with no build working file and overlap freely — a planning session can close a completed `[user]` item, and either can carry hand edits. `done.md`'s router now sends every no-build shape to that one sub-doc.

**Measured, as the item required, because it exists to make a felt impression checkable.** A build close (`done.md` + `done-build.md`) read 6,529 words and now reads 5,526 — down 1,003, about 15%. A planning close (`done.md` + `done-plan.md`) read 7,297 and now reads 7,264, essentially flat. That flatness is the correct result rather than a failure: the plan close is the shape that actually uses the moved text.

**Nothing was duplicated**, which was the failure this had to avoid — two copies that must agree and will not, the exact drift the done-family dedup audit was run to remove. Every moved section exists in one place, verified by grep across `docs-b/` and `skills/`. Sections used by two shapes stayed in `done.md`: Verify completion, the staleness sweep, the red-flag lifecycle, LOG entry files, the wind-down re-scan, session-file cleanup, the commit core, recommend-next. That is the item's own rule for anything not cleanly assignable, and it is what bounds how much this could achieve.

**The alternative stays rejected so it is not re-proposed:** reducing `done.md` to routing alone and moving the shared core into a new `done-core.md`. It adds a file and a fetch for text every close reads anyway, so the saving is zero for genuinely shared material. The entire win came from relocating shape-*specific* text.

**One honest cost.** A close that is *only* a completed `[user]` item, or *only* handmade work, now reads `done-plan.md`'s planning steps it does not need. That is a small increase for the two rarest shapes, bought by a 15% cut for the commonest one, and it avoids the duplication that would otherwise be the price.

One consequence had to be handled rather than left: `done-plan.md`'s push override said flatly that this close does not offer push, true when it covered only planning. It now branches — planning, setup and method-doc-only commit without offering push, while a completed `[user]` item or handmade work offers it, both being real project progress. The branch existed before inside the two moved sections; bringing them together is what made it need stating once.

**Files touched:** `plugin/si-plugin/docs-b/done.md`, `docs-b/done-plan.md`
**Routed to Captures:** none from this item
**Rule gate:** not needed — text was relocated between two procedure docs and one push-offer branch stated in one place instead of two; the obligations are unchanged.
**Retired:** `Completed [user]-item close (in done.md)` and `Standalone handmade-work close (in done.md)` — both relocated to `done-plan.md`
