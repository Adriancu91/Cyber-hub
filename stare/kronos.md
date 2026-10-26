# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-26 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S27 (E3 cu antrenare) gata: CONFIRMAT, la limită.** Index + model nou (#438) răspund corect la **60/100** întrebări noi fără text dat
  (prag ≥ 60), fără regresie cu text dat (69/70, 39/60). #415 fără antrenare face 57 → câștigul vine mai ales din căutare. 928 teste trec.
- Închise: E1 NECLAR (tipuri nevăzute 6/50 → 13/50); E2 (3 specialiști + ruter) INFIRMAT (137/210 sub #415 = 144).
- **Memoria (E3), pe procesor:** index propriu SQLite FTS5/BM25 peste Wikipedia ro (277.357 articole), fără model, ~30 ms pe întrebare.
  **S26 (examen nou, 100 de întrebări neatinse, o singură măsurare):** răspunsul în primele 5 bucăți la **80 %**, în primele 3 la **72 %**
  (plafonul pentru E3 cu model). Cifrele vechi de pe 160 de întrebări (86,9 %) erau umflate.

## Urmează
- **S29 (C-21.1, memoria mai bună):** pașii 0–3 gata pe validare (rădăcini românești + RRF + reordonare cu #438: k = 3 78,2 % față de 77,0 %).
  Setul nou nu se mai putea alege (S27 a folosit aproape toate întrebările) → examenul decisiv = cele 100 S26, prag C-21 neschimbat (+5 puncte la k = 3).
  Sub o oră pe placă, în noaptea asta. Așteptat: INFIRMAT (+~1 punct).
- Apoi, în ordine: S30–S31 Muon + răcire lungă (AdamW contra Muon, câte 2 h; prag −0,010 val_bpb română), S32 motorul de inferență fără PyTorch.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- Căutare în text fără model, pe procesor (SQLite FTS5 + BM25, `unelte/e3_memorie.py`): pe română, răspunsul în primele 5 la ~80–85 % pe întrebări noi.
- Lecție E2: un specialist antrenat pe o singură familie uită repede restul; ruterul trebuie să fie aproape perfect ca să merite.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor** (PDF/Word → text). Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului: S29 (sub o oră) în noaptea 26→27, apoi S30–S31 (~6 h); fereastra
  OS/GPU (~30 min, cu Adrian, mâine/poimâine) se alege între două sarcini, prin centrul de comandă.
- Pentru K6-CPU („Kronos bare-metal v0.2”): S32 (C-21) va scrie formatul propriu de greutăți (fp32 + Q8_0) și un motor de referință
  fără PyTorch — contractul pentru motorul Rust din OS (după S29–S31).

## Blocaje / nevoie de Adrian
- Nimic urgent. Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului) și, fără grabă,
  un port nou `cautare` în `kronos/` (propus de S29; schimbările în `kronos/` doar cu „da”-ul lui Adrian).
