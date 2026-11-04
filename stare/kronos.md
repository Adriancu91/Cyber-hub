# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-04 14:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie; pe termen lung Kronos dedicat pe cod.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **Kronos-Cod (linia `cod_c1`, model S63):** 0,5004 biți/octet, `ascuns2` 3/163. Încercat fără câștig: multe încercări (S64), o noapte pe exerciții (S70: 2/163),
  memoria de cod (S71: proba 0/20). S72a: 889 exerciții cu test care trec în cutie (P_verif 200 / P_scoala 689).
- **S74 (gata, 4 nov 12:11):** reperul S63 pe P_verif = **14/200** cu 10 încercări (13 fără un `return <valoare fixă>`); ≥ 10 → școala de cod poate porni. Placa max 2.032 MB. **1207 teste trec.**

## Urmează
- **S75 (aprobat, azi după-amiază, ~1,5 h):** S63 scrie 8 soluții la cele 689 de exerciții ale școlii, cutia le verifică → DESTULE (≥ 100 corecte diferite) sau PREA PUȚINE.
- **S72b (aprobat, noaptea 4→5 nov, de la 19:00):** dacă DESTULE, o trecere de învățare din soluțiile corecte, apoi examen pe P_verif + `ascuns2`.
  AJUTĂ = R ≥ 24/200 și validarea ≤ 0,505; NU AJUTĂ = R ≤ 17. Verdictul mâine dimineață.
- **C-64 (preluat):** dacă S72b nu e AJUTĂ → S76 răspunsuri în română (o noapte din #477 pe o copie), apoi S77 Kronos mai mare crescut din #477. Dacă AJUTĂ → runda 2 a școlii; S73 (alegerea datelor) după.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper pe Windows: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod (păstrează indentarea).
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.
- Pentru „super-școala de română” (DECIZII 4 nov 11:33): rețeta școlii de cod (generează → verifică → învață doar din ce e corect) se poate refolosi; rezultatul S72b arată dacă merită.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**
  sau să nu pornească dacă rulează o antrenare. Important în noaptea 4→5 nov (S72b) și azi după-amiază (S75 pe placă până cel târziu 18:30).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **URGENT până pe 6 nov:** autentificarea Claude Code de pe workstation expiră între 6 și 9 nov → executantul și raportul de dimineață s-ar opri.
  Adrian rulează pe workstation `claude setup-token` (sau `claude auth login`). Probabil privește și sarcinile programate ale altor proiecte de pe același calculator.
- La C-64 am socotit „nu ajută” orice verdict S72b în afară de AJUTĂ (inclusiv NECLAR) — Adrian poate spune altfel.
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill` pe workstation; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
