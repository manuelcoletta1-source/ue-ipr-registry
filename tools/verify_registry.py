#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------------------------------------------------------------
# fail-closed helpers
# ---------------------------------------------------------------------
def fail(msg: str, code: int = 1):
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(code)

def pass_msg(tag: str):
    print(tag)

def read_text(path: str) -> str:
    if not os.path.isfile(path):
        fail(f"missing file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_json(path: str):
    try:
        return json.loads(read_text(path))
    except Exception as e:
        fail(f"invalid JSON: {path} ({e})")

def run(cmd: list[str], cwd: str | None = None) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        out = (r.stderr or r.stdout or "").strip()
        fail("command failed:\n" + " ".join(cmd) + ("\n" + out if out else ""))
    return (r.stdout or "").strip()

# ---------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------
def check_events():
    p = os.path.join(REPO_ROOT, "registry", "events", "README.md")
    txt = read_text(p)

    # must have canonical header
    if not txt.startswith("# UE IPR Registry — Events (append-only)"):
        fail("events README missing canonical header")

    # must contain at least one timeline entry
    if not re.search(r"(?m)^\- date:\s+\d{4}\-\d{2}\-\d{2}T", txt):
        fail("events README has no '- date:' timeline entries")

    pass_msg("PASS_EVENTS")

def check_issued():
    p = os.path.join(REPO_ROOT, "registry", "issued", "README.md")
    txt = read_text(p)

    if not txt.startswith("# UE IPR Registry — Issued (hash-only, append-only)"):
        fail("issued README missing canonical header")

    # minimal anchor: must mention IPR-5
    if "IPR-5" not in txt:
        fail("issued README does not mention IPR-5")

    pass_msg("PASS_ISSUED")

def check_manifest():
    p = os.path.join(REPO_ROOT, "ipr5-gitjoker.manifest.json")
    j = read_json(p)

    # hard requirements (fail-closed)
    if j.get("schema") != "UE-IPR-MANIFEST":
        fail("manifest schema mismatch")
    if j.get("schema_version") != "1.0.0":
        fail("manifest schema_version mismatch")

    ipr = j.get("ipr") or {}
    if ipr.get("id") != "IPR-5":
        fail("manifest ipr.id must be IPR-5")
    if ipr.get("status") != "ACTIVE":
        fail("manifest ipr.status must be ACTIVE")

    holder = j.get("holder") or {}
    if holder.get("type") != "ipr_ref":
        fail("manifest holder.type must be ipr_ref (hash-only)")
    if holder.get("ipr_id") != "IPR-3":
        fail("manifest holder.ipr_id must be IPR-3")
    if holder.get("jurisdiction") != "EU":
        fail("manifest holder.jurisdiction must be EU")

    verification = j.get("verification") or {}
    act_chain = (verification.get("act_chain") or {})

    # act-chain section must exist for this verifier
    if not isinstance(act_chain, dict) or not act_chain:
        fail("manifest missing verification.act_chain section")

    pass_msg("PASS_MANIFEST")
    return j

def check_gitjoker_act_chain(manifest: dict):
    """
    Deterministic gate:
    - Reads verifier cmd and expected result from the UE manifest
    - Runs verifier inside local gitjoker repo
    - Compares deterministic 'PASS_ACTS verified=... segments=... last_entry=...'
    """
    verification = manifest.get("verification") or {}
    act_chain = verification.get("act_chain") or {}
    verifier = act_chain.get("verifier") or {}
    expected = act_chain.get("expected") or {}
    pubkey_ref = act_chain.get("pubkey_ref") or {}

    # Validate required fields
    cmd = verifier.get("cmd")
    where = verifier.get("where")
    if not cmd or not where:
        fail("manifest act_chain.verifier missing cmd/where")

    # For safety & determinism: accept only the canonical command form
    # (fail-closed if different)
    if not cmd.startswith("python3 tools/verify_acts.py"):
        fail("act_chain verifier cmd must start with: python3 tools/verify_acts.py")

    # local repo location (expected by your environment)
    gitjoker_root = "/home/manuelcoletta1/gitjoker-c2"
    if not os.path.isdir(gitjoker_root):
        fail(f"missing local gitjoker-c2 repo at {gitjoker_root}")

    # Ensure pubkey ref exists in that repo
    pub_path = pubkey_ref.get("path")
    if not pub_path:
        fail("manifest act_chain.pubkey_ref.path missing")
    pub_abs = os.path.join(gitjoker_root, pub_path)
    if not os.path.isfile(pub_abs):
        fail(f"missing act-chain pubkey ref file: {pub_abs}")

    # Run verifier cmd in gitjoker_root
    cmd_argv = cmd.split()
    out = run(cmd_argv, cwd=gitjoker_root).strip()

    # Must match deterministic PASS_ACTS line
    if not out.startswith("PASS_ACTS"):
        fail(f"act-chain verifier output not PASS_ACTS: {out}")

    # Parse numbers + last_entry from output
    m_ver = re.search(r"\bverified=(\d+)\b", out)
    m_seg = re.search(r"\bsegments=(\d+)\b", out)
    m_last = re.search(r"\blast_entry=([0-9a-f]{64})\b", out)
    if not (m_ver and m_seg and m_last):
        fail(f"act-chain verifier output not parseable: {out}")

    got_verified = int(m_ver.group(1))
    got_segments = int(m_seg.group(1))
    got_last = m_last.group(1)

    # Compare to manifest expected (fail-closed)
    exp_verified = expected.get("verified")
    exp_segments = expected.get("segments")
    exp_last = expected.get("last_entry_sha256")

    if not isinstance(exp_verified, int) or not isinstance(exp_segments, int) or not isinstance(exp_last, str):
        fail("manifest act_chain.expected must contain: verified(int), segments(int), last_entry_sha256(str)")

    if got_verified != exp_verified:
        fail(f"act-chain mismatch verified: expected={exp_verified} got={got_verified}")
    if got_segments != exp_segments:
        fail(f"act-chain mismatch segments: expected={exp_segments} got={got_segments}")
    if got_last != exp_last:
        fail(f"act-chain mismatch last_entry_sha256: expected={exp_last} got={got_last}")

    pass_msg("PASS_ACT_CHAIN")

def main():
    # core docs checks
    manifest = check_manifest()
    check_events()
    check_issued()

    # cross-repo act-chain check (GitJoker-C2)
    check_gitjoker_act_chain(manifest)

    pass_msg("PASS_REGISTRY")

if __name__ == "__main__":
    main()
