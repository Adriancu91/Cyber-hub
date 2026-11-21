# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-21 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **Pauză la antrenări (C-156, Adrian, 21 nov 08:01), în vigoare:** nicio antrenare pe workstation și nimic pe placa video, la nicio oră. **S131 nu pornește** — „în așteptare (pauză)”, cu pregătirile păstrate (date `conversatie_chat6`, configurarea `w2_mare_24zcj`, pre-înregistrarea). Executantul a verificat: nimic din scripturile lui nu pornește S131 singur.
- **S132 „pasul de aur” gata** (21 nov 09:01, verificat de supraveghetor): 10 pași de antrenare PyTorch pe procesor, F32, repetabil; rețetele SGD și AdamW-ul liniei #513; modelul mic + fișa copiate în `integrare/kronos/`.
- **S133 „fișa de antrenare” gata** (C-162, 21 nov 17:36, verificată): `integrare/kronos/FISA_ANTRENARE.md`.
- Ultimul verdict de antrenare: S129 → rămâne #651. 1.563 teste trec. Chat-ul Kronos merge pe 8787 cu **#651**. Disc C: ~145 GB liberi.

## Urmează
- Nimic în coadă. Antrenările se reiau doar după o decizie nouă a lui Adrian (în OS-ul nostru, când motorul de antrenare e gata).
- La cerere: fișierele mari ale pasului de aur pentru #513 (2,74 GB), un pas de aur pentru #651 sau cu lot mai mare (tot pe procesor).

## Ce oferă proiectul celorlalți
- **PREDARE → cyber-gpu (C-160 p.7): `integrare/kronos/FISA_ANTRENARE.md`** — cifra de bătut: PyTorch pe RTX 3070 Ti, linia #513 ~39.300 simb/s (12 × 512, adunare 8, bf16), linia #651 ~15.500 simb/s (6 × 512, adunare 16, bf16 + recalculul activărilor); plus pasul adevărat (adunare, tăiere 1,0, AdamW cu scădere pe toți parametrii, încălzire, răcire după ceas, pierderea mascată), datele (int16 fără antet), punctul de control, examenul. Lipsesc din jurnale: viteza fără recalcul, timpul pe bucăți al pasului, F32 curat.
- **PREDARE → cyber-gpu (C-157 punctul 9c):** „pasul de aur” e în hub:
  - `integrare/kronos/PAS_DE_AUR.md` — fișa: fișierele, ordinea tensorilor, formulele SGD și AdamW pas cu pas (cu tăierea gradientului și corecția de bias), toleranțele măsurate (1 fir vs 16 fire);
  - `integrare/kronos/pas_de_aur_mic/` — modelul mic (arhitectura #513: 2 straturi, n_emb 64, 4 capete, vocabular 256, context 32), lot 2 × 32; greutățile de la început, gradientul pasului 1, greutățile după pasul 1 și 10, eroarea la fiecare pas; fișiere `.f32`/`.i32` little-endian fără antet, SHA-256 în `reteta.json`; 3,32 MB;
  - `integrare/kronos/pas_de_aur_513/reteta.json` — rețeta pentru #513 (fișierele de 2,74 GB pe workstation, `lucru/pas_de_aur/513/`).
  - Toleranțe recomandate: eroarea relativ ≤ 1e-5; gradientul ≤ 1e-5 absolut (‖Δ‖/‖g‖ ≤ 1e-3 pe tensor); greutăți SGD ≤ 1e-6, AdamW ≤ 1e-4. Nu „bit cu bit”: ordinea adunărilor schimbă ultimele cifre.
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL_651.md` — #651, 183 M parametri, `KRONOS\kronos_651_q8_0.kgr` (pe stick), SHA-256 `2edf75ac12eedb54bd2eace55d82bf5c14cc3240e11c0fca40263d3e65ea0bf2`. `MODEL.md` rămâne cu **#513**, implicit.
- **Pentru `cyber-gpu`:** cifrele lui #651 (C-157 punctul 4): 24 de straturi, 12 capete, n_emb 768, context 512, vocabular 16.384, 292 de tensori (98 Q8_0, 194 F32). Viteza PyTorch în Windows (C-153): #513 pe placă 129,12 simb/s, procesor 41,74.

## De ce are nevoie de la ceilalți
- Nimic. Pentru motorul de antrenare (C-160/C-161): Cyber-GPU spune dacă vrea un „pas de aur” cu lot mai mare (tot pe procesor). Cifrele lipsă din fișă se măsoară doar cu „da”-ul lui Adrian. Placa e a testelor OS/GPU zi și noapte.

## Blocaje / nevoie de Adrian
- Niciun blocaj. Reluarea antrenărilor (S131 sau #736 în chat) — doar cu o decizie nouă a lui Adrian.
- Opțional, la workstation: `schtasks /query /fo list | findstr /i "Kronos"` (să vadă el că nicio sarcină Windows nu pornește o antrenare) și `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`. Doar dacă vrea: „da CulturaX”.
