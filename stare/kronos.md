# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-24 14:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **Pauză la antrenări (C-156, Adrian, 21 nov 08:01), în vigoare:** nicio antrenare pe workstation, nimic de-al Kronos pe placa video. **S131** „în așteptare (pauză)”, pregătirile păstrate. Chat-ul merge pe 8787 cu **#651**. 1.563 teste trec (raportul de dimineață 24 nov).
- **Nou (după decizia lui Adrian din `DECIZII.md`, 24 nov 14:15, și nota centrului 14:20 la C-162): S134 „bancul de antrenare #513”** în coada Kronos:
  - **A — aprobată, doar procesor:** `unelte/banc_antrenare.py` — pașii #513 exact ca OS-ul (din greutățile #513, date reale ale liniei, loturi trase ca `DateBucati.lot` cu sămânța 1134, AdamW la fiecare lot cu parametrii liniei #513, tăiere 1,0, rata constantă), F32 sau bf16 (autocast); scrie pierderea, norma gradientului, ms/pas, simb/s, memoria plăcii, pozițiile loturilor. Niciun model salvat. Proba pe procesor + fișa `BANC_ANTRENARE.md`.
  - **B — placa, ~10–20 min (4 variante: 2×512 / 12×512 × F32 / bf16, câte 20 de pași): așteaptă „da”-ul lui Adrian** (pauza C-156 spune „nimic pe placă, la nicio oră”). Rulează doar când `in-lucru/` nu arată placa ocupată de OS/GPU.
- Propunerea de la 11:15 (oracolul #513 pe procesor) e **retrasă**: Cyber-GPU a făcut oracolul (placa = oracolul în pașii 1–9), iar bancul dă și pierderea pe aceleași loturi.

## Urmează
- S134 A (executantul, la următoarea trecere); apoi fișa `integrare/kronos/BANC_ANTRENARE.md` copiată aici, cu rețeta și tabelul gol.
- S134 B doar după „da”; tabelul completat cu cele 4 variante Windows/PyTorch.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe` / `cyber-gpu` (C-161/C-160, bancul cinstit):** rețeta exactă a pașilor PyTorch (date, sămânță, pozițiile loturilor în `loturi.i64`, AdamW, precizie), ca OS-ul să tragă aceleași loturi (`antrenare date … --lot`, P6-153) și să compare ms/pas, simb/s și pierderea pas cu pas.
- `integrare/kronos/FISA_ANTRENARE.md` — viteza din jurnal: #513 ~39.300 simb/s (12 × 512, adunare 8, bf16), #651 ~15.500 simb/s.
- `integrare/kronos/PAS_DE_AUR.md` + `pas_de_aur_mic/` + `pas_de_aur_513/reteta.json` — pasul de aur (SGD și AdamW, toleranțe).
- `integrare/kronos/MODEL.md` (#513, implicit) și `MODEL_651.md` (#651, SHA `2edf75ac…0bf2`).

## De ce are nevoie de la ceilalți
- De la `cyber-universe` / centru: dacă tabelul comun are alte coloane sau alt număr de pași, o notă în `integrare/kronos/BANC_ANTRENARE.md` (Kronos se aliniază). Sămânța propusă: 1134.
- Cererea os-363 (reperul bpb #513 Q8_0) rămâne văzută; intră în coadă doar cu „da”-ul lui Adrian.

## Blocaje / nevoie de Adrian
- **„da bancul Kronos pe placă (S134 B)”** — ca bancul să aibă și cifrele din Windows (minute, nimic salvat); fără el rămâne doar partea pe procesor.
- **Conectarea lui Claude Code pe workstation expiră între 29 nov și 2 dec:** `claude auth login` (sau `claude setup-token`) la workstation; altfel executantul și raportul de dimineață se opresc.
- La workstation: `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`.
- Reluarea antrenărilor Kronos (S131 sau altele) — doar cu o decizie nouă a lui Adrian.
