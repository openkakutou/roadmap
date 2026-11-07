---
status: todo
---
# Scope Bitmap Font Support

## Description
Real lifebars and screenpacks render names, timers and combo counters with MUGEN/Ikemen `.fnt` bitmap fonts, and mode-quick-versus needs them for its HUD, yet no repo parses them. Decide where this lives (new shared `fnt` library like `sff`/`snd`, or inside an existing repo), who consumes it, and the timeline.

## Acceptance Criteria
- [ ] Decision recorded in roadmap/.vibe/decisions with the chosen home and consumers (lifebar-viewer-web, lifebar-editor, mode-quick-versus)
- [ ] repos.md updated, and a repo-creation backlog item added if a new repo is chosen
- [ ] MUGEN 1.0/1.1 and Ikemen GO font formats named as targets, with real fonts as fixtures

## Notes
Lifebar viewer/editor currently have no font handling (no .fnt code in src/). Follows the extraction logic of decision 007 (sff) and 026 (snd). Compat is a MUST: MUGEN 1.0/1.1 and Ikemen GO, validated against real community files.
