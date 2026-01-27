# UE-IPR-REGISTRY — Registro sperimentale (UE-oriented)

UE-IPR-REGISTRY è un registro **sperimentale** per la pubblicazione di
riferimenti tecnici verificabili relativi a IPR (Identity Primary Record).

## Principi
UE_FIRST · HASH_ONLY · AUDIT_FIRST · FAIL_CLOSED · EXPERIMENTAL

## Cosa pubblica
- digest verificabili (SHA-512)
- receipt firmate (ED25519) se presenti
- riferimenti a manifest (PACK_MANIFEST) se presenti
- metadati minimi (timestamp, versione)

## FAIL-CLOSED
Se una verifica fallisce o è indeterminata, il record **non è ammesso**.

## Non è
- registro civile
- sostituto eIDAS/EUDI
- albo o certificazione legale
- garanzia sul contenuto: garantisce solo verificabilità tecnica

## Collegamenti
- Gateway UE: https://manuelcoletta1-source.github.io/hermeticum-bce-platform/
- IPR Gateway: https://manuelcoletta1-source.github.io/hermeticum-bce-ipr/
- IPR-CORE: https://manuelcoletta1-source.github.io/ipr-core/
- UNEBDO: https://manuelcoletta1-source.github.io/unebdo/
- OPC: https://manuelcoletta1-source.github.io/opc/
