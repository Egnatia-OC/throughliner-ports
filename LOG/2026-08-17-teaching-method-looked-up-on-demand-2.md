# 7e3c1c8 — on a repeat question, look up how that specific thing is taught

One clause on the research-and-evidence rule, whose *what would answer this?* trigger already covers reaching outward. This points the same question at how something is taught rather than at an external fact, so it costs no new slot.

The trigger is the user asking about the same thing again. "Explained twice" was rejected because it requires Claude to notice its own explanation did not land, and noticing-based triggers do not fire here — a session satisfied with its answer notices nothing. A repeat question is a fact rather than a self-assessment.

The clause opens by working out which part did not land, asking the user where that is not obvious. That answers the user's own objection that a repeat question may be too vague to search on: "I still don't get it" names no concept, and searching the whole subject returns exactly the generic pedagogy she had already rejected. It also feeds the search the narrow target that gets better answers.

The option set is what Claude can perform in text plus what Claude can point at, taking the shortest source whose content it can read — captions, an article, a transcript — and reading it before pointing. That is the same bar the method already sets for handing over a command: a non-coder cannot tell a bad resource from a good one, and the failure arrives in their hands.

The limit is written into the rule rather than assumed: where neither party can name the missing part, no lookup helps and the answer is a different explanation. One residual stands unfixed — a transcript is not the demonstration, and Claude can confirm a source is on-topic without confirming the presentation works.

Rule gate: run — a clause on an existing rule; nothing evicted.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none
