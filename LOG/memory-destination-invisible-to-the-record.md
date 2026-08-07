# [HASH] — Made asking before a memory write explicit, and gave a memory write a one-line trace in the LOG

At a close in another project, Claude surfaced a discovery — a local build tool's daemon producing a loopback error that reads as a firewall block — reasoned that it was a fact about **the machine** rather than that project, noted it was recorded in that project's CLAUDE.md where no other project would ever see it, and offered to save it to memory as the one place that travels. It asked rather than acting.

**On the rule as written that was correct**, and the reasoning matched the rule almost exactly: memory is a good home for cross-project facts, and a machine-level tooling fact is the paradigm case. So the finding was never misbehaviour — it was a **visibility gap the rule creates and does not address**. Memory does not travel with the project and the user cannot read it. The rule accepts that for things no project doc owns, but never asks what happens when such a fact later turns out to matter here.

**The abstract worry became concrete, because the fact was traced and found WRONG.** The diagnosis was corrected two sessions later and the corrected write-up contradicts it on both counts: *"it is not the machine, not a firewall"*, and *"It is specific to Claude, not to the machine."* The real cause is the desktop app's MSIX sandbox. So the candidate cross-project fact was false in exactly the dimension that made it look cross-project in the first place.

**That turns this from bookkeeping into correctness.** Had it been saved, memory would now hold a false claim about the user's machine, presented to every future session in every project — and the user cannot read memory to notice, and no session can enumerate it to correct. Every other destination in this method is correctable because it is findable. Memory is the only one that is not, which makes it the one destination where being wrong is permanent by default. That also answers the against-argument the capture raised: the trace is **not a copy of the content**, it is the thread back to a fact that may later need correcting.

Two parts built. Asking before writing to memory becomes an explicit rule — the observed session asked anyway, which was good judgment, but good judgment is not a mechanism. And a memory write that arose inside a project leaves one line in that session's LOG entry: that a cross-project fact was saved and roughly what it concerns, **never the content**, which would re-create the double record the boundary rule exists to prevent.

The sharpening the incident argued for was taken but kept bounded: a **diagnosis** is exactly the kind of cross-project fact that looks most worth saving and is least likely to have been verified, so it is named — without growing into a general prohibition on saving anything uncertain, which would recreate the too-strong blanket rule this method already retired once.

**This is about visibility, not about restricting memory as a destination.**

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none
