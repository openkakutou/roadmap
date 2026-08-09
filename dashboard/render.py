#!/usr/bin/env python3
"""Inject dashboard_data.json into template.html, producing a ready-to-publish page.

Usage:
    python3 render.py [template.html] [dashboard_data.json] [output.html]

Defaults to the files in this directory and writes `rendered.html` next to
them. The output is meant to be published via the Artifact tool, targeting
the dashboard's existing URL (see README.md) so it updates in place rather
than minting a new one.
"""
import sys
import json
import os

PLACEHOLDER = "/*__DASHBOARD_DATA_JSON__*/"


def render(template_path, data_path, output_path):
    template = open(template_path, encoding="utf-8").read()
    data = json.load(open(data_path, encoding="utf-8"))
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    if PLACEHOLDER not in template:
        raise SystemExit(f"placeholder {PLACEHOLDER!r} not found in {template_path} — did the template change shape?")
    out = template.replace(PLACEHOLDER, data_json, 1)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {output_path}: {len(out)} bytes")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    template_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "template.html")
    data_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, "dashboard_data.json")
    output_path = sys.argv[3] if len(sys.argv) > 3 else os.path.join(here, "rendered.html")
    render(template_path, data_path, output_path)
