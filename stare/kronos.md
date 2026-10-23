# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-23 11:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Direcția (decizia lui Adrian, 22 oct): fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie; notarea o face
  verificatorul nostru (S16).
- **E1 („întrebări născute de Kronos”) e închis cu NECLAR** (decizia lui Adrian, 23 oct 10:20): tipuri nevăzute 6/50 → 13/50, dar mai
  ales prin răspunsuri lungi (cu nota strictă, 2/50 față de 4/50). Fără regresie pe restul.
- **E2 aprobat de Adrian (23 oct 10:20):** 3 specialiști + ruter, antrenați pe rând din #415. Kronos lucrează și cât e Adrian plecat.
- **S22 (pregătirea E2) gata:** 3 familii (20.564 / 4.083 / 2.821 întrebări), ruterul pe primele cuvinte alege corect 189/210 = 90,0 %
  (condiția ≥ 90 % trece la limită), #415 = 144/210 pe aceleași întrebări. **S23 rulează pe placă de la ~11:05.**
- Teste: 900 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- **S23** (placa, ~7 ore, sfârșit estimat ~18:10, cel târziu ~19:05): cei 3 specialiști antrenați pe rând din #415, examenele și nota
  sistemului. Criterii: niciun specialist sub #415 pe familia lui (minus 1); sistemul ≥ 144/210; ruterul ≥ 90 % (îndeplinit).
- Verdictul E2 la trecerea de 20:15; apoi pregătirea E3 (index de memorie peste articolele deja descărcate) doar pe procesor.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
  Lecție utilă și altora: o potrivire îngăduitoare numără bune și răspunsurile lungi; măsurați și varianta strictă.
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, încă slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor** (PDF/Word → text),
  apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului e ocupată de E2 (S23, până pe la ~18:10); fereastra OS/GPU de la
  întoarcerea lui Adrian (~30–60 min) se ia între sarcini — executantul scrie în coadă când se termină sarcina curentă.
- Pentru K6-CPU („Kronos bare-metal v0.2”), dacă Adrian aprobă: unealta de export al greutăților (#415) și examenele în JSON.

## Blocaje / nevoie de Adrian
- Niciunul acum. E2 e aprobat întreg; nicio descărcare nouă, nimic în `kronos/`, examen sau paznic.
