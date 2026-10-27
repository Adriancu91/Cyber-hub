# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-27 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S34 gata: CONFIRMAT.** Rețeta A (AdamW + gradient adunat pe 8 loturi + răcire 25 %) câștigă prin rețetă, nu prin ore: aceleași 2 h cu rețeta
  veche dau 1,2903 pe română curat (nicio îmbunătățire față de #415, 1,2858), rețeta A 1,2332.
- **S35 gata: NECLAR.** Citirea cu bucățile reordonate pe 500 de întrebări de validare nevăzute: 336 față de 331 (+1 punct; pragul +2).
  Ajută la definiții (+18), strică la „rest” (−17).
- **S32 gata (C-21.3):** formatul propriu de greutăți **KGR1** + motor de referință în numpy, fără PyTorch. Q8_0 (111 MB): bpb +0,00002 → TRECE;
  F32 (392 MB): dif. maximă 1,34e-4 față de pragul 1e-4 → NU TRECE la limită (argmax și textul identice). **C-21 e închisă.** 960 teste trec.

## Urmează
- **S36** (rulează din ~15:05, sfârșit estimat ~17:15; pre-înregistrarea urcată înainte): proba D — rețeta A fără adunare pe loturi, ca să aflăm
  dacă răcirea singură aduce câștigul. Verdictul la trecerea de 20:15.
- **S37** (doar procesor): motorul KGR1 adună în float64 la LayerNorm/softmax; o remăsurare F32 cu același prag 1e-4.
- **S38** (o noapte cu rețeta A, din #441): propus, așteaptă „da”-ul lui Adrian.

## Ce oferă proiectul celorlalți
- **Nou:** contractul fișierului de greutăți KGR1 (`docs/format_greutati.md` din cyberspace: antet chei-valori, little-endian, aliniere 32,
  F32 și Q8_0 pe blocuri de 32 + tokenizerul în fișier) și motorul de referință `unelte/inferenta_bruta.py` (forward strat cu strat, testat față de
  PyTorch) — pentru K6-CPU în `cyber-universe` (motorul Rust ar compara cu el). Q8_0 de 111 MB nu pierde practic nimic.
- `verifica_text(text)` din motorul de română; verificatorul „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF), cu reordonare de model.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor**. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului: S36 până pe la ~17:30; apoi liberă (S37 e doar procesor), deci
  bună pentru fereastra OS/GPU (~30 min, cu Adrian, prin centrul de comandă; o sarcină de placă nu pornește cât e anunțată fereastra).

## Blocaje / nevoie de Adrian
- O decizie: vrea o noapte de antrenare cu rețeta A, din #441 (S38)? Fără „da”, placa stă liberă la noapte.
- Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului), un port nou `cautare` și unul `inferenta`
  în `kronos/` (doar cu „da”-ul lui Adrian).
