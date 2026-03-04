# UE IPR Registry — Events

Registro aggiornamenti, correzioni e normalizzazioni.

Formato:
- data
- evento
- riferimento (commit / manifest)

- date: 2026-03-04T17:42:35+01:00
  event: "normalize events path + ipr-4 filename (refactor)"
  ref: "commit 02420db"

- date: 2026-03-04T17:44:36+01:00
  event: "bridge: GitJoker-C2 ACT chain published + verifiable (Ed25519) — UE IPR registry reference"
  ref:
    repo: "manuelcoletta1-source/gitjoker-c2"
    commits:
      - "adae01c fix(verify): support genesis resets for bootstrap act chains (strict by default)"
      - "df1f52b feat(keys): add Ed25519 public key ref for act signature verification"
      - "4915108 chore(gitignore): ignore runtime verification artifacts"
    acts:
      verified: 3
      segments: 2
      last_entry_sha256: "ec1d82731237c66b63bce77fd0ffb011f80df2f949b19753ff5483f403998d5b"
    verifier:
      cmd: "python3 /home/manuelcoletta1/gitjoker-c2/tools/verify_acts.py --allow-genesis-resets"

- date: 2026-03-04T17:51:31+01:00
  event: "refactor issued index as hash-only + fail-closed entry"
  ref: "commit 8f99d3b (refactor(issued))"
