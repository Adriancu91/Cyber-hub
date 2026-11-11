# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-11 13:30 (ora României) · **de:** sesiunea Cyber-GPU 85 (cloud, fără placă) — **(1) jurnalul os-279 analizat: GSP-RM pornește, dar refuză inițializarea (`GSP_INIT_DONE` cu `0x59` = `NV_ERR_OPERATING_SYSTEM`) după 843 de înregistrări de diagnostic pe care jurnalul nu le citea; acum le decodează** (continuarea C-102). **(2) C-103 partea GPU gata în SIMULARE: WPR2 coborât fără repornire prin Booter Unload** (programul semnat NVIDIA deja pe stick), ca driverul NVIDIA. Commit `bcc314e` (cod: `5cfe523`, `364ece2`), 437 teste PASS, CI verde. **Nimic testat pe RTX 3070 Ti.**

## Acum
- **Sesiunea 85 (13:20–13:30) — C-103 (placa readusă la starea de pornire fără repornire), partea GPU, SIMULARE.** Preluat 13:20 (după C-102, cum cere comanda).
  - **Studiul (`cyber-gpu/docs/C-103_RESET_PLACA.md`):** calea publică de a coborî WPR2 fără reset PCIe e **Booter Unload** — exact ce face driverul NVIDIA la descărcare
    (`kgspExecuteBooterUnloadIfNeeded_TU102`, 570.144 MIT): reset SEC2, programul semnat `booter_unload` cu cutiile poștale `0xFF`/`0xFF`, mailbox0 trebuie 0, apoi
    `WPR2_ADDR_HI` trebuie să citească 0. **Fișierul e deja pe stick-ul lui Adrian** (al 4-lea din I4). FLR: plăcile GeForce de regulă nu-l anunță — se citește din
    spațiul de configurare; Secondary Bus Reset pe root-port (`b2:xx.0` → `b3`) = rezervă, decizia OS-ului; D3hot nu resetează dacă `No_Soft_Reset` = 1; D3cold nu există pe desktop
    fără S5 + „Power On By RTC” (varianta (b) a lui Adrian) sau priză inteligentă (c).
  - **Implementat (`364ece2`, doar adăugări):** `falcon::booter_unload[_dma]` (reset GSP → reset SEC2 → Booter Unload → verificări), modelul în `gpu-sim`; test T118: după I6 + I7,
    unload → WPR2 = 0 → **I6 rulează din nou în aceeași „pornire”**. `gpu_pci::caps::reset_capabilities` (doar citiri: FLR, `No_Soft_Reset`, D-state) pentru `raport` (T119).
    Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-103_gpu-recupereaza.md`. Nicio scriere nouă în afara ferestrelor GSP/SEC2; registrele WPR2 nu le scriem noi.
  - Pe placă: `gpu recupereaza` (OS) după un lanț oprit la I8; dacă WPR2 citește 0, a doua încercare nu mai cere cablul scos. Dacă Booter dă eroare: codul se notează, varianta cu
    FWSEC-SB înainte. 437 teste PASS, CI verde (`364ece2`, `bcc314e`). Copia din hub (C-34) la `bcc314e`.
- **Sesiunea 85 (12:28–13:05) — jurnalul `os-279` (`gpu-jurnal-007.txt`, 12:20) citit și răspuns la întrebarea sesiunii 84.** Nicio comandă nouă în hub; e pasul următor scris de C-102.
  - **Vestea bună:** lanțul de pornire merge **până la capăt**: I6, I7, toate cele 420 de comenzi ale secvențiatorului; la `#419 CORE_RESUME` Booter-ul a rulat
    de-adevăratelea (SCRATCH_14 `0x13100000` → `0x17100000`, bitul 26 pus abia după `0x840130 ← 2`, nu era bit vechi; SEC2 MAILBOX0 = 0), GSP RISC-V activ (`0x80`).
    **GSP-RM a pornit și a răspuns.**
  - **Vestea proastă:** răspunsul lui e `GSP_INIT_DONE` cu `rpc_result = 0x59` = **`NV_ERR_OPERATING_SYSTEM`** — GSP-RM însuși spune că inițializarea lui a eșuat
    (driverul NVIDIA citește același câmp la fel). Varianta „pointer stricat în coadă” e **exclusă**. Înainte de asta GSP-RM trimisese **843 de mesaje `0x1020`**
    și 2 × `0x100c`, pe care jurnalul le număra, dar nu le citea.
  - **Ce sunt (antetele MIT 570.144):** `0x1020` = `GSP_POST_NOCAT_RECORD` — o înregistrare de diagnostic (NOCAT) pe care RM-ul de pe GSP o trimite driverului:
    tip (BUGCHECK/ENGINE/TDR/RC/ASSERT), sursă (text), subsistem, cod de eroare, motorul vinovat; la ASSERT, adresa + linia din sursă și stiva de apeluri.
    **843 de astfel de înregistrări = RM-ul de pe GSP s-a plâns de 843 de ori în timpul propriei inițializări** — pe o pornire sănătoasă nu apare niciuna.
    `0x100c` = `UCODE_LIBOS_PRINT`, jurnalul PMU-ului în format binar LibOS (nu-l decodăm: ar cere simbolurile firmware-ului).
  - **Cauza lui `0x59` nu se poate spune încă** — e în conținutul celor 843 de înregistrări, pe care jurnalul vechi nu l-a scris. O „reparație” a parametrilor acum ar fi inventată.
  - **Ce am făcut (`5cfe523`, doar adăugări, doar citiri din mesaje primite):** jurnalul **decodează** fiecare înregistrare NOCAT (primele 4 și fiecare fel nou în
    întregime — `text NOCAT: source = "..."`, `recType`, codul cu numele `NV_STATUS` sau adresa + linia assertului, `subsystem`, stiva —, restul numărate),
    scrie descriptorul și mărimea jurnalelor PMU, numește orice mesaj sărit și orice cod `NV_STATUS` (tabel generat din antetele NVIDIA: 143 coduri, 228 funcții,
    36 evenimente), și pune un **rezumat** la orice sfârșit al așteptării (total, NOCAT, feluri, LibOS). Tip nou de rând: `text <nume> = "..."`. Teste T116–T117
    (SIMULARE); `verifica_jurnal_lant` pe `gpu-jurnal-007.txt`: „OPRIT CURAT la i8-gsp-init”, rândurile noi ignorate (verificat).
  - 433 teste PASS, clippy, format, build no_std PASS, CI verde (`93d530c`, `d84e331`, `5cfe523`). Nota pentru OS: `cyber-gpu/integration/cyber-universe/os-279_nocat-decodat.md`.
    Copia din hub (C-34) reîmprospătată la `f781428` (clonă completă, 195 commit-uri, `git bundle verify` OK, fără firmware).
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

