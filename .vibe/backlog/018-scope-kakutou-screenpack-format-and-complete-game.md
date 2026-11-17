---
status: todo
---
# Scope the complete-game layer: an OpenKakutou screenpack format, options, controls and content discovery

## Description
`mode-quick-versus` plays a match end to end, but it is not yet a complete game: no title screen or main menu, no options screen (difficulty, round time, life, audio volumes, video), controls can't be configured (only `mode-quick-versus` 022 exists, scoped to that mode), and select/setup screens are minimal.

In MUGEN and Ikemen GO this layer is a **screenpack** (`system.def`, `select.def`) plus a global engine configuration file. Product Owner direction (2026-11-17): **do not reproduce that organization.** Specifically rejected:
- **the catch-all `system.def`** — one huge file mixing every screen (title, select, VS, options, victory…) with hundreds of positioning keys;
- **the global engine config** (`mugen.cfg` / Ikemen GO config) holding options and key bindings together;
- **the hand-declared roster** (`select.def` listing every character and stage by hand) — content must be **discovered automatically** from what is installed. Today's web roster is itself a hand-written JSON manifest (`mode-quick-versus/src/roster/manifest.ts`), the same problem.

**The screenpack concept is kept, with an OpenKakutou-specific format** (Product Owner, 2026-11-17): the game's screens are themable through data, so a community can make and share screenpacks — but in our own format, designed to avoid the rejected points above. **MUGEN/Ikemen GO screenpacks are not supported** (no reading, no conversion). The MUGEN 1.0/1.1 + Ikemen GO compatibility MUST still fully applies to **combat content** — characters, stages, lifebars, sounds, sprites, fonts used by that content; it does not extend to screenpacks, `select.def` or engine configuration files. The content folder layout (`chars/`, `stages/`…) was not objected to and can stay familiar to the community.

Questions to settle:
0. **The screenpack format itself**:
   - modular: one file per screen (title/main menu, select, VS, options, controls, pause, results…) plus a small root manifest, instead of one catch-all;
   - layout model: anchors / relative layout that adapts to resolution and aspect ratio, instead of MUGEN's absolute pixel coordinates;
   - file syntax: a standard, schema-validated format (e.g. JSON + JSON Schema, or TOML) so editors and validation come for free, instead of MUGEN's ad-hoc INI dialect;
   - assets: standard formats (PNG/WebP, OGG, TTF/OTF) and/or MUGEN ones (`.sff`, `.snd`, `.fnt`, see `016`) — decide;
   - what a screenpack can and cannot change (visuals, sounds, layout, menu entries?) versus what stays game logic;
   - a default screenpack shipped with the game, built in this format.
   Repo split per the org naming convention: a `screenpack` library (parse/write, no rendering, WASM), `screenpack-viewer-web`, `screenpack-editor`, with `mode-quick-versus` rendering it — or a lighter split if justified.
1. **Content discovery**: native scans the installed content folders; the web build has no directory listing, so its manifest must be generated at build/deploy time from the same folders, never hand-written. Per-content metadata (display name, portrait, order, hidden) comes from the content's own files (e.g. `.def` `[Info]`, portrait sprite), with an optional small per-content override file if needed — never a central list.
2. **Screens**: the list of screens the game has (title/main menu, select, VS, options, controls, pause, results) and the data each exposes to the screenpack.
3. **Options and controls**: split by concern (per-player controls, gameplay options, audio, video) rather than one global file; where they persist on web and native; `mode-quick-versus` 022 re-homed or kept accordingly.
4. **Where the complete game lives**: decision `006` makes each `mode-*` a standalone game and defers a multi-mode shell until a second mode exists. Recommended: grow `mode-quick-versus` itself first, revisit `006` when `mode-tag-battle` is scoped. Decide what is shared (e.g. an options/controls/menu kit in `web-ui-kit`) so a future shell or second mode doesn't rebuild it.
5. **Order relative to the combat-completeness milestone** (`013`).

## Acceptance Criteria
- [ ] Decision recorded in `roadmap/.vibe/decisions` answering questions 1–5, stating explicitly that MUGEN/Ikemen screenpacks, `select.def` and engine config files are out of the compatibility MUST, and why
- [ ] `repos.md` updated if a repo's scope changes; per-repo backlog items added (`mode-quick-versus`, `web-ui-kit`, others as needed)
- [ ] `repos.md` lists the new screenpack repos if created, with repo-creation items
- [ ] Link with font scoping (`016`) settled: whether OpenKakutou screenpacks use `.fnt`, standard fonts, or both
