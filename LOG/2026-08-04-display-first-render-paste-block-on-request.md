# [HASH] — Fences narrowed to code and shell commands only, prose flipped to display-first with a paste block on request, and the fence rule's justification rewritten

Two rules collided on any long piece of prose the user intends to paste elsewhere,
and nothing said which won. The verbatim-copy rule sent genuine paste targets to
fenced code blocks; the approval-time rule sent drafts to blockquotes, because
fences don't wrap in the desktop app and an unreadable draft can't be meaningfully
approved. A long announcement draft is both at once. Claude hit exactly this,
chose the fence, and the user — on remote control — could not read the text she
was being asked to approve.

The decision, and the reasoning is the user's: default to the readable rendering
and *offer* a paste block rather than producing one unasked. Most people select
the text they want and copy that, so a blockquote is already copyable. Display-first
therefore costs nothing, and the paste block is a cheap follow-up when someone
actually wants one.

The second change is the one that would have been missed, and it matters more than
the scope trim. The fence rule's stated reason was that the desktop app's copy
takes the whole message, so a fence is the only clean copy affordance. That premise
is precisely what the user disproved. Fences survive for commands on entirely
different grounds: markdown rendering would corrupt characters whose exactness is
the substance, and the app attaches a Run button to shell-tagged blocks. Trimming
the scope while leaving the old why in place would have let the rule drift back,
because the why is what a session steers on. The disproved reason is now recorded
in the file as wrong, so it isn't restored by someone reasoning from first
principles.

**Files touched:** docs-b/plugin-behaviour.md (the fence rule's scope and
justification; a new bullet putting prose outside fences; the approval-time
rendering rule, which absorbs the prose case). Docset A is frozen and was not
touched.
**Routed to Captures:** none.
**FAQ:** not needed — a rendering nuance with no new user-facing capability behind
it, and no question a non-coder would arrive with.
