# de2f5fc — The after-a-write report stops being written as a substitute for reading the record

SPEC makes reading and approving the record the control model — the user keeps Claude aligned by reading what it does. The write-first rule contradicted that in one clause: the one-line report after a write had to be *"specific enough to object to without opening the file."* That designs around the artifact not being read, in the same corpus where reading is the control.

The first reading of this item proposed correcting SPEC to describe what currently happens. That was refused, and the refusal is the item's substance: SPEC states the design being built toward, and rewriting it to match a degraded present deletes the goal while calling it a correction. The user's position settled it — reading and approving the record is what she has been aiming at throughout, and what changed is not the goal but that verbosity started costing too much time. So the defect is in the rule, not in SPEC. The bands shipped in the same run are what keep the reading affordable; the report is not.

The report stays one line. What changed is that it names its artifact precisely enough that the user knows which one to open, and points there rather than standing in for it.

The item's Files line named one file, on that same finding — the defect is in the rules, not in SPEC. That turned out to be wrong in a way worth recording. The repealed clause was restated verbatim in three further live places: `SPEC.md`'s own write-first paragraph, the shipped FAQ template, and the FAQ copy. Leaving them would have left SPEC and the user-facing documentation describing behaviour the method had just repealed. Scope grew twice mid-run, with the user's approval each time, and the run stopped twice to ask — in a run whose premise is that it does not stop. That cost is captured as `[repeal-has-no-ripple-trace]`: the existing rule requiring a grep-traced ripple covers only formats the hooks enforce, and a repealed sentence is a literal string that needs exactly the same trace.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (report clause reworded; a following paragraph states the report is a pointer to the record, never a substitute), `SPEC.md` (same repealed phrase corrected in the write-first paragraph — scope grow, user approved), `plugin/throughliner/templates/faq-template.md` and `FAQ/faq.md` (the consumer-facing statement of the repealed clause rewritten — scope grow, user approved).

**Routed to Captures:** `[repeal-has-no-ripple-trace]`, filed at the `/rescan`.

**Rule gate:** not needed — no rule authored or amended in shape; an existing rule's clause was reworded and its workaround premise repealed.

**FAQ:** updated — the write-first entry's closing paragraph, which repeated the repealed clause to users, now says the report names its document precisely and points there rather than replacing it.
