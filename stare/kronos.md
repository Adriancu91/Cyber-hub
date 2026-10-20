# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-20 16:00 · **de:** supraveghetorul Kronos

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu, română + cod + engleză simplă), antrenat de la zero pe
  workstation-ul RTX 3070 Ti, în „cascadă”: executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Pe examen neutru (texte apărute după 12 oct.), Kronos bate GPT-2 small și GPT-Neo românesc 125M la română și cod.
- Nou (20 oct.): modelul #401 răspunde la întrebări **din textul primit** (50/50 pe tiparele învățate), dar la
  întrebări formulate altfel doar parțial (7/15; tipuri noi 3/15). Fila „Întreabă din text” e în interfața de pe 8787.
- Motorul de română (Romanian Language Core) e în `main`; bun ca analizor, dar încă nu ca filtru de date (multe alarme
  false la nume proprii străine).

## Urmează
- Noaptea 11 (20→21 oct.): aceleași întrebări în 5–6 formulări + da/nu, ca #401 să înțeleagă întrebarea, nu tiparul.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Mai târziu: „răspuns din text” — întrebi despre un document, primești răspunsul din el (local, fără internet).
- Modelul de lucru „nucleu + porturi + contracte + teste de contract” și regulile de pre-înregistrare a experimentelor.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): un motor de **calcul** (formulele Excel) și **citirea
  documentelor** (PDF/Word → text), apelabile din Python fără interfață. Sunt exact modulul „memorie + calcul” din planul Kronos.
- De la `cyber-universe`: formatul comun de modul (vezi `idei/2026-10-20-format-comun-module.md`).

## Blocaje / nevoie de Adrian
- Nimic blocat. Decizia lui Adrian la propunerea „format comun pentru module”.
