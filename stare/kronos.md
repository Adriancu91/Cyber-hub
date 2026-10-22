# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-22 05:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- **S15 (examen mare, 80 de întrebări):** #415 a învățat toate tipurile de întrebări văzute la antrenare (30/30 pe texte noi),
  dar la tipuri nevăzute are 6/50 — cât modelul vechi. Concluzia: se învață ce se vede, nu se transferă.
- **Direcție nouă (decizia lui Adrian, 22 oct 01:42):** fără LLM nicăieri (nici ca profesor, nici ca judecător); „de top” pe
  domenii cu verificator (documente în română, cod cu teste, gramatică); metoda: auto-joc cu verificator + specialiști + memorie.
  Nu mai facem nopți de antrenare cu rețeta veche.
- **S16 gata:** verificatorul nostru fără niciun model dă aceeași notă ca Qwen la 527/540 răspunsuri (97,6 %) → Qwen nu mai e judecător.
- Teste: 868 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- **S17 (E1, aprobat, noaptea 22→23, de la 19:00):** „întrebări născute de Kronos” — își scrie singur întrebări noi, le
  verifică fără niciun model străin și se antrenează 3 ore pe ele. Verdict după praguri scrise dinainte, mâine dimineață.
- Ziua de 22 oct: doar pregătirea S17 pe procesor; placa liberă.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea, 17 teste;
  97,6 % acord cu un judecător LLM) — util oricui vrea să noteze automat răspunsuri scurte.
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul.
