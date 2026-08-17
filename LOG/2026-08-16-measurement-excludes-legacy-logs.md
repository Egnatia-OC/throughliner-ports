# de2f5fc — The length measurement now reads the pre-split logs, and the baseline is shorter than anyone estimated

The tool could not see the era before the growth. It read per-entry LOG files only, and its own note said the earlier record "lives in the legacy combined log and is not measured here" — which reads as *cannot be*. It parses fine: every legacy file carries `## <hash> — <title>` headings, one per entry. So the growth was being reported only from inside the period during which it happened, which is why its scale was invisible to anyone reading the output.

Legacy entries are measured as one undifferentiated group, with no plan/build split, settled when the item was processed. Flavor was not recorded then, and inferring it from a title's wording would be guesswork printed as measurement.

The item was kept on the user's purpose after Claude recommended dropping it. That recommendation judged the item against deriving the bands, which July already settles; her purpose was different and had not been weighed — she wanted the legacy work measured properly so the growth is shown.

The measurement changed the picture rather than confirming it. The item estimated legacy entries at "roughly 250–460 words each". Measured across 157 entries: median 183, mean 197, maximum 656. So the growth is larger than the item claimed, not smaller — against 183, August's build median of 485 is a 2.7-fold rise rather than the roughly 1.5-fold the estimate implied. The baseline also sits comfortably inside the 115–229 build-entry band shipped in this same run, which means that band describes a length this project has already sustained rather than an aspiration.

The corrected figure and the wrong estimate both went to the audit that followed, as `[pre-split-baseline-corroborates-the-bands]`, so anything quoting the old number — including a queued Discord post drawing on it — has the measured one available.

**Files touched:** `resources/measure_written_shape_length.py` (new `legacy_entries()` parsing the combined logs by heading; report gains a pre-split baseline table and its longest-ten list; the false coverage note replaced by a statement of what the group is and why it is undifferentiated; docstring updated to match).

**Routed to Captures:** none directly — the audit item that follows this one routed the findings.

**Rule gate:** not needed — a measurement tool, no rule authored or amended.

**FAQ:** not needed because this is a host-only dev resource, not shipped in the plugin package.
