# Fable 5 compatibility with the project's Opus 4.8-specific authoring techniques

Researched 2026-07-02. Triggered by the user asking how compatible Claude Fable 5 is with the 4.8-specific instructions in the method, and whether some can go to make the method lighter. Primary source: Anthropic's official Fable 5 prompting guide. Note: the session doing this research ran on Fable 5 itself.

## Headline

Fable 5's instruction following is strong enough that most of the 4.8 compensation machinery is no longer *needed* — and the official guide warns some of it can now *hurt*: "Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality. Review and consider removing older instructions if default performance is better."

The guide's through-line: "Instruction-following is improved enough that you can steer most behaviors with a brief instruction rather than enumerating each behavior by name."

## The 4.8 checklist (authoring-heuristic.md), item by item

1. **Quantify the target, don't adjective it** — no longer necessary. A short brevity instruction steers Fable as well as quantified targets. Harmless to keep, but it's weight the docs no longer need.
2. **Show the shape (positive exemplar)** — still useful, still cheap. Exemplars remain a general prompting best practice; keep where they exist, stop requiring them everywhere.
3. **Lead with the decision, gate the detail** — keep. The Fable guide recommends exactly this shape ("Lead with the outcome. Your first sentence… the thing the user would ask for if they said 'just give me the TLDR'").
4. **State the scope in words** — largely obsolete. This existed because 4.8 "does not silently generalize an instruction from one item to another." Fable generalizes well; the guide's examples carry no scope enumerations and it explicitly says enumeration is unnecessary. The long "scope: every message in every skill, with no exception for…" tails are the single biggest candidate for trimming.
5. **Name each verbosity pattern to kill** — obsolete. Direct quote: "A short brevity instruction is as effective as listing each pattern."
6. **Action-framing instead of "don't"** — obsolete as a requirement. Fable follows prohibitions fine; the official guide itself uses "Don't add features, refactor…" blocks.
7. **Guard against over-terseness** — keep. Matches Fable guidance verbatim in spirit: "Being readable and being concise are different things, and readability matters more."

**Response-shape tags ([SILENT]/[BRIEF]/[PROMPT]/[SEQUENCE])** — the 4.8 research found abstract tags were the "weak form." On Fable, stronger instruction following means the tags likely hold *better*, and their quantified definitions in plugin-behaviour.md remain compatible. No removal needed; the elaborate per-tag "why" justifications (added because 4.8 needed reasons to comply) are the trimmable part.

**"Carry the why with the rule"** — partially obsolete as a compliance technique (Fable complies without the reason), but the guide still says Fable "performs better when it understands the intent behind a request," and the why-pipeline's rationale-preservation serves the human and future sessions, not just model compliance. Keep the why-pipeline; stop treating why-attachment as a compliance requirement.

## New Fable-specific cautions (things to ADD awareness of, not remove)

- **Over-prescription degrades output.** The failure mode flips: on 4.8 the risk was under-specification; on Fable it's micromanagement. "Claude Fable 5 isn't meant to be micromanaged through lengthy instructions."
- **Reasoning-echo instructions can trigger refusals.** "Prompts, skills, or harness instructions that tell the model to echo, transcribe, or explain its internal reasoning as response text can trigger the reasoning_extraction refusal category… Audit existing skills and system prompts for reflection or show-your-thinking instructions when migrating." The method's docs should be audited for anything reading as "explain your reasoning in the response" (the why-pipeline writes rationale into artifacts, which is document content, not reasoning-echo — but wording matters).
- **Longer turns, overplanning at high effort** — steerable with a short "when you have enough information to act, act" instruction.
- **Unrequested actions** — Fable can occasionally act beyond the ask; explicit boundary statements still earn their place.

## Scope caveat for this project

The project's declared model target is Opus 4.8 (CLAUDE.md Model target, resolved 2026-06-15: "future models are adopted when they arrive"). Nothing in the 4.8-shaped text can "go" until the project decides to retarget (or dual-target) — and consumers of the plugin may run either model, so shipped docs face a mixed audience. The 4.8 techniques are mostly *harmless-but-heavy* on Fable, except the over-prescription risk, which is a genuine reason to slim rather than just tolerate.

## Sources

- [Prompting Claude Fable 5 — Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) (primary; all quotes above)
- [How to Actually Prompt Claude Fable 5 — AlphaSignal](https://alphasignalai.substack.com/p/how-to-actually-prompt-claude-fable) (corroborates the "deletion" through-line)
