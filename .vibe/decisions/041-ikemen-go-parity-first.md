---
date: 2026-11-18
status: accepted
---
# Ikemen GO parity first: reproduce whatever Ikemen GO does, starting with special states

**Context:** The first conformance run (engine 030, `engine/docs/conformance.md`) showed that only 4 of 442 real characters ever leave their first state, because the engine never runs the special states -3, -2 and -1, and that `character` refuses file forms Ikemen GO accepts. The Product Owner: everything must be done to reproduce Ikemen GO's behavior.
**Decision:**
- **Ikemen GO's observable behavior is the specification** for `engine` and `character` (decision `038` made it the verification reference): execution order, defaults, tolerance of malformed files, file search paths. When OpenKakutou differs, OpenKakutou is wrong, unless the difference is an OpenKakutou-only extension (decision `028`). Every such behavior is grounded in Ikemen GO's source, cited by file:line and commit.
- **Order of decision `036` amended:** engine 037 (special states -3/-2/-1 every tick) comes first: 027, 028 and 036 now depend on it. The defects found by the run (engine 038 command matcher crash, 039 `VarSet` form, 040 `PlaySnd` common sounds) and `character` 074-077 (file forms Ikemen GO accepts, every state file and `stcommon` searched like Ikemen GO) are picked as soon as they are eligible. Then 027, 028, 041 (expression grammar) and the rest of `036`'s order.
- **The conformance harness is re-run after each step** and its Results updated, so progress is measured, not claimed; the differential tests against Ikemen GO (engine 036, game 051) then prove behavior frame by frame.
**Reason:** Product Owner direction; the run showed the special states block every other measurement.
**Rejected alternatives:** *Keep `036`'s order (controllers and triggers first)* — nothing they add is reachable while no character leaves state 0. *Tolerate only "reasonable" malformed files* — Ikemen GO loads them; refusing them breaks real content.
