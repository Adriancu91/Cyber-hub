# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-20 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu, română + cod + engleză simplă), antrenat de la zero pe
  workstation-ul RTX 3070 Ti, în „cascadă”: executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Pe examen neutru (texte apărute după 12 oct.), Kronos bate GPT-2 small și GPT-Neo românesc 125M la română și cod.
- Modelul #401 răspunde la întrebări **din textul primit** (50/50 pe tiparele învățate), dar la întrebări formulate altfel
  doar parțial (7/15; tipuri noi 3/15; da/nu 0/15). Fila „Întreabă din text” e în interfața de pe portul 8787.
- Datele pentru noaptea 11 sunt gata (24.149 de perechi: fiecare întrebare în 5–6 formulări + 3.585 da/nu), verificate.
- Noaptea 11 (20→21 oct.) **rulează** de la 20:46 (pornită de mână, după două încercări oprite la 19:29 și 20:33 — nimic
  stricat): linia nouă `w2_conv_text_v2`, din #401, aceleași praguri scrise dinainte. Placa: 6.225 MB, 55 °C, sub limite.
- Motorul de română (Romanian Language Core) e în `main`; bun ca analizor, dar nu ca filtru de date (3 greșeli adevărate din 50 semnalate).

## Urmează
- Noaptea 11: antrenarea se termină ~23:50, apoi examenele nopții 10 + examenul cu întrebări puse altfel; verdictul mâine, 08:15.
- S9 (mâine ziua, pe procesor): unealta de pornire primește `--din-nou`, ca o sarcină oprită să se poată reporni fără om.
- S8 (mâine ziua, pe procesor): `module.toml` pentru cele ~27 de module Kronos, după `standarde/modul-v0.md` (partea Kronos din
  propunerea aprobată), cu unealtă + test ca să nu se desincronizeze de `MANIFEST`.
- Școala de cod (nivel nou): după verdictul nopții 11.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Mai târziu: „răspuns din text” — întrebi despre un document, primești răspunsul din el (local, fără internet).
- Modelul de lucru „nucleu + porturi + contracte + teste de contract” și regulile de pre-înregistrare a experimentelor.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață — modulul „memorie + calcul” din planul Kronos. Nimic acum.
- De la `cyber-universe`: nimic acum; formatul comun de modul e aprobat și îl aplicăm (S8).

## Blocaje / nevoie de Adrian
- Niciunul. (Accesul supraveghetorului la hub: rezolvat, 20 oct 20:30.)
