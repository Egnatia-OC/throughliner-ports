# c904687 — resources/rule_signals.py — audit-lag boundary reads candidate bodies, accepting only genuine audit records

Found on the audit-lag check's first run ([audit-lag-boundary-matches-processing-record]): the boundary was the newest LOG entry whose filename contains "compliance-audit", and a planning session writes a record per item it processes named for the item's slug — so a processing record of the audit item satisfied the boundary before the audit ran, silencing the check. The filename alone cannot tell the two apart, the same told-apart-by-reading problem SPEC records for the digest. The fix, settled at processing: candidates are read newest-first and accepted only where the body reads as an audit's own record — it carries "Routed to Captures:" or "Files touched:" and does not carry "Work processed:", which marks a planning record. A boundary artifact only an audit close writes was refused as a new format for one consumer.

Tick: done, confirmed (the boundary is now 2026-08-22-post-restyle-compliance-audit-2.md, the genuine audit record, not the processing record; `py resources/rule_signals.py .` runs clean; the suite passes).

Rule gate: not needed — a check's own defect fixed in script code; no method rule touched.
FAQ: not needed because the script is a host-only dev artifact.

**Files touched:** resources/rule_signals.py
**Routed to Captures:** none
