# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-07 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #513** (C-82, S83b gata 02:39): KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`; aceleași simboluri ca
  PyTorch. `integrare/kronos/MODEL.md` e la zi cu #513. #477 și #459 rămân rezerve. Release `kronos-kgr1-513` nefăcut (îl face Adrian).
- **C-85 pasul 2 (S86, gata 04:06): DA** — cu optimizatorul Muon, modelul de 24 de straturi (183M) folosește la antrenare cu 649 MB
  mai puțin decât cu AdamW; încape la loturile 4×24, 6×16, 12×8. AdamW la lotul obișnuit nu mai încape. Locul strâmt e validarea.
- Paza de memorie la fiecare oră pusă în unealta de antrenare (oprire curată peste 6.700 MB).
- **1278 teste trec, 0 pică.** Placa max 6.431 MB / 63 °C.

## Urmează
- **Ziua de 7 nov (08:00–18:30): S87** — de ce crește memoria plăcii de la o oră la alta (căderile de la ora 3 din S77c și S85):
  3 ore scurte cu Muon, în ordinea orchestratorului, cu și fără golire. Abia după aceea o noapte lungă cu modelul mare.
- **S88 (C-86, Adrian):** se șterg cele 82 de modele intermediare (~33,4 GB; numele, SHA și scorul scrise înainte); cele 31 de `gpt.pt` de linie
  și rezervele rămân; apoi, după S87, copiile de lucru `lucru/memorie_mare/` (9,8 GB). Procesor + disc, nu încurcă S87.
- Apoi C-85 pasul 3: examenul de română ca modul nou (fără schimbări în nucleu).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma nouă, 3 texte de control, mărimea 110.859.008 —
  diferă de #477 doar antetul). Rezervele #477 și #459 rămân pornibile.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- Nota automată pentru răspunsuri în română (`unelte/romana_raspunsuri.py noteaza`, fără alt AI) + setul ascuns de 500.
- Unealta `unelte/puncte_salvare.py` (listă PĂSTREAZĂ / SE POATE ȘTERGE, fără ștergere) — ideea se poate refolosi.
- Lecții: la un model crescut, rata mică ține ce știa modelul (5e-5 strica, 1e-5 nu); pe 8 GB, un optimizator cu o singură stare
  (Muon) câștigă ~0,65 GB la 183M; validarea, nu antrenarea, e locul strâmt.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Release-ul `kronos-kgr1-513` — luni 9 nov, cu Adrian la workstation (C-86; comanda e în `integrare/kronos/MODEL.md`).
- Opțional: ștergerea arhivei de mutare (26,2 GB) + golirea Coșului (o face Adrian).
- Fereastra lui Adrian pentru testul OS (luni 9 nov, C-83) — Kronos ține placa liberă atunci.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul `kronos-kgr1-477`.
