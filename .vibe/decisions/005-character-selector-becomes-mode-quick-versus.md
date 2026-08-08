---
date: 2026-08-08
status: accepted
---
# `character-selector` is reframed as `mode-quick-versus`, the first of several game modes

**Context:** `character-selector` (decision `004`) was framed as a standalone "select screen" piece that uses `engine`. On reflection, it isn't a self-contained piece at all — it's a specific *way of consuming* `engine`: select characters, run a match, show results, for one particular game mode ("quick versus", two players, one match). Other modes are already anticipated, e.g. tag battle (multiple characters per side).

**Decision:** Rename the repo to `mode-quick-versus`. Introduce `mode-<name>` as a repo category: a game mode is the unit that actually consumes `engine`, each one owning its own selection flow, match flow, and result flow for that mode. Future modes (e.g. `mode-tag-battle`) are separate repos following the same pattern, not variants bolted onto `mode-quick-versus`.

**Reason:** `engine`'s scope (decision `004`) is combat simulation for a single match — it has no opinion on how players got there or how many characters per side. That "how players got there" logic differs enough per mode (quick versus vs. tag battle have different selection and flow needs) that modeling it as one `character-selector` with mode branches would reintroduce coupling the composable-pieces principle (decision `004`) is meant to avoid. One repo per mode keeps each mode's flow independently buildable/replaceable, same rationale as one repo per domain viewer/editor.

**Rejected alternatives:** Keeping `character-selector` as a single repo that grows mode-specific branches internally as tag battle etc. are added — rejected as it would recreate a mini-monolith one layer up from `engine`.
