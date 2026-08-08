---
date: 2026-08-09
status: accepted
---
# Scope `stage` as a parser library depending on `sff`; `lifebar` gets no domain library

**Context:** `.vibe/backlog/002` left open whether `stage` and `lifebar` need their own parsing library repos, mirroring `character`.

**Decision:**
- **`stage`** gets a dedicated Go parser library (`stage`), following the same shape as `character`: data model (BGdef, BG elements, camera bounds, boundaries), `.def` parse/serialize (format-preserving round trip), BG element frame/animation resolution, WASM build. It depends on `sff` (decision `007`) for stage sprite sheets, never on `character`. `stage-viewer-web` and `stage-editor` consume `stage`'s WASM build, same pattern as `character-viewer-web`/`character-editor` consume `character`'s.
- **`lifebar`** gets no separate parsing-library repo. Its `.def`-style layout format (element positions, fonts, sprite references, no binary sub-formats of its own) is simple enough to parse directly inside `lifebar-viewer-web` and `lifebar-editor` (TypeScript), each with its own lightweight implementation. Both still depend on `sff`'s WASM build directly to decode the sprite sheets a lifebar references.
- Both domains target MUGEN 1.0/1.1 and Ikemen GO compatibility, validated by fixture-driven tests against real files, the same practice `character` already follows for `.sff`/`.cns`.

**Reason:** `stage`'s format complexity (layered, animated, parallaxed backgrounds) justifies the same investment as `character`. `lifebar`'s format doesn't carry that complexity — it's closer to a flat config file — so a dedicated repo would be overhead without a matching payoff. This is explicitly revisable: if lifebar parsing turns out more complex in practice (e.g. once Ikemen GO's own lifebar extensions are fully accounted for), extracting a `lifebar` library later is a cheap correction, not a redesign.

**Rejected alternatives:**
- *Give `lifebar` a library repo for symmetry with `character`/`stage`* — rejected for now: no evidence yet that the format needs it; symmetry alone isn't a reason to add a repo.
- *Have `lifebar-viewer-web` and `lifebar-editor` share a common lifebar-parsing package* — not adopted at this pass; each implements its own parsing since the two apps are already deliberately separate (decision `002`) and the format is simple enough that duplication cost is low. Can be revisited if drift becomes a real maintenance problem.
