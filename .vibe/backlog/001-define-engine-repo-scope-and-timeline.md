---
status: todo
---
# Define `engine` repo scope and timeline

## Description
`character`'s CLAUDE.md names `engine` — a game engine in the spirit of Ikemen GO, built on the same extracted libraries as `character` — as a future repo, but with no defined scope, dependencies beyond `character`, or timeline. Unlike `editor` (scope now clarified, see `.vibe/decisions/002`), `engine` remains an open placeholder.

Needs a Product Owner decision on: what "engine" covers first (rendering? input? full match simulation?), which repos it depends on beyond `character` (does it need `editor` or `character-viewer-web` to exist first?), and roughly when it becomes worth starting relative to `editor`.

## Acceptance Criteria
- [ ] `engine`'s initial scope is written down (what it does and explicitly does not do at first)
- [ ] Its dependency on other OpenKakutou repos is stated
- [ ] `repos.md` status for `engine` is updated from "planned (future)" to reflect the actual sequencing decision

## Notes
Raised while setting up the `roadmap` repo's initial structure; not yet discussed with the Product Owner.
