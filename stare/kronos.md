# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-28 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). Rulează în Cyber Universe OS cu exact aceleași simboluri ca referința (os-195).
  Release-ul privat `kronos-kgr1-459` e publicat (28 oct 13:08).
- **S41 gata — Kronos-Cod (C-28), etapa 1a:** lista surselor de cod cu licențe permisive (6 surse fără cont, ~3 mld simboluri estimate),
  examenul de cod cu 200 de probleme ascunse (referințele 200/200, corpul gol 0/200) și cutia izolată pentru codul generat (rețea, fișiere din afară,
  procese, `ctypes` blocate; limite de timp și memorie). Fără descărcări. 999 de teste trec.
- **S42 gata: INFIRMAT.** Cititorul E3 refăcut din #459 cu rețeta A (#466) răspunde corect la 66/100, exact cât #438 (prag +5); S4 −3.
  Concluzia: plafonul vine din bucățile de text date modelului, nu din model. Cititorul rămâne #438. 1003 teste trec.
- Kronos-Cod etapa 1b: Adrian a spus „da” pentru pilotul de descărcare (data-limită 29 iunie 2021, fără surse cu cont). S43a scrie întâi unealta, fără rețea.

## Urmează
- S43a (unealta pilotului de descărcare, fără rețea), apoi pilotul S43 (~1 oră, procesor + rețea), apoi descărcarea întreagă după verificarea pilotului.
- S44: bucățile tăiate pe propozițiile utile (să încapă mai multe în 448 de simboluri), măsurat pe validare (500 de întrebări), praguri scrise înainte.

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru profilul de viteză din C-29.
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Nou: o cutie izolată pentru rularea de cod Python netestat (`unelte/kronos_cod/cutie.py`, în cyberspace) — utilă oricui rulează cod generat.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: viteza după C-29 (simb/s pe 1 fir și pe toate nucleele, pe #459) — fără grabă, nu blochează nimic la Kronos.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Nimic acum. (Tokenizerul nou pe cod va cere un al doilea „da”, după descărcare.)
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
