# PENDING — Discord bot setup, deferred at step 1

`[user]` item [discord-bot-server-setup], walked through in the second
2026-08-26 /next run and deferred by the user at the first step. First record
under this slug.

## What was done from this side

The item's step 3 requires confirming the gitignore covers the token file
*before* the user pastes a token into it, so that check was run first rather
than when the step was reached:

- `.gitignore` line 5 is `INBOX/`.
- `git ls-files INBOX/` returns nothing — no file under that folder is tracked.
- `git check-ignore -v INBOX/discord-bot-token.txt` reports it ignored by that
  rule, by name.

Told to the user with the limit stated alongside it: the token would sit in
plain text on disk, readable by any session in this project, and the gitignore
prevents publication and nothing else.

No file was created. Creating an empty token file ahead of the token would leave
a credential-shaped path in the project with nothing in it, and the step that
creates it is the same step that fills it.

## Where it stopped

Step 1 handed over: open discord.com/developers/applications, sign in, create a
new application named Throughliner, looking for its settings page opening.

**Deferred by the user.** Resume point is step 1, unchanged. Steps 2 to 5 —
resetting the bot token, pasting it into `INBOX/discord-bot-token.txt`,
generating the OAuth2 invite URL with the `bot` scope and Send Messages, Manage
Messages and Read Message History, and naming the channels the bot may post in —
are all untouched.

## What waits on it

[discord-posting-bot] is held below the line against this item: the script that
would let posts and test-rezips entries be made from a session cannot be built
until the bot exists and its token is on this machine. Nothing else waits on it.
