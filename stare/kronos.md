# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-21 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu, română + cod + engleză simplă), antrenat de la zero pe
  workstation-ul RTX 3070 Ti, în „cascadă”: executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- **Noaptea 11 s-a terminat fără erori → modelul #407: PARȚIAL, fără regresie** (verificat de supraveghetor după praguri).
  Răspunde din textul primit și la întrebări puse altfel (11/15, față de 7 la #401), la da/nu (13/15, față de 0) și refuză
  pe nedrept de două ori mai rar; dar la **tipuri noi** de întrebări tot 2/15 (pragul: 5). N-a uitat româna, codul, poveștile.
- Efect nou de urmărit: uneori răspunde „Da.”/„Nu.” la întrebări care nu sunt da/nu (3 din 45).
- Fila „Întreabă din text” din interfață (portul 8787) folosește încă #401; trecerea la #407 așteaptă „da”-ul lui Adrian.
- Motorul de română (Romanian Language Core) e în `main`; bun ca analizor, nu ca filtru de date.

## Urmează
- Azi ziua: S10 (același examen pe modelele de la ora 1 și 2, ~10 min pe placă); S11 (date noi cu **tipuri noi** de
  întrebări — râuri, specii, deputați —, altele decât cele din examen); S9 (unealta de pornire `--din-nou`);
  S8 (`module.toml` pentru modulele Kronos, după `standarde/modul-v0.md`).
- La noapte (21→22): noaptea 12, 3 ore din #407 pe datele S11, doar dacă supraveghetorul verifică perechile la 17:15.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Mai târziu: „răspuns din text” — întrebi despre un document, primești răspunsul din el (local, fără internet).
  Acum: bun pe întrebări obișnuite (nume, ani, locuri, populație, da/nu), încă slab pe tipuri de întrebări nevăzute.
- Modelul de lucru „nucleu + porturi + contracte + teste de contract” și regulile de pre-înregistrare a experimentelor.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață — modulul „memorie + calcul” din planul Kronos. Nimic acum.
- De la `cyber-universe`: nimic acum; formatul comun de modul e aprobat și îl aplicăm (S8, azi).

## Blocaje / nevoie de Adrian
- Un „da”/„nu” la S13: fila „Întreabă din text” să folosească #407 în loc de #401 (recomandarea: da). Nu e urgent.
