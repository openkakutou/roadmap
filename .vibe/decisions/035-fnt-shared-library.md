---
date: 2026-11-17
status: accepted
---
# Bitmap fonts (`.fnt`) get a shared `fnt` library, like `sff` and `snd`

**Context:** Backlog `016`. Real lifebars render names, timers and combo counters with MUGEN/Ikemen GO `.fnt` fonts; `game` needs them for its HUD (game#049), and `lifebar-viewer-web`/`lifebar-editor` for faithful previews. No repo parses them. Screenpacks use standard fonts (decision `029`), so they are not consumers.
**Decision:** A new **`fnt`** repo: read/write Go library for `.fnt` v1 and v2 (glyph map, sprite-based v2 fonts through `sff`), compiled to WASM, no rendering dependency — the same shape as `sff` (`007`) and `snd` (`026`). Consumers: `game`, `lifebar-viewer-web`, `lifebar-editor`.
**Reason:** Three consumers across Go (native game) and TypeScript (web apps) must agree on parsing; one Go library imported natively and via WASM avoids drifting implementations — the argument already used for `sff`, `snd` and `screenpack`.
**Rejected alternatives:** *Inside `game`* — the lifebar apps would reimplement it. *Inside `sff`* — `.fnt` is its own format with its own consumers; `sff` stays sprite-only.
