# 32675a3 — Chat record: 24 builds, five walk-throughs, a live Discord bot, and three rules this run broke itself

Chat-level record for the 2026-08-27 build session. The per-item records are the
24 `-build.md` entries and the four `[user]` records of the same date; this one
carries what belongs to no single item.

## The run

Twenty-four cleared items built back-to-back, then the walk-through pass over
five `[user]` items. Roughly twenty of the twenty-four authored or amended a
method rule, which is the largest single movement the growth report has recorded:
+47 always-loaded rule statements for consumers, +45 for this project, +144 across
the fetched procedure docs.

**The user changed the run order before it started**, and the reason was sound:
[builds-read-the-queue-again] retires the generated view and rewrites the
scope-lock hook, so building it last kept the run's own machinery stable while
the other twenty-three went through. The run was reading a file produced by the
script that item deletes.

**Two files were added to the run's scope mid-run**, both completing described
work rather than growing it: `feedback-and-inbox.md` and `migrate-checklist.md`
carried cross-doc references to the renamed decision step, which
[keep-term-retired-for-processed] required updating and had under-enumerated;
then `.gitignore` and `test_queue_lint_flags.py` for the build-view retirement.
Each is recorded on its own item.

## Also in this chat

**Three rules did not fire at the moment they applied, and two were caught by the
user rather than by the method.**

- She had to tell Claude the Discord bot could read message history —
  *"you're supposed to have read message history access through the bot"* —
  twenty minutes after Claude had itself walked her through granting exactly that
  permission. Filed as [capability-just-granted-not-considered].
- A hand-over step went out reading "Developer Portal → Bot → Privileged Gateway
  Intents → Message Content Intent", with no indication where any of it sits on
  screen. Her reply: *"I don't understand what you want me to do"*. That broke
  the jargon rule **this same run had authored an hour earlier**. Filed as
  [walkthrough-jargon-broken-by-its-own-author].
- She had to ask for a clickable file link the view-in-doc rule already requires.
  Filed as [file-link-not-offered-at-hand-over].

Recorded together because they share a shape: a clearly written, long-shipped
rule failing at the composition of a hand-over message, never at a file edit.
The advisory asks the next planning run to weigh them as one question.

**The Discord bot went live and was used.** Created and authorised during
[discord-bot-server-setup], it then read the test-rezips pin — the first time this
project has read from an external service. Two gates were found and fixed live: a
per-channel permission (403 on test-rezips and main, while announcements and tips
answered 200) and Discord's Message Content Intent, without which message text
returns as an empty string with no error.

**The pin's text was not recoverable from this project's own records.**
`INBOX/sent.md` pointed at a LOG entry that contains no quoted text. Rewriting the
pin from the register's paraphrase was refused and said so plainly — it would have
handed the user invented wording as her own post. The bot recovered the real text.
Filed as [sent-register-pointer-resolves-to-nothing].

**A /rescan ran before this close** and filed three further captures, including
that this project's CLAUDE.md still tells every session Claude has no route to
Discord — false as of today.

**The user filed one capture directly**: [bot-icon-house-style], for the bot's
icon in the sibling-project style. Claude read both reference icons and recorded
that the gap is a redraw rather than a recolour.

## Close obligations

- **Hook suites:** run, all 27 passed. The count fell from 29 because the
  build-view retirement deleted two suites; three were added this run.
- **Rule checks:** four run, one found something — rule-bearing commits since the
  last compliance audit are uncovered. Filed under its printed slug,
  [compliance-audit-lag]. Nothing here is evidence the rules are correct or that
  they fire; this run's three self-observations are the counter-example.
- **SPEC:** checked against, not synced. SPEC already carried the sentences for
  the queue-reading model, the completion-ask carve-out and the date anchor —
  written at planning ahead of the builds, which is the lead model working. Two
  sentences it does not carry are filed as [spec-owes-warn-and-outcomes] rather
  than written, because a build does not write product truth.
- **README:** no feature-list change owed. Nothing this run added or removed a
  skill, mode, command or user-visible hook behaviour the list describes.
- **FORMAT_EPOCH:** not bumped, deliberately, with the reasoning on
  [builds-read-the-queue-again].
- **Retired terms and artifacts:** appended to `resources/retired-terms.md`, and
  that section's first real entries. The compounds are listed, never the bare
  words "keep" and "line", which have correct live uses — the cry-wolf rule that
  file already records against `CEILING`.

Advisory: filed — [last-session-advises]

Rule gate: run — twenty-plus dispositions, one per built item, each transcribed onto its own record from the item that carried it. No rule was authored at this close.
