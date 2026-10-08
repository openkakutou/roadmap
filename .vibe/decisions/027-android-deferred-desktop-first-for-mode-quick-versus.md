---
date: 2026-10-08
status: accepted
---
# Ship `mode-quick-versus` native on desktop first; Android deferred

**Context:** Backlog `010` asked how to bridge desktop OpenGL (`go-gl`) and Android's OpenGL ES (gl4es, a second GLES codepath, or deferring Android). Validating either technical option needs an Android device/emulator and SDK, unavailable in the current environment, and the desktop native renderer isn't proven yet.

**Decision:** Desktop first (Windows/Mac/Linux). Android stays a committed target (decision `010`) but is sequenced after the desktop native renderer ships. gl4es vs. a separate GLES codepath is re-evaluated then, with a real device available. `openkakutou.github.io`'s Android pending pill stays pending until that is resolved.

**Consequences:** Backlog `010` is closed as a sequencing decision; a new item is raised when desktop native is shipped.
