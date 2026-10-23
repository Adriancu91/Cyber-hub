# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-23 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`. Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **E1 închis cu NECLAR** (Adrian, 23 oct 10:20): tipuri nevăzute 6/50 → 13/50, mai ales prin răspunsuri lungi.
- **E2 (3 specialiști + ruter, din #415) închis cu INFIRMAT** (S23, 11:00–17:31, fără erori): sistemul **137/210**, sub #415 monolit
  (**144**); chiar cu ruter perfect 142. Specialistul F1 98/165 (prag 100). Lecție: specialiștii uită repede tot ce nu e familia lor.
  Ruterul a ales corect 90,0 %. Validările (română, cod, povești, fapte noi) în praguri.
- **S24 (pregătirea E3, memoria, doar procesor) gata:** index propriu SQLite FTS5/BM25 peste Wikipedia ro (277.357 articole, 1,25 mil. bucăți,
  construit în 4 min). La 160 de întrebări de examen: bucata cu răspunsul în primele 1 / 5 / 20 la **64,4 / 80,6 / 92,5 %**, articolul corect
  în primele 5 la **84,4 %**; ~65 ms pe întrebare, fără model. Documente noi se adaugă în ~3 ms („învățate instant”).
- Teste: 904 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407. **Placa workstation-ului e liberă de la 17:31.**

## Urmează
- **S25 (doar procesor, ~2–3 ore):** căutare mai bună (numele proprii cântăresc mai mult, paginile-listă coborâte), ajustată doar pe validare
  (500 de întrebări vechi + 500 noi), apoi o singură rulare pe examene.
- E3 cu antrenare pe placă doar după „da”-ul lui Adrian, pe cifrele din S24/S25. Până atunci placa stă liberă.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- Lecție E2, utilă oricui împarte o problemă în „specialiști”: un specialist antrenat pe o singură familie uită repede restul,
  deci ruterul trebuie să fie aproape perfect și câștigul pe familie trebuie să fie mare ca să merite.
- Căutare în text fără model, pe procesor (SQLite FTS5 + BM25, `unelte/e3_memorie.py`), măsurată pe română: răspunsul în primele 5 la ~81 %.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor** (PDF/Word → text),
  apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Workstation-ul e **liber pe placă** (S24 folosește doar procesorul), deci fereastra
  OS/GPU de la întoarcerea lui Adrian (~30–60 min) se poate lua oricând.
- Pentru K6-CPU („Kronos bare-metal v0.2”), dacă Adrian aprobă: unealta de export al greutăților (#415) și examenele în JSON.

## Blocaje / nevoie de Adrian
- Nimic urgent. Când se întoarce Adrian: „da”/„nu” pentru E3 cu antrenare pe placă și pragul de căutare (propus: ≥ 80 % răspunsul în primele 5,
  ≥ 85 % articolul în primele 5; azi 80,6 % și 84,4 %).
