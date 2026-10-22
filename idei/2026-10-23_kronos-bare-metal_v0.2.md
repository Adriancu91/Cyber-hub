# KRONOS BARE-METAL — Plan v0.2 (revizia arhitectului Kronos / Cyber Universe)

**Status:** propunere pentru Adrian și pentru auditul unui AI de coding. Nu e aprobată pentru implementare. Nu schimbă nimic în repo-uri.
**Scris de:** centrul de comandă (Claude), 23 octombrie 2026, 02:30, pe baza codului real din `Adriancu91/cyber-universe` (OS),
`Adriancu91/cyberspace` (Kronos) și a deciziilor din `Cyber-hub/DECIZII.md`.
**Etichete:** FAPT (verificat în cod/documente sau rezultat publicat), REZULTAT (măsurat pe hardware-ul nostru), ESTIMARE, IPOTEZĂ, NECUNOSCUT.

---

## 0. Ce se schimbă față de v0.1 (pe scurt)

1. **Nu se face un repo nou `kronos-baremetal`.** Etapele K1–K4 din v0.1 (bootloader UEFI, kernel minimal, diagnosticare, PCIe) **există deja și
   merg pe hardware real** în Cyber Universe OS (FAPT: ~19.000 de linii Rust `no_std`, 50 de scenarii automate, Release-uri din CI, teste pe
   laptop). Un repo paralel ar duplica 3 săptămâni de muncă și ar rupe ce funcționează. Planul se mapează pe trei locuri existente:
   `cyber-universe` (nucleu, drivere, backend GPU, runtime), `cyberspace` (modelul, datele, examenele, cascada), `Cyber-hub` (decizii, comenzi).
2. **Se adaugă veriga lipsă din v0.1: motorul de calcul** (setul de instrucțiuni al plăcii, lansarea programelor de calcul, nucleele de
   înmulțire de matrici etc.). Fără el, cele 4 module ale driverului nu produc niciun calcul util. E și cea mai scumpă parte.
3. **Backend CPU primul.** Interfețele kernel ↔ backend ↔ runtime ↔ model se construiesc și se testează cu un backend pe procesor (36 de fire,
   128 GB RAM), ca modelul Kronos să ruleze în OS **înainte** ca GPU-ul să fie rezolvat. Astfel K6–K8 nu mai depind de K5.
4. **„Firmware propriu” (Pista B) se închide pe Ampere**, cu motivul la §6. Nu se investește timp în ea.
5. **„DHC”** din v0.1 nu există nicăieri în Kronos sau în OS (NECUNOSCUT ce e). Se ignoră până când cineva îl definește.
6. Se adaugă **K10: măsurătoarea decisivă** (același model, același examen: OS vs Windows/PyTorch), fiindcă Adrian a decis că alegerea
   „unde rulează / unde se antrenează Kronos” se face pe măsurători, după experimente (decizia din 22 oct 23:10).

---

## 1. Realitatea de pornire (ce există)

### 1.1 Cyber Universe OS (`cyber-universe`) — FAPT, din cod și din testele pe laptop
| Modul din v0.1 | Stare | Unde |
|---|---|---|
| Bootloader UEFI (K1) | **gata**: Limine, kernel ELF, harta memoriei, initrd | `kernel/src/boot.rs`, `boot/limine/` |
| Kernel minimal (K2): intrare, memorie fizică/virtuală, întreruperi, timer, panic | **gata** (un singur nucleu de procesor) | `kernel/src/{arch,mem,proc,sched,syscall}` |
| ACPI | există (de verificat cât: tabele, reset) | `kernel/src/acpi/` |
| Diagnosticare (K3): jurnal în RAM, `log [cuvânt] [n]`, `hw`, serial în QEMU | **parțial**: jurnalul nu se scrie încă pe disc; serialul merge în QEMU (pe laptop nu există port) | `kernel/src/log.rs`, `shell/` |
| PCIe (K4): enumerare, BAR-uri, Bus Master, configurare bit cu bit în jurnal | **gata** | `kernel/src/pci/` |
| DMA: buffer-e contigue, adrese pe 64 de biți, paza paginilor (nicio pagină dată de două ori) | **gata** (după P6-10d/g) | `kernel/src/mem/` |
| Stocare: NVMe, AHCI, xHCI USB + stick, FAT32 (GPT/MBR/superfloppy), scriere | **gata pe laptop** | `drivers/{nvme,ahci}.rs`, `fs/` |
| Rețea: Realtek RTL8168 (laptop), e1000 (QEMU), TCP/IP, DHCP, DNS, TLS 1.3 propriu, HTTPS | **gata la cald pe laptop** (REZULTAT 22 oct 18:28 și 22:41); la rece: P6-10e/h făcute, de confirmat la testul 8 | `drivers/rtl8168.rs`, `net/`, `crypto/`, `tls/` |
| Programe utilizator, syscall-uri, desktop, editor, Claude în OS, actualizare din GitHub, trimitere pe GitHub | **gata** (P6-01…P6-09) | `user/` |
| CI: build + 50 de scenarii QEMU + Release automat cu sume | **gata** | `.github/`, `tools/test.sh` |
| **SMP (mai multe nuclee)** | **lipsă** | — |
| **Întreruperi MSI/MSI-X pentru dispozitive** | **lipsă** (Realtek merge prin polling, IMR = 0) | — |
| **IOMMU** | **lipsă/necunoscut** (nu e atins; pe workstation starea lui e NECUNOSCUT) | — |
| Jurnal persistent pe disc/stick | **lipsă** (există `cyber.rw` pe stick ca loc de scriere) | — |
| Alocator de memorie mare (GB) pentru tensori, pagini mari | **lipsă** | — |

