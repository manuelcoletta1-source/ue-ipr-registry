# Submission (come proporre un record)

## Requisito
Il record deve essere verificabile offline:
- hash SHA-512 del `ipr.canon.json`
- receipt ED25519 (se presente)
- manifest (se dichiarato)

## Cosa inviare (hash-only)
- canon_hash_sha512
- receipt (firma + public key) o riferimento
- hash del PACK_MANIFEST (se presente)
- timestamp e versione

## Divieti
- vietato inserire documenti
- vietato inserire dati personali identificativi
- vietato inserire contenuti sensibili

## Esito
- LISTED solo con verifiche complete
- altrimenti REJECTED (fail-closed)
