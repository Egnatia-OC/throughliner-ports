# 8330209 — the self-resolving date hold extended to captures, so work waiting on the world stops being re-offered every session

Noticed while processing the third item in a row whose only fault was waiting on something outside this project, and worked immediately on Alex's instruction rather than filed for later.

`Not before: YYYY-MM-DD` is the one hold that resolves itself — nobody confirms it and the hooks read it off the calendar. It was available only to an item in Processed, and Processed requires passing the keep check, which an entry with nothing to build cannot do. So the hold designed for *come back later, nobody needs to think about it* was out of reach for exactly the entries that wanted it. Three instances in one session: an audit-programme entry reaching its third skip for the reason both earlier sessions gave, a show-first item re-offered since 1 August against a GitHub issue with no maintainer response, and a Taskflow bridge item filed and deferred within the hour.

Three readers were read before the build was described, and two need nothing. The digest already prints the field on every entry, ungated by section, so an unprocessed date reports correctly today. The session-start hook scopes its date scan to Processed and stays that way, since its facts are about *held* work and a capture is not held. The queue lint skips Unprocessed entirely, so there is no false warning to fix — but its malformed-date check sits behind that same skip, and a date nothing can parse holds an entry forever.

The prior refusal was cited rather than walked past. The skip rule bars a durable marker for skips and bars a file to hold them, as a phantom queue state. What that refused is a record of *Claude skipped this*, written by the session that skipped it; this is a date approved at processing on work waiting on the world. Put to Alex, who ruled the refusal does not reach it. No new state was proposed and must not be — one field reaching one more section is what survives a refusal that has defeated three earlier proposals here.

The item interlocks with the ladder work settled the same session and recorded in `2026-08-19-decay-rung-unreachable-in-practice.md`: the new third rung hands the user the contested entries first, and this field is what lets one genuinely bow out. Neither is sound alone.

**Queue changes:** [not-before-reaches-unprocessed] filed to Unprocessed and kept into Processed; SPEC's shelved-work paragraph rewritten to carry the second meaning.

**Work processed:** kept — [not-before-reaches-unprocessed]. Deleted — none.
