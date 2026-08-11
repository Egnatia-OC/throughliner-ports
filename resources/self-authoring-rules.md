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

### Admitting an exception — restate first

§4 says where an exception goes once it exists. This says whether it gets to exist. Nothing did, which is why exceptions have been admitted on the author's say-so.

**Three parts, in this order:**

1. **Restatement first.** Before writing an exception, restate the rule so that it does not need one. An exception is admissible only where restatement was attempted and lost content.
2. **Admission, on evidence.** Where restatement genuinely fails, the exception requires a recorded instance of the bare rule producing a wrong outcome — not the author's belief that an edge case exists. Every author believes their own rule is the edge case; that belief is what the purpose-clause test (under Rationale lives outside the operative rule) was rebuilt to stop counting as evidence. This test mirrors its shape on purpose — same bar, same reason.
3. **Review, from the drafting note.** The LOG entry admitting the exception cites the instance, so a later auditor can ask whether it is still a live risk.

**The worked case, which is the evidence for the test.** [derivation-required-for-limits] was drafted as *a bare number is banned, except where it derives from a proportion, from research, or from an external constraint*. It restates without loss as **a limit must state what it was derived from** — the same rule, with no exception in it. The first test disposed of the case that produced the block.

**No count is written, deliberately.** "More than N exceptions means the rule was never worked out" would itself be a bare limit needing its own derivation, with nothing to derive it from. The restatement test does that work without counting: a rule accreting exceptions is one whose exceptions each failed restatement, which is visible on the face of it.

## 2. Eviction — what comes out

Adding a rule names what it replaces or supersedes. Rules mostly arrive as refinements of existing ones, and the superseded version is what never gets removed. Two named mechanisms:

- **Consolidation** — combine the rules on a topic into one and **repeal the priors**. The repeal is the essential half: a clearer restatement that leaves the old statement standing has doubled the text, not merged it.
- **Recasting** — where amendments have accreted past legibility, repeal the whole thing and replace it with a single new text incorporating the original and all its amendments. Substantive changes are allowed in the same move.

Also apply a **staleness test**: is this still true? A confidently wrong rule is worse than a missing one.

## 3. Distribution — where it lives

Always-loaded, or fetched on demand?

Routing works for reference material and fails for standing behavioural rules: a session cannot fetch a rule it has never read. A rule that must shape behaviour unprompted is always-loaded, and therefore pays the full admission cost. Reference material a session knows to go looking for can be fetched.

Without that constraint, distribution becomes a way of hiding bloat rather than removing it. The limit is recorded in [`LOG/2026-08-03-docset-b-progressive-disclosure.md`](../LOG/2026-08-03-docset-b-progressive-disclosure.md).

**The always-loaded file is `docs-b/skill-nonspecific-rules.md`, and its name is the admission test: a rule belongs there only if it fires in all four skills.** Anything firing inside one skill goes into that skill's own doc, where it is paid only when the skill runs. The name is deliberately defined by negation, and the trade is worth stating because it was argued out and settled. A negative name is a good test at *authoring* time — it repels a rule that cannot pass — and a poor signal at *run* time, since a session inside /next could read "skill-nonspecific" as "not about the skill I'm running". The two risks are not symmetrical: the dumping-ground failure is evidenced, at 6,162 words growing to 21,445, while the run-time misread is hypothetical and has not been observed. So the name guards the evidenced failure, and making the file actually get read is left to a mechanism, which is the right tool for forcing in any case.

The residual weakness, stated rather than left to be discovered: a filename is soft steering, and nothing produces evidence the test was applied. The file's own first line restates the test, which improves on a filename because an editing session has necessarily read its first page — but it is still steering, not enforcement.

## 4. Wording — state the action the rule requires

