# cc33c1e — The bracketed name is explained once in the queue header, and every slug shown to the user now carries what its item is for

**Why this was worth doing.** The user captured it in her own terms: she had never
actually known what the bracketed part of the title was for — it just randomly emerged
one day and she didn't have time to deal with it. The slug is load-bearing structure:
it is what `Blocked by:` resolves against, what the queue lint checks, what a LOG entry
names to say which item it built, and what Claude uses to refer to an item exactly in
chat. None of that was stated anywhere she reads. It appeared in her own documents and
she worked around it for weeks.

**Why "harmless to ignore" is not an answer.** It is harmless to ignore only once you
know you may. Until then it is unexplained structure in a document the user is asked to
read and approve, and the method's own standard is that unreadable is unapprovable.

**Two halves, at opposite ends of the same subject.** The notation is explained once, in
the queue header `/setup` authors, where anyone opening the file meets it — what the
bracketed name is for, and that the user never has to write one. Then each *use* stops
being opaque: the always-loaded vocabulary rule's in-passing/explained table gains a
third arm requiring a slug shown to the user to carry what that item is for on its first
appearance in a message.

**Scope is output, never documents** — the same split
`[two-column-fences-wrap-unreadably]` settled the same day. Inside queue prose slugs
stay bare: the always-loaded rule deliberately requires citing items by slug there, that
text is read by Claude, and glossing every citation would inflate the entries this queue
already struggles with.

**First use per message, not per chat**, and the alternative was refused explicitly: per
chat is readable only to someone holding the scrollback in their head, which is the
assumption being objected to. The cost is a clause each time, stated rather than
presented as free.

**The parent is the vocabulary rule**, which already asks whether a term is used in
passing or explained and already lists a dozen internal terms to translate or omit. **A
slug cannot simply join that list** — omitting it loses the one handle the user has on
an item — so it is a third arm on an existing table rather than a freestanding rule. A
second queue item for the presentation half was refused: two entries on one notation
would answer the same question twice.

**One cost stated rather than discovered.** The header clause reaches new projects only.
An existing project's queue header is the user's own text and the migration is barred
from rewriting user prose, so for those users the FAQ entry is the whole answer.

**Files touched:** `plugin/throughliner/docs/setup.md`,
`plugin/throughliner/docs/skill-nonspecific-rules.md`,
`plugin/throughliner/templates/faq-template.md`,
`plugin/throughliner/templates/faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none from this item.

**FAQ: updated** — new entry, "What is the short name in square brackets at the end of
each queue item?" It answers that it is a handle, that the user never writes one, that
it stays stable across rewording, where it shows up (session records, waiting
relationships, chat), and that Claude naming one without explaining it is Claude getting
it wrong.

Rule gate: run — admitted as a third arm on the always-loaded vocabulary rule's existing in-passing/explained table, subordinate rather than freestanding. **Nothing is evicted, stated plainly rather than dressed up as a merge of rules.** Failure evidence is four instances, two of them the user's verbatim words. **A hook was considered and refused: nothing mechanical reads Claude's chat output** — the same finding reached independently by [two-column-fences-wrap-unreadably] hours earlier, which is what makes it a property of the surface rather than of either item.

Depth: short. Built and confirmed.
