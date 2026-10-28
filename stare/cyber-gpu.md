# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-29 01:50 (ora României) · **de:** sesiunea Cyber-GPU 16 (cloud, fără placă)

## Acum
- Nicio comandă nouă pentru noi; C-36 (pregătirea ferestrei I3 → I4) e gata și așteaptă fereastra cu Adrian.
- Pas nou, **doar în SIMULARE**: I9c — „clientul de lucru”. După „golden image”, driverul deschide al doilea client și îi spune lui GSP-RM,
  prin mesajul `SET_PAGE_DIRECTORY`, că spațiul lui de adrese folosește tabelele de pagini făcute de noi (după RM 570.144 și tinygrad, MIT).
  Structurile mesajului sunt generate din antetele NVIDIA. Commit `695e537` pe `g0-g2-fundatie`; 256 de teste trec în sesiune; nimic nu scrie în placă.
- Testele automate GitHub merg din nou (Adrian a plătit): rulările 60 și 61 (`695e537`) verzi.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `695e537` (verificată, clonare de probă cu teste verzi).

## Urmează
- Fereastra C-36 pe workstation (cu Adrian): pașii 1 → 2 → 3 (mai jos).
- Fără placă: restul I9 pentru clientul de lucru (grupul de canale, contextul, canalul GPFIFO, jetonul soneriei); treapta 6 matmul.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Licență proprietară de la
  commit-ul de după `8313973` (până atunci MIT). Față de `8313973`: **doar adăugări** — nou în sesiunea 16: `nvidia_ga104::gsp::user_space`,
  `gsp::rmapi::{user_vaspace_params, set_page_directory_rpc, check_root}`, `GoldenImage::next_handle`. OS-ul nu trebuie să schimbe nimic.
  Schița pentru OS: `integration/cyber-universe/C-36_gpu-firmware-fwsec.md`; ghid: `integration/cyber-universe/UTILIZARE.md`.
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: `gpu fwsec` + `gpu firmware` (propunerea din `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md`) pe stick-ul pentru fereastră, dacă se aprobă; altfel ajunge stick-ul cu C-31.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
**Fereastra I3 → I4 (C-36), ~10–15 min fără proba tinygrad, ~45 min cu ea. Lista întreagă: `cyber-gpu/docs/FEREASTRA_C-36.md`.**
0. **Înainte, pe Windows:** pui pe stick-ul OS cele 4 fișiere în `firmware\nvidia\ga102\gsp\` și `LICENCE.nvidia` în `firmware\`.
   Verifici sumele: în PowerShell, în folderul cu fișierele, `Get-FileHash *.bin -Algorithm SHA256 | Format-List` → trebuie să înceapă cu
   `4497E3EF` (booter_load), `8E63DB5B` (booter_unload), `82428F53` (bootloader), `A8C3EBEE` (gsp). Kronos oprit și salvat.
1. **Placa, doar citire (nu scrie nimic):** pornești de pe stick, apoi `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile.
   Trece dacă lista nu se mai rupe la `0x24600` și rândul „rezumat” spune `criteriul I3: indeplinit`. Dacă există, și `gpu fwsec` → poză.
   Dacă nu trece: poze și te oprești cu placa.
2. **Fișierele de pe stick (nu atinge placa):** `gpu firmware` → 4 rânduri „ok … oficial” și `criteriul I4: TRECE`. Dacă OS-ul nu are încă
   comanda: `ls /usb/firmware/nvidia/ga102/gsp` → poză (ajung sumele verificate pe Windows).
3. **Doar dacă 1 și 2 au trecut — ⚠️ SCRIE ÎN PLACA VIDEO:** proba tinygrad (aprobată de tine pe 26 oct, doar cu tine de față). Ai nevoie de
   un al doilea stick cu Ubuntu 24.04 live, laptopul în aceeași rețea și cablu de rețea. Nu scrie în memoria permanentă a plăcii; după o
   oprire completă placa revine ca din fabrică. **Oprire sigură:** `Ctrl+C`, `sudo poweroff`; dacă nu răspunde, butonul ținut 10 s și
   cablul scos 30 s. La final, în Windows, `nvidia-smi` trebuie să vadă placa.
   Pornirea plăcii cu driverul nostru **nu** se face acum (vine într-o fereastră separată).
4. După: pozele (+ folderul `proba-tinygrad/`) în hub `rezultate/2026-10-29-workstation-gpu/`. **Fișierele firmware nu le pui în hub.**
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
