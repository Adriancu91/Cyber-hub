# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-27 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S31 (C-21.2) gata: INFIRMAT.** Muon (B) 1,3019 val_bpb română curat față de AdamW (A) 1,2332 (prag: B ≤ A − 0,010); B mai rău și la
  TinyStories R2, cod, fapte noi. Muon se închide. Surpriză: A (AdamW + adunare pe 8 loturi + răcire 25 %) a coborât de la 1,2858 (#415) la 1,2332,
  dar cu 2 ore de antrenare în plus — se verifică la S34.
- **S29 (C-21.1, memoria) CONFIRMAT:** rădăcini românești + RRF + reordonare cu modelul nostru: răspunsul în primele 3 bucăți 83/100 față de 72.
- Închise: S27 (E3 cu antrenare) CONFIRMAT la limită (60/100 fără text dat); E1 NECLAR; E2 INFIRMAT. 946 teste trec.

## Urmează
- **S33** (azi, < 1 h pe placă): #438 răspunde din bucățile reordonate (azi 60/100; prag +5).
- **S34** (azi, după S33, ~2,5 h pe placă): proba de control — #415 + 2 h cu rețeta veche; rețeta A se păstrează dacă e mai bună cu ≥ 0,010.
- **S32** (C-21.3, doar procesor, ~2 zile): formatul propriu de greutăți (fp32 + Q8_0) + motor de referință fără PyTorch.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română (acord, „al/a/ai/ale”, numerale, diacritice; Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: fără model, fără rețea).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF), cu reordonare de model (~0,14 s/întrebare pe placă, ~1 GB).
- Lecții: E2 — un specialist pe o singură familie uită repede restul; S31 — trecerea la Muon pe un model deja antrenat cu AdamW dă un „șoc” care nu se reface în 2 h.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor**. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului azi: S33 (< 1 h) apoi S34 (~2,5 h); apoi S32 e doar procesor,
  deci placa e liberă pentru fereastra OS/GPU (~30 min, cu Adrian, prin centrul de comandă; S34 nu pornește cât e anunțată fereastra).
- Pentru K6-CPU („Kronos bare-metal v0.2”): S32 va da contractul fișierului de greutăți pentru motorul Rust din OS.

## Blocaje / nevoie de Adrian
- Nimic urgent. Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului), un port nou `cautare`
  în `kronos/` (propus de S29; doar cu „da”-ul lui Adrian) și, după S34, dacă vrea o continuare cu rețeta A.
