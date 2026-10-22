# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-22 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”:
  executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`.
- Direcția (decizia lui Adrian, 22 oct): fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie; notarea o face
  verificatorul nostru (S16: 97,6 % acord cu vechiul judecător LLM).
- **S17 (E1, „întrebări născute de Kronos”) gata, verdict NECLAR:** Kronos și-a scris singur ~30.000 de întrebări, au trecut
  verificările 516; după 3 ore de antrenare pe ele, la tipuri de întrebări nevăzute urcă de la 6/50 la **13/50**
  (confirmat cerea ≥ 16, infirmat ≤ 9). Fără regresie pe ce știa deja. Placa: max 6.274 MB, 64 °C.
- Teste: 886 trec, 1 sărit. Interfața „Întreabă din text” rămâne pe #407.

## Urmează
- **S18 pe placă, din noaptea asta (~7 ore):** repetarea cu 3× întrebări născute (≈1.550), aceleași praguri și același judecător.
  Ultima rundă: dacă e iar „neclar”, decide Adrian. Verdict la trecerea de 08:15.
- După S18: E2 (specialiști + ruter) sau, dacă E1 se confirmă, extinderea auto-jocului.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- „Răspuns din text” local: bun pe tipurile de întrebări învățate, încă slab pe cele nevăzute.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** (formulele) și **citirea documentelor**
  (PDF/Word → text), apelabile din Python fără interfață. Nimic acum.
- De la `cyber-universe`: nimic acum. Pentru experimentele lor de nivel 0 pe workstation (C-11, decizia din 22 oct 23:10):
  placa Kronos e ocupată cu S18 până dimineață; o fereastră se stabilește doar cu Adrian, între două sarcini Kronos.

## Blocaje / nevoie de Adrian
- Niciunul acum. Dacă S18 iese tot „neclar”, Adrian alege pasul următor (îi scriu variantele).
