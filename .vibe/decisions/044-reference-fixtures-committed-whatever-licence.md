---
date: 2026-11-18
status: accepted
---
# Reference fixtures are committed as downloaded, licence notwithstanding

**Context:** Decision `043` replaced Kung Fu Man with a character of our own, because `kfm`/`kfm_zss` and MUGEN's `common1.cns` are Elecbyte content under non-commercial terms. The Product Owner reviewed that choice.
**Decision:** This supersedes `043` and restores point 3 of `036`, with one change: the files are committed instead of staying local.
- Commit unmodified, as engine test fixtures, each with its source (repo and commit, or install) and its licence notice: Ikemen GO's `data/common1.cns.zss`, MUGEN 1.1's `common1.cns`, and Kung Fu Man (`kfm`, `kfm_zss`) from the Ikemen-GO-Screenpack repo.
- This applies to test fixtures only. Shipping files in the game's `common/` folder is still governed by decision `037`.
**Reason:** Product Owner decision (2026-11-18): "no worry about the licence". The milestone's fidelity measure needs the real reference content in CI.
**Rejected alternatives:**
- *Author our own free character (`043`)*: it is not Ikemen GO's reference content, and it costs a lot to author.
- *Local-only copies*: they never run in CI.
