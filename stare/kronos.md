# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-06 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **#513** (S76b, 5 nov): urmează instrucțiunile din setul ascuns (R1 98,97 vs 37,47 la #477), fără regresii. Generalizarea se măsoară azi (S76c).
- **Kronos mare (24 de straturi, 183M, crescut din #477):** S77b a căzut după 1 minut (memorie); **S77c (noaptea 5→6) OPRIT după 2 ore din 5** —
  out of memory la ora 3 (placa max 6.433 MB, 64 °C, nimic stricat). Verdict NEMĂSURAT; informativ la ora 2 **mai slab decât #477**
  (română 1,2268 vs 1,2096, R2 0,4155 vs 0,4060), încă din prima oră.
- **Discul C: al workstation-ului: 34 GB liberi** (sub pragul de 40 GB) → 1 test pică din cauza discului (1237 trec), nu a codului.

## Urmează
- **Noaptea asta (procesor + disc):** S78 (C-77, salvarea „Mini Brain”, nimic șters) → S79 (C-76, raportul de spațiu + propunere de curățenie, nimic șters).
- **6 nov ziua:** S81 (o oră anulată oprește lanțul cu cod ≠ 0) → S77d (placa, ~2,5 h, după fereastra lui Adrian: modelul mare cu rată mai mică, 2 × 1 oră);
  S76c (procesor): #513 urmează instrucțiuni formulate altfel? Noaptea 6→7 se decide după S77d. #477 rămâne în uz.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Un model mai mare (24 de straturi, KGR1 F32 ~733 MB,
  memorie ~2×, viteză ~½) e încă în probă și nu e mai bun deocamdată; nimic nu se schimbă în pachet fără „da”-ul lui Adrian.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- **Nota automată pentru răspunsuri în română** (`unelte/romana_raspunsuri.py noteaza`, deterministă, fără alt AI) + setul ascuns de 500.
- Lecția S77c: un model crescut „neutru” poate pierde din ce știa în prima oră de antrenare; se verifică ieftin (o oră) înainte de o noapte.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **Discul C: aproape plin (34 GB liberi):** după raportul S79, Adrian alege ce grupuri se șterg (agentul nu șterge nimic).
- După S78: confirmarea că poate șterge folderele „test ai brain” (doar după „Mini Brain salvat”).
- Decizia: #513 îl înlocuiește pe #477? (recomandat după S76c).
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
