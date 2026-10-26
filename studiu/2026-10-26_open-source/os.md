# Studiu: alte sisteme de operare și componente, ca inspirație pentru Cyber Universe OS

Data: 2026-10-26. Autor: Claude (cercetare, fără nicio modificare în vreun repo).
Starea Cyber Universe citită: `main` la `0a76f8e` (după P6-20, Release `os-190`), fișierele `README.md`, `docs/DECISIONS.md`,
`docs/ROADMAP.md`, `docs/STATE.md`, `docs/TASKS.md`, `docs/CLEAN_ROOM.md`, `docs/ARCHITECTURE.md`, `docs/METRICS.md`,
`docs/research/STUDIU-P0-P1.md`, plus `kernel/src/syscall/README.md` și câteva fișiere de cod (heap, alocatorul de cadre,
planificatorul, `drivers/rtl8168.rs`, `power.rs`, `shell/mod.rs`, `tools/test.sh`, `tests/scenarios.txt`).

**Cum să citești notițele:** „[citit: …]” = am văzut eu fișierul/secțiunea respectivă (calea e din repo-ul acelui proiect,
la commit-ul din tabel). „[dedus]” = concluzia mea, neverificată practic. Nu am rulat niciun cod descărcat.

Câteva cuvinte explicate o dată:
- **unsafe** = cod Rust în care compilatorul nu mai poate garanta că memoria e folosită corect; trebuie verificat de om.
- **DMA** = placa (rețea, USB) scrie/citește direct în memoria RAM, fără procesor. „Cache” = copia rapidă a memoriei din procesor;
  dacă nu e golită la momentul potrivit, procesorul vede date vechi (exact problema „cadrele 2+ citite ca zero” de la Realtek).
- **TLB** = memoria procesorului pentru traducerea adreselor; **pagini mari** (2 MiB, 1 GiB) = mai puține traduceri, calcul mai rapid pe date mari.
- **fuzzing** = un program care dă la întâmplare mii de intrări ciudate unei funcții și caută căderi.
- **unikernel** = aplicația și nucleul compilate împreună într-un singur program care pornește direct pe mașină.

---

## 1. Tabel: ce am studiat

