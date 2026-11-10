# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-10 11:20 (ora României) · **de:** sesiunea Cyber-GPU 78 (cloud, fără placă) — **C-96 URGENT: partea GPU gata în SIMULARE**, commit **`2d66deb`** pe `g0-g2-fundatie`; OS-ul (partea 2) poate lega commit-ul acum

## Acum
- **Sesiunea 78 — C-96 (I8 „eroare hardware 0xbadf5620”): cauza găsită, reparată, testată în simulare.** Preluat 10:52, jurnalul `gpu-jurnal-004.txt` citit 10:55, commit **`2d66deb`** la 11:15.
  - **Ce s-a întâmplat pe placă:** prima cerere a secvențiatorului GSP-RM a fost `WRITE 0x110040 ← 0`, apoi `CORE_RESET` = resetul falcon-ului GSP
    (`0x1103c0 ← 1`, `← 0`). **Prima citire a registrului HWCFG2 după eliberarea resetului a întors `0xbadf5620`** (cod PRI „client error”): falcon-ul care
    tocmai rula GSP-RM nu răspunde încă. Noi tratam orice `0xbadf…` ca defect și opream pe loc. Driverul NVIDIA 570.144 (public, MIT) și nouveau citesc
    registrul **în buclă** până arată „scrubbing gata”, fără să se oprească la `0xbadf…`. La I6/I7 același reset mersese pentru că GSP-ul era liber.
  - **Al doilea gol găsit (din driverul NVIDIA):** `CORE_RESUME` nu reseta GSP-ul în RISC-V înainte de cutiile LibOS — ar fi căzut la testul următor. Adăugat.
  - **Reparații (doar adăugări; interfața publică la fel):** buclele de așteptare trec prin `0xbadf…` („încă nu”) și, dacă registrul rămâne inaccesibil până
    expiră timpul, eroarea poartă valoarea citită; resetul ca în RM (citiri de propagare, limita RM de 4 s pentru scrubbing); `CORE_RESET` face și trecerea
    nucleului pe falcon (RM `kflcnSwitchToFalcon`); `CORE_RESUME` începe cu resetul în RISC-V. **Jurnalul** scrie acum fiecare cerere a secvențiatorului
    **întreagă, înainte de execuție** (`secv #0 WRITE 0x110040 0x0`, `secv #1 CORE_RESET`, …) și numește comanda care s-a oprit (cererea centrului de comandă).
  - **Dovada în simulare:** modelul `gpu-sim` răspunde `0xbadf5620` la primele citiri după resetul unui GSP care rula GSP-RM (OBSERVAT pe placă; durata e DEDUS).
    Driverul vechi pe acest model pică **exact ca placa**; cel nou trece până la `GSP_INIT_DONE`. 420 teste PASS, clippy, format, build no_std PASS.
    **Nimic testat pe RTX 3070 Ti** — pe placă se vede la următoarea rulare `gpu lant`.
  - Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-96_reset-gsp.md` (doar `kernel/Cargo.toml` pe `2d66deb`; niciun apel nou; compilează neschimbat).
  - Ce urmărim la rulare: rândurile `secv #…` (ce a cerut GSP-RM), apoi fie `GSP_INIT_DONE`, fie o eroare cinstită la pasul următor (`CORE_WAIT_FOR_HALT`,
    `CORE_RESUME`: cutia SEC2 ≠ 0, RISC-V inactiv). Orice eroare nouă va avea comanda vinovată în jurnal.
- **Sesiunea 77 — C-95 (laptopul GA106) parcat de Adrian;** rămâne notița `cyber-gpu/docs/GA106_LAPTOP.md`, codul retras (`24dc19c`).
- **Sesiunile 68–76:** C-83/C-87 gata în simulare (I11–I14, generare continuă, recuperare, „un singur program pe simbol” compilat, nerulat), `verifica_jurnal_lant`
  pentru lanțul C-83; C-91 (secvențiatorul, `bbbdb2f`) a mers pe placă azi. Detalii în `cyber-gpu/docs/IMPLEMENTATION_STATUS.md`.
- **Pe placă până acum:** I0–I4 doar citire TREC; I6 TRECE (os-242, os-275, os-276); I7 TRECE (os-246, os-275, os-276); I8: mesajul GSP-RM citit corect,
  secvențiatorul a pornit și s-a oprit la primul reset (reparat acum, în simulare); I9–I14 neîncercate.

## Lista pentru următoarea rulare `gpu lant` (după Release-ul OS cu `2d66deb`)
1. Pornire rece; stick-ul de test cu noul Release + stick-ul cu firmware 570.144 și #513 în `kronos\`.
2. `gpu lant` + „DA” o dată. De urmărit la I8: rândurile `secv #…`, nota de dinaintea resetului, `GSP_INIT_DONE`. O oprire curată la orice pas de după e un rezultat bun.
3. După: jurnalul în `rezultate/`; noi rulăm `verifica_jurnal_lant` și reparăm primul pas care se oprește.

## Urmează
1. OS-ul leagă `2d66deb` și scoate Release-ul (C-96 partea 2); apoi testul pe placă și analiza jurnalului.
2. „Un singur program pe simbol” — doar după ce lansările separate trec pe placă.

## Ce oferă proiectul celorlalți
- **Sesiunea 78 (C-96, doar adăugări):** `falcon::{switch_to_falcon, RESET_PROPAGATION_READS}`, `SeqCmd::event`, `gpu_core::diag::Event::SeqCmd`, `gpu-sim`
  `fake_gsp::{PRIV_ERROR_AFTER_RESET, PRIV_ERROR_READS, SimFault::PrivErrorStuck}`; `falcon::SCRUB_US` 20 ms → 4 s (aceeași constantă, altă valoare).
  Nimic redenumit sau șters. Jurnalul OS va conține rândurile noi `secv #…` prin `Display`, fără cod nou în OS.
- **Mai vechi (toate doar adăugări):** sesiunea 68 `chain_log::{check_chain_journal_for, chain_for_journal, step_ids_for}`; sesiunea 65 `kronos_token`; sesiunea 64
  `kronos_gen`, `recovery`, `user_space::stop_compute_group`, `GpuMemory::vram_free`; sesiunile 57–61 I11–I14 (`transfer`, `q8_matvec`, `kronos_layer`,
  `kronos_model`, `WINDOW_CHAIN_C83`, `push_bytes_per_token`); sesiunea 51 `falcon::{booter_load_dma_libos, gsp_reset_into_riscv, …}`. Lista completă:
  `cyber-gpu/docs/IMPLEMENTATION_STATUS.md` și notele din `cyber-gpu/integration/cyber-universe/`.
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). `kronos` / K6-CPU: operatorii pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (C-96 partea 2): `kernel/Cargo.toml` pe `2d66deb` + Release nou cu CI verde; nimic altceva de schimbat.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.
- De la Adrian: rularea `gpu lant` cu noul Release și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pașii pe placă cer fereastra cu Adrian.
- CI GitHub pe `2d66deb`: de verificat (local toate verificările trec).
