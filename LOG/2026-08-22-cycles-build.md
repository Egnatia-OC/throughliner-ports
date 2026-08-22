# c904687 — Cycles shipped: due-ness checks at plan/next/done, keep-step authoring route and one-time suggest clause, FAQ entry

The user's concept, raised 2026-08-22 in the planning session; the definitions/position split is Claude's. A user can put an artifact on a cycle — recurring work with its own rhythm, independent of the work cycle's — by defining it once: posts, articles, videos, and this project's own release timing were her examples. Her framing set the constraints: no new skill, a template-like concept, checks at the openings and closes for what cycles exist and where each is up to.

The design as built: definitions live in `CYCLES.md` at the project root, created by /plan the first time one is asked for — a project with no cycles has no doc and pays nothing. Position is never stored (the board and merge-cycle failures, plus rule_signals' nothing-is-stored rule, are the grounds); each definition names the artifact, the steps of one turn, the cadence (declared or derived — the definition says which), and the observable that marks a completed turn. The three sites — plan.md's opening, next.md's pre-flight, done.md's wind-down — read the definitions and compute due-ness from the observable, filing one capture per due step, satisfied while an open capture with its slug exists, so due work enters the queue rather than standing on a board nobody reads. /next and /done file only; /plan is the one site that also processes. At the user's instruction, added before close: the keep-step offers a cycle once where an item is recurring-shaped, in the item's own message, never as a turn of its own — suggestion only, creating one stays the user's call.

Refused, carried from processing: a new skill (her call), stored position (a state file the first forgetful session makes lie), a standing board of cycle positions (the notice nobody is obliged to read).

Tick: done, UNCONFIRMED: the one-capture-across-repeated-checks behaviour needs a live session with a hand-made CYCLES.md carrying a past-due observable — this project has none, so only the no-doc silent path is exercised.

Rule gate: run — a new fetched-doc mechanism plus one check clause at each of the three sites and one suggest-clause at the keep-step; the doc is fetched on a named trigger (its own presence), so nothing joins the always-loaded set; nothing is displaced at the three sites and that is stated rather than hidden; the file-a-capture pattern is copied from rule_signals rather than invented.
FAQ: updated — "What is a cycle?" entry and its index line added to the templates; FAQ/ re-copied byte-identical.

**Files touched:** plugin/throughliner/docs/plan.md, plugin/throughliner/docs/next.md, plugin/throughliner/docs/done.md, plugin/throughliner/templates/faq-template.md, plugin/throughliner/templates/faq-index-template.md, FAQ/faq.md, FAQ/index.md
**Routed to Captures:** none