| Proiect | Link (commit studiat) | Licență (din fișierul LICENSE) | Ce am învățat (concret) | Unde se aplică la Cyber Universe | Cod folosibil? |
|---|---|---|---|---|---|
| **Theseus OS** | github.com/theseus-os/Theseus (`1fbfe56`) | MIT (`LICENSE-MIT`) | Testele în QEMU: o singură pornire rulează **toate** aplicațiile `test_*` una după alta și iese cu codul 0x11 prin `isa-debug-exit` [citit: `applications/qemu_test/src/lib.rs`, `Makefile` ținta `test:`]. `MappedPages` = o zonă mapată e un obiect Rust; când dispare, se demapează singură [citit: `kernel/memory/src/paging/mapper.rs`]. Heap per nucleu (slab-uri de 8 B…8 KiB) [citit: `kernel/multiple_heaps/src/lib.rs`]. Totul rulează în ring 0, izolarea vine doar din limbaj [citit: `book/src/design/idea.md`]. | Testare (propunerea 2); idee de heap per nucleu pentru Kronos pe multe nuclee. | Da, cu atribuire (MIT) — dar recomand doar idei. |
| **Asterinas** (framekernel, OSTD) | github.com/asterinas/asterinas (`3ed4fc4`) | **MPL-2.0** (`LICENSE-MPL`) | Tot codul `unsafe` stă într-un singur strat (OSTD); restul nucleului și driverele au `#![deny(unsafe_code)]` [citit: `kernel/src/lib.rs`, `kernel/comps/*/src/lib.rs`, `ostd/README.md`]. Teste `#[ktest]` strânse într-o secțiune de linker și rulate după pornire, cu `should_panic` [citit: `ostd/libs/ostd-test/src/lib.rs`]. DMA cu **tip de direcție** (`ToDevice`/`FromDevice`) și apeluri obligatorii `sync_to_device`/`sync_from_device` [citit: `ostd/src/mm/dma/dma_stream.rs`]. Acoperirea codului (coverage) scoasă la oprire [citit: `ostd/src/coverage.rs`]. | Propunerea 2 (teste într-o pornire), propunerea 5 (DMA cu tip). | **Doar idei.** MPL-2.0 e „copyleft pe fișier”: un fișier copiat rămâne MPL. Nu e GPL, dar complică regula „totul MIT”. |
| **ArceOS** | github.com/arceos-org/arceos (`8d2e6f9`) | Triplă: GPL-3.0-or-later **SAU** Apache-2.0 **SAU** MulanPSL-2.0 (`Cargo.toml`, fișierele LICENSE.*) | Componentele se aleg la compilare din „features”: alocator `tlsf`/`slab`/`buddy`, planificator `fifo`/`rr`/`cfs`, `smp`, `net`, `fs` [citit: `api/axfeat/Cargo.toml`]. Coadă de sarcini **per nucleu**, cu mască de nuclee permise (`cpumask`) [citit: `modules/axtask/src/run_queue.rs`]. | Propunerea 3 (fixarea firelor Kronos pe nuclee). | Se poate alege Apache-2.0 → cod folosibil cu atribuire; recomand doar idei. |
| **Hubris** (Oxide) | github.com/oxidecomputer/hubris (`6676910`) | **MPL-2.0** (`LICENSE.txt`) | Nucleul nu repornește nimic; un „supraveghetor” (`jefe`) primește căderile sarcinilor și le repornește [citit: `doc/tasks.adoc`, `task/jefe/src/main.rs`]. „Livrare întreagă”: se livrează doar imaginea testată în întregime, nu bucăți [citit: `doc/intro.adoc`]. Jurnale circulare per modul, cu numărare și eliminarea dublurilor (`ringbuf`) [citit: `lib/ringbuf/src/lib.rs`]. | Propunerea 1 (cutia neagră). Confirmă regula voastră D-013 și Release-urile păstrate. | Doar idei (MPL-2.0). |
| **Tock** | github.com/tock/tock (`0ab8b44`) | MIT **sau** Apache-2.0 | Nucleul nu ia dependențe externe, cu excepții aprobate și documentate [citit: `doc/ExternalDependencies.md`]. „Grants”: memoria de care nucleul are nevoie pentru un program e luată din cota acelui program [citit: `kernel/src/grant.rs`]. Teste automate pe plăci reale prin CI (Treadmill) [citit: `doc/TockHardwareCI.md`]. | Propunerea 4 (limite per program); idee de teste pe hardware la distanță. | Da, cu atribuire; recomand doar idei. |
| **Redox OS** (nucleul) | github.com/redox-os/kernel (`b68957d`) | MIT | „Scheme”: resursele se deschid ca adrese (`disk:`, `irq:`) [citit: `src/scheme/mod.rs`]. **Încuietori pe niveluri** L1…L5 verificate la compilare: nu poți lua o încuietoare de nivel mic ținând una de nivel mare → fără blocaje reciproce [citit: `src/sync/ordered.rs`, adaptat din crate-ul MIT `ordered-locks`]. NUMA din ACPI SRAT [citit: `src/numa.rs`]. | Propunerea 5 (după K6-02b aveți multe încuietori: heap, cadre, DMA, pagini, jurnal, serial, intrare). | Da, cu atribuire (MIT); recomand să scriem varianta noastră. |
| **Redox Orbital** (ferestre) | github.com/redox-os/orbital | MIT | Server de ferestre de ~4.500 de rânduri, în spațiul utilizator; aplicațiile primesc un buffer și îl trimit [citit: `README.md`, structura `src/`]. | Confirmă că serverul vostru de ferestre (în nucleu, ~ aceeași idee) e de mărime potrivită. | Doar idei. |
| **Hermit** (unikernel) | github.com/hermit-os/kernel (`9a75584`) | MIT **sau** Apache-2.0 | Mapează heap-ul cu pagini de 2 MiB până la o graniță de 1 GiB, apoi cu **pagini de 1 GiB** dacă procesorul le are [citit: `src/mm/mod.rs`, ~r. 117–180]. Folosește `talc` și `smoltcp` [citit: `Cargo.toml`]. | Propunerea 3 (pagini de 1 GiB pentru greutățile modelului). | Da, cu atribuire; recomand doar idei. |
| **talc** (alocator) | github.com/SFBdragon/talc (`4a547f5`) | MIT (`LICENSE.md`) | Alocator „pe coșuri” (binning, ca TLSF): un bit per coș spune unde e loc → aproape timp constant; heap-uri multiple; contoare; **testat cu fuzzing** pe liste de acțiuni alocare/eliberare [citit: `talc/src/base/INTERNALS.md`, `fuzz/fuzz_targets/`]. | Heap-ul vostru e „first-fit” pe o listă sortată (timp crește cu fragmentarea) [citit: `kernel/src/mem/heap.rs`]. Propunerea 2 (fuzzing). | Da, cu atribuire (MIT). Recomand idei + test de fuzzing pe heap-ul nostru. |
| **linked_list_allocator** | github.com/rust-osdev/linked-list-allocator | MIT **sau** Apache-2.0 | Același tip de alocator ca al vostru (listă de blocuri libere). | Doar comparație. | Nu e nevoie. |
| **smoltcp** (TCP/IP) | github.com/smoltcp-rs/smoltcp (`24bda3b`) | **0BSD** (cea mai liberă) | Stivă fără heap; listă cinstită cu ce **nu** suportă (ex. SACK); `FaultInjector` = pierde/strică pachete la întâmplare, limitează viteza; `PcapWriter` = salvează traficul pentru Wireshark; fuzzing pe parsere [citit: `README.md`, `src/phy/fault_injector.rs`, `fuzz/fuzz_targets/`]. | Stiva voastră e în `kernel/src/net/` și se testează doar în QEMU [citit: `kernel/src/net/tcp.rs`]. Propunerea 2. | Juridic da (0BSD). Dar ar încălca „≥ 90 % propriu” → **doar idei** (injectorul de erori). |
| **acpi** (crate) | github.com/rust-osdev/acpi (`4841ccb`) | MIT **sau** Apache-2.0 (`LICENCE-*`) | Interpretorul AML (codul din tabelele DSDT/SSDT) are ~6.800 de rânduri [citit: `src/aml/*.rs`, numărat cu `wc`]. | Aveți MADT și FADT; nu aveți oprire (S5) [citit: `kernel/src/power.rs` — doar repornire]. | Ar fi folosibil cu atribuire, dar e mare; vezi „Ce NU merită”. |
| **Managarm** | github.com/managarm/managarm (`7917bc3`) | MIT (`LICENSE`) | Microkernel complet asincron; suite separate `kernel-tests`, `kernel-torture`, `kernel-bench`; server GDB în nucleu [citit: `README.md`, `testsuites/`, `kernel/thor/generic/gdbserver.cpp`]. | Idee de „test de tortură” separat de testele normale (voi aveți deja `stress.yml`). | Doar idei (e C++). |
| **blog_os** (Phil Opp) | github.com/phil-opp/blog_os | MIT **sau** Apache-2.0 | Testele care trebuie să cadă (panică) trebuie rulate ca programe separate („no harness”) [citit: `blog/content/edition-2/posts/04-testing/index.md`, secțiunile „Tests that Should Panic”, „No Harness Tests”]; trei feluri de alocatoare explicate [citit: `11-allocator-designs`]. | Propunerea 2: scenariile `panic`, `doublefault`, `pagefault` rămân porniri separate. | Doar idei. |
| **NIGHTRUN** | github.com/hardrave/NIGHTRUN (`cb1c2bb`) | MIT | Aplicație UEFI în Rust care pornește direct într-un chat cu un LLM local. Modelul se citește o dată în RAM cu verificare CRC în timpul citirii, apoi **discul e „sigilat”** (orice citire ulterioară = eroare); o arenă de memorie calculată la pornire → **zero alocări în bucla de generare**; nucleele secundare fac doar calcul; AVX pornit pe fiecare nucleu (XCR0 e per nucleu); teste de paritate token cu token față de llama.cpp; viteza de generare e limitată de lățimea de bandă a memoriei [citit: `docs/architecture.md`, `docs/benchmarks.md`, `crates/nr-boot/src/smp.rs`, `crates/nr-boot/src/modelload.rs`, `crates/nr-model/tests/parity.rs`]. Rămâne pe serviciile firmware-ului UEFI (nu are driver USB propriu). | Propunerea 3 (găzduirea lui Kronos). | Da, cu atribuire (MIT); recomand idei (voi aveți deja SMP, AVX, xHCI proprii). |
| **llama2.c** (Karpathy) | github.com/karpathy/llama2.c (`350e04f`) | MIT | ~970 de rânduri: greutățile se mapează doar-citire (`mmap`), memoria de lucru se alocă o dată, `matmul` e bucla fierbinte [citit: `run.c` r. 77–231]. | Model de „motor minim” pentru Kronos. | Da, cu atribuire. |
| **llama2.c „L2E”** (fork) | github.com/trholding/llama2.c | **Mixt**: originalul MIT, adăugirile L2E sub „L2E Non-Commercial Research License” [citit: `LICENSE`] | Pornirea bare-metal BIOS/EFI e marcată „not fully functional yet”; „L2E OS” folosește nucleul Linux [citit: `README.md` r. 178–232]. | Arată că „LLM bootabil” pur e greu; NIGHTRUN e exemplul mai bun. | **Nu** (licență necomercială pe adăugiri). |
| **SerenityOS** | github.com/SerenityOS/serenity | BSD-2-Clause | `pledge` (programul promite că folosește doar unele grupe de apeluri; dacă încalcă, e oprit) și `unveil` (lista de căi pe care le mai poate atinge, cu `r`/`w`/`c`/`x`/`b`) [citit: doar `Base/usr/share/man/man2/pledge.md`, `unveil.md`]. | Propunerea 4 (aplicația Claude și cheile de pe stick). | Doar idei (am citit doar documentația). |
| **Fuchsia / Zircon** | fuchsia.dev | (n-am verificat fișierul LICENSE) | Drepturile unui „mâner” (handle) pot doar să scadă la copiere; un obiect de memorie (VMO) cu MAP+READ fără WRITE = mapare doar-citire [citit: pagina fuchsia.dev „Rights”]. Pagina despre VMO n-am putut-o deschide (nepermisă în sesiune). | Propunerea 3 (obiectul „model” doar-citire, partajat). | Doar idei. |
| **seL4** | github.com/seL4/seL4 | Nucleul **GPLv2**, codul utilizator BSD-2 [citit: `LICENSE.md`] | — (doar licența) | — | **Doar idei, GPL.** |
| **Genode** | github.com/genodelabs/genode | **AGPLv3** + excepție de legare [citit: `LICENSE`] | — (doar licența) | — | **Doar idei, AGPL.** |
| **Maestro** | github.com/maestro-os/maestro | **AGPLv3** [citit: `COPYING`] | Nucleu Unix-like în Rust, ~30 % din apelurile Linux, alocator buddy [citit: `README.md`]. | — | **Doar idei, AGPL.** |
| Haiku, xv6, Plan 9, Unikraft, Slint | (doar licențe) | Haiku: majoritar MIT [`License.md`]; xv6: MIT; Plan 9: MIT (2021, Plan 9 Foundation) + fonturi sub Aladdin; Unikraft: BSD-3 per bibliotecă [`COPYING.md`]; **Slint: GPLv3 / gratuit-dar-fără-embedded / comercial** [`LICENSE.md`] | Codul lor **nu l-am citit** în această sesiune. | — | Slint: nu (vezi „Ce NU merită”). |

