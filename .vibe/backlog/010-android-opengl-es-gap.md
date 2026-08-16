---
status: todo
---
# Resolve desktop OpenGL vs. OpenGL ES for `mode-quick-versus`'s Android build

## Description
Decision `022` adopts `go-gl` (desktop OpenGL bindings) + SDL2 for `mode-quick-versus`'s native rendering, mirroring Ikemen GO's own stack. SDL2 itself supports Android (unlike GLFW), which is necessary but not sufficient: Android only exposes **OpenGL ES**, not desktop OpenGL, so `go-gl`'s calls don't run as-is on an Android device. Even Ikemen GO — the org's own reference implementation — hasn't fully solved this: its official Android build path is a Docker-based APK build, and the more complete Android port lives in a separate community fork using [gl4es](https://github.com/ptitSeb/gl4es) (a desktop-OpenGL-to-GLES translation layer), not fully mainlined upstream.

## Options to evaluate
- **gl4es**, matching the community Ikemen GO Android fork: translation layer between the existing desktop-OpenGL rendering code and Android's GLES — least code change, but an extra dependency of unclear maintenance status, and translation layers can have their own performance/compatibility gaps.
- **A second, GLES-targeted rendering codepath** for Android specifically: more code to maintain (a third UI/rendering implementation alongside web and desktop-native), but no translation-layer risk.
- **Deprioritize Android** for `mode-quick-versus`'s first releases, ship Windows/Mac/Linux first, revisit once the desktop native renderer is proven — not a rejection of the Android target (still committed per decision `010`), just a sequencing question.

## Acceptance Criteria
- [ ] One option chosen and recorded, with the reasoning (this doesn't have to be this roadmap item alone — could land as `mode-quick-versus`'s own decision if it turns out repo-local)
- [ ] If gl4es or an equivalent is chosen: a minimal `go-gl`-rendered scene confirmed actually running on an Android device or emulator
- [ ] If a separate GLES codepath is chosen: scoped as its own `mode-quick-versus` backlog item, not conflated with the desktop renderer's
- [ ] `openkakutou.github.io`'s Android pending pill only flips to live once this is actually resolved, not before

## Notes
Raised from decision `022`, replacing the now-moot Wails-Android-maturity item (backlog `009`, done) — same underlying concern (is Android actually reachable), different technical cause now that Wails is dropped. Needs a real Android device/emulator and SDK to validate — not achievable in the headless sandbox that produced `benchmarks/render-lang-spike/` (no display server, no Android tooling), same limitation noted throughout this thread.
