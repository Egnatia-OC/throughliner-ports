# 3b094b5 — Visibility: the keep-private decline speaks, the answer lands where sessions read it, and a second repository is called out

From a consumer project's defect report, re-read in full before scoping as the item required. Three defects in one incident, and one fix each.

**Tracking is not visibility.** Declining keep-private produced tracked files and nothing more — no later step connected tracking to a remote existing, so a user who wanted collaborator-readable docs had version-controlled, invisible docs for days. The decline now carries a plain follow-through: tracked but on no remote, nobody can read these until an online home exists, set up whenever you ask. The only-on-request constraint is intact, so declining never becomes publishing — the fix is the silence replaced by a statement.

**An answer recorded only in a session record is one nobody reads.** The visibility decision was written into the setup entry, so when publishing came up later Claude reasoned from scratch and recommended the opposite of what had been decided. It is now written as a standing line in the project's own CLAUDE.md, which loads at every session start, and the template carries a slot for it.

**Forks.** Code arrived post-setup as a gitignored clone of a public fork, docs were scaffolded in the parent, and the two ended up in different repositories — one public from birth, one on no remote — presented to the user as normal, twice, until they distrusted their own grasp of their own project. A new freestanding rule fires on the event: any session that brings a second git repository inside the project says so at that moment, names which repository holds the documents, and puts the root choice to the user. Setup's existing-content case runs the same check at adoption.

That third rule is freestanding with no parent, and the slot cost is owned rather than hidden. It was admitted on the recorded failure, on a trigger that is an event rather than a judgment, and because no hook can decide which root was intended.

**Files touched:** `plugin/throughliner/docs/setup.md`, `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed. The follow-up message the item promised was drafted at this close, approved, and delivered to the reporting project's mailbox; its line is in the outbound register. It states plainly that the work is committed rather than released, so they know what they are updating to and when.
Rule gate: run — the keep-private follow-through and the setup check are amendments to setup's keep-private step and Case B, their parents; the two-repositories rule is freestanding, admitted on the recorded failure, the event trigger, and no hook being able to judge it; nothing evicted, and the slot cost is stated rather than hidden.
