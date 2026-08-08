# CLAUDE.md — roadmap

## Project overview

`roadmap` is the org-level planning repo for OpenKakutou (github.com/openkakutou). It holds what doesn't belong to any single repo: which repos exist or are planned, how they depend on each other, and decisions/backlog items that span more than one repo.

**Stack:** none — markdown only, no code, no build, no tests.
**Type:** planning / meta

## Project language

English — all documentation, backlog items, decisions and other generated content for this project must be written in English (matches the convention in every other OpenKakutou repo).

## What belongs here vs. in a repo's own `.vibe/` <!-- keep -->

This is the one decision to get right every time something needs tracking. Default to the repo's own backlog unless it clearly fails the test below.

**Belongs here (`roadmap`):**
- A new repo being proposed, scoped, or sequenced (e.g. "define what `engine` needs before it can start").
- Coordination *between* repos: which one should move first, a naming/ownership ambiguity spanning two repos, an org-wide convention (license, CI pattern, versioning scheme).
- A decision that would still be true even if every current repo were rewritten from scratch.

**Belongs in the repo's own `.vibe/backlog/` instead:**
- Any concrete implementation task, bug, or feature — even if it's motivated by another repo's needs. Example: `character` needing a WASM entrypoint for `character-viewer-web` to consume is tracked as a `character` backlog item (it already is — see `character/.vibe/backlog/033-wasm-entrypoint-and-release-pipeline.md`), not duplicated here. If cross-repo context is useful, this repo can *link* to that item from `repos.md` or a decision — never copy its content, or the two will drift.
- A design decision local to one repo's own code (its own `.vibe/decisions/`).

When in doubt: if the item disappears the moment a specific repo is deleted, it belongs in that repo, not here.

## Structure <!-- keep -->

```
roadmap/
├── repos.md            # status table: every repo, active/planned/idea, one-line role
├── .vibe/
│   ├── backlog/         # org-level backlog items (see split above)
│   └── decisions/       # ADRs for decisions that span repos
```

Same `.vibe/backlog/` and `.vibe/decisions/` conventions as every other OpenKakutou repo (frontmatter, numbering, lifecycle) — see `.vibe/README.md`. Managed the same way, via `/vibe:backlog` and friends; there's just no code/tests/lint step here, so the TDD workflow other repos document doesn't apply.

## Workflow

- Add/update planned or future repos in `repos.md` directly.
- Track org-level work as backlog items under `.vibe/backlog/`, same frontmatter (`status: todo|doing|done`) as other repos.
- Record a decision under `.vibe/decisions/` whenever a cross-repo choice is made (new repo greenlit, org convention adopted, repo's scope redefined) — same ADR format as other repos (`date`, `status`, Context/Decision/Reason/Rejected alternatives).
- The user is the Product Owner: describes what to plan, decides priority and scope. This repo's job is to make that persist and stay organized, not to invent roadmap items unprompted.
