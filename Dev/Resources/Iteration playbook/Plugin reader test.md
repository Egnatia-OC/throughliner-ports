# Plugin reader test

*Experimental. Adaptation of [[Reader test]] for the plugin's shipped artifacts.*

A diagnostic pass that finds comprehension gaps in the plugin's instructions — places where a stranger-Claude, encountering the artifacts through their normal entry points, would misinterpret, guess, or produce wrong behaviour. Produces a ranked gap list, not edits.

## How it differs from the doc-level reader test

The original reader test reads four standalone docs front-to-back as a stranger. The plugin's artifacts aren't encountered that way. A fresh Claude in a consumer project hits them through triggers:

- **SessionStart injection** delivers universal-behaviour.md + a state summary. This is the first (and sometimes only) instruction surface a session-Claude sees before the user speaks.
- **Skills invoke procedure docs** on demand — `/sovbuild` reads `build.md`, `/sovplan` reads `planning.md`. Each procedure doc must be self-contained enough to follow cold.
- **Hook deny messages** surface as tool-use errors during work. They must be clear enough that Claude self-corrects without further instruction.
- **Canonical docs** (DOC-STRUCTURE.md, VOCABULARY.md) are referenced from inside procedure docs. A stranger has to know when to look there and what to look for.

The test question shifts from "can a stranger understand these docs?" to "when a stranger-Claude encounters these artifacts through their normal entry points, does it do the right thing?"

## Trigger

You're about to ship a plugin version that changes instructions Claude reads at runtime — universal-behaviour.md, a procedure doc, a skill handoff, a hook deny message, or a canonical doc. The trigger is an upcoming release to consumer projects, not routine maintenance.

Also useful after a batch of structural changes (new sections, relocated rules, renamed concepts) even if no single change seems large — accumulated drift is invisible until tested.

## What to test

Plugin artifacts that carry instructions a stranger-Claude must interpret:

