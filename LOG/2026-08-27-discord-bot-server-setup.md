# 32675a3 — Discord bot created, token on disk, three channels named

`[user]` item [discord-bot-server-setup], walked through live in the 2026-08-27
build run's walk-through pass. Complete.

## Walk-through record

Actions appended as they happened, one step at a time.

- **Record check first.** One record on file, `2026-08-26-discord-bot-server-setup.md`.
- **Step 1 — application created.** The user created the Discord application and
  reached its settings page.
- **Before any credential existed, the destination was proved safe.** `.gitignore`
  carries `INBOX/`, and `git check-ignore -v INBOX/discord-bot-token.txt` reports
  it matched at `.gitignore:5`, with `git status` showing nothing for the folder.
  Proof from git rather than the presence of a line.
- **Step 2 — token obtained.** The user reset and copied the bot token. It was
  never pasted into this chat.
- **Step 3 — token saved.** Claude created `INBOX/discord-bot-token.txt` empty;
  the user pasted the token in and saved. **Claude did not write, read or repeat
  the value** — pasting a credential is the user's to do. Confirmed only by
  file size (72 bytes, the right order for a bot token), never by reading it.
- **Step 4 — bot invited.** OAuth2 URL Generator with the `bot` scope and
  Send Messages, Manage Messages and Read Message History. The bot appears in
  the server's member list.
- **Step 5 — channels named by the user.**

## The channels the bot may post in

Three, in the user's own words: **tips**, **announcements**, and **test rezips
for nerds**.

**And the two text channels do different jobs from now on, which the user
settled in the same message.** What is currently in *announcements* is posts
that will from here be known as **tips**; *announcements* is being narrowed to
**news only**. So the bot's two general-purpose destinations are not
interchangeable, and a draft has to be aimed at one of them deliberately.

That distinction reaches further than this item — the project's own posting rule
describes a single kind of Discord post — so it is filed as
[discord-channel-purposes-split] rather than written into a rule from here.

## Outcome: done

The item's own close condition was the token file existing and the bot being in
the server. Both are met, and the channel list is recorded above, which is what
[discord-posting-bot] was waiting on.

## Red flag: none outstanding

A live bot token now sits in plain text at `INBOX/discord-bot-token.txt`. It is
outside the repository and outside git's view, which is what the item designed
for, and the file's contents have never been read by a session. Stated as a fact
about where the credential lives rather than as an unaddressed risk: anyone with
access to this machine's filesystem can read it, which is true of the address
book beside it and is the accepted shape of `INBOX/`.
