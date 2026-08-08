---
date: 2026-08-08
status: accepted
---
# A `mode-*` repo is a standalone, autonomous game — not a piece requiring external assembly

**Context:** After introducing `mode-quick-versus`/`mode-tag-battle` (decision `005`), it was open whether a `mode-*` repo is itself a complete playable game, or a flow/UI piece that still needs assembling with something else to become one.

**Decision:** Each `mode-*` repo is a complete, autonomous, playable game on its own — `mode-quick-versus` alone is a finished game, not a fragment. Combining multiple modes into a single game (sharing/reusing code across `mode-*` repos) is a real future possibility, but explicitly deferred — not scoped, not a current backlog item.

**Reason:** Product Owner decision. Keeps every `mode-*` repo independently shippable and testable end-to-end without depending on a not-yet-designed combination mechanism. Avoids speculatively designing that mechanism now, before more than one mode exists to learn from.

**Rejected alternatives:** Designing `mode-quick-versus` from the start as a component meant to be embedded by a future multi-mode shell — rejected as premature: no second mode exists yet to validate what such a shell would even need.
