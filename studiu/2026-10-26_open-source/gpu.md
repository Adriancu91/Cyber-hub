# Studiu: proiecte deschise utile pentru Cyber-GPU

*26 octombrie 2026. Cercetare, fără nicio modificare în vreun repo. Am pornit de la `Adriancu91/cyber-gpu`, ramura `g0-g2-fundatie`
(README + tot `docs/`), apoi am clonat și am citit efectiv sursele de mai jos.*

**Etichete folosite:** **CITIT** = am văzut cu ochii mei în fișierul indicat (cu linia aproximativă); **DEDUS** = concluzia mea din ce am citit;
**NEVERIFICAT** = nu am văzut sursa, nu te baza pe asta fără verificare.

**Pe scurt (pentru Adrian):** cea mai importantă descoperire e că **tinygrad** (licență MIT) conține deja un driver NVIDIA complet,
scris în ~1 100 de rânduri de Python, care **pornește singur GSP-ul pe plăcile Ampere (GA102, deci și GA104) cu exact firmware-ul ales de tine,
570.144**, fără driverul NVIDIA și fără CUDA, și apoi lansează programe de calcul. Practic e „harta” pașilor I4–I10, scrisă de altcineva,
testată pe plăci reale și cu o licență care ne permite s-o folosim. Asta poate scurta mult drumul până la primul calcul.

---

## 1. Tabelul surselor

Versiunile citite: tinygrad `f5b17be` (26 oct 2026); NVIDIA open-gpu-kernel-modules eticheta `570.144`; Mesa `8e3dba4` (26 oct 2026);
envytools `f102b82` (oct 2023); SGEMM_CUDA (siboehm) ultima versiune; CUTLASS ultima versiune (doar licența).