---

## 2. Lecții (notițe concrete, cu sursa)

1. **O pornire, multe teste.** Theseus rulează toate testele într-o singură pornire QEMU și iese cu un cod (0x11 = succes)
   [citit: Theseus `applications/qemu_test/src/lib.rs`]. Asterinas strânge funcțiile `#[ktest]` într-o secțiune a linker-ului și le
   rulează după inițializare [citit: Asterinas `ostd/libs/ostd-test/src/lib.rs`]. La voi: 75 de scenarii, ~47 de combinații de
   „features” diferite, deci ~47 de nuclee compilate și ~75 de porniri; un CI complet a durat ~18 minute în rulările din 23 oct.
   [citit: `tests/scenarios.txt`, `gh run list`].
2. **Testele cu panică rămân separate.** Un test care trebuie să cadă oprește tot nucleul, deci are nevoie de pornirea lui
   [citit: blog_os, capitolul 04-testing, „Tests that Should Panic” / „No Harness Tests”]. Scenariile `panic`, `doublefault`,
   `pagefault`, `unmapped`, `rodata` trebuie să rămână cum sunt.
3. **`unsafe` într-un singur loc.** Asterinas pune `#![deny(unsafe_code)]` în nucleu și în fiecare driver; doar OSTD are voie
   [citit: Asterinas `kernel/src/lib.rs`, `kernel/comps/uart/src/lib.rs`]. La voi: `crypto/`, `tls/`, `json/` au 0 `unsafe`, dar nu au
   interdicția scrisă; `rtl8168/` are 14 și `e1000e/` 12 locuri; nucleul are ~304 [numărat cu `grep`].
