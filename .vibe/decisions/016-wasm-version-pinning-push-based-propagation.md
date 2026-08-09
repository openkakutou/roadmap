---
date: 2026-08-10
status: accepted
---
# Cross-repo WASM version pinning: exact pins, propagated by the producer's own release step

**Context:** Backlog item `004` flagged that no policy existed for how a consumer web app picks/updates the version of a producer library's (`character`, `stage`, `sff`, `engine`) WASM build it consumes. This stopped being theoretical: `character-viewer-web` pinned `character` `v0.3.0` in its deploy workflow, `character` shipped `v0.4.1` with a real-world bug fix (a MUGEN character failing to load), and nothing updated the consumer's pin — the fix existed but the deployed app couldn't benefit from it until someone noticed and bumped the tag by hand.

**Decision:**
- **Consumers pin an exact producer release tag**, not a range or "latest" — matches this org's existing convention of pinning GitHub Actions to an exact commit SHA rather than a floating tag, for the same reproducibility reason: a deploy should never change behavior without an intentional, visible commit.
- **Propagation is push-based, triggered by the producer's own release, not a separately scheduled poll.** When a producer repo's `/vibe:release` tags a new version, that same session — guided by a standing instruction in the producer's own `CLAUDE.md` — checks each known consumer for its pin, bumps it, runs the consumer's own test suite, and commits/pushes if green. No cron, no `/loop`; the trigger is the release event itself, which is already a deliberate, agent-driven action in this org's workflow.
- **Each consumer repo documents its own pin's exact location** (file + line pattern) in its own `CLAUDE.md`'s WASM-dependency section, so the producer-side step doesn't need a central registry to find what to bump — it reads the one file every session already loads for that repo.
- **If bumping breaks the consumer's tests, the propagation step stops and flags it** instead of forcing the bump through — an incompatibility surfaces immediately, at the producer's release time, not months later when a user reports a bug that was already fixed upstream.
- **Cross-library shared-dependency conflicts** (e.g. `stage` and `character-editor` pinning different `sff` releases) are explicitly out of scope for now — no real conflict has occurred yet; revisit if/when one does, rather than designing for a hypothetical.

**Reason:** The actual failure mode observed wasn't "we lack a strategy" in the abstract — it was "a fix shipped and nobody told the consumer to pick it up". A scheduled watcher would solve that too, but adds a new piece of always-running infrastructure for a need that only ever fires at release time, which the producer's own release action already knows is happening. Attaching propagation to that existing, human-triggered event is simpler and needs no new infrastructure — consistent with this org's preference (see `vibe:review-overengineering` being active across every repo) for not building recurring/speculative machinery ahead of a proven need.

**Rejected alternatives:**
- *Scheduled/`/loop` job polling producer releases across all consumers* — rejected: real automation, but new infrastructure (a recurring job, its own failure mode, its own place to monitor) for a trigger (a producer release) that already happens under an agent's direct control; push-based propagation gets the same outcome without it.
- *Consumers pin a semver range and always build against the latest matching release* — rejected: reintroduces exactly the "deploy behavior changes without a visible commit" risk this org's SHA-pinning convention for CI Actions already deliberately avoids.
- *A central cross-repo registry file that consumers/producers both read* — rejected for now: with a single real producer→consumer pin in existence (`character` → `character-viewer-web`), a registry is speculative machinery for a fan-out that doesn't exist yet; each consumer's own `CLAUDE.md` is sufficient today. Revisit if/when several consumers pin several producers and a registry actually earns its cost.