| Proiect | Link | Licență (din fișierul LICENSE) | Ce am învățat (concret) | Unde se aplică la Cyber-GPU | Cod folosibil? |
|---|---|---|---|---|---|
| **tinygrad — driverul NV prin PCI** (`tinygrad/runtime/support/nv/nvdev.py`, `nv/ip.py`) | github.com/tinygrad/tinygrad | **MIT** (© 2024 the tiny corp) | Toată secvența de pornire GA102 cu 570.144: FWSEC din VBIOS → FRTS (WPR2) → GSP în mod RISC-V → Booter pe SEC2 → cozi RPC → `INIT_DONE` → „golden image” → canal → lansare. Registre, ordine, limite de timp, formatul mesajelor RPC. | **I4–I10, tot drumul** | **Da, cu atribuire** (MIT). Recomand însă „scriere proprie după el ca specificație” (vezi propunerea B) |
| **tinygrad — `ops_nv.py`** | idem | MIT | Cum se construiește pushbuffer-ul (antetul metodei), intrarea GPFIFO, semafoarele, QMD v3, lansarea (`SEND_PCAS_A` + `SEND_SIGNALING_PCAS2_B`), cum se încarcă un program compilat cu **NAK** | I9–I10, primul program | Da, cu atribuire |
| **tinygrad — `test/mockgpu/nv/nvgpu.py`, `test/mockgpu/am/amgpu.py`** | idem | MIT | Un „GPU fals” care citește GPFIFO + pushbuffer + QMD și execută programul pe CPU; pentru AMD, un fals la nivel de registre (PSP, SMU, SDMA ca mici automate) | Teste pe simulare (`gpu-sim`) | Doar idei (e Python, pentru alt strat) |
| **NVIDIA open-gpu-kernel-modules @570.144** | github.com/NVIDIA/open-gpu-kernel-modules | **MIT** (fișierul `COPYING`: „individual files … licensed as MIT”, cu excepțiile notate) | Antetele cu registrele falcon/GSP/SEC2 pentru GA102 sunt publicate oficial; structurile RPC, cozile `msgq`, `GspFwWprMeta`, clasele C56F/C6C0/C7C0 | I5–I10 | **Da, cu notificarea NVIDIA** (sunt antete MIT = specificație) |
| **NVIDIA open-gpu-doc** | github.com/NVIDIA/open-gpu-doc | **MIT** (© 2019 NVIDIA) | Deja folosit în proiect (dev_boot, clc56f, clc7c0qmd) | I1, I9–I10 | Da, cu notificare |
| **Mesa NAK** (`src/nouveau/compiler/nak/`) | gitlab.freedesktop.org/mesa/mesa | **MIT** (SPDX în fiecare fișier, © Collabora) | `qmd.rs` umple QMD-ul în Rust pentru Ampere (QMDV03_00, clasa C6C0); `hw_runner.rs` = cel mai mic „lansator de calcul” (5 metode de inițializare + 2 de lansare); `hw_tests.rs` construiește programe direct din IR-ul NAK și le compară cu calculul pe CPU; `nvdisasm_tests.rs` verifică codificarea cu dezasamblorul NVIDIA | Unealta NAK (G6), I10, matmul, teste | Da, cu atribuire (dar noi îl folosim ca **unealtă pe gazdă**, cum ai decis) |
| **Mesa NVK** (`src/nouveau/vulkan/`) | idem | MIT | Același model de lansare ca NAK (doar privit pe deasupra) | I10 | Doar idei |
| **nova-core** (Linux, Rust) | kernel.org / LKML | **GPL-2.0** | Deja în PROVENANCE. Stare (Phoronix, 8 oct 2026): GSP pornește pe Turing…Blackwell, **calculul nu merge încă**, nu e gata pentru utilizatori | Doar ordinea pașilor | **Doar idei** (GPL) |
| **nouveau** `nvkm/subdev/gsp/r535*` | kernel.org | MIT-style | Deja folosit ca idee; tinygrad acoperă același teren, cu 570.144 | I5–I8 | Doar idei (regula proiectului) |
| **envytools** | github.com/envytools/envytools | **MIT** (fișierul `COPYING`) | Documentație bună pentru *concepte*: falcon (transferuri DMA, `docs/hw/falcon/xfer.rst`), formatul pushbuffer/IB (`docs/hw/fifo/dma-pusher.rst`); acoperirea se oprește înainte de Turing/Ampere, ultimul commit oct 2023 | Înțelegere, nu valori | Doar idei |
| **siboehm SGEMM_CUDA** | github.com/siboehm/SGEMM_CUDA | **MIT** (© 2023 Simon Boehm) | 10 trepte de matmul, măsurate pe A6000 (GA102, Ampere): naiv 309 GFLOP/s → 2D blocktiling 15 972 → warptiling 21 779 (94 % din cuBLAS) | Matmul pentru Kronos | Da, cu atribuire (dar e CUDA C; la noi se rescrie pentru NAK) |
| **CUTLASS** | github.com/NVIDIA/cutlass | **BSD-3-Clause** pentru bibliotecă; **atenție: `EULA.txt` = licență proprietară NVIDIA pentru „CUTLASS DSLs”** | Doar am verificat licențele | Matmul (idei de împărțire în blocuri) | Doar idei (C++/CUDA, nu se compilează la noi) |
| **gdev** (Shinpei Kato) | github.com/shinpei0208/gdev | **MIT** | Doar licența; e un runtime pentru plăci vechi (dinainte de GSP) | — | Nu merită (vezi §4) |
| **Asahi (driverul GPU Apple, Rust)** | LKML, patch „rust: macros: Add versions macro” (mar. 2023) | GPL-2.0 (kernel) | Macro-ul `versions` generează automat câte o variantă de structură pentru fiecare versiune de firmware | Stratul RPC (dacă vreodată schimbăm versiunea) | Doar idei |
| **Documentația mmiotrace** (Linux) | stuff.mit.edu (copie a `Documentation/trace/mmiotrace.rst`) | GPL-2.0 (documentație) | Înregistrează fiecare citire/scriere MMIO (lățime, timp, adresă, valoare); doar x86, oprește celelalte procesoare | Testare pe placa reală | Doar idei |

---

## 2. Lecții (notițele)

**Despre pornirea GSP (I4–I8) — totul CITIT în tinygrad `support/nv/ip.py` și `nvdev.py`, cu verificare în antetele NVIDIA 570.144**

1. **Ordinea completă există, scrisă, pentru GA102 + 570.144.** `NVDev.__init__` (nvdev.py ~l. 74–85) face: inițializare timpurie →
   MMU → `init_sw` pentru falcon și GSP (pregătește tot în memorie) → `init_hw` pentru falcon și GSP (pornește). La oprire:
   `rpc_unloading_guest_driver` (ip.py ~l. 611). Codul nostru `init.rs` are pașii I0–I10; ordinea lor coincide cu a tinygrad. (CITIT + DEDUS)
2. **Sumele SHA-256 se potrivesc.** tinygrad fixează `booter_load-570.144.bin` = `4497e3ef…`, `bootloader-570.144.bin` = `82428f53…`,
   `gsp-570.144.bin` = `a8c3ebee…` (ip.py ~l. 172, 402, 426) — **identice** cu cele din `cyber-gpu/crates/nvidia-ga104/src/firmware.rs`.
   Confirmare independentă că avem fișierele corecte. (CITIT)
