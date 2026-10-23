# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-24 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

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
- **S25 (căutarea mai bună, doar procesor) gata:** nume proprii obligatorii + pagini-listă coborâte. Pe 500 de întrebări noi: primele 5
  la **84,8 %** față de 84,6 % (+0,2 puncte → **nu e câștig real**, prag 3). Pe cele 160 de examene 86,9 % / articolul 90,6 %, dar umflat
  (ideile au venit din greșelile de acolo). Nu strică nimic, median 27 ms în loc de 45 ms.
- Teste: 907 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407. **Placa workstation-ului e liberă de la 23 oct 17:31.**

## Urmează
- **S26 (doar procesor, ~1 oră):** un examen E3 nou de 100 de întrebări neatinse, măsurat o singură dată (cifra curată), plus „primele 3 bucăți”.
- **S27 (E3 cu antrenare pe placă, ~4 ore): propus, doar după „da”-ul lui Adrian.** Până atunci placa stă liberă.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- Lecție E2, utilă oricui împarte o problemă în „specialiști”: un specialist antrenat pe o singură familie uită repede restul,
  deci ruterul trebuie să fie aproape perfect și câștigul pe familie trebuie să fie mare ca să merite.
- Căutare în text fără model, pe procesor (SQLite FTS5 + BM25, `unelte/e3_memorie.py`), măsurată pe română: răspunsul în primele 5 la ~85 % pe întrebări noi.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor** (PDF/Word → text),
  apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Workstation-ul e **liber pe placă** (S26 folosește doar procesorul), deci fereastra
  OS/GPU de la întoarcerea lui Adrian (~30–60 min) se poate lua oricând.
- Pentru K6-CPU („Kronos bare-metal v0.2”), dacă Adrian aprobă: unealta de export al greutăților (#415) și examenele în JSON.

## Blocaje / nevoie de Adrian
- Nimic urgent. Când se întoarce Adrian (după cifrele S26): „da”/„nu” pentru S27 (E3 cu antrenare pe placă) și pragul E3
  (propus: sistemul index + model ≥ 60 % corecte fără text dat).
