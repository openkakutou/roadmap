---
status: done
---
# Create the `lifebar` repo

## Description
Decision `046`. Create `openkakutou/lifebar` with the usual Go library setup (`/vibe:init`, CI, release pipeline with WASM build, license), like `stage`: read/write `fight.def` with Ikemen GO's extensions, layout resolution, sprites through `sff`, fonts through `fnt`. Seed its backlog from what the four existing readers already handle (`lifebar-viewer-web`, `lifebar-editor`, `game/native/internal/lifebar`, `game` web HUD) plus `game` 059's remaining elements, then create the adoption item in each consumer.

🔒 MUST: lifebars as used by real MUGEN 1.0/1.1 and Ikemen GO content, behavior grounded in Ikemen GO's source (decision `041`).

## Acceptance Criteria
- [x] Repo exists with CLAUDE.md, CI and release pipeline, like `stage`/`fnt`
- [x] Backlog seeded, each item linking decision `046`
- [x] Adoption items created in `lifebar-viewer-web`, `lifebar-editor` and `game` (the latter through `game` 060's shared core)
- [x] `repos.md` lists `lifebar` as active; decision `009`'s lifebar line points to `046`
