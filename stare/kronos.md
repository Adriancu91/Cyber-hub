# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-06 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **#513** (S76b, 5 nov): urmează instrucțiunile din setul ascuns (R1 98,97 vs 37,47 la #477), fără regresii. **S76c (6 nov): URMEAZĂ și cereri
  formulate altfel**, la limită (R1 83,22 vs 61,38; prag +20); slab la „județ și țară” spus altfel (7,5 % corect).
- **Kronos mare (24 de straturi, 183M):** S77c oprit după 2 ore din 5 (memorie), mai slab decât #477 din prima oră. Diagnoza S77d (rată mai mică)
  a fost închisă din afară după 20 min (repornirea workstation-ului pentru testul OS, C-79) → NEMĂSURAT, nimic stricat.
- **1247 teste trec, 0 pică.** Discul C: ~106 GB liberi la 11:15; Adrian a mai șters (C-81), S82 verifică.

## Urmează
- **Acum (6 nov, după-amiază):** S82 — verificare doar prin citire a spațiului după ștergerea lui Adrian (C-81). Adrian a plecat fără testul OS (C-80), placa e liberă.
- **Noaptea 6→7, de la 19:00:** S77e = reluarea S77d pe linii noi (24 de straturi, rate 1e-5 / 2e-5, 2 × 1 oră). #477 rămâne în uz.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Modelul de 24 de straturi e încă în probă
  și nu e mai bun deocamdată; nimic nu se schimbă în pachet fără „da”-ul lui Adrian.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- **Nota automată pentru răspunsuri în română** (`unelte/romana_raspunsuri.py noteaza`, deterministă, fără alt AI) + setul ascuns de 500.
- Lecții: un model crescut „neutru” poate pierde din ce știa în prima oră (se verifică ieftin înainte de o noapte); un lanț trebuie să se oprească
  la primul cod ≠ 0, iar uneltele trebuie să întoarcă cod ≠ 0 la orice oprire înainte de vreme (S81).

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Decizia: #513 îl înlocuiește pe #477? (ambele verdicte gata: S76b AJUTĂ, S76c URMEAZĂ).
- Opțional: după S82, golirea Coșului de reciclare și restul grupurilor din S79 (le face Adrian; agentul nu șterge nimic).
- Următoarea fereastră a lui Adrian pentru testul OS (os-250) — Kronos ține placa liberă atunci.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
