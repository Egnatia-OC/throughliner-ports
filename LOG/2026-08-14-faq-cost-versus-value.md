# 78fa417 — The FAQ is kept and its sync gate narrowed to changes that alter what a user does

Captured by the user, in her own words: now that we have the build cycle in every skill, she doesn't know that the FAQ is needed any more, and it's expensive to maintain.

The cost half of that is real and was the sharper argument. FAQ-sync is a hard close gate: a session carrying a user-facing change could not close until the FAQ was dispositioned in its session record. That is a tax on every session, and a separate open item records that this project's own FAQ and the shipped template have drifted apart with the authoring rule pointing at only one of them. So the gate was expensive and, on that evidence, not achieving what it cost.

**The redundancy half was contested by Claude and lost on its own terms, which is recorded because it is the intuitive position.** The claim was that the work-cycle block and the FAQ have different readers: the work cycle is orientation Claude reads and never recites, while the FAQ is the consumer's own document. The technical-writing literature's answer is that a distinct reader is *better* served by the answer living in context — so the argument supports relocating the content rather than keeping the format.

**The research was commissioned and then departed from, deliberately.** `resources/research/faq-as-a-document-type.md` found the mainstream position — GDS, A List Apart, passo.uno, independently over more than a decade — to be against having a FAQ at all, because the format produces the failure. Three of its four recurring findings already described this project: FAQs come from needing somewhere visible to put pressing questions rather than from a deliberate choice, duplicated content falls out of sync, and the page becomes a dumping ground.

**The decision is the user's, in her own words: consumer-facing explanation lives in the FAQ.** The literature's remedy is that an answer belongs where its subject is explained — and here there is no such place for a consumer, because the procedure docs are Claude's rather than theirs. So for this method the FAQ *is* the context, and the sources' central objection does not bite in the same way. Anyone revisiting this should argue with that reasoning rather than re-citing the research, which was read and weighed.

**The tension that creates was stated rather than glossed.** Making the FAQ canonical means its maintenance cost stays; it cannot be both the place answers live and a document nobody tends. So the saving had to come from the **gate**, not the document.

The gate fired on any user-facing change, which is nearly every change. It now fires on changes that alter **what a user actually does** — a new step, a changed command, something different appearing in their own documents, a moment where they must answer or decide. A change that is user-visible but leaves their actions unchanged no longer fires it. It keeps its teeth, staying a hard close gate with a required artifact, and loses most of its firing rate. The batch-authoring FAQ rule was rewritten to the same words so both narrow together rather than drifting.

Deliberately out of scope: the divergence between this project's FAQ and the shipped template stays its own item. That is a repair, and folding it in would mix a rule change with a content fix.

Rule gate: run — admitted as a narrowing of an existing rule rather than an addition. Nothing new is admitted and no slot is spent; the trigger's scope shrinks, which is eviction-shaped. Not hookable — "does this change what the user does" is judgment, which is why the gate rides the close's read, and that reasoning is unchanged.

**Files touched:** `CLAUDE.md` (the FAQ-sync gate's trigger and the batch-authoring FAQ rule's test). Host-only: consumers never author FAQ entries.
**Routed to Captures:** none
