# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-11 10:52 (ora României) · **de:** sesiunea Cyber-GPU 84 (cloud, fără placă) — **C-102 (I8 „eroare hardware 0x59” la os-278): partea GPU gata, în SIMULARE** — oprirea de siguranță s-a ridicat (jurnal nou + comandă nouă). Commit `f96c0ee` (cod: `d31ad8d`), 426 teste PASS, CI verde (rularea 160). **Nimic testat pe RTX 3070 Ti.**

## Acum
- **Sesiunea 84 (10:28–10:52) — C-102 URGENT: ce e `0x59` și de unde vine.** Preluat 10:30; jurnalul `gpu-jurnal-006.txt` citit 10:35; commit `d31ad8d` 10:46, CI verde 10:48.
  - **Vestea bună din jurnal:** reparația C-99 a mers: `#419 CORE_RESUME` a pornit SEC2 prin alias (`0x840130 ← 2`), „SEC2 (Booter) gata: răspuns după 2 µs”, `FALCON_OS` scris, „GSP RISC-V activ: răspuns după 2 µs”. **Toate cele 420 de comenzi ale secvențiatorului au trecut.** Eroarea a venit ~150 ms **după** secvențiator (nu există rândul „comanda de mai jos s-a oprit”).
  - **Ce e `0x59`:** în codul nostru, după secvențiator, `0x59` poate veni din exact două locuri: (1) `GSP_INIT_DONE` sosit de la GSP-RM cu `rpc_result = 0x59` — în antetele publice NVIDIA 570.144 (`nvstatuscodes.h`, MIT) `0x59` = **`NV_ERR_OPERATING_SYSTEM`** („eroare generică de sistem de operare” — pe GSP-RM, un apel către sistemul lui LibOS care a dat greș); (2) pointerul de scriere al cozii de stare citit **89** (= 0x59), în afara cozii de 63 (memoria cozii stricată după resume). **Jurnalul vechi nu scria nicio citire în I8, așa că nu se poate spune care din două** — o „reparație” fără acest răspuns ar fi inventată, deci nu am făcut-o.
  - **Observația (a) din REZULTAT stă:** 2 µs e prea puțin ca Booter să fi rulat; bitul 26 din `NV_PGC6_BSI_SECURE_SCRATCH_14` putea fi deja pus de la I7. Am citit driverul NVIDIA (`kernel_gsp_ga102.c`, CORE_RESUME): face exact pașii noștri și **nu scrie și nu șterge** acest registru → nu scriem nici noi în el (regula: nicio scriere nouă în registre).
  - **Ce am făcut (`d31ad8d`, doar adăugări, doar citiri):** jurnalul numește acum sursa oricărei erori din I8: rânduri `valoare <nume> = 0x…` cu 7 registre (SCRATCH_14, SEC2 CPUCTL/MAILBOX0/1, GSP RISCV_CPUCTL, GSP MAILBOX0/1) **înainte de pornirea SEC2** și **după predarea etapei 3** la `CORE_RESUME`; fiecare mesaj GSP-RM sărit (funcția, `rpc_result`); la `GSP_INIT_DONE` → `rpc_result` + „I8: eroarea vine din GSP_INIT_DONE”; la coadă → „pointer in afara cozii (0..62)” + „eroarea vine din coada de stare”; la timp expirat / Esc → aceleași registre. Teste T113–T115 (SIMULARE). `verifica_jurnal_lant` pe `gpu-jurnal-006.txt`: „OPRIT CURAT la i8-gsp-init”, I8 326 scrieri + 1 sonerie; rândurile noi sunt ignorate de parser (verificat).
  - 426 teste PASS, clippy, format, build no_std PASS, CI verde (rularea 160 pe `d31ad8d`). Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-102_i8-0x59-diagnostic.md`. Copia din hub (C-34) rămâne la `6290eee` (OS-ul citește direct de pe GitHub; se reîmprospătează la sesiunea următoare).
- **Sesiunea 80 (17:16–17:40) — C-99 (I8 „timeout după 2 s”): cauza găsită, reparată, testată în simulare.** Preluat 17:16, jurnalul `gpu-jurnal-005.txt` citit 17:20, reparația `3fe11f9` la 17:28, așteptarea lungă `3aed5eb` la 17:36.
  - **Vestea bună din jurnal:** după reparația C-96, **toate cele 420 de comenzi ale secvențiatorului GSP-RM au mers** (POLL/WRITE pe falcon-ul GSP, `CORE_RESET`, copierea DMA, configurarea) până la ultima, `secv #419 CORE_RESUME`.
  - **Ce s-a întâmplat pe placă la `CORE_RESUME`:** după resetul GSP-ului în RISC-V și cutiile LibOS, driverul a scris pornirea SEC2 (Booter) în `0x840100` (`CPUCTL`):
    **`0x840100: 0x50 <- 0x2 => 0x50`** — registrul arăta `0x50` = HALTED | **ALIAS_EN** și scrierea nu s-a prins (citit înapoi neschimbat). SEC2 n-a pornit niciodată,
    deci „predarea etapei 3” pe care o așteptam n-a venit: timeout după 2 s. La I7 același registru arăta `0x10` (ALIAS_EN = 0) și pornirea mersese; după ce rulează
    Booter (program semnat), `CPUCTL` rămâne în spatele aliasului. Driverul NVIDIA 570.144 (public, MIT, `kflcnStartCpu_TU102`) și nouveau verifică bitul `ALIAS_EN`
    și scriu atunci în `CPUCTL_ALIAS` (`0x840130`). **Noi făceam asta la `CORE_START`, dar nu la `CORE_RESUME`.** Nu era „prea puțin timp”: oricât am fi așteptat, SEC2 nu pornise.
  - **Reparația (`3fe11f9`, doar adăugări):** `falcon::start_cpu` — pornirea prin `CPUCTL_ALIAS` când `ALIAS_EN` e pus; folosit acum și de `CORE_RESUME`.
    **Dovada în simulare:** `gpu-sim` modelează placa (după Booter, `CPUCTL` al SEC2 citește `0x50`, scrierea în `CPUCTL` e ignorată — OBSERVAT); driverul vechi
    pe acest model dă exact `Timeout { waited_us: 2000000 }` (placa: 2 000 003 µs); cel nou pornește prin `0x840130` și ajunge la `GSP_INIT_DONE` (T111).
  - **Ideea lui Adrian (aprobată 17:16, `3aed5eb`):** așteptările I8 de după sonerie care depind de GSP-RM (`CORE_WAIT_FOR_HALT`, `CORE_RESUME`, `GSP_INIT_DONE`)
    au acum limita **60 s** (`sequencer::LONG_WAIT_US`; `INIT_DONE_US` 10 s → 60 s); când răspunsul vine, jurnalul scrie **după cât timp**
    (`asteptat CORE_RESUME: SEC2 (Booter) gata: raspuns dupa N us`, …); **oprirea manuală**: metodă nouă `Clock::abort_requested` (implicit `false`) întrebată
    în toate buclele de așteptare → eroarea nouă „oprit manual dupa N us”. Tasta Esc și rândul „aștept GSP… N s” de pe ecran le leagă OS-ul în `TscClock` (T112).
  - 423 teste PASS, clippy, format, build no_std PASS, CI verde pe `3fe11f9` și `3aed5eb`. **Nimic testat pe RTX 3070 Ti.**
  - Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-99_core-resume-alias.md`.
- **Sesiunea 78 — C-96 (`0xbadf5620` la `CORE_RESET`)** a mers pe placă azi (os-277): secvențiatorul a trecut de reset. Detalii în `cyber-gpu/docs/IMPLEMENTATION_STATUS.md`.
- **Sesiunea 77 — C-95 (laptopul GA106) parcat de Adrian;** rămâne notița `cyber-gpu/docs/GA106_LAPTOP.md`.
- **Pe placă până acum:** I0–I4 doar citire TREC; I6 TRECE (os-242, os-275, os-276, os-277); I7 TRECE (os-246, os-275, os-276, os-277); I8: mesajul GSP-RM citit corect,
  **419 din 420 de comenzi ale secvențiatorului executate**, oprit la `CORE_RESUME` (reparat acum, în simulare); I9–I14 neîncercate.

## Lista pentru următoarea rulare `gpu lant` (Release `os-279`, cu `d31ad8d` sau mai nou)
1. Pornire rece; stick-ul de test cu noul Release + stick-ul cu firmware 570.144 și #513 în `kronos\`.
2. `gpu lant` + „DA” o dată. De urmărit la I8, după `secv #419 CORE_RESUME`: rândurile `valoare …` dinainte de `bar0 w 0x840130` (dacă `PGC6 SCRATCH_14` are deja
   bitul 26 = `0x04000000`, „2 µs” era bitul vechi de la I7), apoi `GSP_INIT_DONE` sau rândul „I8: eroarea vine din …” cu valorile de lângă el. Esc oprește curat după ~1 minut.
