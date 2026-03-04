# UE IPR Registry — Issued

Elenco **hash-only** degli IPR emessi e pubblicati (append-only).
Questo documento NON contiene PII né documenti: solo riferimenti verificabili.

Principi:
- **FAIL_CLOSED**: se una verifica non è riproducibile ⇒ non è “Issued”
- **HASH_ONLY**: niente contenuti sensibili, solo hash/ID/link pubblici
- **APPEND_ONLY**: non si riscrive la storia, si aggiungono eventi/righe

---

## Issued

### IPR-5 — GitJoker-C2 (Operational issuance environment)
- **Status:** ACTIVE
- **Scope:** EU (technical evidence, non-certification)
- **Evidence:** repository + act-chain + verification tools
- **References:**
  - Repo: `manuelcoletta1-source/gitjoker-c2`
  - UE Registry manifest: `ipr5-gitjoker.manifest.json`
  - Latest verification point (GitJoker-C2):
    - `verify_acts.py --allow-genesis-resets` ⇒ PASS (signature + chain)  
      Evidence bound to committed public key ref in `keys/`

Notes:
- Questo “Issued” attesta solo **esistenza + continuità verificabile** in ambiente pubblico Git.
- Non sostituisce eIDAS / registri istituzionali: è **evidenza tecnica opponibile**.
