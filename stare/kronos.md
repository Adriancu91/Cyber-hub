# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-23 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Direcția (decizia lui Adrian, 22 oct): fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie; notarea o face
  verificatorul nostru (S16: 97,6 % acord cu vechiul judecător LLM).
- **E1 („întrebări născute de Kronos”) s-a încheiat fără verdict clar:** S17 = NECLAR (tipuri nevăzute 6/50 → **13/50**;
  confirmat cerea ≥ 16, infirmat ≤ 9). S18 (repetarea cu 3× întrebări) n-a trecut poarta: doar 918 întrebări din 1.032 cerute,
  fiindcă articolele de Wikipedia pe care le avem s-au terminat → nu s-a antrenat (regula scrisă dinainte).
- Teste: 893 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- **S19 acum (~1 oră, doar examen):** cât din creșterea 6 → 13 vine din tipurile atinse direct de întrebările născute.
- Apoi Adrian alege: E2 (specialiști + ruter), o antrenare pe cele 918 întrebări existente, sau altă metodă/sursă.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, încă slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe`: nimic acum. Pentru experimentele lor de nivel 0 pe workstation (C-11, decizia din 22 oct 23:10):
  placa Kronos are doar S19 (~1 oră) până la decizia lui Adrian; o fereastră se stabilește doar cu Adrian, între două sarcini Kronos.
- Pentru propunerea „Kronos bare-metal v0.2” (K6-CPU), dacă Adrian o aprobă: unealta de export al greutăților și examenele în JSON
  le putem da din `cyberspace/unelte/` (poziția noastră e în `idei/`).

## Blocaje / nevoie de Adrian
- **Adrian alege pasul următor după E1** (variantele 1/2/3 în `cyberspace/plan/pentru_adrian.md`, sarcina S20): E2, antrenare pe
  cele 918 întrebări, sau altă metodă/articole noi (descărcarea cere „da”-ul lui).
