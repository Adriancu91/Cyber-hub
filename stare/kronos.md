# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-03 20:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **Kronos-Cod:** două nopți (S58, S63) → 0,5004 biți/octet, pass@10 ~2 % (3/163). **Diagnosticul S64 (gata, NECLAR):** cu 200 de încercări
  pe cele 20 de probleme de probă rezolvă doar 2 (pass@100 = 1,25/20; AJUTĂ cerea ≥ 4, NU AJUTĂ ≤ 1). ~6 % din răspunsuri nu se compilează,
  ~92 % rulează dar dau rezultat greșit: a învățat forma codului, nu logica. Placa max 1.468 MB / 49 °C.
- **S65–S68 (numărarea funcțiilor din codul descărcat, doar procesor):** 319.430 funcții cu explicație care trec cutia; „autonome” 83.349
  (3,55 mil. simboluri de corp); **S68 (gata, PUȚIN):** chemabile ca la examen doar 12.648 (0,77 mil.), 78 % sunt metode. Scurgere 0. 1190 teste trec.
- **Direcția aleasă de Adrian (C-60, C-62):** A exercițiile → B o noapte pe ele → D memoria de cod → C școala de cod → E Kronos își alege datele; modelul mai mare nu acum.

## Urmează
- **S69 (gata, verificat):** 313.910 exerciții „antet + explicație → corp”, amestec 970,8 mil. simboluri cu 25,0 % exerciții; 5.516 ținute deoparte; scurgeri scoase; 1195 teste trec.
- **S70 (rulează din 3 nov 19:09, 8 ore pe placă):** continuare din `gpt.pt` pe o copie (linia `cod_c1_ex`), examen pe `ascuns2` ca la S63 (3/163). AJUTĂ ≥ 8/163, NU AJUTĂ ≤ 4/163.
  Pre-înregistrarea urcată și verificată; placa 5.918 MB / 58 °C. **C-63:** totul terminat sau oprit curat până la **06:45**; 07:00–~09:30 placa și calculatorul libere pentru Adrian.
- **S71 (aprobat, 4 nov după ~09:30):** memoria de cod („rege / regat”) + măsurare pe setul de probă. S72 (școala) și S73 (alegerea datelor) după S70.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper pe Windows: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice).
- Un tokenizer pentru cod (Python/Rust/C), care păstrează indentarea ca simboluri întregi.
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**
  sau să nu pornească dacă rulează o antrenare (DECIZII 1 nov 19:45, „nu în nopțile de antrenare”). Important de la noaptea 3→4 nov (S70 pe placă de la 19:00).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Fără grabă: dacă cifrele S58 contează (abaterea de memorie la examen); permisiunea `taskkill` pe workstation; ora limită 18:30 la bucla automată.
- Release-ul privat `kronos-kgr1-477`: doar copie pe GitHub, fără grabă — comanda în `integrare/kronos/MODEL.md`.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
