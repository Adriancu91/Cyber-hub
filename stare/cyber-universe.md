# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 11:50 (ora României) · **de:** sesiunea OS programată (10:05) — C-13 punctele 1–3 gata, Release `os-169`

## Acum
- **P6-13 (Release `os-166`):** OS-ul caută dispozitive PCI pe **toate** magistralele-rădăcină, nu doar pe cea de la 0. Pe workstation
  placa RTX 3070 Ti (la `b3`) ar trebui să apară acum în `lspci`. Test nou în QEMU cu o rădăcină în plus (pică pe codul vechi, trece acum).
- **P6-14 (Release `os-167`):** USB vede și dispozitivele din spatele hub-urilor (ex. `port 26.3` = portul 3 al hub-ului de pe portul 26).
  QEMU are doar hub-uri lente; hub-urile rapide și USB 3 ale workstation-ului se verifică doar acolo.
- **P6-15 (Release `os-169`):** `/usb` = stick-ul cu sistemul (cel cu `cyber.rw` și `VERSIUNE`); cititorul de carduri gol e sărit.
- **Observațiile Cyber-GPU** judecate (C-13 p.5): `docs/research/OBSERVATII-CYBER-GPU.md` din repo-ul OS — nicio schimbare de cod acum.
- 54 de scenarii automate trecute (+1 sărit fără internet). CI verde pe `os-169`. Un CI roșu (testul `desktop`, ordine întâmplătoare
  a două rânduri, veche) reparat în test.
- O altă sesiune OS lucrează acum la **P6-17** (`reboot` pe workstation, C-13 p.5b); apoi C-14 (P6-16 I219, K6-CPU).

## Urmează
- P6-17 (în lucru, altă sesiune), apoi C-14: P6-16 (rețeaua I219), K6-CPU pașii 1–4. C-7 și C-11 așteaptă întoarcerea lui Adrian.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`.
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0, doar citire); acum vede plăcile de pe orice magistrală-rădăcină.

## De ce are nevoie de la ceilalți
- Nimic nou (observațiile `cyber-gpu` au venit prin hub, mulțumim).

## Blocaje / nevoie de Adrian (când se întoarce — nimic urgent)
- **Fereastra a doua pe workstation** (Release `os-169` sau mai nou, ~30 min, Kronos oprit; Secure Boot oprit, apoi repus pe Enabled):
  stick din Release → F12 → **Esc** → `cyber>`, câte o poză după: `lspci` (trebuie să apară `10de:2482` la `b3:00.0`), `gpu identifica`,
  `gpu plan`, `log gpu 40`, `log pci 40`, `hw`, `lsusb` (stick-ul ADATA trebuie să apară ca `port X.Y`), `log usb 60`.
  Nimic nu scrie în placa video.
- **Testul 8 pe laptop** (tot `os-169`; rețeaua e neschimbată față de os-155), cablul la laptopul cu Windows (ICS pornit):
  **(C) La cald — F12 → stick:** **Esc** → `cyber>`, nicio comandă `rtl`. 1. ~30 s → `net` → poză. 2. `log rtl 20` → poză.
  3. Cu adresă: `fetch https://example.com/` → poză; fără adresă: `log rx` → poză, apoi `rtl porneste pagini` → ~30 s → `net` → poză.
  **(R) La rece — pornit direct de pe stick:** **Esc** → `cyber>`. 4. `net` → poză. 5. `rtl porneste rece` → ~30 s → `net` → poză; `log rtl 60` → poză.
  În plus, pe laptop: `lspci` și `lsusb` ca înainte (verificăm că P6-13/P6-14 nu schimbă nimic acolo).
- `github.token` / `claude.key`: încă nu — după ce trece (R). B-003 / P5-07: mai târziu.
