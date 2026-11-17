---
status: todo
---
# Seed `game`'s backlog with the install folder layout

## Description
Decision `031`: content root next to the executable with `chars/`, `stages/`, `lifebars/`, `screenpacks/`, `modes/`, `common/`; lifebar chosen as its own setting; defaults shipped as on-disk content. Create the matching `game` items (lifebar discovery and selection setting, `common/` loading, screenpack discovery from `screenpacks/`, default content on disk, macOS root next to the bundle) and update `game` 028's notes.

## Acceptance Criteria
- [ ] `game` backlog items created, each linking decision `031`
- [ ] `game` 028 notes mention the other content folders
