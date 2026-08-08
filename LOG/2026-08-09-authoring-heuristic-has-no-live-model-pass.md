# [HASH] — The authoring heuristic's 4.8 pass deleted and its three model-agnostic checks promoted, leaving a doc that is true rather than one carrying a tombstone

The capture that produced this item asked for a 5-series authoring pass to be
written. Processing reversed the direction to a deletion, and the build carried
that out.

**The premise the capture rested on was false, and the true state was worse.**
The capture said the 4.8 section "is now marked historical — correctly". It was
not marked at all. `resources/authoring-heuristic.md` opened by stating "The
current target is Opus 4.8 (see CLAUDE.md Model target)", and the section itself
opened "Every session here runs on Opus 4.8." The historical framing existed only
in CLAUDE.md — which is not the file anyone opens at authoring time. So the
artifact actually consulted read as entirely live, and anyone following it would
apply a checklist tuned to a retired model, pushing new text back toward the
heavier register the docset-A retirement had just removed.

**Why subtraction rather than a replacement section.** All seven 4.8 checks split
cleanly at processing. Three are not model-specific at all — lead with the
decision and gate the detail, show the shape with a one-line exemplar rather than
describing it, and guard against over-terseness. Two of those three are already
stated in `docs-b/plugin-behaviour.md`, which is itself the evidence that they are
universal rather than tuned. The other four — quantify the target instead of using
an adjective, state the scope in words, name the verbosity pattern to kill, write
it as an action not a prohibition — are prescription-*adding* by design, which is
precisely what the 5-series wants less of. Keeping them live would have worked
against the docset the method now ships.

**A 5-series pass was deliberately not written, and the reasoning is worth
keeping** because the intuitive move is to write one. Two reasons. The thing that
would establish need — the adherence-measurement harness — was consciously waived,
so a new pass would be authored from published guidance and impression exactly as
the 4.8 one was, with no way to tell whether it helped. And the method's live
problem is that its documents only ever grow, so replacing a dead section with a
speculative new one is the growth pattern rather than a fix for it. The raw
material stays banked in `resources/research/opus-5-instruction-compliance.md` and
`fable-5-instruction-compatibility.md`, and the audit plan now records that the
authoring-compliance lens returns as a pass if one is ever written.

**What is genuinely lost, stated rather than glossed.** SPEC's position is that
the method *is* model-tuned prose, and after this there is no written account of
what the current models steer on. The honest answer is that there has been no such
account since the retirement anyway — this only stops the document pretending
otherwise. The three promoted checks are the part that was carrying real weight.

The doc went from 61 lines to 44, and its opening now says plainly that there is
no per-model pass and why.

**Files touched:**
- `resources/authoring-heuristic.md` — opening two paragraphs rewritten; new "The three checks — run these over any authored method text" subsection carrying the three promoted checks with their worked good/bad examples; the "4.8 — the authoring pass" section deleted outright.
- `CLAUDE.md` — the authoring rule collapsed from a long paragraph explaining that half the doc was historical to two sentences pointing at it.

**Routed to Captures:** none from this item.

**FAQ:** not needed because this doc is a host-only development artifact that never ships in the plugin package, so no consumer meets it.
