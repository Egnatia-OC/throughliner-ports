# [HASH] — Test-rezips pin edited: entries promise a commit line, pruning claim made mechanism-neutral

`[user]` item [test-rezips-entries-name-obtain-route], walked through live in the
2026-08-27 build run's walk-through pass. Step 1 done.

## Record check first

One record on file, `2026-08-27-test-rezips-entries-name-obtain-route.md` — a
planning record only. The item had never been walked; the drive started at step 1.

## The pin's text could not be found in this project, and that is a fault worth naming

The item needed the pin rewritten whole, which needs the pin's words.
`INBOX/sent.md` claimed the posted text was verbatim in
`LOG/2026-08-26-beta-day-one-posts-2.md`. **It is not there** — that record holds
no quoted text at all, and the text is in no other record either. All this
project held was the register's one-clause paraphrase.

Rewriting the pin from a paraphrase was refused and said so plainly: it would
have handed the user invented wording as their own post, to be pasted over the
real one. The register's whole purpose is to make a claim checkable later, and a
pointer to text that is not there defeats it. Filed as
[sent-register-pointer-resolves-to-nothing].

## The bot read it instead — the user's correction

Claude offered the user two ways to supply the text and did not consider the bot
it had itself provisioned twenty minutes earlier, with Read Message History
among its permissions. **The user pointed this out.** Her words: *"you're
supposed to have read message history access through the bot"*.

That is the capability-check failure this method has a rule against, committed
immediately after granting the capability. Filed as
[capability-just-granted-not-considered].

## Two gates found live, each fixed by the user in one step

1. **HTTP 403 Missing Access** on the channel's pins. The bot could see the
   channel in the guild listing but not read it — a per-channel permission
   overwrite, not a missing scope. Diagnosed by testing four channels: announcements
   and tips returned 200 while test-rezips and main returned 403. The user added
   the bot to that channel's permissions.
2. **Message content returned empty.** `content` was present as `''` with no
   embeds and no attachments — the signature of Discord's Message Content Intent
   being off. The user enabled it.

**The first explanation of gate 2 did not land** — it named the Developer Portal,
Privileged Gateway Intents and the intent itself with no indication where any of
them are on screen. The user said so: *"I don't understand what you want me to
do"*. Re-explained as five located steps. This is the walk-through vocabulary
rule, built earlier in this same run, broken within the hour by the session that
built it. Filed as [walkthrough-jargon-broken-by-its-own-author].

## What was edited, and what could not be

**A bot cannot edit a message it did not author.** `Manage Messages` permits
deleting others' messages and pinning, never rewriting them. The pin is the
user's own message, so the edit was hers to paste; the bot's part was reading it
and reading it back afterwards.

Two changes, everything else carried verbatim:

- **added**, after the three labels: *"Every entry also names the commit it was
  cut from, so you can always tell exactly which version you're running and get
  back to it later — and attaches a zip where one is offered."*
- **reworded**, the closing line: *"The list keeps the newest builds; I prune old
  entries by hand"* became *"The list keeps the newest builds; older entries are
  pruned as new ones go up."*

**Why the second names no mechanism.** The user's instruction was that pruning is
no longer by hand now the bot exists. But the posting bot is unbuilt, so a pin
claiming automatic pruning would announce behaviour that does not ship — barred
by the announce-only-what-has-shipped rule. Mechanism-neutral wording is true
today with hand-pruning and stays true once the bot does it, so the pin needs no
second edit. The intent itself is filed as [bot-prunes-test-rezips], carrying an
uncleared red flag: an unattended prune with Manage Messages deletes published
messages irreversibly.

## Verified from the world, not from the report

The pin was read back through the bot after the edit. The live text carries both
changes. Full edited text is the block the user pasted, reproduced in the register
line's pointer.

## Outcome: step 1 done; the item is NOT complete

Step 2 — every future rezip entry carrying a `Commit: <hash>` line — is a
standing commitment on entries not yet written, not something this session can
finish. Step 3 said to report the pin edited so the register line could be
updated; that is done above.

The item stays in Processed. What it now waits on is the first entry posted under
the new promise, which is where step 2 is either honoured or not.
