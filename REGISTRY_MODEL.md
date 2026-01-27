# Modello del registro (UE-IPR-REGISTRY)

## Oggetto record (hash-only)
Un record di registro NON contiene documenti o PII.
Contiene solo riferimenti verificabili:

- `ipr_id` (o digest)
- `canon_hash_sha512`
- `receipt_ed25519` (opzionale ma verificabile se dichiarata)
- `pack_manifest_hash` (opzionale)
- `created_at` (ISO-8601)
- `version`
- `status`: LISTED | REJECTED | REMOVED

## Stati
- LISTED: verifiche complete e coerenti
- REJECTED: verifiche fallite/indeterminate (fail-closed)
- REMOVED: rimozione per policy (es. dati personali pubblicati)

## FAIL-CLOSED (ammissione)
Qualsiasi errore/unknown ⇒ REJECTED