3. După: jurnalul în `rezultate/`; noi rulăm `verifica_jurnal_lant` și reparăm primul pas care se oprește.

## Urmează
1. OS-ul leagă `d31ad8d` (sau mai nou) → Release `os-279` → `gpu lant` cu Adrian de față; apoi `verifica_jurnal_lant` pe jurnalul din `rezultate/` și **repararea lui `0x59`
   acum că jurnalul spune de unde vine** (GSP_INIT_DONE cu cod NV_STATUS → ce i-a lipsit GSP-RM la resume; pointer stricat → ce a scris peste coadă). Fără jurnal nou, niciun pas nou.
2. După `GSP_INIT_DONE` pe placă: primele apeluri RM (`GSP_GET_GSP_STATIC_INFO`), golden (I8e), I9, I10 — toate scrise, testate doar în simulare.
3. „Un singur program pe simbol” — doar după ce lansările separate trec pe placă.

## Ce oferă proiectul celorlalți
- **Sesiunea 84 (C-102, doar adăugări):** `gpu_core::diag::Event::Value { what, value }` (afișat `valoare <nume> = 0x........`), `falcon::{RESUME_STATE_READS, journal_resume_state}`.
  Nicio scriere nouă în registre. OS-ul folosește `_ =>` la evenimente și `Display`, deci compilează neschimbat.
