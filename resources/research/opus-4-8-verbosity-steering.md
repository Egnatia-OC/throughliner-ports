# Steering Opus 4.8 toward concise, user-readable output

Researched 2026-06-15. Triggered by the recurring problem that Claude's exchanges run so long the non-coder user can't sustain attention — and under-the-hood project problems go unnoticed for many sessions as a result. Question asked: how to prompt Opus 4.8 for brevity *around the constraints of the system prompt*.

## Headline finding — this is steerable, and the old premise was partly wrong

The earlier file [model-instruction-compliance.md](model-instruction-compliance.md) assumed the system prompt's "helpfulness/thoroughness" directives outrank any brevity instruction, so brevity tags can't win. The current evidence corrects this:

- Anthropic's **consumer system prompt actually instructs conciseness**, not thoroughness. Simon Willison's diff of the 4.6→4.7 system prompt found new language: *"Claude keeps its responses focused and concise so as to avoid potentially overwhelming the user with overly-long responses,"* and notes **there is no instruction in either version requiring comprehensive or thorough responses.**
- The official **Opus 4.8 prompting guide** frames length as *calibration*, not a fixed thoroughness mandate: *"Claude Opus 4.8 calibrates response length to how complex it judges the task to be."* It then gives concrete levers to shorten output.

So verbosity is not an immovable system-prompt wall. The model goes long because (a) it judges the task complex and (b) the plugin steers it with the *weak form* of brevity instruction. Both are fixable. (Caveat: Claude Code's own agent system prompt differs from the consumer one and leans more agentic; but the official 4.8 levers below are written for exactly that setting.)

## What does NOT work (and is what the plugin currently leans on)

- **Negative / "don't" instructions.** "Don't be verbose," "avoid over-explaining." Official guidance: *"Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do."* MindStudio's 4.8 guide is titled on exactly this: *tell it what to do, not what to avoid.*
- **Abstract adjectives.** "Be brief," "[BRIEF]." Official guidance: quantified targets beat adjectives — *"specify 'four bullet points' rather than 'brief.'"* The plugin's response-shape tags ([BRIEF], [SILENT], etc.) are abstract adjectives; they are the weak form.
- **More / louder instructions.** Repeating or capitalising the same abstract rule adds nothing the model can act on. Volume is not the missing ingredient; *actionability* is.

## What works (ranked, from the official guidance)

1. **Positive, quantified length targets.** "Answer in ≤4 sentences, then stop." "One short paragraph, no preamble." A number the model can hit beats an adjective it has to interpret.
2. **Show a positive exemplar of the concision wanted.** A one-line model answer in the desired shape steers better than any description of it. This is the single most-recommended technique.
3. **Lead with the decision/ask; gate detail behind request.** Put the one thing the user must act on first, in one line. Offer detail ("say the word for the reasoning") instead of front-loading it. This is progressive disclosure applied to *output*, not just to docs.
4. **State scope explicitly — 4.8 is literal.** "This applies to every message in every skill, including close-outs and walkthroughs, with no exception for steps that seem short." 4.8 *"does not silently generalize an instruction from one item to another,"* so an unscoped brevity rule is read as optional in the next context.
5. **Name the specific verbosity patterns to kill.** "Don't restate what you just showed." "Don't narrate internal steps." "Don't write a meta-description of what you did — show only what's genuinely new." Concrete offenders, with the positive replacement stated.
6. **Describe user-facing updates explicitly, with examples.** Official guidance for progress updates: *"explicitly describe what these updates should look like in the prompt and provide examples."*

## The strongest lever: an output style (system-prompt priority)

Claude Code supports **output styles** — *persistent, file-based configurations that modify Claude's system prompt.* Setting `"outputStyle": "Concise"` enables a built-in concise mode. This matters because it operates **at system-prompt priority**, i.e. the level the old file worried we couldn't reach from a skill doc. A custom output style can encode the positive/quantified/exemplified rules above so they ride at the highest-priority level rather than at user-message priority where CLAUDE.md and plugin docs sit.

- Desktop app: settings are reached via the standard OS settings shortcut; the exact path to set an output style in the current desktop build needs confirmation in-app (the search evidence describes the setting key, not the desktop click-path).
- An output style is project/host-level config, not part of the plugin package — so it would steer the *developer's* sessions, and for consumers it would need to be part of what /setup or the install guide recommends.

## Effort parameter — not the lever for prose brevity

Lowering `effort` to low/medium does make 4.8 *"scope its work to what was asked rather than going above and beyond,"* which trims over-delivery — but it also risks under-thinking on complex work, and Anthropic recommends high/xhigh for coding/agentic use. Effort governs reasoning depth and tool use, not user-facing prose length. Keep effort high for the plugin's design work; steer prose brevity separately with the techniques above.

## Application to the plugin

The current verbosity system is the weak form: abstract response-shape tags ([BRIEF]/[SILENT]/…) and "don't bundle" negatives, restated across CLAUDE.md (global, project) and plugin-behaviour.md. The redesign direction:

- Give each tag a **quantified definition and a positive exemplar**, not just an adjective.
- Make "lead with the decision, gate the detail" a structural output rule, not a tone note.
- Consider encoding the concise rules in a **Claude Code output style** so they sit at system-prompt priority instead of competing at user-message priority.
- This is the same arc as [output-tag-audit] and [opening-narration-audit]; this research is design input for them.

## Sources

- [Prompting Claude Opus 4.8 — Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)
- [Claude prompting best practices — Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Simon Willison — changes in the system prompt between Opus 4.6 and 4.7](https://simonwillison.net/2026/apr/18/opus-system-prompt/)
- [MindStudio — How to Prompt Claude Opus 4.8: Tell It What to Do, Not What to Avoid](https://www.mindstudio.ai/blog/how-to-prompt-claude-opus-4-8)
- [shanraisshan/claude-code-best-practice — settings reference (outputStyle, verbose)](https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-settings.md)
