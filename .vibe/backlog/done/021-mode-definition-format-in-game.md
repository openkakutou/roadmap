---
status: done
---
# Mode definitions in `game`: format, built-in screens, quick versus as data

## Description
Decision `030`: a mode is a definition file (flow of built-in screens + match rules), JSONC validated by a published JSON Schema, loaded by a Go package in `game` (native import, WASM for web). Seed `game`'s backlog with: the mode format spec and schema; the built-in screen-type library refactored out of today's hard-wired quick versus flow; the main menu listing installed modes; quick versus rewritten as the first built-in definition with no behavior change; discovery of installable modes from a `modes/` folder (build-time manifest on web).

Do after `020` (rename).

## Acceptance Criteria
- [ ] `game` backlog items created, each linking decision `030`
- [ ] Ordering against `game`'s existing items 028–030 (decision `029`) written in their Notes
