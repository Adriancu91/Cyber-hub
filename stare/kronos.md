# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-23 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Direcția (decizia lui Adrian, 22 oct): fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie; notarea o face
  verificatorul nostru (S16: 97,6 % acord cu vechiul judecător LLM).
- **E1 („întrebări născute de Kronos”) e NECLAR:** tipuri nevăzute 6/50 → 13/50. Analiza S19: creșterea nu vine din tipurile
  atinse direct (+7 pe restul), dar 7 din 13 răspunsuri bune sunt „lungi” (text copiat); cu nota strictă (F1 ≥ 0,8) 2/50 față de 4/50.
  Concluzie: auto-jocul a învățat modelul să copieze mai mult, nu clar să răspundă mai exact.
- **S21 (23 oct):** răspunsurile lungi apar doar pe tipurile nevăzute; pe restul examenelor, corecte fără cele lungi 117 (#415)
  față de 116 (#425) → „fără regresie” e real și cu nota strictă.
- Teste: 895 trec, 1 sărit. Placa e liberă. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- Nimic programat pe placă. Adrian alege pasul următor după E1 (S20): E2 (specialiști + ruter; recomandarea supraveghetorului), o antrenare pe cele 918 întrebări existente
  (cu poartă strictă), sau altă metodă/sursă.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
  Lecție utilă și altora: o potrivire îngăduitoare numără bune și răspunsurile lungi; măsurați și varianta strictă.
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, încă slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Ferestrele pe workstation (C-11, Cyber-GPU K0): placa Kronos e liberă
  până la decizia lui Adrian (S20); o fereastră se stabilește doar cu Adrian, cu Kronos oprit cât durează.
- Pentru „Kronos bare-metal v0.2” (K6-CPU) și operatorii de referință din `cyber-gpu`, dacă Adrian aprobă: unealta de export al
  greutăților (#415) și examenele în JSON le putem da din `cyberspace/unelte/`.

## Blocaje / nevoie de Adrian
- **Adrian alege pasul următor după E1** (variantele 1/2/3 în `cyberspace/plan/pentru_adrian.md`, sarcina S20).
- Dacă vrea fereastra Cyber-GPU pe workstation: acum e un moment bun (placa liberă); o spune în centrul de comandă.
