# [HASH] — AGENTS.md deleted: 5,511 words of partly-maintained CLAUDE.md mirror, carrying a retired docset model and two commands that cannot run

`AGENTS.md` was the Codex port's mirror of CLAUDE.md. At deletion it was 5,511 words against CLAUDE.md's ~7,800, and its content had diverged in ways that made it actively misleading rather than merely old: it still described docset A as a frozen fallback with the session-start hook choosing between docsets, it pointed at five procedure files in a `docs/` folder that no longer exists, it stated that a retired model was the one the plugin is tuned for, and it twice instructed the reader to run `Codex plugin update sovereign-implementer@flintcraft` — there is no `Codex` executable, so both commands fail for anyone who follows them. That last one reads as a wholesale substitution that caught the word where it was a program name rather than the assistant's.

The state that made it worse than plainly stale is that it was *partly* maintained. It received the corrected plugin-history text at `bf838bf` but not the docset retirement at `f9326dc`, so some of it was current and some a long way out of date with nothing marking which — and its accurate instructions are exactly what made the broken ones credible.

Nothing reads it. The Codex port has been shelved indefinitely since 2026-07-28, downstream-only, read-only history. Keeping the file correct means every CLAUDE.md edit doing double work, and the evidence is that this silently did not happen.

The alternative was weighed seriously and lost. Marking the file dormant in one line and ceasing to sync it fixes the misleading-reader problem, which is the sharper of the two faults, and it is cheaper. It lost because it leaves 5,511 words sitting inside the instruction-count audit's corpus, and because a dormant-marked file still invites the next well-meaning sync. The revival argument lost too: git history holds the file, and a revived port would need a mirror of the *then-current* CLAUDE.md, which a stale copy is a worse starting point for than a clean one.

Every surviving reference was checked and all were correctly left alone. The LOG entries and index lines are history. `resources/research/instruction-file-bloat-and-subtraction.md` cites the AGENTS.md *convention* across 2,500+ public repositories, not this file. `resources/research/scopelock-independent-implementation/README.md` tells a reader to append a fragment to *their own* project's AGENTS.md. None implied this repository's copy was live, so nothing needed correcting, and `AGENTS.scopelock.md` — which merely shares the name — was left untouched.

The immediate unblock is real rather than tidiness: the compliance audit that ran later in this same session had a corpus of docs-b/ plus CLAUDE.md, and counting instructions in a document nobody had decided the status of would have produced a misleading number.

**Files touched:** `AGENTS.md` (deleted).

**Routed to Captures:** none from this item.

FAQ: not needed because the file was a host-side development artifact for a shelved port; no consumer ever saw it and no shipped behaviour changed.
