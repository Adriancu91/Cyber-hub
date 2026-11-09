# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-09 02:50 (ora României) · **de:** sesiunea OS programată (02:40) — oprire scurtă: nicio comandă nouă, nicio sarcină liberă până la fereastra de luni. Cod neschimbat. Release de testat: **`os-275`** (CI verde, run 42405596803)

## Acum
- **P6-67 GATA (CI mai rapid):** testele automate rulau ~55 min din limita de 60 a GitHub; acum rulează în trei părți în același timp (97/97 scenarii, ~30–35 min). Release nou **`os-275`** (sistemul e același ca `os-273`).
- **C-87 (partea OS) → P6-64, P6-65, P6-66 GATA** (testate în QEMU / SIMULARE, nimic încă pe hardware):
  - **Comenzi din hub (P6-64):** Adrian scrie în `integrare/cyber-universe/os-comenzi.md` rânduri `- [ ] K-1: test tot`; în OS `hub ruleaza` le ia,
    rulează **doar lista albă** (citiri, `test tot`, `raport`, `trimite`, `run kronos --control/--profil`), fiecare o singură dată, și trimite raportul
    în `rezultate/os-automat/`. `gpu lant`, `--gpu`, `--scrie`, `reboot`, `DA`, ștergeri, actualizări: refuzate mereu. Pe stick `hub/la-pornire` = la fiecare pornire.
  - **Conversație cu Kronos (P6-65):** `run kronos --conversatie` — #513 încărcat o dată, întrebări tastate una după alta, `\` = continui rândul, `gata` = sfârșit.
  - **`kronos --gpu` (P6-66):** cyber-gpu `34a9793`; generarea continuă a cyber-gpu (oprire la prima eroare, viteza din ceasul plăcii, memoria VRAM verificată
    înainte), apoi același text pe procesor: „comparatie: placa … / procesor … simboluri/s; simbolurile IDENTICE”. La orice eroare: pe procesor.
- CI: reparată lipsa de spațiu pe disc a mașinii GitHub (toate cele 97 de scenarii treceau).

## Urmează
- Luni, după fereastră: citim jurnalul (`verifica_jurnal_lant` la cyber-gpu, analiza la noi) și reparăm primul pas care se oprește.
- Propunere (doar cu „da”): recuperarea plăcii fără repornire (`recover` din cyber-gpu) legată în `gpu lant`.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14 și `kronos --gpu` cu comparația de viteză, pe stick-ul de test (I11–I14 doar în SIMULARE); jurnale + rapoarte trimise singure în hub (cu token).
- Comenzi trimise OS-ului din hub (`os-comenzi.md`), `hub`, `test tot`, `ora`, git pe ramuri `os/…`, `web`, `files`, `kronos --conversatie`.
- Bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; decodorul `png.rs`.

## De ce are nevoie de la ceilalți
- **`kronos`:** doar Release-ul `kronos-kgr1-513` (luni, cu Adrian — C-86 pct. 4).
- **`cyber-gpu`:** nimic urgent; `34a9793` e în OS. Pentru modelul de 24 de straturi, zona de comenzi de 32 KiB (o facem când vine modelul).

## Blocaje / nevoie de Adrian

### LISTA PENTRU FEREASTRA DE LUNI 9 NOV (workstation, P6-63) — Release **`os-275`**
Ce e nou față de 5 nov: lanțul merge acum **I6 → I7 → I8 → golden → I9 → I10 → I11 → I12 → I13 → I14** (I8–I14 n-au rulat niciodată pe placă;
în teste trec doar în SIMULARE). Orice oprire curată (un pas „ESUAT”, Bus Master pus la loc, jurnal scris) e un rezultat bun.

**Înainte (în Windows, ~10 min):**
1. Din Release-ul **`os-275`** (github.com/Adriancu91/cyber-universe → Releases) iei `cyber-universe-gpu-scrie-usb.img` și îl scrii cu Rufus pe
   **stick-ul de test** (ca pe 5 nov; dacă îl refaci ca „TESTGPU” FAT32, copiază și `github.token` în rădăcina lui — atunci jurnalul pleacă singur în hub).
   Modelul mic de control (`kronos\mic_q8_0.kgr`) e deja în imagine.
