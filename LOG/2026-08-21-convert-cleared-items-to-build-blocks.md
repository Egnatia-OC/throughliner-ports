# [HASH] — this project's own epoch-4 conversion, filed as freeform because the blocks must be written with the user

Sibling of `2026-08-21-setup-migration-gate-is-epoch-3-shaped.md`, which carries the reasoning for both; one decision settled the pair, so it is written once and cited rather than restated. That item repairs the recipe, this one runs it here.

**The state, measured.** Seventeen items sit cleared to run and one — [rescan-does-not-hand-back], authored today — carries a build block. The rest do not. The queue lint has been reporting thirteen standing flags at every edit, and the hook's own phrasing, "already present in the last commit and none introduced by this change", is what made them invisible: nobody had examined them.

**What a run does with this, established by reading `next.md` and `next-build.md` rather than from the lint's word.** /next works the cleared region top-down and stops at the first item with no block. The items behind it are never reached — so this is not a run per item, it is one run that builds nothing. And it cannot repair itself by design: the build block is "the whole brief", `next-build.md` says not to open QUEUE.md to fill it out, the scope-lock refuses a build's reads of it, and `next.md`'s worked example instructs a halt rather than choosing a rule the user never agreed. The stated reason is that a halt on "which files" is a clean stop with a clear question, while a halt on "how should this work" is a design conversation started by the runner in a session whose premise is that design already happened.

**`[freeform]` from the tag's definition rather than a judgment call.** `migrate-checklist.md` requires the blocks to be written **with the user, not for them**, because telling instruction from decision history is the judgment the design reserves for a moment the user is present — the same siting the rule gate uses. A run is unattended in practice, so it is the one place this must not happen. Not `[user]`: Claude does the work with the user in the room. Placed last in the cleared region, since /next halts on a freeform item and anything beneath it is never reached.

**Nothing is lost and no instruction gets invented** — the block is a projection of prose that already exists and stays where it is.

**One judgment the conversion must not make silently.** The checklist's second branch moves a cleared item that never said what changes inside its files back below the readiness line. At least one is expected: [concurrent-plan-and-build-sessions] was deliberately left held today because its file list is provisional. Moving an item out of the cleared region is a fate decision and stays Alex's, so each is surfaced rather than decided.

**The marker is wrong until this runs**, and the item says so: `.throughliner-format-epoch` reads 4 after a run that converted nothing, and the marker is what the halt reads, so nothing will raise it.

Rule gate: not needed — no rule authored or amended; this is one project running an existing migration recipe on its own documents.

**Queue changes:** [convert-cleared-items-to-build-blocks] kept into Processed and cleared, placed last in the cleared region.
**Work processed:** kept — [convert-cleared-items-to-build-blocks].
