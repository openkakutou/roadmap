---
date: 2026-11-18
status: accepted
---
# Acceptance character: our own free character, not Kung Fu Man

**Context:** Decision `036` (point 3) picked Kung Fu Man (`kfm`, `kfm_zss`) as the milestone's acceptance characters. The Ikemen-GO-Screenpack README classes `chars/kfm*` as Elecbyte content under non-commercial terms. Ikemen GO itself ships only `data/common1.cns.zss` (MIT), and no `common1.cns`.
**Decision:** This replaces point 3 of `036`.
- The acceptance character is a test character that OpenKakutou authors under a free licence, in `.cns` and `.zss` versions, and that runs in Ikemen GO (engine#053).
- Ikemen GO's `common1.cns.zss` is committed with its MIT notice (engine#047).
- MUGEN 1.1's `common1.cns` (Elecbyte) is exercised only from a local copy and never committed (decision `037`).
**Reason:** Product Owner decision. Committing Kung Fu Man would redistribute content that its licence does not let us redistribute.
**Rejected alternatives:**
- *Download Kung Fu Man at test time from Ikemen GO's repo*: nothing is redistributed, but tests then depend on a third party's non-free content.
- *Local-only Kung Fu Man*: never runs in CI.
