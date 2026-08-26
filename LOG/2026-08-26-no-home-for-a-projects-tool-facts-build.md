# [HASH] — TOOLS.md: a home for what a project has on hand, writable under the scope-lock in every session type

A build session in Taskflowapp established four facts worth keeping — Android
Studio installed, its bundled JDK at a known path, the SDK at another, and
Gradle's daemon connection failing from Claude's shell specifically while a plain
loopback test succeeded — and had nowhere durable to put any of them. The last one
especially: rediscovering it costs a run its first act, which is exactly what had
just happened. You expected a list, and the method had none.

The design was settled at planning against this project's own machinery rather
than by preference. A section in the project's CLAUDE.md is the intuitive home and
was refused: the scope-lock denies CLAUDE.md to planning sessions and to any build
whose item does not list it, so recording one path would cost a
capture-then-plan-then-build chain nobody would ever run. `TOOLS.md` at the
project root mirrors the cycles doc instead — created on first use, so a project
with no tool facts has no file and pays nothing.

**The hook change is the load-bearing half**, because the permission has to hold in
both branches of the scope-lock and they are separate code paths. A build learns
an environment fact while locked to files chosen before the fact existed, so
`TOOLS.md` is never in its list by construction; a planning session is held to a
standing list that never included it either. A `_is_tools_file` helper is now
checked in both. It matches the project root exactly, so a `TOOLS.md` a user keeps
inside a subfolder of their own app stays under the ordinary lock — the new suite
pins that, along with an unlisted ordinary file still being denied mid-build.

The doc half gives the environment check both directions: read the file before
assuming a tool or environment is absent, and write a newly learned fact there in
the moment, one line each.

**Files touched:**
`plugin/throughliner/hooks/pre_tool_use.py` — `_is_tools_file` helper, checked in
the build branch and the standing planning list; module docstring and the planning
deny message updated.
`plugin/throughliner/docs/next-build.md` — the environment check gains a read half
and a write half.
`resources/testing/test_pre_tool_use_tools_md.py` — new suite, 14 cases.

**Routed to Captures:** none.

Tick form: done, confirmed — the new suite passes all 14 cases, including both
end-to-end blocks driving the hook as a subprocess.

Rule gate: run — amendments to the environment-check rule (the read half) and the
scope-lock's quiet list (the write half), no freestanding rule added. The
CLAUDE.md-section alternative was refused at planning: unreachable under the lock
without a heavier carve-out. A /setup scaffold step was refused too — the file is
created on first use.

SPEC already carries the sentence for this, written at the keep, so nothing lags.
