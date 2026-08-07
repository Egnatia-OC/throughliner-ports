# [HASH] — Added a claim-provenance clause: a capability claim in a project doc names its evidence, or is read as unverified

A session concluded that Claude could run Gradle in a project and wrote the recipe into that project's CLAUDE.md as settled fact. The evidence was `gradlew --version` succeeding — the one Gradle command that does not open a selector, so precisely the command that cannot detect the failure. A later session built a work item on the recorded fact and it collapsed the moment it ran.

The method already carried the rule this violates — *"'It ran' and 'it worked' are different claims"* — and the rule was in force and slipped anyway. That makes this the third recorded instance of a clearly-worded loaded rule failing under local pressure.

**The compounding half is the part worth designing against.** The failure was not believing a false positive; it was **writing it into a project doc as settled fact**, where it outlived the session, was inherited without provenance, and became the premise of queued work. A wrong belief inside one session is cheap. A wrong belief promoted into the record cost two sessions here.

So the fix is one clause, not a form or a field: a capability claim written into a project doc names, inside the same sentence, what was run and what it showed. Two things follow and both are stated as the rule — a reader can see what the basis actually was and judge it, and **a claim recorded without that clause is read as unverified**, which is what actually stops the next session building on it. Today a conclusion and a tested fact look identical on the page forever, and that indistinguishability is the whole defect.

Scoped to capability claims deliberately, not to every fact in a project doc, which would be a documentation tax paid on every sentence to catch a rare failure. The trigger is narrow and recognisable: an assertion about what this environment or tool can do — exactly the class that becomes the premise of queued work.

**The mechanical option was checked and does not exist here**, rather than being assumed away. The sibling item where a loaded rule kept slipping was fixed by *removing the pressure* — giving the safe path a cheap tool. That shape does not transfer: nothing made writing the false fact cheaper than testing properly, so there is no pressure to remove, and no hook can inspect whether a claim is true. Recorded so a later pass does not re-open it and re-derive the same negative.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
