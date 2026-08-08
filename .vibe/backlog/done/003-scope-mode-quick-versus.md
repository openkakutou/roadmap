---
status: done
---
# Scope `mode-quick-versus`

## Description
`mode-quick-versus` (formerly `character-selector`, see `.vibe/decisions/005`) is the first game mode: standard two-player, one-character-each versus. It consumes `engine` to run the actual match, and owns its own character-selection and result flow.

Not yet scoped: what it needs from `engine` (does `engine` need to exist first, or can selection/flow be built against `character` alone initially?), how characters are discovered/listed, and whether it's a standalone app or a component meant to be embedded by something else. Also worth settling early since `mode-tag-battle` and other future modes will likely share conventions with whatever `mode-quick-versus` establishes first (e.g. how a mode talks to `engine`) — without necessarily sharing code.

## Acceptance Criteria
- [x] `mode-quick-versus`'s initial scope is written down
- [x] Its dependency on `engine`/`character` is stated (including whether it can start before `engine` exists)
- [x] `repos.md` status updated from "idea" to "planned" once scoped

## Notes
Originally raised as `character-selector`; reframed as the first of several `mode-*` repos once the Product Owner clarified it's a way of consuming `engine`, not a standalone piece — see `.vibe/decisions/005`.

Resolved by `.vibe/decisions/010`: standalone TS/Vite app consuming `character`+`stage`+`sff`+`engine` WASM builds plus its own lifebar rendering. Selection/setup screens can start before `engine` is finished; match-flow work needs `engine`'s state model and input handling first. `repos.md` moved to `active`.
