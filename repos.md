# Repos

Status of every repo in the OpenKakutou organization (github.com/openkakutou). Kept up to date by hand as repos are created or their role changes.

## Naming convention <!-- keep -->

Each domain (`character`, `stage`, `lifebar`, …) follows the same split, mirrored in the repo name:
- `<domain>` — read/write parsing library for that domain's MUGEN/Ikemen file format(s), no rendering dependency, compiles to WASM. Only exists where the format needs its own parser (e.g. `character`).
- `<domain>-viewer-web` — static web app to **visualize** (and, where applicable, control) content of that domain. Read-only.
- `<domain>-editor` — app to **modify and/or create** content of that domain. Read+write.

Separately, `mode-<name>` is a **game mode**: the unit that actually consumes `engine` for one specific way of playing (its own character-selection flow, match flow, result flow) — e.g. `mode-quick-versus`, `mode-tag-battle`. See `.vibe/decisions/005`.

## Repos

| Domain | Repo | Status | Role |
|---|---|---|---|
| character | [`character`](https://github.com/openkakutou/character) | active | Read/write Go library for MUGEN/Ikemen GO character files (`.def`/`.sff`/`.air`/`.cns`). Foundation everything else in this domain depends on; compiles to WASM, no rendering dependency. |
| character | [`character-viewer-web`](https://github.com/openkakutou/character-viewer-web) | active | Visualize and control a character: browse sprites, palettes, characteristics and animations, and trigger animations/moves live, via the `character` WASM build. Read-only. |
| character | `character-editor` | planned | Modify and/or create a character: read+write UI on top of `character`. Separate app from `character-viewer-web`, not a successor to it — see `.vibe/decisions/002`. Named `character-editor`, not just `editor` — see `.vibe/decisions/003`. |
| stage | `stage-viewer-web` | idea | Visualize a stage (background). Not yet scoped — see `.vibe/backlog/002`. |
| stage | `stage-editor` | idea | Modify and/or create a stage. Not yet scoped — see `.vibe/backlog/002`. |
| lifebar | `lifebar-viewer-web` | idea | Visualize/preview a lifebar (health/power bar UI). Not yet scoped — see `.vibe/backlog/002`. |
| lifebar | `lifebar-editor` | idea | Modify and/or create a lifebar. Not yet scoped — see `.vibe/backlog/002`. |
| (org-wide) | `engine` | planned (future) | Combat simulation that runs while two characters fight, built on the same extracted libraries as `character`. Not game modes, not menus/game flow — see `.vibe/decisions/004`. Detailed scope/timeline not yet defined — see `.vibe/backlog/001`. |
| mode | `mode-quick-versus` | idea | First game mode: standard two-player, one-character-each versus match. Consumes `engine`, owns its own character-selection/match/result flow. Formerly named `character-selector` — see `.vibe/decisions/005`. Not yet scoped — see `.vibe/backlog/003`. |
| mode | `mode-tag-battle` | idea | Tag battle mode (multiple characters per side). Mentioned as an example of another mode; not yet committed to or scoped. |

## Status legend

- **active** — repo exists, under development
- **planned** — named and scoped in the roadmap, repo not created yet
- **idea** — mentioned as a possibility, not committed to