4. **DMA cu direcție în tip.** Asterinas: `DmaStream<ToDevice>` / `<FromDevice>` și sincronizare obligatorie înainte/după ce lucrează
   placa; crearea de buffere DMA cere întreruperi pornite (din cauza golirii TLB pe alte nuclee) [citit: Asterinas `ostd/src/mm/dma/`].
   La voi, `dma_sync` e o funcție simplă fără direcție [citit: `kernel/src/drivers/rtl8168.rs` r. 69–83] — iar greșelile de cache au
   costat P6-10c, P6-10f, P6-10g.
5. **Încuietori pe niveluri.** Redox verifică la compilare ordinea încuietorilor (L1…L5) → blocajele reciproce între ele devin
   imposibile [citit: Redox `src/sync/ordered.rs`]. Relevant după K6-02b, care a introdus încuietori pentru heap, cadre, paza DMA,
   tabele de pagini, jurnal, serial, cozile de intrare [citit: `docs/STATE.md`].
6. **Supraveghetor în afara nucleului.** În Hubris nucleul doar înregistrează căderea; „jefe” decide repornirea [citit: Hubris
   `doc/tasks.adoc` r. 99–146]. La voi, `modmgr` ar putea juca acest rol pentru module (pornire/oprire există deja) [dedus].
