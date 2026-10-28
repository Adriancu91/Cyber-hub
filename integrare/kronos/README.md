# Kronos → Cyber Universe OS: pachetul KGR1 (C-24)

Scris de supraveghetorul Kronos. Greutăți reale **nu** se pun aici (sunt doar ca Release în repo-ul privat `cyberspace`).

| fișier | ce e | stare |
|---|---|---|
| `format_greutati.md` | specificația fișierului de greutăți KGR1 (F32 și Q8_0, tokenizerul inclus) — copie exactă a `docs/format_greutati.md` din cyberspace, commit `190bd38` | **aici** (28 oct 02:15) |
| `vectori/` | model KGR1 minuscul cu greutăți aleatoare (≤ 1 MB, F32 + Q8_0), 3 texte, logit-urile și generarea greedy de referință, toleranța declarată | vine după S39 partea A |
| `MODEL.md` | modelul real exportat (numărul, mărimea, SHA-256, eticheta Release-ului) + 3 texte cu primele 5 simboluri greedy | vine după S39 partea B |

Motorul OS se scrie din specificație, fără codul Kronos. Dacă specificația se schimbă în cyberspace, supraveghetorul o recopiază aici și notează commit-ul.
