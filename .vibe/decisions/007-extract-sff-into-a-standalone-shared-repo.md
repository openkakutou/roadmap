---
date: 2026-08-09
status: accepted
---
# Extract `.sff` sprite parsing into a standalone `sff` repo shared by `character`, `stage` and `lifebar`

**Context:** `character` currently owns sprite (`.sff` v1/v2) parsing, serialization, and palette resolution as an internal package. Scoping `stage` (decision `009`) and `lifebar` (also `009`) surfaced that both domains need to decode the same `.sff` format — stage backgrounds and lifebar elements both reference sprite sheets in exactly the file format `character` already parses. Coupling `stage`/`lifebar` to the `character` repo just to reach its sprite decoder would be a wrong dependency (a stage or lifebar has nothing to do with a character), and duplicating the decoder in two or three more repos would mean re-fixing every real-world compatibility edge case `character` has already found (see its fixture-driven work on `.sff` v1/v2) in multiple places.

**Decision:** Extract sprite handling into a new standalone repo, `sff`: a Go library, no rendering dependency, compiles to WASM, covering `.sff` v1/v2 parse/serialize and palette resolution (including `.act` overrides) — exactly the current `character/sff` package's scope, unchanged. `character` migrates to depend on it as an external module instead of an internal package (tracked as a `character` backlog item, since it's a concrete repo-local task, not a roadmap item). `stage`, `lifebar-viewer-web` and `lifebar-editor` all depend on `sff` directly, never on `character`.

**Reason:** Sprite decoding is genuinely domain-independent — it's a file format, not a character concept. Extracting it once, where the hard compatibility work already happened, is cheaper than either a wrong dependency edge (domain repos depending on `character` for something that isn't character-specific) or duplicated decoders drifting apart on edge-case fixes.

**Rejected alternatives:**
- *Keep `sff` inside `character`, have `stage`/`lifebar` depend on `character` for it* — rejected: wrong conceptual dependency, and pulls in `character`'s unrelated `.def`/`.air`/`.cns`/`.cmd`/`.zss` parsing as dead weight for repos that only need sprites.
- *Duplicate a minimal `.sff` decoder in each of `stage`, `lifebar-viewer-web`, `lifebar-editor`* — rejected: `character`'s own history shows `.sff` compatibility is hard-won (real-file corpus testing, multiple pixel-format decoders); duplicating it means re-discovering the same bugs three more times and having them drift.
