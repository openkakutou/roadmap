---
status: done
---
# Pick a packaging/stack strategy for `mode-quick-versus` across Windows, Mac, Linux, and Android (web optional)

## Description
`.vibe/decisions/010`'s 2026-08-10 amendment corrects `mode-quick-versus`'s target platforms: Windows, Mac, Linux, and Android as native targets, with web only as a bonus if performance allows there — not the browser-only web app the decision originally scoped. `mode-quick-versus`'s own CLAUDE.md (`Type: frontend (static site, no backend)`, TypeScript/Vite) predates this correction and reflects the old, now-incorrect assumption.

What's still open, needing a Product Owner + technical decision:
- How to hit desktop (Windows/Mac/Linux) and Android from one codebase: a native shell wrapping the same web UI (e.g. Tauri, Capacitor/Cordova), a full rewrite in a native/cross-platform game toolchain, or something else.
- Whether `web-ui-kit` (Web Components) still fits — likely yes if the native shell renders a webview, questionable if the strategy moves away from a web UI entirely.
- Whether `character`/`stage`/`sff`/`engine`'s WASM builds remain the delivery mechanism on every platform, or whether native platforms should consume them as native Go binaries/libraries instead of WASM (both are plausible given these libraries "compile to WASM, no rendering dependency" per `repos.md` — i.e. they're not inherently browser-locked).
- Whether this is `mode-quick-versus`-specific or should become an org-wide convention for every `mode-*` repo (only one mode exists today, so may be premature to generalize — mirrors the reasoning in decision `006` about not designing for a second mode too early).

## Acceptance Criteria
- [x] Packaging/stack strategy chosen and recorded (a `mode-quick-versus` decision if repo-local, a roadmap decision if it turns out to generalize across `mode-*`)
- [x] `mode-quick-versus`'s own CLAUDE.md updated to drop the stale "static site, no backend" framing
- [x] Open question above about WASM vs. native library consumption per platform resolved

## Notes
Raised from `.vibe/decisions/010`'s amendment, prompted by the Product Owner correcting the `openkakutou.github.io` showcase site's copy (it wrongly implied every app, including games, runs only in the browser).

**Resolved 2026-08-16** by `.vibe/decisions/020`: Tauri (webview-wrapping native shell, no rewrite), reusing the existing web build for the web target and the same codebase for Windows/Mac/Linux/Android via Tauri Mobile. WASM stays the delivery mechanism on every platform (Tauri's webview loads it the same as a browser does) — no native Go binary path needed. Turned out to generalize beyond `mode-quick-versus` alone, to the `*-editor` repos' desktop builds too (see backlog `007`, same decision).

**Superseded 2026-08-16 (later same day)** by `.vibe/decisions/021`: backlog `008`'s Rust-vs-Go spike led to staying on Go, which removed the reason for a Rust-based shell (Tauri). Switched to **Wails** — native Go binaries for Windows/Mac/Linux/Android, WASM kept only for the web build. The "WASM everywhere" answer above is no longer current; native Go library consumption is now the answer for every non-web target.
