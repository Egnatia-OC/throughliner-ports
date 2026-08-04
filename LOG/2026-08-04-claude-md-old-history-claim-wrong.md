# bf838bf — CLAUDE.md's old-history bullet corrected: the pre-rebuild history survives in this repo as the v17–v157 orphan tags, which must never be deleted

The bullet said the old plugin history was on GitHub as pre-rebuild commits and
not in this folder. Both halves were wrong, and the replacement wording drafted
three days ago was wrong in the opposite direction — it concluded the early
history existed in neither repo and was probably on the user's old machine. That
conclusion came from a full-history clone, and a clone follows branches.

What is actually there: the plugin was rebuilt from scratch on 2026-06-01, and
both this repo's and GitHub's branch histories start there. The May 2026
pre-rebuild history is a disconnected commit graph in this same repo, reachable
only through 135 tags named `v17`–`v157`, dated 2026-05-12 to 2026-05-29, the
earliest being "Initial commit". None is an ancestor of HEAD, which is exactly why
it looks absent. `git ls-remote` shows 134 of them on the remote, so this history
is published, not merely local. It surfaced only because `git describe --tags`
failed during the release-ritual rewrite, nothing being reachable to describe.

The load-bearing half of the correction is the warning. Those tags are the only
references keeping that history reachable; deleting them is the single action that
would actually destroy it, after which git would collect the commits. And the
mistake is plausible rather than exotic — `v17` and `v1.16.0` sort together, so
the range reads as clutter in a confusing namespace, and tidying it up is a
normal-looking thing to do. That is why the warning belongs in the file rather
than in anyone's memory.

Two questions are left open in the text rather than settled here: whether to
rename the range to remove the sorting confusion, and whether to connect the two
histories with a graft or replace-ref so the record reads continuously, or leave
them disconnected and merely documented.

The privacy result from the folded capture is carried across: a scrub sweep over
the whole orphan history on 2026-08-04 — 179 reachable commits, 3,085 distinct
prose files — found no occurrence of the known third-party name, which is what
cleared that capture's red flag on evidence rather than on consent.

**Files touched:** CLAUDE.md (the "Old plugin history" bullet in Working conventions).
**Routed to Captures:** none.
**FAQ:** not needed — a host-only developer note about this repo's own git
history; consumers never meet it.
