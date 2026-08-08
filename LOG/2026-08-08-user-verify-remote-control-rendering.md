# c4cf5af — Both remote-control rendering checks answered: fences don't wrap there, chips didn't appear on either surface

Walked through with the user during a /next run. The item's design paid off in a way worth recording: it was written to be run *opportunistically*, with no special trip, and it was — the user happened to have both surfaces in front of them (watching on a phone while at the computer), which made the comparison simultaneous rather than remembered.

**Check 1 — fence wrapping. Answered, and it is the narrowing outcome.** A ~300-character single sentence in a plain fence **ran off the side on the phone and wrapped on the desktop**. The split was confirmed explicitly with the user before being recorded, after an initial exchange where "no wrap" and "it is wrapping on desktop" arrived in sequence and could have been read either way — the confirmation cost one question and prevented a wrong finding being written into a rule's fate.

So the prose-never-in-a-fence rule **keeps its reason, corrected rather than repaired away**. Its stated justification — "fences don't wrap in the app" — is false at the desk and true on remote control, which is precisely the surface the original failure happened on: a long draft a user on remote control could not read the end of. Of the three outcomes [fences-wrap-so-prose-rule-reason-is-false] enumerates, this is the second. The rule is not deleted and not re-founded on readability; its reason narrows to name the surface.

**Check 2 — suggested replies. Answered, and it confirms the safe direction.** No chips on the phone, and none on the desktop either (evidenced by a screenshot of an empty input box). The method's assumption — that the reply suggestions cannot be relied on, so every stop must name both replies in its own text — holds.

This does **not** overturn the "chips appear sometimes, unpredictably" finding recorded earlier the same day, when a chip did appear at the desk and was clicked by accident. A chip present once and absent later is what unpredictable means. If anything the pair strengthens the rule: the same surface produced both results within a day, so nothing may assume the suggestions are present, and nothing may assume their absence is stable either.

**What came out of it beyond the two answers.** The user reframed the wrapping difference as a bug rather than a preference — the two surfaces disagree, so the same message is readable on one and not the other — and it was filed as **anthropics/claude-code#84965**. It went up first as a feature request for a copyable prose block, and was rewritten in place within minutes once the user corrected the framing. That reframing is the user's, and it is better than the one Claude drafted.

The same conversation produced [copy-affordance-correction-too-strong-on-mobile]: the behaviour rules currently assert that people simply select the text they want and copy it, which the user's own experience contradicts on a phone. Both that clause and the wrapping claim it sits beside were written from the desk, which is the pattern worth noticing rather than either instance.

**Files touched:** none — this item produces knowledge. `QUEUE.md` records the answers, on this item and on the one it unblocks.

**FAQ:** not needed because nothing shipped and no behaviour changed — the findings confirm two existing rules rather than altering them. The rule change they enable is queued, and the FAQ question rides that build if it needs one.

**Routed to Captures:** [copy-affordance-correction-too-strong-on-mobile].

**A note for the item this unblocks.** [fences-wrap-so-prose-rule-reason-is-false] carries the answer in its own block now, and its `Blocked by:` line was deliberately left in place: this item is complete, but lifting an item's readiness is /plan's call rather than /next's or /done's. It is ready for a planning session to lift.