3. **Registrele falcon pentru GA102 NU mai sunt necunoscute.** `docs/RESEARCH_I4_I8.md` §3 spune „offset-urile exacte ale registrelor falcon pe
   GA10x: NECUNOSCUT”. Ele sunt publicate de NVIDIA, MIT, în `src/common/inc/swref/published/ampere/ga102/`: `dev_falcon_v4.h`
   (ex. `DMATRFCMD 0x118`, `HWCFG2 0xf4`, `CPUCTL 0x100`, `BOOTVEC 0x104`, `OS 0x80`), `dev_gsp.h` (`NV_PGSP_FALCON_MAILBOX0 0x110040`,
   `NV_PGSP_FALCON_ENGINE 0x1103c0`, `NV_PGSP_QUEUE_HEAD(i) 0x110c00+i*8`), `dev_sec_pri.h`, `dev_riscv_pri.h`, `dev_fbif_v4.h`,
   `dev_falcon_second_pri.h` + fișierele `*_addendum.h`. Bazele: GSP = `0x110000`, SEC2 = `0x840000` (ip.py ~l. 187). (CITIT în ambele)
4. **GFW_BOOT are și sursă NVIDIA, nu doar nouveau.** `dev_gc6_island_addendum.h` (MIT, NVIDIA) definește `…GROUP_05_0_GFW_BOOT_PROGRESS 7:0`,
   valoarea `COMPLETED = 0xFF`, și `NV_USABLE_FB_SIZE_IN_MB = NV_PGC6_AON_SECURE_SCRATCH_GROUP_42` (`0x1183a4`). Codul nostru `gfw.rs` e corect
   și poate cita NVIDIA direct. Bonus: **mărimea VRAM se citește dintr-un singur registru** (tinygrad: `vram_size = GROUP_42 << 20`, nvdev.py ~l. 127). (CITIT)
5. **Verificare ieftină înainte de orice: „e WPR2 deja ridicat?”** tinygrad citește `NV_PFB_PRI_MMU_WPR2_ADDR_HI` (`0x1FA828`, confirmat în
   `turing/tu102/dev_fb.h` al NVIDIA); dacă e ≠ 0, placa a fost deja pornită de un driver și face reset (nvdev.py ~l. 101–105). La noi:
   **o citire în plus, doar-citire, care se poate adăuga la testul I2** — spune dacă placa e „curată” (cum ar trebui după pornire din UEFI). (CITIT + DEDUS)
6. **FWSEC-FRTS (I6): rețeta exactă.** Din VBIOS se găsește aplicația `0x85` (FWSEC_PROD) → descriptorul V3 (44 de octeți) → în imagine se găsește
   „interfața aplicației”, intrarea `DMEMMAPPER` (id 4) → se scrie comanda `0x15` (FRTS) și o structură `FWSECLIC_FRTS_CMD`
   (citire VBIOS + regiunea FRTS: offset în pagini de 4 KiB, mărime `0x100` = 1 MiB, tip 2 = VRAM) → se pune semnătura de 384 de octeți
   la `IMEMLoadSize + PKCDataOffset` (ip.py ~l. 145–169; structurile în `extra/nv_gpu_driver/vbios.h`, **antet NVIDIA, MIT**). (CITIT)
   - **Diferență importantă:** tinygrad ia **ultima** semnătură (`signature[-0x180:]`), fără să citească siguranțele („fuse”) plăcii.
     Noi avem în `fwsec.rs` formula de alegere după siguranță (DEDUS din nouveau). Pe plăcile lor merge varianta simplă; pe placa noastră
     e de comparat — **nu ghicim, notăm la testul 5c ce index ar alege formula noastră și câte semnături sunt**. (CITIT + DEDUS)
7. **Imaginile semnate (FWSEC, Booter) stau în VRAM, nu în RAM.** tinygrad le scrie în VRAM prin fereastra BAR1 (`_alloc_boot_mem(..., sysmem=False)`)
   și le trage în falcon cu DMA din memoria plăcii (`FBIF_TRANSCFG target=0`, comentariul lor: „target=0 is FB (not in published headers)”),
   în bucăți de 256 de octeți (ip.py ~l. 212–248). `RESEARCH_I4_I8.md` §0.2 presupune DMA din RAM pentru I6. (CITIT)
   → DEDUS (NEVERIFICAT pe placă): pentru I6 s-ar putea să nu fie nevoie ca placa să citească din RAM-ul calculatorului; doar scrieri prin BAR1.
   tinygrad pornește totuși „Bus Master” de la început (nvdev.py ~l. 107), deci nu au testat varianta fără.
8. **Regiunile din VRAM — cifre de comparat cu `fb_layout.rs`.** tinygrad (ip.py ~l. 447–453) pune pentru Ampere: VGA 1 MiB la capătul VRAM
   (fix, nu citește registrul `0x625f04`), FRTS 1 MiB sub el, apoi bootloader, imaginea GSP aliniată la 64 KiB, heap GSP **fix `0x8100000` (129 MiB)**,
   început WPR la aliniere de 1 MiB, heap non-WPR 1 MiB. Și verifică (`assert`) că offset-ul FRTS dat lui FWSEC = cel din `GspFwWprMeta`.
   Noi calculăm heap-ul cu formula LIBOS3 din nova; **un test care compară cele două rezultate pentru 8 GiB e ieftin și util**. (CITIT + DEDUS)
