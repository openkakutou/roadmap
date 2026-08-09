#!/usr/bin/env python3
"""Scan every OpenKakutou repo's `.vibe/backlog/` and produce dashboard_data.json.

Usage:
    python3 build_data.py <workspace_root> [output_path]

<workspace_root> is the directory that holds every repo as a sibling checkout
(e.g. the local `kakutou/` workspace, or wherever the cloud routine checks
out `sources` — run `ls <workspace_root>` first if unsure which directory
that is). Each repo listed in REPO_ORDER below must exist as
`<workspace_root>/<repo>` with a real git checkout (used to date "done" items
via `git log`).

Output is a JSON blob matching the shape `template.html`'s embedded
`DATA`/`DOMAIN_LABEL` constants expect. See README.md in this directory for
the full regeneration contract.
"""
import os
import re
import sys
import glob
import json
import datetime
import subprocess

# Keep in sync with ../repos.md. Order here controls display order within
# each domain group in the dashboard.
REPO_ORDER = [
    "sff", "web-ui-kit",
    "character", "character-viewer-web", "character-editor",
    "stage", "stage-viewer-web", "stage-editor",
    "lifebar-viewer-web", "lifebar-editor",
    "engine", "roadmap",
    "mode-quick-versus",
]

DOMAIN = {
    "sff": "shared", "web-ui-kit": "shared",
    "character": "character", "character-viewer-web": "character", "character-editor": "character",
    "stage": "stage", "stage-viewer-web": "stage", "stage-editor": "stage",
    "lifebar-viewer-web": "lifebar", "lifebar-editor": "lifebar",
    "engine": "org-wide", "roadmap": "org-wide",
    "mode-quick-versus": "mode",
}

KNOWN_STATUSES = {"todo", "in_progress", "blocked"}


def parse_task(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    status = None
    m = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    if m:
        sm = re.search(r"^status:\s*(\S+)", m.group(1), re.M)
        if sm:
            status = sm.group(1)
    title_m = re.search(r"^#\s+(.+)$", content, re.M)
    title = title_m.group(1).strip() if title_m else os.path.basename(path)
    return status, title


def build(workspace_root):
    out = {
        "generated_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "repos": [],
    }
    totals = {"todo": 0, "in_progress": 0, "blocked": 0, "done": 0}
    all_done = []

    for repo in REPO_ORDER:
        repo_path = os.path.join(workspace_root, repo)
        base = os.path.join(repo_path, ".vibe", "backlog")
        pending_files = sorted(glob.glob(os.path.join(base, "*.md")))
        done_files = sorted(glob.glob(os.path.join(base, "done", "*.md")))

        counts = {"todo": 0, "in_progress": 0, "blocked": 0}
        pending = []
        for p in pending_files:
            status, title = parse_task(p)
            status = status if status in KNOWN_STATUSES else "todo"
            counts[status] += 1
            pending.append({"id": os.path.basename(p).split("-")[0], "title": title, "status": status})

        done_items = []
        for p in done_files:
            _, title = parse_task(p)
            try:
                ts = subprocess.run(
                    ["git", "-C", repo_path, "log", "-1", "--format=%cI", "--", os.path.relpath(p, repo_path)],
                    capture_output=True, text=True, timeout=5,
                ).stdout.strip()
            except Exception:
                ts = ""
            item = {"id": os.path.basename(p).split("-")[0], "title": title, "date": ts}
            done_items.append(item)
            all_done.append({"repo": repo, **item})

        for k in counts:
            totals[k] += counts[k]
        totals["done"] += len(done_items)

        total_all = counts["todo"] + counts["in_progress"] + counts["blocked"] + len(done_items)
        pct = round(100 * len(done_items) / total_all) if total_all else 0

        out["repos"].append({
            "name": repo, "domain": DOMAIN[repo],
            "todo": counts["todo"], "in_progress": counts["in_progress"],
            "blocked": counts["blocked"], "done": len(done_items), "total": total_all,
            "pct_done": pct, "pending": pending,
        })

    out["totals"] = totals
    out["totals"]["total"] = sum(totals.values())
    out["recent_done_global"] = sorted(
        (x for x in all_done if x["date"]), key=lambda x: x["date"], reverse=True
    )[:12]
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    workspace_root = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "dashboard_data.json"
    data = build(workspace_root)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"wrote {output_path}: {data['totals']}")
