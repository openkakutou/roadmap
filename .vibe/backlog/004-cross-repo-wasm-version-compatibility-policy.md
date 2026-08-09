---
status: todo
---
# Define a cross-repo WASM version-compatibility policy

## Description
`character`, `stage`, `sff`, and `engine` each release their own WASM builds independently (own tags, own release pipelines). They're consumed, directly or transitively, by up to seven web apps (`character-viewer-web`, `character-editor`, `stage-viewer-web`, `stage-editor`, `lifebar-viewer-web`, `lifebar-editor`, `mode-quick-versus`) — `mode-quick-versus` alone already depends on all four (roadmap decision `010`). Nothing today documents how a consumer app is supposed to pick which version of each WASM build to use, whether/how breaking changes are signaled across that boundary, or what happens if two consumed libraries' WASM builds expect incompatible versions of a third (e.g. both `stage` and `character-editor` depending on different `sff` releases). This gap was noted during the stages-3D planning pass (decision `014`), which adds yet another cross-repo WASM dependency (`stage` → consumed by `stage-viewer-web`/`stage-editor`) without making the underlying gap worse — it already existed.

This is a real cross-repo coordination question — it would still be true even if every current repo were rewritten from scratch (see this repo's own CLAUDE.md for the "belongs here vs. in a repo's own backlog" test) — so it belongs here, not in any one consumer's backlog.

## Acceptance Criteria
- [ ] A recorded decision (or explicit "not needed yet, here's why") on whether consumer apps pin exact WASM versions, use a semver-range-like convention, or something else
- [ ] A recorded answer for what a consumer app does when it needs two libraries whose own WASM builds were built against incompatible versions of a shared dependency (e.g. `sff`)
- [ ] Existing per-repo `wasm:download`-style scripts (see `character-viewer-web`'s own convention) reviewed against whatever policy is chosen, and updated only if they contradict it

## Notes
Not urgent — no consumer has hit a real incompatibility yet. Scoped now so it's tracked rather than silently deferred; timing of the actual decision is the Product Owner's call.
