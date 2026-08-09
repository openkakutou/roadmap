---
date: 2026-08-09
status: accepted
---
# `web-ui-kit` is published to the public npmjs.org registry

**Context:** `web-ui-kit#006` ("Publish/Consumption Pipeline") needs a concrete distribution mechanism for the seven consumer apps (`character-viewer-web`, `character-editor`, `stage-viewer-web`, `stage-editor`, `lifebar-viewer-web`, `lifebar-editor`, `mode-quick-versus`) to install it "as a normal ESM dependency" (decision `011`). Three options were viable: a direct git dependency (no registry, mirroring how `sff`/`character` are consumed as Go modules via a bare git tag), the public npmjs.org registry, or GitHub Packages' npm registry.

**Decision:** Publish `@openkakutou/web-ui-kit` to the public npmjs.org registry. A GitHub Actions workflow, triggered on a version tag (mirroring the tag-triggered pattern already used by `character`/`sff`'s `release.yml`), builds the package and runs `npm publish` using an `NPM_TOKEN` repository secret.

**Reason:** npmjs.org is the standard, zero-friction path for consumers: a plain `npm install @openkakutou/web-ui-kit` with normal semver ranges (`^0.1.0`), no per-consumer registry configuration or auth token — unlike GitHub Packages, which requires an authenticated `.npmrc` even to install a public package, contradicting `web-ui-kit#006`'s own "zero extra build configuration" acceptance criterion.

**Rejected alternatives:**
- *Direct git dependency* (`"web-ui-kit": "github:openkakutou/web-ui-kit#v0.1.0"`, built on install via a `prepare` script) — rejected: no registry/token to manage, and consistent with how `sff`/`character` are already consumed, but semver-range updates are clunkier for consumers than a real registry, and it was judged worth the small extra CI/token setup to get normal `npm install` ergonomics.
- *GitHub Packages npm registry* — rejected: forces every consumer to configure an authenticated `.npmrc` even though the package is public, adding friction the other two options don't have.
