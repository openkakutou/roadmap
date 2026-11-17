---
date: 2026-11-18
status: accepted
---
# The goal measure: run both engines with the same controlled inputs and get the same result

**Context:** Decisions `036`, `039` and `041` set Ikemen GO parity as the target. The Product Owner states the goal plainly: run both engines, control the characters with the same inputs, and obtain the same result.
**Decision:**
- **The measure of the combat milestone is the differential test** (engine 036, game 051, protocol of decision `039`): for each scripted match on real content, the number of frames identical to Ikemen GO before the first divergence, then a match identical end to end. The conformance harness (engine 030) stays a guide to what to build next, not the goal.
- **Engine 036 starts now**, in parallel with engine 037: it no longer waits for 037. Building the Ikemen GO side (driving it with recorded inputs, fixed seed, dumping per-frame state) does not need any engine progress, and once it exists every later step is judged by how far the identical prefix grows.
- Amends `041`'s order on this one point; everything else in `041` stands.
**Reason:** Product Owner direction: "same result when controlling the characters" is the definition of done; measuring it from the start keeps every step honest.
**Rejected alternatives:** *Build the differential test after the engine catches up* — progress would be judged by proxy counts until then.
