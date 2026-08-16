---
date: 2026-08-16
status: accepted
---
# Adopt Tauri as the packaging strategy for `mode-quick-versus` (Web + Windows + Mac + Linux + Android) and for the `*-editor` repos' desktop builds (Windows + Mac + Linux)

**Context:** Backlog `006` left `mode-quick-versus`'s native-platform packaging strategy open (decision `010`'s amendment: Windows, Mac, Linux, and Android as native targets, web only "if performance allows"). Backlog `007` left the same question open for `character-editor`/`stage-editor`/`lifebar-editor`'s planned desktop builds (decision `019`), explicitly flagging that one answer might serve both. The Product Owner asked directly: keep Windows/Mac/Linux for `mode-quick-versus`, and confirm whether web is still feasible alongside them.

Every one of these apps — `mode-quick-versus` and the three editors — is already a TypeScript/Vite frontend consuming `character`/`stage`/`sff`/`engine` as WebAssembly modules, with `web-ui-kit` for non-real-time UI. None needs server-side logic; all are "no backend" by design already.

**Decision:** Adopt [Tauri](https://tauri.app/) as the shared packaging strategy: it wraps the existing Vite web build in a native shell using the OS's own webview (WebView2 on Windows, WebKit on Mac, WebKitGTK on Linux) rather than bundling a full browser runtime — no rewrite of the existing TypeScript/`web-ui-kit`/WASM-loading code, since the shell just renders the same web app. Consequences per app:
- **`mode-quick-versus`**: one codebase, four-plus targets — the existing web build deploys as-is to GitHub Pages (web is not just feasible, it's close to free: it's the same `dist/` output the desktop builds start from), and Tauri produces the Windows/Mac/Linux desktop binaries. Tauri Mobile (Tauri v2) extends the same approach to Android, preserving decision `010`'s original Android target instead of dropping it — not explicitly requested in this pass, kept unless the Product Owner says otherwise.
- **`character-editor`/`stage-editor`/`lifebar-editor`**: same Tauri wrapper, Windows/Mac/Linux only (no mobile target scoped for the editors) — resolves backlog `007` with the same stack, as it anticipated.

Each repo's own backlog gets the concrete implementation work (Tauri setup, CI build matrix per OS, code signing if needed, release artifact publishing) — not tracked here, this decision only settles the stack.

**Reason:** One stack answers both open questions (backlog `006` and `007`) with no per-repo bespoke choice, and fits every app's existing shape exactly: already a pure client-side web app with no backend, so a webview-wrapping shell is the smallest possible step to native, not a rewrite. Using the OS's own webview instead of bundling Chromium (the Electron alternative) keeps binaries small and matches this org's general preference for lean tooling (Go compiling straight to WASM elsewhere, no framework on the showcase site). Getting the web target essentially for free (same build artifact) directly answers whether web is "worth attempting" alongside desktop — yes, since it costs nothing beyond what desktop already requires.

**Rejected alternatives:**
- *Electron* — rejected: bundles a full Chromium + Node runtime per app, meaningfully heavier distribution for no capability this project needs (no deep Node-API/OS integration beyond a window and WASM execution, which the browser platform already provides).
- *A full rewrite in a native/cross-platform game toolchain (e.g. a game engine with its own desktop/mobile export)* — rejected: would abandon the existing WASM-consuming TypeScript/`web-ui-kit` codebase and the web target entirely, disproportionate to what's needed (a window and a webview, not custom rendering).
- *Decide per-repo instead of one shared answer* — rejected: the four apps are structurally identical in what they need from packaging (client-side web app → also-native shell); no signal yet that any of them needs something different.
