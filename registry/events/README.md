# UE IPR Registry — Events (append-only)

Registro eventi e normalizzazioni del **UE IPR Registry**.
Questo file è **append-only**: in caso di errore si aggiunge una *correzione* (non si cancella).

## Format (machine-friendly)
Each entry MUST be:

- date: ISO-8601 (local offset allowed)
  event: short description (no PII)
  ref: commit / manifest / hash / external repo pointer (public)

## Policy
- **FAIL_CLOSED**: se non verificabile ⇒ non elevare a “Issued”
- **HASH_ONLY**: niente documenti, niente dati personali
- **APPEND_ONLY**: correzioni via nuove righe, non riscrittura selettiva

## Dedupe rule (non-destructive)
Se due eventi sono duplicati:
- si lascia tutto com’è
- si aggiunge una entry “correction: duplicate detected” con i riferimenti

---

## Timeline
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

- date: 2026-03-04T18:09:46+01:00
  event: "bridge GitJoker-C2 ACT update (append-only)"
  ref: "gitjoker-c2 act_id=3 entry_sha256=ec1d82731237c66b63bce77fd0ffb011f80df2f949b19753ff5483f403998d5b"

- date: 2026-03-04T18:10:52+01:00
  event: "bridge GitJoker-C2 ACT update (append-only)"
  ref: "gitjoker-c2 act_id=3 entry_sha256=ec1d82731237c66b63bce77fd0ffb011f80df2f949b19753ff5483f403998d5b"

- date: 2026-03-04T18:11:27+01:00
  event: "correction: duplicate event entry detected (append-only note)"
  ref: "duplicates: 2026-03-04T18:09:46+01:00 and 2026-03-04T18:10:52+01:00 are same act_id=3 entry_sha256=ec1d8273..."
