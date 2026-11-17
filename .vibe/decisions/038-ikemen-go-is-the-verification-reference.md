---
date: 2026-11-17
status: accepted
---
# Ikemen GO is the verification reference: compare with it end to end, no separate MUGEN check

**Context:** The org-wide MUST requires MUGEN 1.0/1.1 and Ikemen GO compatibility. Decision `036` (engine 036) and the 3D character spec (`character` item 069, then item 072) planned hand checks in MUGEN, whose source is closed. The Product Owner settles how compatibility is verified.
**Decision:**
- **Ikemen GO is the reference.** It already aims at MUGEN compatibility, so matching Ikemen GO is how MUGEN compatibility is verified: no separate visual or manual MUGEN confirmation. The MUST itself (both engines' content keeps working) is unchanged.
- **End-to-end differential tests against Ikemen GO are approved**: run the same content and inputs in Ikemen GO and in OpenKakutou, compare the resulting state, and report the first divergence; claims are otherwise grounded in Ikemen GO's source.
- **Scope**: content that works in Ikemen GO — characters (engine 036), stages and lifebars (game 051). Content Ikemen GO cannot run is out of scope.
- **OpenKakutou-only extensions** (3D characters, decision `028`; the screenpack and mode formats, decisions `029`, `030`) have no reference: no differential test, no MUGEN check. Their only compatibility requirement is being strictly additive, proven by the existing content still passing its own tests.
**Effects:** decision `036`'s note that MUGEN-specific divergences are checked by hand is dropped; `character` item 072 (check the 3D extension in MUGEN 1.1) is withdrawn; every repo's `CLAUDE.md` compatibility section gains a "Reference for verification" paragraph.
**Reason:** Product Owner direction. One automatable reference beats an unautomatable closed-source one, and Ikemen GO's own goal already covers MUGEN.
**Rejected alternatives:** *Manual MUGEN checks* — not automatable, closed source, redundant with Ikemen GO's own goal. *Differential tests for OpenKakutou-only features* — nothing to compare with.
