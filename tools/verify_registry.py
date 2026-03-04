#!/usr/bin/env python3
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def fail(msg: str) -> None:
    print("FAIL_CLOSED:", msg)
    raise SystemExit(1)

def _require_file(path: str) -> None:
    if not os.path.isfile(path):
        fail(f"missing file: {path}")

def verify_manifest() -> None:
    path = os.path.join(ROOT, "ipr5-gitjoker.manifest.json")
    _require_file(path)

    try:
        with open(path, "r", encoding="utf-8") as f:
            j = json.load(f)
    except Exception as e:
        fail(f"manifest JSON parse error: {e}")

    # Minimal deterministic checks (fail-closed)
    if j.get("schema") != "UE-IPR-MANIFEST":
        fail("manifest schema mismatch")
    if j.get("ipr", {}).get("id") != "IPR-5":
        fail("manifest ipr.id mismatch (expected IPR-5)")
    holder = j.get("holder", {})
    if holder.get("type") != "ipr_ref":
        fail("manifest holder.type mismatch (expected ipr_ref)")
    if holder.get("ipr_id") != "IPR-3":
        fail("manifest holder.ipr_id mismatch (expected IPR-3)")

    print("PASS_MANIFEST")

def verify_events() -> None:
    path = os.path.join(ROOT, "registry", "events", "README.md")
    _require_file(path)
    print("PASS_EVENTS")

def verify_issued() -> None:
    path = os.path.join(ROOT, "registry", "issued", "README.md")
    _require_file(path)
    print("PASS_ISSUED")

def main() -> None:
    verify_manifest()
    verify_events()
    verify_issued()
    print("PASS_REGISTRY")

if __name__ == "__main__":
    main()
