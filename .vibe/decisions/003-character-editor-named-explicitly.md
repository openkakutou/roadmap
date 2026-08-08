---
date: 2026-08-08
status: accepted
---
# The character editor is named `character-editor`, not `editor`

**Context:** Decision `002` split the planned `editor` repo from `character-viewer-web` by scope (read+write vs. read-only). Separately, a `lifebar-editor` is now anticipated: an editor for MUGEN/Ikemen lifebar files (health/power bar UI config), a distinct concern from character data. A bare `editor` name would collide/be ambiguous once more than one editor exists in the org.

**Decision:** Rename the planned repo from `editor` to `character-editor`. `repos.md` and future references use `character-editor` going forward; `002`'s use of `editor` stands as written (historical record of the scope decision, not the naming one).

**Reason:** Repo names should say what they edit, not just that they're an editor, once the org plans more than one. Matches the existing `character` / `character-viewer-web` naming pattern (domain-first).

**Rejected alternatives:** Keeping `editor` and disambiguating the lifebar one instead (e.g. `lifebar-editor` alone would then read inconsistently next to a bare `editor`) — rejected in favor of both being explicit about their domain.