7. **Livrare întreagă.** Hubris livrează numai imaginea testată în întregime, pentru că actualizarea pe bucăți explodează numărul de
   combinații de testat [citit: Hubris `doc/intro.adoc`, „Holistic deployment”]. Exact ce face Release-ul vostru de stick + D-013.
8. **Jurnal circular per modul, cu contoare.** Hubris `ringbuf`: intrări mici, fiecare modul cu buffer-ul lui, dublurile se numără în
   loc să se repete [citit: Hubris `lib/ringbuf/src/lib.rs`]. La voi `log [cuvânt] [n]` filtrează un jurnal comun; rezultatele de pe
   hardware ajung la Claude prin **poze** [citit: `docs/DECISIONS.md` D-013, `docs/STATE.md` r. 390].
9. **Dependențe externe doar cu aprobare scrisă.** Tock ține lista excepțiilor aprobate și motivul [citit: Tock
   `doc/ExternalDependencies.md`]. Se potrivește cu dependența voastră pe `cyber-gpu` fixată pe commit (P6-19).
10. **Memoria nucleului „plătită” de program.** Tock „grants”: starea pe care nucleul o ține pentru un program vine din cota
    programului [citit: Tock `kernel/src/grant.rs`]. La voi heap-ul nucleului are o limită de 256 MiB comună tuturor [citit:
    `kernel/src/mem/heap.rs`, `HEAP_MAX`]; un program cu multe ferestre/socket-uri îl poate umple [dedus].
11. **Cozi per nucleu + mască de nuclee.** ArceOS pune fiecare sarcină pe o coadă aleasă din nucleele permise [citit: ArceOS
    `modules/axtask/src/run_queue.rs`]. La voi: o coadă comună pentru toate nucleele [citit: `kernel/src/sched/mod.rs`, antet].
    Pentru Kronos, „firul X stă pe nucleul Y” evită mutarea datelor din cache între nuclee [dedus].
12. **Pagini de 1 GiB.** Hermit folosește pagini de 1 GiB când procesorul le are [citit: Hermit `src/mm/mod.rs`]. La voi `mem_map`
    folosește 2 MiB (maximul) [citit: `kernel/src/syscall/README.md`, K6-03]; tabelele de pagini știu deja de nivelul de 1 GiB
    [citit: `kernel/src/mem/paging.rs` r. 231].
13. **Alocator pe coșuri + fuzzing.** talc caută loc folosind un bit per coș și e testat cu fuzzing pe secvențe aleatoare de
    alocări/eliberări [citit: talc `INTERNALS.md`, `fuzz/fuzz_targets/`]. Heap-ul vostru e first-fit, verificat azi doar prin testul de
    stres din QEMU [citit: `heap.rs`, `docs/METRICS.md`].
14. **Rețeaua testată cu erori injectate.** smoltcp are un „strat” care pierde, strică sau încetinește pachete la cerere și unul care
    salvează traficul ca `.pcap` [citit: smoltcp `src/phy/fault_injector.rs`, `pcap_writer.rs`]. Voi ați făcut deja tiparul „logica pe
    gazdă + model software” pentru `rtl8168/`, `e1000e/`, `tls/`, `crypto/`, dar nu și pentru `kernel/src/net/` [citit: structura repo].
15. **Motor AI bare-metal: încarcă o dată, sigilează, zero alocări.** NIGHTRUN: model citit în bucăți de 16 MB cu CRC în timpul citirii,
    discul sigilat după, arenă dimensionată la pornire, nicio alocare în bucla de generare, nucleele secundare fac doar calcul
    [citit: NIGHTRUN `docs/architecture.md`, „Boot flow”, „Memory model”].
16. **Paritatea cu referința e testul principal.** NIGHTRUN compară token cu token cu llama.cpp; voi faceți deja la fel la
    `kronos-calcul` (bit cu bit / toleranțe) [citit: NIGHTRUN `crates/nr-model/tests/parity.rs`; `docs/STATE.md` P6-19].
17. **Viteza unui LLM pe procesor e limitată de memorie, nu de calcul.** [citit: NIGHTRUN `docs/benchmarks.md`: „decode speed is
    limited by memory bandwidth”]. Consecință [dedus]: pentru Kronos pe workstation contează paginile mari, datele aliniate și
    fixarea firelor, mai mult decât încă un nucleu.
18. **Restrângerea drepturilor unui program, doar în jos.** SerenityOS `pledge`/`unveil`; Zircon: drepturile scad la copierea mânerului
    [citit: man2 `pledge.md`, `unveil.md`; fuchsia.dev „Rights”]. La voi orice program poate citi `/usb/claude.key` și
    `/usb/github.token` și poate instala module (apelul 21) [citit: `kernel/src/syscall/README.md` — nu există niciun model de permisiuni].
