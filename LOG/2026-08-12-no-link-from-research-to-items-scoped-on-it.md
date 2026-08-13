# 16ed591 — Superseded research now says so at the top of its own file, and the queue digest carries the correction to the work built on it

Research is filed precisely because it will be re-read and reused, so a research file is an upstream dependency of everything that cites it. But citation runs one way: an item names the file, and the file names nothing. When a finding is superseded there is no path from the correction back to the decisions built on it, and those decisions do not announce that they rest on anything at all.

Two halves. A superseded research file gains a `Superseded by:` line at its top, written at the moment it is superseded — which is the moment someone already has the file open to re-validate it, so the cost lands where the work already is. And `queue_digest.py` now scans each work item's prose for `resources/research/` filenames, opens each one, and flags the item where that file carries the line. Reported alongside the existing placement contradictions, which is where a flag-don't-decide finding belongs.

The convention is documented in the always-loaded research-filing section rather than fetched, and that was tested rather than assumed. The trigger looks unmissable, which usually argues for fetching — but it fails that way here: the moment a finding is superseded arrives inside whatever session happens to re-validate it, announcing nothing, so a session cannot fetch a rule telling it to write a line it does not know it owes. The detection half needs no rule at all, because the digest does it.

The check proved itself on a real instance rather than a fixture. `instruction-file-bloat-and-subtraction.md` is genuinely superseded in part — its section 1 ceiling was re-validated and found roughly an order of magnitude too tight, while its relevance argument and subtraction techniques stand — so the first marker written was the true one, saying explicitly which part falls and which does not. The digest immediately flagged this very item, which cites that file. Running it also caught a bug the design had not anticipated: a superseded note legitimately runs to a paragraph, and the flag swallowed the whole thing, so the display truncates.

The coverage limit is written into the rule text **and** printed by the digest unconditionally, on clean runs too, at the user's instruction: this catches only items that *name* the research file in their prose. An item scoped on a finding it never cites stays invisible and nothing here reaches it. A clean result means "nothing obvious", never "all clear".

Two routes lost. A "what cited this" list maintained on the research file fails silently the moment someone forgets a line — which is the exact failure mode being fixed, so it would leave the appearance of coverage with none of it. Doing nothing was weighed seriously and lost on the count: the item was filed believing this was the first caught instance, and by the time it was built there were three.

**Files touched:** `plugin/si-plugin/scripts/queue_digest.py`, `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `SPEC.md`, `resources/research/instruction-file-bloat-and-subtraction.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none

**FAQ:** updated — "Claude said a queue item 'rests on a superseded finding'. What does that mean?"

Rule gate: run — admitted as an amendment, consuming no slot. Parent named: the "Research and evidence filing" section already in skill-nonspecific-rules.md, which governs where findings land; this adds what happens when one is overtaken, subordinate to that section. Nothing evicted, and nothing needed to be — the section had no account of a finding's end of life, which is the gap. Distribution reasoned above rather than assumed. Admission evidence: three recorded instances. No bare number introduced.
