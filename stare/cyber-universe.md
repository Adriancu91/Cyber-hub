# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 00:05 (ora României) · **de:** sesiunea OS programată (23:42) — fără lucru nou; Release `os-155` așteaptă testul 8 (CI verde)

## Acum
- **P6-10g gata (Release `os-155`, CI verde):** la pornire, inelele și bufferele plăcii Realtek stau acum într-un **bloc separat, între
  16 MiB și 4 GB** (ca la repornirea care a mers la testul 7), nu în memoria de jos (3db000). Golirea cache-ului rămâne deocamdată.
  `rtl porneste pagini` = alocarea veche, pentru comparație.
- **Paza memoriei:** paginile în care scrie o placă nu mai pot fi date altcuiva (încercarea apare în jurnal, cu locul din cod).
  Testul din QEMU: nicio pagină dată de două ori. `net` arată „paza memoriei: ok”.
- **Diagnostic nou (nu schimbă placa):** bufferele se umplu cu `A5` în loc de zero. Dacă un cadru rău începe cu `a5a5…` → placa nu a
  scris; dacă e `0000…` → altcineva a șters pagina. `net` numără „necitite de placa (model A5)”.
- **P6-10h gata (doar `rtl porneste rece`):** accesul OCP e verificat înainte de scriere (citirea ta `0001` arată că OCP răspunde);
  bitul 15 din E8DE e o comandă pe care cipul o șterge singur, iar C+ bit 3 există doar la 8169 — deci pașii 7, 9, 12 nu erau defecte.
  La rece rămâne un singur semn real: **FIFO-ul de primire nu se golește** (pasul 3).
- Rețeaua de test prin partajarea Windows (ICS) e notată în `docs/HARDWARE.md` și `docs/USB.md`.
- 39 de teste ale driverului, 50 de scenarii automate (49 trecute + 1 sărit fără internet).

## Urmează
- Testul 8 (lista mai jos). Dacă (C) ia adresă singur → P6-10g confirmată; apoi, ca schimbare separată, scoatem golirea cache-ului.
- La rece: după (R), sarcina pentru FIFO (pasul 3) sau pentru registrele reviziei GU.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3, rădăcini Mozilla), `json/` (și base64), `rtl8168/`.
- Clienți minimali: API-ul Claude, GitHub Releases + contents, cu imitații pentru teste în `tools/`.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 8 (Release `os-155`), cablul la laptopul cu Windows (partajarea ICS pornită).** Copiezi pe stick fișierele din Release
  (ca la testul 7, inclusiv `cyber.rw`).
  **(C) La cald — oprit complet, pornit cu F12 → stick:** **Esc** → `cyber>`. **Nu scrii nicio comandă `rtl`.**
  1. Aștepți ~30 s → `net` → poză. Așteptat: o adresă 192.168.137.x, „cadre cu tip 0000: 0”, „necitite de placa (model A5): 0”,
     „paza memoriei: ok”.
  2. `log rtl 20` → poză (rândul „memorie DMA: un bloc …”).
  3. Dacă are adresă: `fetch https://example.com/` → poză. Dacă NU are adresă: `log rx` → poză (primii octeți: `a5…` sau `00…`),
     apoi `rtl porneste pagini` → ~30 s → `net` → poză.
  **(R) La rece — oprit complet, pornit direct de pe stick (fără F12):** **Esc** → `cyber>`.
  4. `net` → poză. 5. `rtl porneste rece` → ~30 s → `net` → poză; `log rtl 60` → poză (pașii; acum cu „OCP proba”).
- `github.token` / `claude.key`: încă nu — după ce trece (R).
- B-003 / P5-07 (suita ca modul): mai târziu.
