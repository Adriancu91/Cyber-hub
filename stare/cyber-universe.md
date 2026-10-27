# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-27 14:47 (ora României) · **de:** sesiunea OS programată — nimic nou (fără comenzi noi); ultimul Release **`os-191`**

## Acum
- **C-19 gata (P6-21): `gpu gfw` și `gpu vbios`, doar citire.** Cyber-GPU fixat pe commit-ul lor `dac2e32` (ramura `g0-g2-fundatie`).
  `gpu gfw` = „a terminat placa pornirea?” (așteaptă max 4 s, gata = 0xff); `gpu vbios` = lista imaginilor din VBIOS (PCI-AT, EFI, FWSEC),
  tabela BIT cu jetonul 0x70. Primii 4 MiB din registrele plăcii se citesc pagină cu pagină **fără drept de scriere**; orice scriere cerută de
  bibliotecă e refuzată și numărată („0 scrieri in placa”). Testat doar în **SIMULARE** (`--sim`, în CI) și în QEMU; nimic pe placa reală.
- **C-22 gata (P6-22, P6-23):**
  - **„Cutia neagră”:** comanda `raport` scrie pe stick `/usb/raport/<data>-<nr>.txt` cu tot ce trebuie (versiune, `hw`, `lspci`, `net`,
    jurnalele rețea/USB/PCI/GPU, tot jurnalul). Se scrie și **singur** când apare o eroare nouă în jurnal (max 3 pe pornire). Cheile și
    tokenurile apar ca `[ascuns]`. La o cădere totală (panică) nu se scrie — ar putea strica stick-ul.
  - **Permisiuni pe program:** un program poate promite ce apeluri folosește și ce căi vede, apoi nu le mai poate lărgi. `claude.key` și
    `github.token` se văd doar de programele care le cer (Claude, `gh-trimite`, `actualizeaza`), iar acestea renunță la ele imediat după citire;
    `cat` nu le mai afișează. Testat în QEMU (scenariul `drepturi`).
- CI run 191 verde → **Release `os-191`**. os-187 rămâne punctul de revenire.
- **C-17 gata: Release-urile testate pe hardware nu se mai șterg.** Lista e în `docs/RELEASES_PASTRATE.md` din repo-ul OS
  (os-120, os-125, os-136, os-138, os-150, os-161 + punctul de revenire os-187); curățarea automată sare peste ele.
  **os-150 și os-161 există din nou** la Releases, cu exact fișierele de atunci (sumele verificate), marcate „(păstrat)”, nu „latest”.
  Release nou: **`os-190`** (același OS ca os-189, doar regula nouă în CI).
- **C-16 gata: OS-ul folosește bibliotecile Cyber-GPU** (fixate pe commit-ul lor `41e44ba`), testate automat. **Release nou: `os-189`.**
  - `gpu identifica` trece placa prin `nvidia-ga104` (biblioteca Cyber-GPU); orice scriere cerută de bibliotecă e **refuzată și numărată**
    (rândul final arată „a refuzat 0 scrieri”). În QEMU: „nicio placa NVIDIA”, cum trebuie.
  - **SIMULARE** (doar în testele automate, nu pe stick): `gpu identifica --sim` pe modelul plăcii de pe workstation — 10de:2482 la b3:00.0,
    BAR0 16 MiB, BAR1 256 MiB, BAR3 32 MiB, cipul GA104. Asta nu dovedește nimic despre placa reală.
  - `/bin/kronos-calcul` (program nou): calculul lui Kronos (un bloc de tip Kronos + matmul) pe toate nucleele și cu SSE/AVX, comparat cu
    referința bibliotecii: identic bit cu bit pe 4 nuclee; cu AVX2+FMA eroarea maximă 0,0000038 (toleranța 0,00001). Timpii din QEMU nu contează.
- Lucrat pe ramura `wip/integrare-gpu`, unită în `main` doar după CI verde (run 188); `main` verde și după unire (run 189).
- **Punct de revenire:** ramura `revenire/stabil-2026-10-23` (commit `9f67d7b`) + **Release `os-187` păstrat pentru totdeauna** (= aceeași stare).
  Tag-ul `stabil-2026-10-23` există doar local: sesiunea cloud nu are voie să urce tag-uri (eroare 403). Copia offline (bundle) trimisă lui Adrian.

## Urmează
- Coada OS-ului nu are nimic de făcut fără hardware. Când se întoarce Adrian: listele de mai jos (cu `os-190`), apoi C-7, C-11.

Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/` (Intel 8254x/82574/I219).
- Pentru `cyber-gpu`: bibliotecile lor (fixate pe `dac2e32`) rulează în nucleu (adaptoare doar-citire, inclusiv fereastra de 4 MiB pentru I2/I3) și în programe (`gpu-compute`); scenarii CI `gpu`, `gpu-sim`, `kronos-calcul`.
- Pentru Kronos: SSE/AVX/AVX2 în programe, fire pe toate nucleele, `mem_map` (GiB), fire multiple într-un program, `/bin/kronos-calcul` ca punct de pornire.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: o ramură `main` (sau un tag) ar fi mai clar de fixat decât un commit de pe `g0-g2-fundatie`; nu blochează (OS-ul folosește `dac2e32`).
  Sesiunea OS nu vede CI-ul lor (repo-ul nu e în lista sesiunii) — am verificat doar că se compilează și merge în testele OS-ului.

## Blocaje / nevoie de Adrian
- **Tag-ul `stabil-2026-10-23` (2 minute, când ai timp):** pe GitHub → cyber-universe → Releases → „Draft a new release” → „Choose a tag” →
  scrie `stabil-2026-10-23` → „Create new tag” → Target: ramura `revenire/stabil-2026-10-23` → bifează „Set as a pre-release” → Publish.
  Până atunci punctul de revenire e ramura + os-187 (suficient).
- Totul de mai jos e pentru când se întoarce (Release-ul de folosit: `os-191` sau mai nou):
- **Release de folosit acum: `os-191`.** Pe orice test: la final scrie **`raport`** → fișierul din `raport/` de pe stick înlocuiește pozele
  (îl trimiți sau îl pui în hub; cheile sunt ascunse).
- **Fereastra a doua pe workstation** (~30 min, Kronos oprit; Secure Boot oprit, apoi repus pe Enabled): stick → F12 → **Esc** → `cyber>`,
  **nou (C-19):** `gpu gfw` (așteptat: „GFW gata (progres 0xff)”, sub 4 s, „0 scrieri”) și `gpu vbios` (așteptat: PCI-AT, EFI, cel puțin o FWSEC,
  „jetonul 0x70: da”, „complet: da”, „0 scrieri”); apoi `raport`. Restul ca înainte, câte o poză după:
  `lspci` (`10de:2482` la `b3:00.0`), `gpu identifica` (rândurile „cyber-gpu dac2e32 nvidia-ga104: GeForce RTX 3070 Ti”,
  BOOT_0/BOOT_42, „a refuzat 0 scrieri”), `log gpu 40`, `log pci 40`, `hw`, `lsusb`, `log usb 60`, `net`, `log e1000 40`, `cpu`, `cpu porneste`,
  `cpu`, **nou:** `run kronos-calcul` (timpii reali pe 1 și pe toate nucleele), la final `reboot`. Nimic nu scrie în placa video.
- **Testul 8 pe laptop** (rețeaua Realtek neschimbată față de os-155): pașii (C) și (R) de data trecută; în plus `run kronos-calcul` → poză.
- `github.token`: doar pentru `gh-trimite`, mai târziu. `claude.key`: după ce trece (R). B-003 / P5-07: mai târziu.
