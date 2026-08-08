# Repos

Status of every repo in the OpenKakutou organization (github.com/openkakutou). Kept up to date by hand as repos are created or their role changes.

| Repo | Status | Role |
|---|---|---|
| [`character`](https://github.com/openkakutou/character) | active | Read/write Go library for MUGEN/Ikemen GO character files (`.def`/`.sff`/`.air`/`.cns`). Foundation everything else depends on; compiles to WASM, no rendering dependency. |
| [`character-viewer-web`](https://github.com/openkakutou/character-viewer-web) | active | Visualize and control a character: browse sprites, palettes, characteristics and animations, and trigger animations/moves live, via the `character` WASM build. Read-only. |
| `editor` | planned | Modify and/or create a character: read+write UI on top of `character`. Separate app from `character-viewer-web`, not a successor to it — see `.vibe/decisions/002`. |
| `engine` | planned (future) | Game engine in the spirit of Ikemen GO, built on the same extracted libraries as `character`. Scope/timeline not yet defined — see `.vibe/backlog/001`. |

## Status legend

- **active** — repo exists, under development
- **planned** — named and scoped in the roadmap, repo not created yet
- **idea** — mentioned as a possibility, not committed to
