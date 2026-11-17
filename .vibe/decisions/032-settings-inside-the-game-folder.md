---
date: 2026-11-17
status: accepted
---
# Settings live inside the game folder, not in the user config directory

**Context:** Decision `029` §4 put the native settings files in `os.UserConfigDir()/openkakutou/`, and decision `031` kept that. The Product Owner rejects any preference file outside the game folder. The selected screenpack and lifebar (`029` §4, `031` §2) also had no file.

**Decision:** Amends `029` §4 and `031` §4 on location only; the split by concern stands.

```
OpenKakutou/
├── openkakutou(.exe)
├── config/
│   ├── controls.json     per-player keyboard/gamepad bindings
│   ├── gameplay.json     difficulty, round time, life, rounds…
│   ├── audio.json        volumes
│   ├── video.json        resolution, fullscreen, vsync
│   └── appearance.json   selected screenpack and lifebar
├── chars/  stages/  lifebars/  screenpacks/  modes/  common/   (031)
```

- Native: `config/` in the content root, next to the executable (on macOS next to the bundle, as in `031`). Created on first launch when missing; a missing or corrupt file falls back to defaults for that concern only.
- Web: unchanged, browser storage, one key per concern (now including `appearance`).
- The game folder is self-contained: copying it copies the game, its content and its settings.

**Reason:** Product Owner direction; it also matches the portable, unzip-and-play install `031` chose and the MUGEN/Ikemen GO habit (their config sits in the game folder).

**Rejected alternatives:**
- *`os.UserConfigDir()`* (`029` §4) — rejected by the Product Owner.
- *Selections inside `video.json`* — mixes display hardware settings with appearance choices, against `029`'s one-file-per-concern rule.
- *Settings files at the root of the game folder* — clutters the root next to the content folders; one `config/` folder keeps them together.
