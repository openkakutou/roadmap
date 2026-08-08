---
date: 2026-08-08
status: accepted
---
# OpenKakutou builds composable pieces, not a full game framework like MUGEN/Ikemen

**Context:** MUGEN and Ikemen GO are monolithic: a single engine owns file parsing, rendering, combat simulation, the character select screen, menus, and overall game flow together. While scoping `engine` and a newly-identified character-select component, the question came up of where the select screen belongs.

**Decision:** OpenKakutou is explicitly not trying to reproduce a full game framework. Each concern gets its own repo with a narrow, well-defined boundary, composed by whoever builds an actual game on top:
- `engine` is only the combat simulation that runs while two characters fight — not rendering-agnostic in the sense `character` is (it does run a match), but it does not own character selection, menus, or overall game flow.
- The character select screen is a separate component (`character-selector`) that *uses* `engine` (and `character`) but is not part of it.
- Menus, options, and full game flow are out of scope for this org entirely, unless a future decision explicitly changes that.

**Reason:** Matches the pattern already set by `character`: single-purpose, composable pieces (Product Owner's stated goal — not managing "entire games like Mugen and Ikemen"). Keeping `engine` scoped to match simulation only avoids it re-absorbing the concerns `character`'s own extraction was designed to avoid, and keeps `character-selector` free to be reused or replaced independently of `engine`.

**Rejected alternatives:** Folding character selection into `engine` (the Ikemen precedent) — rejected as it would recreate the monolith this org is deliberately not building.
