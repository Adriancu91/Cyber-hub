# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-21 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu, română + cod + engleză simplă), antrenat de la zero pe
  workstation-ul RTX 3070 Ti, în „cascadă”: executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Cel mai bun model „răspuns din text”: **#407** (noaptea 11, PARȚIAL, fără regresie): formulări noi 11/15, da/nu 13/15,
  tipuri noi de întrebări doar 2/15.
- Azi dimineață: examenul pe modelele de la ora 1 și 2 arată că greșeala „Da./Nu.” la întrebări care nu sunt da/nu
  scade cu orele (10 → 6 → 3), iar tipurile noi stau pe loc (2 → 1 → 2) — trebuie alte tipuri în date, nu mai multe ore.
- **Formatul comun de modul aplicat:** 24 de fișiere `module/manifeste/<nume>.toml` după `standarde/modul-v0.md`, ținute
  la zi din `MANIFEST` de o unealtă, cu test. Unealta de pornire a sarcinilor se descurcă acum singură la repornire.
- **Noaptea 12 (azi): INFIRMAT, fără regresie.** 3.319 întrebări de tipuri noi la antrenare n-au ajutat la tipurile
  nevăzute (tot 2 din 15). Dar modelul nou (#415) a făcut 50/50 pe examenul „răspuns din text” (cel mai bun până acum)
  și n-a uitat nimic. Fila „Întreabă din text” din interfață rămâne pe #407.
- Raportul de dimineață își actualizează singur instrucțiunea înainte să ruleze (`git pull`).
- Teste: 851 trec, 1 sărit.

## Urmează
- S15 (noaptea asta sau mâine dimineață, doar examen): 50 de întrebări de tipuri nevăzute în loc de 15, plus 30 din
  tipurile antrenate pe texte noi, pe #401, #407, #415 — ca să vedem dacă „2 din 15” e chiar zero.
- Mâine: pasul următor pentru întrebările nevăzute, ales după S15.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Mai târziu: „răspuns din text” — întrebi despre un document, primești răspunsul din el (local, fără internet).
  Acum: bun pe întrebări obișnuite (nume, ani, locuri, populație, da/nu), încă slab pe tipuri de întrebări nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`), pentru o viitoare mutare ca modul în Cyber Universe.
- Modelul de lucru „nucleu + porturi + contracte + teste de contract” și regulile de pre-înregistrare a experimentelor.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață — modulul „memorie + calcul” din planul Kronos. Nimic acum.
- De la `cyber-universe`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul.
