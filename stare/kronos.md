# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-04 11:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

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
- **S69 (gata):** 313.910 exerciții „antet + explicație → corp”. **S70 (gata, NU AJUTĂ):** 8 ore pe exerciții din S63 → `ascuns2` **2/163** (S63: 3/163),
  validarea 0,5074 (S63: 0,5004). Mergem din S63.
- **S71 (gata, 4 nov 10:34, NU AJUTĂ):** memoria de cod (2–4 funcții asemănătoare în față, index FTS5 pe 313.910 exerciții) → proba **0/20** cu memorie (fără: S63 0/20, S70 1/20);
  funcțiile găsite seamănă la nume, nu la soluție. Placa max 1.506 MB / 55 °C.
- **S72a (gata, 4 nov 11:13):** **889 exerciții cu test** care trec în cutie (și pică cu `return None`); P_verif 200 / P_scoala 689 (≥ 500). Scurgere 0. **1207 teste trec.**

## Urmează
- **S74 (aprobat, azi ziua, ~30 min pe placă):** reperul S63 pe P_verif (200 × 10) — aflăm înainte de noapte dacă școala are din ce învăța (B ≥ 10).
- **S72b (aprobat, noaptea 4→5 nov, de la 19:00):** prima rundă a școlii de cod din S63: 8 încercări pe exercițiu, cutia păstrează doar corpurile corecte (fără `return <valoare fixă>`),
  o trecere de învățare, apoi examen pe P_verif + `ascuns2`. AJUTĂ = cel puțin +10/200 față de S63 și validarea ≤ 0,505. S73 (alegerea datelor) după verdictul S72b.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper pe Windows: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice).
- Un tokenizer pentru cod (Python/Rust/C), care păstrează indentarea ca simboluri întregi.
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**
  sau să nu pornească dacă rulează o antrenare (DECIZII 1 nov 19:45, „nu în nopțile de antrenare”). Important și în noaptea 4→5 nov (S72b pe placă de la 19:00).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **URGENT până pe 6 nov:** autentificarea Claude Code de pe workstation expiră între 6 și 9 nov → executantul și raportul de dimineață s-ar opri. Adrian rulează pe workstation `claude setup-token` (sau `claude auth login`). Probabil privește și sarcinile programate ale altor proiecte de pe același calculator.
- Fără grabă: dacă cifrele S58 contează (abaterea de memorie la examen); permisiunea `taskkill` pe workstation; ora limită 18:30 la bucla automată.
- Release-ul privat `kronos-kgr1-477`: doar copie pe GitHub, fără grabă — comanda în `integrare/kronos/MODEL.md`.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
