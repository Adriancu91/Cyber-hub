# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-24 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **Pauză la antrenări (C-156, Adrian, 21 nov 08:01), în vigoare:** nicio antrenare pe workstation, nimic de-al Kronos pe placa video. S131 „în așteptare”. Chat-ul merge pe 8787 cu **#651**. **1.569 teste trec.**
- **S134 A — GATA (24 nov 14:48, verificat):** `unelte/banc_antrenare.py` face pașii #513 exact ca OS-ul (greutățile #513, textul liniei, loturi `DateBucati.lot` cu sămânța **1134**, AdamW **lr 5e-5** la fiecare lot, tăiere 1,0, F32 sau bf16 autocast) și scrie pierderea, norma, ms/pas, simb/s, memoria și pozițiile loturilor. Proba pe procesor (2 × 512): F32 1.618 ms/pas, bf16 4.860 ms/pas (procesorul n-are bf16 nativ); bf16 vs F32 la pasul 1: 0,002 %. Pierderea la pasul 1 = **1,068** (ferestre TinyStories; medie pe 32 de ferestre 1,66) — nu e greșeală.
- **Fișa e aici:** `integrare/kronos/BANC_ANTRENARE.md` (rețeta, comenzile, tabelul cu cele 4 variante, gol până la partea B).

## Urmează
- **S134 B (placa, ~15 min, 4 variante × 20 de pași, nimic salvat) — doar după „da”-ul lui Adrian** și doar când `in-lucru/` nu arată placa ocupată. Apoi tabelul completat.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe` / `cyber-gpu` (bancul cinstit):** rețeta exactă din `BANC_ANTRENARE.md`; pozițiile loturilor (`loturi.i64`) se pot da la cerere. Atenție: oracolul os-395 a folosit lr 1e-3; pentru pierderea comparabilă pas cu pas, OS-ul trebuie să folosească **lr 5e-5**, același lot, aceeași sămânță și **doar textul** (fără conversație/hrană).
- `integrare/kronos/FISA_ANTRENARE.md` (viteza din jurnal: #513 ~39.300 simb/s, 12 × 512, adunare 8, bf16), `PAS_DE_AUR.md`, `MODEL.md` (#513), `MODEL_651.md` (#651).
- Răspunsuri Kronos în „Discuție” la `idei/2026-11-24-centru-viteza-peste-windows.md` și `idei/2026-11-24-centru-antrenarea-in-trepte.md`.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: rândul `banc antrenare:` (P6-187) cu aceleași coloane ca tabelul din fișă — dacă diferă ceva, o notă în `BANC_ANTRENARE.md`, Kronos se aliniază.

## Blocaje / nevoie de Adrian
- **„da bancul Kronos pe placă (S134 B)”** — altfel bancul are doar cifrele OS-ului și proba pe procesor.
- **Conectarea lui Claude Code pe workstation expiră între 29 nov și 2 dec:** `claude auth login` (sau `claude setup-token`) la workstation.
- La workstation: `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`.
- „Da”/„nu” la propunerile centrului (pistele B/C, antrenarea în trepte): laboratorul Kronos ar cere antrenări scurte pe placă, deci ridicarea pauzei C-156 doar pentru ele.
- Reluarea antrenărilor Kronos (S131 sau altele) — doar cu o decizie nouă a lui Adrian.
