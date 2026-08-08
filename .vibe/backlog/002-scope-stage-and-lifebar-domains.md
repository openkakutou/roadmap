---
status: todo
---
# Scope the `stage` and `lifebar` domains

## Description
`stage-viewer-web`/`stage-editor` and `lifebar-viewer-web`/`lifebar-editor` are named in the roadmap (`repos.md`), following the same viewer/editor split as the `character` domain, but neither domain has been scoped yet.

Open questions to resolve with the Product Owner before any of these repos starts:
- Does `stage` need its own parsing library repo (a `stage` equivalent of `character`, for MUGEN/Ikemen stage/background `.def` files), the same way `character-viewer-web`/`character-editor` depend on `character`? Lifebars are typically a single `.def`-style config file — does `lifebar` need a separate library repo at all, or is parsing simple enough to live directly in `lifebar-viewer-web`/`lifebar-editor`?
- Relative priority/sequencing against `character-editor` and `engine`.

## Acceptance Criteria
- [ ] Decide whether `stage` and/or `lifebar` need their own parsing library repo, recorded as a decision
- [ ] `repos.md` updated with any new library repo, and statuses moved from "idea" to "planned" once scoped
- [ ] Rough sequencing relative to `character-editor`/`engine` stated

## Notes
Raised when `stage-editor`, `stage-viewer-web`, and `lifebar-viewer-web` were added to the roadmap alongside the already-noted `lifebar-editor`.
