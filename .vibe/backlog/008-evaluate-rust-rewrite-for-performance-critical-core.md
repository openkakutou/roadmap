---
status: todo
---
# Evaluate whether performance-critical core libraries (starting with `engine`) should be rewritten in Rust

## Description
Raised while deciding `mode-quick-versus`/editors' desktop packaging strategy (`.vibe/decisions/020`): the Product Owner's stated top priority for that decision was performance, explicitly open to moving to Rust if needed, and unbothered by multiple execution paths as long as each is tested. Decision `020` itself only settled the desktop *shell* (Tauri, Rust-based) — it deliberately did not decide whether the underlying Go libraries (`character`, `stage`, `sff`, and especially `engine`, whose per-frame combat simulation is the most performance-sensitive code in the org) should themselves move to Rust.

Go compiled to WebAssembly (`GOOS=js GOARCH=wasm`) embeds Go's own runtime (goroutine scheduler, garbage collector) in the output, which is a known source of larger binaries and GC-pause latency versus Rust-compiled WASM, which has no GC and a much smaller runtime. Whether this actually matters here is unproven — no profiling exists yet, because `engine`'s simulation loop (physics, hit detection, round flow) is still being built.

## Acceptance Criteria
- [ ] `engine`'s core simulation loop reaches a state where it can be profiled under realistic load (e.g. driven by `mode-quick-versus`'s in-match HUD/rendering work)
- [ ] Actual GC-pause / frame-time / binary-size data gathered for the Go/WASM build, in both browser and Tauri-webview contexts
- [ ] A decision recorded (roadmap, since it would touch `character`/`stage`/`sff`/`engine` — foundational, cross-repo) on whether a Rust rewrite is justified, and if so which library first (`engine` alone vs. all four) and how migration is sequenced without freezing feature work
- [ ] If rewrite is rejected, the reasoning (e.g. "GC pauses proved negligible for a turn/frame budget of Xms") is recorded so the question isn't silently reopened without new evidence

## Notes
Deliberately not decided speculatively in decision `020` — rewriting `character`/`stage`/`sff`/`engine` is a large, foundational, multi-repo undertaking; committing to it without profiling data would be premature optimization. This item exists so the question isn't lost, not to imply the answer is already "yes."
