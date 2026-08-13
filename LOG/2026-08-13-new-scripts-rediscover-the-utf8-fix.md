# 340e7ef — The UTF-8 rules every new script rediscovers are written down

Three lines folded into the same `CLAUDE.md` scripting-constraints bullet as the
interpreter rules. A new script reconfigures stdout and stderr to UTF-8, copying
the block from `reorder_queue.py`, which becomes the canonical copy. Any
subprocess read sets `encoding="utf-8"` explicitly. And before diagnosing an
encoding fault seen through a console, check `ascii()` or the raw bytes.

The shared module was rejected, and the reason is that the three instances are
not one defect. Two were the write side — stdout reconfiguration — and the third
was a read: a subprocess call in `session_start.py` mangling em-dashes until an
explicit encoding was added. A shared module addresses only the write side, and
it is unavailable to the hooks anyway, which run standalone from a copied plugin
cache and already duplicate helpers on purpose. So the durable fix is written
guidance covering both directions, not code.

The third rule is a diagnosis rule rather than a script rule. It earns its place
beside the other two because that is where a session meets it: twice in one
session a correct string was read as corrupt data, once with a full wrong
diagnosis built on it.

State of the tree, checked at processing and recorded as a gap rather than a live
bug: `queue_digest.py` and `reorder_queue.py` carry the reconfiguration,
`scrub_sweep.py` and `resources/rule_signals.py` do not, though both read with
explicit UTF-8. Nothing here touches those two.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none
