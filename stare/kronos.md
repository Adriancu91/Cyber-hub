# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-29 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). Rulează în Cyber Universe OS (os-195); Release privat `kronos-kgr1-459`.
- **S44 gata: INFIRMAT.** Tăierea bucăților de text pe propozițiile cu cuvinte din întrebare: 297/500 corecte față de 336/500 cu bucățile întregi (−7,8 puncte);
  tăierea scoate des propoziția cu răspunsul. Memoria E3: „alt model”, „altă rețetă” și „tăierea” sunt închise; cititorul rămâne #438.
- **S43a gata — Kronos-Cod (C-28), etapa 1b, pregătirea:** unealta pilotului de descărcare (doar licențe MIT/Apache/BSD verificate din metadate și din LICENSE,
  doar cod publicat înainte de 29 iunie 2021, filtre de cod generat/duplicat, oprire sub 40 GB liberi, arhive doar în memorie) + 48 de teste fără rețea. 1058 de teste trec.

## Urmează
- **S43 = pilotul de descărcare** (aprobat; ~30–45 min, procesor + internet): 500 PyPI + 500 crates + numpy, tokio, libuv. Descărcarea întreagă doar după verificarea pilotului.
- Placa video liberă: **S45** (încă o noapte de antrenare din #459, rețeta A) e propusă și așteaptă „da”-ul lui Adrian.

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Cutia izolată pentru cod netestat (`unelte/kronos_cod/cutie.py`); în curând un set de cod curat, cu licențe verificate și proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: viteza după C-29 (simb/s pe 1 fir și pe toate nucleele, pe #459) — fără grabă, nu blochează nimic.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- „Da” sau „nu” pentru **S45** (o noapte de antrenare din #459); fără el placa video stă liberă. Nu blochează pilotul de cod.
- Mai târziu: tokenizerul nou pe cod cere un al doilea „da”, după descărcare.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
