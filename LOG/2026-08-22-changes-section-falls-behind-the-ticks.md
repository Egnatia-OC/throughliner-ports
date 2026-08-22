# d7ea8a0 — `Changes:` joins the per-item completion set as the fourth required write

Kept on the first of the item's two candidate fixes: the close-side mismatch check only detects the gap at the moment a fresh or crashed session can no longer fill it — the design-target session is the one it fails in — while the per-item write is the shape the other three required writes already prove. The close's existing reconcile stays as the backstop that found this. Cost accepted: one more write per built item during the run. Full disposition and build block on the item.

**Queue changes:** kept into Processed, cleared to run.
**Work processed:** kept — [changes-section-falls-behind-the-ticks].
