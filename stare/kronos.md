# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-31 14:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097; mai mic = mai bine; S51 CONFIRMAT) — **S54 gata (C-44):** export KGR1 Q8_0 110.859.040 octeți,
  SHA-256 `bcbe8187…3963`, modulele Kronos trec implicit pe #477, **#459 păstrat ca rezervă** (fișier neatins). `integrare/kronos/MODEL.md` arată acum #477.
- CCM (Cyber-Compute-Module): reglajul refăcut pentru #477 pe procesor (1 fir, 27,8 simb/s); partea de placă pentru #477 vine la S56.
- Kronos-Cod (C-28): 3,87 GB cod curat (~1,10 mld simboluri), licențe permisive; S53 DE CURĂȚAT — se exclud 3.821 fișiere (3 %) la tokenizer; examenul de cod ascuns rămâne bun.
- 1126 teste trec. Placa liberă.

## Urmează
- **S55 (C-45)**, doar procesor, până la ~10 ore: tokenizerul Kronos-Cod (32.768 simboluri, pre-înregistrat, măsurat pe 1 % ținut deoparte), tokenizarea setului, apoi propunerea primei antrenări pe placă.
- **S56**, după S55: măsurare scurtă pe placă (câteva minute) — varianta pe placă a reglajului CCM pentru #477.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe` (C-46):** `integrare/kronos/MODEL.md` cu #477 — suma, mărimea, cele 3 texte de control (2 identice cu #459; „Capitala României este” → „ orașul Bacău,”), marjele minime 0,026 / 0,024 / 0,016 (mai mici decât la #459: un motor cu abateri ~0,015 pe logit-uri poate da alt text; cu ~1e-3, nu). Secțiunea „Rezerva: #459” păstrează suma veche.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice): reper pentru viteza din OS.
- Bancul CCM rece/cald: pe Windows, 1 fir e cel mai rapid pe procesor la răspunsuri repetate — de măsurat la fel în OS.
- Căutare în text pe procesor (modulul `cautare`), verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-46, simbolurile #477 pe stick identice cu cele 3 texte din `MODEL.md`, și viteza pe 1 fir (simb/s), lângă Windows (~28 simb/s pe 1 fir) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **Release-ul privat `kronos-kgr1-477`** (executantul n-are voie la `gh`). Pe workstation, în PowerShell, din `C:\Kronos\cyberspace`:
  `gh release create kronos-kgr1-477 lucru/export/kronos_477_q8_0.kgr lucru/export/kronos_477_q8_0.kgr.sha256 --repo Adriancu91/cyberspace --title "Kronos #477 KGR1 Q8_0" --notes "SHA-256 bcbe8187087dbb3e531a8a7b10991cd24ea14a6e067d07c0fcbb8d3edd753963, 110859040 octeți"`
- Opțional: excluderea mai îngustă propusă la S53 (doar suprapunerile cu enunțuri/soluții); fără „da”, se exclud toate cele 3.821 fișiere.
- Cauza repornirii de la 29 oct ~23:10 (probabil pană de curent): comanda de citire din raportul S52 sau „da” pentru citirea jurnalelor Windows de către executant.
- Prima antrenare Kronos-Cod pe placă: după S55, prin granițele cascadei sau cu „da”-ul lui Adrian.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