## Lista pentru următoarea rulare `gpu lant` (Release `os-280`, cu `5cfe523` sau mai nou)
1. Pornire rece; stick-ul de test cu noul Release + stick-ul cu firmware 570.144 și #513 în `kronos\`.
2. `gpu lant` + „DA” o dată. **I8 se va opri probabil tot la `0x59`** — important e ce scrie înainte: rândurile `NOCAT` (mai ales `text NOCAT: source = "..."`,
   `text NOCAT: recType = "..."`, `NOCAT ASSERT: adresa …` + `linia …` sau `errorCode (nume NV_STATUS)`, `subsystem`) și rezumatul de la final
   (`I8 NOCAT (0x1020): inregistrari … primite`, `feluri distincte`). Poze la ele; jurnalul de pe stick e cel care contează. Esc oprește curat.
3. După: jurnalul în `rezultate/`; noi rulăm `verifica_jurnal_lant`, citim înregistrările și **abia atunci** reparăm ce îi lipsește lui GSP-RM.

## Urmează
0. **C-103 pe placă (OS):** `gpu recupereaza` după un lanț oprit — Booter Unload → WPR2 = 0? Dacă da, I6–I8 se reiau fără pornire rece (`cyber-gpu/integration/cyber-universe/C-103_gpu-recupereaza.md`).
1. OS-ul leagă `364ece2` (sau mai nou) → Release `os-280` → `gpu lant` cu Adrian de față; apoi `verifica_jurnal_lant` pe jurnalul din `rezultate/` și **repararea lui `0x59`
   din ce spun înregistrările NOCAT** (ce parametru / ce memorie / ce registru îi lipsește lui GSP-RM: `GSP_SET_SYSTEM_INFO`, registrul `SET_REGISTRY`, argumentele LibOS,
   `GspFwWprMeta`). Fără jurnal nou, niciun pas nou.
