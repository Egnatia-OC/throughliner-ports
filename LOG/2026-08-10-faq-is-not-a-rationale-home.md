# 94bba66 — The self-authoring gate no longer routes evicted rationale to the shipped FAQ

The correction is the user's, in their own words: the FAQ is where frequently
asked questions would live, it is not where rationale lives, it has nothing to do
with this, and it keeps coming up in other sessions too. Claude's contribution was
the grep, the narrowing, and the provisionality note the user then supplied the
reason for.

## Why sessions kept proposing it: the document supplied the argument

The routing lived in exactly one place — `resources/self-authoring-rules.md`, the
first bullet of the audience split under "Rationale lives outside the operative
rule" — confirmed by grep at build, as the item asked. It reasoned that the plugin
package ships neither `LOG/` nor `resources/`, so sending a consumer-facing why to
the LOG does not relocate it but deletes it for everyone not developing the method.
The reasoning is sound on its own premise. **The user's correction rejects the
premise rather than the reasoning:** an evicted why does not need to land anywhere.
Git history keeps it, and anything still needing a decision becomes a capture.

## The wording is narrower than the item's title, deliberately

"The FAQ is not a rationale home" overshoots — an FAQ legitimately answers *why
does the method behave this way* when a user asks, which is what an FAQ is for.
What it must not be is a **destination for eviction**. An FAQ entry is written
because a user would ask the question, never because a rule shed some prose.
Stating it that way leaves the FAQ-sync rule in `CLAUDE.md` standing, which the
blunt form would have read as contradicting.

## The surviving destination is provisional, and that is the point

Routing *why a rule is worded as it is* to the LOG entry that decided it is fine
for now, but it may not survive applying law-writing style to our own prose. The
model the section cites puts reasoning in recitals and explanatory memoranda
**published alongside** the instrument; our LOG is a development record that does
not ship at all. So the LOG is where authoring-why goes because no published-
alongside artifact exists, not because it is the right home. That is written into
the section as an open question rather than a settled one. The artifact is
deliberately not designed here.

**Files touched:** `resources/self-authoring-rules.md`.

**FAQ: not needed because** this governs where the method's own authoring
reasoning goes. What a consumer reads in the FAQ is unchanged — and the point of
the fix is that nothing new gets pushed into it.

**Routed to Captures:** none from this item.
