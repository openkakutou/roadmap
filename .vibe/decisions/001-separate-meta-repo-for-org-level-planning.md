---
date: 2026-08-08
status: accepted
---
# Org-level planning lives in a separate `roadmap` repo, not inside an existing repo

**Context:** The organization plans to grow beyond its first two repos (`character`, `character-viewer-web`), with more repos already named in the roadmap (`editor`, `engine`). Each repo already tracks its own work well via `.vibe/backlog` and `.vibe/decisions`, but there was no place for planning that isn't scoped to one repo: which future repos to create, how they sequence, cross-repo coordination.

**Decision:** Create a dedicated repo, `roadmap`, holding only org-level planning: a `repos.md` status table and its own `.vibe/backlog`/`.vibe/decisions` for items that span repos. It follows the same markdown/git conventions as every other repo so it stays editable the same way, but has no code, tests, or CI.

**Reason:** Keeping this in an existing repo (e.g. `character`, since it already documents the org roadmap in its own CLAUDE.md) would tie org-level planning to that repo's lifecycle and make it look like `character`-specific work. A separate repo persists independently of any single project, is git-versioned (history, no reliance on chat memory), and reuses tooling/conventions the org already has instead of introducing a new system (e.g. GitHub Projects).

**Rejected alternatives:**
- *GitHub Projects / Issues at the org level* — native cross-repo visibility, but not directly editable as part of this workflow and a separate system to keep in sync.
- *Keep the roadmap section inside `character`'s CLAUDE.md* — what was already happening; rejected because it conflates one repo's context with the org's, and doesn't scale once `character` isn't obviously "first."
- *A local-only folder, not a git repo* — rejected because it doesn't persist with history or survive independently of this machine.
