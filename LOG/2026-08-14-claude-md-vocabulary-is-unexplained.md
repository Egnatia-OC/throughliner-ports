# [HASH] — The background-only vocabulary list is recast around one test: does the term name something in this user's world, something you could show them

Captured by Alex on 2026-08-13 by repeatedly having to ask what the words meant.
Over one session she asked, in her own words, what a disposition is, what a gate
is, what the board is and why it is called that.

**The site is not the document, and she corrected this at processing.** The
complaint is not about reading `CLAUDE.md` — it is Claude carrying these terms into
conversation. Glossing first use inside a Claude-facing file fixes nothing, so that
limb was dropped. Counted at processing: `rung` appears in `CLAUDE.md` zero times
and only in the shipped `plan.md`, which confirms the diagnosis — she met the word
because /plan *said* it while narrating its ordering, not because she read it.

**Three proposals were defeated on the way to the fix, and each is recorded so it
is not re-proposed.** (1) First-use explanation, rejected in her words: it has been
explained many times and she still does not get it. Every explanation offered,
including one in that session, was a definition — swapping the hard word for a
longer sentence. Nobody had opened a LOG entry and pointed at the actual line, and
for a word whose whole meaning is "that line, there", a definition is the one form
that cannot land. (2) A ban, proposed by Claude and defeated: `gate` was already on
the background-only list and was said repeatedly in the very session that filed
this, so the list is demonstrably insufficient — and her objection goes further,
that these are the project's own words. `disposition` names a real line sitting in
her LOG entries, so refusing to say it leaves the word in her files unexplained,
waiting to be met alone. (3) A two-category split of scaffolding terms versus
artifact-naming terms, also Claude's and also defeated, on self-hosting: in this
project the procedure *is* the subject matter, so `pre-flight` names a doc section
she can open here and nothing at all in a recipe app. The same word would get
opposite answers in two projects, so the category cannot be a property of the term.

**Decided: one test replaces the list's implicit one.** Does the term name
something in *this* user's world — something they could be shown? Where it does
not, it stays unsaid, which is what the old list achieved for consumer projects.
Where it does, saying it is right, and what is owed the first time is **being shown
the thing** rather than given a definition: open the file, point at the line, then
use the word. This dissolves the self-hosting contradiction rather than carving an
exception for it.

**Confirmed live minutes after it was processed.** In the same session Claude used
the word "checkpoint" — its internal name for the message handing her the next item
— and she replied that she did not know what it meant. The defect occurring inside
the conversation that had just settled how to fix it is the strongest evidence
available that a rule alone will not carry this.

**A stop-hook check was raised and dropped.** Banned vocabulary in finished output
is genuinely a literal string match, so unlike most of this method's judgement calls
a hook could detect it — but with the ban itself defeated there is nothing left for
it to enforce.

**Rule gate: run** — a recast rather than an addition. The existing list is
repealed and replaced by one text built on a single test, so the section's rule
count does not rise; the show-it-once obligation is subordinate to that test,
written as its "yes" arm. The old list survives inside the "no" arm as typical
examples rather than as the rule itself, which is what lets the test rather than the
enumeration do the deciding — the enumeration demonstrably could not.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none.
