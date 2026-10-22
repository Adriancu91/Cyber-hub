# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 05:45 (ora României) · **de:** sesiunea OS programată (05:40) — fără schimbări de cod; așteaptă testul 3

## Acum
- **Toată Faza 6 e scrisă și testată în emulator** (C-3, pașii 1–5): rețea Realtek, HTTPS cu site-uri reale, Claude în OS
  (comanda `claude`, chatul „claude-app” cu unelte confirmate pe ecran), Release automat în CI.
- **Nou: auto-actualizarea** — în Setări, butonul **„Actualizeaza”** (sau `run actualizeaza` în terminal) descarcă ultimul
  Release de pe GitHub, verifică fiecare fișier cu sumele lui și abia apoi le pune pe stick; dacă ceva pică, stick-ul rămâne
  cum era. Dacă versiunea e aceeași, nu face nimic.
- **Nou: trimitere pe GitHub din OS** — `run gh-trimite <fișier> <proprietar/depozit> <cale>`; și Claude o poate cere din
  chat (unealta `github_push`), tot cu „Da” pe ecran.
- 47 de scenarii automate trec (+1 doar în CI, cu internet). CI verde pe P6-08.

## Urmează
- P6-10: testul mare pe laptop (cu Adrian) — apoi reparațiile din poze și închiderea Fazei 6 și a Fazei 3 (P3-10).
- Nu mai e nicio sarcină care să se poată face fără testul pe laptop.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3, rădăcini Mozilla), `json/` (acum și base64), `rtl8168/`.
- Clienți minimali: API-ul Claude (`user/src/claude_api.rs`), GitHub Releases + contents (`user/src/bin/actualizeaza.rs`,
  `gh-trimite.rs`), cu imitații pentru teste în `tools/`.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 3, dintr-o singură pornire, cablul de rețea băgat** (imaginea din ultimul Release `os-…`):
  1. Copiezi pe stick fișierele noi din Release — **inclusiv fișierul nou `cyber.rw`** în rădăcina stick-ului (lângă `EFI` și
     `boot`); Secure Boot oprit, pornești de pe stick.
  2. Aștepți ~30 s pe desktop, apoi **Esc** → consola `cyber>`.
  3. `log rtl` → poză; `net` → poză; `ping 1.1.1.1` → poză; `host github.com` → poză.
  4. `ls /usb` → poză (dacă scrie „nu exista”: `hw` → poză și `log usb` → poză).
  5. **Doar dacă rețeaua merge:** `fetch https://example.com/` → poză.
- **Pentru pașii cu internet (când rețeaua merge), pe stick, în rădăcină:**
  - `claude.key` — cheia ta API Claude pe un rând (ideal cu limită mică de cheltuieli) → apoi `run claude Salut`.
  - `github.token` — un token GitHub „fine-grained”: *Repository access* doar `cyber-universe`, *Permissions → Contents*:
    **Read and write** (citire pentru actualizare, scriere pentru trimitere). Pașii exacți: `docs/USB.md`, secțiunea 7.
    → apoi în Setări **Actualizeaza** (poză cu mesajul final) și `run gh-trimite /usb/cyber.rw Adriancu91/cyber-universe test/din-os.txt`
    (poză; apare un commit nou în depozit, în dosarul `test/`).
  - Cheia și tokenul nu se afișează pe ecran și nu ajung niciodată în repo sau în hub.
- Alternativă la token pentru actualizare: faci depozitul `cyber-universe` public (atunci actualizarea merge fără token;
  pentru `gh-trimite` tot e nevoie de token).
- B-003 / P5-07 (suita ca modul): mai târziu.
