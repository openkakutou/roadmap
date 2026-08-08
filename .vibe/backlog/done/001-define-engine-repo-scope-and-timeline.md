---
status: done
---
# Define `engine` repo scope and timeline

## Description
`character`'s CLAUDE.md names `engine` — a game engine in the spirit of Ikemen GO, built on the same extracted libraries as `character` — as a future repo. Its high-level boundary is now settled: `engine` is only the combat simulation that runs while two characters fight — not character selection, not menus, not overall game flow (see `.vibe/decisions/004`). What's still open is the detailed scope within that boundary and the timeline.

Needs a Product Owner decision on: what "engine" covers first within combat simulation (rendering? input? full match rules/win conditions?), which repos it depends on beyond `character` (does it need `character-editor` or `character-viewer-web` to exist first?), and roughly when it becomes worth starting relative to `character-editor`.

## Acceptance Criteria
- [x] `engine`'s initial scope is written down within the combat-simulation boundary (what it does and explicitly does not do at first)
- [x] Its dependency on other OpenKakutou repos is stated
- [x] `repos.md` status for `engine` is updated from "planned (future)" to reflect the actual sequencing decision

## Notes
Raised while setting up the `roadmap` repo's initial structure; not yet discussed with the Product Owner.

Resolved by `.vibe/decisions/008`: state model → trigger/expression evaluator → state-machine execution → `.zss` execution (decision `012`) → physics → hit detection → damage/combo → round flow. Depends on `character` and `stage`; can start immediately, not gated on `character-editor`. `repos.md` moved to `active`.
