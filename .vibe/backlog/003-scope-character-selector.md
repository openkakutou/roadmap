---
status: todo
---
# Scope `character-selector`

## Description
`character-selector` (the character select screen) is identified as a separate repo from `engine`, per `.vibe/decisions/004` — it uses `engine` to let a selected character be tried/previewed, and uses `character` (or `character-viewer-web`'s approach) to read what's selectable, but isn't part of `engine` itself.

Not yet scoped: what it actually needs from `engine` (does `engine` need to exist first, or can selection be built against `character` alone initially?), how characters are discovered/listed, and whether it's a standalone app or a component meant to be embedded by something else.

## Acceptance Criteria
- [ ] `character-selector`'s initial scope is written down
- [ ] Its dependency on `engine`/`character` is stated (including whether it can start before `engine` exists)
- [ ] `repos.md` status updated from "idea" to "planned" once scoped

## Notes
Raised when the Product Owner distinguished `character-selector` from `engine`, explicitly ruling out the Ikemen precedent of folding select-screen logic into the engine.
