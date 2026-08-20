# 8330209 — communication feedback routed by the reporting discriminator instead of absorbed into memory, and made general rather than host-only

The always-loaded memory-boundaries rule lists what memory is free for, and communication feedback is on that list. This project's own instructions say any moment memory covers for something the docs should carry is a mandatory capture. The two disagree, and the capture's diagnosis holds: saving *you are using too much text* to memory makes Claude behave better here while the shipped defect survives for everyone else.

The entry asked whether the exception should be scoped to projects testing the method. Alex decided general, and the scope goes the opposite way to the one the entry proposed. A consumer's complaint that Claude narrated badly is evidence about the method too, and it is the only such signal originating outside this project — routed to memory it makes their Claude quieter and tells the method's author nothing. Scoping to self-hosting would have protected the one project that already has other ways of noticing and left every other project silently absorbing the evidence.

So the fix needs no new machinery. The three-way discriminator already sends *the method is misbehaving* to the feedback channel and *my app* to the queue; the memory-boundaries rule simply never cross-references it. The bare term comes off memory's list and is replaced by the qualified form: feedback about a behaviour the method produced routes by the discriminator, while a preference no method rule governs — a name, a timezone, a tool the user likes — stays memory's.

Two things were corrected in passing. The entry's file list named a document retired on 2026-08-10; the rule moved into the always-loaded file, and the stale pointer was fixed at processing rather than left for the build to discover. And SPEC was checked rather than assumed — it describes no memory routing anywhere, so no sentence there goes wrong or incomplete and none was written.

**Queue changes:** [memory-masks-method-defects] kept into Processed beside the other always-loaded-rules work, its stale file pointer corrected.

**Work processed:** kept — [memory-masks-method-defects]. Deleted — none.