2. Pe **stick-ul normal** (cel cu `firmware\nvidia\ga102\gsp\`, cele 4 fișiere 570.144) pui în dosarul `kronos\` modelul **#513**:
   `kronos_513_q8_0.kgr` (105,7 MiB) + `kronos_513_q8_0.kgr.sha256`, din `C:\Kronos\cyberspace\lucru\export\` (sau din Release-ul `kronos-kgr1-513`, dacă îl faci).
   Pe stick-ul de test nu încape (are ~62 MB) — de aceea stă pe al doilea stick, pe care OS-ul îl vede la `/usb2`.
3. **Oprire completă**: calculatorul oprit, cablul scos **30 s** (placa trebuie să pornească rece).

**Încercarea 1 — lanțul (amândouă stick-urile băgate, pornești de pe cel de test cu F8):**
4. Pe ecran trebuie să apară `fs: /usb2: al doilea stick, cu dosarul firmware/nvidia/ga102/gsp (doar citire)`. Dacă nu: poză, apoi `gpu firmware` → poză.
5. `gpu lant` → citești avertismentul → scrii `DA` (litere mari) + Enter. Durează 1–3 minute; **poză la tot ce scrie** (derulează dacă e mult).
   La final, rândul important: `rezultat lant: toti pasii au trecut` **sau** `rezultat lant: oprit la <pas> (N scrieri)`.
6. `raport` → poză (scrie `/usb/raport/...` lângă `gpu-jurnal-NNN.txt`). Dacă ai token pe stick: `trimite`.

**Încercarea 2 — Kronos pe placă (DOAR dacă la pasul 5 scrie „toti pasii au trecut”):**
7. **Oprire completă din nou, cablul scos 30 s.** Lanțul nu se poate rula de două ori la aceeași pornire (după prima trecere placa nu mai e „rece”,
   iar `kronos --gpu` rulează tot lanțul de la capăt). Pornești iar de pe stick-ul de test, cu ambele stick-uri.
8. Tastezi exact (cu `--model`, altfel Kronos ia modelul mic de pe stick-ul de test):
   `run kronos --gpu --model /usb2/kronos/kronos_513_q8_0.kgr --n 32 Ana are mere.`
   → `DA` + Enter. **Poză** la: `i14-simbol: ...`, `kronos --gpu: ... simboluri generate pe placa`, și ultimul rând
   `kronos: comparatie: placa ... / procesor ... simboluri/s; simbolurile IDENTICE` (sau ce scrie în loc).
9. `raport` (+ `trimite` dacă ai token) → poză.

*Dacă ai timp pentru o singură pornire:* sari peste pasul 5 și faci direct pasul 8 — `kronos --gpu` rulează și el tot lanțul (un singur „DA” care face tot, C-87 pct. 4), dar pe ecran arată mai puține rânduri (detaliile rămân în `gpu-jurnal-NNN.txt`).

**Dacă se blochează ecranul:** aștepți 1 minut, apoi butonul ținut 10 s și cablul scos 30 s. Nimic nu rămâne în placă după oprirea completă.
**La sfârșit:** oprire completă → Windows. Copiezi de pe stick-ul de test (`E:\raport\`) toate fișierele `gpu-jurnal-*.txt` și `*.txt` de azi.

**Ce aduci în hub:** pozele + fișierele din `raport\` în `rezultate/2026-11-09-workstation-os275/` (sau le lași centrului de comandă să le pună).

**Ce înseamnă rezultatul:**
- `oprit la i7-booter-gsp` / `i7-citit` → ordinea nouă de la I7 (resetul GSP în RISC-V) nu e cum crede placa; jurnalul ne spune unde.
- `oprit la i8-gsp-init` → GSP-RM n-a răspuns în coadă (ca pe 5 nov); cel mai probabil loc de oprire. Jurnalul arată dacă a pornit.
- `oprit la i8e-golden` / `i9-canal-lucru` / `i10-add64` → GSP-RM merge, dar crearea canalului sau soneria de lucru nu; pas mare înainte oricum.
- `oprit la i11` … `i14-simbol` → placa rulează programe; ne mai trebuie doar potrivirea copierii/calculului.
- `toti pasii au trecut` + la Kronos `simbolurile IDENTICE` → **Kronos rulează pe placa video în OS-ul tău**, cu viteza scrisă alături de procesor.
- În toate cazurile, **după** fereastră facem noi analiza; tu nu trebuie să interpretezi nimic.

### Restul
- **Release-ul modelului #513 (luni, pe workstation, în `C:\Kronos\cyberspace`):** comanda e în `integrare/kronos/MODEL.md` (`gh release create kronos-kgr1-513 …`).
  Apoi pe stick, în dosarul `kronos`: `kronos_513_q8_0.kgr` + `kronos_513_q8_0.kgr.sha256` (sau copiate din `lucru\export\`). Fără ele OS-ul folosește #477.
- **Tokenul GitHub pe stick** (pentru rapoarte și `hub ruleaza`): GitHub → Settings → Developer settings → Fine-grained tokens → doar **`Cyber-hub`**,
  *Contents: Read and write*; salvat ca `github.token` (un rând) în rădăcina stick-ului.
- **Coada OS e goală până la fereastră:** după luni, sarcinile noi vin din rezultatele ei sau din comenzile tale în `COMENZI.md`.
- 2026-11-08 23:50 — sesiune scurtă: nicio comandă nouă, CI `os-275` verde; lista pentru luni rămâne cea de la 20:50 (mai sus).
- 2026-11-09 02:50 · sesiunea OS programată · oprire scurtă: nicio comandă nouă; aștept fereastra de luni cu `os-275` (lista de pași e mai sus) și jurnalul în `rezultate/2026-11-09-workstation-os275/`.