19. **AML costă mult.** Un interpretor AML complet are ~6.800 de rânduri [citit: crate-ul `acpi`, `src/aml`]. Oprirea calculatorului
    (S5) cere doar valorile `_S5` din DSDT, care se pot găsi fără interpretor complet [dedus, după tehnica descrisă public pe OSDev Wiki
    „Shutdown”; n-am recitit pagina azi].
20. **Teste pe hardware real la distanță există, dar cer infrastructură.** Tock folosește Treadmill (calculatoare-gazdă care controlează
    plăcile, alimentare, serial) [citit: Tock `doc/TockHardwareCI.md`]. Pentru voi e prea devreme; o variantă ieftină e propunerea 1.

---

## 3. Propuneri (ordonate după câștig / cost)

### Propunerea 1 — „Cutia neagră” pe stick (robustețe pe hardware real)
- **Ce e:** la fiecare pornire și la comanda `log salveaza`, OS-ul scrie pe stick un fișier text nou
  `/usb/jurnal/<release>-<nr>.txt` cu: `hw`, `log` (tot jurnalul din memorie), registrele cheie ale driverelor (`log rtl`, `log e1000`,
  `log usb`). Fiecare driver își ține propriul jurnal circular mic, cu contor pentru mesajele repetate (ideea din Hubris `ringbuf`).
  Opțional, la a doua etapă: `gh-trimite` urcă fișierul în `rezultate/` din hub.
- **De ce e mai bună:** acum rezultatele de pe laptop ajung prin poze (D-013 cere chiar „o poză”). Un fișier e complet, exact, se poate
  compara automat între Release-uri și nu depinde de cât încape pe ecran. Scade numărul de drumuri Adrian ↔ laptop.
- **Cost estimat:** 1–2 sesiuni (scrierea FAT32 și montarea stick-ului există deja: P4-07, P6-15).
- **Primul pas mic, testabil în QEMU:** comanda `log salveaza` → scrie `/usb/jurnal/test-1.txt`; scenariu nou `jurnal-stick` cu
  stick-ul de test (`test-usbdisk`, `disk=...`) și un `tools/after-jurnal-stick.sh` care verifică în imagine că fișierul există și
  conține „== raport hardware ==” (același tipar ca `after-fatwrite.sh`).
- **Riscuri:** scrierea pe stick în timp ce un driver e defect (de aceea: doar la comandă la început, nu automat; numai fișier nou, apoi
  `sync`); stick fără `cyber.rw` → mesaj clar, nu scriere. Scrierea în caz de panică NU în primul pas (driverul USB poate fi chiar el
  cauza). Respectă D-013: e o funcție nouă, nu schimbă comportamentul unui driver.

### Propunerea 2 — Testare mai rapidă și mai adâncă: „o pornire, multe teste” + teste pe gazdă cu fuzzing
- **Ce e:** (a) un registru de teste în nucleu (atribut/macro propriu care pune testele într-o secțiune `.cu_teste` a linker-ului, ca
  `#[ktest]` din Asterinas); un singur nucleu de test „toate” rulează toate testele care nu cad intenționat și scrie
  `teste: N trecute, M picate` pe serial. (b) Logica fără hardware din heap și din `kernel/src/net/` mutată treptat în biblioteci
  `no_std` testate pe gazdă (cum ați făcut la `rtl8168/`, `tls/`), cu un test de fuzzing pentru heap (acțiuni aleatoare
  alocare/eliberare, verificare că nu se suprapun și că totul revine) și un „injector de erori” pentru TCP (pierde/strică pachete).
- **De ce e mai bună:** CI-ul (~18 min) compilează ~47 de nuclee [dedus din `tests/scenarios.txt`]; multe scenarii doar pornesc și rulează
  un test din `kernel/src/tests/`. Testele pe gazdă rulează în secunde și pot încerca milioane de cazuri, nu doar cele scrise de mână.
- **Cost estimat:** (a) 1–2 sesiuni; (b) 2–3 sesiuni (heap întâi, rețeaua după).
- **Primul pas mic, testabil în QEMU:** feature nou `test-toate` + scenariu `toate` care rulează doar 3 teste existente
  (memorie, fire, fpu) în aceeași pornire; scenariile vechi rămân neatinse până când `toate` e verde de mai multe ori.
- **Riscuri:** un test care strică starea nucleului îi poate strica pe următorii (de aceea: doar teste „curate”, iar cele cu panică rămân
  separate — lecția 2); testul vechi al temporizatorului (90–110/s) e deja instabil sub încărcare și nu trebuie mutat în `toate`.
  Mutarea codului din heap/rețea într-o bibliotecă trebuie să lase comportamentul identic (aceleași scenarii trec înainte și după).

