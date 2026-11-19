---
date: 2026-11-19
status: accepted
---
# Architecture audit of 2026-11-19: what was fixed, and the priority items

**Context:** A light audit of the plan and architecture found five issues: two runtimes in `game` (decision `045`), lifebar read in four places (decision `046`), editors built twice (decision `047`), broken version propagation, and stale decisions.

**Decision:**
- **Fixed directly:**
  - `engine` was tagged v2.x with a module path without `/v2`, so Go could not resolve its tags and `game` pinned a raw commit. `engine` v2.23.0 moves to `github.com/openkakutou/engine/v2`; `game` now pins `engine/v2 v2.23.0`. Decisions `016`/`025` propagation applies again to `engine`.
  - `engine` pinned `stage` v0.13.0 and `sff` v0.8.0 while `game` used v0.17.0 and v0.8.1; aligned in `engine` v2.23.0.
  - The 7 web apps declared `@openkakutou/web-ui-kit` `^0.17.0`, which on a 0.x version means `<0.18.0`: releases 0.18–0.23 reached no app. All moved to `^0.23.1`. Because a caret range on 0.x stops at the next minor, `web-ui-kit`'s own release step must bump the consumers' range on every minor release (decision `016` propagation applies).
  - Decision `004` (menus and game flow out of scope) is superseded by `029` and `030`; decision `006` by `030`. Their status now says so.
- **Priority for `vibe:next-task`**, right after the combat milestone's current engine step: roadmap `026` (create `lifebar`), then `game` `060` (shared Go core). No `game` 031+ item starts before `game` `060` is done.

**Reason:** Product Owner direction (2026-11-19): turn every audit point into backlog work and do it first.
