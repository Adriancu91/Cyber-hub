# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 01:35 (ora României) · **de:** sesiunea OS programată (23:40)

## Acum
- **Claude e în OS (Faza 6, pașii 2–5 din C-3):** `fetch https://` merge cu site-uri adevărate (117 rădăcini de încredere
  din lista publică Mozilla; verificat în CI cu api.anthropic.com, github.com, google, wikipedia ș.a.). Comanda **`claude`**
  întreabă Claude din terminal; aplicația **„claude-app”** din meniul Start e un chat în fereastră; Claude poate **citi,
  lista, scrie fișiere și rula comenzi** — scrierea și rularea doar după ce apeși **„Da”** în caseta de pe ecran.
- Toate se testează automat față de o imitație a API-ului (fără cheie reală). Pe laptop au nevoie de cheie și de rețea.
- **CI publică acum un Release** (`os-<număr>`, „Latest”) cu fișierele stick-ului și sumele lor — nu mai cauți în Actions.
- Sesiunea manuală (C-4) a reparat recepția Realtek și montarea stick-urilor din Windows; codul celor două sesiuni e unit.
- 45 de scenarii automate trec (+1 care rulează doar în CI, cu internet); CI verde.

## Urmează
- P6-08: comanda „Actualizează” (descarcă ultimul Release și rescrie stick-ul).
- P6-09: trimitere pe GitHub din OS. P6-10: testul mare pe laptop.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/` (acum și ECDSA P-384), `tls/` (TLS 1.3, rădăcini Mozilla), `json/`
  (cititor/scriitor JSON verificat față de Python), `rtl8168/`.
- Un client minimal pentru API-ul Claude (`user/src/claude_api.rs`) și o imitație a API-ului pentru teste
  (`tools/claude-test-server.py`, cu unelte).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 3 (imaginea din ultimul Release `os-…` sau din CI-ul verde), dintr-o singură pornire, cablul băgat:**
  1. Copiezi fișierele noi pe stick (îl poți lăsa formatat din Windows), Secure Boot oprit, pornești de pe stick.
  2. Aștepți ~30 de secunde pe desktop (rețeaua încearcă singură), apoi **Esc** → consola `cyber>`.
  3. `log rtl` → **poză** (registrele plăcii de rețea — de aici văd ce nu merge, dacă tot nu merge).
  4. `net` → **poză** (linia „legatura: …” și „primire: …”).
  5. `ping 1.1.1.1` → poză; `host github.com` → poză.
  6. `ls /usb` → poză; dacă scrie „nu exista”: `hw` → poză (rândul `/usb:` spune motivul) și `log usb` → poză.
  7. **Doar dacă rețeaua merge:** `fetch https://example.com/` → poză (prima pagină HTTPS adevărată pe laptop).
- **Pentru Claude pe laptop (când rețeaua merge):** pe stick, un fișier **`claude.key`** cu cheia ta API Claude pe un singur
  rând (ideal o cheie cu limită mică de cheltuieli). Apoi `claude Salut` în consolă, sau „claude-app” din meniul Start.
  Cheia nu ajunge niciodată în repo sau în hub și nu se afișează pe ecran.
- **De decis (pentru P6-08, nu urgent):** depozitul `cyber-universe` e **privat**, deci OS-ul poate descărca actualizările doar
  cu un token GitHub. Variante: (a) un token „fine-grained”, doar citire + scriere pe acest depozit, în `github.token` pe stick
  (servește și la P6-09) — recomandarea mea; (b) faci depozitul public și actualizarea merge fără token.
- B-003 / P5-07 (suita ca modul): mai târziu.
