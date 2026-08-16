---
status: todo
---
# Validate Wails' Android build for `mode-quick-versus` before treating Android as a confirmed target

## Description
Decision `021` switches native-target packaging from Tauri to Wails, now that the core stays Go. Wails v3's mobile support (Android/iOS) is documented as experimental and explicitly outside its desktop beta's stability promise, not yet a settled production path — a different risk than the one previously flagged for Tauri (Android WebView treating Tauri's asset origin as a non-secure context), but a real one, and equally unverified in this org's own hands so far.

Nothing about this blocks Windows/Mac/Linux, where Wails' desktop support is mature. It only affects `mode-quick-versus`'s Android target (the editors don't target mobile at all, per decision `019`).

## Acceptance Criteria
- [ ] A minimal Wails app (can reuse/extend the existing web-ui-kit shell, doesn't need to wait for full gameplay) built and run on an actual Android device or emulator
- [ ] Confirms the Go backend ↔ JS frontend bridge works on Android the same way it does on desktop (bindings, events at minimum — full feature parity not required for this check)
- [ ] If broken or unworkably immature: fallback options recorded (e.g. Tauri for Android specifically while Wails covers desktop, revisiting the "one shell for everything" preference from decision `021`) rather than silently dropping the Android target
- [ ] Needs a real workstation with Android SDK/emulator or a physical device — not achievable in a headless sandbox with no display server, same limitation noted in backlog `008`'s spike

## Notes
Raised from decision `021`'s rejected-alternatives section, which chose not to pre-emptively split shells (Wails desktop / Tauri mobile) without first confirming Wails' mobile path is actually broken for this use case.
