---
name: rescan
docset: current
note: >
  /rescan procedure. Split out of done.md's wind-down re-scan on 2026-08-15 so
  the step has its own trigger and can run repeatedly in one chat.
  Register: structure in typed blocks, everything else in prose, tags inline.
---

# /rescan procedure

Look back over the conversation for things decided, noticed or asked for that
were never written into a file, and file them as captures.

## What it does, and the one thing it does not

```
/rescan  ->  FILES what it finds, as captures in Unprocessed
         ->  never ROUTES them (keep / delete / where it sits)
         ->  never BUILDS them
```

Filing is capture-making and is open to every skill. Routing and building are
/plan's and /next's, and this skill stays on the filing side of that line.

**It does not build, and the reason is worth keeping.** The complaint that
produced this skill is a real one: a finding about the machinery being used right
now waits for a /plan to process it, a /next to build it, and a reinstall before
it is live. Building on the spot would not answer that, because the installed
plugin is a frozen copy — a fix made now does not reach the chat that made it
until the plugin is reinstalled and the app restarted. And a skill that could
route and build would let any chat change the project without the user having
agreed to the work.

## Step 1: Find the stopping point  [SILENT]

Scan back only as far as the last /rescan in this chat, not to the beginning.
That is what lets the skill run several times in one chat without re-surfacing
what it already surfaced.

```
/rescan already ran in this chat  ->  scan back to where it stopped
first /rescan of the chat         ->  scan the whole conversation
can't tell (the conversation      ->  read the captures filed earlier today and
  has been summarised)                use those as the boundary
```

**The stopping point is held in the conversation, and nothing is written to a
file for it.** A durable marker was weighed and refused: it is a new artifact,
and this method deletes the state files it invents. Where the conversation has
been summarised the memory of it is gone — and that is undetectable from the
inside, exactly as a compaction is — so the fallback is the captures already
filed. A stretch that yielded nothing yields nothing again, so the cost of
re-reading it is re-reading, not duplicate items.

## Step 2: File what you find  [BRIEF]

Write every candidate to Unprocessed first, then report them as ONE numbered
set. Nothing waits on approval before reaching disk: a capture in a git-tracked
QUEUE.md is recoverable without the user's help, which is the write-first test.
The user contests by number, and a contested item is reverted or reworked one at
a time.

Placement is the standing one — appended to the bottom of Unprocessed, no
judgment, no narration of the mechanics.

**State this sentence, as written:**

> I can't tell whether any of our earlier conversation has dropped out of view,
> so this is what I could still see rather than a guarantee I've caught
> everything.

**Say it as written rather than conveying its sense.** An instruction to explain
the limit honestly invites improvement, and improving it is what went wrong
before: a chat once substituted "this has been a long session, so I can only
re-read what's still in view". Length is a proxy Claude *can* observe, standing
in for the thing that actually decides the result — whether the conversation has
been summarised — which is not observable at all. The substitute invites the
user to discount the result by a factor that is fictional. Never name length,
duration, message count, or any other observable proxy.

**Nothing found is a result, and it takes one line.**

> Read back over our discussion — nothing came up that isn't already captured.

## Step 3: Say what happens next  [BRIEF]

Name what the captures are waiting for: a planning session decides what happens
to each one. Say it once, plainly, and stop.

**Recommend nothing else.** This skill exists partly because close machinery
accumulating at the end of a chat pulls the whole chat toward ending. A /rescan
that finishes by suggesting the close would rebuild that pull at a new site.
