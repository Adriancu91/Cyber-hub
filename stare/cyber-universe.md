# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 19:00 (ora României) · **de:** sesiunea OS programată (17:55) — C-9 făcută (P6-10e), Release `os-144`

## Acum
- **C-9 (după testul 6) e gata, CI verde, Release `os-144`:**
  - **Placa de pe laptop e RTL8168GU/8111GU** (numărul `50800000`, după lista publică din FreeBSD), nu 8168H cum credeam.
  - **Pornirea la rece, ca variantă** (pornirea obișnuită rămâne exact ca în os-125, regula „o schimbare pe Release”):
    `rtl porneste rece` face pașii pe care driverele FreeBSD și SerenityOS îi fac și noi nu-i făceam: preia placa de la firmware
    (`mcu`), trezește PHY-ul (`phy`), setează registrul „C+ Command” (`cplus`), scrie configurarea înainte de pornire (`ordine`).
    Fiecare pas se poate da și singur. Fiecare registru: citit → un bit → scris, cu valorile în `log rtl` („pas 1 … pas 18”).
  - **P6-10f (pachetele 2+ citite ca zero):** se diagnostichează la cald cu `log rx` (există din os-138). Golirea cache-ului
    (`rtl porneste cache`) n-a fost încercată niciodată la cald → o încercăm la testul 7.
- 32 de teste ale driverului (un model de placă „rece”), 50 de scenarii automate.

## Urmează
- Testul 7 pe laptop (lista mai jos). Dacă `rece` merge → devine pornirea obișnuită în versiunea următoare → apoi C-7 (bucla automată).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3, rădăcini Mozilla), `json/` (și base64), `rtl8168/`.
- Clienți minimali: API-ul Claude, GitHub Releases + contents, cu imitații pentru teste în `tools/`.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 7 (Release `os-144`), cablul de rețea băgat.** Copiezi pe stick fișierele din Release (ca la testul 6, inclusiv `cyber.rw`).
  **(R) La rece — oprit complet, pornit direct de pe stick (fără F12):** aștepți ~1 minut, **Esc** → `cyber>`.
  1. `net` → poză (așteptat 0 / 0, ca la testul 6).
  2. `rtl porneste rece` → aștepți ~30 s → `net` → poză; `log rtl 60` → poză (pot fi două ecrane: pașii 1–18 și registrele).
  3. Dacă „trimise” > 0 și „primite” > 0: `ping 1.1.1.1` → poză. (Opțional, dacă ai timp: oprit complet, pornit direct, încearcă pe rând
     `rtl porneste cplus`, apoi `rtl porneste cplus ordine` → `net` după fiecare — ca să aflăm pasul minim.)
  **(C) La cald — oprit complet, pornit cu F12 → stick:** **Esc** → `cyber>`.
  4. `net` → poză; `log rx` → poză; `ping 1.1.1.1` → poză.
  5. `rtl porneste cache` → aștepți ~30 s → `net` → poză; `log rx` → poză.
- `github.token` / `claude.key`: încă nu — după ce merge rețeaua.
- B-003 / P5-07 (suita ca modul): mai târziu.
