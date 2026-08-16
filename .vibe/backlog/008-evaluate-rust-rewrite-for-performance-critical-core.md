---
status: todo
---
# Evaluate whether performance-critical core libraries (starting with `engine`) should be rewritten in Rust

## Description
Raised while deciding `mode-quick-versus`/editors' desktop packaging strategy (`.vibe/decisions/020`): the Product Owner's stated top priority for that decision was performance, explicitly open to moving to Rust if needed, and unbothered by multiple execution paths as long as each is tested. Decision `020` itself only settled the desktop *shell* (Tauri, Rust-based) — it deliberately did not decide whether the underlying Go libraries (`character`, `stage`, `sff`, and especially `engine`, whose per-frame combat simulation is the most performance-sensitive code in the org) should themselves move to Rust.

Go compiled to WebAssembly (`GOOS=js GOARCH=wasm`) embeds Go's own runtime (goroutine scheduler, garbage collector) in the output, which is a known source of larger binaries and GC-pause latency versus Rust-compiled WASM, which has no GC and a much smaller runtime. Whether this actually matters here is unproven — no profiling exists yet.

**Timing matters.** `engine`'s own backlog already has 4 items done in Go (`001`-`003`, `008`: combat state model, CNS trigger evaluator, state machine execution, input/command matching) — real, working, tested code that a full Rust rewrite would discard. Its two most performance-critical remaining items, `005` (physics/movement) and `006` (hit detection), haven't been started yet. Waiting until the whole simulation loop is finished before profiling — as this item originally proposed — would mean writing `005`/`006` in Go first and only then finding out whether they should have been Rust, maximizing throwaway work instead of avoiding it. A cheap, targeted spike, done *before* `005` starts, avoids that without resorting to a blind guess.

## Acceptance Criteria
- [ ] A small synthetic benchmark — representative of one simulation tick under realistic match load (N trigger evaluations + state transitions + collision checks per frame) — built in both Go/WASM and Rust/WASM, before `engine` backlog item `005` (physics/movement) starts
- [ ] Frame-time, GC-pause, and binary-size data gathered for both, run inside an actual Tauri webview (not just a browser) since that's the real deployment context
- [ ] A decision recorded (roadmap, since it would touch `character`/`stage`/`sff`/`engine` — foundational, cross-repo) on whether a Rust rewrite is justified, and if so which library first (`engine` alone vs. all four) and how migration is sequenced without freezing feature work
- [ ] If rewrite is rejected, the reasoning (e.g. "GC pauses proved negligible for a turn/frame budget of Xms") is recorded so the question isn't silently reopened without new evidence
- [ ] Either way, the decision lands before `engine` backlog item `005` starts, so `005`/`006` are written once, in the right language, not written in Go then possibly redone

## Notes
Deliberately not decided speculatively in decision `020` — rewriting `character`/`stage`/`sff`/`engine` outright, with no data, would be premature optimization. But deferring indefinitely has a real, growing cost (more Go code to discard the longer it waits), so this is scoped as a fast, cheap spike gated in front of `engine`'s next backlog item, not an open-ended "someday" question.
