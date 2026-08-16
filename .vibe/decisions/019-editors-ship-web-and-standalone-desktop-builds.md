---
date: 2026-08-16
status: accepted
---
# Every `*-editor` repo ships both a web build and standalone desktop builds (Windows, Mac, Linux)

**Context:** Decision `015` gave each `*-viewer-web` app its own GitHub Pages deployment and explicitly scoped `character-editor`/`stage-editor`/`lifebar-editor` out, deferring them ("the same per-repo GitHub Pages pattern applies to them whenever that's taken up, no new decision needed to extend it") on the assumption they'd stay web-only like the viewers. The Product Owner has now clarified that's not the target: every editor is also meant to ship as a standalone desktop app on Windows, Mac, and Linux, alongside its web build — not web-only. This mirrors `mode-quick-versus`'s own multi-platform correction (decision `010`'s 2026-08-10 amendment), and is consistent with the org's naming convention already omitting a `-web` suffix from `<domain>-editor` (unlike `<domain>-viewer-web`, which is web-only by name).

**Decision:** `character-editor`, `stage-editor`, and `lifebar-editor` each target four distribution channels: a web build (GitHub Pages, per decision `015`'s pattern, now extended to these three repos) plus standalone desktop builds for Windows, Mac, and Linux. `openkakutou.github.io` links out to all four per editor once each exists; today only the web build exists for any of them, so the other three show as pending on the showcase page. The actual packaging/stack strategy to produce the desktop builds (e.g. a native shell wrapping the same web UI such as Tauri, a different toolchain, one shared approach across all three editors vs. picked per-repo) is not yet decided — tracked as roadmap backlog `007`, deliberately mirroring how `mode-quick-versus`'s own native-platform packaging strategy is still open per backlog `006`. Whether both should end up using the same stack is an open question for whichever gets decided first.

**Reason:** Matches direct Product Owner direction. Recording it now (rather than leaving it implicit) prevents the editors' web deployment — done in this same pass — from being mistaken for the finished distribution story, and gives `openkakutou.github.io` a stable card shape (a platform-links row per app) to grow into as desktop builds land, instead of restructuring the page again later.

**Rejected alternatives:**
- *Leave editors web-only, matching the viewers* — rejected: superseded by explicit Product Owner direction; the naming convention already left room for this (no `-web` suffix on `-editor` repos).
- *Decide the packaging strategy now, in this same decision* — rejected: no stack choice has been made yet (same open question as `mode-quick-versus`'s backlog `006`); forcing one now would be premature and is better resolved as its own piece of work, possibly jointly with `006` if a shared stack turns out to make sense.
