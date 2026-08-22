# 2625fa0 — Kept and cleared: the audit-lag boundary reads the matched entry's body rather than trusting the filename

The read-the-entry design won: the check accepts a filename-matched LOG entry as boundary only where its body carries the audit-record markers (the artifacts-read list); a processing record of the audit item lacks them and is passed over, the search continuing older. Keying on a new artifact only an audit close writes was refused as a new format for one consumer — the same told-apart-by-reading answer the digest uses for shipped-versus-processed records.

Rule gate: not needed — a check's own defect fixed in script code.

**Work processed:** kept — [audit-lag-boundary-matches-processing-record].
