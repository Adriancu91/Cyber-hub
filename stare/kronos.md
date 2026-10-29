# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-29 14:35 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). Rulează în Cyber Universe OS (os-195); Release privat `kronos-kgr1-459`.
- **S47 gata și verificat — CCM (Cyber-Compute-Module), etapa 1, doar procesor:** pe #459, Windows, numpy: cea mai rapidă e referința cu **1 fir**
  (2,47 s / 64 simb., 31 simb/s), de 1,37× mai rapidă decât cu toate cele 36 de fire; toate variantele dau simboluri identice; înmulțirile ~73 % din timp.
  1080 de teste trec. Planul: `cyberspace/docs/CCM_plan.md` (decizia din 29 oct 10:20).
- Kronos-Cod (C-28): pilotul (S43) și unealta completă (S46a) gata și verificate; descărcarea întreagă (S46) oprită corect — cere „da”-ul lui Adrian scris anume.
- S44 INFIRMAT (bucăți tăiate 297/500 vs întregi 336/500): memoria E3 rămâne pe #438.

## Urmează
- Acum pe procesor: **S48** (modulul `inferenta_ccm` pe portul `inferenta`, cu reglaj salvat și rezervă). **S49** (varianta pe placa video) după S48, cu placa liberă.
- Diseară de la 19:00: **S45** = încă o noapte de antrenare din #459 (aprobată; pragurile scrise înainte).
- **S46** = descărcarea întreagă a codului (~3 nopți, fără placă), doar după „da”-ul lui Adrian; apoi tokenizerul pe cod (al doilea „da”).

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Profilul S47 pe operații (MLP 37 %, QKV 18 %, ieșirea atenției 16 %, atenția 10 %) și lecția „pe un model mic, mai multe fire = mai lent” — util pentru C-40
  (OS: 69,5 simb/s pe 18 fire, așteptarea firelor 62,6 %).
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Cutia izolată pentru cod netestat (`unelte/kronos_cod/cutie.py`); în curând un set de cod curat, cu licențe verificate și proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-40, viteza pe #459 și pe **1 fir** (simb/s), ca s-o punem lângă Windows (31 simb/s pe 1 fir) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- „Da” sau „nu”, scris anume, pentru **S46** (descărcarea întreagă a codului, ~3 nopți, fără placă): aprobarea prin delegare nu ajunge pentru descărcări.
- Mai târziu: tokenizerul nou pe cod cere un al doilea „da”, după descărcare.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
- Dacă CONTINUUM (observatorul de noapte, oprit din 28 oct 12:36) să fie repornit.
