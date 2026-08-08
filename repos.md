# Repos

Status of every repo in the OpenKakutou organization (github.com/openkakutou). Kept up to date by hand as repos are created or their role changes.

## Naming convention <!-- keep -->

Each domain (`character`, `stage`, `lifebar`, …) follows the same split, mirrored in the repo name:
- `<domain>` — read/write parsing library for that domain's MUGEN/Ikemen file format(s), no rendering dependency, compiles to WASM. Only exists where the format needs its own parser (e.g. `character`, `stage`). Not every domain gets one — `lifebar` doesn't, see `.vibe/decisions/009`.
- `<domain>-viewer-web` — static web app to **visualize** (and, where applicable, control) content of that domain. Read-only.
- `<domain>-editor` — app to **modify and/or create** content of that domain. Read+write.

Two repos sit outside any single domain, shared by several of the above:
- [`sff`](https://github.com/openkakutou/sff) — sprite (`.sff` v1/v2 + palettes) parsing, extracted out of `character` because `stage` and `lifebar` need it too. See `.vibe/decisions/007`.
- [`web-ui-kit`](https://github.com/openkakutou/web-ui-kit) — shared design system (Web Components + tokens) for every viewer/editor/mode web app. See `.vibe/decisions/011`.

Separately, `mode-<name>` is a **game mode**: a standalone, autonomous game consuming `engine` for one specific way of playing (its own character-selection flow, match flow, result flow) — e.g. `mode-quick-versus`, `mode-tag-battle`. Each ships as a complete playable game on its own; combining several modes into one game is a deferred future possibility, not currently scoped. See `.vibe/decisions/005` and `.vibe/decisions/006`.

Compatibility target for every parser in this org (`character`, `sff`, `stage`, and lifebar's in-app parsing): MUGEN 1.0/1.1 **and** Ikemen GO, validated against real community files — not just the spec. Includes Ikemen GO's `.cmd`/`.zss` extensions where applicable (see `.vibe/decisions/012` for `.zss`).

## Repos

| Domain | Repo | Status | Role |
|---|---|---|---|
| shared | [`sff`](https://github.com/openkakutou/sff) | active | Read/write Go library for MUGEN/Ikemen `.sff` v1/v2 sprite files and palette resolution. Extracted out of `character`; depended on by `character`, `stage`, `lifebar-viewer-web`, `lifebar-editor`. Compiles to WASM, no rendering dependency. See `.vibe/decisions/007`. |
| shared | [`web-ui-kit`](https://github.com/openkakutou/web-ui-kit) | active | Shared design system (Web Components + CSS tokens, framework-agnostic) for every viewer/editor/mode web app: layout shell, form/input components, canvas/viewport controls, accessibility baseline. See `.vibe/decisions/011`. |
| character | [`character`](https://github.com/openkakutou/character) | active | Read/write Go library for MUGEN/Ikemen GO character files (`.def`/`.air`/`.cns`/`.cmd`/`.zss`, sprites via `sff`). Foundation everything else in this domain depends on; compiles to WASM, no rendering dependency. |
| character | [`character-viewer-web`](https://github.com/openkakutou/character-viewer-web) | active | Visualize and control a character: browse sprites, palettes, characteristics and animations, and trigger animations/moves live, via the `character` WASM build. Read-only. |
| character | [`character-editor`](https://github.com/openkakutou/character-editor) | active | Modify and/or create a character: read+write UI on top of `character` and `sff`. Separate app from `character-viewer-web`, not a successor to it — see `.vibe/decisions/002`. Named `character-editor`, not just `editor` — see `.vibe/decisions/003`. |
| stage | [`stage`](https://github.com/openkakutou/stage) | active | Read/write Go library for MUGEN/Ikemen stage (background) `.def` files: BGdef, BG elements/layers, camera bounds. Depends on `sff` for stage sprite sheets. Compiles to WASM. See `.vibe/decisions/009`. |
| stage | [`stage-viewer-web`](https://github.com/openkakutou/stage-viewer-web) | active | Visualize a stage: layers, parallax, animated backgrounds, via the `stage` WASM build. Read-only. |
| stage | [`stage-editor`](https://github.com/openkakutou/stage-editor) | active | Modify and/or create a stage: read+write UI on top of `stage`. |
| lifebar | [`lifebar-viewer-web`](https://github.com/openkakutou/lifebar-viewer-web) | active | Visualize/preview a lifebar (health/power bar UI, combo counter, round display), with live value simulation. Parses the lifebar `.def`-style format directly (no separate `lifebar` library, see `.vibe/decisions/009`); uses `sff` for referenced sprites. Read-only. |
| lifebar | [`lifebar-editor`](https://github.com/openkakutou/lifebar-editor) | active | Modify and/or create a lifebar: read+write UI, own lifebar parsing (see `.vibe/decisions/009`) plus `sff` for sprite assignment. |
| (org-wide) | [`engine`](https://github.com/openkakutou/engine) | active | Combat simulation that runs while two characters fight: CNS trigger evaluation, state-machine execution, `.zss` execution, physics, hit detection, damage/combo, round flow. Not game modes, not menus/game flow — see `.vibe/decisions/004`, `.vibe/decisions/008`. Depends on `character` and `stage`. |
| mode | [`mode-quick-versus`](https://github.com/openkakutou/mode-quick-versus) | active | First game mode: a standalone, playable game — standard two-player, one-character-each versus match. Consumes `character`, `stage`, `sff`, `engine`; owns its own character-selection/match/result flow. Formerly named `character-selector` — see `.vibe/decisions/005`, `.vibe/decisions/006`, `.vibe/decisions/010`. |
| mode | `mode-tag-battle` | idea | Tag battle mode (multiple characters per side), a standalone game like `mode-quick-versus`. Mentioned as an example of another mode; not yet committed to or scoped. |

## Status legend

- **active** — repo exists, under development
- **planned** — named and scoped in the roadmap, repo not created yet
- **idea** — mentioned as a possibility, not committed to
