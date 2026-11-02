# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-02 11:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- CCM pentru #477: procesor 1 fir 2,14 s/răspuns; **placa fp32 acceptată, 1,226 s (1,75× mai rapid)**, |Δ logit| 0,000155; placa 1,5 GB (S56).
- **Kronos-Cod (C-45 gata):** tokenizerul de cod (32.768 simboluri) BUN — 3,46 octeți/simbol (+22 % față de w2), refacere 100 % identică;
  setul de antrenare tokenizat: 1,08 mld simboluri; validare 5.686 fișiere ținute deoparte; examenul ascuns neatins.
- **S57/S59/S60/S61 gata:** datele de cod, modelul care citește simbolurile, examenul pe ore, proba de la zero, comanda pass@k; încorporările pornite mici (S61: AJUTĂ). 1168 teste trec.
- **S58 terminat (prima antrenare pe cod, 10 ore, `cod_c1_init002`): NECLAR** — validarea întreagă **0,514 biți/octet** (Rust 0,438, Python 0,555, C 0,622; prag ≤ 1,10 ✓), setul ascuns **pass@10 = 3/200** (prag ≥ 10 ✗). Știe forma codului, rezolvă rar.
  Antrenarea în limite (6.205 MB, 64 °C); **la examenul ascuns placa a trecut de 7.000 MB (~17 min)** → S58 `oprit` până decide Adrian.

## Urmează
- **S62 gata (2 nov 09:04):** uneltele de examen de cod se opresc singure peste 6.500 MB; vârf 1.924 / 4.416 MB (S58: 7.971); validarea 0,5141 = S58; 1174 teste trec.
- **S63 (aprobată de Adrian, C-56):** a doua antrenare pe `cod_c1` (10 ore, din modelul S58). Oprită 09:32 înainte de pornire (un set ascuns nou de 200
  fără repetări din S58 nu încape); supraveghetorul a ales setul fără suprapunere (~163 de probleme, praguri pe procente) → din nou `aprobat`.
  Ordinea: setul + teste (procesor), pre-înregistrarea, apoi 10 ore pe placă + examene → placa ocupată până pe la ~22:00–23:00.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper de viteză pe Windows pentru #477: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice).
- Un tokenizer pentru cod (Python/Rust/C), care păstrează indentarea ca simboluri întregi — util dacă OS-ul va rula vreodată Kronos-Cod.
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: **primit (1 nov)** — #477 pe stick, `--control` TRECE (simbolurile identice), 123 simb/s fără ecran (os-210). Mulțumim; nimic altceva acum.
- De la `cyber-universe` (bucla automată, C-53): `bucla-automata.ps1 pregateste` acceptă acum 08–22, dar în nopțile de antrenare Kronos ține placa de la **19:00** (fereastra de noapte 19:00–07:00; ziua placa e liberă 08:00–18:30). Rugăm ca limita să fie **18:30**, sau ca scriptul să nu pornească dacă rulează o antrenare (ex. `nvidia-smi` arată un proces `python`) — cum cere DECIZII 1 nov 19:45 („nu în nopțile de antrenare”). De făcut înainte de prima tură cu Adrian (~3 nov).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **2 nov:** „da S63” primit (C-56); setul S63 ales de supraveghetor (fără suprapunere) — Adrian poate cere „S63 varianta b” (200, cu repetări) până la examene. Rămân: dacă cifrele S58 contează (abaterea de memorie la examen); opțional: permisiunea `taskkill` pe workstation (executantul n-a putut opri procesul care depășea limita).
- Release-ul privat `kronos-kgr1-477` nu mai blochează OS-ul (fișierul e pe stick); doar copie pe GitHub, fără grabă — comanda în `integrare/kronos/MODEL.md`.
- Bucla automată (DECIZII 1 nov 19:45): doar ziua; ora limită a scriptului (acum 22:00) de coborât la 18:30 la pregătirea cu Adrian (~3 nov). La ferestrele OS/GPU: antrenarea de pe placă oprită întâi.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
