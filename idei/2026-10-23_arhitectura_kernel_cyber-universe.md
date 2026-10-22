# Arhitectura actuală a nucleului Cyber Universe OS (23 octombrie 2026)

*Document de referință pentru planul de coding „Kronos bare-metal”. Scris de centrul de comandă din codul real
(`Adriancu91/cyber-universe`, Release os-150+) și din README-urile fiecărui modul. Tot ce e aici e FAPT verificat în repo,
în afară de rândurile marcate ESTIMARE. Companion al planului v0.2 (`idei/2026-10-23_kronos-bare-metal_v0.2.md`).*

---

## 1. Pe scurt

- **Limbaj / platformă:** Rust `no_std`, x86_64, pornire UEFI prin **Limine** (versiune fixată), licență MIT, cod propriu (clean-room,
  `docs/CLEAN_ROOM.md`). ~**19.000 de linii** în nucleu + programe, plus crate-uri separate: `crypto/` (2.556), `rtl8168/` (2.038),
  `tls/` (770), `json/` (717).
- **Model:** nucleu monolitic mic (memorie, fire, procese, apeluri de sistem, drivere de bază) + **programe în ring 3** (ELF statice) +
  **module instalabile** (pachete `.cum`, format `docs/specs/MODULE.md`, compatibil cu standardul comun `modul-v0`).
- **Un singur nucleu de procesor** activ (ACPI/MADT vede toate procesoarele, dar nu le pornește). Toate driverele lucrează prin
  **polling** (fără întreruperi de dispozitiv, fără MSI/MSI-X); singurele întreruperi folosite: ceasul (APIC, 100 Hz) și tastatura PS/2 (IRQ 1).
- **Testare:** 50 de scenarii automate în QEMU (`tests/scenarios.txt`, `tools/test.sh`, verifică textul de pe portul serial), test de stres de
  5 minute zilnic, CI pe GitHub Actions care publică **Release** cu fișierele stick-ului și sumele SHA-256. Pe hardware: Lenovo ThinkPad
  (Ryzen 5 4500U) — totul din `docs/HARDWARE.md` și `Cyber-hub/rezultate/`.

## 2. Structura repo-ului

```
boot/            limine.conf, resurse de pornire
kernel/src/
  boot.rs        cererile Limine: harta memoriei, HHDM, framebuffer, RSDP, module (initrd, /bin/*)
  arch/x86_64/   gdt.rs, idt.rs (întreruperi, `extern "x86-interrupt"`), apic.rs (APIC local, ceas 100 Hz, I/O APIC), syscall.rs (intrarea `syscall`)
  mem/           map.rs, frame.rs, paging.rs, address_space.rs, heap.rs
  sched/         fire ale nucleului, round-robin, preempțiune, WaitQueue, Mutex, sleep
  proc/          procese ring 3, ELF, argumente, wait/kill, tabel de fișiere
  syscall/       cele 35 de apeluri de sistem (listă la §8)
  acpi/          RSDP → tabele, MADT, MCFG (fără interpretor AML)
  pci/           ECAM, enumerare, BAR-uri (64 de biți), enable (memorie + Bus Master), configurare bit cu bit în jurnal
  drivers/       serial.rs (16550), keyboard.rs (PS/2 + aranjament RO), mouse.rs, rtc.rs, nvme.rs, ahci.rs, e1000.rs, rtl8168.rs, nic.rs, usb/ (xhci.rs, hid.rs, storage.rs)
  block/         interfața BlockDevice (sectoare 512), MemDisk, Partition
  fs/            vfs.rs (montări), ramfs.rs, part.rs (GPT/MBR), fat32.rs (citire + scriere), tar
  net/           Ethernet, ARP, IPv4, ICMP, UDP, DHCP, DNS, TCP; `tls/` și `crypto/` ca crate-uri
  gfx/           framebuffer, Canvas (buffer de spate), font propriu 5×7 cu diacritice
  ui/            serverul grafic: ferestre, focus, mouse, compunere pe zone schimbate
  input/         evenimente tastatură/mouse
  shell/         consola `cyber>`: help, ls, cat, run, desktop, mod, tastatura, ping, host, http, mem, lspci, lsusb, net, rtl, hw, log, uptime, reboot, exit
  modmgr/        managerul de module (.cum)
  log.rs         jurnalul nucleului în memorie (`log [cuvânt] [n]`), și pe serial
  random.rs      RDRAND + amestec; time.rs
  tests/         stress.rs
user/src/        lib.rs (apeluri de sistem, print!, entry!), heap.rs, gfx.rs, net.rs, https.rs, http_client.rs, claude_api.rs, claude_tools.rs, text.rs, settings.rs
user/src/bin/    hello, cat, demo, desktop, editor, files, monitor, network, settings, terminal, udp, modules, mod_salut, fetch, claude, claude-app, actualizeaza, gh-trimite
modules/         pachete de module de test (salut, cere-salut)
tests/           scenarios.txt, disk/ (imagini), screens/ (capturi de referință)
tools/           build.sh, test.sh (QEMU fără ecran, `-serial stdio`, limită de timp), before-*/after-* (servere de test), check-release.sh, env-check.sh
docs/            ARCHITECTURE, DECISIONS (D-001…D-013), ROADMAP (Fazele 0–7), TASKS (P0…P6), STATE, BLOCKERS, HARDWARE, USB, METRICS, CLEAN_ROOM, plans/, research/, specs/
```

