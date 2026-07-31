# 29ba751 - pre_tool_use.py: exempt the user's Claude memory directory from the scope-lock

During a scoped /next or /done, saving communication feedback to Claude's memory directory was blocked by the scope-lock, because the memory directory is never in a batch's Files list - a false positive that silently prevented capturing feedback at the moment it is given. A path-shape helper (_is_memory_dir: a memory directory beneath a .claude directory, matched by shape never a hardcoded machine path) now exempts memory writes, mirroring the method-docs exemption. An in-session import test confirmed memory paths are allowed while non-listed non-memory paths are still denied, and a bare memory/ dir with no .claude ancestor is correctly not exempt.

**Files touched:**
- plugin/si-plugin/hooks/pre_tool_use.py

**Routed to Captures:** none
