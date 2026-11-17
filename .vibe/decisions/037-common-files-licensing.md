---
date: 2026-11-17
status: accepted
---
# Common combat files in `common/`: ship third-party files only with a verified license, kept beside them

**Context:** Decision `031` puts `common1`, `fightfx` and `common.snd` in `common/`; game#038 ships them. The Product Owner asks whether existing files can be shipped with their license stated.
**Decision:**
- **Ikemen GO's `data/common1.cns.zss`: shipped.** Ikemen GO's `LICENCE.txt` (commit `54d4148a728153c2097a0fb899a06812b2d3e193`) states that the MIT License "applies to the Ikemen GO engine and the scripts in this repo"; MIT allows redistribution with the copyright and permission notice, so `common/` carries the file with that notice beside it (`common/LICENSE-ikemen-go.txt`).
- **`fightfx.sff`/`.air` and `common.snd`: not shipped until their license is verified.** They come from the Ikemen-GO-Screenpack repo, whose `LICENCE.txt` lists Elecbyte's fonts (CC BY-NC 3.0) and named artist assets (CC BY 3.0) but does not name these files; their origin is presumably Elecbyte's MUGEN data, unverified.
- **MUGEN 1.1's own `common1.cns` (Elecbyte): not shipped** unless Elecbyte's license is verified to allow it.
- Every file in `common/` has its license and source recorded in `common/LICENSES.md`; a file with no verified license never ships.
**Reason:** Shipping is redistribution; a stated license only helps when the license actually grants it.
**Rejected alternatives:** *Ship everything with a "belongs to its authors" notice* — not a license. *Author every common file ourselves* — unnecessary for `common1`, whose MIT license already allows it; kept as the fallback for the effects and sounds.
