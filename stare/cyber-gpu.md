# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-01 19:30 (ora României) · **de:** sesiunea Cyber-GPU 32 (cloud, fără placă) — fără lucru nou; C-52 (OS) preluat de sesiunea OS

## Acum
- **Pe placa reală, doar citire, 0 scrieri:** I0/I1 identitatea, I2 GFW_BOOT (28 oct), I3 + I3b VBIOS și FWSEC (29 oct), **I4 fișierele
  firmware 570.144: TRECE** (1 nov). Toate verificările de citire sunt dovedite. Următorul pas e prima scriere.
- **Decizia din 1 nov 12:00:** pe placa reală rulează doar Cyber Universe; proba tinygrad s-a anulat. Planul (C-49 + C-51) e acum doar cu
  driverul nostru, din OS: `cyber-gpu/docs/FEREASTRA_C-49.md`.
- Gata în cod, **doar în SIMULARE** (315 teste trec, CI verde):
  - siguranța „ucode version” → ce semnătură FWSEC acceptă placa (registrul `0x8241E0`, aflat din sursele NVIDIA MIT);
  - verificarea I6 doar citire (semnătura, VRAM, zona protejată WPR2, regiunea FRTS);
  - Bus Master pornit/oprit cu **o scriere, recitită** (valoarea veche pusă la loc dacă recitirea nu se potrivește);
  - FWSEC copiat neatins din VBIOS în RAM;
  - un test care fixează **exact cele 18 registre** pe care le scrie I6;
  - jurnalul fiecărei citiri/scrieri trimis OS-ului **pe loc** (ca să rămână pe stick și dacă placa se blochează), plus verificatorul care
    citește jurnalul de pe stick după fereastră și spune unde s-a abătut, dacă s-a abătut.
- Commit-uri până la `8c76084` pe `g0-g2-fundatie` (codul neschimbat de la `d879742`). Copia pentru sesiunea OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `8c76084`).
- Propunerea din `idei/` a devenit comanda **C-52** (OS), preluată de sesiunea OS (P6-40). Pentru noi nu e nimic nou de făcut fără placă.

## Urmează
1. **Sesiunea OS, C-52 (în lucru):** `gpu pregatire-i6` (doar citire), jurnalul pe loc, apoi `gpu i6 --scrie` (doar în stick-ul de test,
   cu confirmare „DA”) + Release nou. Dacă sesiunea OS ne cere ceva, are prioritate.
2. **Fereastra pe workstation, cu Adrian** — pașii (detalii în `FEREASTRA_C-49.md`):
   1. oprire completă înainte (cablul scos 30 s);
   2. `gpu pregatire-i6` — doar citire: semnătura 0/1/2, VRAM 8192 MiB, „WPR2 coborat”, „0 scrieri”;
   3. ⚠️ Bus Master pornit — 1 scriere, recitită;
   4. ⚠️ I6 FWSEC-FRTS — 18 registre, toate în fereastra GSP; dovada: falcon oprit fără cod de eroare și zona protejată exact unde am cerut;
   5. ⚠️ Bus Master oprit la loc — 1 scriere, recitită;
   6. oprire completă → Windows: `nvidia-smi` vede placa, Kronos pornește.
   - **Nu se poate strica:** VBIOS-ul (nicio cale de scriere spre el), siguranțele (doar citite); totul se șterge la oprirea completă.
   - Fără Booter/GSP/lansări (I7+) în fereastra asta.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului
  (`aee06c4`): **doar adăugări** — în sesiunea 30/30b: `nvidia_ga104::{fuse, i6_check, i6_log}`, `fwsec::read_ucode_and_signature`,
  `gpu_pci::bus_master`, `gpu_core::diag::Journal::with_sink` (lista completă în `docs/IMPLEMENTATION_STATUS.md`). Codul OS existent nu
  trebuie schimbat. Schița pentru comenzile noi: `integration/cyber-universe/C-49_gpu-pregatire-i6.md`.
- Pentru `gpu i6 --scrie`, OS-ul va trebui să dea: o zonă de RAM contiguă sub 4 GiB (~60 KiB), fereastra BAR0 de 16 MiB (cu scriere doar
  pentru comanda asta) și accesul la configurația PCI a plăcii.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: C-52 terminat (Release cu `gpu pregatire-i6` + `gpu i6 --scrie`).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- Fereastra cu prima scriere — după ce OS-ul termină C-52; Adrian de față (pașii în `stare/cyber-universe.md` și `FEREASTRA_C-49.md`).
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
