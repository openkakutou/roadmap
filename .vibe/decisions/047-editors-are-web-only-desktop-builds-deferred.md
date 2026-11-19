---
date: 2026-11-19
status: accepted
---
# Editors ship on the web only; native desktop builds are deferred; amends decisions `019` and `022`

**Context:** Decision `022` dropped the webview because of real-time rendering overhead in the game, and gave the editors a separate native Fyne UI. The editors have no real-time constraint (`022` says so itself). Today `character-editor`, `stage-editor` and `lifebar-editor` each have a Fyne skeleton under `desktop/`, while the web editors themselves still need a usability pass (`web-ui-kit` 012, editors' `*-web-ui-kit-adoption-and-ux-pass` items). Each editor feature would be written twice, in TypeScript and in Fyne.

**Decision:**
- The editors are **web only** for now. No new feature goes into `desktop/`; the existing skeletons stay as they are, with their CI, and are not removed.
- Reopen when the web editors are usable (their UX-pass items done) **and** a concrete need for a desktop editor appears (e.g. working on a large local content folder the browser cannot handle). At that point, compare a webview shell again with Fyne: the performance argument of `022` does not apply to editors.
- The game is unaffected: `game` native stays go-gl + SDL2.

**Reason:** Halves the editors' cost while their single UI is not good yet; the reason for native UI (real-time rendering) only holds for the game.

**Rejected alternatives:** *Keep both UIs* — doubles every editor feature with no benefit. *Delete the `desktop/` skeletons now* — loses work cheaply kept until the reopen point.
