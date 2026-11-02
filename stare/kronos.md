# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-02 23:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **Kronos-Cod, a doua antrenare (S63, C-56) gata: NECLAR** — 10 ore în plus pe `cod_c1`; validarea întreagă **0,5004 biți/octet** (S58: 0,5141;
  CONTINUĂ cerea ≤ 0,494), setul ascuns nou **pass@10 = 3/163** (1,8 %; CONTINUĂ ≥ 5, PLATOU ≤ 2). Placa max 6.013 MB / 63 °C; 1177 teste trec.
  Concluzia: învață forma codului, dar rezolvă tot ~2 % din probleme; o a treia noapte la fel ar aduce puțin.
- Uneltele de examen de cod se opresc singure peste 6.500 MB (S62); depășirea de la S58 nu s-a repetat.

## Urmează
- **S64 (aprobat de supraveghetor, ~1,5 ore pe placă, noaptea 2→3 nov):** 200 de încercări pe fiecare din cele 20 de probleme de probă,
  la două temperaturi → pass@k cu k mare + de ce pică corpurile. Praguri scrise înainte: AJUTĂ = pass@100 ≥ 4/20; NU AJUTĂ ≤ 1/20.
  Fără antrenare; seturile ascunse nu se redeschid.
- După S64: direcția pentru Kronos-Cod o alege Adrian (încercări multe + verificator / date cu funcții și teste / model mai mare).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper pe Windows: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice).
- Un tokenizer pentru cod (Python/Rust/C), care păstrează indentarea ca simboluri întregi.
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**
  sau să nu pornească dacă rulează o antrenare (DECIZII 1 nov 19:45, „nu în nopțile de antrenare”). De făcut înainte de prima tură cu Adrian (~3 nov).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Nimic urgent. După S64 (3 nov): alegerea direcției pentru Kronos-Cod (variantele noi cer „da”).
- Fără grabă: dacă cifrele S58 contează (abaterea de memorie la examen); permisiunea `taskkill` pe workstation; ora limită 18:30 la bucla automată (~3 nov).
- Release-ul privat `kronos-kgr1-477`: doar copie pe GitHub, fără grabă — comanda în `integrare/kronos/MODEL.md`.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
