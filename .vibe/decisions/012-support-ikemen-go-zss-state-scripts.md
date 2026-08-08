---
date: 2026-08-09
status: accepted
---
# Support Ikemen GO's `.zss` Lua-like state scripts, split between parsing (`character`) and execution (`engine`)

**Context:** Ikemen GO allows a character's state logic to be written as `.zss` — a Lua-like scripting format — as an alternative to the classic `.cns` state definitions. A character uses one or the other, never both, so this isn't a blocking dependency for anything else, but full MUGEN/Ikemen GO compatibility (the stated target — see decision `009`'s compatibility note) is incomplete without it.

**Decision:** `character` gains a `zss` package that parses `.zss` files into a structured document model, following the same principle as `cns`: script bodies and trigger-like expressions are kept as unevaluated raw text at this layer, not interpreted. `engine` is responsible for actually executing `.zss` scripts at runtime, alongside its CNS trigger evaluator — this will likely require embedding a Lua-compatible interpreter, which would be `engine`'s first third-party dependency. Which specific interpreter (or whether to write a minimal compatible subset by hand) is deliberately left to be decided during that item's implementation, not now.

**Reason:** Keeps the same read-path/write-path and parse/execute split already established for `.cns`: `character` stays a pure-data library with zero evaluation semantics, `engine` owns all runtime interpretation. Committing to supporting `.zss` now (rather than leaving it an open question) is justified by the org's explicit MUGEN+Ikemen compatibility target — a character defined via `.zss` should be just as usable as one defined via `.cns`.

**Rejected alternatives:**
- *Leave `.zss` support as an unscoped open question* — rejected: the compatibility target explicitly includes Ikemen GO, and `.zss` is a real, non-niche way Ikemen GO characters are built; deferring it indefinitely would leave a known gap unaddressed.
- *Parse and evaluate `.zss` together in one step inside `character`* — rejected: would break `character`'s pure-data design constraint and duplicate evaluation logic that already needs to exist in `engine` for CNS triggers.
