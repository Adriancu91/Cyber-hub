# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-26 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **Pauza s-a încheiat** (Adrian, 26 oct 16:10). În pauză (24–26 oct) nu a rulat nimic; executantul a mers fără erori; 908 teste trec.
- Închise: E1 NECLAR (tipuri nevăzute 6/50 → 13/50); E2 (3 specialiști + ruter) INFIRMAT (137/210 sub #415 = 144).
- **Memoria (E3), pe procesor:** index propriu SQLite FTS5/BM25 peste Wikipedia ro (277.357 articole), fără model, ~30 ms pe întrebare.
  **S26 (examen nou, 100 de întrebări neatinse, o singură măsurare):** răspunsul în primele 5 bucăți la **80 %**, în primele 3 la **72 %**
  (plafonul pentru E3 cu model). Cifrele vechi de pe 160 de întrebări (86,9 %) erau umflate.

## Urmează
- **S27 rulează pe placă de la 16:52** (aprobat de Adrian 26 oct 16:10): E3 cu antrenare — din #415, 3 ore pe întrebări cu bucățile găsite
  de index (de obicei încap 2 bucăți în contextul de 512, nu 3); apoi examenul oficial pe cele 100 de întrebări S26, modelul primește doar
  întrebarea. Confirmat la ≥ 60 %, infirmat sub 45 %. Examenele se termină pe la ~20:45; verdictul îl verific la 23:15.
- **C-21 (studiul open-source) preluată:** după S27, în ordine: S29 memoria mai bună (rădăcini românești + RRF + reordonare cu modelul
  propriu; prag +5 puncte la k = 3 pe un set nou), S30–S31 Muon + răcire lungă (AdamW contra Muon, câte 2 h; prag −0,010 val_bpb română),
  S32 motorul de inferență fără PyTorch (fp32 + Q8_0, doar procesor). Fiecare cu pre-înregistrare.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română: acord, „al/a/ai/ale”, numerale cu „de”, diacritice (Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: Python, fără model, fără rețea).
- Căutare în text fără model, pe procesor (SQLite FTS5 + BM25, `unelte/e3_memorie.py`): pe română, răspunsul în primele 5 la ~80–85 % pe întrebări noi.
- Lecție E2: un specialist antrenat pe o singură familie uită repede restul; ruterul trebuie să fie aproape perfect ca să merite.
- Descrierile modulelor în formatul comun (`module/manifeste/`) și modelul „nucleu + porturi + contracte + pre-înregistrare”.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor** (PDF/Word → text). Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. **Placa workstation-ului e ocupată cu S27 până pe la ~20:45** (26 oct); fereastra
  OS/GPU (~30 min, cu Adrian, mâine/poimâine) se alege între două sarcini, prin centrul de comandă.
- Pentru K6-CPU („Kronos bare-metal v0.2”): S32 (C-21) va scrie formatul propriu de greutăți (fp32 + Q8_0) și un motor de referință
  fără PyTorch — contractul pentru motorul Rust din OS (după S27–S31).

## Blocaje / nevoie de Adrian
- Nimic urgent. Mici întrebări: ora raportului de dimineață (06:40 de la ora de iarnă, sau înapoi la 07:40?) și închiderea S28
  (oprirea workstation-ului, rămasă nefăcută — calculatorul e pornit, cum trebuie acum).
