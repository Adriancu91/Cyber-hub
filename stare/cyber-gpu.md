# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-28 22:50 (ora României) · **de:** sesiunea Cyber-GPU 15 (cloud, fără placă)

## Acum
- **C-36 gata (pregătirea ferestrei I3 → I4):** pașii exacți sunt în `cyber-gpu/docs/FEREASTRA_C-36.md` (rezumat mai jos, la „nevoie de Adrian”).
- Cod nou, **doar în SIMULARE**: `fw_check` verifică, fără să atingă placa, toate cele 4 fișiere firmware de pe stick (lipsă / altă mărime /
  alt conținut / oficial) și spune separat dacă greșeala e în fișier sau în codul nostru; rândurile I3b (unde e FWSEC în VBIOS) pentru ecran.
  Commit-uri `2c9c90c`, `51848d6` pe `g0-g2-fundatie`. 251 de teste trec în sesiune; nimic nu scrie în placă.
- Pentru OS: comanda-propunere `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md` (`gpu fwsec` + `gpu firmware`, ambele doar citire);
  schița a fost compilată într-o copie a OS-ului (repo-ul OS neatins).
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `0d06f4d` (verificată, clonare de probă cu teste verzi).
- CI-ul GitHub tot nu pornește (repo privat, fără minute). Testele rulează în fiecare sesiune.

## Urmează
- Fereastra C-36 pe workstation (posibil 29 oct, cu Adrian): pașii 1 → 2 → 3.
- Sesiunea OS: propunerea din `idei/` (dacă e aprobată) + stick nou prin hub (C-35).
- Fără placă: treapta 6 matmul (Mesa NAK pe gazdă); `SET_PAGE_DIRECTORY`.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Licență proprietară de la
  commit-ul de după `8313973` (până atunci MIT). Față de `8313973`: **doar adăugări** — nou: `nvidia_ga104::fw_check`,
  `fwsec::FwsecLocation::lines()`, `gpu_sim::fw_stick`. Schița pentru OS: `integration/cyber-universe/C-36_gpu-firmware-fwsec.md`;
  ghid: `integration/cyber-universe/UTILIZARE.md`. Sursa: bundle-ul din hub.
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: `gpu fwsec` + `gpu firmware` (propunerea din `idei/`) pe stick-ul pentru fereastră, dacă se aprobă; altfel ajunge stick-ul cu C-31.
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
- **De decis (fără grabă):** testele automate GitHub nu rulează cu repo-ul privat (merge și așa, testele rulează în fiecare sesiune).
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
