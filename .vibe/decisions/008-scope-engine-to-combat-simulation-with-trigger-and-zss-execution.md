---
date: 2026-08-09
status: accepted
---
# Scope `engine` to combat simulation: state execution, physics, hit detection, damage, round flow

**Context:** `.vibe/backlog/001` asked what `engine` covers first, which repos it depends on, and when it becomes worth starting. Decision `004` had already fixed the outer boundary (combat simulation only, not menus/game flow), but left the inside unscoped.

**Decision:** `engine` is a Go library compiling to WASM, depending on `character` (and reading boundary/camera data from `stage`). Its scope, in dependency order: a match/combat state model (fighters, round, timer, position, facing); a trigger/expression evaluator for the MUGEN CNS syntax that `character/cns` deliberately leaves unevaluated as raw strings; state-machine execution (StateDef/Controller interpretation) built on that evaluator; `.zss` script execution (see decision `012`) as an alternative state-execution path; physics and movement (velocity, gravity, ground/air, stage-boundary clamping); hit detection (Clsn box collision); damage, health and combo resolution; and round/match flow (win conditions, KO, timeout, reset). Character-select screens, menus and any other game flow stay out of scope — that's `mode-*` territory (decision `010`). `engine` can start now: its early state-model and evaluator work doesn't require `character-editor` or any viewer to exist first, only `character`'s own parse output.

**Reason:** This is the natural build order for a combat simulator — nothing later on the list is usable without the trigger evaluator and state execution beneath it. Keeping `character` as pure-data parsing and putting all evaluation/execution in `engine` matches `character`'s own stated design constraint (its read path is "the surface a future game engine would consume", not an evaluator itself).

**Rejected alternatives:**
- *Have `character` evaluate CNS triggers itself* — rejected: contradicts `character`'s existing design constraint of staying a pure-data library with no execution semantics; would also force every non-engine consumer (viewers, editors) to carry evaluation logic they don't need.
- *Wait for `character-editor` before starting `engine`* — rejected: the two are independent consumers of `character`'s read path; there's no reason to sequence them.
