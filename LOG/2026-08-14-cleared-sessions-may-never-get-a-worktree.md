# Start one genuinely new desktop session and compare two git paths

Slug: `[cleared-sessions-may-never-get-a-worktree]`. Entry opened live during the
/next walk-through, per next.md's `[user]` branch, and appended to as the
walk-through ran.

## What this tests

The hypothesis: Claude Code allocates a worktree at session *creation*, not at
`/clear`. Alex pre-makes sessions at home and clears them rather than starting
new ones, because starting one by remote control causes a fuss — so a workflow
built entirely on reused sessions would never see a worktree, which is exactly
what has been observed here.

**Weigh it on the right terms.** This is not an open mystery. The contradiction
between documented and observed behaviour was investigated on 2026-08-11, written
up in `resources/research/worktree-isolation-and-desktop-sessions.md`, and
reported to Anthropic as `anthropics/claude-code#85560`. The test confirms a
filed issue's symptom on this machine rather than explaining something nobody
understands.

## Capability check

Claude has no route to starting a desktop-app session — no tool exposes it. So
this is genuinely user work rather than work Claude could do but cannot do yet.

## World-state observed before the walk-through

Run in this session, on the main checkout:

```
.claude/worktrees/   — does not exist
git worktree list    — main checkout, plus the deliberate Codex port at
                       ../Sovereign Implementer - Codex port [codex/si-port]
```

So no session-allocated worktree exists on this machine at the moment the test
begins. That is the state the test is trying to explain.

## The walk-through, as it ran

1. Alex started a genuinely new desktop session (+ New session, not `/clear`) and
   opened it on this project.
2. That session ran `git rev-parse --git-dir` and `git rev-parse
   --git-common-dir`. **Both printed `.git`** — identical.
3. Re-checked the world from this session immediately afterwards:
   `.claude/worktrees/` still does not exist, and `git worktree list` still shows
   only the main checkout and the Codex port.

## Result — the hypothesis is REFUTED

A genuinely new desktop session got no worktree. Identical paths mean a main
working tree, so the reused-session explanation is wrong: it was never about
`/clear` at all.

**What that leaves.** The documented behaviour — every new desktop session gets
its own worktree at `<project-root>/.claude/worktrees/` — simply does not happen
on this machine, under any session-creation route tested. The setting was already
confirmed at its default ("Inside project"), so nothing is redirecting worktrees
elsewhere either. The discrepancy recorded on 2026-08-11 stands, and this test
removes the leading explanation for it rather than supplying one.

**Why that is still worth having.** It strengthens `anthropics/claude-code#85560`
rather than dissolving it: what looked like it might be a workflow artefact on
Alex's side is now shown not to be. The bug is in the app's behaviour, not in how
she starts sessions.

**And it settles a live consequence.** `[concurrent-session-support]` is written
for the isolated case and silent when isolation is absent. Isolation is absent
here under every route tested, so the method's own testing on this machine never
exercises the isolated path — which is now established rather than suspected.

## Where the finding was filed

Appended to `resources/research/worktree-isolation-and-desktop-sessions.md`,
which is the durable file a future session re-reads before re-opening this
question, and which previously recorded the contradiction as unexplained with
this hypothesis outstanding.

