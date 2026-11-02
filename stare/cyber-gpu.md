# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-02 13:27 (ora României) · **de:** sesiunea Cyber-GPU 36 (cloud, fără placă) — **OPRIT: necesită analiza lui Adrian** (3 sesiuni la rând fără pas, regula de oprire de siguranță)

## Acum
- **OPRIT** (2 nov 13:27): sesiunile 33b, 34, 35 și 36 n-au avut niciun pas — nimic de făcut fără placă. Codul e neschimbat de la `4e6f747`; CI verde (rularea 87). Sesiunile următoare doar verifică hub-ul și se opresc până apare o comandă nouă sau un raport de pe placă.
- **Pe placa reală, doar citire, 0 scrieri:** I0/I1 identitatea, I2 GFW_BOOT (28 oct), I3 + I3b VBIOS și FWSEC (29 oct), **I4 fișierele
  firmware 570.144: TRECE** (1 nov). Următorul pas pe placă e prima scriere (fereastra cu Adrian, `cyber-gpu/docs/FEREASTRA_C-49.md`).
- **C-54 gata, doar în SIMULARE** (332 teste, CI verde la rularea 80):
  - `gpu-sim` are acum **modelul plăcii reale** (`gpu_sim::observed`), din rapoartele de pe workstation: Command, Resizable BAR, BOOT_0/42,
    GFW, așezarea VBIOS (4 imagini, BIT, FWSEC). Modelul vechi greșea 4 lucruri (BOOT_0, Bus Master, unde începe a doua imagine VBIOS, `ucode_id`).
    Fără conținut VBIOS sau firmware NVIDIA în repo.
  - **Turul de citire** pentru bucla automată (`read_tour`): doar citiri deja făcute în siguranță pe placă + 3 registre de pregătire I6;
    rezultatul e respins dacă apare vreo scriere. Temperatura nu intră încă (nu are sursă NVIDIA MIT pentru Ampere).
  - **`compara_raport`**: pune raportul de pe stick lângă simulare. Pe cele 3 rapoarte reale: **33 la fel, 0 diferit**.
  - **Pașii în lanț** (`chain`): pregătire → Bus Master → I6 → I7 → Bus Master oprit → tur; oprire la primul eșec, placa pusă la loc,
    niciun pas care scrie în modul automat, I7 nu se încearcă (nu e gata).
- Propunere pentru OS: `idei/2026-11-01_cyber-gpu-tur-si-lant.md` (`gpu tur` pe lista albă a buclei; `gpu lant` doar cu „DA”).
- Commit-uri până la `4e6f747` pe `g0-g2-fundatie`. Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `4e6f747`).

## Urmează
0. **Sesiunea OS a terminat C-52, C-53 și C-55** (Release `os-214`, fixat pe `4e6f747`): `gpu pregatire-i6`, `gpu i6 --scrie`, bucla automată,
   `gpu tur`, `gpu lant` — testate doar în QEMU/simulare. Din partea noastră nu mai e nimic de făcut fără placă.
1. După prima tură automată (`gpu tur`) sau după fereastră: raportul/jurnalul în `rezultate/` → noi rulăm `compara_raport` și verificăm
   jurnalul cu `i6_log`; orice „DIFERIT” → reparăm modelul.
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
  `gpu_pci::bus_master`, `gpu_core::diag::Journal::with_sink`; în sesiunea 33 (C-54): `nvidia_ga104::{read_tour, chain, board_compare}`,
  `gpu_sim::observed` (lista completă în `docs/IMPLEMENTATION_STATUS.md`). Schița pentru `gpu tur`/`gpu lant`: `integration/cyber-universe/C-54_gpu-tur-si-lant.md`. Codul OS existent nu
  trebuie schimbat. Schița pentru comenzile noi: `integration/cyber-universe/C-49_gpu-pregatire-i6.md`.
- Pentru `gpu i6 --scrie`, OS-ul va trebui să dea: o zonă de RAM contiguă sub 4 GiB (~60 KiB), fereastra BAR0 de 16 MiB (cu scriere doar
  pentru comanda asta) și accesul la configurația PCI a plăcii.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: nimic nou (C-52/C-53/C-55 gata, `os-214`).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **OPRIT** după regula de oprire de siguranță: deblocarea = fereastra I6 cu Adrian, un raport `gpu tur` în `rezultate/` sau o comandă nouă în `COMENZI.md`.
- Fereastra cu prima scriere — OS-ul e gata (`os-214`); Adrian de față (pașii în `stare/cyber-universe.md` și `FEREASTRA_C-49.md`).
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