### Propunerea 3 — Găzduirea lui Kronos: „obiect model” + pagini de 1 GiB + nuclee dedicate
- **Ce e:** trei piese mici, fiecare separată:
  1. `mem_map` cu pagini de **1 GiB** când procesorul le are (CPUID 80000001h, bitul EDX 26) și există un bloc fizic liber aliniat;
     altfel ca acum (2 MiB / 4 KiB).
  2. **Obiectul model:** un apel nou `model_incarca(cale)`: nucleul citește fișierul o singură dată într-o zonă contiguă, verifică suma
     SHA-256 (aveți `crypto/`), apoi îl mapează **doar-citire** în orice program care îl cere (mai multe procese Kronos partajează
     aceeași copie). După încărcare zona e „sigilată” (nu se mai scrie) — ideea din NIGHTRUN + drepturile Zircon.
  3. **Nuclee dedicate:** `thread_fixeaza(nucleu)` + o opțiune de pornire „nucleele 2..N doar pentru Kronos” (planificatorul nu pune
     alte fire acolo). Bucla de calcul a lui Kronos nu alocă memorie (arenă calculată la pornire, ca NIGHTRUN).
- **De ce e mai bună:** pe workstation (128 GB, i9-10980XE) un model mare încape în RAM; paginile de 1 GiB reduc ratările de TLB, iar
  viteza unui LLM e limitată de memorie (lecția 17). Doar-citire + sumă SHA-256 = un model stricat sau modificat nu rulează.
  Totul se sprijină pe ce aveți deja: `mem_map`, SMP, fire, AVX, `kronos-calcul`.
- **Cost estimat:** 1 GiB: 1 sesiune; obiectul model: 2 sesiuni; nuclee dedicate: 1–2 sesiuni. Total 4–5.
- **Primul pas mic, testabil în QEMU:** scenariul `memorie-1g` (`-m 3G -cpu max`): `/bin/memorie` cere 1 GiB și raportează câte pagini
  de 1 GiB / 2 MiB a primit; pe `-cpu` fără 1 GiB trebuie să revină la 2 MiB și să treacă la fel.
- **Riscuri:** memoria fizică fragmentată → rar există 1 GiB contiguu aliniat (de aceea revenirea la 2 MiB e obligatorie); cât timp o
  pagină de 1 GiB e mapată, nucleul nu o poate „împrumuta”; nucleele dedicate cer atenție la temporizator și la golirea TLB între nuclee.
  **NUMA nu e necesar:** i9-10980XE e un singur procesor fizic [dedus din specificația Intel; neverificat pe mașină — se poate confirma
  ieftin: există sau nu tabela ACPI SRAT].

### Propunerea 4 — Permisiuni pe program („promisiuni” și „căi vizibile”), mai ales pentru aplicația Claude
- **Ce e:** două apeluri noi, opționale: `promite(listă)` (ex. `fisiere-citire`, `fisiere-scriere`, `retea`, `programe`, `module`) și
  `dezvaluie(cale, "rwc")`. Un program care nu le cheamă merge exact ca acum. Odată făcută o promisiune, drepturile pot doar să scadă;
  încălcarea oprește programul cu un mesaj în `log`. Aplicația Claude și uneltele ei, `actualizeaza`, `gh-trimite` și modulele instalate
  le folosesc: de ex. „Claude vede doar `/usb/claude.key` (r) și `/usb/lucru/` (rwc)”.
- **De ce e mai bună:** cheile API și token-ul GitHub stau pe stick, iar azi orice program (inclusiv unul descărcat) le poate citi
  (lecția 18). Confirmarea pe ecran rămâne, dar o greșeală sau un program rău nu mai ajunge la chei.
- **Cost estimat:** 1–2 sesiuni.
- **Primul pas mic, testabil în QEMU:** `/bin/promisiune-test`: promite `fisiere-citire` fără `retea`, apoi încearcă `tcp_connect`
  → nucleul îl oprește; scenariul verifică pe serial „încălcare promisiune: retea” și că shell-ul merge mai departe.
- **Riscuri:** verificări uitate la unele apeluri (de aceea: o singură funcție de verificare chemată din dispecerul de apeluri, plus un
  test care parcurge toate numerele de apel); programe vechi stricate — evitat, pentru că totul e opțional.

### Propunerea 5 — Tipuri care previn greșelile din drivere: DMA cu direcție și încuietori pe niveluri
- **Ce e:** (a) un tip propriu `DmaBuf<Spre/DinPlacă>` în `rtl8168/` și `e1000e/` care obligă la `sincronizeaza_spre_placa()` înainte de
  a da buffer-ul plăcii și `sincronizeaza_din_placa()` înainte de citire (azi `dma_sync` e chemat „de mână”). (b) Încuietori cu nivel
  (ex. 1 = jurnal/serial, 2 = cadre, 3 = heap, 4 = DMA…) verificate la compilare, după ideea Redox; plus `#![forbid(unsafe_code)]`
  în `crypto/`, `tls/`, `json/` (au deja 0 `unsafe`).
