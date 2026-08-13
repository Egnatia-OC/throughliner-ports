# d6efa7c — The output style now says how often to speak while working, which is the half of the length problem it never addressed

Alex raised this in her own words: she is extremely fatigued from reading very long responses and believes they could be shorter. The specific diagnosis is Claude's, from `resources/research/response-length-and-bundling-steering.md`.

Length and narration are two different problems, and the plugin only addressed one. Anthropic's Opus 5 guidance gives them separate sections and separate fixes. Response length is how long a single message is; progress narration is how often the model speaks at all during agentic work — announcing before each tool call, updating mid-task, summarising afterwards. The output style addressed the first and said nothing whatever about the second.

For a Claude Code session the second is the larger of the two, because most of the text a user reads is narration between tool calls rather than any one long answer. The guidance names it directly: Opus 5 narrates readily during agentic work, tending to announce what it is about to do, with per-message output in agentic sessions often longer than prior models'.

Two things the item left open were settled in the build. The first is whether the official wording is adopted close to verbatim or reworded for the plugin's register — reworded, because the surrounding paragraphs are written as bold lead-in plus plain sentences and a verbatim block would read as an imported foreign rule. What is kept faithfully is its *shape*: the fix is a cadence, not an adjective, and it names three concrete moments — one sentence before the first tool call, a brief update on finding something important or changing direction, and leading with the outcome at the finish. Naming the moments is what makes it steerable; asking for brevity does not reach it.

The second is where it lives. The output style won over skill-nonspecific-rules.md, and the reasoning is the one already recorded for this concern: the style rides system-prompt priority, which is the level that holds when lower-priority instructions are skipped, and it reaches every consumer automatically. It also maps onto the existing lead-with-the-decision rule rather than competing with it.

SPEC's output-style paragraph listed what the style steers — lead with the decision, one item at a time, gate detail — and cadence is a fourth thing not in that list, so the sentence would have gone incomplete the moment this shipped. It now names cadence in the list and carries a sub-paragraph on why it is a separate subject from message length.

Rule gate: run — admitted, freestanding. No parent: cadence is a different subject from message length, which is precisely why the style addressed length and never reached the thing a Claude Code user actually reads most. It has failed repeatedly and pointably, applies to every session, and no hook could do it. It evicts nothing, which is a real cost — the style is loaded in every session of every consumer project, so growth here is the most expensive growth in the method.

FAQ: not needed because this changes how Claude writes, not how the workflow works, and the FAQ documents the workflow.

**Files touched:**
- `plugin/throughliner/output-styles/concise-throughliner.md` — a new narration-cadence paragraph.
- `SPEC.md` — the output-style entry's steer-list extended, plus a sub-paragraph on why cadence is its own subject.

**Routed to Captures:** [distribute-brevity-rules-further], filed in the post-close tail below.

---

## After the close

Alex asked, after the commit, whether these changes mostly affect docs or in-chat prose, and on being told four of the five are chat-facing said she wanted to "distribute this benefit as much as I can" and to capture any further distribution worth doing.

That became `[distribute-brevity-rules-further]` in Unprocessed. It surveys four surfaces that carry nothing about cadence today — `CLAUDE-TEMPLATE.md` (the file /setup writes into a consumer's own project, and the one layer a user can edit themselves), `skill-nonspecific-rules.md`'s Communication section, the four `skills/*/SKILL.md` prompts, and the response-shape tags.

The item is written to be capable of resolving as "do nothing", and that framing is deliberate rather than hedging. The research this whole set was built from says repetition is not the missing ingredient: the one-at-a-time rule is already stated in three layers and still slips, which is exactly why the fix chosen this session was a shown specimen rather than a fourth statement. Adding cadence to three more files would be doing the thing that has demonstrably not worked, and it would make [communication-rules-untestable-here] worse, since every additional layer masks the others and nothing can then be attributed.

The one limb that is not repetition is the response-shape tags. `[BRIEF]` and its siblings bound what a *step* outputs, and nothing bounds narration between tool calls *within* a step — which is precisely the thing this entry's rule addresses. That is new coverage rather than another copy, and the capture recommends processing it first.
