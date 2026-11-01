# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-01 12:20 (ora României) · **de:** sesiunea Cyber-GPU 30 (cloud, fără placă) — **OPRIT ridicat** (C-49)

## Acum
- **Pe placa reală, doar citire, 0 scrieri:** I0/I1 identitatea, I2 GFW_BOOT (28 oct), I3 + I3b VBIOS și FWSEC (29 oct), **I4 fișierele
  firmware 570.144: TRECE** (1 nov, 4/4 oficiale, antete 4/4). Toate verificările de citire sunt dovedite. Următorul pas e prima scriere.
- **C-49 gata:** planul ferestrei următoare (mai jos și în `cyber-gpu/docs/FEREASTRA_C-49.md`).
- Nou în cod (doar SIMULARE): **siguranța „ucode version”** — registrul care spune ce semnătură acceptă placa (era necunoscut; acum din
  sursele NVIDIA MIT 570.144: pentru FWSEC-ul plăcii noastre, `0x8241E0`); **verificarea I6 doar citire** (siguranța + semnătura aleasă,
  VRAM, zona protejată WPR2, regiunea FRTS); un test care fixează **exact cele 18 registre** pe care le-ar scrie I6. 304 teste trec.
  Commit-uri `3b47958`, `d6de57e`, `1dfa649` pe `g0-g2-fundatie`.
- Copia pentru sesiunea OS (C-34): `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `1dfa649`.

## Urmează — planul ferestrei următoare (C-49)
**Recomandare: întâi (a) proba tinygrad, apoi (b) prima scriere a driverului nostru.** De ce: tinygrad e un driver care merge deja pe plăci ca
a noastră cu același firmware; dacă trece, drumul e liber și primim „jurnalul de aur” (fiecare scriere, în ordine), cu care comparăm lista
noastră **înainte** de prima noastră scriere; dacă pică, știm că nu e greșeala noastră. În plus, (b) cere cod nou în OS, care nu există încă.
1. *(dacă OS-ul o adaugă — propunerea `idei/2026-11-01_cyber-gpu-i6-in-os.md`)* `gpu pregatire-i6` — **doar citire**: trebuie semnătura 0/1/2,
   VRAM 8192 MiB, „WPR2 coborat”, „0 scrieri”. Poză.
2. **(a) ⚠️ SCRIE ÎN PLACĂ (prin tinygrad):** proba tinygrad, exact ca în `cyber-gpu/docs/FEREASTRA_C-36.md` §3 (stick Ubuntu 24.04 live,
   laptopul pentru SSH, cablu de rețea, ~30 min). Scrie registre și VRAM; **nu scrie VBIOS-ul**; totul se șterge la oprirea completă.
3. **(b) — într-o fereastră separată, după (a):** I5g Bus Master = **o scriere** în configurația PCI (`0x04`, bitul 2) + I6 FWSEC-FRTS =
   **18 registre, toate în fereastra GSP** `0x110000–0x113FFF` (~720 de scrieri, majoritatea copierea programului FWSEC). Programul FWSEC
   (semnat NVIDIA) ridică apoi zona protejată WPR2 în VRAM — asta e tot ce schimbă în placă.
   - **Nu se poate strica:** VBIOS-ul (codul nostru nu are nicio cale de scriere spre el), siguranțele (doar citite); cod nesemnat sau o
     semnătură greșită sunt refuzate de placă; orice scriere în afara GSP e refuzată de cod înainte să ajungă la placă.
   - **Revenire:** butonul 10 s → cablul scos 30 s → Windows; `nvidia-smi` vede placa, Kronos pornește normal.
   - Nu în (b): Booter, pornirea GSP, lansările (I7+).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului
  (`aee06c4`): **doar adăugări** în interfața publică (ultimele: `nvidia_ga104::fuse`, `nvidia_ga104::i6_check` în sesiunea 30;
  `gpu_sim::cmdproc::{matmul_vec4_on_cpu, MATMUL_VEC4_NEEDS}` în 24; lista completă în `docs/IMPLEMENTATION_STATUS.md`). Codul OS nu trebuie
  schimbat; propunerea opțională `gpu pregatire-i6`: `integration/cyber-universe/C-49_gpu-pregatire-i6.md` (cere fereastra BAR0 doar-citire
  de 16 MiB).
- Pentru (b), mai târziu: OS-ul va trebui să dea o zonă de RAM pentru DMA (sub 4 GiB, ~64 KiB pentru FWSEC) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: opțional, `gpu pregatire-i6` (doar cu „da”-ul lui Adrian).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Alegerea ta:** fereastra următoare cu proba tinygrad (recomandat; trebuie stick Ubuntu, laptopul, cablu de rețea) și, dacă vrei,
  „da” pentru `gpu pregatire-i6` în OS. Prima scriere a driverului nostru (b) doar după, cu tine de față.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
