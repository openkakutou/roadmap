---
date: 2026-08-09
status: accepted
---
# Adopt a shared `web-ui-kit` design system for every viewer/editor/mode web app

**Context:** The org is about to have up to seven independent web apps (`character-viewer-web`, `character-editor`, `stage-viewer-web`, `stage-editor`, `lifebar-viewer-web`, `lifebar-editor`, `mode-quick-versus`), each TypeScript/Vite with no framework. Left alone, each would reinvent its own buttons, panels, layout shell and input widgets, producing an inconsistent look and duplicated UI work — directly against the requirement that editors get a real graphical/ergonomic design pass, not just functional forms.

**Decision:** Create `web-ui-kit`: a shared, framework-agnostic library (native Web Components + CSS custom properties for tokens) covering design tokens (color, spacing, typography, light/dark), a shared layout shell (app frame, panels, tabs, toolbar), core form/input components (file drop-zone, sliders, color/palette picker, buttons), reusable canvas/viewport controls (zoom/pan, used by every sprite/stage/animation preview), and an accessibility baseline (keyboard navigation, focus states, contrast). Published as a plain ESM package consumable by any Vite app without a build-framework dependency. Every viewer/editor app adopts it early — before or alongside its first real screen, not bolted on afterward.

**Reason:** Framework-agnostic Web Components match the org's existing no-framework TS/Vite convention exactly, so adopting the kit doesn't force any app to add React/Vue/etc. Building shared visual/interaction patterns once, in one place with its own accessibility and cross-browser testing, is cheaper and more consistent than seven parallel, drifting implementations — and it's the direct answer to needing editors that are visually and ergonomically complete, not just functionally complete.

**Rejected alternatives:**
- *Each app builds its own UI from scratch* — rejected: guarantees visual inconsistency across the org's apps and duplicates the same component work seven times.
- *Adopt an existing third-party component framework (e.g. a React/Vue design system)* — rejected: would force every app off its current framework-free stack for the sake of a design system, when the actual need (shared tokens/components) doesn't require a UI framework at all.
