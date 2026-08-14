# [HASH] — A command offered inside an ask is named in words and never ends the sentence

The desktop app lifts a trailing slash command out of an assistant message and pre-fills the composer with it, so a message ending "…or shall we run /done?" leaves that command sitting in the input box as though the user had typed it, one keystroke from being sent. A user was already caught by exactly that.

This is a compliance fix rather than a new rule, which is what makes it strong. `done.md`'s recommend-next ladder had the same defect and it was fixed for this precise reason: a message ending in a question whose answer looks like a command is one keystroke from being run by accident. That reasoning was written down, it is about this mechanism, and it never reached `plan.md` — which specifies its end-of-queue gate in exactly the offending words while requiring in the same breath that the ask be neutral and not lean toward closing. The doc's stated intent and its own specimen wording were in conflict.

A rule was authored rather than three edits made, and that was the cheaper option refused. Three fixed sites with no rule behind them drift back the next time anyone writes a gate — which is exactly what produced this item, since one site was fixed for this reason and its siblings were not. Correcting three more sites without stating the rule would repeat the failure being corrected.

Three sites reworded: the rung-6 offer, the last-item checkpoint off-ramp, and the neutral end-of-queue gate. Two "say skip, stop, or run /done whenever" recitals were read and deliberately left as they are — they teach the user what the commands are rather than offering one inside an ask, so the rule does not reach them. `done.md` already complies and is the precedent, not a target.

The standing limit is kept from the capture because it bounds the whole item: this shapes the method's prose around a third-party behaviour that is undocumented and can change without notice. It is defensible only because the wording is independently better under the method's existing rules — lead with the decision, one bold ask at the end — and would stand if the suggestion chips disappeared tomorrow. **If a future proposal contorts wording only to steer the chip, that is the line**, and this item is not licence for it.

The useful direction the user found — that the chip is a channel rather than only a hazard, and the recommendation is often what she reads there — stays in scope and is not designed for here.

The report that supplied the three sites came in as INBOX mail from Hexboard. A reply is owed and could not be sent this session: Hexboard's folder is not in the address book and the user could not supply it. The draft is held.

Rule gate: run — amends the message-shape rule with one clause on how a command appears inside an ask, with a named parent, spending no slot. Evidence is three named sites plus a documented precedent fix at a fourth, and a live reproduction inside this project.

FAQ: not needed because this changes the wording of an ask and leaves every option the user has, and every action available to them, exactly as it was. The item flagged the trigger for checking; this is the check.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plugin/throughliner/docs-b/plan.md`.

**Routed to Captures:** none.
