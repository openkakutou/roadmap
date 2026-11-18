---
status: todo
---
# Architecture Audit Once End-to-End Coverage Exists

## Description
Audit the architecture of `engine` and `game` (`/vibe:audit` in each repo), then turn what is kept into backlog items. Postponed by the Product Owner on 2026-11-18: wait until there are more game elements, because a refactor is only worth doing when tests protect it.

## Acceptance Criteria
- [ ] Triggered only once both conditions hold: engine's end-to-end scenarios run through `Tick` on the reference fixtures (engine#054, then #035), and `game` has started its screens and modes (game 031+)
- [ ] The kept findings become backlog items in the repos concerned

## Notes
Signals already seen on 2026-11-18:
- `evaluator.Context` keeps gaining fields (locals, persistent counters, `.zss` flag, get-hit variables).
- `.cns` and `.zss` run on two separate paths.
- The hit-pause handling is split between those two paths.
