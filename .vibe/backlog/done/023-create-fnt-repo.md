---
status: done
---
# Create the `fnt` repo

## Description
Decision `035`. Create `openkakutou/fnt` with the usual Go library setup (`/vibe:init`, CI, release pipeline with WASM build, license), seed its backlog (`.fnt` v1 read, v2 read through `sff`, write, WASM entrypoint, real-file validation), and add it to `repos.md` as active.

🔒 MUST: `.fnt` v1 and v2 as used by real MUGEN 1.0/1.1 and Ikemen GO content.

## Acceptance Criteria
- [ ] Repo exists with CLAUDE.md, CI and release pipeline, like `sff`/`snd`
- [ ] Backlog seeded, each item linking decision `035`
- [ ] `repos.md` lists `fnt` as active
