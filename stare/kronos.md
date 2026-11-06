# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-06 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **#513** (S76b, 5 nov): urmează instrucțiunile din setul ascuns (R1 98,97 vs 37,47 la #477), fără regresii. Generalizarea se măsoară azi (S76c).
- **Kronos mare (24 de straturi, 183M):** S77c (noaptea 5→6) oprit după 2 ore din 5 (memorie), mai slab decât #477 încă din prima oră; azi diagnoza (S77d).
- **Noaptea 5→6, gata:** S78 (C-77, Mini Brain salvat, 1,54 GB, 0 diferențe), S79 (C-76, raport de spațiu: ~104 GB se pot elibera fără pierdere),
  S81 (o oră anulată oprește acum lanțul cu cod 1). **1242 teste trec**; 1 pică doar din cauza discului (C: 31 GB liberi la 06:46, sub pragul de 40 GB).

## Urmează
- **6 nov ziua:** S76c (procesor, de la 08:00): #513 urmează și instrucțiuni formulate altfel? → S77d (placa, ~2,5 h, când Adrian nu e la workstation):
  modelul de 24 de straturi cu rată mai mică, 2 × 1 oră. Noaptea 6→7 se decide după S77d. #477 rămâne în uz.

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
- **Discul C: (31 GB liberi, scade):** Adrian alege ce grupuri din raportul S79 se șterg (A + B = 104 GB fără pierdere; C–H de decis). Agentul nu șterge nimic.
- Folderele „test ai brain” se pot șterge (Mini Brain salvat).
- Decizia: #513 îl înlocuiește pe #477? (recomandat după S76c).
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