- `hooks/universal-behaviour.md` — the always-loaded rules surface.
- `docs/procedures/*.md` — demand-loaded procedure docs (11 total).
- `skills/*/SKILL.md` — skill handoff bodies (thin, but the bridge between the user's command and the procedure doc).
- `docs/DOC-STRUCTURE.md` — structural specs referenced from procedures.
- `docs/VOCABULARY.md` — term definitions referenced from procedures.
- Hook deny/inject messages — the text Claude sees when a hook blocks or annotates a tool call (embedded in the Python hook files as format strings).

Not tested: hook Python logic (that's code correctness, not comprehension), templates (those are scaffolding, not instructions), scripts.

## Steps

1. **Prepare a mock project state.** Create (or describe) a realistic consumer project at a specific lifecycle point — e.g. "three builds in, top batch has 4 files, 2 unconfirmed test rows from the previous batch, one OQ." The state doesn't need to physically exist; a prose description is enough for the sub-agents. The lifecycle point determines which artifacts get exercised.

2. **Spawn three sub-agents in parallel.** Each reads the relevant plugin artifacts fresh — no prior context about the method. Each runs a different scenario:

   *Sub-agent A — Routing comprehension.*
   Give it the full text of `universal-behaviour.md` plus a mock tier 3 state summary (the kind SessionStart injects). Then give it 6–8 user openers, one at a time, covering:

   - Test notes from a previous build.
   - A feature request ("I want to add dark mode").
   - A scope question ("Should we support offline mode?").
   - Resume intent ("Let's keep going").
   - An ambiguous opener ("Hey, I was thinking about the settings page").
   - A cold start (template-state docs detected in the state summary).
   - An opener when unconfirmed test rows exist in the state summary.

   For each opener, ask: what route does this take? What procedure doc would you read? What's the first thing you'd say to the user? Instruct the agent to say "the instructions don't cover this" rather than guessing. End with a list of ambiguities, contradictions, or missing routes.

   *Sub-agent B — Procedure walk-through.*
   Give it one procedure doc (pick the most recently changed, or rotate across test runs). Also give it `DOC-STRUCTURE.md` and `VOCABULARY.md` as reference material, and the mock project state. Ask it to narrate, step by step, what it would do from invocation to completion — including what it would load, what it would write, and what it would say to the user. Instruct it to flag every moment it has to guess, interpret ambiguously, or can't find the answer in the docs it was given.

   Good procedure docs to test (rotate):
   - `build.md` — the most complex, highest-stakes procedure.
   - `close.md` — many steps, cross-references, two-turn structure.
   - `planning.md` — long, branching, with sub-procedures.
   - `setup.md` — four cases, migration logic.

   *Sub-agent C — Boundary enforcement.*
   Give it `universal-behaviour.md` + `build.md` + the mock project state. Throw 5–6 scenarios that test boundary rules, one at a time:

   - "Edit UX.md to fix a typo I noticed" (during build phase).
   - "While you're in that file, clean up the naming" (out-of-scope refactor).
   - "Add this feature too, it's small" (feature not in batch).
   - "Skip the test log, I trust it works" (test-confirmation gate).
   - "Just commit, we don't need the close steps" (skipping `/sovclose`).
   - A genuine prerequisite carve-out situation.

   For each scenario, ask: what do you do? What rule applies? What do you say to the user? Instruct it to produce the actual response it would give, then reflect on which rules it applied, which were unclear, and which moments it had to guess.

3. **Synthesize.** Cluster findings from all three sub-agents into a single deduplicated gap list, ranked by impact:

   - **Top tier:** comprehension gaps that would cause wrong behaviour in a real consumer session — a stranger-Claude would do the wrong thing, not just be confused.
   - **Middle tier:** ambiguities a stranger-Claude could resolve by guessing correctly, but shouldn't have to.
   - **Bottom tier:** wording issues, redundancies, missing cross-references that don't change behaviour.

4. **Confirm before acting.** Present the ranked gap list in plain English. Wait for okay. Don't start editing on the list alone.

## Output

A ranked gap list with three tiers. Top-tier gaps are weighted toward the most recent plugin changes — gaps in newly changed artifacts matter more than gaps in stable ones.

## When wasted

- The plugin's instruction surfaces haven't changed since the last test.
- No consumer-project sessions have happened since the last test (no downstream signal to weight findings against).
- You're about to change the artifacts anyway — test after the change, not before.

## Refinements

- **Rotate the procedure doc in Sub-agent B** across runs. One procedure per test; cycle through build → close → planning → setup over successive iterations.
- **Save the gap list as a file** in `Dev/Planning/` or the test-log, not just in chat. Plugin reader test findings are inputs to the next plugin version cut.
- **Run in a separate session from any fixes.** Same rationale as the doc-level reader test — sleeping on the gap list reduces over-fixing.
- **The mock project state matters.** A bare mock (fresh project, no history) exercises setup paths but misses the mid-lifecycle artifacts. A rich mock (multiple builds, test rows, OQs, red flags) exercises the full surface. Default to a rich mock.
- **Sub-agent A's opener list is the most valuable knob.** The routing table is the highest-traffic instruction surface — every session hits it. If you only have time for one sub-agent, run A.
- **Hook deny messages are hard to test via sub-agents** because they're embedded in Python format strings, not standalone docs. A complementary approach: collect the deny message templates from the hook files, present them to a sub-agent as "you just received this error while trying to edit a file," and ask what it would do next. This tests the deny-message-as-instruction surface.

## Relationship to E2E testing

E2E tests run the plugin against a real project (Taskflow) and observe runtime behaviour — whether hooks fire, whether skills produce correct output, whether the lifecycle works end to end. The plugin reader test is complementary: it finds *comprehension* gaps that E2E can miss. A hook can fire correctly and still contain instructions a stranger-Claude interprets differently than intended.

E2E catches: code bugs, integration failures, missing hook triggers.
Plugin reader test catches: ambiguous instructions, contradictory rules, missing guidance, unclear cross-references.

Run both. Neither subsumes the other.

## The prompt

Open a fresh session in the "No code method" project. Copy the prompt below. Replace `<PROCEDURE>` with the procedure doc you want to test (default: `build.md`). Paste and send.

---

Run a plugin reader test on the no-code-method plugin's shipped artifacts. The goal is to find comprehension gaps — places where a stranger-Claude, encountering these instructions for the first time in a consumer project, would misinterpret them or produce wrong behaviour. Don't edit anything — find the gaps, present them, get my okay.

**Mock project state.** A consumer project three builds in. BACKLOG has one queued build batch (4 files, goal and scope context filled). Two unconfirmed test rows from the previous build. One open question surfaced 8 sessions ago. No red flags. UX.md has 6 functionalities and 3 principles. MANIFEST has 12 entries. Method version footers match the plugin.

**Step 1: spawn three sub-agents in parallel using the Agent tool.**

*Sub-agent A — Routing comprehension.*
Read `plugin/hooks/universal-behaviour.md` fresh. Compose a mock tier 3 SessionStart state summary matching the project state above (use the format from `plugin/hooks/session_start.py` → `build_state_summary`). Then process these openers one at a time:

1. "Here are my test results from last session — settings toggle passed, but the export button is misaligned."
2. "I want to add dark mode support."
3. "Should we support offline sync? I keep going back and forth."
4. "Let's keep going from where we left off."
5. "Hey, I was thinking about the settings page."
6. (Pretend the state summary showed template-state docs detected.)
7. (Note the 2 unconfirmed test rows in the state summary — what happens before anything else?)

For each: what route? What procedure doc? What's the first thing you'd say? Say "the instructions don't cover this" rather than guessing. End with a list of ambiguities or contradictions.

*Sub-agent B — Procedure walk-through.*
Read `plugin/docs/procedures/<PROCEDURE>` fresh, plus `plugin/docs/DOC-STRUCTURE.md` and `plugin/docs/VOCABULARY.md`. Using the mock project state, narrate step by step what you'd do from invocation to completion. Flag every moment you have to guess, interpret ambiguously, or can't find the answer.

*Sub-agent C — Boundary enforcement.*
Read `plugin/hooks/universal-behaviour.md` and `plugin/docs/procedures/build.md` fresh. Using the mock project state (assume you're mid-build, 2 of 4 files ticked), process these scenarios one at a time:

1. User: "Fix that typo in UX.md while you're at it."
2. User: "Clean up the variable names in that file too, they're messy."
3. User: "Actually, add the notification badge feature too — it's tiny."
4. User: "The other tests are all fine, just mark them passed."
5. User: "Just commit now, skip the close stuff."
6. You discover you need to edit a utility file that isn't on the Files: list to make the current file work.

For each: what do you do? What rule? What do you say? Produce the actual response, then reflect.

**Step 2: synthesize.** Cluster findings into a single deduplicated gap list:
- **Top tier:** would cause wrong behaviour in a real session.
- **Middle tier:** ambiguous but survivable.
- **Bottom tier:** wording, redundancy, missing cross-refs.

**Step 3: confirm before editing.** Present the ranked gap list. Wait for my okay.

---

## Notes

- The mock project state is deliberately mid-lifecycle (not fresh, not late-stage) because that's where the instruction surface is widest — routing, procedure docs, boundaries, and cross-references are all in play.
- The stranger framing matters more here than in the doc-level test, because the plugin's artifacts arrive through injection and demand-loading — a stranger-Claude never sees the full picture at once.
- Sub-agent A (routing) has historically been the highest-yield scenario in the doc-level test. Expect the same here — the routing table is the most-used instruction surface.
- Consider adding a fourth sub-agent for hook deny messages once the format stabilises. Collect deny templates from `pre_tool_use.py`, present them as "you received this error," and ask what the agent would do next.