9. **Cozile RPC — formatul exact** (ip.py ~l. 19–91, 364–387; antete NVIDIA `msgq_priv.h`, `rpc_global_enums.h`):
   o zonă în RAM = tabelă de pagini (lista adreselor fizice ale paginilor) + coada de comenzi (0x40000) + coada de stare (0x40000);
   antet `msgqTxHeader` (versiune 0, mărime 0x40000, `entryOff` 0x1000, `msgSize` 0x1000, `msgCount` 63, `flags` 1);
   fiecare mesaj = antet de element (număr de sloturi, nr. de secvență, **sumă de control = XOR al cuvintelor de 64 de biți, pliat hi^lo**)
   + antet RPC de 0x20 octeți (semnătură, `header_version 3<<24`, funcția) + date; mesaje mari → „continuation records” după 16 sloturi;
   „soneria” = scrierea `NV_PGSP_QUEUE_HEAD(0)=0`. Coada de stare e inițializată de GSP (se așteaptă `entryOff == 0x1000`).
   Numerele funcțiilor (NVIDIA, CITIT): `GSP_SET_SYSTEM_INFO 72`, `SET_REGISTRY 73`, `GSP_RM_CONTROL 76`, `GSP_RM_ALLOC 103`,
   evenimente `GSP_INIT_DONE 0x1001`, `GSP_RUN_CPU_SEQUENCER 0x1002`. **Totul e aritmetică pură → testabil pe simulare acum.**
10. **„Secvențiatorul”**: în timpul pornirii, GSP-ul cere driverului să execute mici comenzi (scrie registru, modifică, așteaptă, pauză,
    salvează, reset falcon, pornește, așteaptă oprire, „reia”) — 9 coduri, 0–8 (ip.py ~l. 629–661). Mic, dar obligatoriu. Fiecare cerere e o
    **scriere în placă pe care o decide firmware-ul** → la noi trebuie să treacă prin aceeași listă de permisiuni și jurnal. (CITIT + DEDUS)
11. **După `INIT_DONE` mai e un pas pe care documentația noastră nu-l are: „golden image”.** tinygrad (ip.py ~l. 468–508) creează, ca client
    privilegiat: dispozitiv, subdispozitiv, spațiu de adrese, citește tabela de motoare (runlist-uri), un canal, „promovează” bufferele de context
    grafic (dimensiunile cerute de la RM) și alocă obiectele compute + copiere. Abia apoi canalele „normale” merg. (CITIT; de ce e nevoie: DEDUS —
    RM-ul are nevoie de un context de referință pentru motorul GR.) → **de adăugat ca pas explicit între I8 și I9.**
12. **Tabelele de pagini ale GPU-ului le face driverul, nu GSP-ul.** tinygrad își construiește singur tabelele (MMU v2, 5 niveluri, pagini 4K/64K/2M,
    nvdev.py ~l. 32–66, 132–143; formatele din antetul NVIDIA `hwref/turing/tu102/dev_mmu.h`) și îi spune lui RM unde sunt, prin RPC
    `SET_PAGE_DIRECTORY` (ip.py ~l. 594). E o bucată nouă de lucru pentru I9, pe care `gpu-memory` o poate modela aritmetic. (CITIT)

**Despre canal și lansare (I9–I10)**

13. **Soneria `0xBB0090` e confirmată.** `docs/GA104_INITIALIZATION.md` §6 o avea „dedusă”. tinygrad mapează BAR0 de la `0xbb0000` (ops_nv.py ~l. 539)
    și scrie jetonul canalului la `+0x90` (~l. 653). Jetonul primit de la GSP conține doar numărul canalului; **driverul adaugă `runlist << 16`**
    (ip.py ~l. 588–591). (CITIT)
14. **Intrarea GPFIFO — o diferență de verificat.** tinygrad pune bitul 41 (= bitul 9 din cuvântul 1 = `GP_ENTRY1_LEVEL`, `SUBROUTINE` în `clc56f.h`)
    la fiecare intrare (ops_nv.py ~l. 97). `push.rs` al nostru îl lasă 0 (`MAIN`). Ambele pot fi corecte; pentru primul test real e mai sigur
    să copiem varianta deja dovedită (NECUNOSCUT de ce o folosesc). (CITIT + DEDUS)
