---
date: 2026-08-09
status: accepted
---
# Support Ikemen GO's 3D model-based stages, split parse (`stage`) / render (`stage-viewer-web`, `stage-editor`) / shared 3D viewport (`web-ui-kit`)

**Context:** Ikemen GO extends the stage `.def` format to let a stage use a 3D model (glTF v2.0, PBR pipeline) instead of — or alongside — 2D sprite-based BG elements. This graduated from nightly-build-only to an official **v1.0 release candidate feature in July 2026** (per the engine's own DeepWiki and GitHub wiki), so it is mainline compatibility now, not a fringe extension. `stage`'s own decision `001` explicitly deferred exactly this question:

> *"If Ikemen GO's nightly Z-axis `topbound`/`botbound` extension ever needs modeling, that is a separate, later decision — not a same-axis twin of Left/Right."*

Verified (not assumed) against the engine's documentation, the relevant `.def` additions are:

| Section | Keys | Role |
|---|---|---|
| `[Model]` | `Environment` (`.hdr` file), `EnvironmentIntensity`, `Offset` (X/Y/Z), `Scale` (X/Y/Z) | 3D model reference + placement, image-based lighting |
| `[Camera]` | `Near`, `Far`, `fov`, `YShift` | 3D projection/frustum, additive to the already-modeled 2D zoom keys |
| `[Scaling]` (new section) | `DepthToScreen`, `topz`/`botz`, `topscale`/`botscale` | Perspective scaling of a player's on-screen size by Z position |
| `[PlayerInfo]` | `topbound`/`botbound`, `Startz` (P1-P8) | Character Z-axis movement bound, per-player Z start position |

Also verified: **3D character models are not officially supported** — only unofficial, experimental community work exists outside the main engine (e.g. GitHub discussion "True 3D Chars"). And armature/skeletal deformation on 3D models is a known current limitation: models with armatures are drawn but do not animate.

Sources: [DeepWiki — 3D Model Support](https://deepwiki.com/ikemen-engine/Ikemen-GO/5.3-3d-model-support), [GitHub Wiki — Stage features](https://github.com/ikemen-engine/Ikemen-GO/wiki/Stage-features), [GitHub Discussion #2225 — True 3D Chars](https://github.com/ikemen-engine/Ikemen-GO/discussions/2225), [GitHub Discussion #1328 — 3D-model Stage Interface](https://github.com/ikemen-engine/Ikemen-GO/discussions/1328).

**Decision:** Commit to supporting Ikemen GO 3D model-based stages now, split the same way decision `012` split `.zss` parsing from execution:

- **`stage`** parses/serializes the new sections as pure data — `[Model]` reference and placement, the `[Camera]` 3D additions, the new `[Scaling]` section, and the Z-axis extension of `StageBoundaries` (`topbound`/`botbound`, per-player `Startz`). No rendering, no model-file reading — same no-rendering-dependency constraint `stage` already holds. Resolves decision `001`'s deferred question: yes, model it, now that it is verified real.
- **`stage-viewer-web`** and **`stage-editor`** do the actual WebGL rendering: loading the referenced glTF model and `.hdr` lighting file directly via existing standard loaders. Unlike `.sff`, glTF is an open, tooled format — no dedicated OpenKakutou parsing repo is needed the way `sff` was extracted (decision `007`).
- **`web-ui-kit`** gains a shared 3D viewport control (orbit/pan/zoom camera), consumed by both `stage-viewer-web` and `stage-editor` from the start — same reasoning that already justified the existing 2D canvas/viewport control (backlog item `004`), not deferred until a second consumer appears the way `sff`'s extraction was (decision `007`'s situation was different: `sff` was pulled out of `character` *after* `stage`/`lifebar` both needed it; here both consumers are already known upfront).
- **`engine`** gets no new backlog item. Its own `005` ("physics and movement", not yet started) is already the sole place `StageBoundaries` will be consumed for movement clamping — a note is added there pointing at this decision, so a future Z bound is picked up naturally when that item is implemented, without speculatively scoping deeper gameplay questions (e.g. whether hit detection should ever consider Z) that this decision does not answer.
- **`character`** is explicitly out of scope — no official Ikemen GO 3D character support exists to target.

The exact 3D rendering library (three.js, raw WebGL, etc.) is left open, to be chosen during implementation — same treatment decision `012` gave the `.zss` Lua interpreter choice. Whether a stage's `[Model]` is a single global section or repeatable like `[BG name]` is also left to be confirmed against real stage files during `stage`'s own implementation (backlog item `008`), not decided here.

**Reason:** Matches this org's stated compatibility target (MUGEN + Ikemen GO, extensions included) and its existing precedent for committing to real, verified format extensions rather than leaving them open (decision `012`). Keeping the split along existing repo boundaries (`stage` = data, `stage-viewer-web`/`stage-editor` = rendering, `web-ui-kit` = shared UI primitive) avoids inventing new repos or blurring `stage`'s no-rendering-dependency constraint.

**Rejected alternatives:**
- *Also scope 3D character model support* — rejected: not an official Ikemen GO engine feature, no compatibility target to build against; a claim to the contrary in an earlier draft of this decision was corrected after verification.
- *Extract a dedicated 3D-model-parsing repo, mirroring `sff`* — rejected: glTF is an open, standard, already-tooled format (unlike MUGEN's proprietary `.sff`), so there is no bespoke parsing work to centralize; `stage-viewer-web`/`stage-editor` can each load it directly via standard loaders.
- *Defer the shared 3D viewport control until a second consumer appears, mirroring `sff`'s extraction timing* — rejected: `stage-viewer-web` and `stage-editor` both need it from day one, the same situation that already justified `web-ui-kit`'s existing 2D viewport control being built as shared infrastructure rather than duplicated.
- *Add a new `engine` backlog item for Z-axis movement now* — rejected: `engine` hasn't even started consuming `stage`'s existing (X-axis) boundary data yet (item `005` is still `todo`); adding a separate Z-specific item ahead of that would speculate about gameplay mechanics (does Z affect hit detection? movement input?) this decision has no verified answer for. A pointer note is enough for now.
