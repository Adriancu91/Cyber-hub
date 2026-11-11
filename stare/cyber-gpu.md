# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-11 07:35 (ora României) · **de:** sesiunea Cyber-GPU 83 (cloud, fără placă) — **OPRIT: necesită analiza lui Adrian** (regula 8 din programare: sesiunile 81–83 fără pas nou, pentru că tot ce se poate face fără placă e făcut; se ridică singur la jurnalul testului cu `os-278` sau la o comandă nouă pentru `cyber-gpu`). Codul neschimbat (`3aed5eb`), 423 teste PASS, CI verde; copia din hub (C-34) la `6290eee`.

## Acum
- **Sesiunea 83 (07:20–07:40) — OPRIT (regula 8).** Nicio comandă nouă pentru cyber-gpu (C-100, pentru Kronos, s-a închis la 02:15: placa a fost la Kronos noaptea, liberă de la 01:59),
  niciun jurnal nou de pe placă (ultimul: `rezultate/2026-11-10-workstation-os277/`; dosarul `…-os278/` nu există). OS-ul e pe `os-278` și s-a oprit la fel la 05:45.
  Nu e nimic stricat: I8 e reparat de două ori în simulare (C-96, C-99), I9–I14 sunt scrise și testate în simulare — **următorul pas depinde doar de un jurnal real de pe placă.**
  Nu se începe lucru nou și nu se inventează. `sh tools/check.sh`: 423 teste PASS, CI verde pe `54cf0a2`; copia din hub (C-34) reîmprospătată la `6290eee` (istorie completă, 188 commit-uri, fără firmware). **Nimic testat pe RTX 3070 Ti.**
- **Sesiunea 82 (01:25–01:40) — oprire scurtă.** Nicio comandă nouă pentru cyber-gpu (ultima e C-100, pentru Kronos), niciun jurnal nou de pe placă
  (ultimul: `rezultate/2026-11-10-workstation-os277/`). OS-ul e tot pe `os-278`. Codul neschimbat față de `3aed5eb` (doar starea, `54cf0a2`); `sh tools/check.sh`: 423 teste PASS, CI verde pe `ec23e4d`.
  Copia din hub (C-34) reîmprospătată la `54cf0a2` (istorie completă, 187 commit-uri, fără firmware). **Nimic testat pe RTX 3070 Ti.**
  Regula 8: sesiunile 81 și 82 fără pas de cod (80 a avut) — dacă nici sesiunea 83 nu găsește jurnal sau comandă nouă, se aplică oprirea de siguranță, fără lucru inventat.
- **Sesiunea 81 (19:25–19:45) — oprire scurtă.** Nicio comandă nouă pentru cyber-gpu, niciun jurnal nou de pe placă. OS-ul a terminat partea lui din C-99
  (`de63f32`, Release **`os-278`**: Esc + „astept raspunsul placii (GSP)... N s”). Adrian a plecat ~18:00, placa e la Kronos până la 07:00 (C-100) → **testul cu `os-278` așteaptă fereastra următoare.**
  Codul neschimbat față de `3aed5eb` (doar starea, `ec23e4d`); 423 teste PASS, CI verde. **Copia din hub (C-34)** era rămasă la `bbbdb2f` (9 nov) — refăcută din clona completă la `ec23e4d`
  (verificată: istorie completă, clonă de probă cu același arbore, fără firmware). **Nimic testat pe RTX 3070 Ti.**
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

## Lista pentru următoarea rulare `gpu lant` (Release `os-278`, cu `3aed5eb`)
1. Pornire rece; stick-ul de test cu noul Release + stick-ul cu firmware 570.144 și #513 în `kronos\`.
2. `gpu lant` + „DA” o dată. De urmărit la I8, după `secv #419 CORE_RESUME`: `bar0 w 0x840130` (pornirea prin alias), rândurile `asteptat …` (cât a durat),
   apoi `GSP_INIT_DONE` sau prima eroare după el. Dacă ecranul arată „aștept GSP…” mai mult de ~1 minut, Esc oprește curat (Bus Master pus la loc).
3. După: jurnalul în `rezultate/`; noi rulăm `verifica_jurnal_lant` și reparăm primul pas care se oprește.

## Urmează
1. Testul pe placă cu `os-278` (fereastra următoare a lui Adrian; pașii sunt în `stare/cyber-universe.md`), apoi `verifica_jurnal_lant` pe jurnalul din `rezultate/`
   și repararea primului pas care se oprește. Fără jurnal nou și fără comandă nouă, sesiunile următoare rămân OPRITE (doar verificarea CI și a copiei C-34).
2. După `GSP_INIT_DONE` pe placă: primele apeluri RM (`GSP_GET_GSP_STATIC_INFO`), golden (I8e), I9, I10 — toate scrise, testate doar în simulare.
3. „Un singur program pe simbol” — doar după ce lansările separate trec pe placă.

## Ce oferă proiectul celorlalți
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
- De la `cyber-universe`: nimic acum — C-99 partea 2 e gata (`de63f32`, `os-278`, cu Esc și antetul cozii de stare tot 60 s).
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.
- De la Adrian: rularea `gpu lant` cu Release-ul `os-278` la următoarea fereastră și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- **OPRIT (regula 8), nu blocat:** cyber-gpu așteaptă testul `gpu lant` cu `os-278` pe workstation (pașii: `stare/cyber-universe.md`) și jurnalul `raport\gpu-jurnal-*.txt` în `rezultate/`. Orice oprire curată e un rezultat bun — analiza o facem noi.
- CI GitHub VERDE pe `3aed5eb` … `54cf0a2` (rularea 158, 01:30); `6290eee` e doar document.
