# Cross-repo task dashboard

A single-page dashboard aggregating `.vibe/backlog/` status (todo / in_progress
/ blocked / done) across every OpenKakutou repo, published as a Claude
Artifact and kept up to date by a scheduled cloud routine.

**Live URL:** https://claude.ai/code/artifact/3770391f-9d0d-4fe9-bcea-8594c75d180a
**Routine:** see `openkakutou-dashboard-refresh` at https://claude.ai/code/routines

## How it works

1. `build_data.py <workspace_root>` walks every repo listed in `REPO_ORDER`
   (kept in sync with `../repos.md`), reads each `.vibe/backlog/*.md`
   (pending) and `.vibe/backlog/done/*.md` (done), parses the `status:`
   frontmatter and the `# Title` heading, and writes `dashboard_data.json`.
2. `render.py` substitutes that JSON into `template.html`'s
   `/*__DASHBOARD_DATA_JSON__*/` placeholder, producing a ready-to-publish
   HTML page.
3. The rendered page is published via the Artifact tool with `url` set to
   the live URL above, so it updates in place instead of minting a new link.

## Regeneration contract — read before touching `template.html`

- `template.html` is a self-contained page (fonts embedded as base64
  `@font-face` data URIs, no external requests) with all markup/CSS/JS
  already in place. A refresh **only ever replaces the JSON assigned to
  the placeholder** — never regenerate or redesign the page from scratch.
- The placeholder is the exact string `/*__DASHBOARD_DATA_JSON__*/` inside
  a `<script>` block (`const DATA = /*__DASHBOARD_DATA_JSON__*/;`). If a
  design change is ever wanted, edit `template.html` directly (keeping that
  placeholder token intact) rather than hand-editing the rendered output.
- `DATA` shape: `{generated_at, totals: {todo, in_progress, blocked, done,
  total}, repos: [{name, domain, todo, in_progress, blocked, done, total,
  pct_done, pending: [{id, title, status}]}], recent_done_global: [{repo,
  id, title, date}]}`. `domain` must be one of `shared`/`character`/`stage`/
  `lifebar`/`org-wide`/`mode` (see `DOMAIN_LABEL` in `template.html`).

## Manual refresh

From this workspace (`kakutou/`, where every repo is a sibling checkout):

```sh
python3 roadmap/dashboard/build_data.py . roadmap/dashboard/dashboard_data.json
python3 roadmap/dashboard/render.py
```

Then publish `roadmap/dashboard/rendered.html` via the Artifact tool with
`url` set to the live URL above.

## Scheduled refresh

A cloud routine (`openkakutou-dashboard-refresh`, daily) clones every
OpenKakutou repo, runs the same two scripts, and republishes to the same
URL. Its prompt is intentionally self-contained (the cloud session starts
with zero context) — see the routine definition at
https://claude.ai/code/routines for the exact prompt if it ever needs
editing. If a repo is renamed or a new one is added, update `REPO_ORDER`/
`DOMAIN` in `build_data.py` **and** the routine's `sources` list.