- **Sesiunea 80 (C-99, doar adăugări):** `falcon::{start_cpu, wait_riscv_active_for}`, `sequencer::LONG_WAIT_US`, `gpu_core::hal::Clock::abort_requested`
  (metodă cu implementare implicită — implementările existente compilează neschimbate), `gpu_core::error::GpuError::Aborted { waited_us }`,
  `gpu_core::diag::Event::Waited { what, waited_us }`, `gpu-sim`: `SimClock::abort_at`, modelul `ALIAS_EN` după Booter. `sequencer::INIT_DONE_US` 10 s → 60 s
  (aceeași constantă, altă valoare). Nimic redenumit sau șters. OS-ul folosește `_ =>` la potrivirea evenimentelor și `Display` la erori, deci compilează neschimbat.
- **Sesiunea 78 (C-96, doar adăugări):** `falcon::{switch_to_falcon, RESET_PROPAGATION_READS}`, `SeqCmd::event`, `Event::SeqCmd`, `gpu-sim`
  `fake_gsp::{PRIV_ERROR_AFTER_RESET, PRIV_ERROR_READS, SimFault::PrivErrorStuck}`; `falcon::SCRUB_US` 20 ms → 4 s.
- **Mai vechi (toate doar adăugări):** sesiunea 68 `chain_log::{check_chain_journal_for, chain_for_journal, step_ids_for}`; sesiunea 65 `kronos_token`; sesiunea 64
  `kronos_gen`, `recovery`, `user_space::stop_compute_group`, `GpuMemory::vram_free`; sesiunile 57–61 I11–I14 (`transfer`, `q8_matvec`, `kronos_layer`,
  `kronos_model`, `WINDOW_CHAIN_C83`, `push_bytes_per_token`); sesiunea 51 `falcon::{booter_load_dma_libos, gsp_reset_into_riscv, …}`. Lista completă:
  `cyber-gpu/docs/IMPLEMENTATION_STATUS.md` și notele din `cyber-gpu/integration/cyber-universe/`.
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). `kronos` / K6-CPU: operatorii pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (C-102 partea 2): legarea `cyber-gpu` la `d31ad8d` (sau `f96c0ee`), Release `os-279` cu CI verde — nimic de schimbat în codul OS (`Event::Value` e doar o variantă nouă).
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.
- De la Adrian: rularea `gpu lant` cu Release-ul `os-279` (azi, dacă OS-ul îl scoate până ~12:15) și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- **Nu e blocat:** `0x59` nu se poate repara „la sigur” fără să știm din care din cele două locuri vine — Release-ul `os-279` cu jurnalul nou răspunde la asta la prima rulare. Orice oprire curată e un rezultat bun — analiza o facem noi.
- CI GitHub VERDE pe `d31ad8d` (rularea 160, 10:47) și `f96c0ee` (document).
