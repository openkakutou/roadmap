---
date: 2026-08-10
status: accepted
---
# Add an `openkakutou.github.io` repo: public showcase site for live viewer/editor/game apps

**Context:** Decision `015` gave each `*-viewer-web` app its own independent GitHub Pages deployment and explicitly rejected a unified portal *for now*, reasoning that with only three viewer apps discoverability wasn't yet a real friction point — but flagged it as "revisable once more viewer/editor/mode apps exist and navigating between them becomes a real friction point." The org has since grown past that point: `character-viewer-web`, `character-editor`, `stage-viewer-web`, `stage-editor`, `lifebar-viewer-web`, `lifebar-editor` are all active, and `mode-quick-versus` is the first complete playable game. The Product Owner now wants a repo whose job is presenting these to the outside world as they become visible/live — highlighting viewers, editors, and complete games — rather than leaving discovery to whoever already knows the GitHub org exists.

GitHub Pages treats one specific repo name specially: a repo named exactly `<account>.github.io` publishes at the bare domain root (`https://openkakutou.github.io/`) instead of the project-site sub-path every other repo gets (`https://openkakutou.github.io/<repo-name>/`, the pattern decision `015` already uses). Only one such repo is allowed per org. For a repo whose entire purpose is being the org's public landing page, the root URL is the better fit than a sub-path.

**Decision:** Create `openkakutou.github.io`, an org-wide repo sitting outside any single domain (like `engine`), using GitHub's special user/organization-site repo name so it deploys to the bare org root rather than a project-site sub-path. Its sole purpose is a public-facing showcase site: a landing page that lists and links out to each live viewer, editor, and complete game (`mode-*`) app, kept up to date as new apps ship or existing ones gain features. It does not host or re-implement any app's own functionality — each app keeps its own project-site deployment per decision `015`; this repo is a discovery/marketing layer on top, not a replacement for it. Status starts **planned** in `repos.md`; implementation specifics (stack, exact content) are deferred to the repo's own `.vibe/backlog` once created — tracked meanwhile by roadmap backlog item `005`.

**Reason:** Matches the Product Owner's stated intent directly. Distinct enough from decision `015`'s scope (per-repo hosting) that it doesn't need to reopen or amend that decision — it fills the exact gap `015` named as revisable, now that the trigger condition (more apps, real discoverability friction) has been met. The special repo name is a one-time naming choice with no downside (still a normal GitHub Pages deployment under the hood) and gets the memorable root URL a landing page should have.

**Rejected alternatives:**
- *Name it `website` (regular project-site repo, `.../website/` sub-path)* — rejected in favor of the root URL once the special-repo-name option was identified; no functional difference otherwise.
- *Fold a showcase page into `roadmap`'s own README* — rejected: `roadmap` is internal, contributor-facing planning (markdown/ADRs), not meant to be a public entry point for end users looking for the apps.
- *Keep deferring, per decision `015`'s original stance* — rejected: the condition `015` set for revisiting (more apps, real friction) is now met, and the Product Owner has decided to act on it.
