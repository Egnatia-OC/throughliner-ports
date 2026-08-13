# [HASH] — /next opens waiting mail before presenting the run, and the close offers the reply

`next.md`'s pre-flight gained a mail step, placed before the run is presented.
That ordering is what makes the user's reason operative — in her words, mail can
block work, resulting in deferment of work items and captures where applicable —
because mail is read while the run can still change rather than after scope is
locked. /next opens, files and defers, and never processes: anything a message
raises becomes a capture, and where it bears on an item in the cleared region,
/next names it at the present-the-run beat and recommends dropping that item from
that run only, leaving the queue untouched for a later /plan.

The reply-draft offer went to `done-build.md` rather than mid-run, which the item
did not anticipate. A run is unattended in practice, and stopping it to approve
text that leaves the machine would defeat that and bend the never-send-unseen
rule rather than honouring it. The close is the moment the user is reliably
present.

Narration matches /plan's — silent on an empty mailbox, brief otherwise. A run
announcing "no mail" every time is noise.

`plan.md` turned out to be entirely out of scope: its mail step is already tagged
silent-when-empty and brief otherwise, so the read *and* the narration exist
there. The item assumed narration was owed on both sides.

The scope-lock needed nothing, confirmed rather than assumed: `_is_inbox_dir`
returns early, before the file-list test, so mail cannot be denied during a
locked run.

SPEC's Cross-project INBOX paragraph moved in the same commit, since it stated
that /plan is the moment mail is always read.

Rule gate: run — admitted. This adds a scan to a skill opening, so the
displacement test was the live one; nothing is displaced, and the bound is the
consolidated-opening rule plus silence on an empty mailbox. The reply-offer half
is an amendment to the existing unprompted-reply-draft rule, which gains a site
rather than a new obligation.

FAQ: updated "Another project sent me a message. When does Claude actually read
it?" and added "A build run started by telling me a message affects one of
today's jobs. What does that mean?"

**Files touched:** `plugin/si-plugin/docs-b/next.md`,
`plugin/si-plugin/docs-b/done-build.md`, `SPEC.md`, `FAQ/faq.md`, `FAQ/index.md`
**Routed to Captures:** none
