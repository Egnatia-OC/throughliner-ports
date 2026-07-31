# c7c6cd5 — plugin-behaviour.md: added the red-flags screen-and-surface rule and three flag states

Reintroduces the old plugin's security screening as a compliance-hardened rule in plugin-behaviour.md. The prior plugin had a "Red flags — screen and surface" behaviour, but it lived as an unstructured convention. This version makes it a written rule with explicit scope (security, privacy, breach risk), a why-clause explaining why it must not be smoothed over, and positive constraints stating what Claude does (names and routes the risk, never silently fixes or ships past it). Placed in plugin-behaviour.md so it fires in every session type, including mid-build — where Claude is writing the code that could expose data.

The three flag states — open, resolved, accepted — are the mechanism the future autopilot gate will read. Open blocks unattended execution; resolved and accepted clear it. Accepted carries informed consent: what the user was warned about and that they chose to proceed, recorded in the LOG as the trail that protects them later. The states are defined here; the routing (where flags collect, how /plan manages their lifecycle) ships in [red-flags-structure].

Deferred-test confirmation this session: [queue-format-lint-hook] — both halves confirmed live. QUEUE.md edits triggered advisory warnings next to the tool result; edits to other files (plugin-behaviour.md, REGISTRY.md, _build.md) stayed silent. Line removed from Deferred tests.

Capture filed mid-session: "deferred tests vs test batches" — user questioned the deferred-test mechanism's relationship to test batches, noting the fuzzy boundary and that the section is dominated by self-hosting host-side tests a normal consumer would rarely see.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added Red flags section (screen-and-surface rule + Flag states subsection) between Captures and Why-pipeline

**Routed to Captures:** deferred tests vs test batches (mechanism overlap question)
