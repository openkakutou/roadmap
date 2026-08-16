---
status: todo
---
# Pick a packaging/stack strategy for standalone desktop builds (Windows, Mac, Linux) of `character-editor`, `stage-editor`, and `lifebar-editor`

## Description
`.vibe/decisions/019` commits every `*-editor` repo to shipping standalone desktop builds on Windows, Mac, and Linux, alongside the web build each already has (see decision `015`'s pattern, extended to the editors). The web build is live for all three as of 2026-08-16; the desktop side is not started.

What's still open, needing a Product Owner + technical decision:
- How to turn the existing TypeScript/Vite web UI into native desktop apps: a webview-wrapping shell (e.g. Tauri, Electron), or something else.
- Whether one shared approach/config is used across all three editors (likely, since they're structurally identical Vite + `web-ui-kit` apps) or each repo decides independently.
- Whether this should share a strategy with `mode-quick-versus`'s own still-open native packaging question (backlog `006`) — that repo needs Windows/Mac/Linux/Android, these need Windows/Mac/Linux only, but the desktop-three overlap enough that one answer might serve both.
- Build/release/signing pipeline: where desktop artifacts get built (per-repo CI vs. shared), how they're versioned relative to each repo's own release process, and where `openkakutou.github.io` links to (e.g. GitHub Releases assets per repo).

## Acceptance Criteria
- [x] Packaging/stack strategy chosen and recorded (a decision in whichever repo if it ends up repo-specific, a roadmap decision if it generalizes across `*-editor` and/or `mode-quick-versus`)
- [ ] First desktop build (any one platform, any one editor) produced and reachable at a stable URL
- [ ] `openkakutou.github.io`'s pending Windows/Mac/Linux platform pills updated to live links as each becomes available

## Notes
Raised from decision `019`, prompted by the Product Owner clarifying `openkakutou.github.io`'s editor cards needed four platform links (web included), not just web.

**Strategy resolved 2026-08-16** by `.vibe/decisions/020`: Tauri, same choice as `mode-quick-versus`'s backlog `006` (the two questions turned out to share one answer, as this item anticipated). What remains open here is purely implementation: setting up Tauri per editor repo, a per-OS CI build matrix, and flipping the showcase page's pending pills to live links as builds land — tracked as each editor's own repo-local backlog once that work starts, not further detailed here.

**Superseded 2026-08-16 (later same day)** by `.vibe/decisions/021`: after backlog `008`'s Rust-vs-Go spike, the core stays Go — which removes decision `020`'s reason for Tauri over Wails. The strategy is now **Wails**, not Tauri, still shared across all three editors and `mode-quick-versus`. Implementation work (per-repo Wails setup, per-OS CI matrix, showcase pill updates) is unchanged in shape, just targets Wails instead.

**Superseded again 2026-08-16 (same day)** by `.vibe/decisions/022`: Wails dropped entirely — no webview anywhere in the org. The three editors no longer share a strategy with `mode-quick-versus` (which moves to a from-scratch `go-gl`+SDL2 renderer, not a fit for forms/panels apps). Editors' strategy is now **[Fyne](https://fyne.io/)**, a native Go GUI toolkit with ready-made widgets (forms, lists, buttons, scrolling) suited to CRUD-style editing UI — chosen over Gio (lower-level, immediate-mode, answers a performance question these apps don't have). Each editor gets its own from-scratch Fyne UI; `web-ui-kit` stays web-only, same "two separate UI implementations" shape decision `022` describes for `mode-quick-versus`. Implementation (per-repo Fyne setup, per-OS CI matrix, showcase pill updates) still not started — tracked as each editor's own repo-local backlog once that work begins.
