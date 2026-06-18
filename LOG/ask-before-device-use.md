# [HASH] — Added device/hardware access consent — confirm before touching a connected device (plugin-behaviour.md), ask-before-using step at the verification point (next-build.md), + FAQ; red flag [device-access-consent] fix built, kept open pending reinstall. Goal-session batch 1 of 5.

Builds the fix for the open red flag [device-access-consent], which arose when a 2026-06-17 Taskflow build connected to a reachable Pixel 6 over wireless adb and tested on it without asking. Two gaps fed that: the build deferred its on-device checks on an untested assumption that no device was available, and when a device was in fact there it was used silently.

The fix is consent. plugin-behaviour.md gains a "Device and hardware access" section, placed right after File safety: confirm with the user before connecting to or acting on their physical device or external hardware (adb to a phone, flashing firmware, driving any attached hardware), with the why inline — an adb-class channel is powerful and reaches past installing one app into the user's whole device, so silent use is a consent surprise; this is the same confirm-first rule that already covers outward-facing and hard-to-reverse actions, extended to hardware. next-build.md's test step gains a paired note: before deferring a test because a device or environment "isn't available here," don't assume it's absent — ask whether one is available, and before using any connected device ask permission ("May I use your connected device to test this?") and wait for a yes.

An FAQ entry ("Will Claude use my phone or another device to test my app?") and its index line ship so a consumer who meets the permission ask understands it.

The red flag stays OPEN, deliberately — not resolved at build time. The installed host still behaves the old way until reinstall, so resolution waits on the deferred test: the first on-device build that asks permission before connecting rather than connecting silently.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added "## Device and hardware access" consent rule after File safety.
- plugin/si-plugin/docs/next-build.md: added the don't-assume-absent / ask-permission note at the test-entries step.
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md: added the device-consent FAQ entry + index line.
- QUEUE.md: removed the batch from Batches; updated red flag [device-access-consent] (fix built, stays open); added its host-side deferred-test line.

**Routed to Captures:** none (run-level captures recorded under batch 2's entry).
