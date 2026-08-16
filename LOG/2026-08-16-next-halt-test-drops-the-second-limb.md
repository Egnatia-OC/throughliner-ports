# d82f538 — /next's halt condition gains the second limb it already claimed to have

Captured by the user as a testing observation about a run in another chat, in her words: stopping build to ask questions about how things should be — maybe it should be okay inside the scope? but wasn't it always "defer item back to top of queue for processing" or something?

**What `next.md` actually said, read at processing rather than recalled.** It splits two situations and forbids conflating them. **Underspecification** — you cannot tell which files this item's described work would change — surfaces, and is named as *the only case that halts*. **Adjacent-work discovery** — you can scope it but notice other work — captures and continues, "never a blocking scope-ask".

A design question about the item in hand falls through both. "How should this behave?" is not a question about which files change, and it is not other work. So a run meeting one had no defined route, and what happened is the run improvising: it stopped and asked.

**The defect is one sentence away in the same doc.** `next.md` states that "the same two-limb test runs at /plan's keep-step" — but **its own halt condition named only the first limb.** The keep check asks which files change *and what changes inside them*; the /next test asked only which files. Two tests the text says are the same test were not. An item can therefore pass the keep step at a coarse level, reach a build, and leave the design open with nothing here covering it.

**So the answer to her question is no, and no new permission is needed.** A design question about the item being built **is** underspecification — the item did not say how — arriving late because limb two was never tested at the halt. Widening the halt to both limbs routes it through a mechanism that already exists, rather than inventing a design-question branch that would legitimise stopping an unattended run to ask how things should be.

**On the requeue she remembered: it is not in the current text.** The shipped route for underspecification is halt and surface, not defer to the top of the queue. No requeue mechanism was found for this case and none is asserted — if one existed it predates the current doc, and finding it was not needed to settle this.

**Why it bites hardest where it is least visible.** A halt on "which files" is a clean stop with a clear question; a halt on "how should this work" is a design conversation started by the runner, in a session whose whole premise is that design already happened. That is the plan/build boundary failing from the build side.

A second worked example was added alongside the existing file-level one, since the original illustrated only the first limb.

Depth: short.

Rule gate: run — admitted as a correction to the existing halt condition, which already claims to be the keep-step's two-limb test; this makes the statement true. **No slot spent and nothing added** — one limb the doc says is there is written in. Failure evidence is her recorded observation of a run stopping to ask design questions, plus the doc contradicting itself in adjacent sentences.

FAQ: updated — "A build run stopped and said a job doesn't say enough to build. What does it want from me?", with its index line.

**Files touched:** `plugin/throughliner/docs-b/next.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/`. `plan.md` deliberately not edited — its keep-step already carries both limbs, and this brings `next.md` into line with it rather than the reverse.

**Routed to Captures:** none from this item. A consumer report arriving the same day describes the upstream half — an item that *states* a design question as open and schedules it into the build, which passes the keep-step on a plain reading — filed as [stated-open-design-question-passes-the-keep-step].
