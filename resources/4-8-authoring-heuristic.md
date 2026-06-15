# The 4.8-shaped authoring pass

**What.** A short checklist for any doc, procedure, or SPEC text authored in this project. Run it over the text before that text ships.

**Why.** Every session here runs on Opus 4.8. 4.8 steers on positive, quantified, exemplified, explicitly-scoped instruction — and steers least on abstract adjectives and "don't" rules. Authoring against what it actually responds to is how the plugin's own method text lands.

**Aim.** Anti-overwhelm structure and plain English — never arbitrary terseness (see the last check).

**Sources.** Distilled from [opus-4-8-verbosity-steering.md](research/opus-4-8-verbosity-steering.md) and [model-instruction-compliance.md](research/model-instruction-compliance.md).

Run each check. Each names something to do, not something to avoid.

1. **Quantify the target; don't adjective it.** Give a number the model can hit instead of an adjective it has to interpret.
   - Good: "Answer in ≤2 sentences, then stop." — Bad: "Be brief."

2. **Show the shape; don't describe it.** Include a one-line positive exemplar of the output you want. This is the single strongest lever in the research.
   - Good: a model line — "Three captures waiting; none touches the next batch — nothing blocks it." — Bad: "keep the verdict concise."

3. **Lead with the decision or ask; gate the detail.** Put the one thing the user must see or act on in the first line. Offer the reasoning behind a request rather than front-loading it.
   - Good: "Commit and push, or just commit?" then stop. — Bad: three paragraphs of rationale before the question.

4. **State the scope in words.** 4.8 is literal and won't carry an instruction from one context to another, so name where the rule applies.
   - Good: "every message in every skill, including close-outs and walkthroughs, with no exception for short steps." — Bad: leaving scope implied.

5. **Name the verbosity pattern to kill, with its positive replacement.** A concrete offender plus what to do instead beats a general "don't ramble."
   - Good: "don't restate what you just showed — point to it." — Bad: "avoid redundancy."

6. **Write it as an action, not a prohibition.** Tell the model what to do; a rule framed as a positive action steers, a bare "don't" mostly doesn't.
   - Good: "say it in one line, then wait." — Bad: "don't write more than one line."

7. **Guard against over-terseness.** Concision comes from cutting bloat — meta-narration, restating what was shown, hedging — never from cramming or dropping plain-English explanation a non-coder needs. If a cut removes something the reader needs in order to act, it is the wrong cut.
   - Good: drop the "I'm now going to…" preamble, keep the plain-English what-and-why. — Bad: compress a non-coder explanation into jargon to save words.

This list is kept short enough to apply in one pass — it models its own advice.
