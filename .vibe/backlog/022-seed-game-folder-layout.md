---
status: todo
---
# Seed `game`'s backlog with the install folder layout

## Description
Decisions `031`, `032`, `033`: content root next to the executable with `chars/`, `stages/`, `lifebars/`, `screenpacks/`, `modes/`, `common/`; lifebar chosen as its own setting; defaults shipped as on-disk content. Create the matching `game` items (lifebar discovery and selection setting, `common/` loading, screenpack discovery from `screenpacks/`, default content on disk, desktop programs side by side at the root, `config/` with per-platform sections in `video.json`/`controls.json`, cross-platform file rules; Android folder picker to fold into roadmap `014`) and update `game` 028's notes.

## Acceptance Criteria
- [ ] `game` backlog items created, each linking decisions `031`-`033`
- [ ] `game` 028 notes mention the other content folders
