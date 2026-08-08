# [HASH] — The project glossary built: GLOSSARY.md scaffolded at /setup, the vocabulary rule rewritten around define-and-record, and the mirroring correction

The largest item of the run, and the only one consumers meet directly. Three
threads, one design — the glossary is the mechanism the other two need.

**The core mechanism is a check, not a document.** When a general term is used, it
gets defined at the point of use and then added to GLOSSARY.md. Membership is what
decides whether a term needs explaining at all: in the glossary means already
explained, use it freely; absent means define it now, then record it. The user's
framing of why this matters — before, Claude had no way of knowing what the user
might know; now it at least knows what has been explained to them before.

**The two-sided guarantee is kept as the feature's plainest statement**, in the
words from the launch announcement: *Claude never re-explains what you know, and
never assumes you know what it hasn't told you.* Both halves are load-bearing — the
first is the anti-nag direction, the second the anti-stranding direction, and one
record delivers both.

This **extends** the existing vocabulary test ("would the user have met this word in
something they actually read?") rather than replacing it. An explained term is one
they have met; the glossary is what makes that checkable across sessions instead of
held in one session's memory.

**The two-axis distinction, named this way at the user's correction.** Project-specific
terms are the project's own naming set — canonical, always usable, with the glossary
as the authority on which name is canonical when two are in circulation. General
terms come from the wider world and are governed by define-and-record. The first cut
was "in-project / out-of-project" and it was wrong: a general term is still
technically *in* the project the moment it gets used, so the axis is where a term
comes from, not where it appears. Term drift happens in both the AI and the human,
and words don't get caught at their many statement sites — so the glossary also gives
the ripple-grep discipline a known index of names to work from, which is what a
corpus-wide rename would need.

**How entries work, which is the user's design and the part most likely to be
"corrected" later by someone who thinks a glossary should be authoritative.** An
entry carries the explanation **as it was last given to the user** — mirroring what
they might actually remember, not a textbook definition. Each re-explanation may be
worded however fits the moment, and after explaining a term Claude updates its
entry, developing the definition rather than necessarily replacing it. Entries stay
terse. Update-after-explaining is also the staleness answer: explaining *is* the
trigger, so the record cannot fall behind the conversation.

**The mirroring-correction rule.** Models mirror the human, so a not-quite-right
technical term gets absorbed and repeated indefinitely. Where the user *chooses* a
nonstandard term — especially with reasoning — it goes in the glossary with that
reasoning as a deliberate project-specific term and is then simply correct. Where
they have used the wrong word for a real technical thing, silently adopting it
leaves them exposed in professional settings, so Claude names the standard term
once, plainly, then just uses it: no correction ritual, no repeats. The glossary
entry is what stops re-correction.

**The four design calls, all approved at processing.** Its own file, `GLOSSARY.md`,
beside SPEC.md and QUEUE.md, and **committed** — unlike the FAQ, it is the user's
own record of what has been explained to them, not a copy of the plugin's help. It
**ships to consumers now**, scaffolded by /setup; the mechanic stands alone without
[learning-mode-fork-at-setup], and consumers are its point. Existing projects get it
via the migration path when [setup-as-migration-home] lands, and until then a
missing GLOSSARY.md simply means the check treats every term as unexplained, which
is safe. And it joins the always-editable set plus the planning quiet-list, because
define-and-record fires unpredictably in any session type and a build's agreed file
list cannot anticipate it.

**That last call made this a hook-enforced-set change, so the build ran the required
grep over every statement site of the always-editable set before finalising the file
list.** Six sites were edited — the hook's module docstring (rules 1 and 4),
`_is_method_doc()`, `_is_plan_quiet_path()`'s docstring, the no-files denial message,
the behaviour rules' Scope section, plan.md's quiet-list, next.md's two sites,
SPEC.md's bullet, and the FAQ entry describing the lock. Two hits were left alone
with reasons: the hook's note that FAQ/ is deliberately *not* in the always-editable
set (still true, and about FAQ/ rather than the glossary), and the behaviour rules'
retired-"method docs" paragraph (which names the set as a concept and lists no
members). Both hook test suites passed afterwards.

**One tension carried from the record so the build didn't rebuild a retired thing.**
The vocabulary rule deliberately retired an enumerated banned-word list, because a
list is only ever complete for the past. The glossary is not that list reborn — it
is positive content, canonical names and explained terms, never an enumeration of
forbidden words. The test stays the rule; the glossary is its memory. The rewritten
rule says so explicitly.

**One scope note, stated rather than glossed:** `templates/CLAUDE-TEMPLATE.md` was
edited without having been named in the item's file list. It carries the project-docs
list every consumer receives, so leaving it would have shipped a template describing
three docs where /setup now scaffolds four. A legitimate widening, but it should have
been narrated in one line at the moment it was added, and it wasn't.

**Files touched:**
- `plugin/si-plugin/docs-b/plugin-behaviour.md` — the Vocabulary section rewritten as "the test, the glossary, and the two kinds of term", gaining the two-axis split, define-and-record with the guarantee, how entries are written, the not-the-banned-list note, and the mirroring correction; Scope section's always-editable list.
- `plugin/si-plugin/docs-b/setup.md` — four project docs rather than three; the GLOSSARY.md scaffold step with its committed-not-gitignored reasoning and the don't-pre-populate instruction.
- `plugin/si-plugin/templates/GLOSSARY-TEMPLATE.md` — new.
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` — project-docs list.
- `plugin/si-plugin/hooks/pre_tool_use.py` — always-editable set and its four statement sites.
- `plugin/si-plugin/docs-b/plan.md` — quiet-list.
- `plugin/si-plugin/docs-b/next.md` — two always-editable statement sites.
- `SPEC.md` — four project docs, the GLOSSARY.md entry, the always-editable list.
- `README.md` — a glossary paragraph in "What it does".
- `FAQ/faq.md`, `FAQ/index.md` and their shipped templates — a new entry.

**Routed to Captures:** none from this item.

**FAQ:** updated — new entry "There's a GLOSSARY.md in my project. What is it, and do I have to fill it in?", written into both the shipped templates and this project's local copy, with its index line.
