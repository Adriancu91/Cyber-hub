# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-05 02:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie; pe termen lung Kronos dedicat pe cod.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **Kronos-Cod (linia `cod_c1`, model S63):** 0,5004 biți/octet, `ascuns2` 3/163. Încercat fără câștig: multe încercări (S64), o noapte pe exerciții (S70: 2/163),
  memoria de cod (S71: proba 0/20). S72a: 889 exerciții cu test care trec în cutie (P_verif 200 / P_scoala 689).
- **Școala de cod (S74 → S75 → S72b, 4 nov):** reper 14/200; 109 soluții corecte scrise de Kronos; după o trecere de învățare: 18/200, dar validarea de cod
  0,513 (> 0,510) → **STRICĂ**. Școala, așa cum e, nu avansează codul. **1212 teste trec.**
- **S76a gata (4 nov 20:50): GATA** — 23.251 exerciții „întrebare/instrucțiune → răspuns” în română, făcute prin reguli (50 % instrucțiuni, 8 feluri noi),
  500 ascunse, scurgeri 0, notă automată fără alt AI (corect / în temă / limbă curată, scorul R1). Reper #477: R1 63,73; felurile vechi 100, **instrucțiunile 37,47**. **1221 teste trec.**
- **Acum rulează (noaptea 4→5 nov, pornit ~23:30): S76b** — 5 ore din #477 pe o copie (`w2_romana_r1`), pe exercițiile S76a; pre-înregistrarea urcată înainte și verificată.
  AJUTĂ = R1 pe instrucțiuni ≥ 47,47 fără regresie. Sfârșit estimat ~05:45, oricum până la 06:45.

## Urmează
- Verdictul S76b (5 nov dimineața); #477 rămâne în uz până îl bate copia și Adrian spune „da”.
- **S77** — Kronos mai mare crescut din #477: întâi aceeași ieșire pe vectorii KGR1 + test de memorie/viteză pe placă (ziua de 5 nov), apoi nopți.
- S73 (alegerea datelor de către Kronos) rămâne în așteptare.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper pe Windows: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod (păstrează indentarea).
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.
- Pentru „super-școala de română” (DECIZII 4 nov 11:33): lecția S72b — învățarea din propriile soluții, repetate de 8 ori, strică ce știa modelul; de folosit cu mai puține repetări și mai multe date obișnuite.
- **Nota automată pentru răspunsuri în română** (`unelte/romana_raspunsuri.py noteaza`, deterministă, fără alt AI) + setul ascuns de 500 — utilă pentru orice test de răspuns în română.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**
  sau să nu pornească dacă rulează o antrenare (S76b rulează în noaptea 4→5 nov).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **URGENT până pe 6 nov:** autentificarea Claude Code de pe workstation expiră între 6 și 9 nov → executantul și raportul de dimineață s-ar opri.
  Adrian rulează pe workstation `claude setup-token` (sau `claude auth login`). Probabil privește și sarcinile programate ale altor proiecte de pe același calculator.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill` pe workstation; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