**Anything that is described in terms of what not to do only means the rule of what TO do was never adequately described in the first place** (the user's words, 2026-08-09). A prohibition is therefore a signal to go back and specify the action, not a wording to polish. Where no action can be stated, that is the finding: the rule was never worked out.

One check, and the drafting devices that serve it. All of them are forms of a single instruction: **express a qualification as structure, not as explanation.**

- Avoid provisos. A rule followed by a swelling "provided that" is the habit this exists to break.
- Put the main clause first — the rule, then its conditions — especially where the conditions are long, since a reader needs a sentence's principal parts before it can place the rest.
- Use `subject to <X>` as a cross-reference rather than restating the exception — a restatement costs a paragraph and creates a second copy that drifts.
- Put multiple exceptions in their own subsection, referenced from the rule.
- These two bullets place an exception that has already earned its place. **Whether it earns one at all is decided by the restatement test in §1** (Admitting an exception — restate first): restate the rule so it needs no exception, and admit one only where restatement lost content and a recorded instance shows the bare rule going wrong.
- Use short connectives — but, except that, unless, so long as — not explanations.
- One idea per provision. Don't mix conditions and exceptions in one sentence.
- Don't hide exceptions. Clarity and brevity are both served by structure over prose.

## Rationale lives outside the operative rule

Legislation states the binding rule bare and puts the reasoning in recitals and explanatory memoranda — published alongside, aiding interpretation, but not the law. The method has done the opposite, and that habit is the single largest contributor to per-rule weight. It is settled, not open: [opus-5-instruction-compliance.md](research/opus-5-instruction-compliance.md) records that why-clauses travelling with every rule are exactly the over-prescription the 5-series guidance says degrades output, and [fable-5-instruction-compatibility.md](research/fable-5-instruction-compatibility.md) resolves it — keep the why-pipeline; stop treating why-attachment as a compliance requirement.

So the operative statement stays bare. **The reasoning is published, not hidden — and it splits by audience:**

- **Why a rule is worded as it is** — which alternative lost, what the authoring trade-off was → the LOG entry that decided it.
- **An evicted why does not have to land anywhere.** Git history keeps it, and anything still needing a decision becomes a capture. That is the whole disposal route.

**The FAQ is never an eviction destination.** An FAQ entry is written because a user would ask that question — never because a rule shed some prose. This is narrower than "the FAQ is not a rationale home", deliberately: an FAQ legitimately answers *why does the method behave this way* when a user asks, which is what an FAQ is for, and the FAQ-sync rule requiring an entry when a user-facing change lands stands untouched. What is repealed is the routing of *relocated rationale* into it. Sessions kept proposing that routing because this document used to supply the argument for it — the plugin ships neither `LOG/` nor `resources/`, so a consumer-facing why sent to the LOG is deleted rather than moved. The reasoning was sound on its premise; the premise is what is rejected, since an evicted why needs no home at all.

**The surviving destination is provisional, and this is an open question rather than a caveat.** Routing authoring-why to the LOG entry that decided it is fine for now, but it may not survive applying law-writing style to our own prose. The model this section cites puts reasoning in recitals and explanatory memoranda **published alongside** the instrument; our LOG is a development record that does not ship at all. So the LOG is where authoring-why goes because no published-alongside artifact exists, not because it is the right home.

### Where a reason is needed to apply the rule — the purpose-clause test

The old narrow exception — *a rule whose reason is genuinely needed to apply it correctly at its edges keeps one short clause* — is **repealed**. It is not consistent with the legislation this section derives from, which states the binding rule bare with no "unless the reason helps" carve-out; and an exception phrased as a judgment is decided by whoever is authoring, every one of whom believes their own rule is the edge case. That is the shape under which the predecessor document grew from 6,162 to 21,445 words while being honestly applied.

But some sentences genuinely must travel with a rule for the rule to be applied correctly, and repealing the exception with nothing in its place strips them. The replacement is **reclassification, not exemption**: if a reason is needed to apply the rule correctly, it is not rationale attached to the rule — it is part of the rule, and it is written as operative text. Law does this as a purpose or objects clause: inside the instrument, shipping with it, guiding application, neither recital nor memorandum. Reclassification asks a question with an answer — *can this rule be applied correctly without this sentence?* — where the repealed exception asked how special a rule is.

**Three parts, and the order is the safeguard.**

1. **Admission, on evidence.** A purpose clause earns its place only where there is a recorded instance of the rule being misapplied without it. Not the author's belief that it helps at the edges.
2. **Protection, by grammar.** Once admitted, write it into the operative sentence so it cannot be removed without leaving the rule incomplete. The auditor's test is the same one in reverse: delete the sentence and read what remains — a complete instruction means what you deleted was rationale, an unfinished one means it was operative. §1's subordination test supplies the grammar. A marker or tag was rejected: a fresh short session may not know a convention and will strip it while skimming, whereas broken grammar is visible at the moment of the cut.
3. **Review, from the drafting note.** The LOG entry admitting the clause cites the instance, so a later auditor can ask whether the misapplication is still a live risk. Without this the category would be permanently immune to the staleness test.

**Three proposals were defeated on the way to that order, recorded so they are not re-proposed.** (a) Grammar as the *admission* test — rejected: necessity is not decided by syntactic validity, and using it that way inverts into a bloat vector, since welding any sentence into the operative clause would make it permanently unstrippable. Syntax protects; it never admits. (b) Weld-first, justify after — that is exactly the failure the order above prevents; gate-then-weld is the same two steps in the order that works. (c) Shipping the admitting instance alongside the clause — rejected, because that ships history with the rules, which is the bloat being fought. **The instance never ships.** What ships is the purpose clause alone, bare and operative.

**Why the unshipped evidence leaves no gap.** Protection is readable from the shipped text alone, since inseparability is visible in the sentence. The instance is needed only to re-test an admission, and re-testing is maintenance, which happens only in the repo where the LOG is — consumers never audit method rules. Net effect: the shipped docs get *shorter* than under the repealed exception, which licensed a short clause of reasoning; this licenses none, only operative text.

**The honest limit.** This protects against accidental stripping, which is the failure that has actually happened. It cannot stop a pass that deliberately rewrites a rule to remove the dependency; nothing short of a hook that understands meaning could. What the form guarantees is that doing so is a visible rewrite rather than a quiet deletion.

**When moving a why, don't take an operative statement with it.** Docset B's fidelity audit found rules that had been *stated inside* their why-clauses — an exception at the end of a sentence, a definition in a parenthetical, a mechanism named in a subordinate clause — and lost when those clauses went. The risk in a subtraction pass is not what a paragraph argues; it is what a paragraph quietly defines while arguing.

## This document's own limits

It is subject to its own admission test, and its maximum size is **1,200 words**. Past that, recast it rather than appending. Per-rule worked examples are deliberately excluded: they are the growth engine, and they are how its predecessor justified its own length.

**There is no per-model authoring pass, and that is deliberate.** This document used to carry one for Opus 4.8. Docset A retired on 2026-08-09 and 4.8 is no longer a supported model, so the checklist was deleted rather than marked historical — a document that reads as live gives live instructions, and its model-specific checks were all prescription-*adding*, the opposite of what the 5-series wants. The honest cost: there is now no written account of what the current models steer on. There hasn't been one since the retirement; this only stops the document pretending otherwise. A 5-series pass gets written if something shows one is needed.