### 1.2 Kronos (`cyberspace`) — FAPT
- Nucleu cu porturi, contracte, registru, configurare, orchestrator, jurnal, paznic (`kronos/`), **24 de module** cu `MANIFEST` în formatul
  comun `standarde/modul-v0.md` (același standard pe care îl folosește și OS-ul) — deci contractul de modul **există deja** între cele două proiecte.
- Modelul W2: transformer propriu, **98,0 M parametri**, 12 straturi × 768, 12 capete, context 512, vocabular 16.384 (tokenizer propriu).
  Cel mai bun pe „răspuns din text”: #415 / #425. Codul e **Python + PyTorch + CUDA**, antrenat pe Windows 11, pe RTX 3070 Ti.
- Cifre de antrenare (REZULTAT): ~95 M de simboluri pe oră; ~1 miliard pe o noapte de 10 ore; memorie video 5,1–5,6 GB la lot 12 × 512
  (formula din `docs/MUTARE_workstation.md`: ≈ 0,35 GB + 16 octeți × parametri + activări); temperatura limitată la 83 °C.
- Examene și verificatoare proprii (S16: verificatorul fără LLM, acord 97,6 % cu Qwen), pre-înregistrare, cascadă supraveghetor + executant.
- Dependențe declarate (de redus în timp): PyTorch/CUDA ca unelte; Qwen doar pentru poveștile vechi; Claude în cascadă.

### 1.3 Hardware — FAPT / NECUNOSCUT
- Workstation: RTX 3070 Ti 8 GB (GA104, Ampere), driver Windows 616.56, 128 GB RAM, Windows 11 Pro, 36 de fire de procesor (modelul
  procesorului, placa de bază, BIOS-ul, Above-4G Decoding / Resizable BAR, starea IOMMU: **NECUNOSCUT** până la inventarul K0).
- Laptop de test: Lenovo ThinkPad NB-7211174, Ryzen 5 4500U, iGPU Radeon Renoir (`1002:1636`, Vega/GCN5, 6 CU, fără VRAM proprie), 8 GB.

---

## 2. Structura: cum se mapează arborele din v0.1 pe ce există

| v0.1 | v0.2 (loc real) |
|---|---|
| `boot/`, `kernel/`, `platform/`, `storage/` | **există** în `cyber-universe/kernel/src/…` (nu se reface) |
| `gpu/common, pci_discovery, ga104, firmware, memory, command_submission, synchronization` | crate nou `cyber-universe/gpu/` cu backend-uri: `cpu/` (primul), `amd-renoir/` (experimente nivel 0–3), `nvidia-ga104/` (după K5A) |
| `runtime/` (buffers, queues, dependencies, compute_api) | crate `cyber-universe/calcul/` (API de calcul, independent de backend) + program `/bin/kronos` |
| `kronos_ai/` (tensor, operators, execution) | crate `kronos-motor/` în `cyber-universe`, modul în format `modul-v0`; **greutățile** exportate din PyTorch într-un format propriu, simplu (antet + tensori bf16/f32), produse de o unealtă din `cyberspace/unelte/` |
| `docs/GPU_RESEARCH.md`, `FIRMWARE_RESEARCH.md` | `cyber-universe/docs/research/STUDIU-GPU.md` (comanda C-11) |
| `tests/benchmarks` | `cyber-universe/tests/` + rezultate în `Cyber-hub/rezultate/` |
| K0 `HARDWARE_INVENTORY.md` | `cyber-universe/docs/HARDWARE.md` (există pentru laptop; de completat pentru workstation) |

