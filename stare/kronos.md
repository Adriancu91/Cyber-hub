# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-28 05:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie. Pe termen lung (27 oct): Kronos dedicat pe cod și autodezvoltare.
- **Workstation-ul Kronos tace din 27 oct 19:34.** S38 (6 ore cu rețeta A din #441) trebuia să se termine ~01:55; la 05:15 nu are raport.
  Adrian e anunțat să verifice calculatorul. Până atunci nimic nu rulează la Kronos (nici S39–S41 pe procesor).
- **C-24 → S39** (doar procesor, aprobat; pornește când revine executantul): model KGR1 minuscul + vectori de test + **descrierea tokenizerului**
  în specificație (cererea OS pentru P6-27b, adăugată 28 oct 05:15); exportul Q8_0 ca Release privat după S38.
  **Specificația KGR1 e deja în hub:** `integrare/kronos/format_greutati.md` (copiată azi 02:15, ca OS-ul să poată începe motorul).
- **Porturile `cautare` și `inferenta` în nucleu** (aprobate de Adrian, 27 oct 23:49) → **S40** (doar procesor): căutarea E3 și motorul KGR1 devin module înlocuibile.
- **C-28 (E4 Kronos-Cod) → S41, etapa 1a** (doar procesor, fără descărcări): lista surselor de cod cu licențe permisive, examenul de cod scris
  înainte (pass@1 / pass@10, set ascuns) și cutia izolată pentru codul generat. Linia română rămâne neatinsă.

## Urmează
- Când revine executantul: verdictul S38 (CONFIRMAT dacă română curat ≤ 1,2232 fără regresie > 0,005) sau `oprit` dacă s-a întrerupt; apoi placa pentru ziua de 28 oct.
- Pe procesor: S39 → S40 → S41. După S41: verificarea listei de surse, apoi etapa 1b (descărcare + tokenizer pe cod) și pragurile etapei 2.
- `integrare/kronos/vectori/`, descrierea tokenizerului și `MODEL.md` ajung în hub după S39 (întârziate cât tace workstation-ul).

## Ce oferă proiectul celorlalți
- **Contractul KGR1** (`integrare/kronos/format_greutati.md`) și, curând, vectorii de test — pentru motorul KGR1 din `cyber-universe` (C-25).
- Motorul de referință `unelte/inferenta_bruta.py` (în cyberspace); Q8_0 de 111 MB nu pierde practic nimic.
- `verifica_text(text)` din motorul de română; verificatorul „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF), cu reordonare de model — curând modul pe portul `cautare`.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după C-25, rezultatul motorului Rust pe vectorii de test (logit-uri și viteza).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.
- Fereastra OS/GPU pe workstation se anunță prin centrul de comandă; o sarcină de placă nu pornește cât e anunțată fereastra.

## Blocaje / nevoie de Adrian
- **Adrian:** să verifice workstation-ul (pornit, treaz, Claude Code executant deschis în `cyberspace`); fără el nu se mișcă nimic la Kronos.
