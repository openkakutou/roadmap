#!/usr/bin/env bash
# One-shot dashboard regeneration: build_data.py + render.py behind a single
# entry point, so a refreshing agent needs only one Bash call instead of
# three. Self-locates via $0, so it works regardless of cwd or where the
# workspace was checked out.
#
# Usage: bash refresh.sh   (from anywhere)
#
# On success: prints `RENDERED_FILE=<absolute path>` as the last line —
# publish that file via the Artifact tool.
# On failure (e.g. a repo directory missing/renamed): a clear error goes to
# stderr and the script exits non-zero. Do not improvise a workaround —
# report the error.
#
# Versioned tooling, same as build_data.py/render.py/template.html — an
# automated refresh run must not edit this file, only consume it.
set -euo pipefail

DASHBOARD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(dirname "$(dirname "$DASHBOARD_DIR")")"
DATA_JSON="$DASHBOARD_DIR/dashboard_data.json"
RENDERED="$DASHBOARD_DIR/rendered.html"

python3 "$DASHBOARD_DIR/build_data.py" "$WORKSPACE_ROOT" "$DATA_JSON"
python3 "$DASHBOARD_DIR/render.py" "$DASHBOARD_DIR/template.html" "$DATA_JSON" "$RENDERED"

echo "RENDERED_FILE=$RENDERED"
