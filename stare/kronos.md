# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-27 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **27 nov, raportul de dimineață (verificat):** noaptea n-a rulat nimic la Kronos (nimic aprobat); 1.605 teste trec, placa liberă (458 MB, 30 °C), nimic oprit de paznic. Cele 14 reporniri ale workstation-ului din ultima zi vin toate de la testele OS de pe stick (os-456 … os-476).
- **S140 gata, verificat (procesor, placa neatinsă):** la cererea centrului (os-445) — #513 în PyTorch, 300 de pași pe aceleași loturi reale (sămânța 1134, lot 2 × 512, SHA `loturi.i64` identic), F32 față de bf16. **Valid.** Media pierderii pe pașii 251–300: bf16 1,66466 vs F32 1,66611 (**−0,087 %**, prag ±1 %) → **„bf16 nu strică învățarea pe 300 de pași”**.
- **Banda pentru OS** (|bf16 − F32| la pașii 1/10/50/100/200/300): **[2,4e-5; 3,8e-4; 9,4e-4; 1,4e-3; 1,6e-3; 2,7e-3]**. Cinstit: între acești pași diferența sare până la **5,1e-2** (pasul 291); 12 pași din 300 trec de 7,2e-3, toți după pasul 100; pașii 1–50 rămân sub 1,5e-3. O singură pereche de rulări. Tabelul întreg: `integrare/kronos/BANC_ANTRENARE.md`, secțiunea S140.
- Laboratorul (probele aprobate, toate închise): bucăți K = 4 PIERDE (S135), harta câștig strâmb (S137), portarul LA FEL (S139).
- Placa liberă la Kronos; 1.605 teste trec. Chat-ul merge pe 8787 cu **#651**. Pauza C-156 rămâne pentru orice altă antrenare.

## Urmează
- Nimic aprobat pentru placă. Propus (S138, doar cu „da”): **(0′) altă sămânță** — cât e zgomotul între două rulări identice; apoi (2) piesele ieftine, (3) + fără γ.
- Candidații din `idei/2026-11-24-centru-cele-patru-piese.md`: doar cu „da” separat.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe` / `cyber-gpu` (nou, S140):** banda de toleranță F32 vs mixt pe text real. Citire propusă: pasul mixt din OS față de F32-ul lui pe text real e „doar rotunjire” dacă stă sub banda de la pașii 1/10/50/100/200/300; abaterea de 7,2e-3 de la os-445 e de mărimea rotunjirii bf16 după pasul 100, dar nu la pașii 1–50. bf16 (8 biți mantisă) e mai grosier decât f16 (11), deci banda e generoasă pentru OS. Aceleași loturi se pot reface cu `unelte/banc_antrenare.py --samanta 1134 --lot 2 512`.
- Poziția pe calitate pentru piesele v2: `integrare/KRONOS_V2_FISA.md`.
- `integrare/kronos/BANC_ANTRENARE.md`, `FISA_ANTRENARE.md`, `PAS_DE_AUR.md`, `MODEL.md` (#513), `MODEL_651.md` (#651).

## De ce are nevoie de la ceilalți
- Nimic acum. Dacă vine „da (0′)”: ~1 h 40 min de placă liberă ziua (07:00–23:00), niciun test cât `laborator-ocupat.txt` scrie „OCUPAT”.
- `laborator-ocupat.txt` poate exista cu textul „LIBER” (executantul nu-l poate șterge) — „LIBER” = placa nu e a laboratorului.

## Blocaje / nevoie de Adrian
- Să șteargă de mână `C:\Kronos\cyber-test\laborator-ocupat.txt` (acum scrie „LIBER”).
- **Conectarea lui Claude Code pe workstation expiră între 29 nov și 2 dec (cel mai devreme peste 2 zile):** `claude auth login` la workstation — altfel se opresc executantul, supraveghetorul și raportul de dimineață.
- La workstation: `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`.
- Opțional, recomandat: „da (0′)”; „da probele v2 (S138)”; „da bancul Kronos pe placă (S134 B)”.
- Orice antrenare în afara laboratorului și antrenarea lungă a lui Kronos v2 în OS — doar cu „da” separat.
