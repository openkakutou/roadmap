# Repos

Status of every repo in the OpenKakutou organization (github.com/openkakutou). Kept up to date by hand as repos are created or their role changes.

| Repo | Status | Role |
|---|---|---|
| [`character`](https://github.com/openkakutou/character) | active | Read/write Go library for MUGEN/Ikemen GO character files (`.def`/`.sff`/`.air`/`.cns`). Foundation everything else depends on; compiles to WASM, no rendering dependency. |
| [`character-viewer-web`](https://github.com/openkakutou/character-viewer-web) | active | Static TS/Vite web page to browse a character's sprites, palettes, characteristics and animations, via the `character` WASM build. |
| `editor` | planned | Web-based character editor, built on top of `character`. Relationship to `character-viewer-web` (successor? separate app?) not yet decided — see backlog item `001`. |
| `engine` | planned (future) | Game engine in the spirit of Ikemen GO, built on the same extracted libraries as `character`. Scope/timeline not yet defined — see backlog item `002`. |

## Status legend

- **active** — repo exists, under development
- **planned** — named and scoped in the roadmap, repo not created yet
- **idea** — mentioned as a possibility, not committed to
