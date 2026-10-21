# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-21 20:45 (ora României) · **de:** sesiunea programată a OS-ului (20:41), cu acces la hub

## Acum
- Fazele 1, 2 și 4 închise; Faza 3 gata în emulator (lipsește doar testul pe un calculator real).
- Interfață grafică: desktop „Cyber Universe” care pornește singur, ferestre, aplicații (Terminal, Fișiere, Editor,
  Monitor, Setări, Module, Rețea), tastatură românească, module instalabile din interfață.
- Rețea (Faza 5): DHCP, DNS, TCP sigur, `ping`, `host`, `http`, programele `fetch` și `udp`, aplicația **Rețea**.
- **Nou: HTTPS cu criptografie scrisă integral de noi** (după „da”-ul lui Adrian, D-011): `fetch https://nume/cale`.
  Certificatul site-ului e verificat (lanțul până la o rădăcină de încredere, numele, data); unul greșit e refuzat.
  Testat față de un server OpenSSL real (pe gazdă și din OS-ul pornit în emulator: 18 KB în ~1,3 s).
  Neauditat de specialiști: nu pentru date sensibile până la o verificare separată.
- 41 de scenarii de test automate trec (nou: `https`); CI verde, testul de stres zilnic verde.

## Urmează
- **Oprit, conform deciziei tale din 21 oct, 10:05:** nu se închide Faza 5, nu pornește Faza 6. Sesiunile OS doar verifică
  hub-ul și CI-ul până apar rezultatele testului pe stick sau o comandă nouă în `COMENZI.md`.
- P3-09 / P3-10: testul pe un calculator real, când Adrian trimite pozele.
- P5-07 / P5-08: suita office și Kronos ca module în OS — după ce suita își atinge ținta.

## Ce oferă proiectul celorlalți
- Biblioteca `crypto/` (Rust, fără dependențe, MIT): SHA-2, HMAC, HKDF, X25519, ChaCha20-Poly1305, RSA, ECDSA P-256, X.509.
- Biblioteca `tls/`: client TLS 1.3 fără heap, peste orice conexiune.
- Infrastructura de test pe scenarii (`tests/scenarios.txt` + `tools/test.sh`, cu servere de test pornite automat).
- Formatul comun de modul (`standarde/modul-v0.md`) e folosit în `modules/` și `apps/`.

## De ce are nevoie de la ceilalți
- Nimic acum. (Testul pe stick se face pe alt calculator, nu pe ThinkPad-ul suitei.)

## Blocaje / nevoie de Adrian
- **B-001 / P3-09 (singurul lucru care repornește OS-ul):** testul pe un calculator real (nu ThinkPad-ul suitei) — scrii
  imaginea pe stick (pașii în `docs/USB.md` din repo-ul OS; imaginea e artefactul `stick-usb` din GitHub Actions), pornești
  calculatorul de pe stick și trimiți poze cu ecranul. P3-10 așteaptă după el.
- Opțional: o comandă nouă în `COMENZI.md` (ex. rădăcinile reale de încredere, ca HTTPS să meargă cu site-uri adevărate).
- **B-003 / P5-07:** suita office ca modul — mai târziu, după ce suita e gata.
