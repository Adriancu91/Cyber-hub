# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 10:40 (ora României) · **de:** sesiunea OS programată (09:25) — comanda C-5 gata

## Acum
- **C-5 (după testul 3) e gata, CI verde, Release `os-123`:**
  - **Rețeaua Realtek:** placa primea exact 16 pachete (cât încăpea în „coada” de primire), apoi se oprea. Coada are acum 256 de
    locuri, iar dacă placa se blochează totuși, OS-ul îi repornește singur primirea. `net` arată acum și starea cozii, de câte ori
    s-a blocat, repornirile, câte răspunsuri DHCP au venit și ce tip aveau primele 8 pachete.
  - **Stick-ul:** OS-ul aștepta răspunsul stick-ului doar câteva milisecunde (în emulator e instant, pe un stick real nu).
    Acum așteaptă până la 5 secunde, reîncearcă, iar fiecare pas apare în `log usb`, cu motivul exact dacă pică.
- 49 de scenarii automate trec (nou: stick USB 2 pe port USB 2), +1 doar în CI, cu internet.

## Urmează
- Testul 4 pe laptop (lista mai jos) → din poze: reparații, apoi P6-10 (închiderea Fazei 6) și P3-10.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3, rădăcini Mozilla), `json/` (și base64), `rtl8168/`.
- Clienți minimali: API-ul Claude, GitHub Releases + contents, cu imitații pentru teste în `tools/`.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 4, dintr-o singură pornire, cablul de rețea băgat** (Release **`os-123`** sau mai nou):
  1. Copiezi pe stick fișierele din Release (ca la testul 3, inclusiv `cyber.rw`); Secure Boot oprit, pornești de pe stick.
  2. Aștepți ~1 minut pe desktop, apoi **Esc** → consola `cyber>`.
  3. `net` → poză (acum are 2 rânduri noi: „inel RX 256 …” și „primele cadre …”); `log rtl` → poză.
  4. `ping 1.1.1.1` → poză; `host github.com` → poză.
  5. `log usb` → poză (dacă nu încape: `log usb 20`); `hw` → poză; `ls /usb` → poză.
  6. Peste ~1 minut, încă o dată `net` → poză (să vedem dacă „primite” crește).
  7. Doar dacă rețeaua merge: `fetch https://example.com/` → poză.
- `claude.key` și `github.token` NU încă: fără `/usb` n-au unde sta (vin la testul următor).
- B-003 / P5-07 (suita ca modul): mai târziu.
