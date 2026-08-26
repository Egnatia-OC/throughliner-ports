# 46fde79 — Install docs pinned to `#beta`; the branch itself could not be cut, because today's release has not run

The docs half is done. Every marketplace-add string in `README.md` and `INSTALL.md` now reads `FlintcraftTech/throughliner#beta` — the paste prompt, both reference commands, and the guide's own command block — each with a plain-English line saying beta is the tested weekly pick while main carries day-to-day development, and both update instructions saying an update brings the newest beta. The FAQ's install entry, authored earlier in this same run, was carried across too rather than being left contradicting the docs it was written beside.

**The branch was not created, and the item's own instruction is why.** It says to cut `beta` immediately after today's release commit exists on main, so the branch never points at pre-release state. Retried at the run's end and again at the close: the version is still `1.20.0-test19` and there is no release commit. Creating and pushing a branch is also an outward action needing Alex's word, so it would have waited regardless.

**The gap this leaves was surfaced and accepted rather than discovered.** Between now and the release, README and INSTALL.md name an install route that does not resolve. A revert of the pin was offered as the alternative; Alex's decision was to leave it, on the ground that the release is being pushed through within the hour. Recorded here because if the release does not happen, a broken instruction is sitting in shipped docs — and the docs and the branch have to land together whenever it does.

Files touched: `README.md`, `INSTALL.md`, `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`
Routed to Captures: none — the outstanding half is the item's own second step rather than new work.
Rule gate: not needed — install docs and a git branch, no method rule text.

Depth: short. Ticked as done, UNCONFIRMED: the `beta` branch does not exist, and cannot until a release commit is on main.
