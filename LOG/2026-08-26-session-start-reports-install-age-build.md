# [HASH] — Session openings now report when the installed build arrived, and refuse to guess when they can't tell

You raised this from a live instance: an announcement draft claimed you had been
running a build "all week" when you had been running it since late the night
before. Claude had no way to know how long an installed build had been in place,
and the misjudgment recurs.

Install age won over time-under-use at planning, and the reason is worth keeping.
Time-under-use is closer to what anyone actually wants to know, and it needs a
state file recording sessions per build — which this project refuses on standing
grounds, because the first session that forgets to update one makes it lie. Install
age needs no maintenance at all: the CLI writes the snapshot into the plugin cache
at install time and never touches it again, so the directory's own timestamp is
when the build arrived. And it covers the failure that prompted this — "installed
11 hours ago" kills an "all week" claim on sight.

The line reports the fact bare, beside the version and the content stamp. It is
never a verdict on how tested a build is; that judgment stays the reader's.

**The degrade rule earned its keep immediately, and this is the part worth
recording.** A try/except was not enough. Windows clamps an unreadable mtime to
zero rather than raising, so a lost timestamp arrived as a perfectly well-formed
`1970-01-01` — a plausible date that is pure noise, which is precisely what "no age
claim rather than a guess" forbids. The suite case found it. The helper now also
carries a date floor, and that floor is derived rather than invented: the plugin
was rebuilt from scratch on 2026-06-01, so nothing installed can predate it.

**Files touched:**
`plugin/throughliner/hooks/session_start.py` — `PLUGIN_EPOCH` constant,
`install_date` helper, and the date added to the version line.
`resources/testing/test_session_start_install_age.py` — new suite, 8 cases.

**Routed to Captures:** none.

Tick form: done, confirmed — 8 cases passing, including a real install, a backdated
one, three unreadable-input cases, the 1970 clamp, and both sides of the floor.

Rule gate: not needed — a reported fact added to a hook's payload, no method rule
authored or amended. The floor is a derived value with its derivation stated in the
code, not a rule.

SPEC already carries the clause for this, written at the keep.
