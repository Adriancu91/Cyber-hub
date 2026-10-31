# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-31 11:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#477** (română 1,2097; mai mic = mai bine) — **S51 CONFIRMAT** (a doua noapte din #459, fără cădere; cod 0,7270, R2 0,4060, toate validările puțin mai bune).
  Câștigul scade (−0,0065 față de −0,017 prima noapte), deci nu urmează o a treia noapte la fel. În OS rulează încă **#459** (os-195, Release `kronos-kgr1-459`); #477 îl înlocuiește doar cu „da”-ul lui Adrian.
- **CCM (Cyber-Compute-Module), etapele 1–4 gata și verificate:** S47 profilul (înmulțirile ~73 % din timp); S48 modulul `inferenta_ccm` (portul `inferenta`,
  reglaj salvat + rezervă, simboluri identice); S49 placa video (doar **fp32** corectă; fp16/bf16 respinse); **S50 bancul măsoară „rece” și „cald”
  (în același motor) și alege după cald:** procesor **1 fir 2,30 s vs toate firele 3,14 s (1,36×)**, placa fp32 1,25 s (1,84× față de procesor). Placa nu se
  folosește implicit. Efectul „toate firele rapid la primul răspuns” din S49 nu s-a repetat azi. 1119 teste trec.
- Kronos-Cod (C-28): **descărcarea întreagă S46 (C-43) gata** în 2 nopți: **3,87 GB cod curat, ~1,10 mld simboluri** (Python + Rust + puțin C), licențe permisive, data-limită 29 iunie 2021, proveniență pe fișier. Sub estimarea de 3–6 mld (multe crates fără fișier de licență; lista PyPI de la sursă = 15.000). Acum: **S53** (doar procesor) verifică dacă examenul de cod ascuns apare în date.
- S44 INFIRMAT (bucăți tăiate 297/500 vs întregi 336/500): memoria E3 rămâne pe #438.
- S45 (căzută la 29 oct 23:09 din cauza unei reporniri a calculatorului, probabil pană de curent) închisă fără verdict; repetată ca S51.
- **Rulează / urmează azi: S53** (verificarea scurgerii, procesor). Placa e liberă.

## Urmează
- S53: examenul de cod ascuns curat sau nu în datele descărcate (listă de excludere, nimic șters).
- Pe placă: nimic până la decizia lui Adrian. Tokenizerul pe cod: al doilea „da”.

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) + Release-ul privat cu #459 (#477 poate urma, după „da”).
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Bancul CCM rece/cald (S50): pe Windows, 1 fir e cel mai rapid pe procesor la răspunsuri repetate — de măsurat la fel în OS. Profilul S47 pe operații (MLP 37 %, QKV 18 %, ieșirea atenției 16 %, atenția 10 %) și lecția „pe un model mic, mai multe fire = mai lent” — util pentru C-40
  (OS: 69,5 simb/s pe 18 fire, așteptarea firelor 62,6 %).
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), ca modul `cautare`; verificatorul de răspunsuri.
- Cutia izolată pentru cod netestat (`unelte/kronos_cod/cutie.py`); un set de cod curat (~1,1 mld simboluri), cu licențe verificate și proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-40, viteza pe #459 și pe **1 fir** (simb/s), ca s-o punem lângă Windows (31 simb/s pe 1 fir) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- „da #477” dacă #477 îl înlocuiește pe #459 în interfață și în OS; ce să facă placa de acum.
- Cauza repornirii de la ~23:10 (probabil pană de curent): Adrian rulează comanda de citire din raportul S52 sau aprobă citirea jurnalelor Windows de către executant. Dacă e curent: UPS; dacă e Windows Update: „ore active”.
- Descărcarea codului e gata: tokenizerul pe cod cere un al doilea „da”; tot Adrian decide dacă ~1,1 mld simboluri ajung sau vrea surse în plus.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