15. **Cea mai scurtă lansare de calcul** (NAK `hw_runner.rs` ~l. 464–508, 663–677; tinygrad ops_nv.py ~l. 618–620, 178–181):
    o singură dată: `SET_OBJECT` (clasa compute), ferestrele de memorie locală/partajată, memoria locală; la fiecare lansare:
    `SEND_PCAS_A` (adresa QMD >> 8) + `SEND_SIGNALING_PCAS2_B`. Diferență: NAK folosește acțiunea `INVALIDATE_COPY_SCHEDULE`, tinygrad
    `PREFETCH_SCHEDULE`. Semnalul de terminare poate sta **chiar în QMD** (`release0`), fără metodă separată. Pe Ampere tinygrad folosește
    descrierea QMD **V03_00 din `clc6c0qmd.h`** (256 de octeți) chiar și cu clasa C7C0. (CITIT)
16. **NAK dă „cod brut + o fișă”, nu un fișier CUDA.** `compiler_mesa.py` ~l. 67–73: ieșirea = `nak_shader_info` (nr. de registre, memorie partajată,
    memorie locală) + codul SASS. QMD-ul se umple din fișă. Argumentele programului se citesc din „constant buffer 0”. Pentru SM86: 48 de warp-uri
    pe SM (~l. 56). **Exact ce ne trebuie pentru „încărcătorul” din `TOOLCHAIN.md`**, fără ELF/cubin. (CITIT)

**Despre teste și matmul**

17. **Programe scrise direct în IR-ul NAK, fără NIR/GLSL**: `hw_tests.rs` `TestShaderBuilder` (~l. 53–200) construiește un program cu câteva
    instrucțiuni, îl compilează și compară rezultatul de pe placă cu calculul pe CPU (`test_foldable_op`). Aceeași idee ca oracolul nostru
    `gpu-compute::reference`. `nvdisasm_tests.rs` verifică fiecare codificare cu dezasamblorul NVIDIA. (CITIT)
18. **Tensor cores în NAK: doar f16 pe Ampere.** `from_nir.rs` ~l. 4090–4110: `OpHmma` cere ca A și B să fie `FLOAT16`; bf16 apare în codificator
    doar pentru SM90+ (`sm70_encode.rs` ~l. 1189). → Pentru greutățile bf16 ale lui Kronos, primul matmul trebuie să meargă pe f32 obișnuit:
    bf16 → f32 e o simplă deplasare cu 16 biți (exactă). (CITIT + DEDUS)
19. **Trepte de matmul măsurate pe Ampere** (siboehm, A6000 = GA102): naiv 1,3 % din cuBLAS; acces „coalesced” 8,5 %; memorie partajată 12,8 %;
    1D blocktiling 36,5 %; 2D blocktiling 68,7 %; warptiling 93,7 %. Treapta 2 (o linie de cod schimbată) dă ×6. (CITIT în README)
20. **Atenție la „bit cu bit”:** compilatoarele GPU contopesc `a*b + c` într-o singură instrucțiune FFMA (o singură rotunjire), iar oracolul
    nostru pe CPU face două rotunjiri. Rezultatul matmul **nu va fi identic bit cu bit** decât dacă (a) cerem compilatorului să nu contopească
    (în NIR există marcajul „exact”; NEVERIFICAT cum îl respectă NAK) sau (b) adăugăm în `gpu-compute` un oracol cu FMA. Adunarea a 64 de f32
    nu are problema asta (de aceea e un prim program bun). (DEDUS)

---

## 3. Propuneri (ordonate după câștig/cost — cele mai bune primele)

### A. „Proba de referință” pe placa reală, în 30 de minute — înainte să scriem I4–I8
**Ce e.** Într-o fereastră cu Adrian de față, pe workstation, pornim de pe un stick cu Linux (nu Cyber Universe) și rulăm **driverul tinygrad**
(Python, MIT) pe RTX 3070 Ti, cu jurnalizarea fiecărei scrieri în registre activă (`NV_DEBUG=4` tipărește `wreg: adresă = valoare`,
nvdev.py ~l. 91–93) și `DEBUG=3` (tipărește fiecare RPC). Facem un singur calcul mic (o adunare). Salvăm jurnalul pe stick.
**De ce e mai bună.** Răspunde, înainte de luni de muncă, la întrebarea mare: *merge 570.144 pe placa ASUS cu VBIOS 94.04.65.00.3e?*
Și ne dă un **„jurnal de aur”**: lista exactă de scrieri, în ordine, cu care placa noastră a pornit. Driverul nostru se compară apoi cu el, pas cu pas,
întâi în simulare. E observarea propriului nostru driver, nu desfacerea firmware-ului (regula §2.1.3 rămâne respectată).
**Plan pe minute (DEDUS):**
- 0–5: Kronos oprit și salvat; pornire de pe stick-ul Linux (nouveau dezactivat la pornire); **ecranul se va stinge când tinygrad preia placa**
  (i9-10980XE nu are placă video integrată, RTX-ul ține ecranul) → comenzile se dau prin SSH de pe laptopul ThinkPad sau dintr-un script care
  scrie totul pe stick și repornește singur.
