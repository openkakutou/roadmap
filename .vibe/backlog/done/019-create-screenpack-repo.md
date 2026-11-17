---
status: done
---
# Create the `screenpack` repo

## Description
Decision `029` greenlights an OpenKakutou-specific screenpack format and a `screenpack` repo holding it. Create the repo with the org's usual setup (`/vibe:init`, CI, release pipeline with WASM build, license), then seed its backlog with: the format specification, the JSON Schemas (root `screenpack.json` + one per screen), the Go library (load, validate incl. cross-file checks, resolve fallbacks to the default screenpack, write), the WASM entrypoint, and the default screenpack. The screens to cover are those of `game`'s built-in screen types (game#032): title/main menu, character and stage select (with a sort rule: folder name, display name or author, decision `034`), match setup, VS, options (gameplay, audio, video, controls, appearance), pause, move list, results, continue, victory. Lifebars are not part of a screenpack (decision `031`).

## Acceptance Criteria
- [ ] Repo `openkakutou/screenpack` exists with CLAUDE.md, CI and release pipeline, following the other Go library repos (`sff`, `snd`, `character`)
- [ ] Backlog seeded with the items above, each linking decision `029`
- [ ] `repos.md` status moved from planned to active
