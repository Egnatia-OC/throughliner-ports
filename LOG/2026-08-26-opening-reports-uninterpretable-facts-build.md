# [HASH] — Session openings now name the hash backfill as what it is, instead of reporting a count nobody could interpret

The instance behind this: an opening said nine LOG entries carried uncommitted changes from a previous session. It read as alarming, nothing in the message explained it, and Alex went back to another session to find out — where it was correctly identified as the automatic hash backfill. `done.md`'s staging step has carried recognition for that exact signature all along; the openings had no equivalent, so the same facts arrived as a bare number with no reading attached.

The hook now separates them. Every uncommitted `LOG/` file whose entire diff is a placeholder becoming a real hash — matched one-for-one, same line shape, same text either side — is reported as the automatic backfill and as normal. Everything else keeps the plain count and the existing wording. Mixed changes produce both lines, which is what the acceptance asked for.

The reading is strict on purpose and fails in the safe direction: any file where something else changed alongside the hash falls back to the plain count rather than being called routine. `_dirty_tree_count()` came out with its last caller.

**The generalisation was refused at processing and that refusal stands** — "explain any fact you cannot interpret" is untestable judgment, which is the defect this pair of items exists to remove. Further signatures earn recognitions one at a time as they are found.

Files touched: `plugin/throughliner/hooks/session_start.py`, `resources/testing/test_session_start_uncommitted_changes.py` (new)
Routed to Captures: none
Rule gate: not needed — hook behaviour, no method rule text.

Verified by a new suite built over real git repositories: a pure backfill is recognised, a hash filled alongside a prose edit is not, a heading retitled with the placeholder left in is not, mixed changes separate, and a clean tree reports nothing. All session_start suites pass. Depth: short. Ticked as done, confirmed.
