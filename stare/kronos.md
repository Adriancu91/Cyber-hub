# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-27 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud, prin `plan/coada.md`). Direcția (Adrian, 22 oct): fără LLM nicăieri;
  auto-joc cu verificator + specialiști + memorie; notarea o face verificatorul nostru (S16).
- **S31 (C-21.2) rulează pe placă:** AdamW contra Muon, câte 2 h din #415, aceeași sămânță, adunare pe 8 loturi, răcire 25 %; pre-înregistrare
  urcată înainte; sfârșit ~05:50. Prag: Muon ≤ AdamW − 0,010 val_bpb română, fără regresie > 0,005 în rest.
- **S29 (C-21.1, memoria mai bună) gata: CONFIRMAT.** Rădăcini românești + RRF + reordonarea cu modelul nostru (#438): răspunsul în primele 3
  bucăți la **83/100** față de 72 (prag +5), k = 20 95 față de 94. Pe validare câștigul fusese +1,2 → efectul real e probabil mai mic;
  aproape tot vine din reordonare (log p(întrebare | bucată)), la definiții.
- **S30 gata:** Muon scris de noi ca modul nou (MANIFEST + teste de contract), implicit pașii vechi bit cu bit; proba 5.917 MB.
- Închise: S27 (E3 cu antrenare) CONFIRMAT la limită (60/100 fără text dat); E1 NECLAR; E2 INFIRMAT.

## Urmează
- **S33** (ziua de 27 oct, < 1 h pe placă): E3 citește cu căutarea nouă — #438 răspunde din bucățile reordonate (azi 60/100; prag +5).
- **S32** (C-21.3, doar procesor, ~2 zile): formatul propriu de greutăți (fp32 + Q8_0) + motor de referință fără PyTorch.

## Ce oferă proiectul celorlalți
- `verifica_text(text)` din motorul de română (acord, „al/a/ai/ale”, numerale, diacritice; Python, fără rețea).
- Verificator „răspunsul se potrivește cu referința?” (`unelte/verificator_text.py`: fără model, fără rețea).
- Căutare în text pe procesor (SQLite FTS5 + BM25 + rădăcini românești + RRF, `unelte/e3_memorie.py`, `unelte/e3_reordonare.py`);
  cu reordonarea de model (~0,14 s/întrebare pe placă, ~1 GB).
- Muon (Newton-Schulz, scris de noi) ca modul cu teste — rezultatul comparației după S31.
- Lecție E2: un specialist pe o singură familie uită repede restul.

## De ce are nevoie de la ceilalți
- De la `suita-office` (după ce e gata și testată de oameni): motorul de **calcul** și **citirea documentelor**. Nimic acum.
- De la `cyber-universe` și `cyber-gpu`: nimic acum. Placa workstation-ului: S31 până ~05:50, S33 (< 1 h) ziua de 27 oct; apoi S32 e doar
  procesor, deci placa e liberă pentru fereastra OS/GPU (~30 min, cu Adrian, prin centrul de comandă).
- Pentru K6-CPU („Kronos bare-metal v0.2”): S32 va da contractul fișierului de greutăți pentru motorul Rust din OS.

## Blocaje / nevoie de Adrian
- Nimic urgent. Mici întrebări: ora raportului de dimineață (06:40 sau 07:40), închiderea S28 (oprirea workstation-ului) și, fără grabă,
  un port nou `cautare` în `kronos/` (propus de S29; schimbările în `kronos/` doar cu „da”-ul lui Adrian).
