#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime, timezone
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run_verify():
    r = subprocess.run(
        ["python3", os.path.join(ROOT,"tools","verify_registry.py")],
        capture_output=True,
        text=True
    )
    ok = (r.returncode == 0) and ("PASS_REGISTRY" in r.stdout)
    return ok, r.stdout, r.stderr

def main():
    ok, out, err = run_verify()

    status = "PASS" if ok else "FAIL"
    now = datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

    os.makedirs(os.path.join(ROOT,"registry","status"),exist_ok=True)

    payload={
        "schema":"UE-IPR-REGISTRY-STATUS",
        "status":status,
        "ts_utc":now
    }

    with open(os.path.join(ROOT,"registry","status","status.json"),"w") as f:
        json.dump(payload,f,indent=2)

    with open(os.path.join(ROOT,"registry","status","status.txt"),"w") as f:
        f.write(f"REGISTRY_STATUS={status}\n")
        f.write(f"TS_UTC={now}\n")

    print("STATUS:",status)

if __name__=="__main__":
    main()
