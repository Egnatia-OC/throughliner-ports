# f832385 — Select the docset from a recorded model setting, since the payload's model field never arrives in the desktop app

The live check ran and failed: with the hook's injection working, the payload contained no docset directive anywhere in 92,112 characters, so the fallback fired and docset A loaded on an Opus 5 session. The whole of phase 2 was inert.

Two of the three possible causes were ruled out at processing, so this build didn't re-check them: `docs-b/` is present in the installed host, and the classifier is sound. The decisive finding was the documented contract, which had never been read — only SessionStart hooks can receive a `model` field, its presence is **not guaranteed**, and there is no environment-variable equivalent. So this was never a bug to fix but a premise to replace: even if the field appeared tomorrow, it cannot be depended on. The hook's own docstring already cited the project's research saying so, and phase 3 was built on it anyway, which is worth recording because the same shape can recur.

The replacement is a project setting, and the sources are **layered** rather than swapped: the payload's `model` field wins where it arrives (it's ground truth about the running session), then a `Model:` field recorded in CLAUDE.md, then docset A. Layering costs nothing, keeps working automatically wherever the harness does supply the field, and never weakens the no-strand guarantee. /setup asks which model the user runs — something they know — never which docset they want, which is background machinery they should never meet.

One thing nearly reproduced the bug being fixed. The family regex was anchored on a hyphen, matching `claude-opus-5` but not the recorded answer `Opus 5` — so every human answer would have failed to parse and silently fallen back to docset A. The separator was loosened, and the reason is written into the code so it isn't tightened back.

The payload is also now recorded once to a research file, as the original capture asked: it distinguishes an absent field from a malformed one after the fact, and is nearly free.

Verified live: this project's payload now carries the docs-b directive, where before it carried none. It also measured **54,666 characters**, not the 3,524 that [session-start-payload-oversized-and-misordered] predicted — that item assumed docset B replaces the inlined rules with a pointer, and it does not. The size question survives this fix rather than dissolving with it, and the item was annotated with the measurement rather than left to mislead.

SPEC's two-docsets paragraph promised the pick happens "with nothing for the user to configure or notice." That stopped being true and was rewritten in the same change, including why the one small configuration exists.

**Files touched:** `plugin/si-plugin/hooks/session_start.py` (source layering, the loosened family regex, the payload recording), `plugin/si-plugin/docs-b/setup.md` and `docs/setup.md` (the new question), `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` and `CLAUDE.md` (the Model field), `SPEC.md`, `plugin/si-plugin/templates/faq-template.md` and `faq-index-template.md`.
**Routed to Captures:** the measurement correction was recorded onto [session-start-payload-oversized-and-misordered] rather than filed as a new item.
