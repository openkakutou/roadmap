---
status: todo
---
# Scope and create the `openkakutou.github.io` repo

## Description
Greenlit by `.vibe/decisions/018`: an `openkakutou.github.io` repo (GitHub's special org-site name, deploys at the bare root `https://openkakutou.github.io/`) will be the org's public-facing showcase site, listing and linking out to whichever viewer, editor, and complete game (`mode-*`) apps are currently live, updated as new ones ship. The repo doesn't exist yet — this item covers turning the decision into an actual repo with a scoped first version.

Open questions for the Product Owner before/at repo creation:
- Which live apps to list at launch (likely: `character-viewer-web`, `character-editor`, `stage-viewer-web`, `stage-editor`, `lifebar-viewer-web`, `lifebar-editor`, `mode-quick-versus`) and how each is described/categorized (viewer / editor / complete game).
- Stack: static site is the natural fit (matches every other web app in the org); whether it reuses `web-ui-kit` for visual consistency with the apps it links to.
- Hosting: GitHub Pages, same pattern as decision `015`, or something else.
- How the list stays up to date as new apps ship (manual edit vs. some generated data source) — keep it simple first, no need to over-engineer this at launch.

## Acceptance Criteria
- [x] `openkakutou.github.io` repo created under github.com/openkakutou with its own `CLAUDE.md` per org convention (`.vibe/` deliberately deferred — see Notes)
- [x] Stack choice recorded: plain HTML/CSS, no framework, no build step. Hosting: GitHub Pages via the special org-site repo name, root URL — Pages was already auto-enabled on repo creation (`build_type: legacy`, source `main` root)
- [x] First version live at https://openkakutou.github.io/ — links to the three currently-live `*-viewer-web` apps, with `character-editor`/`stage-editor`/`lifebar-editor`/`mode-quick-versus` shown as "in development" placeholders (no Pages deployment yet to link to)
- [x] `repos.md` status for `openkakutou.github.io` updated from "planned" to "active"
- [ ] `openkakutou.github.io` added to `REPO_ORDER`/`DOMAIN` in `dashboard/build_data.py` (org-wide) — left for a follow-up pass, low priority for a repo with no `.vibe/backlog` yet

## Notes
Raised from `.vibe/decisions/018`. Resolved 2026-08-10 per Product Owner's "create it now, simple site, iterate later": repo created, minimal hand-written `index.html`, no `.vibe/` scaffold or CI yet — noted in the repo's own `CLAUDE.md` as an intentional deferral, not an oversight, to revisit once the site grows past a single static page. Placeholder cards for editors/`mode-quick-versus` should become real links once those repos get their own GitHub Pages deployment (decision `015`'s pattern extended to them, still an open question per that decision's "deferred, not rejected" note).
