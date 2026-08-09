# 96166c6 — Published a versioned `.throughliner/` editing-state signal other apps can read, as a heartbeat rather than a lock

> **Recovered 2026-08-09.** This entry records the signal's original design decision (2026-08-07). The 2026-08-09 emergency revert removed the code, and it was restored by surgical extraction at marker **version 2** — so read the payload details below as version 1, superseded. Version 2 landed at `3633c7d` (2026-08-08): `files` became project-relative, `updated` was renamed `written_at` and is no longer read at all (freshness comes from the marker file's own mtime), `session` and `pid` were dropped, and `producer` was added. The current contract is in SPEC.md. The reasoning below — heartbeat not lock, staleness as the safety property, one file per session, version leading the payload, errors swallowed in full — is unchanged and is why the recovery was worth making.

A separate project of the user's — mdreader, a Markdown reader and writer — needs to know when Claude is writing a file it has open, so the two don't land on the same document mid-sentence. Inferring that from file-modification times was rejected at design and the reasoning is what shaped the build: a watcher can see *that* a file changed but not *who* changed it, and can never tell "finished" from "paused to think", so a wrong guess locks the user out of their own document.

The core decision is that this is a **heartbeat, not a lock**, and that is what makes it safe. A plain on/off flag has one catastrophic failure — a session that crashes between starting a write and finishing one leaves the flag stuck on forever, which reintroduces the exact harm the timing guess was rejected for. So every marker carries a fresh timestamp and a reader treats a stale marker as "not editing" whatever the flag says. Staleness is the safety property, not a detail.

One file per session (`editing-<session-id>.json`) rather than one shared file, because two Claude sessions in one project is a supported shape: with a shared file, session A finishing a write would clear the flag while session B was still writing — precisely the harm this exists to prevent. The reader's rule is therefore trivially correct: editing is happening if any file in the directory is active and fresh.

`version` leads the payload and is non-negotiable, since another application is built against this contract and must be able to recognise a format it doesn't understand and fall back safely. `files` carries absolute paths so a reader can hold off in the affected document only rather than blocking everything. Marker writes are wrapped so any error is swallowed in full — a companion-app convenience must never be able to block or fail the user's actual work.

Two limits were recorded rather than left to be discovered: writes made through a shell command aren't covered (the hook only sees the edit tools, and a shell command's target isn't reliably knowable), and the signal exists only where the plugin is installed and the project adopted — which the fail-open rule already handles, since most projects will never have this at all.

The `.throughliner/` name is deliberate and tied to the pending product rename: this is a published contract an external app builds against, so shipping the current plugin name would guarantee a breaking change later.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `plugin/si-plugin/hooks/post_tool_use.py`, `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/docs-b/setup.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
