# bf838bf — Approval-time text now written to its doc first and approved in place, collapsing the render rule's two branches into one

The render rule had two cases: text already in a doc got a pointer, and text not
yet written was always pasted inline "since there's nothing to point at". Write it
and it's resident — so the second case doesn't need answering, it needs deleting.
That is the argument the build led with, and it is why this is a simplification
rather than another branch.

Doc-destined approval text — a capture, a work item, a LOG entry, a SPEC or
CLAUDE.md edit — is now written to its file first, and the user approves it there,
reading it in final position next to the items around it. Remote mode is the one
exception: opening a file on a phone means navigating Drive, so the text is pasted
inline as well.

Three things had to be specified rather than assumed, and each was a real hole.

The boundary. Not every approval-time output is headed for a file — a commit
message isn't, and neither is a recommendation or a set of options. Without the
clause the rule would try to invent somewhere to write a commit message purely so
it could link to it. Those keep the ordinary inline rendering.

The reject path. "Revert on reject" is load-bearing and isn't free. Nothing is
committed mid-session, so a reject means editing the text back out, and getting
that wrong leaves rejected content sitting in a tracked file. The rule now states
it plainly: remove exactly what was written, re-read to confirm it's gone, say so.
This buys back explicitly the safety that showing-first gave for free. The residual
cost is named rather than waved off — there is a short window where a tracked file
holds unapproved text, and a crash or concurrent session landing in it leaves that
text there.

The write-verify-point order. The existing rule already said to verify before
pointing, and it did not prevent a session announcing a write it had not yet made.
That failure is specific to this flow: a pasted draft cannot be claimed without
being produced, but a pointer can. So the order is restated as the rule, with that
incident as its why.

Link behaviour, tested live on desktop app 2.1.219 and now written into the docs
as a constraint: a plain relative `.md` link opens the file at the top; the same
link with a `:N` line suffix is dead, and fails silently while still looking
clickable; code files honour their anchors. Because a markdown link can only reach
a file and never a position, every pointer now carries the target's exact heading
text. That is not decoration — landing at the top of a 480-line queue and being
told "it's in there" is the failure the pointer exists to avoid, and searchable
heading text turns a scan into a copy-paste.

This inverts plan.md's "never write to QUEUE.md without showing the exact text
first", deliberately. Approval still attaches to exact text — arguably more firmly,
since the user reads it in rendered position — but it now attaches after the write
rather than before.

The flow was exercised live during a /plan session on 2026-08-04 across eight
processed items, including one rejected and rewritten in place, and it held.

**Files touched:** docs-b/plugin-behaviour.md (the working-mode render rule
rewritten; Captures, why-pipeline and capture-and-continue reworded), docs-b/plan.md
(the show-before-write rule inverted; both view-in-doc passages), docs-b/next.md
(run presentation, reshape-direction capture), docs-b/next-build.md (readable-edit
reveal, two capture steps), docs-b/done.md (LOG-entry approval), SPEC.md
(working-mode description), FAQ/faq.md + FAQ/index.md. README.md needed no change —
its feature list never described the approval flow. Docset A is frozen and was not
touched.
**Routed to Captures:** none from this item.
**FAQ:** updated — "Claude wrote a draft straight into my queue before I approved
it. Is that meant to happen?"