## 3. Pornirea (boot)

- UEFI → `BOOTX64.EFI` (Limine) → `limine.conf` → `kernel` (ELF64, jumătatea de sus a memoriei) + `initrd.tar` (programele `/bin/*`, rădăcinile
  de încredere, fonturi) + `cyber.rw` pe stick (marcaj „se poate scrie”).
- Cereri Limine folosite: harta memoriei fizice, **HHDM** (toată memoria fizică mapată la `0xffff_8000_0000_0000 + fizic`), framebuffer
  (32 bpp), RSDP, module. După pornire nucleul își copiază tabelele de pagini (`adopt_tables`) și recuperează memoria bootloader-ului.
- Pe laptopul real: **14 secunde** de la selectarea stick-ului la desktop. Secure Boot trebuie oprit.

## 4. Memoria

- **Cadre fizice (4 KiB):** alocator cu hartă de biți; la P6-10g s-a adăugat **paza paginilor DMA** (nicio pagină dată de două ori; jurnal al
  regiunii din harta memoriei) după bug-ul de pe laptop; buffer-ele DMA ale rețelei se alocă într-un bloc contiguu, **peste 16 MiB, sub 4 GB**,
  cu adrese pe 64 de biți scrise în descriptori.
- **Paginare pe 4 niveluri:** mapare/demapare, pagini mari, NX, CR0.WP; `map_mmio` pentru registre de dispozitive; `address_space.rs` —
  fiecare proces are PML4 propriu, jumătatea de sus (nucleul) comună (256 de tabele de nivel 3 create din start).
- **Heap-ul nucleului:** listă de blocuri libere cu unire, crește de la `0xffff_9000_0000_0000`, **maxim 256 MiB** (limită de ridicat pentru
  tensori). **Programele utilizator n-au heap de la nucleu**: `user/src/heap.rs` e un heap mic al programului; stiva programului 64 KiB sub
  `0x7fff_fff0_0000`.
- Nu există: alocator de blocuri mari (GB), pagini de 1 GiB folosite explicit, NUMA, IOMMU, memorie necache-abilă (PAT/MTRR) pentru DMA
  (golirea cache-ului se face cu instrucțiuni, unde e nevoie).

## 5. Procesor, întreruperi, timp

- GDT/IDT proprii; întreruperile ca `extern "x86-interrupt"` (D-010); APIC local + I/O APIC din MADT; ceasul APIC la **100 Hz** (10 ms);
  RTC pentru dată/oră (folosită de TLS); RDRAND pentru numere aleatoare.
- **SMP: nu.** MADT numără procesoarele (scenariul `smp` cu `-smp 4` verifică „4 procesoare”), dar nu sunt pornite (fără INIT/SIPI, fără
  planificare pe mai multe nuclee). ESTIMARE pentru adăugare: 1–2 săptămâni (trampolină, stive per nucleu, APIC per nucleu, încuietori reale).
- Fără MSI/MSI-X, fără întreruperi de la PCIe; dispozitivele sunt interogate (polling) de fire de sistem (rețea la ~2 ms, USB la 8 ms).

## 6. Fire și procese

- **Fire ale nucleului** (`sched`): round-robin cu preempțiune la tick; `spawn`, `spawn_system` (fire care trăiesc cât nucleul), `yield_now`,
  `sleep_ms`, `WaitQueue` (`wait_until`, `wake_one/all`, se poate chema din întreruperi), `Mutex<T>` (firul doarme), `kill(id)`, `cpu_ticks(id)`;
  firul idle face `hlt`. Comutarea de context salvează rbx, rbp, r12–r15, rsp; `CR3` se încarcă doar dacă diferă.
