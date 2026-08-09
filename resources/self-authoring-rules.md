# Self-authoring rules — the gate on the method's own rules

Run this before any rule, clause, or standing instruction is added to the method's own text: the procedure docs, the behaviour rules, the hooks, SPEC. Four parts, in use order — admission, eviction, distribution, wording. Model-agnostic.

## Additions are not free

The binding limit is a **count of instructions**, not a word count. Models follow roughly 150–200 reliably; past that, adding one causes fewer to be followed. Worse, content that merely doesn't apply this session does not get filtered out selectively — irrelevant instructions cause wholesale dismissal of the set, and semantically similar but inapplicable rules are the principal mechanism of that interference. A large body of same-sounding behavioural rules is exactly that shape.

So every rule admitted degrades the rules already there. That is the cost this document exists to charge, and the reason it opens by stating it: each individual addition looks free, which is how the predecessor to this document was honestly applied all the way from 6,162 words to 21,445.

Sources: [instruction-file-bloat-and-subtraction.md](research/instruction-file-bloat-and-subtraction.md), [legal-drafting-for-tight-rules.md](research/legal-drafting-for-tight-rules.md), [legislative-prose-syntax.md](research/legislative-prose-syntax.md).

## 1. Admission — does this rule get to exist?

**First, name the parent: which existing rule does this amend?** Legislation distinguishes an amendment from a *freestanding* provision. That distinction maps onto the ceiling exactly: a freestanding rule consumes one of the slots a model follows reliably; an amendment consumes none, because it changes a rule already occupying its slot. A change that can't name a parent is either genuinely new territory or — far more often — a refinement whose parent was never looked for. Look for it.

**Then write the rule as a subordinate unit of that parent, and ship it in that form if it holds.** Freestanding is what a rule falls back to when subordination fails, not the default. The test is syntactic:

```
genuinely subordinate when ALL hold:
    at least two parallel units exist
    each reads as a continuation of the parent's opening words
    all share one grammatical function
    every modifier points only at the opening words or at its own unit
    none is a complete sentence
```

A complete sentence formatted as a nested bullet is a freestanding rule wearing a bullet, and spends a slot accordingly. The same test runs both directions: writing, try the fragment before the sentence; auditing, hunt for standing rules that should have been subordinate. A unit that won't convert without losing content is genuinely freestanding — forcing it is how a subordination pass deletes a rule.

Then, four questions:

1. Has this actually failed, more than once, in a way you can point to? A speculative rule stops here.
2. Does Claude already do it unprompted?
3. Does it apply to every session, or only some?
4. Could a hook do it instead, at no attention cost? Escalate to a hook when the failure's cost justifies its standing friction — every hook adds friction every session forever, so a cheap, self-correcting slip earns sharper wording instead. The cost of the failure decides, not the fact that a rule slipped.

## 2. Eviction — what comes out

Adding a rule names what it replaces or supersedes. Rules mostly arrive as refinements of existing ones, and the superseded version is what never gets removed. Two named mechanisms:

- **Consolidation** — combine the rules on a topic into one and **repeal the priors**. The repeal is the essential half: a clearer restatement that leaves the old statement standing has doubled the text, not merged it.
- **Recasting** — where amendments have accreted past legibility, repeal the whole thing and replace it with a single new text incorporating the original and all its amendments. Substantive changes are allowed in the same move.

Also apply a **staleness test**: is this still true? A confidently wrong rule is worse than a missing one.

## 3. Distribution — where it lives

Always-loaded, or fetched on demand?

Routing works for reference material and fails for standing behavioural rules: a session cannot fetch a rule it has never read. A rule that must shape behaviour unprompted is always-loaded, and therefore pays the full admission cost. Reference material a session knows to go looking for can be fetched.

Without that constraint, distribution becomes a way of hiding bloat rather than removing it. The limit is recorded in [`LOG/2026-08-03-docset-b-progressive-disclosure.md`](../LOG/2026-08-03-docset-b-progressive-disclosure.md).

## 4. Wording — state the action the rule requires

**Anything that is described in terms of what not to do only means the rule of what TO do was never adequately described in the first place** (the user's words, 2026-08-09). A prohibition is therefore a signal to go back and specify the action, not a wording to polish. Where no action can be stated, that is the finding: the rule was never worked out.

One check, and the drafting devices that serve it. All of them are forms of a single instruction: **express a qualification as structure, not as explanation.**

- Avoid provisos. A rule followed by a swelling "provided that" is the habit this exists to break.
- Put the main clause first — the rule, then its conditions — especially where the conditions are long, since a reader needs a sentence's principal parts before it can place the rest.
- Use `subject to <X>` as a cross-reference rather than restating the exception — a restatement costs a paragraph and creates a second copy that drifts.
- Put multiple exceptions in their own subsection, referenced from the rule.
- Use short connectives — but, except that, unless, so long as — not explanations.
- One idea per provision. Don't mix conditions and exceptions in one sentence.
- Don't hide exceptions. Clarity and brevity are both served by structure over prose.

## Rationale lives outside the operative rule

Legislation states the binding rule bare and puts the reasoning in recitals and explanatory memoranda — published alongside, aiding interpretation, but not the law. The method has done the opposite, and that habit is the single largest contributor to per-rule weight. It is settled, not open: [opus-5-instruction-compliance.md](research/opus-5-instruction-compliance.md) records that why-clauses travelling with every rule are exactly the over-prescription the 5-series guidance says degrades output, and [fable-5-instruction-compatibility.md](research/fable-5-instruction-compatibility.md) resolves it — keep the why-pipeline; stop treating why-attachment as a compliance requirement.

So the operative statement stays bare. **The reasoning is published, not hidden — and it splits by audience:**

- **Why the method behaves this way** → the shipped FAQ. This is what a consumer wants, and the plugin package ships `docs/`, `docs-b/`, `hooks/`, `skills/`, `templates/`, `scripts/` and `output-styles/` — it ships neither `LOG/` nor `resources/`. Sending a consumer-facing why to the LOG doesn't relocate it, it deletes it, for everyone who isn't developing the method. The FAQ already ships, is already fetched on demand, and already carries a sync rule requiring an entry when a user-facing change lands.
- **Why a rule is worded as it is** — which alternative lost, what the authoring trade-off was → the LOG entry that decided it.

**The narrow exception, by exception and not by default:** a rule whose reason is genuinely needed to apply it correctly *at its edges* keeps one short clause.

**When moving a why, don't take an operative statement with it.** Docset B's fidelity audit found rules that had been *stated inside* their why-clauses — an exception at the end of a sentence, a definition in a parenthetical, a mechanism named in a subordinate clause — and lost when those clauses went. The risk in a subtraction pass is not what a paragraph argues; it is what a paragraph quietly defines while arguing.

## This document's own limits

It is subject to its own admission test, and its maximum size is **1,200 words**. Past that, recast it rather than appending. Per-rule worked examples are deliberately excluded: they are the growth engine, and they are how its predecessor justified its own length.

**There is no per-model authoring pass, and that is deliberate.** This document used to carry one for Opus 4.8. Docset A retired on 2026-08-09 and 4.8 is no longer a supported model, so the checklist was deleted rather than marked historical — a document that reads as live gives live instructions, and its model-specific checks were all prescription-*adding*, the opposite of what the 5-series wants. The honest cost: there is now no written account of what the current models steer on. There hasn't been one since the retirement; this only stops the document pretending otherwise. A 5-series pass gets written if something shows one is needed.
