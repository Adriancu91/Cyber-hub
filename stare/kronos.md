# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-07 14:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #513** (KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #477 și #459 rezerve. Release `kronos-kgr1-513` nefăcut (luni, Adrian).
- **S87 (C-85 pasul 2, gata 10:04): găsită cauza căderilor de la ora 3** la modelul de 24 de straturi: de la o oră la alta rămâneau
  ținuți ~1.340 MB pe placă (cicluri de obiecte). Cu `gc.collect()` + golire la începutul fiecărei ore rămân 16 MB și trec toate orele
  (vârf 6.399 MB). Leacul e în unealta de antrenare; nucleul `kronos/` nu se schimbă.
- **S90 (C-85 pasul 3, gata 12:26): examenul de română e modul separat** (`examen_romana`): aceleași cifre ca înainte
  (#513 1,2060, #477 1,2096, ± 0,001; R1 99,27), setul păzit cu amprente SHA-256; neactivat în nicio configurare fără Adrian.
- **S88 (C-86): oprit** — unealta de ștergere și proba sunt gata (exact 82 fișiere / 33,4 GB), dar regula executantului interzice ștergerea; decide Adrian.
- **1306 teste trec, 0 pică.** Placa liberă ziua.

## Urmează
- **Azi, procesor: S91** — C-85 pasul 4a: unealta „cercetător cu model trimis în avans” (rețetele încercate pe un model mic, pe cel mare doar câștigătorul); doar unealtă + teste.
- **Noaptea 7→8 (de la 19:00): S89** — reluarea nopții de 5 ore pe modelul de 24 de straturi (rețeta e1, acum cu paza nouă): bate #513 la timp egal?
- Apoi C-85 pasul 4b (pe placă: prezice modelul mic clasamentul celui mare?) și pașii 5–8, câte unul.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 rămân pornibile.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- Nota automată pentru răspunsuri în română (fără alt AI) + setul ascuns de 500; acum și ca modul de examen `examen_romana` (amprente pe set).
- Unealta `unelte/puncte_salvare.py` (listă + ștergere cu probă implicită, jurnal SHA înainte de ștergere).
- Lecții: rata mică ține ce știa un model crescut; Muon câștigă ~0,65 GB la 183M; **memoria plăcii se poate aduna de la o oră la alta
  din cicluri de obiecte Python — `gc.collect()` înainte de `empty_cache()` o eliberează.**

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm oprirea scriptului la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) + `lucru/memorie_mare` (10,5 GB) — Adrian rulează comanda din raportul S88 sau dă executantului o excepție pentru ștergeri aprobate.
- Opțional: „da examen română” — modulul `examen_romana` folosit în configurări (paznicul îi memorează amprenta).
- Release-ul `kronos-kgr1-513` — luni 9 nov, cu Adrian la workstation.
- Fereastra lui Adrian pentru testul OS (luni 9 nov, C-83) — Kronos ține placa liberă atunci.
- Opțional: arhiva de mutare (26,2 GB) + Coșul. Fără grabă: S58, `taskkill`, ora 18:30 la bucla automată, Release-ul `kronos-kgr1-477`.