- **Procese** (`proc`): un spațiu de adrese + un fir în ring 3; `spawn_elf` (ELF64 static, segmentele mapate cu drepturile lor, `.bss` zero),
  `spawn_path(cale, argumente)` (argc/argv pe stiva programului), `wait(id)`, `kill(id)` (cod -9), `list()`. Fiecare proces are tabelul lui de
  fișiere deschise. Programele se încarcă la `0x400000` (`user.ld`).

## 7. Dispozitive și drivere (toate cod propriu, după specificații publice)

| Driver | Ce face | Stare pe hardware (ThinkPad) |
|---|---|---|
| ACPI | RSDP, sume de control, MADT, MCFG; fără AML | merge |
| PCIe (ECAM) | enumerare, punți, BAR 64 de biți, `enable()` (memorie + Bus Master), `lspci` | merge |
| Serial 16550 | jurnal + teste (QEMU) | laptopul n-are port |
| PS/2 tastatură, mouse | IRQ 1; aranjament US și **Română (standard)** | merge |
| xHCI | reset, inele de comenzi/evenimente, contexte, scratchpad, enumerare, descriptori, HID boot (tastatură, mouse), Mass Storage (BOT, SCSI: INQUIRY, READ CAPACITY, READ/WRITE, Unit Attention, așteptări după ceas), jurnal pe pas (`log usb`) | merge (stick ADATA montat cu scriere) |
| NVMe | cozi admin/IO, citire/scriere | merge (`/disk` montat) |
| AHCI | SATA | QEMU |
| e1000 | placa de rețea din QEMU | QEMU |
| **rtl8168** (crate propriu + model software al cipului pentru teste pe gazdă) | PHY, legătură, inel RX 256 / TX, re-pornire după RDU, revizia 8168GU, acces MAC OCP verificat, variante de pornire la rece (`rtl porneste rece/mcu/phy/cplus/ordine/cache/faracache`), `log rtl`/`log rx` cu registre și adrese | **merge la cald** (DHCP, ping, DNS, HTTPS pe 22 oct); la rece: P6-10h făcut, de confirmat la testul 8 |
| Framebuffer | 32 bpp de la firmware; fără accelerare | merge |

## 8. Apelurile de sistem (ring 3 → nucleu, `syscall`; `rax` = număr, argumente `rdi rsi rdx r10 r8`, rezultat `rax`, negativ = eroare)

`0 exit`, `1 write`, `2 yield`, `3 sleep_ms`, `4 open`, `5 read`, `6 close`, `7 stat`, `8 window_create`, `9 window_present`, `10 event_wait`,
`11 window_close`, `12 spawn`, `13 wait`, `14 list`, `15 time`, `16 screen_size`, `17 sysinfo`, `18 kill`, `19 create`, `20 remove`,
`21 module`, `22 term_open`, `23 term_read`, `24 term_write`, `25 resolve`, `26 tcp_connect`, `27 udp_open`, `28 udp_send`, `29 udp_recv`,
`30 net_info`, `31 ping`, `32 random`, `33 rename`, `34 sync`. Erori: `-1` argument, `-2` pointer, `-3` nu există, `-7` există deja,
`-8` disc doar citire, `-9` director plin, `-10` disc plin. **Lipsesc** (pentru Kronos): mmap/alocare de memorie mare pentru programe, fire
multiple într-un proces, memorie partajată, acces direct la dispozitive din ring 3.

## 9. Fișiere și stocare

- `BlockDevice` (sectoare de 512) → `Partition` (GPT/MBR/superfloppy) → **FAT32** citire + scriere (nume lungi, ambele FAT, FSInfo, dată/oră);
  scrierea e permisă **doar** pe partițiile cu fișierul `cyber.rw` în rădăcină; ordinea date → FAT → director limitează pagubele la oprire bruscă.
- `vfs` cu montări: `/` (ramfs + initrd), `/bin`, `/disk` (NVMe/AHCI), `/usb` (stick). `tar` pentru initrd și pachete de module.
- Nu există: alt sistem de fișiere (ext/NTFS), jurnalizare, cache de blocuri serios, fișiere mari (>4 GB, limita FAT32).

## 10. Rețea și criptografie

- Stiva proprie: Ethernet, ARP (cache 5 min), IPv4 (fără fragmente), ICMP, UDP, **DHCP** (reînnoire), **DNS**, **TCP** (conectare, trimitere,
  primire cu limită de timp), un fir de sistem pentru cadrele primite. `crypto/`: primitivele TLS 1.3 scrise de noi (D-011, cu vectorii oficiali
  de test); `tls/`: handshake 1.3 cu rădăcinile Mozilla din initrd și **certificat verificat** (REZULTAT: `example.com` pe laptop).
