# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-10 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S95 (gata 10 nov 02:13, verificat): LA FEL.** Modelul de 24 de straturi, 5 ore din #536 cu rata 5e-6: română curat **1,2040**
  (cel mai bun scor de până acum) vs #513 1,2060 — sub pragul MAI BUN (≤ 1,2010); nimic stricat (R1 instrucțiuni 99,20). Câștigul vine tot din răcire.
  Placa liberă de la 02:13 (max 6.496 MB / 62 °C) pentru testul `os-276` de la 07:15.
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #513** (KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #477 și #459 rezerve. Release `kronos-kgr1-513` nefăcut (luni, Adrian).
- **S89 (gata 8 nov 01:30): modelul de 24 de straturi (183M) a mers 5 ore fără să cadă** (leacul de memorie din S87 ține: vârf 6.465 MB, 62 °C).
  Verdict **LA FEL** cu #513: română curat 1,2063 vs 1,2060; nimic stricat (R1 instrucțiuni 99,20). A văzut doar 237 M simboluri față de 707 M la #513.
- **S96 (C-85 pasul 5, gata 9 nov 14:40, verificat): DA.** Datele de antrenare pe bucăți (27 × 50 M simboluri) dau exact același șir
  (SHA-256 identic pe 1,34 mld simboluri), cu 125 MB RAM în loc de 3 GB. Pornirea liniei ia 41,7 GB RAM din cauza textului brut citit pentru amprentă.
- **S93 (C-88, gata 02:36):** examenul de română decide de acum pe linia nouă `w2_mare_24r`; paznicul îi păzește amprenta, `kronos/` neschimbat.
- **S88 (C-86): oprit** — ștergerea celor 82 de modele intermediare (33,4 GB) așteaptă mâna lui Adrian.
- **S94 (C-85 pasul 4, gata 9 nov 01:05, verificat): NU.** Modelul mic de 6 straturi a clasat rețetele ×4 < ×2 < bază ≈ încălzire ×2 < ×0,5;
  pe modelul de 24 (câte 1 oră) ordinea a ieșit inversă: ×0,5 1,2102 < bază ≈ încălzire ×2 1,2118 < ×2 1,2158 < ×4 1,2232 (ρ = −0,92).
  Lecție: rata nu se alege pe un model mic tăiat; la modelul bun, rata mică strică cel mai puțin. Vârf 6.426 MB / 61 °C. **1337 teste trec, 0 pică.**

## Urmează
- **C-98 (preluat 17:15):** Adrian e la workstation din 16:36 (test `os-277`) — nimic pe placă. **S99 (placa) pornește cel mai devreme la 19:30**
  (sau la nota că Adrian a terminat), doar cu workstation-ul în Windows: rețeta Muon pe modelul de 24, 5 ore din #554, judecată pe română
  (praguri scrise dinainte); **placa liberă până la 07:00** mâine. Un test neanunțat al lui Adrian o poate întrerupe — e în regulă.
- **S98 (procesor, 11 nov de la 08:00, după S99):** legarea datelor pe bucăți în antrenare printr-un modul nou, neactivat; proba: aceleași 1.000 de loturi.
- **C-89 (tokenizer românesc): PARCAT** de Adrian până la >1 miliard de parametri.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 rămân pornibile.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- Nota automată pentru răspunsuri în română (fără alt AI) + setul ascuns de 500; acum și ca modul de examen `examen_romana` (amprente pe set).
- Unealta `unelte/date_bucati.py` (date pre-tokenizate pe bucăți, citite prin mmap, cu SHA pe fiecare bucată).
- Unealta `unelte/puncte_salvare.py` (listă + ștergere cu probă implicită, jurnal SHA înainte de ștergere).
- Lecții: rata mică ține ce știa un model crescut (confirmat de S94: un model mic tăiat dă ordinea inversă a ratelor); Muon câștigă ~0,65 GB la 183M; **memoria plăcii se poate aduna de la o oră la alta
  din cicluri de obiecte Python — `gc.collect()` înainte de `empty_cache()` o eliberează.**

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm oprirea scriptului la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- `claude setup-token` pe workstation dacă n-a fost reînnoit (autentificarea expira în jur de 9 nov; executantul a mers normal azi-noapte).
- **S97 / C-92: stick-urile pentru `os-276` NU sunt pregătite de Kronos** — după C-93 le pregătește centrul de comandă / Adrian (lista din `stare/cyber-universe.md`).
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) + `lucru/memorie_mare` (10,5 GB) — Adrian rulează comanda din raportul S88 sau dă executantului o excepție pentru ștergeri aprobate.
- Release-ul `kronos-kgr1-513` — luni 9 nov, cu Adrian la workstation.
- Când Adrian termină testul `os-277`: o notă aici (C-98); fără notă, S99 pornește de la 19:30 (placa liberă la 07:00). Dacă vrea placa toată seara, s-o scrie.
- Opțional: arhiva de mutare (26,2 GB) + Coșul. Fără grabă: S58, `taskkill`, ora 18:30 la bucla automată, Release-ul `kronos-kgr1-477`.
