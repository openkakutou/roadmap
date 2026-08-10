---
date: 2026-08-09
status: accepted
---
# Scope `mode-quick-versus` as a standalone web game consuming `engine`, `character`, `stage` and lifebar parsing

**Context:** `.vibe/backlog/003` asked what `mode-quick-versus` needs from `engine`, how it discovers characters, and whether it can start before `engine` exists.

**Decision:** `mode-quick-versus` is a standalone TypeScript/Vite web app (per decision `006`, a complete playable game on its own), consuming the WASM builds of `character`, `stage`, `sff`, and `engine`, plus its own lifebar-rendering logic (mirroring `lifebar-viewer-web`'s approach, per decision `009`). Scope: character roster discovery/selection, stage selection, match setup (rounds/timer), in-match HUD driven by `engine`'s live state, sprite/stage match rendering, keyboard/gamepad input routed into `engine`, round/match result screen, a minimal first-pass CPU opponent, and static-build release packaging. It cannot meaningfully start its match-flow work before `engine` has at least a usable match state model and input handling, but its selection-screen and setup-screen work can start in parallel with early `engine` work.

**Reason:** This is the first complete, shippable game the org produces — it's the concrete validation that `character`+`stage`+`lifebar`+`engine` compose into something playable. Scoping it now (rather than leaving it an idea) lets its early screens start without blocking on all of `engine` being finished.

**Rejected alternatives:**
- *Design `mode-quick-versus` as a component embedded by a future multi-mode shell* — rejected per decision `006`: no second mode exists yet to justify that abstraction.
- *Block all of `mode-quick-versus` until `engine` is fully done* — rejected: unnecessarily serializes independent work (selection/setup screens don't need a finished combat simulator).

**Amendment (2026-08-10):** This decision's "standalone TypeScript/Vite **web app**" framing is corrected — `mode-quick-versus` targets Windows, Mac, Linux, and Android as native platforms, with web as an additional target only if performance allows there, not the primary or only target as originally scoped. Everything else in this decision (feature scope, dependency on `engine`/`character`/`stage`, sequencing) still holds; only the deployment-platform assumption changes. The actual packaging/stack strategy to hit those native + mobile targets (e.g. a native shell wrapping the same web UI, a different toolchain entirely) is not yet decided — tracked as roadmap backlog `006`. `mode-quick-versus`'s own CLAUDE.md ("Type: frontend (static site, no backend)") predates this correction and should be revisited once that strategy is picked, not treated as settled.