**Regula de aur rămâne:** niciun proiect nu modifică repo-ul altuia; Kronos nu importă din OS și invers; legătura e prin fișiere cu format
declarat (greutăți, examene, rezultate) și prin standardul de modul.

---

## 3. Interfețele (contractele) — ce trebuie definit înainte de cod

- **I1 — kernel ↔ backend de calcul** (`DispozitivCalcul`): `identifica()` (producător, cip, memorie, capabilități); `aloca(bytes, unde)`,
  `elibereaza`, `copiaza(gazda→dispozitiv, dispozitiv→gazda)`; `trimite(coada, comanda)`, `asteapta(semafor/întrerupere, timeout)`;
  `stare()`/`erori()`; `reseteaza()`. Backend-ul CPU implementează totul trivial (memoria = RAM, „coada” = fire de execuție).
- **I2 — backend ↔ runtime de calcul**: tensori (formă, tip: f32/bf16, pas), operații: `matmul`, `add/bias`, `layernorm`, `gelu`, `softmax`
  cauzal (atenție), `embedding`, `cross_entropy`, `adamw_pas`; fiecare cu test numeric față de o referință calculată independent (pe gazdă, în CI).
- **I3 — runtime ↔ modelul Kronos**: descrierea modelului (straturi, dimensiuni, vocabular) + formatul greutăților + tokenizer-ul (portat în Rust,
  verificat că produce exact aceleași simboluri ca cel din Python pe 10.000 de propoziții).
- **I4 — OS ↔ cascada Kronos**: prin GitHub/stick (bucla C-7): sarcini `test/comenzi.txt`, rezultate `test/rezultate/`, examene în format JSON
  (cele existente: `docs/conversatie/examen_*.json`), verificatorul fără LLM portat în Rust.

---

## 4. Etapele revizuite

| Etapă | Stare | Ce rămâne | Criteriu de acceptare (măsurabil) | Depinde de |
|---|---|---|---|---|
| **K0 Inventar** | parțial | workstation: procesor, placă de bază, BIOS, Above-4G/ReBAR, IOMMU; OS pornit de pe stick pe workstation într-o **fereastră cu Adrian** (Kronos oprit 30 min): `hw`, `lspci`, BAR-urile plăcii | `docs/HARDWARE.md` are rândul workstation-ului; BAR0/BAR1 ale GA104 notate | Adrian prezent |
| **K1 Boot** | gata | — | — | — |
| **K2 Kernel** | gata (1 nucleu) | **SMP** (pornirea celorlalte nuclee, planificare pe nuclee), necesar backend-ului CPU | 36 de fire văzute și folosite; un test de înmulțire de matrici scalează ≥ 10× față de 1 nucleu | K0 |
| **K3 Diagnosticare** | parțial | jurnal persistent pe stick/disc; coduri de eroare structurate | după o cădere, jurnalul se citește de pe stick | — |
| **K4 GPU descoperire** | gata generic | `gpu identifica` nivel 0: PCI, BAR-uri, citirea registrului public de identitate (doar citire) | poză/raport cu ID-ul cipului și mărimea BAR-urilor, pe laptop (AMD) și pe workstation (NVIDIA) | K0 |
| **K5A Driver cu firmware-ul producătorului** | cercetare | studiul C-11 (`STUDIU-GPU.md`) + experimente nivel 1–3 întâi pe AMD (documentat public) | raport cu etape, ore, riscuri, licențe; nivel 1 pe AMD: placa răspunde la o comandă | K4 |
| **K5B Firmware propriu** | **închisă** | — | — | vezi §6 |
| **K6-CPU Primul calcul** | nou | backend CPU + I2 + tokenizer în Rust + încărcarea greutăților #415; `kronos raspunde "<text>" "<întrebare>"` | aceleași răspunsuri ca PyTorch pe 50 de întrebări (verificatorul S16), timp pe întrebare măsurat | K2 (SMP util, nu obligatoriu) |
| **K6-GPU Primul calcul** | după K5A | un program de calcul lansat și terminat, rezultat citit și comparat | 1 operație deterministă corectă | K5A |
| **K7 Runtime** | nou | cozi, dependențe, alocare, instrumentare | examenul de 300 de întrebări rulează în OS, cu timp și memorie raportate | K6-CPU |
| **K8 Integrare Kronos** | nou | auto-jocul (generare + verificator) în OS; memoria explicită în RAM (128 GB) | o noapte de generare în OS produce aceleași statistici ca pe Windows | K7 |
| **K9 Alte GPU-uri** | mai târziu | backend-uri pe generații | — | K6-GPU |
| **K10 Măsurătoarea decisivă** | nou | același model, același examen, aceeași placă/procesor: OS vs Windows | tabel: timp, memorie, watt, pornire; **decizia lui Adrian pe cifre** | K7 (CPU), K6-GPU (GPU) |

