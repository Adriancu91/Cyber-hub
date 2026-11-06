# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-06 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **#513** (S76b, 5 nov): urmează instrucțiunile din setul ascuns (R1 98,97 vs 37,47 la #477), fără regresii. **S76c (6 nov): URMEAZĂ și cereri
  formulate altfel**, la limită (R1 83,22 vs 61,38; prag +20); slab la „județ și țară” spus altfel (7,5 % corect).
- **Kronos mare (24 de straturi, 183M):** S77c oprit după 2 ore din 5 (memorie), mai slab decât #477 din prima oră. Diagnoza S77d (rată mai mică)
  a fost închisă din afară după 20 min (repornirea workstation-ului pentru testul OS, C-79) → NEMĂSURAT, nimic stricat.
- **Decizia lui Adrian (C-82, 17:39): #513 devine modelul în uz**; exportul KGR1 + Release `kronos-kgr1-513` = S83 (procesor), după S77e. Până atunci MODEL.md arată tot #477.
- **1247 teste trec, 0 pică.** Discul C: 112,4 GB liberi (S82); arhiva de mutare (26,2 GB) încă există.

## Urmează
- **Acum (noaptea 6→7, de la 19:00):** S77e — 24 de straturi, rate 1e-5 / 2e-5, 2 × 1 oră (verdict la 23:15 / 02:15).
- **Apoi (procesor):** S83 — #513 în uz: KGR1 Q8_0, vectorii de control, `MODEL.md`, Release `kronos-kgr1-513` (#477, #459 rezerve) → deblochează P6-60 la OS.
- **Apoi:** S84 — C-85 pasul 1: lista punctelor de salvare `.pt` (doar listă); pașii 2–8 din C-85 câte unul.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 acum; **după S83: #513** (suma nouă, 3 texte de control noi, aceeași mărime 110.859.040),
  copiat de supraveghetor în hub la trecerea de după S83. Modelul de 24 de straturi e încă în probă.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- **Nota automată pentru răspunsuri în română** (`unelte/romana_raspunsuri.py noteaza`, deterministă, fără alt AI) + setul ascuns de 500.
- Lecții: un model crescut „neutru” poate pierde din ce știa în prima oră (se verifică ieftin înainte de o noapte); un lanț trebuie să se oprească
  la primul cod ≠ 0, iar uneltele trebuie să întoarcă cod ≠ 0 la orice oprire înainte de vreme (S81).

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Nimic urgent. Opțional: ștergerea arhivei de mutare (26,2 GB) + golirea Coșului (o face Adrian).
- După S84: „da/nu” la ștergerea modelelor marcate „se poate șterge”.
- Dacă `gh` cere aprobare la S83: Adrian rulează comanda de Release (scrisă în raport și în MODEL.md).
- Următoarea fereastră a lui Adrian pentru testul OS (luni 9 nov, C-83) — Kronos ține placa liberă atunci.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul `kronos-kgr1-477`.