- 5–10: doar citiri (aceleași ca I0–I3 + cele noi): `BOOT_0`, `BOOT_42`, GFW_BOOT, `WPR2_ADDR_HI` (lecția 5), `USABLE_FB_SIZE_IN_MB` (lecția 4),
  semnătura VBIOS. Le notăm.
- 10–20: rularea tinygrad (adunarea), jurnal pe stick.
- 20–25: repornire în Windows, verificare `nvidia-smi` și Kronos.
- 25–30: copierea jurnalului în hub (`rezultate/`).
**Cost.** ~1 sesiune de pregătire (stick + script + instrucțiuni exacte), 30 de minute de fereastră.
**Primul pas mic testabil pe simulare.** Un parser `tools/` care citește un jurnal în formatul tinygrad și îl transformă în lista
`(adresă, valoare)` pe care o poate reda `gpu-sim::SimMmio` — testat cu un jurnal scris de mână.
**Riscuri.** Ecran negru până la repornire (așteptat); un reset PCI dacă WPR2 era deja ridicat (tinygrad îl face singur); cere Python și
instalarea tinygrad pe stick (cod străin rulat pe placă — decizia lui Adrian). Placa nu se poate „strica” prin software în mod obișnuit, dar
asta rămâne o **scriere în placa reală → doar cu Adrian de față**, ca orice alt test.

### B. Antete NVIDIA 570.144 → structuri Rust generate, cu teste de mărime și poziție
**Ce e.** Pe gazdă (nu în OS), o unealtă care citește antetele MIT ale NVIDIA de la eticheta `570.144` (lista exactă e deja făcută de tinygrad în
`tinygrad/runtime/autogen/__init__.py` ~l. 72–103 și `autogen/nv_regs/__init__.py`) și produce un crate `nvidia-rm570` cu: registrele falcon/GSP/SEC2,
`GspFwWprMeta`, `msgqTxHeader`, antetele RPC, `GspSystemInfo`, `PACKED_REGISTRY_*`, QMD V03_00, metodele C56F/C6C0. Fiecare structură are un test
de mărime și de poziție a câmpurilor. Fișierele generate poartă notificarea MIT a NVIDIA.
**De ce e mai bună.** Înlocuiește „citit de mână din antete” (sursă de greșeli la I5–I10) cu valori luate automat din specificația oficială; rezolvă
direct necunoscuta din `RESEARCH_I4_I8.md` §3. Riscul „ABI-ul RPC r570 citit greșit” din `RISKS.md` scade mult.
**Cost.** Mic–mediu: 1–2 sesiuni (unealtă + primele 10 structuri). Fără nicio scriere în placă.
**Primul pas mic.** Doar `GspFwWprMeta` + `msgqTxHeader`: generate, cu test „mărimea = X octeți, `magic` la offset 0 = `0xdc3aae21371a60b3`,
`revision` = 1” (valori CITITE în `gsp_fw_wpr_meta.h`).
**Riscuri.** Unealta de generare (bindgen/clang) trăiește doar pe gazdă; trebuie fixată versiunea. Regula clean-room a OS-ului cere „scriere proprie
după specificație” — antetele *sunt* specificația și sunt MIT, dar **Adrian confirmă că generarea din ele e acceptată** (recomandarea mea: da).

### C. Calea tinygrad ca „schelet” pentru I4–I10 (drumul cel mai scurt până la primul calcul)
**Ce e.** Rescriem în Rust, pas cu pas, secvența din tinygrad (lecțiile 1–16), folosind-o ca specificație: fiecare funcție a lor devine un pas al
nostru, cu `HardwarePermit`, limită de timp și jurnal. Ordinea: FWSEC (I6) → RISC-V + mailbox → Booter (I7) → cozi + `SetSystemInfo`/`SetRegistry`
+ secvențiator (I8) → **golden image (pas nou, „I8b”)** → tabele de pagini + canal (I9) → QMD + lansare (I10).
**De ce e mai bună.** În loc să reconstituim din nouveau (C, mult mai mare și pentru mai multe generații; mărimea exactă NEVERIFICATĂ) și nova (GPL, nu se poate folosi), avem ~1 100 de rânduri de
Python **MIT, care rulează pe aceeași familie de plăci și aceeași versiune de firmware**. ESTIMARE: 3 500–5 500 de rânduri Rust pentru I4–I10,
față de 6 000–10 000 doar pentru I6–I8 în estimarea din `RESEARCH_I4_I8.md` §4; și mai puține sesiuni pe placă, pentru că pașii sunt deja dovediți.
**Cost.** Mare în total (săptămâni), dar împărțit în bucăți mici, fiecare testabilă întâi pe simulare.
**Primul pas mic testabil pe simulare.** Codificarea și decodificarea unui mesaj RPC (lecția 9): suma de control XOR, numărul de sloturi, înfășurarea în
coada circulară, „continuation records”. Test: un mesaj `SET_REGISTRY` cu cele două intrări folosite de tinygrad (`RMForcePcieConfigSave=1`,
`RMSecBusResetEnable=1`) se codifică și se decodifică identic; un mesaj de 20 de sloturi se rupe corect în 16 + continuare.
**Riscuri.** (1) Licența: MIT permite și portarea directă cu atribuire; dacă Adrian vrea „scriere proprie”, o tratăm ca pe o specificație și notăm
sursa în PROVENANCE. (2) tinygrad e cod de cercetare: unele valori sunt „magice” (ex. `flags=0x200320`, `internalFlags=0x1a` la canal, ip.py ~l. 490)
— le notăm ca „dovedite empiric, neexplicate”. (3) tinygrad presupune Linux (pagini fixate, `pagemap`); la noi echivalentul e `gpu-memory::dma`.

