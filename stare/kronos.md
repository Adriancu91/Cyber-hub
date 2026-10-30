# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-30 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). Rulează în Cyber Universe OS (os-195); Release privat `kronos-kgr1-459`.
- **CCM (Cyber-Compute-Module), etapele 1–4 gata și verificate:** S47 profilul (înmulțirile ~73 % din timp); S48 modulul `inferenta_ccm` (portul `inferenta`,
  reglaj salvat + rezervă, simboluri identice); S49 placa video (doar **fp32** corectă; fp16/bf16 respinse); **S50 bancul măsoară „rece” și „cald”
  (în același motor) și alege după cald:** procesor **1 fir 2,30 s vs toate firele 3,14 s (1,36×)**, placa fp32 1,25 s (1,84× față de procesor). Placa nu se
  folosește implicit. Efectul „toate firele rapid la primul răspuns” din S49 nu s-a repetat azi. 1119 teste trec.
- Kronos-Cod (C-28): pilotul (S43) și unealta completă (S46a) gata și verificate; **descărcarea întreagă (S46, „da” de la Adrian, C-43): bucata 1 gata** (00:29–10:29, oprită curat la 10 ore): **3,73 GB cod curat, ~1,07 mld simboluri**, doar licențe permisive, data-limită 29 iunie 2021; 68,9 GB liberi pe disc. Mai trebuie cel puțin o bucată.
- S44 INFIRMAT (bucăți tăiate 297/500 vs întregi 336/500): memoria E3 rămâne pe #438.
- **S45 (a doua noapte de antrenare din #459) a căzut la 23:09, în ora 4/6**, fără eroare: **calculatorul s-a repornit** între 23:09 și 23:12 (confirmat din jurnalele de logare; cauza încă necunoscută, placa în limite). Închisă fără verdict; orele 1–3 (#469–#471) doar informative.
- S52 (diagnosticul repornirii, doar citire) **oprit**: jurnalele Windows nu se pot citi de executant. Placa a fost normală până în ultima secundă (64 °C, 6.116 MB) → nu supraîncălzire; probabil pană de curent (cum bănuiește Adrian), neconfirmat.

- **Rulează S51** (de la 19:00) = repetarea S45 de la capăt din #459, pre-înregistrată înainte de pornire, aceleași praguri (CONFIRMAT dacă română ≤ 1,2112). Sfârșit ~02:00.

## Urmează
- ~02:00: verdictul S51; apoi **S46 bucata 2** (fără placă).
- După descărcare: tokenizerul pe cod (al doilea „da” al lui Adrian).

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Bancul CCM rece/cald (S50): pe Windows, 1 fir e cel mai rapid pe procesor la răspunsuri repetate — de măsurat la fel în OS. Profilul S47 pe operații (MLP 37 %, QKV 18 %, ieșirea atenției 16 %, atenția 10 %) și lecția „pe un model mic, mai multe fire = mai lent” — util pentru C-40
  (OS: 69,5 simb/s pe 18 fire, așteptarea firelor 62,6 %).
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Cutia izolată pentru cod netestat (`unelte/kronos_cod/cutie.py`); în curând un set de cod curat, cu licențe verificate și proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-40, viteza pe #459 și pe **1 fir** (simb/s), ca s-o punem lângă Windows (31 simb/s pe 1 fir) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Cauza repornirii de la ~23:10 (probabil pană de curent): Adrian rulează comanda de citire din raportul S52 sau aprobă citirea jurnalelor Windows de către executant. Dacă e curent: UPS; dacă e Windows Update: „ore active”.
- Mai târziu: tokenizerul nou pe cod cere un al doilea „da”, după descărcare.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
