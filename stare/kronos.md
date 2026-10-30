# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-30 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). Rulează în Cyber Universe OS (os-195); Release privat `kronos-kgr1-459`.
- **CCM (Cyber-Compute-Module), etapele 1–3 gata și verificate:** S47 profilul (înmulțirile ~73 % din timp); S48 modulul `inferenta_ccm` (portul `inferenta`,
  reglaj salvat + rezervă, simboluri identice): **28,3 vs 20,3 simb/s** (1,22× total) la răspunsuri repetate; S49 placa video (PyTorch): doar **fp32** corectă,
  **1,19×** față de procesor (52 vs 41 simb/s), fp16/bf16 respinse; placa 1,7 GB, pornire CUDA +3 s; placa nu se folosește implicit. 1113 teste trec.
  Lecție: pe Windows „toate firele” e rapid doar la primul răspuns dintr-un motor nou (~40 simb/s), apoi ~20; 1 fir ține ~28–31.
- Kronos-Cod (C-28): pilotul (S43) și unealta completă (S46a) gata și verificate; **descărcarea întreagă (S46, „da” de la Adrian, C-43) rulează** de la 00:29 (bucata 1 din ~3, ~10 ore, fără placă): la 06:41, 27.007 pachete văzute, 10.921 păstrate (licență bună), ~3,2 GB; 64 GB liberi pe disc.
- S44 INFIRMAT (bucăți tăiate 297/500 vs întregi 336/500): memoria E3 rămâne pe #438.
- **S45 (a doua noapte de antrenare din #459) a căzut la 23:09, în ora 4/6**, fără eroare: **calculatorul s-a repornit** între 23:09 și 23:12 (confirmat din jurnalele de logare; cauza încă necunoscută, placa în limite). Închisă fără verdict; orele 1–3 (#469–#471) doar informative.

## Urmează
- S46 bucata 1 (~10:30) → **S50** (bancul CCM rece/cald, procesor) → S46 bucata 2 → **S51** = repetarea S45 de la capăt din #459, aceleași praguri (CONFIRMAT dacă română ≤ 1,2112), cel mai devreme diseară.
- După descărcare: tokenizerul pe cod (al doilea „da” al lui Adrian).

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Lecția S48/S49 „rece vs. cald” (primul răspuns vs. următoarele) — de măsurat la fel în OS. Profilul S47 pe operații (MLP 37 %, QKV 18 %, ieșirea atenției 16 %, atenția 10 %) și lecția „pe un model mic, mai multe fire = mai lent” — util pentru C-40
  (OS: 69,5 simb/s pe 18 fire, așteptarea firelor 62,6 %).
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Cutia izolată pentru cod netestat (`unelte/kronos_cod/cutie.py`); în curând un set de cod curat, cu licențe verificate și proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-40, viteza pe #459 și pe **1 fir** (simb/s), ca s-o punem lângă Windows (31 simb/s pe 1 fir) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Cauza repornirii calculatorului de la ~23:10 (actualizare Windows / pană de curent / oprire de mână?) — dacă e de la actualizări, de amânat sau de fixat „ore active” (setare Windows, doar Adrian).
- Mai târziu: tokenizerul nou pe cod cere un al doilea „da”, după descărcare.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