### D. Un „procesor de comenzi Ampere” și un „GSP fals” în `gpu-sim`
**Ce e.** Două modele noi, ambele doar pentru teste pe gazdă:
1. **Procesorul de comenzi** (după `test/mockgpu/nv/nvgpu.py`, ~l. 21–206): citește inelul GPFIFO, pushbuffer-ul (antet: tip 28–30, număr 16–28,
   subcanal 13–15, metodă), execută `SEM_EXECUTE` (release / acquire ≥), `SEND_PCAS_A` + `PCAS2_B`, citește QMD-ul și „rulează programul” chemând
   backend-ul CPU din `gpu-compute` (programul e recunoscut după amprenta lui), apoi scrie semaforul `release0`.
2. **GSP-ul fals** (după ideea `MockPSP`/`MockSMU` din `test/mockgpu/am/amgpu.py`): un mic automat pe registre care răspunde la reset falcon,
   „scrubbing” terminat, mailbox, scrie `WPR2_ADDR_HI` după FWSEC, inițializează coada de stare și trimite `INIT_DONE` + o cerere de secvențiator.
**De ce e mai bună.** Azi `push.rs` e „codificare niciodată executată” (RISKS.md). Cu D, întregul lanț — de la operatorul Kronos la semaforul
de terminare — rulează în CI, inclusiv cazurile rele: GSP care nu răspunde (limita de timp), sumă de control greșită, coadă plină, semafor care nu vine.
**Cost.** Mediu: ~2–3 sesiuni pentru (1), ~2–3 pentru (2).
**Primul pas mic.** (1) cu un singur „program”: adunarea a 64 de f32; test: push + QMD construite de noi → modelul scrie rezultatul identic cu
`reference::add` și semaforul ajunge la valoarea așteptată.
**Riscuri.** Modelul spune doar că suntem **consecvenți cu noi înșine**; nu dovedește că placa face la fel. De aceea D se leagă de A: modelul trebuie
să reproducă jurnalul de aur.

### E. Unealta NAK pe gazdă + scara matmul pentru Kronos
**Ce e.** Un program pe gazdă (Rust, legat de Mesa) care scrie fiecare nucleu direct în IR-ul NAK (ca `TestShaderBuilder` din `hw_tests.rs`) sau
în NIR, îl compilează pentru SM86 și scrie un fișier de date al nostru: fișa (registre, memorie partajată/locală, mărimea grupului, așezarea
constant buffer 0) + codul brut. Driverul doar îl încarcă și umple QMD-ul (lecțiile 15–16). Nucleele, în ordine:
`add64` (primul calcul) → matmul naiv f32 → „coalesced” → cu memorie partajată → 2D blocktiling (≈ 69 % din cuBLAS pe Ampere) →
varianta cu greutăți bf16 (despachetare prin deplasare, lecția 18).
**De ce e mai bună.** Evită complet ELF/cubin și orice unealtă NVIDIA; fiecare nucleu are oracolul lui pe CPU deja scris (`gpu-compute`). Treptele
siboehm dau o țintă măsurabilă la fiecare pas.
**Cost.** Mediu: unealta 2–3 sesiuni (cea mai mare problemă: construirea Mesa pe gazdă); fiecare treaptă de matmul 1–2 sesiuni.
**Primul pas mic testabil fără placă.** Unealta produce `add64` și un test verifică fișa (ex. „registre ≤ 16, mărime grup 64”); dezasamblat
cu `nvdisasm` (unealtă NVIDIA, doar pe gazdă, doar ca verificare — ca `nvdisasm_tests.rs`) sau cu dezasamblorul NAK. Apoi rulat în modelul D.
**Riscuri.** API-ul intern Mesa se schimbă (fixăm un commit); politica „exact” vs FFMA (lecția 20) trebuie decisă înainte de matmul;
tensor cores bf16 nu sunt disponibile prin NAK pe Ampere (lecția 18) — performanța maximă vine mai târziu.

