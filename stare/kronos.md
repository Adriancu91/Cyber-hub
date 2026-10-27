# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-27 11:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S33 gata: CONFIRMAT la limită.** #438 răspunde corect la 66/100 cu bucățile reordonate (`rrf_reord`) față de 60/100 cu căutarea veche,
  în aceeași rulare (prag +5). Câștigul vine din definiții („Ce este X?”); pe celelalte tipuri e zero sau ușor negativ.
- **S34 rulează** (din 09:00): proba de control — #415 + 2 h cu rețeta veche, ca să știm dacă rețeta A (1,2332 față de 1,2858) câștigă prin rețetă sau prin ore.
- S31 (Muon) INFIRMAT — Muon se închide. S29 (memoria: rădăcini + RRF + reordonare) CONFIRMAT: 83/100 în primele 3 bucăți față de 72. 950 teste trec.

## Urmează
- **S34** (azi, verdict pe la prânz): rețeta A se păstrează dacă e mai bună cu ≥ 0,010 față de proba de control.
- **S35** (azi, < 1 h pe placă): aceeași citire pe eșantionul de validare nevăzut de #438 — ține +6 și pe alt amestec de întrebări?
- **S32** (C-21.3, doar procesor, ~2 zile): formatul propriu de greutăți (fp32 + Q8_0) + motor de referință fără PyTorch.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română (acord, „al/a/ai/ale”, numerale, diacritice; Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: fără model, fără rețea).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF), cu reordonare de model (~0,14 s/întrebare pe placă, ~1 GB).
- Lecții: E2 — un specialist pe o singură familie uită repede restul; S31 — trecerea la Muon pe un model deja antrenat cu AdamW dă un „șoc” care nu se reface în 2 h.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor**. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului azi: S34 (până pe la prânz), apoi S35 (< 1 h); apoi S32 e doar procesor,
  deci placa e liberă pentru fereastra OS/GPU (~30 min, cu Adrian, prin centrul de comandă; o sarcină de placă nu pornește cât e anunțată fereastra).
- Pentru K6-CPU („Kronos bare-metal v0.2”): S32 va da contractul fișierului de greutăți pentru motorul Rust din OS.

## Blocaje / nevoie de Adrian
- Nimic urgent. Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului), un port nou `cautare`
  în `kronos/` (propus de S29; doar cu „da”-ul lui Adrian) și, după S34, dacă vrea o continuare cu rețeta A.
