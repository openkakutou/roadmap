---
status: todo
---
# Rename `mode-quick-versus` to `game`

## Description
Decision `030` turns `mode-quick-versus` into the game runtime, `game`. Rename the GitHub repo and follow every reference. GitHub redirects the repo URL but not GitHub Pages: `https://openkakutou.github.io/mode-quick-versus/` becomes `https://openkakutou.github.io/game/`.

Known references (2026-11-17 scan, excluding history: decisions, done items, changelogs):
- the repo itself: `package.json`, `native/go.mod` module path and its imports, `native/cmd/quickversus` binary name, `src/i18n/i18n.ts`, `native/internal/gfx/screens.go`, `native/internal/audio/audio.go`, `README.md`, `CLAUDE.md`, `docs/architecture.md`, `.vibe/index.md`, Pages base path and native artifact names in workflows;
- other repos' docs/code: `engine` (`README.md`, `CLAUDE.md`, backlog 012/024/029, `testdata/fighter.cns` comment), `snd` (`CLAUDE.md`, `README.md`, `cmd/wasm/main.go`, `.vibe/modules/wasm.md`), `character` (`CLAUDE.md`, `docs/architecture.md`, `.vibe/index.md`, backlog 069/071), `web-ui-kit/CLAUDE.md`, `stage-viewer-web/src/viewer/background-composition.ts`, `character-viewer-web/src/i18n/i18n.ts`, the open "refresh stale planned docs" items of the viewer/editor repos;
- `openkakutou.github.io` (`index.html` link, `README.md`, `CLAUDE.md`);
- `roadmap`: `repos.md` (row + retire the `mode-*` naming convention paragraph), `dashboard/build_data.py` (`REPO_ORDER`, `DOMAIN`), regenerated dashboard;
- the local workspace folder and the workspace `CLAUDE.md`.

## Acceptance Criteria
- [ ] Repo renamed on GitHub; local checkout moved to `game/`, remote URL updated
- [ ] Go module path updated, native build and tests green
- [ ] Web build deployed at `openkakutou.github.io/game/`; showcase site link updated
- [ ] No remaining reference to `mode-quick-versus` outside history (decisions, done items, changelogs)
- [ ] Release/pin propagation docs of producer repos (`character`, `engine`, `snd`, `sff`, `stage`) name `game` as the consumer
