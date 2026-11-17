---
date: 2026-11-17
status: accepted
---
# OpenKakutou authors its own common effects and sounds

**Context:** Decision `037` withheld `fightfx.sff`/`.air` and `common.snd` until their license is verified (the Ikemen-GO-Screenpack licence does not name them) and listed authoring our own as the fallback.
**Decision:** The Product Owner chose to author them: OpenKakutou produces its own hit sparks, guard sparks, super effects and common sounds under a free license (CC0 or CC BY), at the numbers real MUGEN/Ikemen GO characters reference (sourced, not from memory), recorded in `common/LICENSES.md`. `common/` therefore ships Ikemen GO's `common1.cns.zss` (MIT, decision `037`) plus these original files. Tracked as game#050, which game#038 depends on.
**Reason:** Legally safe and makes the game complete on unzip, with no third-party asset of unknown license.
**Rejected alternatives:** *Ask Ikemen GO's maintainers* — uncertain answer and delay, nothing ships meanwhile. *Player brings their own files* — the game is not complete on unzip.
