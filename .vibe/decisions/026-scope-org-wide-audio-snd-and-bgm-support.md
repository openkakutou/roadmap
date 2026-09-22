---
date: 2026-09-22
status: accepted
---
# Scope org-wide audio: a new shared `snd` repo for character/system sound effects, `stage` gains BGM path exposure

**Context:** Backlog item `011` flagged that no repo in the org reads, decodes, or plays a MUGEN/Ikemen GO `.snd` sound file — `character.SoundFile` is a metadata path only, never opened. Auditing further while resolving it turned up a second, smaller instance of the same absence: `stage`'s own parser explicitly skips `[Music]` (`stage/parser.go:43`, `"carries nothing this model"`) — a stage's background-music path is recognized as a known section but never exposed. Both are "no audio at all" gaps standing between the current state and a complete `mode-quick-versus` and a complete `character-editor`.

**Decision:**

1. **New shared repo, `snd`** — read/write Go library for MUGEN `.snd` v1/v2 sound files, decoding to raw PCM. Extracted as its own repo from the start (not grown inside `character` first, unlike `sff`'s history) because two independent consumers need it on day one: `character` (a character's own hit/voice/taunt sounds) and `mode-quick-versus` directly (system/common sound sets aren't tied to any one character). Mirrors `sff`'s existing shape exactly: no rendering/playback dependency, compiles to WASM, depended on by whichever app needs decoded samples. Compatibility bar matches every other parser in this org: MUGEN 1.0/1.1 `.snd` v1 (uncompressed PCM groups) and v2 (with Ikemen GO's own v2 extension letting a sound entry point at an external audio file instead of embedding samples — the org's stated "MUGEN 1.0/1.1 and Ikemen GO, validated against real files" bar applies here too, not just to `.cmd`/`.zss`).

2. **`engine` triggers sound, never decodes or plays it** — consistent with `engine` already being scoped to simulation, not rendering (roadmap `.vibe/decisions/004`, `008`): `statemachine.ApplyController` gains a `PlaySnd` case (parsed generically today, executed nowhere) that records a triggered `(group, sample)` pair per tick, exposed through the WASM `tick` JSON contract as a events list — the same shape as an app already reads `Animations`/health from. `engine` never touches `snd`'s decoded audio itself.

3. **`stage` gains a `Music` field** — small, self-contained, no dependency on the `snd` repo (background music is a plain audio file path, not a custom binary format): the currently-skipped `[Music]` section's path is added to `stage`'s data model and exposed through the WASM `load` contract, matching how every other stage field already works.

4. **Playback is each consuming app's own responsibility**, per platform, matching the existing "two independent UI implementations" shape (`.vibe/decisions/022`): `mode-quick-versus` decodes triggered `PlaySnd` events + the character's `snd`-decoded samples through the Web Audio API on its web build, and SDL2_mixer (already part of the `go-gl`+SDL2 stack `.vibe/decisions/022` committed to, no new library needed) on its native build; plays a stage's `Music` file the same way. `character-editor` uses the `snd` WASM build directly (no `engine` involved) to decode and preview a character's own sound file in a new sound browser panel, the same pattern its sprite/palette panels already use for `sff`.

**Reason:** Splitting sound effects (`snd`, needs a real binary decoder, two independent consumers) from background music (`stage.Music`, a plain file path, one consumer, no decoder needed) avoids either overscoping a new repo with something that doesn't need it, or blocking the simpler win on the harder one. Extracting `snd` immediately rather than growing it inside `character` first matches this org's own stated principle (`repos.md`'s naming-convention section) of extracting once a second domain needs the same parsing — here, the second consumer is known from the start, not discovered later like `sff` was.

**Rejected alternatives:**
- *Put `.snd` decoding inside `character`* — rejected: `mode-quick-versus` needs to decode system/common sound sets that aren't part of any character's own files, so a `character`-only dependency wouldn't serve it; would need extracting later anyway, with the same churn `sff`'s own extraction (`.vibe/decisions/007`) already demonstrated once.
- *Have `engine` decode and expose raw PCM itself* — rejected: repeats the exact mistake decision `004`/`008` already ruled out for rendering (engine owns simulation, not asset decode/playback); would also force every future consumer of `engine`'s WASM contract to receive audio payloads whether or not it plays them.
- *Fold `stage`'s BGM path into the same `snd` repo's scope* — rejected: a stage's music file is a plain `.mp3`/`.ogg` reference, not the `.snd` binary format; there's nothing to decode, so routing it through a dedicated parser library would be a pure detour.

## Follow-ups
Concrete backlog items created in each affected repo now that this is scoped:
- `stage#013` — expose the `Music` path (unblocked, no dependency)
- `engine#020` — execute `PlaySnd` and expose triggered sound events via the WASM tick contract (unblocked, no dependency)
- `character#057` — decode and expose a character's own sound effects (blocked: needs the `snd` repo to exist first)
- `character-editor#017` — sound browser/preview panel (blocked: depends on `character#057`)
- `mode-quick-versus#013` — match audio playback, both sound effects and stage BGM (blocked: depends on `stage#013`, `engine#020`, `character#057`)

**Repo created 2026-09-22**, on explicit go-ahead: `gh repo create openkakutou/snd`, scaffolded via `/vibe:init` mirroring `sff`'s own skeleton (`go.mod`, `version.go`, `CLAUDE.md`, `.vibe/`, README with managed sections), pushed to `main`. No `.snd` parsing code yet — `character#057` and `mode-quick-versus#013` are unblockable now, but still need this repo's own read/decode implementation first.