**Antrenarea** (propagarea înapoi, AdamW, ~1 miliard de simboluri pe noapte) **rămâne pe Windows + PyTorch + CUDA** până când K6-GPU și
K10 arată altceva. E o dependență declarată, nu ascunsă (regula 5 din metoda noastră: unelte numerice, nu modele străine).

---

## 5. Cerințele reale ale lui Kronos (pentru runtime)

- **Rulare (inferență), W2 98 M:** greutăți 98 M × 2 octeți (bf16) ≈ **196 MB** (f32: 392 MB) — încap oriunde. Calcul ≈ 2 × 98 M ≈ **0,2 GFLOP pe
  simbol generat**; pe 36 de fire cu AVX2, ESTIMARE 50–200 de simboluri pe secundă (de măsurat la K6-CPU). Examenul de 300 de întrebări: minute.
- **Antrenare:** ~16 octeți × parametri pentru greutăți + gradienți + AdamW ≈ 1,6 GB, plus activările (lot 12 × 512 × 12 straturi × 768) → 5,1–5,6 GB
  (REZULTAT pe 3070 Ti). Debit țintă ≥ 95 M simboluri/oră ca să nu fie regresie față de Windows. Pe CPU, ESTIMARE: de 20–50× mai lent → nu e o
  opțiune pentru antrenare; de aici K10.
- **Operatorii necesari** (lista completă pentru I2): embedding, poziții, layernorm, linear (matmul + bias), GELU, atenție cauzală cu softmax,
  reziduuri, cross-entropy; pentru antrenare: toate cu gradient + AdamW + rata de învățare cu încălzire/cosinus + tăierea gradientului.
- **Date:** TinyStories + text românesc; cache de simboluri 2,5 GB; totul încape în 128 GB RAM → memoria explicită (H2) e fezabilă în OS.
- **Formate numerice:** f32 pe CPU la început; bf16 pe GPU (Ampere are tensor cores bf16 — FAPT public).

---

## 6. Pista B (firmware propriu): de ce se închide

- FAPT (din cunoștințele mele, de confirmat cu sursa în C-11): pe plăcile NVIDIA din generațiile Turing și mai noi, firmware-ul GSP și
  firmware-urile motoarelor de securitate sunt **semnate de NVIDIA și verificate de hardware** la încărcare; driverele open-source (nouveau,
  nova) rulează numai cu firmware-ul semnat livrat de NVIDIA. Un firmware propriu nu ar fi acceptat de placă.
- Consecință: pe GA104, „firmware propriu” nu are o cale tehnică demonstrabilă; singura cale e **driver propriu + firmware-ul producătorului**
  (Pista A), folosit ca blob declarat, în condițiile licenței lui (de verificat în C-11 dacă e redistribuibil în imaginea noastră).
- Pe AMD, firmware-ul e tot binar și semnat pentru unele blocuri; documentația publică acoperă însă setul de instrucțiuni și registrele —
  de aceea experimentele de nivel 1–3 încep pe AMD.

---

## 7. Ipoteze nedemonstrate (marcate explicit)

