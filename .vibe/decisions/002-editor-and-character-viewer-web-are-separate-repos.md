---
date: 2026-08-08
status: accepted
---
# `editor` and `character-viewer-web` are separate repos, not the same project

**Context:** `character`'s own CLAUDE.md names a future `editor` repo, built on top of the `character` library. Once `character-viewer-web` was created, it wasn't clear whether it *was* that `editor` project (perhaps under a different working name), an earlier step toward it, or a genuinely separate app.

**Decision:** They are two distinct repos, split by read vs. read+write scope:
- `character-viewer-web` — **visualize and control** an existing character: browse its sprites/palettes/characteristics/animations, trigger animations and moves live. Read-only against `character`.
- `editor` — **modify and/or create** a character. Read+write UI on top of `character`.

`editor` is not a rename or successor of `character-viewer-web`; both are expected to exist as separate apps.

**Reason:** Product Owner clarification. The split also matches `character`'s own design constraint of keeping its read path (pure-data, consumable by a viewer or a future engine) and write path (format-preserving serialization) as separate concerns — a read-only viewer and a read+write editor are the natural two consumers of that split, rather than one app trying to be both.

**Rejected alternatives:** Treating `character-viewer-web` as the `editor` project under a working name — rejected, since a read-only viewer and a read+write editor are different enough in scope (and UI) to stay separate apps rather than one growing into the other.