- **De ce e mai bună:** cele mai scumpe probleme din Faza 6 au fost exact de cache/DMA (P6-10c, f, g); compilatorul le-ar prinde înainte
  de Release. SMP-ul nou (K6-02b) face blocajele reciproce posibile; nivelurile le exclud.
- **Cost estimat:** (a) 1–2 sesiuni; (b) 2 sesiuni (multe locuri de atins).
- **Primul pas mic, testabil:** pasul `forbid(unsafe_code)` în cele 3 biblioteci (zero schimbări de comportament, testele pe gazdă
  trebuie să treacă identic). Apoi `DmaBuf` doar în modelul software al `rtl8168/` (teste pe gazdă) și scenariile `net`, `net-high` în QEMU.
- **Riscuri:** D-013 — la un driver testat pe hardware orice schimbare trebuie să fie fără efect asupra registrelor; regula: aceeași ordine
  de scrieri în `log rtl` înainte și după (comparat automat), un singur Release pentru schimbare, confirmat pe laptop.

---

## 4. Ce NU merită (acum) și de ce

- **Mutarea pe microkernel / drivere în spațiul utilizator** (Redox, Managarm, Hubris): ar rescrie aproape tot ce merge pe hardware real
  (Realtek, I219, xHCI) — contrar „fiecare pas reversibil” și D-013. Ideile lor se pot lua separat (supraveghetor, scheme).
- **Totul în ring 0 + înlocuire „la cald” a modulelor** (Theseus): cere ca toate programele să fie Rust sigur și un încărcător/linker
  dinamic complex; voi aveți deja ring 3 + ELF + `modmgr`, care merg.
- **Compatibilitate cu apelurile Linux** (Asterinas, Maestro, Managarm): nu e scopul; compatibilitatea plănuită e Windows (Faza 7).
- **Înlocuirea TCP/IP propriu cu smoltcp** sau a heap-ului cu talc: juridic ar fi permis (0BSD / MIT), dar scade „≥ 90 % propriu”;
  luăm ideile (injector de erori, coșuri, fuzzing), nu codul.
- **Interpretor AML complet** (~6.800 de rânduri în crate-ul `acpi`): prea mare acum; pentru oprire ajunge citirea `_S5` din DSDT
  [dedus]. Merită abia pentru baterie/capac la laptop.
- **NUMA pe workstation:** un singur procesor fizic → un singur nod [dedus; de confirmat prin lipsa tabelei SRAT].
- **A rămâne pe serviciile UEFI ca NIGHTRUN:** ei o fac ca să nu scrie driver USB; voi aveți deja xHCI propriu și nucleu propriu.
- **Server GDB în nucleu** (Managarm): mult cod, iar Adrian nu folosește un depanator; „cutia neagră” (propunerea 1) dă mai mult.
- **Slint pentru interfață:** licență GPLv3 / gratuită dar fără sisteme embedded / comercială — nu se potrivește cu MIT + „de la zero”.
- **Fork-ul L2E al llama2.c:** adăugirile sunt sub licență necomercială.
- **Cod din seL4 (nucleu GPLv2), Genode (AGPLv3), Maestro (AGPLv3), ArceOS dacă e luat pe ramura GPL:** doar idei, niciodată cod.
- **Cod din Asterinas și Hubris (MPL-2.0):** doar idei; MPL ar lăsa fișiere cu altă licență în proiect.

---

## 5. Ce n-am putut verifica (cinste)

- Pagina Fuchsia despre VMO n-a fost permisă în sesiune; am citit doar pagina despre drepturi.
- Haiku, xv6, Plan 9, Unikraft, Slint, seL4, Genode: am verificat **doar licențele**, nu și codul. SerenityOS: doar paginile `pledge`/`unveil`.
- Cifrele NIGHTRUN (viteze, timpi de pornire) sunt ale lor; nu le-am reprodus.
- Durata CI-ului (~18 min) e din două rulări CI din 23 oct. (`gh run list`); câștigul de timp din propunerea 2 e o estimare.
- Nu am verificat pe hardware că i7-1185G7 și i9-10980XE au pagini de 1 GiB (Intel le documentează la ambele familii, dar nu am
  rulat CPUID pe ele); primul pas din propunerea 3 tratează oricum cazul „nu există”.
- Toate costurile în „sesiuni” sunt estimări după ritmul din `docs/STATE.md`.