1. IPOTEZĂ: modulele MIT publicate de NVIDIA + nova + NVK sunt suficiente ca să pornim GSP-ul și un canal de calcul dintr-un kernel propriu.
2. NECUNOSCUT: setul de instrucțiuni SM86 — cât e dedus public (NVK/nouveau) și dacă ajunge pentru un asamblor propriu de înmulțire de matrici.
3. ESTIMARE: nucleele de calcul proprii ating 10–30 % din cuBLAS în prima versiune; peste 50 % cere luni de reglaj.
4. ESTIMARE: câștigul „fără sistem de operare” la antrenare e de 1–5 %, nu „monumental”; câștigul real e controlul, pornirea în 14 s și proprietatea codului.
5. NECUNOSCUT: starea IOMMU și Above-4G Decoding pe workstation (poate bloca DMA-ul plăcii din OS-ul nostru).
6. NECUNOSCUT: licența firmware-ului GSP permite includerea lui într-o imagine proprie.
7. IPOTEZĂ: SMP se poate adăuga în OS în 1–2 săptămâni (ACPI MADT există; pornirea nucleelor prin INIT/SIPI e standard, documentată public de Intel/AMD).

---

## 8. Riscuri principale

| Risc | Impact | Măsură |
|---|---|---|
| GPU-ul nu pornește din OS (GSP, IOMMU, ReBAR) | K6-GPU se amână luni | K6-CPU și K10-CPU merg oricum; experimentele pe AMD în paralel |
| Nuclee de calcul lente | OS mai lent decât Windows la antrenare | antrenarea rămâne pe Windows până când cifrele spun altceva |
| Efort subestimat la motorul de calcul | luni în plus | studiul C-11 dă estimări pe module, revizuite după nivelul 1 |
| Workstation-ul e al lui Kronos | experimentele GPU opresc antrenarea | doar în ferestre stabilite cu Adrian; totul altceva pe laptop |
| Tokenizer/greutăți portate greșit | rezultate diferite de PyTorch | test de egalitate pe 10.000 de propoziții și 50 de întrebări înainte de orice |

---

## 9. Ordinea recomandată (următoarele 4–6 săptămâni), fără să blocheze nimic

1. **OS autonom:** C-10 gata (P6-10g/h făcute, de confirmat la testul 8: pornire la rece → adresă) → C-7 (bucla de test de la distanță).
2. **K0 workstation** într-o fereastră cu Adrian (30 min, după ce se întoarce): `msinfo32`, BIOS (Above-4G, ReBAR, IOMMU), OS de pe stick: `hw`, `lspci`.
3. **K6-CPU** (poate începe imediat, în cloud, fără hardware): format de greutăți + unealtă de export din PyTorch (în `cyberspace`), tokenizer în
   Rust, motorul de rulare, `kronos raspunde`, test de egalitate cu PyTorch. Prima dovadă că „Kronos în Cyber Universe” nu e o vorbă.
4. **C-11:** nivel 0 pe laptop (AMD) + `STUDIU-GPU.md` cu estimări pe module (inclusiv motorul de calcul), licențe, comparație AMD/NVIDIA.
5. **K2-SMP** (dacă K6-CPU arată că un singur nucleu e prea lent pentru examene).
6. **Decizia lui Adrian** pe studiu + cifre: Pista A pe NVIDIA, pe AMD, sau deloc deocamdată. Apoi K10.

---

## 10. Întrebări de pus AI-ului de coding (auditul v0.2)

1. Confirmă că I1–I4 sunt suficiente și minime; ce lipsește pentru ca backend-ul GPU să nu ceară schimbări în runtime când apare?
2. Propune formatul greutăților (antet, tipuri, aliniere) și testul de egalitate PyTorch ↔ Rust.
3. Estimează K2-SMP și K6-CPU în ore, cu riscuri.
4. Verifică §6 cu surse: firmware semnat pe Turing+/Ampere; licența GSP; ce documentează modulele MIT ale NVIDIA și ce nu.
5. Pentru AMD Renoir: pașii exacți de nivel 1–3 după documentația publică, cu registrele citite/scrise și cum se verifică fiecare.
6. Spune unde v0.2 e încă naivă.

---

## Discuție
- 2026-10-23 02:15 `kronos` (supraveghetorul): cifrele despre Kronos din §1.2 și §5 se potrivesc cu ce știm (W2 ~98 M, antrenare pe
  Windows + PyTorch, verificatorul S16). Pentru K6-CPU, partea Kronos ar fi mică și în granițele noastre (o unealtă de export al
  greutăților în `unelte/`, cu test; examenele există deja în JSON) — o facem doar după „da”-ul lui Adrian. Modelul de comparat: #415
  (baseline-ul notat de verificator). Antrenarea rămâne pe workstation; orice fereastră pe placa Kronos pentru K0/C-11 doar cu Adrian.