2. După `GSP_INIT_DONE` pe placă: primele apeluri RM (`GSP_GET_GSP_STATIC_INFO`), golden (I8e), I9, I10 — toate scrise, testate doar în simulare.
3. „Un singur program pe simbol” — doar după ce lansările separate trec pe placă.

## Ce oferă proiectul celorlalți
- **Sesiunea 85 (C-103, doar adăugări):** `nvidia_ga104::gsp::falcon::{booter_unload, booter_unload_dma, BOOTER_UNLOAD_MAILBOX, Unloaded}`; `gpu_pci::caps::{reset_capabilities,
  ResetCapabilities}` (doar citiri); `gpu-sim`: `SimUcode::BooterUnload`, `SimFault::Wpr2Stuck`.
- **Sesiunea 85 (după os-279, doar adăugări):** `gpu_core::diag::Event::Text { what, len, bytes }` (afișat `text <nume> = "..."`) + `Event::text(...)`, `TEXT_LEN`;
  `nvidia_rm570::names` (tabele generate) + `status_name`, `status_text`, `rpc_name`; `nvidia_ga104::gsp::nocat` (`NocatRecord`, `LibosPrint`); `rpc::name`,
  `rpc::event::GSP_POST_NOCAT_RECORD`; câmpuri noi în `sequencer::InitLog`. Nicio scriere nouă în registre. OS-ul folosește `_ =>` și `Display` → compilează neschimbat.
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
- De la `cyber-universe`: legarea `cyber-gpu` la `364ece2` (sau `bcc314e`), Release `os-280` cu CI verde — nimic de schimbat în codul OS pentru 0x59 (`Event::Text` e doar o variantă nouă);
  apoi C-103 partea OS: `gpu recupereaza` + rândul `reset_capabilities` în `raport`.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.
- De la Adrian: rularea `gpu lant` cu Release-ul `os-280` la fereastra următoare și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- **13:25 — răspuns la cererea urgentă „C-102 continuare” (Adrian la workstation):** cele trei puncte sunt **deja făcute** în `cyber-gpu` `5cfe523` (push 13:0x, CI verde):
  (1) `0x1020` = `GSP_POST_NOCAT_RECORD` (înregistrare de diagnostic a RM-ului de pe GSP), `0x100c` = `UCODE_LIBOS_PRINT` (jurnalul PMU, binar); (2) conținutul lor e jurnalizat
  (tip, sursă, cod cu nume `NV_STATUS` / adresa + linia asserturilor, subsistem, stiva; descriptor + mărime la LibOS) — doar citiri; (3) din antete **nu** se vede o cauză clară
  pentru `NV_ERR_OPERATING_SYSTEM` (e un cod generic al stratului LibOS al GSP-RM; motivul e în cele 843 de înregistrări) → doar diagnostic, nicio reparație inventată.
  **Release-ul `os-280` îl face sesiunea OS** (legarea `cyber-gpu` ≥ `5cfe523`, nimic de schimbat în codul OS); estimare: ~15 min de la prima ei trecere. Dacă Adrian nu mai poate
  aștepta azi, testul cu `os-280` se face la fereastra următoare — jurnalul va spune cauza.
- **Nu e blocat, dar depinde de placă:** `0x59` vine de la GSP-RM însuși, iar motivul e în cele 843 de înregistrări de diagnostic pe care jurnalul nou le citește.
  Următoarea rulare `gpu lant` (os-280) le aduce; fără ea nu se poate repara nimic „la sigur”.
- CI GitHub VERDE pe `5cfe523`, `364ece2` (cod) și `bcc314e` (document).
