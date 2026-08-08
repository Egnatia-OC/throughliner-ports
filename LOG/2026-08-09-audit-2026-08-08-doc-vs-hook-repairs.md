# 7a4b377 — Four doc-vs-hook mismatches repaired: the shell-write matcher's real scope, the red-flag scan's real owner, the git-push half-claim, and two inert leftovers

All four came from the 2026-08-08 differential audit, and all four are the docs
overstating or misattributing what the hooks do. The code was consistent
throughout, so every repair is a doc reword — the one code change is a docstring
line.

**Point 1, and it matters most.** The behaviour rules claimed that a shell command
writing a file — "a redirect, a heredoc into an interpreter, `Set-Content`,
`sed -i`" — is blocked. `pre_tool_use.py`'s `structured_write_targets()` matches
only a **Python invocation** (heredoc or `-c`) containing a write-mode `open()` or
a `Path(...).write_text/bytes` on a **literal quoted path**. Redirects,
`Set-Content` and `sed -i` pass straight through. Re-verified independently at
processing: the hook has no `Set-Content` or `sed -i` handling at all.

The reason this is the worst of the four is that **the overstatement trains false
confidence precisely where the written rules are the only real protection**. A
session believing the shell route is mechanically closed will not apply the care the
doc-level rules ask for. SPEC.md already stated the honest limit, so the repair was
to bring the behaviour rules into line with SPEC rather than invent new wording —
and the rewritten passage keeps the discipline explicitly, telling the reader to
read the limit as the reason to keep the rule rather than as a loophole.

**Point 2 — both halves of one sentence were wrong.** The Line format rule said the
work-item shape "is what the hooks parse (post_tool_use's queue lint and
pre_tool_use's red-flag scan; session_start does not read work items)".
`pre_tool_use.py` contains no red-flag scan at all, and `session_start.py` **does**
read work items — its `_uncleared_red_flags()` parses `#### ` headings and
`Red flag · State: uncleared` markers to surface risks first thing. Re-verified by
count at processing: seven red-flag references in `session_start.py`, zero in
`pre_tool_use.py`. The sentence now credits the right hook and drops the false
claim.

**Point 3 — a claim that was three-quarters true.** "The first, second, third and
fourth of those are mechanically blocked" covered four never-rules, but the third
is "never git push without asking → and never `--force`", and the hook blocks only
`--force`. A plain `git push` is neither blocked nor asked. The claim now covers
the first, second and fourth, with the third split into its own short paragraph
saying `--force` is blocked and push-without-asking rests entirely on the written
rule — keep it anyway, nothing will stop you.

**Point 4 — two inert leftovers.** `pre_tool_use.py`'s module docstring still said
"For Bash/PowerShell: checks rule 2 (git safety) only", stale since rule 5 was
extended to run unconditionally in that same branch. And `docs-b/next.md`'s
frontmatter still named the deleted `docs/` folder — inert provenance text, but the
audit plan's own rule is that any surviving `docs/` reference is a finding, no
exceptions. (`session_start.py`'s `docs/` mentions are deliberate historical
comments explaining the retirement and were left alone.)

Both hook test suites were re-run after the changes and passed.

**Files touched:**
- `plugin/si-plugin/docs-b/plugin-behaviour.md` — points 1, 2 and 3.
- `plugin/si-plugin/hooks/pre_tool_use.py` — module docstring line.
- `plugin/si-plugin/docs-b/next.md` — frontmatter note.

**Routed to Captures:** none from this item.

**FAQ:** not needed because the existing FAQ entry on the blocked shell-write already describes the behaviour honestly; these repairs bring the internal rules into line with what the FAQ and SPEC already said.
