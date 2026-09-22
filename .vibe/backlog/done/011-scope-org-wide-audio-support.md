---
status: done
---
# Scope org-wide audio (`.snd`) support

## Description
No repo in the org reads, decodes, or plays a MUGEN/Ikemen GO `.snd` sound file today. `character`'s `Character`/`CharacterInfo` only carries `SoundFile` as a referenced path string (metadata copied from the `.def`'s `[Files]` section) — the file itself is never opened or parsed anywhere in `character`, `sff`, `engine`, `character-editor`, `character-viewer-web`, or `mode-quick-versus`. No repo's `.vibe/decisions/` has ever addressed audio scope either way — this isn't a deliberate deferral, it's an untouched gap.

This blocks two things a "complete" org would have:
- **`mode-quick-versus`** (a complete playable game) has no hit/voice/announcer sound during a match — `engine`'s state machine already parses `PlaySnd`-style controllers' parameters generically (via `character/cns`) but has nothing to execute them against, since there's no decoded sound data to play.
- **`character-editor`** (a complete character editor) has no way to browse, preview, or assign a character's sound effects — the sprite/palette/animation/state/command editors all exist, but sound is entirely unaddressed.

What needs a Product Owner + technical decision, mirroring how `sff` was scoped out of `character` (`.vibe/decisions/007`):
- Where `.snd` parsing lives: a new shared repo (parallel to `sff`, if `lifebar-editor` or others turn out to need it too), or inside `character` directly (if it stays character-only, like `stage`'s own format needs no shared extraction).
- Decode scope: MUGEN's classic `.snd` (v1/v2, ADPCM/PCM per-sample groups) and whatever Ikemen GO extends it with, same "MUGEN 1.0/1.1 and Ikemen GO, validated against real files" compatibility bar every other parser in this org already commits to.
- Playback: which repo actually plays decoded audio — `engine`'s WASM boundary would need to expose "sound X should play now" events (mirroring how it currently exposes animation/health/round state), leaving the actual `AudioContext`/playback to `mode-quick-versus`, consistent with `engine` owning simulation and not rendering (`.vibe/decisions/004`, `008` in `engine`... — actually see roadmap `.vibe/decisions/008`).

## Acceptance Criteria
- [x] Where `.snd` parsing lives (new shared repo vs. inside `character`) is decided and recorded as a decision
- [x] Compatibility bar for the decode (MUGEN version(s) + Ikemen GO extensions) is decided and recorded
- [x] How a decoded sound reaches actual playback — which repo/layer triggers it, which plays it — is decided and recorded
- [x] Concrete backlog items exist in each repo whose work this decision unblocks (at minimum: the sound-parsing repo, `engine`'s controller execution, `mode-quick-versus`'s playback, `character-editor`'s sound browser)

## Notes
Raised while auditing the org for gaps standing between the current state and "a complete game and complete editors" (2026-09-22). Cross-repo signal already in place: `character/cns` already parses `PowerAdd`/other state controllers generically without interpreting them — the same pattern likely applies to `PlaySnd`, so `engine` should be able to recognize the controller type once it has real sound data to hand it.

**Resolved 2026-09-22** by `.vibe/decisions/026`: new shared `snd` repo (parallel to `sff`) for `.snd` v1/v2 decode, needed independently by `character` and `mode-quick-versus`; `stage` separately gains a `Music` field (plain file path, no decoder needed — a smaller gap found while resolving this one, `stage/parser.go:43`); `engine` triggers `PlaySnd` as an event, never decodes/plays; playback (Web Audio / SDL2_mixer) is each consuming app's own job. `repos.md` updated with `snd` as `active`. Concrete follow-up items created: `stage#013`, `engine#020`, `character#057` (blocked on `snd` existing), `character-editor#017` (blocked on `character#057`), `mode-quick-versus#013` (blocked on all three). The `snd` GitHub repo was created 2026-09-22 (on explicit go-ahead) and scaffolded via `/vibe:init`, mirroring `sff`'s skeleton — no `.snd` parsing code yet, so `character#057`/`mode-quick-versus#013` are unblockable but not yet unblocked in practice.
