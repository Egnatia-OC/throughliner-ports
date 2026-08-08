#!/usr/bin/env python3
"""
THROWAWAY PROBE — delete this file, its hooks.json entry, and its log at the
close of whichever session reads the result.

Measures exactly one thing: whether Claude Code's PostCompact hook event
actually fires in the desktop app. The event is documented, but the `model`
field is documented in the SessionStart payload and simply never arrives here,
so documented is not the same as delivered.

Appends one line to .throughliner/probe-postcompact.log and exits zero. Emits
nothing, blocks nothing, reads no project state, and fails silent — a probe
that can break a session is not worth the answer.

The log filename must not begin `editing-` or end `.json`: the companion reader
treats any `.throughliner/editing-*.json` file as an edit-in-progress marker,
and a probe file matching that glob would be read as this plugin editing a file
forever.
"""

import datetime
import json
import os
import sys

try:
    payload = json.load(sys.stdin)
    cwd = payload.get("cwd") or os.getcwd()
    trigger = payload.get("trigger", "<absent>")
    folder = os.path.join(cwd, ".throughliner")
    os.makedirs(folder, exist_ok=True)
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    with open(os.path.join(folder, "probe-postcompact.log"), "a",
              encoding="utf-8") as fh:
        fh.write("{} PostCompact fired — trigger={}\n".format(stamp, trigger))
except Exception:
    pass

sys.exit(0)
