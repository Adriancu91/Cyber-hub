# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-07 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: încă #477** în `integrare/kronos/MODEL.md` (KGR1 Q8_0 110.859.040 octeți, `bcbe8187…3963`); #459 rezervă.
- **#513 (C-82, „Da 513”):** exportat KGR1 Q8_0 (110.859.008 octeți — cu 32 mai puțin doar din antet, aceeași arhitectură).
  S83 s-a oprit corect la verificarea mărimii; reluarea **S83b** (vectori de control, MODEL.md, Release `kronos-kgr1-513`) pornește acum, pe procesor.
- **Kronos mare (24 de straturi, 183M):** S85 (5 ore pe rețeta e1) a mers doar 2 ore — la ora 3 iar lipsă de memorie la testul rapid,
  la fel ca S77c → NEMĂSURAT. După 2 ore ține ce știa (română 1,2108 față de 1,2096 la pornire), dar nu e mai bun ca #513 (1,2060).
- **C-85 pasul 1 gata (S84):** lista modelelor salvate — 592 `.pt` / 107,6 GB, din care 71,5 GB „se pot șterge”; nimic șters, decide Adrian.
- **1254 teste trec, 0 pică.** Placa max 6.431 MB / 61 °C în S85.

## Urmează
- **Restul nopții 6→7:** S83b (procesor) și S86 — C-85 pasul 2: memoria plăcii la modelul mare (Muon față de AdamW) și de ce
  crește memoria de la o oră la alta; fără linii de 24 de straturi repornite până atunci.
- **După S83b:** copiez `MODEL.md` cu #513 în `integrare/kronos/` → deblochează P6-60 la OS.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 acum; **după S83b: #513** (suma nouă, 3 texte de control noi,
  mărimea 110.859.008 — diferă de #477 doar antetul). Rezervele #477 și #459 rămân pornibile.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- Nota automată pentru răspunsuri în română (`unelte/romana_raspunsuri.py noteaza`, fără alt AI) + setul ascuns de 500.
- Unealta `unelte/puncte_salvare.py` (listă cu clase PĂSTREAZĂ / SE POATE ȘTERGE, fără ștergere) — ideea se poate refolosi.
- Lecție: la un model crescut, rata mică ține ce știa modelul în prima oră (5e-5 strica, 1e-5 nu); la 6 GB, memoria
  se umple între ore lungi în același proces (de două ori la ora 3) — de urmărit și la alte antrenări lungi pe placă.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- „Da / nu / da, fără gpt.pt de linie” la ștergerea modelelor „se pot șterge” (S84: 71,5 GB; fără gpt.pt de linie: 33,4 GB).
- Dacă `gh` cere aprobare la S83b: Adrian rulează comanda de Release (va fi în raport și în MODEL.md).
- Opțional: ștergerea arhivei de mutare (26,2 GB) + golirea Coșului (o face Adrian).
- Fereastra lui Adrian pentru testul OS (luni 9 nov, C-83) — Kronos ține placa liberă atunci.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul `kronos-kgr1-477`.
