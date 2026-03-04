# UE IPR Registry — Issued (hash-only, append-only)

Elenco degli IPR **emessi e pubblicati** in forma **HASH_ONLY**.
Questo file NON contiene documenti né PII: solo riferimenti verificabili.

Policy:
- **FAIL_CLOSED**: se la verifica non è riproducibile ⇒ NON è “Issued”
- **HASH_ONLY**: niente contenuti sensibili, solo ID/hash/link pubblici
- **APPEND_ONLY**: nuove righe per aggiornamenti/correzioni, mai riscrittura selettiva

---

## Issued

### IPR-5 — GitJoker-C2 (Operational issuance environment)
- **Status:** ACTIVE
- **Scope:** EU (technical evidence, non-certification)
- **UE Registry manifest:** `ipr5-gitjoker.manifest.json`
- **Primary repo:** `manuelcoletta1-source/gitjoker-c2`

#### Verification (reproducible)
- Local verifier cmd:
  - `python3 /home/manuelcoletta1/gitjoker-c2/tools/verify_acts.py --allow-genesis-resets`
- Expected result:
  - `PASS_ACTS verified=3 segments=2 last_entry=ec1d82731237c66b63bce77fd0ffb011f80df2f949b19753ff5483f403998d5b`
- Public key reference (for act signature verification):
  - `keys/joker-c2.pub.json` in `gitjoker-c2`

Notes:
- “Issued” attesta solo **esistenza + continuità verificabile** via Git + verifica riproducibile.
- Non sostituisce eIDAS / registri istituzionali: è **evidenza tecnica opponibile**.
