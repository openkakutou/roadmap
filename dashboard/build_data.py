#!/usr/bin/env python3
"""Scan every OpenKakutou repo's `.vibe/backlog/` and produce dashboard_data.json.

Usage:
    python3 build_data.py <workspace_root> [output_path]

<workspace_root> is the directory that holds every repo as a sibling checkout
(e.g. the local `kakutou/` workspace, or wherever the cloud routine checks
out `sources` — run `ls <workspace_root>` first if unsure which directory
that is). Every sibling directory containing `.vibe/backlog/` is a repo
(used to date "done" items via `git log`); display order and domain come from
../repos.md.

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

REPOS_MD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "repos.md")

# Domains the dashboard template knows how to group (see template.html's
# domainOrder/DOMAIN_LABEL). Any other domain found in repos.md is folded into
# FALLBACK_DOMAIN so the repo is never silently dropped from the page.
KNOWN_DOMAINS = {"shared", "character", "stage", "lifebar", "org-wide", "mode"}
FALLBACK_DOMAIN = "org-wide"

# A repos.md table row: | domain | [`repo`](url) | status | role |
REPO_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*\[`([^`]+)`\]\([^)]*\)\s*\|\s*([^|]+?)\s*\|", re.M)


def load_repos_md():
    """Return [(repo, domain, status)] in repos.md order; [] if unavailable."""
    try:
        with open(REPOS_MD, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        print(f"warning: {REPOS_MD!r} not readable; domains and order fall back", file=sys.stderr)
        return []
    return [(name, domain.strip("()"), status) for domain, name, status in REPO_ROW.findall(content)]


def discover_repos(workspace_root):
    """Return [(repo, domain)] for every checkout in workspace_root with a backlog.

    The workspace itself is the source of truth for which repos exist: any
    sibling directory with `.vibe/backlog/` is included. repos.md only supplies
    display order and domain. An active repo from repos.md with no checkout is
    reported on stderr and skipped, never treated as fatal.
    """
    listed = load_repos_md()
    rank = {name: i for i, (name, _, _) in enumerate(listed)}
    domains = {name: domain for name, domain, _ in listed}

    found = sorted(
        (name for name in os.listdir(workspace_root)
         if os.path.isdir(os.path.join(workspace_root, name, ".vibe", "backlog"))),
        key=lambda name: (rank.get(name, len(rank)), name),
    )

    for name, _, status in listed:
        if status == "active" and name not in found:
            print(f"warning: active repo {name!r} has no checkout in {workspace_root!r}; skipped", file=sys.stderr)

    result = []
    for name in found:
        domain = domains.get(name)
        if domain not in KNOWN_DOMAINS:
            if domain:
                print(f"warning: repo {name!r} has unknown domain {domain!r}; using {FALLBACK_DOMAIN!r}", file=sys.stderr)
            domain = FALLBACK_DOMAIN
        result.append((name, domain))
    return result


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

    for repo, domain in discover_repos(workspace_root):
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
            "name": repo, "domain": domain,
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
