# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-27 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S36 gata: NECLAR.** Rețeta A fără adunarea pe 8 loturi (proba D): 1,2520 pe română curat față de 1,2332 cu A întreagă → ambele părți ajută
  (răcirea singură păstrează ~67 % din câștig).
- **S37 gata: NU TRECE.** Motorul KGR1 fără PyTorch, cu LayerNorm/softmax în float64: dif. maximă F32 1,364e-4 (prag 1e-4); textul identic.
  Executantul propune un prag relativ — decizia e la Adrian. Q8_0 (111 MB) trecuse deja la S32. 961 teste trec.
- **S38 rulează** (noaptea 27→28): 6 ore cu rețeta A din #441 (aprobat 18:00 de centrul de comandă, prin delegare), pre-înregistrare urcată înainte;
  sfârșit estimat ~01:55.

- **C-24 preluată → S39 (doar procesor, aprobat):** acum un model KGR1 minuscul (greutăți aleatoare, ≤ 1 MB, F32 + Q8_0) + vectori de test
  (3 texte, logit-uri, greedy); după S38, exportul celui mai bun model în Q8_0 ca Release în repo-ul privat.

## Urmează
- Verdictul S38 la trecerea de 02:15 (CONFIRMAT dacă română curat ≤ 1,2232 fără regresie > 0,005 la cod și TinyStories).
- Ziua de 28 oct se decide după S38 (posibil proba E: fără adunare, cu rată mai mare).
- Pachetul `integrare/kronos/` (format KGR1 + vectori + `MODEL.md`) ajunge în hub la o trecere a supraveghetorului după S39.

## Ce oferă proiectul celorlalți
- **Nou:** contractul fișierului de greutăți KGR1 (`docs/format_greutati.md` din cyberspace: antet chei-valori, little-endian, aliniere 32,
  F32 și Q8_0 pe blocuri de 32 + tokenizerul în fișier) și motorul de referință `unelte/inferenta_bruta.py` (forward strat cu strat, testat față de
  PyTorch) — pentru K6-CPU în `cyber-universe` (motorul Rust ar compara cu el). Q8_0 de 111 MB nu pierde practic nimic.
- `verifica_text(text)` din motorul de română; verificatorul „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF), cu reordonare de model.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor**. Nimic acum.
- De la `cyber-universe`: după C-25, rezultatul motorului Rust pe vectorii de test (logit-uri și viteza). De la `cyber-gpu`: nimic acum. Placa workstation-ului e ocupată de S38 până pe la ~02:00; ziua de 28 oct nu e încă
  programată (fereastra OS/GPU cu Adrian se anunță prin centrul de comandă; o sarcină de placă nu pornește cât e anunțată fereastra).

## Blocaje / nevoie de Adrian
- Fără grabă: pragul pentru motorul fără PyTorch (F32) — păstrăm 1e-4 fix sau trecem la un prag relativ (propunerea din raportul S37)?
- Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului), un port nou `cautare` și unul `inferenta`
  în `kronos/` (doar cu „da”-ul lui Adrian).
