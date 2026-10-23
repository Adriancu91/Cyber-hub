# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-24 00:10 (ora României) · **de:** sesiunea OS programată (23:35) — C-17 gata, Release os-190

## Acum
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
- Pentru `cyber-gpu`: bibliotecile lor rulează acum în nucleu (adaptor doar-citire) și în programe (`gpu-compute`); scenarii CI `gpu`, `gpu-sim`, `kronos-calcul`.
- Pentru Kronos: SSE/AVX/AVX2 în programe, fire pe toate nucleele, `mem_map` (GiB), fire multiple într-un program, `/bin/kronos-calcul` ca punct de pornire.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: tag-ul lor `stabil-2026-10-23` nu apare încă pe GitHub (probabil aceeași limită 403); OS-ul folosește direct commit-ul `41e44ba`, deci nu blochează.

## Blocaje / nevoie de Adrian
- **Tag-ul `stabil-2026-10-23` (2 minute, când ai timp):** pe GitHub → cyber-universe → Releases → „Draft a new release” → „Choose a tag” →
  scrie `stabil-2026-10-23` → „Create new tag” → Target: ramura `revenire/stabil-2026-10-23` → bifează „Set as a pre-release” → Publish.
  Până atunci punctul de revenire e ramura + os-187 (suficient).
- Totul de mai jos e pentru când se întoarce (Release-ul de folosit: `os-190` sau mai nou):
- **Fereastra a doua pe workstation** (~30 min, Kronos oprit; Secure Boot oprit, apoi repus pe Enabled): stick → F12 → **Esc** → `cyber>`,
  câte o poză după: `lspci` (`10de:2482` la `b3:00.0`), `gpu identifica` (**nou:** rândurile „cyber-gpu 41e44ba nvidia-ga104: GeForce RTX 3070 Ti”,
  BOOT_0/BOOT_42, „a refuzat 0 scrieri”), `log gpu 40`, `log pci 40`, `hw`, `lsusb`, `log usb 60`, `net`, `log e1000 40`, `cpu`, `cpu porneste`,
  `cpu`, **nou:** `run kronos-calcul` (timpii reali pe 1 și pe toate nucleele), la final `reboot`. Nimic nu scrie în placa video.
- **Testul 8 pe laptop** (rețeaua Realtek neschimbată față de os-155): pașii (C) și (R) de data trecută; în plus `run kronos-calcul` → poză.
- `github.token`: doar pentru `gh-trimite`, mai târziu. `claude.key`: după ce trece (R). B-003 / P5-07: mai târziu.
