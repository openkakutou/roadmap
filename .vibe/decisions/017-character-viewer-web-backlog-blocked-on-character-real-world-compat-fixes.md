---
date: 2026-08-10
status: accepted
---
# `character-viewer-web`'s backlog is blocked on `character`'s real-world file compatibility fixes

## Context

The user hit a `character-viewer-web` load failure on a real community character file:

```
Could not load character: character: parsing combat logic bytes: cns: line 453: malformed section header "[State 110, 1"
```

This traces to `character`'s own backlog item `042-cns-parse-rejects-section-header-missing-closing-bracket.md`: `cns.Parse` hard-errors on any `[State ...`/`[Statedef ...]` header line missing its closing `]`, a typo real MUGEN/Ikemen engines tolerate. A full corpus scan (`~/workspace/ikemen-quick-versus/chars`, 717 real `.def` files) found this is the single most common `character.Load` failure — **109 files (~15%)** — and surfaced a whole cluster of sibling real-world-compatibility gaps in the same parser family, all still `status: todo` as of this decision: items `043`–`051` (non-key-value lines inside `.cns`/`.def` blocks, `.air` interpolate directives, boolean header fields rejecting trigger expressions, Clsn/frame line regex strictness, backslash path separators, case-sensitive file resolution, confusing error on a `.def` missing `[Files]`).

`character-viewer-web` is a read-only viewer whose entire purpose is loading and displaying real community character files via `character`'s WASM build. Every one of these parser gaps surfaces to its end users as the same class of opaque load failure, regardless of which viewer feature is being built at the time (sprite browser, animation player, etc.) — new viewer features can't be meaningfully exercised or demoed against real files while ~15%+ of the corpus fails at the parsing step, before any viewer code even runs.

## Decision

`character-viewer-web`'s own backlog (feature work: items `005` and onward) is **blocked** — no new item should be started — until `character`'s real-world-compatibility parser backlog (item `042`, and the sibling items `043`–`051` it surfaced) is resolved and the WASM pin in `character-viewer-web` is bumped to a `character` release that includes the fixes.

This is a full gate on the repo's backlog, not a per-item `depends_on` link: the failure mode is systemic (any real file can hit any of these gaps), not scoped to the specific items that happen to exercise sprites/animations.

## Reason

- The bug is entirely upstream, in the shared `character` library — no amount of `character-viewer-web`-side work fixes it, and workarounds there (e.g. catching/skipping parse errors) would need to be duplicated again in `character-editor` and `engine`, the other two consumers of the same parser.
- Feature work in the viewer is validated against real character files; building/demoing against a parser that fails on ~15%+ of a real corpus produces unreliable signal and wastes review effort on failures that aren't the viewer's fault.
- Fixing the shared foundation once benefits every downstream consumer (`character-viewer-web`, `character-editor`, `engine`), not just the viewer — the org's stated compatibility target (`repos.md`: "validated against real community files — not just the spec") is `character`'s responsibility to meet before its consumers build further on top of it.

## Rejected alternatives

- **Keep building `character-viewer-web` features in parallel, treat each load failure as a separate one-off bug**: rejected — the corpus scan already shows this isn't a long tail of rare edge cases but a small number of systemic parser gaps affecting a large fraction of real files; chasing them one viewer-side symptom at a time duplicates the same root-cause fix in the wrong repo.
- **Scope the block to only the specific `character-viewer-web` items that exercise the failing file patterns**: rejected — the failure is not tied to any specific viewer feature (any loaded file can hit any of the parser gaps), so a per-item `depends_on` link would understate the blast radius and likely miss items as new ones are added.

## Unblocks when

`character`'s items `042`–`051` reach `status: done` (or are explicitly triaged/closed) and `character-viewer-web`'s WASM pin is bumped to a `character` release tag that includes them, per the existing WASM release propagation policy (`.vibe/decisions/016`).