---

## 4. Ce NU merită (și de ce)

- **gdev, PSCNV, „nouveau compute” vechi:** scrise pentru plăci de dinaintea GSP (Fermi/Kepler), când driverul vorbea direct cu motoarele.
  Pe Ampere totul trece prin GSP-RM; nimic de acolo nu se aplică.
- **envytools ca sursă de valori pentru Ampere:** baza de registre și documentația se opresc în mare înainte de Turing; ultimul commit e din 2023.
  Bun doar pentru *concepte* (falcon, pushbuffer). Antetele NVIDIA 570.144 sunt mai bune și oficiale.
- **mmiotrace / `demmio` pe driverul NVIDIA:** cere Linux cu driverul NVIDIA, oprește celelalte procesoare, prinde doar zonele mapate în timpul urmei
  și ar însemna să observăm driverul proprietar. Jurnalul tinygrad (propunerea A) dă același lucru, mai simplu și de la un driver MIT.
- **CUTLASS ca cod:** C++/CUDA cu șabloane, are nevoie de `nvcc`; partea nouă (DSL-urile) e sub EULA NVIDIA, nu BSD. Doar idei de împărțire în blocuri.
- **Tensor cores bf16 acum:** NAK nu le expune pe Ampere (doar HMMA cu f16). Ar cere `ptxas` (decizie amânată de Adrian) sau un codificator propriu.
- **Un asamblor SASS propriu:** codificarea nu e documentată oficial; ar fi o copie a lui NAK cu alt nume. NAK pe gazdă e alegerea corectă.
- **Calea fără GSP (ACR/SEC2 + FECS/GPCCS):** tot firmware semnat, mai puțin documentată, iar acum avem o cale GSP dovedită (tinygrad).
- **Macro-ul `versions` din Asahi:** elegant, dar avem o singură versiune fixată (570.144). Devine util doar dacă vreodată schimbăm firmware-ul.
- **Codul nova-core:** GPL — doar ordinea pașilor; în plus, după Phoronix (8 oct 2026) încă nu rulează calcul, deci tinygrad e oricum mai avansat
  pentru ce ne trebuie.
- **Rularea codului tinygrad în Cyber Universe OS:** e Python și depinde de Linux; folosim tinygrad ca hartă (C) și ca probă pe Linux (A), nu ca dependență.

---

## Surse citite (pentru PROVENANCE, dacă se adoptă ceva)
- tinygrad `f5b17be`: `tinygrad/runtime/support/nv/nvdev.py`, `support/nv/ip.py`, `runtime/ops_nv.py`, `support/compiler_mesa.py`,
  `support/system.py` (l. 98–262), `autogen/__init__.py` (l. 60–103), `autogen/nv_regs/*.py`, `extra/nv_gpu_driver/{vbios,fw,hs}.h`
  (antete NVIDIA MIT / adaptate din nouveau, MIT), `test/mockgpu/nv/nvgpu.py`, `test/mockgpu/am/amgpu.py`, `support/am/amdev.py` (structură), `docs/tinygpu.md`.
- NVIDIA open-gpu-kernel-modules `570.144`: `COPYING`, `src/common/inc/swref/published/ampere/ga102/{dev_falcon_v4,dev_falcon_v4_addendum,dev_gsp,dev_gc6_island,dev_gc6_island_addendum}.h`,
  `.../turing/tu102/dev_fb.h`, `src/nvidia/arch/nvalloc/common/inc/gsp/gsp_fw_wpr_meta.h`, `src/common/shared/msgq/inc/msgq/msgq_priv.h`,
  `src/nvidia/inc/kernel/vgpu/rpc_global_enums.h`, `src/common/sdk/nvidia/inc/class/clc56f.h`.
- Mesa `8e3dba4`: `src/nouveau/compiler/nak/{qmd,hw_runner,hw_tests,nvdisasm_tests,ir,from_nir,sm70_encode}.rs`, `nak_nir_lower_cmat.c`.
- envytools `f102b82`: `COPYING`, `README.rst`, `docs/hw/falcon/xfer.rst`, `docs/hw/fifo/dma-pusher.rst`.
- siboehm/SGEMM_CUDA: `LICENSE`, `README.md`, `src/kernels/1_naive.cuh`, `2_kernel_global_mem_coalesce.cuh`.
- CUTLASS: `LICENSE.txt`, `EULA.txt` (început). gdev: `LICENSE.txt`. open-gpu-doc: `LICENSE.md`.
- Web: Phoronix „Nova Driver Continues Progressing…” (8 oct 2026); LKML „rust: macros: Add versions macro” (Asahi Lina, mar. 2023);
  documentația mmiotrace (copie stuff.mit.edu).
