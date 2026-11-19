---
date: 2026-11-19
status: accepted
---
# `lifebar` gets a shared Go library; amends decision `009`

**Context:** Decision `009` gave lifebar no library because the format looked simple and only two TypeScript apps read it, and said explicitly that extracting one later is a cheap correction if duplication becomes a problem. The lifebar format is now read in `lifebar-viewer-web`, `lifebar-editor`, `game/native/internal/lifebar` (Go) and the web HUD of `game` — two languages, and every reader must match Ikemen GO (🔒 MUST, decision `041`); `game` 059 still has elements to add, in each reader.

**Decision:** Create a `lifebar` repo: Go library, WASM build, no rendering dependency, depending on `sff` and `fnt`, like `stage`. It parses (and writes) `fight.def` and its Ikemen GO extensions, and resolves layout. `lifebar-viewer-web`, `lifebar-editor` and `game` (through its shared core, decision `045`) replace their own parsers with it.

**Reason:** Same argument as `screenpack` (decision `029`): consumers in two languages must agree on parsing and Ikemen GO behavior; one Go implementation imported natively and through WASM avoids four drifting ones.

**Rejected alternatives:** *Keep four parsers* — each Ikemen GO fix four times. *A shared TypeScript package* — `game` native is Go.

**Effect:** roadmap backlog `026`; prioritized by decision `048`.
