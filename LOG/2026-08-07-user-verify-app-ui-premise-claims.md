# [HASH] — Three app-behaviour claims checked with the user: two falsified, one confirmed, and a fourth answered by accident

A `[user]` item, walked through live at the end of the run. Each claim underpins a rule applied many times per session, and each was true when written and had never been re-checked. Two were wrong.

**Claim 1 — line-anchored `.md` links: FALSIFIED.** The docs say a `.md` link with a `:N` suffix is *"dead: the click does nothing, and it fails silently while still looking clickable"*. Sent both forms of the same link, the user reported **both opened the file at the top**. So the anchored form is not dead and does not fail silently — it behaves exactly like the plain link, ignoring the anchor.

The *instruction* survives (don't emit a line anchor on a `.md` link; it will not take the reader to the line) but its *reason* is false, and the reason is what a later session reasons from. That difference is load-bearing in at least one place: the doc-bound-text design accepts a real cost — the pointer lands at the top of a long document, so the short summary has to carry the user — partly on the grounds that the anchored alternative is *unavailable*. It is not unavailable; it is merely no better. Filed as [md-line-anchor-opens-at-top-not-dead], which also flags that the code-file exception (`.py`, `.json` honouring anchors) was **not** tested and must not be assumed correct because its sibling was checked.

**Claim 2 — fenced blocks: SPLIT.** The Run button appears on a shell-tagged fence: **confirmed**, and that is the half earning the one-command-per-block discipline. But a ~280-character sentence inside a fence **wrapped** and was fully readable — falsifying *"fences don't wrap in the app"*, which is the **entire** justification for the rule that prose never goes in a fence.

Filed as [fences-wrap-so-prose-rule-reason-is-false], with the limit kept rather than collapsed: the recorded failure was specifically *a user on remote control* who could not read a long draft, and remote control was **not** tested — the user was at the desk. So it is **falsified at the desk, unverified on remote control**. Deleting the rule on this evidence alone would repeat the very mistake this pass exists to catch: reading a claim more broadly than it was tested, the shape already recorded twice against the orphan-tag history and the remote-branch list.

**Claim 3 — suggested replies: CONFIRMED, more strongly than the rule assumed.** Asked to look at the input box at a live stop, the user reported **none showing at all**. The stop-self-sufficiency rule rests on those suggestions being unreliable; at the desk they were absent outright. So every stop naming both replies in its own text is not belt-and-braces — it is the only thing carrying the ask. No change needed.

**A fourth claim was settled by the user's own question.** They asked what happens if they set their own markdown reader as their editor. The behaviour rules record that nothing reads the retired `Editor:` field because links open in the desktop app's own viewer regardless — a recorded claim of the same unverified class. They then reported the link opened **in the Claude Code sidebar, not their native viewer**. So the justification holds, verified rather than assumed: an external editor never gets the chance, and the field could not have worked whatever it said.

**The remote-control half of claims 2 and 3 stays untested**, and is filed as its own `[user]` item — [user-verify-remote-control-rendering] — rather than left as a note, since it is genuine user work that would otherwise exist only in this conversation. It carries what is already settled, so nothing gets re-run.

**Files touched:** none — this item produces knowledge.
**Routed to Captures:** [md-line-anchor-opens-at-top-not-dead], [fences-wrap-so-prose-rule-reason-is-false], [user-verify-remote-control-rendering]
