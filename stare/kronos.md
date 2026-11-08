# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-08 11:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #513** (KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #477 și #459 rezerve. Release `kronos-kgr1-513` nefăcut (luni, Adrian).
- **S89 (gata 8 nov 01:30): modelul de 24 de straturi (183M) a mers 5 ore fără să cadă** (leacul de memorie din S87 ține: vârf 6.465 MB, 62 °C).
  Verdict **LA FEL** cu #513: română curat 1,2063 vs 1,2060; nimic stricat (R1 instrucțiuni 99,20). A văzut doar 237 M simboluri față de 707 M la #513.
- **S92 (C-85 pasul 4b, gata 02:11):** cercetătorul în avans mută schimbări relative (rata × 2), iar modelul mic de 6 straturi e tăiat din cel de 24
  (pornește slab: română 2,78, trebuie „reparat” scurt).
- **S93 (C-88, gata 02:36):** examenul de română decide de acum pe linia nouă `w2_mare_24r`; paznicul îi păzește amprenta, `kronos/` neschimbat.
- S90/S91 (7 nov): examenul de română e modul separat; unealta „model mic trimis în avans” merge; `kronos/` neschimbat.
- **S88 (C-86): oprit** — ștergerea celor 82 de modele intermediare (33,4 GB) așteaptă mâna lui Adrian.
- **S94a (8 nov 08:52): oprit, motiv bun** — paznicul a anulat repararea modelului mic la 600 s (simbolurile se refăceau într-un cache gol);
  nimic antrenat, placa n-a lucrat. Reparație aleasă: citire din cache-ul comun `lucru/cache` (doar citit). S94 din nou `aprobat`.
- **1336 teste trec, 0 pică.**

## Urmează
- **8 nov ziua (placa, repornire cel târziu 15:30): S94a** — modelul mic: reparare 45 min + 5 rețete × 15 min. **Noaptea 8→9: S94b** — aceleași 5 rețete × 1 oră pe modelul de 24.
  Verdict Spearman (ρ ≥ 0,7 și câștigătorul mic în primele 2 = DA). Totul gata până **luni 07:00**; luni placa e liberă pentru testul OS (C-83).
- Apoi: continuarea liniei de 24 de straturi (curba încă scade) și pașii 5–8 din C-85, câte unul.

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
- Release-ul `kronos-kgr1-513` — luni 9 nov, cu Adrian la workstation.
- Fereastra lui Adrian pentru testul OS (luni 9 nov, C-83) — Kronos ține placa liberă atunci.
- Opțional: arhiva de mutare (26,2 GB) + Coșul. Fără grabă: S58, `taskkill`, ora 18:30 la bucla automată, Release-ul `kronos-kgr1-477`.
