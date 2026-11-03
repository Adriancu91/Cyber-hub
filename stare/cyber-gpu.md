# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-03 12:55 (ora României) · **de:** sesiunea Cyber-GPU 40 (cloud, fără placă) — **C-58 gata** (OPRIT ridicat: a venit rezultatul de pe placă și o comandă nouă)

## Acum
- **Pe placa reală (3 nov, os-214):** primul I6 — FWSEC a rulat, ucode încărcat prin DMA, Bus Master pus la loc; rezultat „NU TRECE” la
  verificare: „la 0x1fa824: asteptat 0x1ffe00, citit 0x1ffe00”. Începutul zonei protejate (WPR2) era **exact** cel cerut; diferea capătul (HI),
  dar mesajul numea registrul greșit.
- **C-58 gata, doar în SIMULARE** (`af02bea` + docs `3286a3b`, 335 teste, CI verde):
  - eroarea numește acum registrul care diferă: LO `0x1fa824` (început) sau HI `0x1fa828` (capăt), cu valorile așteptat/citit;
  - capătul e acceptat dacă e sfârșitul exclusiv **sau** ultima pagină de 4 KiB a zonei. Sursele publice (RM 570.144 MIT, nova-core) verifică
    după FWSEC doar începutul; pe placă capătul nu era sfârșitul exclusiv → cel mai probabil „ultima pagină”. **De confirmat** cu HI brut din
    `raport/gpu-jurnal-002.txt` (pe stick-ul de test);
  - `gpu-sim` scrie HI ca pe placă (ultima pagină; opțiunea `wpr2_hi_last_page`); `i6_log::wpr2_after_i6` verifică LO/HI direct din jurnalul de pe stick.
- Pe placă până acum: I0–I4 doar citire TREC; I6 a scris (2 în configurație + 720 în registrele GSP), toate în ferestrele permise.
- Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `3286a3b`).

## Urmează
1. Sesiunea OS: fixarea cyber-gpu ≥ `af02bea` (propunerea `idei/2026-11-03_cyber-gpu-fixare-c58.md`; doar adăugări, codul OS nu trebuie schimbat).
2. **Fereastra următoare, cu Adrian:** întâi copiază `raport/gpu-jurnal-002.txt` de pe stick-ul de test în `rezultate/` → noi confirmăm HI
   (`wpr2_after_i6`) → apoi I6 din nou, cu pornire rece (cablul scos 30 s), pașii din `cyber-gpu/docs/FEREASTRA_C-49.md`.
3. Dacă I6 trece: I7 (Booter) rămâne blocat în plan până la o comandă separată.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului
  (`aee06c4`): **doar adăugări** — în sesiunea 30/30b: `nvidia_ga104::{fuse, i6_check, i6_log}`, `fwsec::read_ucode_and_signature`,
  `gpu_pci::bus_master`, `gpu_core::diag::Journal::with_sink`; în sesiunea 33 (C-54): `nvidia_ga104::{read_tour, chain, board_compare}`,
  `gpu_sim::observed` (lista completă în `docs/IMPLEMENTATION_STATUS.md`). C-58 (3 nov): `gsp::falcon::{compare_frts, check_frts_detail, FrtsCheck, Wpr2End}`, `i6_log::wpr2_after_i6`, `FakeGsp::wpr2_hi_last_page` — doar adăugări; `check_frts` păstrat (nota: `integration/cyber-universe/C-58_wpr2-capat.md`). Schița pentru `gpu tur`/`gpu lant`: `integration/cyber-universe/C-54_gpu-tur-si-lant.md`. Codul OS existent nu
  trebuie schimbat. Schița pentru comenzile noi: `integration/cyber-universe/C-49_gpu-pregatire-i6.md`.
- Pentru `gpu i6 --scrie`, OS-ul va trebui să dea: o zonă de RAM contiguă sub 4 GiB (~60 KiB), fereastra BAR0 de 16 MiB (cu scriere doar
  pentru comanda asta) și accesul la configurația PCI a plăcii.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: mutarea fixării (după „da”) și un Release nou pentru stick-ul de test.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- La fereastra următoare: copierea fișierului `raport/gpu-jurnal-002.txt` de pe stick-ul de test (736 rânduri) în hub `rezultate/`.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