- Programe: `fetch` (HTTPS), `claude` / `claude-app` (API Claude, JSON propriu, unelte cu confirmare), `actualizeaza` (Release din GitHub,
  sume verificate, scriere pe stick), `gh-trimite` (API `contents`, token din `/usb/github.token`).

## 11. Grafică, interfață, shell

- `gfx::Canvas` cu zonă schimbată și `present()` pe rânduri (~290 cadre/s în QEMU la 1280×800); font propriu cu diacritice.
- `ui::Server`: ferestre, focus, mutare, închidere, cursor; programele desenează în imaginea lor și o trimit cu `window_present`.
- Desktop (Start, ceas), editor, fișiere, monitor (memorie, procesor, programe), setări, terminal (shell în fereastră), rețea.
- Shell-ul `cyber>` (Esc din desktop): comenzile de la §2; `log` cu filtrare și număr de rânduri; `hw` = raport hardware pe o pagină.

## 12. Module

- Pachet `.cum` (tar ustar) cu `module.toml` (nume, versiune, dependențe, `start`), instalat în `/disk/modules/<nume>/`, index în
  `/disk/modules/index`; `mod list|install|start|stop|remove`; dependențele se verifică; ștergerea refuzată dacă e folosit.
- Același format conceptual cu `Cyber-hub/standarde/modul-v0.md` (folosit și de Kronos: 24 de manifeste).

## 13. Testare, CI, reguli de lucru

- `tools/test.sh`: fiecare scenariu = QEMU fără ecran, text așteptat pe serial, limită de timp; `before-*`/`after-*` pornesc servere de test
  (HTTP/HTTPS/DNS/API simulat). Capturi de ecran de referință în `tests/screens/`. `stress` 5 minute zilnic.
- CI: build + toate scenariile la fiecare push; Release automat (`stick-usb` + `SHA256SUMS` + `VERSIUNE`); `check-release.sh`.
- Reguli: `CLAUDE.md` al repo-ului (buclă în cascadă, maximum 3 încercări pe blocaj, `main` mereu construibil, README per modul,
  `unsafe` doar cu `// SAFETY:`), D-013 (**o singură schimbare de comportament pe Release la driverele testate pe hardware**, registre
  scrise un bit odată, cu valorile în jurnal), clean-room (`docs/CLEAN_ROOM.md`).

## 14. Limitări care contează pentru „Kronos bare-metal” (lista de goluri, în ordinea importanței)

1. **Un singur nucleu de procesor** → SMP e primul lucru de adăugat pentru un backend CPU serios (36 de fire pe workstation).
2. **Memorie:** heap-ul nucleului maxim 256 MiB; programele n-au `mmap`/alocare mare → trebuie un alocator de regiuni mari (GB) și un apel
   de sistem pentru el; pagini mari; opțional memorie necache-abilă pentru DMA (PAT).
3. **Fără întreruperi de dispozitiv (MSI/MSI-X)** → pentru GPU se poate începe cu polling (cum fac toate driverele de acum), dar cozile lungi
   vor cere întreruperi.
4. **Fără fire multiple într-un proces** → runtime-ul de calcul va trebui să stea în nucleu (ca fire de sistem) sau să primească fire în ring 3.
5. **Fără IOMMU** și fără cunoașterea stării lui pe workstation (poate bloca DMA-ul plăcii video).
6. **Fără AML** (ACPI complet): oprirea/repornirea prin ACPI e limitată (`reboot` există).
7. **Fără float serios verificat în nucleu** (SSE/AVX în ring 3: de verificat că sunt activate și salvate la comutare — NECUNOSCUT în acest
   document; obligatoriu de clarificat înainte de backend-ul CPU).
8. Stocare: FAT32 (fișiere < 4 GB) — datele lui Kronos (cache de 2,5 GB e OK; seturi mai mari trebuie împărțite) .

## 15. Ce există deja pentru interfețele I1–I4 din planul v0.2

- I1 (kernel ↔ dispozitiv): `pci::Device` (`bar(i)`, `enable()`), `mem::paging::map_mmio`, alocarea DMA contiguă cu adrese fizice, `log`,
  modelul „software al cipului pentru teste pe gazdă” (crate `rtl8168/`) — tipar de refolosit pentru GPU.
- I2/I3 (runtime ↔ model): nimic încă; există `json/` propriu și formatul tar pentru pachete; un format de greutăți trebuie definit.
- I4 (OS ↔ cascada Kronos): `actualizeaza` (descărcare din Release), `gh-trimite` (urcare pe GitHub), `/usb` cu scriere, `cyber.rw`,
  `test/` (urmează C-7).
