# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-22 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- **S15 (examen mare, 80 de întrebări):** #415 a învățat toate tipurile de întrebări văzute la antrenare (30/30 pe texte noi),
  dar la tipuri nevăzute are 6/50 — cât modelul vechi. Concluzia: se învață ce se vede, nu se transferă.
- **Direcție nouă (decizia lui Adrian, 22 oct 01:42):** fără LLM nicăieri (nici ca profesor, nici ca judecător); „de top” pe
  domenii cu verificator (documente în română, cod cu teste, gramatică); metoda: auto-joc cu verificator + specialiști + memorie.
  Nu mai facem nopți de antrenare cu rețeta veche.
- Teste: 851 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- **S16 (E0, procesor, fără placă):** un verificator scris de noi care notează răspunsurile fără Qwen, comparat cu notele lui
  Qwen pe examenele deja făcute (S15 și S4). Pragul: acord ≥ 90 %.
- **S17 (E1, o noapte pe placă, țintă 22→23 oct):** „întrebări născute de Kronos” — își scrie singur întrebări noi, le
  verifică fără niciun model străin și se antrenează pe ele. Pornește doar dacă S16 trece de 90 %.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- În curând: un verificator simplu „răspunsul se potrivește cu bucata din text?” (Python, fără model, fără rețea) — util oricui
  vrea să noteze automat răspunsuri scurte.
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul.
