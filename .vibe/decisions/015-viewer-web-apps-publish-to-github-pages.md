---
date: 2026-08-09
status: accepted
---
# The `*-viewer-web` apps each publish to GitHub Pages, one deployment per repo

**Context:** `character-viewer-web`, `stage-viewer-web`, and `lifebar-viewer-web` are static sites (no backend, per each repo's own `CLAUDE.md`) that currently have no packaging or hosting story at all — no repo has a `.github/workflows/` deploy pipeline, and none is reachable at a URL today. `mode-quick-versus`'s own backlog item `008` ("Release Packaging") only produces a `dist/` bundle "deployable to any static host"; it doesn't publish it anywhere either, and is out of scope for this decision (not a `*-viewer-web` app). `character-editor`/`stage-editor`/`lifebar-editor` are also out of scope here — this decision covers only the three read-only viewers, per Product Owner scoping.

**Decision:** Each of the three `*-viewer-web` repos gets its own GitHub Pages deployment, independent of the others — no shared portal or unified entry point. A standard GitHub Actions workflow, triggered on push to `main`, runs the repo's own tests/lint gate, then `npm run build` (and `npm run wasm:download` first, where that script exists, to pull the pinned WASM release the app needs), then publishes the `dist/` output to that repo's own `gh-pages` branch / GitHub Pages environment — each ends up reachable at its own `https://openkakutou.github.io/<repo-name>/`. Each repo's existing `vite.config.ts` already sets `base: "./"` (relative asset paths), which already works unmodified for a GitHub Pages project site — no path-prefix reconfiguration needed.

**Reason:** Matches the org's existing "each repo is autonomous, independently shippable" principle (already applied to `mode-*` repos, decision `006`) rather than introducing a new coordination point (a shared portal repo/build) this early, with only three consumers and no stated need yet for a unified landing page. A per-repo GitHub Actions workflow triggered on push is the standard, lowest-friction GitHub Pages setup — no new infrastructure choice needed beyond what `character`/`sff`/`web-ui-kit`'s existing tag-triggered release workflows already establish as this org's CI convention (pinned Action versions, tests gate before publish).

**Rejected alternatives:**
- *A single unified portal (new repo or org-level GitHub Pages) linking to each app* — rejected for now: real coordination overhead (a new repo to maintain, cross-repo links to keep in sync) for a benefit — discoverability across three apps — that doesn't yet justify it. Revisable once more viewer/editor/mode apps exist and navigating between them becomes a real friction point.
- *Include `character-editor`/`stage-editor`/`lifebar-editor` in this same decision* — deferred, not rejected: the editors are earlier-stage (less backlog progress) and weren't part of the Product Owner's stated scope for this pass; the same per-repo GitHub Pages pattern applies to them whenever that's taken up, no new decision needed to extend it.
