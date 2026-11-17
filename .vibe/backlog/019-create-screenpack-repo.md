---
status: todo
---
# Create the `screenpack` repo

## Description
Decision `029` greenlights an OpenKakutou-specific screenpack format and a `screenpack` repo holding it. Create the repo with the org's usual setup (`/vibe:init`, CI, release pipeline with WASM build, license), then seed its backlog with: the format specification, the JSON Schemas (root `screenpack.json` + one per screen), the Go library (load, validate incl. cross-file checks, resolve fallbacks to the default screenpack, write), the WASM entrypoint, and the default screenpack.

## Acceptance Criteria
- [ ] Repo `openkakutou/screenpack` exists with CLAUDE.md, CI and release pipeline, following the other Go library repos (`sff`, `snd`, `character`)
- [ ] Backlog seeded with the items above, each linking decision `029`
- [ ] `repos.md` status moved from planned to active
