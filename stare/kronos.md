# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-28 08:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung (27 oct): Kronos dedicat pe cod și autodezvoltare.
- **Workstation-ul a revenit** (tăcerea de azi-noapte = internetul căzut ~01:00–06:01; antrenarea n-a fost afectată).
- **S38 CONFIRMAT:** modelul nou **#459** e cel mai bun pe română (1,2162 față de 1,2332 la #441; mai mic = mai bine), cod și povești tot mai bune.
- **C-24 gata (cu o limită):** în `integrare/kronos/` sunt acum specificația KGR1 **cu descrierea completă a tokenizerului**, vectorii de test
  (`vectori/mic_f32.kgr`, `mic_q8_0.kgr`, `vectori.json`, toleranța declarată în `README.md`) și `MODEL.md` (#459, Q8_0, 110.859.040 octeți,
  SHA-256 `e80618b4…382e`, 3 texte cu primele 5 simboluri greedy). **Limita:** Release-ul privat cu fișierul nu e făcut încă (cere aprobarea lui Adrian).
- Pe placă azi: **S42** — „cititorul” E3 refăcut din #459 cu rețeta A (pragurile scrise înainte). Pe procesor: **S41** (Kronos-Cod, etapa 1a).

## Urmează
- Verdictul S42 (CONFIRMAT dacă răspunde corect la ≥ 5 întrebări mai mult din 100 decât cititorul de azi, #438, fără să piardă în altă parte).
- S41: lista surselor de cod cu licențe, examenul de cod scris înainte, cutia izolată (fără descărcări).
- Porturile `cautare` și `inferenta` în nucleu: partea din `kronos/` (S40a) cu Adrian de față, apoi modulele (S40b).

## Ce oferă proiectul celorlalți
- **Pachetul KGR1 complet** în `integrare/kronos/` (specificație, tokenizer, vectori, testul pe hardware din `MODEL.md`) — pentru C-25 / P6-27b în `cyber-universe`.
- Motorul de referință `unelte/inferenta_bruta.py` (în cyberspace); Q8_0 de 111 MB nu pierde practic nimic.
- `verifica_text(text)` din motorul de română; verificatorul „răspunsul se potrivește cu referința?”; căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF).

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: rezultatul motorului Rust pe vectorii de test (logit-uri față de toleranță, greedy) și, după Release, pe #459 (simbolurile din `MODEL.md`, viteza).
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **Release-ul #459:** o comandă `gh release create …` pe workstation (exactă în `plan/pentru_adrian.md` din cyberspace); fără ea, fișierul .kgr nu ajunge la OS.
- **S40a:** o sesiune Claude Code cu Adrian de față pe workstation („Fă S40a din plan/coada.md”) — executantul n-are voie în `kronos/`.
- Opțional: „da” ca executantul să poată face singur Release-uri.
